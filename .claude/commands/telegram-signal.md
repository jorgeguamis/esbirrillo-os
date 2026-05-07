---
description: Registra una señal resumida de Telegram para que Selenia la use como contexto, sin guardar conversación completa.
---

# /telegram-signal

Registra una señal operativa de Telegram para Selenia.

## Objetivo

Convertir una conversación/mensaje de Telegram en una señal compacta que Selenia pueda revisar por la noche.

Esto NO guarda raw chat logs.

## Uso

Ejecuta:

```bash
python3 ${LIFEOS_ROOT}/.claude/execution/telegram_signal.py <<'JSON'
{
  "owner_agent": "esbirrillo",
  "chat_ref": "dm-jorge",
  "signal_type": "decision",
  "summary": "$ARGUMENTS",
  "suggested_destination": "Selenia report / working-memory if stable",
  "sensitivity": "normal",
  "requires_approval": false
}
JSON
```

Si `$ARGUMENTS` no es una señal clara, pregunta a {{USER_FIRSTNAME}} o resume tú la señal en una frase operativa.

## Campos

- `owner_agent`: esbirrillo, stark, revo, penny, many, dots, jorge, selenia, unknown
- `signal_type`: decision, priority_change, commitment, task, lead_update, client_update, finance_signal, system_error, blocker, idea, energy_signal, meeting_signal, approval_candidate, other
- `summary`: resumen operativo corto, nunca conversación completa
- `suggested_destination`: dónde debería vivir si se consolida
- `requires_approval`: true si implica L3/L4 o cambio externo

## Reglas

- No guardar secretos.
- No guardar dumps de chat.
- No guardar teléfonos/PII salvo necesidad clara.
- Si la señal requiere acción externa, solo registrar como candidate; no ejecutar.
