#!/usr/bin/env python3
"""
Script: telegram_signal.py
System: Helios/Selenia MVP
Description: Append a sanitized Telegram context signal to .claude/logs/telegram/YYYY-MM-DD.jsonl.

This is NOT a raw chat logger. It only stores compact operational signals for Selenia.

Usage:
  python3 ${LIFEOS_ROOT}/.claude/execution/telegram_signal.py <<'JSON'
  {
    "owner_agent": "stark",
    "chat_ref": "stark-group",
    "signal_type": "lead_update",
    "summary": "INCOTEC respondió y necesita follow-up",
    "suggested_destination": "Notion CRM / working-memory {{DOMAIN_AGENT_SALES}}",
    "requires_approval": false
  }
  JSON

  python3 .../telegram_signal.py --json '{"owner_agent":"esbirrillo","signal_type":"decision","summary":"..."}'
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
SIGNAL_DIR = WORKSPACE / ".claude" / "logs" / "telegram"

REQUIRED = ["owner_agent", "signal_type", "summary"]
VALID_AGENTS = {"esbirrillo", "stark", "revo", "penny", "many", "dots", "jorge", "selenia", "unknown"}
VALID_SIGNAL_TYPES = {
    "decision",
    "design_decision",
    "priority_change",
    "commitment",
    "task",
    "lead_update",
    "client_update",
    "finance_signal",
    "system_error",
    "blocker",
    "idea",
    "energy_signal",
    "meeting_signal",
    "approval_candidate",
    "other",
}
VALID_SENSITIVITY = {"low", "normal", "sensitive"}

SECRET_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|token|secret|password|passwd|pwd)\s*[:=]\s*[^\s,;]+"),
    re.compile(r"sk-[A-Za-z0-9_\-]{20,}"),
    re.compile(r"(?i)bearer\s+[A-Za-z0-9._\-]{20,}"),
]

RAW_DUMP_PATTERNS = [
    re.compile(r"(\n.*){20,}"),  # many-line dump
    re.compile(r"(?i)(^|\n)\s*(jorge|yo|tú|tu|assistant|bot|user|stark|revo|many|penny)\s*:\s*.*(\n.*:\s*){8,}"),
]


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def today_from_timestamp(ts: str) -> str:
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00")).date().isoformat()
    except Exception:
        return datetime.now().date().isoformat()


def sanitize_string(value: str) -> str:
    sanitized = value.strip()
    for pattern in SECRET_PATTERNS:
        sanitized = pattern.sub(lambda m: m.group(0).split("=", 1)[0].split(":", 1)[0] + "=<redacted>", sanitized)
    if len(sanitized) > 800:
        sanitized = sanitized[:800].rstrip() + "… <truncated>"
    return sanitized


def sanitize(obj: Any) -> Any:
    if isinstance(obj, str):
        return sanitize_string(obj)
    if isinstance(obj, list):
        return [sanitize(x) for x in obj[:20]]
    if isinstance(obj, dict):
        clean: dict[str, Any] = {}
        for k, v in obj.items():
            key = str(k)
            if re.search(r"(?i)(api[_-]?key|token|secret|password|passwd|pwd|raw|transcript|full_chat|messages)", key):
                clean[key] = "<redacted_or_disallowed>"
            else:
                clean[key] = sanitize(v)
        return clean
    return obj


def read_input(args: argparse.Namespace) -> dict[str, Any]:
    raw = args.json_input if args.json_input is not None else sys.stdin.read()
    raw = raw.strip()
    if not raw:
        raise ValueError("No JSON input provided")
    for pattern in RAW_DUMP_PATTERNS:
        if pattern.search(raw):
            raise ValueError("Input looks like a raw chat dump. Store a compact signal summary instead.")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("Input JSON must be an object")
    return data


def normalize_signal(data: dict[str, Any]) -> dict[str, Any]:
    missing = [field for field in REQUIRED if not data.get(field)]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")

    signal = sanitize(dict(data))
    signal.setdefault("signal_id", str(uuid.uuid4()))
    signal.setdefault("timestamp", now_iso())
    signal.setdefault("source", "telegram")
    signal.setdefault("chat_ref", "redacted-or-alias")
    signal.setdefault("suggested_destination", None)
    signal.setdefault("sensitivity", "normal")
    signal.setdefault("requires_approval", False)
    signal.setdefault("next_action", None)
    signal.setdefault("evidence_ref", None)

    signal["owner_agent"] = str(signal.get("owner_agent", "unknown")).lower().strip()
    if signal["owner_agent"] not in VALID_AGENTS:
        signal["owner_agent"] = "unknown"

    signal["signal_type"] = str(signal.get("signal_type", "other")).lower().strip()
    if signal["signal_type"] not in VALID_SIGNAL_TYPES:
        signal["signal_type"] = "other"

    signal["sensitivity"] = str(signal.get("sensitivity", "normal")).lower().strip()
    if signal["sensitivity"] not in VALID_SENSITIVITY:
        signal["sensitivity"] = "normal"

    if not isinstance(signal.get("requires_approval"), bool):
        signal["requires_approval"] = str(signal.get("requires_approval")).lower() in {"true", "1", "yes", "sí", "si"}

    signal["summary"] = str(signal.get("summary", "")).strip()
    if len(signal["summary"]) < 10:
        raise ValueError("summary is too short; write a useful operational signal")
    if len(signal["summary"]) > 800:
        raise ValueError("summary is too long; do not store raw Telegram content")

    # Detect raw-chat-like content after JSON parsing too. Escaped newlines inside JSON
    # become real newlines only here, so pre-parse checks are not enough.
    summary_lines = [line.strip() for line in signal["summary"].splitlines() if line.strip()]
    speaker_like = sum(1 for line in summary_lines if re.match(r"(?i)^(jorge|yo|tu|tú|assistant|bot|user|stark|revo|many|penny|esbirrillo|dots|selenia)\s*:", line))
    if len(summary_lines) >= 12 or speaker_like >= 6:
        raise ValueError("summary looks like a raw Telegram chat dump. Store one compact operational signal instead.")

    return signal


def append_signal(signal: dict[str, Any]) -> Path:
    SIGNAL_DIR.mkdir(parents=True, exist_ok=True)
    path = SIGNAL_DIR / f"{today_from_timestamp(signal['timestamp'])}.jsonl"
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(signal, ensure_ascii=False, sort_keys=True) + "\n")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Append structured Telegram signal for Selenia")
    parser.add_argument("--json", dest="json_input", help="JSON signal object. If omitted, reads stdin.")
    args = parser.parse_args()

    try:
        signal = normalize_signal(read_input(args))
        path = append_signal(signal)
    except Exception as exc:
        print(json.dumps({"success": False, "error": str(exc)}, ensure_ascii=False), file=sys.stdout)
        return 1

    print(json.dumps({
        "success": True,
        "signal_id": signal["signal_id"],
        "path": str(path),
        "owner_agent": signal["owner_agent"],
        "signal_type": signal["signal_type"],
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
