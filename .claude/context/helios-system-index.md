# Helios/Selenia System Index

Updated: 2026-05-03

## Core scripts

| Script | Purpose | Safety level |
|---|---|---|
| `.claude/execution/log_event.py` | Registra eventos JSONL sanitizados | L1 |
| `.claude/execution/selenia_build_report.py` | Genera Selenia Report desde logs/señales | L1 |
| `.claude/execution/telegram_signal.py` | Registra señales Telegram resumidas | L1 |
| `.claude/execution/route_task.py` | Recomienda ruta Helios | L0 |
| `.claude/execution/approval_item.py` | Crea approval items pendientes | L1 |
| `.claude/execution/helios_healthcheck.py` | Valida scripts críticos | L1 |

## Commands

| Command file | Purpose |
|---|---|
| `.claude/commands/selenia-nightly.md` | Ejecutar Selenia manual |
| `.claude/commands/telegram-signal.md` | Registrar señal Telegram |
| `.claude/commands/route-task.md` | Clasificar tarea/ruta |
| `.claude/commands/approval-item.md` | Crear approval pendiente |
| `.claude/commands/helios-healthcheck.md` | Ejecutar healthcheck |

## Reports

| Path | Purpose |
|---|---|
| `${VAULT_NAME}/00. Inbox/selenia/Selenia Report - YYYY-MM-DD.md` | Informe Selenia |
| `${VAULT_NAME}/00. Inbox/selenia/Healthcheck - YYYY-MM-DD.md` | Resultado healthcheck |
| `${VAULT_NAME}/00. Inbox/selenia/Selenia Cycle - YYYY-MM-DD-HHMM.md` | Informe de ciclo seguro Helios/Selenia |
| `${VAULT_NAME}/00. Inbox/selenia/Initial Audit - YYYY-MM-DD.md` | Auditoría inicial |
| `${VAULT_NAME}/00. Inbox/approvals.md` | Cola de approvals |

## Logs

| Path | Purpose |
|---|---|
| `.claude/logs/executions/YYYY-MM-DD.jsonl` | Eventos de ejecución |
| `.claude/logs/telegram/YYYY-MM-DD.jsonl` | Señales Telegram estructuradas |
| `.claude/logs/approvals/YYYY-MM-DD.jsonl` | Approval items |
| `.claude/logs/selenia/YYYY-MM-DD.jsonl` | Runs internos Selenia |

## Safe commands

```bash
python3 ${LIFEOS_ROOT}/.claude/execution/helios_healthcheck.py
python3 ${LIFEOS_ROOT}/.claude/execution/selenia_build_report.py
python3 ${LIFEOS_ROOT}/.claude/execution/route_task.py "tarea"
```

## Rules

- L3/L4 siempre a approval queue.
- Telegram se guarda como señal, no raw chat.
- Selenia propone, no ejecuta.
- Cron nocturno solo L0/L1.
