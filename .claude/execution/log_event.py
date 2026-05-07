#!/usr/bin/env python3
"""
Script: log_event.py
Skill/System: Helios/Selenia logging
Description: Append a sanitized execution event to .claude/logs/executions/YYYY-MM-DD.jsonl

Usage:
  python3 .claude/execution/log_event.py <<'JSON'
  {"actor":"hermes","source":"cli","objective":"...","result":"..."}
  JSON

  python3 .claude/execution/log_event.py --json '{"actor":"hermes","source":"cli","objective":"...","result":"..."}'
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

# {{USER_FIRSTNAME}}'s workspace root. Note: ${LIFEOS_ROOT}/.claude is a symlink to
# ${LIFEOS_ROOT}/${VAULT_NAME}/.claude, so using Path.resolve() on this file
# would report paths under the vault. Keep the canonical workspace path for outputs.
WORKSPACE = Path(os.environ.get("JORGE_WORKSPACE", "${LIFEOS_ROOT}"))
LOG_DIR = WORKSPACE / ".claude" / "logs" / "executions"
REQUIRED = ["actor", "source", "objective", "result"]
LIST_FIELDS = [
    "tools_used",
    "context_used",
    "files_read",
    "files_modified",
    "external_writes",
    "errors",
]
VALID_PERMISSION_LEVELS = {"L0", "L1", "L2", "L3", "L4", "unknown"}

SECRET_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|token|secret|password|passwd|pwd)\s*[:=]\s*[^\s,;]+"),
    re.compile(r"sk-[A-Za-z0-9_\-]{20,}"),
    re.compile(r"(?i)bearer\s+[A-Za-z0-9._\-]{20,}"),
]


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def today_from_timestamp(ts: str) -> str:
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00")).date().isoformat()
    except Exception:
        return datetime.now().date().isoformat()


def sanitize_string(value: str) -> str:
    sanitized = value
    for pattern in SECRET_PATTERNS:
        sanitized = pattern.sub(lambda m: m.group(0).split("=", 1)[0].split(":", 1)[0] + "=<redacted>", sanitized)
    # Avoid accidental huge raw dumps in log lines.
    if len(sanitized) > 4000:
        sanitized = sanitized[:4000] + "… <truncated>"
    return sanitized


def sanitize(obj: Any) -> Any:
    if isinstance(obj, str):
        return sanitize_string(obj)
    if isinstance(obj, list):
        return [sanitize(x) for x in obj]
    if isinstance(obj, dict):
        clean = {}
        for k, v in obj.items():
            key = str(k)
            if re.search(r"(?i)(api[_-]?key|token|secret|password|passwd|pwd)", key):
                clean[key] = "<redacted>"
            else:
                clean[key] = sanitize(v)
        return clean
    return obj


def normalize_event(event: dict[str, Any]) -> dict[str, Any]:
    missing = [field for field in REQUIRED if not event.get(field)]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")

    event = sanitize(dict(event))
    event.setdefault("event_id", str(uuid.uuid4()))
    event.setdefault("timestamp", now_iso())
    event.setdefault("route", "unknown")
    event.setdefault("skill", None)
    event.setdefault("agent", None)
    event.setdefault("user_confirmation", None)
    event.setdefault("permission_level", "unknown")
    event.setdefault("next_action", None)
    event.setdefault("telegram_context", None)

    if event["permission_level"] not in VALID_PERMISSION_LEVELS:
        event["permission_level"] = "unknown"

    for field in LIST_FIELDS:
        value = event.get(field)
        if value is None:
            event[field] = []
        elif isinstance(value, list):
            event[field] = value
        else:
            event[field] = [str(value)]

    # Keep core fields as strings for predictable downstream aggregation.
    for field in ["actor", "source", "objective", "route", "result"]:
        event[field] = str(event.get(field, ""))

    return event


def read_input(args: argparse.Namespace) -> dict[str, Any]:
    raw = args.json_input if args.json_input is not None else sys.stdin.read()
    raw = raw.strip()
    if not raw:
        raise ValueError("No JSON input provided")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("Input JSON must be an object")
    return data


def append_event(event: dict[str, Any]) -> Path:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    date = today_from_timestamp(event["timestamp"])
    path = LOG_DIR / f"{date}.jsonl"
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Append Helios/Selenia execution log event")
    parser.add_argument("--json", dest="json_input", help="JSON event object. If omitted, reads stdin.")
    args = parser.parse_args()

    try:
        event = normalize_event(read_input(args))
        path = append_event(event)
    except Exception as exc:
        print(json.dumps({"success": False, "error": str(exc)}, ensure_ascii=False), file=sys.stdout)
        return 1

    print(json.dumps({
        "success": True,
        "event_id": event["event_id"],
        "path": str(path),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
