#!/usr/bin/env python3
"""
Script: selenia_build_report.py
System: Helios/Selenia MVP
Description: Build a manual Selenia report from execution logs and summarized Telegram signals.

MVP rules:
- Reads logs and context summaries.
- Writes a markdown report in ${VAULT_NAME}/00. Inbox/selenia/.
- Does NOT send Telegram messages.
- Does NOT edit skills, agents, working-memory, Notion, CRM, finance DBs, or crons.
- Does NOT ingest raw Telegram conversations; only structured signals/digests.

Usage:
  python3 ${LIFEOS_ROOT}/.claude/execution/selenia_build_report.py
  python3 ${LIFEOS_ROOT}/.claude/execution/selenia_build_report.py --date 2026-05-03
  python3 ${LIFEOS_ROOT}/.claude/execution/selenia_build_report.py --days 3
  python3 ${LIFEOS_ROOT}/.claude/execution/selenia_build_report.py --dry-run
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable

WORKSPACE = Path(os.environ.get("JORGE_WORKSPACE", "${LIFEOS_ROOT}"))
CLAUDE_DIR = WORKSPACE / ".claude"
LIFE_OS = WORKSPACE / "Life OS"
EXECUTION_LOG_DIR = CLAUDE_DIR / "logs" / "executions"
TELEGRAM_SIGNAL_DIR = CLAUDE_DIR / "logs" / "telegram"
SELENIA_INTERNAL_LOG_DIR = CLAUDE_DIR / "logs" / "selenia"
REPORT_DIR = LIFE_OS / "00. Inbox" / "selenia"
CONTEXT_DIR = CLAUDE_DIR / "context"

SECRETISH = re.compile(r"(?i)(api[_-]?key|token|secret|password|passwd|pwd|bearer\s+|sk-[a-z0-9_-]{16,})")


@dataclass
class LoadedEvents:
    execution_events: list[dict[str, Any]]
    telegram_signals: list[dict[str, Any]]
    files_read: list[str]
    warnings: list[str]


def parse_date(value: str | None) -> date:
    if not value:
        return datetime.now().date()
    return datetime.strptime(value, "%Y-%m-%d").date()


def dates_for_range(end: date, days: int) -> list[date]:
    return [end - timedelta(days=i) for i in reversed(range(max(days, 1)))]


def safe_read_text(path: Path, warnings: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        warnings.append(f"No existe: {path}")
        return ""
    except Exception as exc:
        warnings.append(f"No se pudo leer {path}: {exc}")
        return ""


def load_jsonl(path: Path, warnings: list[str]) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    if not path.exists():
        return events
    for idx, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        raw = line.strip()
        if not raw:
            continue
        if SECRETISH.search(raw):
            warnings.append(f"Posible secreto detectado en {path.name}:{idx}; línea omitida del informe")
            continue
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError as exc:
            warnings.append(f"JSON inválido en {path.name}:{idx}: {exc}")
            continue
        if isinstance(obj, dict):
            events.append(obj)
        else:
            warnings.append(f"Entrada no objeto en {path.name}:{idx}; omitida")
    return events


def load_events(target_dates: Iterable[date]) -> LoadedEvents:
    warnings: list[str] = []
    files_read: list[str] = []
    execution_events: list[dict[str, Any]] = []
    telegram_signals: list[dict[str, Any]] = []

    for d in target_dates:
        name = f"{d.isoformat()}.jsonl"
        execution_path = EXECUTION_LOG_DIR / name
        telegram_path = TELEGRAM_SIGNAL_DIR / name
        if execution_path.exists():
            execution_events.extend(load_jsonl(execution_path, warnings))
            files_read.append(str(execution_path))
        if telegram_path.exists():
            telegram_signals.extend(load_jsonl(telegram_path, warnings))
            files_read.append(str(telegram_path))

    return LoadedEvents(execution_events, telegram_signals, files_read, warnings)


def s(value: Any, default: str = "") -> str:
    if value is None:
        return default
    if isinstance(value, (dict, list)):
        try:
            return json.dumps(value, ensure_ascii=False)
        except Exception:
            return str(value)
    return str(value)


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def short(text: Any, limit: int = 220) -> str:
    cleaned = re.sub(r"\s+", " ", s(text)).strip()
    if len(cleaned) <= limit:
        return cleaned
    return cleaned[: limit - 1].rstrip() + "…"


def bullet(items: list[str], empty: str = "Nada relevante detectado.") -> str:
    clean = [i for i in items if i]
    if not clean:
        return f"- {empty}"
    return "\n".join(f"- {i}" for i in clean)


def table(rows: list[list[str]], headers: list[str], empty: str = "Sin datos.") -> str:
    if not rows:
        return empty
    out = []
    out.append("| " + " | ".join(headers) + " |")
    out.append("|" + "|".join(["---"] * len(headers)) + "|")
    for row in rows:
        safe = [c.replace("|", "/").replace("\n", " ") for c in row]
        out.append("| " + " | ".join(safe) + " |")
    return "\n".join(out)


def read_context_snippets(warnings: list[str]) -> dict[str, str]:
    candidates = {
        "routing": CONTEXT_DIR / "helios-routing.md",
        "permissions": CONTEXT_DIR / "permissions-matrix.md",
        "source_of_truth": CONTEXT_DIR / "source-of-truth-map.md",
        "constraints": CONTEXT_DIR / "constraints.md",
        "telegram_routing": CLAUDE_DIR / "telegram-routing.md",
    }
    snippets: dict[str, str] = {}
    for key, path in candidates.items():
        if path.exists():
            text = safe_read_text(path, warnings)
            snippets[key] = text[:3000]
        else:
            warnings.append(f"Context file ausente: {path}")
    return snippets


def classify_event(event: dict[str, Any]) -> dict[str, bool]:
    txt = " ".join(
        short(event.get(k), 500)
        for k in ["objective", "result", "next_action", "route", "agent", "skill", "source", "actor"]
    ).lower()
    errors = as_list(event.get("errors"))
    return {
        "has_error": bool(errors) or any(word in txt for word in ["error", "falló", "failed", "timeout", "bloqueado"]),
        "needs_action": bool(short(event.get("next_action"))) and short(event.get("next_action")).lower() not in {"none", "null", "n/a"},
        "is_telegram": event.get("source") == "telegram" or bool(event.get("telegram_context")),
        "is_write": bool(as_list(event.get("files_modified"))) or "write" in txt or "cread" in txt or "actualiz" in txt,
        "needs_approval": event.get("permission_level") in {"L3", "L4"} or "aprob" in txt or "confirm" in txt,
    }


def generate_recommendations(events: list[dict[str, Any]], telegram_signals: list[dict[str, Any]], warnings: list[str]) -> list[str]:
    recs: list[str] = []
    classified = [classify_event(e) for e in events]
    errors = sum(1 for c in classified if c["has_error"])
    writes = sum(1 for c in classified if c["is_write"])
    actions = sum(1 for c in classified if c["needs_action"])
    telegram_count = sum(1 for c in classified if c["is_telegram"]) + len(telegram_signals)

    if errors:
        recs.append(f"Revisar {errors} evento(s) con errores/fricciones antes de automatizar cron nocturno.")
    if actions:
        recs.append(f"Convertir {actions} next_action(s) en cola de approvals o tareas explícitas; ahora solo quedan en logs.")
    if writes and not any(e.get("skill") == "selenia-nightly-report" for e in events):
        recs.append("Mantener logging obligatorio para escrituras internas; el builder ya lo resume, pero falta política de retención automatizada.")
    if telegram_count == 0:
        recs.append("Crear canal de señales Telegram estructuradas: .claude/logs/telegram/YYYY-MM-DD.jsonl. Sin esto, Selenia solo ve Telegram cuando otro log lo resume.")
    else:
        recs.append("Telegram ya entra como señal resumida; siguiente mejora: normalizar signal_type y owner_agent por grupo.")
    if warnings:
        recs.append("Limpiar warnings de lectura/logging para que Selenia no arrastre ruido operativo.")
    recs.append("No activar cron todavía: usar 2-3 ejecuciones manuales para ajustar formato y falsos positivos.")
    return recs


def build_report(target_dates: list[date], loaded: LoadedEvents) -> str:
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    events = loaded.execution_events
    telegram_signals = loaded.telegram_signals
    warnings = loaded.warnings[:]
    contexts = read_context_snippets(warnings)

    by_actor = Counter(short(e.get("actor") or "unknown", 40) for e in events)
    by_source = Counter(short(e.get("source") or "unknown", 40) for e in events)
    by_route = Counter(short(e.get("route") or "unknown", 60) for e in events)
    by_permission = Counter(short(e.get("permission_level") or "unknown", 10) for e in events)

    classified = [(e, classify_event(e)) for e in events]
    error_events = [e for e, c in classified if c["has_error"]]
    action_events = [e for e, c in classified if c["needs_action"]]
    approval_events = [e for e, c in classified if c["needs_approval"]]
    telegram_events = [e for e, c in classified if c["is_telegram"]]

    modified_counter: Counter[str] = Counter()
    read_counter: Counter[str] = Counter()
    tools_counter: Counter[str] = Counter()
    skills_counter: Counter[str] = Counter()
    agents_counter: Counter[str] = Counter()
    for e in events:
        modified_counter.update(short(x, 160) for x in as_list(e.get("files_modified")) if x)
        read_counter.update(short(x, 160) for x in as_list(e.get("files_read")) if x)
        tools_counter.update(short(x, 80) for x in as_list(e.get("tools_used")) if x)
        if e.get("skill"):
            skills_counter.update([short(e.get("skill"), 80)])
        if e.get("agent"):
            agents_counter.update([short(e.get("agent"), 80)])

    event_rows = []
    for e in events[-15:]:
        event_rows.append([
            short(e.get("timestamp"), 19),
            short(e.get("actor") or "?", 20),
            short(e.get("route") or "?", 28),
            short(e.get("objective"), 90),
            short(e.get("result"), 100),
        ])

    next_actions = []
    for e in action_events:
        next_actions.append(f"{short(e.get('actor') or 'unknown', 30)} → {short(e.get('next_action'), 180)}")

    errors = []
    for e in error_events:
        err = "; ".join(short(x, 160) for x in as_list(e.get("errors")) if x) or short(e.get("result"), 180)
        errors.append(f"{short(e.get('actor') or 'unknown', 30)} / {short(e.get('objective'), 100)} → {err}")

    telegram_lines = []
    for e in telegram_events:
        ctx = e.get("telegram_context")
        if isinstance(ctx, dict):
            signal_type = short(ctx.get("signal_type") or "telegram_signal", 40)
            summary = short(ctx.get("signal_summary") or e.get("result"), 180)
            agent = short(ctx.get("chat_agent") or e.get("agent") or e.get("actor") or "?", 30)
            telegram_lines.append(f"{agent} / {signal_type}: {summary}")
        else:
            telegram_lines.append(f"{short(e.get('actor') or '?', 30)}: {short(e.get('result'), 180)}")
    for sig in telegram_signals:
        telegram_lines.append(f"{short(sig.get('owner_agent') or sig.get('actor') or '?', 30)} / {short(sig.get('signal_type') or 'telegram_signal', 40)}: {short(sig.get('summary') or sig.get('result') or sig.get('signal_summary'), 180)}")

    approval_lines = []
    for e in approval_events:
        approval_lines.append(f"{short(e.get('permission_level'), 8)} · {short(e.get('objective'), 120)} · next: {short(e.get('next_action') or 'revisar si requiere aprobación', 120)}")

    recommendations = generate_recommendations(events, telegram_signals, warnings)
    period = f"{target_dates[0].isoformat()} → {target_dates[-1].isoformat()}" if target_dates else "sin fechas"

    lines: list[str] = []
    lines.append(f"# Selenia Report — {target_dates[-1].isoformat() if target_dates else date.today().isoformat()}")
    lines.append("")
    lines.append(f"Generado: {now}")
    lines.append(f"Periodo revisado: {period}")
    lines.append("Modo: manual MVP, sin cron, sin envíos externos, sin modificaciones automáticas.")
    lines.append("")
    lines.append("## 1. Resumen ejecutivo")
    lines.append("")
    lines.append(f"- Eventos de ejecución revisados: {len(events)}")
    lines.append(f"- Señales Telegram estructuradas revisadas: {len(telegram_signals)}")
    lines.append(f"- Eventos con contexto Telegram dentro de logs: {len(telegram_events)}")
    lines.append(f"- Eventos con errores/fricción: {len(error_events)}")
    lines.append(f"- Next actions detectadas: {len(action_events)}")
    lines.append(f"- Posibles approvals L3/L4 o confirmaciones: {len(approval_events)}")
    lines.append(f"- Archivos modificados únicos: {len(modified_counter)}")
    lines.append("")
    lines.append("Lectura Selenia: el sistema ya tiene logging base y rutas claras. El gap principal del MVP es que Telegram todavía entra mayormente como señal manual dentro de logs, no como digest estructurado independiente.")
    lines.append("")
    lines.append("## 2. Actividad reciente")
    lines.append("")
    lines.append(table(event_rows, ["Hora", "Actor", "Ruta", "Objetivo", "Resultado"], "Sin eventos en el periodo."))
    lines.append("")
    lines.append("## 3. Señales de Telegram")
    lines.append("")
    lines.append(bullet(telegram_lines, "No hay señales Telegram estructuradas en el periodo. Recomendado crear .claude/logs/telegram/YYYY-MM-DD.jsonl."))
    lines.append("")
    lines.append("## 4. Errores, fricción y riesgos")
    lines.append("")
    lines.append(bullet(errors, "No se detectaron errores explícitos."))
    lines.append("")
    lines.append("## 5. Next actions detectadas")
    lines.append("")
    lines.append(bullet(next_actions, "No hay next actions pendientes en logs."))
    lines.append("")
    lines.append("## 6. Approval queue candidata")
    lines.append("")
    lines.append(bullet(approval_lines, "No se detectaron eventos L3/L4 o confirmaciones pendientes."))
    lines.append("")
    lines.append("## 7. Archivos y artefactos tocados")
    lines.append("")
    lines.append("### Más modificados")
    lines.append(bullet([f"{path} ({count})" for path, count in modified_counter.most_common(20)], "No hay archivos modificados en logs."))
    lines.append("")
    lines.append("### Herramientas más usadas")
    lines.append(bullet([f"{name} ({count})" for name, count in tools_counter.most_common(15)], "No hay herramientas registradas."))
    lines.append("")
    lines.append("### Agentes / skills")
    lines.append(bullet([f"Agente: {name} ({count})" for name, count in agents_counter.most_common(10)] + [f"Skill: {name} ({count})" for name, count in skills_counter.most_common(10)], "No hay agentes/skills registrados."))
    lines.append("")
    lines.append("## 8. Distribución")
    lines.append("")
    dist_rows = []
    for label, counter in [("actor", by_actor), ("source", by_source), ("route", by_route), ("permission", by_permission)]:
        for key, count in counter.most_common(10):
            dist_rows.append([label, key, str(count)])
    lines.append(table(dist_rows, ["Tipo", "Valor", "Eventos"], "Sin distribución disponible."))
    lines.append("")
    lines.append("## 9. Recomendaciones Selenia")
    lines.append("")
    lines.append(bullet(recommendations))
    lines.append("")
    lines.append("## 10. Gaps del sistema")
    lines.append("")
    gaps = []
    if not telegram_signals:
        gaps.append("Falta digest estructurado independiente para Telegram. Crear writer/convención para señales por agente/grupo.")
    if not (CLAUDE_DIR / "commands" / "selenia-nightly.md").exists():
        gaps.append("Falta comando /selenia-nightly.")
    if not (CLAUDE_DIR / "skills" / "selenia-nightly-report" / "SKILL.md").exists():
        gaps.append("Falta skill local selenia-nightly-report.")
    if len(events) == 0:
        gaps.append("No hay logs de ejecución para el periodo; Selenia queda ciega.")
    if not contexts.get("source_of_truth"):
        gaps.append("Falta mapa source-of-truth accesible.")
    lines.append(bullet(gaps, "No se detectaron gaps críticos adicionales."))
    lines.append("")
    lines.append("## 11. Warnings técnicos")
    lines.append("")
    lines.append(bullet(warnings, "Sin warnings de lectura."))
    lines.append("")
    lines.append("## 12. Próximo paso recomendado")
    lines.append("")
    if not telegram_signals:
        lines.append("Usar `.claude/execution/telegram_signal.py` para registrar señales estructuradas desde Telegram sin guardar conversaciones completas; después ejecutar Selenia 2-3 noches manualmente antes de cron.")
    else:
        lines.append("Normalizar tipos de señal Telegram y empezar a agrupar por owner_agent para alimentar working-memory con aprobación.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("Nota de seguridad: este informe no debe contener secretos ni transcripciones completas. Si aparece información sensible, moverla a una fuente segura o regenerar el informe con eventos sanitizados.")
    return "\n".join(lines) + "\n"


def write_internal_run_log(report_path: Path, loaded: LoadedEvents, target_dates: list[date]) -> None:
    SELENIA_INTERNAL_LOG_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "timestamp": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "report_path": str(report_path),
        "dates": [d.isoformat() for d in target_dates],
        "execution_events": len(loaded.execution_events),
        "telegram_signals": len(loaded.telegram_signals),
        "files_read": loaded.files_read,
        "warnings": loaded.warnings,
    }
    path = SELENIA_INTERNAL_LOG_DIR / f"{target_dates[-1].isoformat()}.jsonl"
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build manual Selenia report from logs")
    parser.add_argument("--date", dest="date_str", help="End date YYYY-MM-DD. Defaults to today.")
    parser.add_argument("--days", type=int, default=1, help="How many days to include, ending at --date. Default: 1")
    parser.add_argument("--output", help="Optional output markdown path. Defaults to ${VAULT_NAME}/00. Inbox/selenia/Selenia Report - YYYY-MM-DD.md")
    parser.add_argument("--dry-run", action="store_true", help="Print report to stdout instead of writing file")
    args = parser.parse_args()

    end = parse_date(args.date_str)
    target_dates = dates_for_range(end, args.days)
    loaded = load_events(target_dates)
    report = build_report(target_dates, loaded)

    if args.dry_run:
        print(report)
        return 0

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    output = Path(args.output) if args.output else REPORT_DIR / f"Selenia Report - {end.isoformat()}.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")
    write_internal_run_log(output, loaded, target_dates)

    print(json.dumps({
        "success": True,
        "report_path": str(output),
        "dates": [d.isoformat() for d in target_dates],
        "execution_events": len(loaded.execution_events),
        "telegram_signals": len(loaded.telegram_signals),
        "warnings": loaded.warnings,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
