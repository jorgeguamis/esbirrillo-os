#!/usr/bin/env python3
"""
Script: route_task.py
System: Helios MVP
Description: Recommend a route for a {{USER_FIRSTNAME}} task. This is a recommender, not a hard gate.

Usage:
  python3 ${LIFEOS_ROOT}/.claude/execution/route_task.py "crea un script para procesar Fireflies"
  echo "tengo que responder a INCOTEC" | python3 .../route_task.py
  python3 .../route_task.py --json '{"task":"...","source":"telegram","actor":"esbirrillo"}'
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

WORKSPACE = Path(os.environ.get("JORGE_WORKSPACE", "${LIFEOS_ROOT}"))
RULES_PATH = WORKSPACE / ".claude" / "execution" / "routing_rules.json"


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def normalize(text: str) -> str:
    text = text.lower()
    text = text.replace("º", "o")
    return text


def load_rules() -> dict[str, Any]:
    return json.loads(RULES_PATH.read_text(encoding="utf-8"))


def read_task(args: argparse.Namespace) -> dict[str, Any]:
    if args.json_input:
        data = json.loads(args.json_input)
        if not isinstance(data, dict):
            raise ValueError("--json must be an object")
        if not data.get("task"):
            raise ValueError("--json requires task")
        return data
    if args.task:
        return {"task": " ".join(args.task), "source": args.source, "actor": args.actor}
    stdin = sys.stdin.read().strip()
    if stdin:
        return {"task": stdin, "source": args.source, "actor": args.actor}
    raise ValueError("Provide a task as argument, stdin, or --json")


def keyword_score(text: str, keywords: list[str]) -> tuple[int, list[str]]:
    hits: list[str] = []
    score = 0
    for kw in keywords:
        k = normalize(kw)
        if not k:
            continue
        if " " in k:
            if k in text:
                hits.append(kw)
                score += 3
        else:
            if re.search(r"\b" + re.escape(k) + r"\w*\b", text):
                hits.append(kw)
                score += 2
    return score, hits


def infer_complexity(task: str) -> dict[str, Any]:
    t = normalize(task)
    signals = []
    if any(x in t for x in ["implement", "constru", "crea", "automat", "script", "sistema", "multiarchivo", "audita", "valida"]):
        signals.append("artifact_or_implementation")
    if any(x in t for x in ["envia", "manda", "publica", "cliente", "factura", "pago", "borra", "deploy", "push"]):
        signals.append("side_effect_risk")
    if len(task) > 400:
        signals.append("long_input")
    return {
        "signals": signals,
        "suggest_claude_code": "artifact_or_implementation" in signals,
        "requires_care": "side_effect_risk" in signals,
    }


def infer_permission(task: str, rules: dict[str, Any], base: str) -> tuple[str, list[str]]:
    t = normalize(task)
    hits: list[str] = []
    level = base.split("-")[-1] if "-" in base else base
    if level not in {"L0", "L1", "L2", "L3", "L4"}:
        level = "L1"
    for candidate in ["L3", "L4"]:
        for kw in rules.get("permission_escalation_keywords", {}).get(candidate, []):
            if normalize(kw) in t:
                hits.append(f"{candidate}:{kw}")
                if candidate == "L4" or level in {"L0", "L1", "L2"}:
                    level = candidate
    return level, hits


def recommend(data: dict[str, Any], rules: dict[str, Any]) -> dict[str, Any]:
    task = str(data["task"]).strip()
    text = normalize(task)
    scored = []
    for route in rules["routes"]:
        score, hits = keyword_score(text, route.get("keywords", []))
        # Mild source priors.
        source = str(data.get("source") or "").lower()
        if source == "telegram" and route["route"] in {"hermes_direct", "jorge_agent"}:
            score += 1
        if route["route"] == rules.get("default_route"):
            score += 0.5
        scored.append((score, hits, route))

    scored.sort(key=lambda x: x[0], reverse=True)
    best_score, best_hits, best_route = scored[0]
    alternatives = [
        {
            "route": r["route"],
            "owner": r["owner"],
            "score": score,
            "matched_keywords": hits[:8],
            "description": r.get("description"),
        }
        for score, hits, r in scored[1:4]
        if score > 0
    ]

    confidence = "low"
    if best_score >= 8:
        confidence = "high"
    elif best_score >= 3:
        confidence = "medium"

    complexity = infer_complexity(task)
    permission, permission_hits = infer_permission(task, rules, best_route.get("permission", "L1"))

    # If implementation/artifact and no domain-specific route is strongly matched, prefer Claude Code.
    if complexity["suggest_claude_code"] and best_route["route"] in {"hermes_direct", "many"} and best_score < 8:
        claude = next((r for r in rules["routes"] if r["route"] == "claude_code"), best_route)
        alternatives.insert(0, {
            "route": best_route["route"],
            "owner": best_route["owner"],
            "score": best_score,
            "matched_keywords": best_hits[:8],
            "description": best_route.get("description"),
        })
        best_route = claude
        best_hits = ["implementation/artifact signal"] + best_hits
        confidence = "medium"
        permission, permission_hits = infer_permission(task, rules, best_route.get("permission", "L1"))

    requires_confirmation = permission in {"L3", "L4"}
    next_step = build_next_step(best_route["route"], task, permission, requires_confirmation)

    return {
        "success": True,
        "timestamp": now_iso(),
        "mode": rules.get("mode", "recommender_not_gate"),
        "task": task,
        "source": data.get("source", "cli"),
        "actor": data.get("actor", "hermes"),
        "recommended_route": best_route["route"],
        "owner": best_route["owner"],
        "confidence": confidence,
        "score": best_score,
        "matched_keywords": best_hits[:10],
        "permission_level": permission,
        "permission_escalation_hits": permission_hits,
        "requires_confirmation": requires_confirmation,
        "description": best_route.get("description"),
        "context_pack": best_route.get("context_pack", []),
        "alternatives": alternatives,
        "complexity": complexity,
        "next_step": next_step,
    }


def build_next_step(route: str, task: str, permission: str, requires_confirmation: bool) -> str:
    if requires_confirmation:
        return f"Preparar borrador/plan y pedir aprobación explícita antes de ejecutar acción {permission}."
    if route == "claude_code":
        return "Delegar a Claude Code en print mode con workdir ${LIFEOS_ROOT} y allowed tools mínimos."
    if route == "selenia_manual":
        return "Ejecutar selenia_build_report.py y revisar informe antes de automatizar."
    if route == "meeting_processor":
        return "Localizar transcript/summary Fireflies, procesar en Life OS y aplicar permisos si hay CRM/tareas."
    if route == "hermes_direct":
        return "Responder o ejecutar directamente con contexto mínimo y logging si hay escritura."
    return f"Usar agente {route} como owner recomendado; Hermes coordina y verifica."


def main() -> int:
    parser = argparse.ArgumentParser(description="Recommend Helios route for a task")
    parser.add_argument("task", nargs="*", help="Task text")
    parser.add_argument("--json", dest="json_input", help="JSON object with task/source/actor")
    parser.add_argument("--source", default="cli", help="Input source, e.g. cli or telegram")
    parser.add_argument("--actor", default="hermes", help="Current actor")
    args = parser.parse_args()

    try:
        data = read_task(args)
        result = recommend(data, load_rules())
    except Exception as exc:
        print(json.dumps({"success": False, "error": str(exc)}, ensure_ascii=False), file=sys.stdout)
        return 1

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
