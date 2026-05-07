---
skill: selenia-nightly-report
description: Genera y revisa Selenia Reports manuales desde logs de ejecución y señales Telegram resumidas, sin automatizaciones peligrosas.
trigger: "Selenia", "revisión nocturna", "/selenia-nightly", "nightly report", "revisar logs", "qué ha pasado hoy con los agentes"
---

# Selenia Nightly Report

Selenia es la capa de revisión/sueño del sistema Helios de {{USER_FIRSTNAME}}. Su trabajo es mirar lo que ha ocurrido, detectar fricción, huecos de contexto y mejoras posibles, y producir un informe interno para que {{USER_FIRSTNAME}} y Hermes decidan el siguiente paso.

## Principio

Selenia propone. No ejecuta cambios sensibles en MVP.

Permitido:
- Leer logs de ejecución en `.claude/logs/executions/YYYY-MM-DD.jsonl`.
- Leer señales Telegram estructuradas en `.claude/logs/telegram/YYYY-MM-DD.jsonl` si existen.
- Leer contexto de routing/permisos/source-of-truth.
- Crear informe markdown en `${VAULT_NAME}/00. Inbox/selenia/`.
- Señalar errores, next actions, approvals candidatos y mejoras.

No permitido en MVP sin aprobación explícita de {{USER_FIRSTNAME}}:
- Activar o modificar cron jobs.
- Enviar el informe por Telegram.
- Editar memoria, working-memory, skills o agentes automáticamente.
- Crear tareas Notion/CRM automáticamente.
- Guardar conversaciones completas de Telegram.
- Guardar transcripciones completas de Fireflies salvo proceso manual autorizado.

## Script principal

Usar siempre:

```bash
python3 ${LIFEOS_ROOT}/.claude/execution/selenia_build_report.py
```

Opciones:

```bash
python3 ${LIFEOS_ROOT}/.claude/execution/selenia_build_report.py --date 2026-05-03
python3 ${LIFEOS_ROOT}/.claude/execution/selenia_build_report.py --days 3
python3 ${LIFEOS_ROOT}/.claude/execution/selenia_build_report.py --dry-run
```

## Output esperado

El script devuelve JSON con:

- `success`
- `report_path`
- `dates`
- `execution_events`
- `telegram_signals`
- `warnings`

Y escribe el informe en:

`${LIFEOS_ROOT}/${VAULT_NAME}/00. Inbox/selenia/Selenia Report - YYYY-MM-DD.md`

## Formato del informe

Debe incluir:

1. Resumen ejecutivo.
2. Actividad reciente.
3. Señales de Telegram.
4. Errores/fricción/riesgos.
5. Next actions detectadas.
6. Approval queue candidata.
7. Archivos y artefactos tocados.
8. Distribución por actor/source/route/permiso.
9. Recomendaciones Selenia.
10. Gaps del sistema.
11. Warnings técnicos.
12. Próximo paso recomendado.

## Telegram como fuente

Telegram es fuente de contexto desde MVP, pero solo mediante señales resumidas.

Formato activo para `.claude/logs/telegram/YYYY-MM-DD.jsonl` usando:

```bash
python3 ${LIFEOS_ROOT}/.claude/execution/telegram_signal.py
```

Schema:

`${LIFEOS_ROOT}/.claude/execution/telegram_signal.schema.json`

Ejemplo:

```json
{
  "timestamp": "2026-05-03T02:15:00+02:00",
  "source": "telegram",
  "owner_agent": "stark",
  "chat_ref": "redacted-or-alias",
  "signal_type": "lead_update",
  "summary": "{{USER_FIRSTNAME}} dijo que INCOTEC respondió y necesita follow-up",
  "suggested_destination": "Notion CRM / working-memory {{DOMAIN_AGENT_SALES}}",
  "sensitivity": "normal",
  "requires_approval": false
}
```

No guardar:
- raw chat logs
- secretos
- teléfonos innecesarios
- datos financieros sensibles si basta con resumen

## Proceso de uso

1. Ejecutar el script.
2. Leer el informe generado.
3. Resumir a {{USER_FIRSTNAME}} los 3-5 puntos importantes.
4. Si hay L3/L4, presentarlo como approval candidate, no ejecutarlo.
5. Loguear la ejecución con `log_event.py`.

## Common Pitfalls

1. Confundir Selenia con un agente ejecutor: en MVP no cambia el sistema, solo informa.
2. Volcar conversaciones completas de Telegram: prohibido salvo autorización explícita y necesidad clara.
3. Activar cron antes de validar manualmente: esperar 2-3 ejecuciones manuales.
4. Asumir que no hay Telegram context si no hay archivo telegram: puede haber señales Telegram dentro de `telegram_context` en execution logs.
5. Usar rutas resueltas del symlink `.claude`: mantener rutas canónicas bajo `${LIFEOS_ROOT}/.claude`.

## Verification Checklist

- [ ] `selenia_build_report.py` compila con `python3 -m py_compile`.
- [ ] El script devuelve JSON `success: true`.
- [ ] El informe existe en Life OS.
- [ ] El informe no contiene secretos ni raw Telegram dumps.
- [ ] La ejecución queda registrada con `log_event.py`.
- [ ] No se creó cron ni se envió Telegram automáticamente.
