---
description: Recomienda la ruta Helios para una tarea: Hermes directo, Claude Code, {{DOMAIN_AGENT_SALES}}, {{DOMAIN_AGENT_PRODUCT}}, {{DOMAIN_AGENT_FINANCE}}, techy, librarian, reviewer agent, meeting-processor o Selenia.
---

# /route-task

Clasifica una intención/tarea y recomienda ruta. Es recomendador, no gate obligatorio.

## Uso

```bash
python3 ${LIFEOS_ROOT}/.claude/execution/route_task.py "$ARGUMENTS"
```

También acepta JSON:

```bash
python3 ${LIFEOS_ROOT}/.claude/execution/route_task.py --json '{"task":"$ARGUMENTS","source":"telegram","actor":"esbirrillo"}'
```

## Output

Devuelve JSON con:

- `recommended_route`
- `owner`
- `confidence`
- `permission_level`
- `requires_confirmation`
- `context_pack`
- `alternatives`
- `next_step`

## Rutas posibles

- `hermes_direct`
- `claude_code`
- `stark`
- `shakes`
- `revo`
- `penny`
- `many`
- `dots`
- `jorge_agent`
- `meeting_processor`
- `selenia_manual`

## Reglas

- Si `requires_confirmation = true`, preparar borrador/plan y pedir aprobación antes de ejecutar.
- Si `recommended_route = claude_code`, usar Claude Code como operador profundo con scope claro.
- Si la tarea toca Telegram/envíos/CRM/finanzas/deploy/borrado, revisar permission_level.
- Registrar con log_event.py si se ejecuta escritura o cambio relevante.
