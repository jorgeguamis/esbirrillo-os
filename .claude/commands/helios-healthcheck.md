---
description: Ejecuta healthcheck local seguro de Helios/Selenia. No envía nada ni toca sistemas externos.
---

# /helios-healthcheck

Ejecuta validaciones locales de scripts Helios/Selenia.

## Uso

```bash
python3 ${LIFEOS_ROOT}/.claude/execution/helios_healthcheck.py
```

## Comprueba

- Compilación de scripts críticos.
- Routing de ejemplos.
- Bloqueo de raw dumps Telegram.
- Selenia dry-run.
- Approval queue en workspace temporal.

## Output

Crea informe:

`${LIFEOS_ROOT}/${VAULT_NAME}/00. Inbox/selenia/Healthcheck - YYYY-MM-DD.md`

## Seguridad

- No envía mensajes.
- No modifica Notion/CRM/finanzas.
- No activa crons.
- No borra.
- Solo escribe informe de healthcheck interno.
