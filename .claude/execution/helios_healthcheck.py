#!/usr/bin/env python3
"""
Script: helios_healthcheck.py
System: Helios/Selenia MVP
Description: Safe local healthcheck for orchestration scripts.

No external writes. No messages. No Notion/CRM/finance. Uses temp files for mutation tests.
"""
from __future__ import annotations

import json
import os
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any

WORKSPACE = Path(os.environ.get("JORGE_WORKSPACE", "${LIFEOS_ROOT}"))
CLAUDE = WORKSPACE / ".claude"
EXEC = CLAUDE / "execution"
LIFE = WORKSPACE / "Life OS"
REPORT_DIR = LIFE / "00. Inbox" / "selenia"

SCRIPTS = {
    "log_event": EXEC / "log_event.py",
    "selenia_build_report": EXEC / "selenia_build_report.py",
    "telegram_signal": EXEC / "telegram_signal.py",
    "route_task": EXEC / "route_task.py",
    "approval_item": EXEC / "approval_item.py",
}


def run(cmd: list[str], input_text: str | None = None, timeout: int = 30) -> dict[str, Any]:
    try:
        p = subprocess.run(
            cmd,
            input=input_text,
            text=True,
            capture_output=True,
            timeout=timeout,
            cwd=str(WORKSPACE),
        )
        return {"ok": p.returncode == 0, "code": p.returncode, "stdout": p.stdout.strip(), "stderr": p.stderr.strip(), "cmd": cmd}
    except Exception as exc:
        return {"ok": False, "code": None, "stdout": "", "stderr": str(exc), "cmd": cmd}


def parse_json(text: str) -> Any:
    return json.loads(text)


def check_compile(results: list[dict[str, Any]]) -> None:
    for name, path in SCRIPTS.items():
        res = run(["python3", "-m", "py_compile", str(path)])
        results.append({"check": f"compile:{name}", **res})


def check_route(results: list[dict[str, Any]]) -> None:
    examples = [
        ("implementa un script para Fireflies", "claude_code"),
        ("prepara follow-up para INCOTEC", "stark"),
        ("revisión nocturna de logs", "selenia_manual"),
    ]
    for task, expected in examples:
        res = run(["python3", str(SCRIPTS["route_task"]), task])
        ok = res["ok"]
        got = None
        if ok:
            try:
                got = parse_json(res["stdout"]).get("recommended_route")
                ok = got == expected
            except Exception as exc:
                ok = False
                res["stderr"] += f"\nparse error: {exc}"
        results.append({"check": f"route:{task}", "expected": expected, "got": got, **res, "ok": ok})


def check_telegram_raw_block(results: list[dict[str, Any]]) -> None:
    raw = {
        "owner_agent": "techy",
        "signal_type": "lead_update",
        "summary": "user: hola\nagent: dime\nuser: msg\nagent: msg\nuser: msg\nagent: msg\nuser: msg\nagent: msg\nuser: msg\nagent: msg\nuser: msg\nagent: msg",
    }
    res = run(["python3", str(SCRIPTS["telegram_signal"]), "--json", json.dumps(raw, ensure_ascii=False)])
    # Expected failure.
    ok = not res["ok"] and "raw Telegram chat dump" in res["stdout"]
    results.append({"check": "telegram:raw_dump_block", "expected": "reject", **res, "ok": ok})


def check_selenia_dry_run(results: list[dict[str, Any]]) -> None:
    res = run(["python3", str(SCRIPTS["selenia_build_report"]), "--dry-run"], timeout=45)
    ok = res["ok"] and "Selenia Report" in res["stdout"] and "sin cron" in res["stdout"]
    results.append({"check": "selenia:dry_run", **res, "ok": ok})


def check_approval_temp(results: list[dict[str, Any]]) -> None:
    # Use a temp workspace so this check does not append to {{USER_FIRSTNAME}}'s real approvals.md.
    with tempfile.TemporaryDirectory() as tmp:
        tmpw = Path(tmp)
        env = os.environ.copy()
        env["JORGE_WORKSPACE"] = str(tmpw)
        (tmpw / "Life OS" / "00. Inbox").mkdir(parents=True, exist_ok=True)
        (tmpw / ".claude" / "logs" / "approvals").mkdir(parents=True, exist_ok=True)
        payload = {
            "owner_agent": "test",
            "permission_level": "L3",
            "action_type": "test",
            "proposed_action": "Test approval item only",
            "why_it_matters": "Healthcheck",
            "risk": "None, temp workspace",
        }
        try:
            p = subprocess.run(
                ["python3", str(SCRIPTS["approval_item"]), "--json", json.dumps(payload)],
                text=True,
                capture_output=True,
                timeout=30,
                cwd=str(WORKSPACE),
                env=env,
            )
            ok = p.returncode == 0 and (tmpw / "Life OS" / "00. Inbox" / "approvals.md").exists()
            results.append({"check": "approval:temp_write", "ok": ok, "code": p.returncode, "stdout": p.stdout.strip(), "stderr": p.stderr.strip(), "cmd": ["approval_item temp"]})
        except Exception as exc:
            results.append({"check": "approval:temp_write", "ok": False, "stderr": str(exc), "cmd": ["approval_item temp"]})


def write_report(results: list[dict[str, Any]]) -> Path:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.now().date().isoformat()
    path = REPORT_DIR / f"Healthcheck - {today}.md"
    passed = sum(1 for r in results if r.get("ok"))
    total = len(results)
    lines = [
        f"# Helios Healthcheck — {today}",
        "",
        f"Generated: {datetime.now().astimezone().isoformat(timespec='seconds')}",
        f"Result: {passed}/{total} checks passed",
        "",
        "## Checks",
        "",
    ]
    for r in results:
        status = "PASS" if r.get("ok") else "FAIL"
        lines.append(f"### {status} — {r.get('check')}")
        if r.get("expected") is not None:
            lines.append(f"- Expected: {r.get('expected')}")
            lines.append(f"- Got: {r.get('got')}")
        if not r.get("ok"):
            lines.append(f"- stdout: `{str(r.get('stdout',''))[:500]}`")
            lines.append(f"- stderr: `{str(r.get('stderr',''))[:500]}`")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> int:
    results: list[dict[str, Any]] = []
    check_compile(results)
    check_route(results)
    check_telegram_raw_block(results)
    check_selenia_dry_run(results)
    check_approval_temp(results)
    report_path = write_report(results)
    ok = all(r.get("ok") for r in results)
    print(json.dumps({
        "success": ok,
        "passed": sum(1 for r in results if r.get("ok")),
        "total": len(results),
        "report_path": str(report_path),
        "failures": [r.get("check") for r in results if not r.get("ok")],
    }, ensure_ascii=False, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
