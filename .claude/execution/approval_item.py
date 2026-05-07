#!/usr/bin/env python3
"""
Script: approval_item.py
System: Helios/Selenia MVP
Description: Append a pending approval item to ${VAULT_NAME}/00. Inbox/approvals.md and JSONL log.

This never executes the proposed action. It only records a pending decision.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

WORKSPACE = Path(os.environ.get("JORGE_WORKSPACE", "${LIFEOS_ROOT}"))
APPROVALS_MD = WORKSPACE / "Life OS" / "00. Inbox" / "approvals.md"
APPROVALS_LOG_DIR = WORKSPACE / ".claude" / "logs" / "approvals"
VALID_PERMISSION_LEVELS = {"L2", "L3", "L4"}
VALID_STATUS = {"pending", "approved", "rejected", "edited", "expired"}
REQUIRED = ["owner_agent", "permission_level", "action_type", "proposed_action", "why_it_matters", "risk"]
SECRET_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|token|secret|password|passwd|pwd)\s*[:=]\s*[^\s,;]+"),
    re.compile(r"sk-[A-Za-z0-9_\-]{20,}"),
    re.compile(r"(?i)bearer\s+[A-Za-z0-9._\-]{20,}"),
]


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def today(ts: str) -> str:
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00")).date().isoformat()
    except Exception:
        return datetime.now().date().isoformat()


def sanitize_string(value: str, limit: int = 1200) -> str:
    value = value.strip()
    for p in SECRET_PATTERNS:
        value = p.sub(lambda m: m.group(0).split("=", 1)[0].split(":", 1)[0] + "=<redacted>", value)
    if len(value) > limit:
        value = value[:limit].rstrip() + "… <truncated>"
    return value


def sanitize(obj: Any) -> Any:
    if isinstance(obj, str):
        return sanitize_string(obj)
    if isinstance(obj, list):
        return [sanitize(x) for x in obj[:20]]
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            key = str(k)
            if re.search(r"(?i)(api[_-]?key|token|secret|password|passwd|pwd)", key):
                out[key] = "<redacted>"
            else:
                out[key] = sanitize(v)
        return out
    return obj


def read_input(args: argparse.Namespace) -> dict[str, Any]:
    raw = args.json_input if args.json_input else sys.stdin.read()
    raw = raw.strip()
    if not raw:
        raise ValueError("No JSON input provided")
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError("Input JSON must be an object")
    return data


def normalize(data: dict[str, Any]) -> dict[str, Any]:
    missing = [field for field in REQUIRED if not data.get(field)]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")
    item = sanitize(dict(data))
    item.setdefault("approval_id", str(uuid.uuid4()))
    item.setdefault("timestamp", now_iso())
    item.setdefault("source", "hermes")
    item.setdefault("status", "pending")
    item.setdefault("rollback_or_safe_alternative", "Preparar borrador o no ejecutar hasta nueva instrucción de {{USER_FIRSTNAME}}.")
    item.setdefault("approval_options", ["aprobar", "editar", "rechazar"])
    item.setdefault("related_files", [])
    item.setdefault("deadline", None)
    item.setdefault("notes", None)

    item["permission_level"] = str(item.get("permission_level", "")).upper()
    if item["permission_level"] not in VALID_PERMISSION_LEVELS:
        raise ValueError("permission_level must be L2, L3 or L4")
    item["status"] = str(item.get("status", "pending")).lower()
    if item["status"] not in VALID_STATUS:
        item["status"] = "pending"
    if item["status"] != "pending":
        raise ValueError("New approval items must start as pending")
    return item


def append_jsonl(item: dict[str, Any]) -> Path:
    APPROVALS_LOG_DIR.mkdir(parents=True, exist_ok=True)
    path = APPROVALS_LOG_DIR / f"{today(item['timestamp'])}.jsonl"
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n")
    return path


def ensure_md_header() -> None:
    APPROVALS_MD.parent.mkdir(parents=True, exist_ok=True)
    if APPROVALS_MD.exists() and APPROVALS_MD.read_text(encoding="utf-8").strip():
        return
    APPROVALS_MD.write_text(
        "# Approval Queue\n\n"
        "> Cola de acciones que requieren decisión explícita de {{USER_FIRSTNAME}}. Nada aquí está ejecutado por defecto.\n\n"
        "Estados: pending / approved / rejected / edited / expired.\n\n"
        "---\n\n",
        encoding="utf-8",
    )


def append_md(item: dict[str, Any]) -> None:
    ensure_md_header()
    related = item.get("related_files") or []
    if isinstance(related, str):
        related = [related]
    block = []
    block.append(f"## Pending — {item['action_type']} — {item['approval_id']}\n")
    block.append(f"- Timestamp: {item['timestamp']}")
    block.append(f"- Source: {item.get('source')}")
    block.append(f"- Owner agent: {item['owner_agent']}")
    block.append(f"- Permission level: {item['permission_level']}")
    block.append(f"- Status: {item['status']}")
    if item.get("deadline"):
        block.append(f"- Deadline: {item['deadline']}")
    block.append("")
    block.append("### Acción propuesta")
    block.append(str(item["proposed_action"]))
    block.append("")
    block.append("### Por qué importa")
    block.append(str(item["why_it_matters"]))
    block.append("")
    block.append("### Riesgo")
    block.append(str(item["risk"]))
    block.append("")
    block.append("### Alternativa segura / rollback")
    block.append(str(item.get("rollback_or_safe_alternative")))
    block.append("")
    block.append("### Opciones de aprobación")
    for opt in item.get("approval_options", ["aprobar", "editar", "rechazar"]):
        block.append(f"- {opt}")
    if related:
        block.append("")
        block.append("### Archivos relacionados")
        for path in related:
            block.append(f"- {path}")
    if item.get("notes"):
        block.append("")
        block.append("### Notas")
        block.append(str(item["notes"]))
    block.append("\n---\n")
    with APPROVALS_MD.open("a", encoding="utf-8") as f:
        f.write("\n".join(block))


def main() -> int:
    parser = argparse.ArgumentParser(description="Create pending approval item")
    parser.add_argument("--json", dest="json_input")
    args = parser.parse_args()
    try:
        item = normalize(read_input(args))
        log_path = append_jsonl(item)
        append_md(item)
    except Exception as exc:
        print(json.dumps({"success": False, "error": str(exc)}, ensure_ascii=False))
        return 1
    print(json.dumps({
        "success": True,
        "approval_id": item["approval_id"],
        "approvals_md": str(APPROVALS_MD),
        "log_path": str(log_path),
        "status": item["status"],
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
