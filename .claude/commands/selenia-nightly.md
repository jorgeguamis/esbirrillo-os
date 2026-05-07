---
description: Genera un Selenia Report manual desde logs y señales Telegram resumidas, sin cron ni envíos externos.
---

# /selenia-nightly

Genera una revisión nocturna/manual de Selenia.

## Objetivo

Revisar lo ocurrido en el sistema de agentes y producir un informe humano en Life OS:

`${VAULT_NAME}/00. Inbox/selenia/Selenia Report - YYYY-MM-DD.md`

## Reglas MVP

- NO activar cron.
- NO enviar Telegram automáticamente.
- NO editar memoria, skills, agentes, Notion, CRM ni finanzas automáticamente.
- NO guardar conversaciones completas de Telegram.
- Sí leer logs JSONL y señales Telegram estructuradas.
- Sí escribir un informe markdown interno recuperable.
- Sí proponer mejoras, approvals y siguientes acciones.

## Comando base

Desde `${LIFEOS_ROOT}` ejecuta:

```bash
python3 ${LIFEOS_ROOT}/.claude/execution/selenia_build_report.py
```

## Argumentos opcionales

- `$ARGUMENTS` puede contener flags como:
  - `--date YYYY-MM-DD`
  - `--days 3`
  - `--dry-run`

Ejemplo:

```bash
python3 ${LIFEOS_ROOT}/.claude/execution/selenia_build_report.py $ARGUMENTS
```

## Después de ejecutar

1. Leer el JSON de salida y confirmar `success: true`.
2. Abrir/leer el informe generado.
3. Resumir a {{USER_FIRSTNAME}}:
   - path del informe
   - errores detectados
   - next actions
   - recomendaciones Selenia
4. Registrar la ejecución con:

```bash
python3 ${LIFEOS_ROOT}/.claude/execution/log_event.py <<'JSON'
{
  "actor": "selenia",
  "source": "cli",
  "objective": "Generar Selenia Report manual",
  "route": "selenia_manual",
  "skill": "selenia-nightly-report",
  "agent": "selenia",
  "tools_used": ["terminal", "read_file"],
  "permission_level": "L1",
  "result": "Selenia Report generado en Life OS",
  "next_action": "Revisar recomendaciones y decidir si crear telegram_signal.py"
}
JSON
```
