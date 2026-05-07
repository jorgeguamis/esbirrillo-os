---
description: Stage 7 of /setup-wizard. Final validation. Runs /helios-healthcheck, validates Telegram bot end-to-end, generates first /morning, confirms Selenia nightly cron is scheduled. ~15 minutes. After this stage the user has a working system.
---

# validate-system — Verificación end-to-end

Stage 7. ~15 minutos. La última etapa del wizard.

## Goal

Asegurar que cada pieza configurada en stages anteriores **realmente funciona**. Si algo falla, dejarlo flagged como pendiente; el usuario puede operar el sistema con el resto.

## Prerequisites

Stages 1–6 completos. `setup-wizard-state.json` debe tener:
- `user_summary` poblado.
- `domain_agents[]` con N≥1.
- `connected_services[]` con al menos Notion + Telegram.

## Protocol

### Test 1 — Helios healthcheck

```
python3 ${LIFEOS_ROOT}/.claude/execution/helios_healthcheck.py
```

Resultado esperado: exit 0. El script verifica:
- `route_task.py` responde correctamente.
- `log_event.py` puede escribir.
- `telegram_signal.py` valida señales.
- `selenia_build_report.py` genera reportes.
- `approval_item.py` crea items.

Si falla: mostrar al usuario qué scripts fallaron + razón. Permitir skip (con flag `pending_fixes[]`).

### Test 2 — Telegram round-trip

1. **Setup verificación:** el usuario manda al bot un mensaje "test".
2. **El sistema responde** desde el grupo correcto:
   - DM → esbirrillo responde.
   - Grupo de techy → techy responde.
   - Grupo de cualquier domain agent → ese agent responde.
3. Validar latencia (<10s desde mensaje hasta respuesta).

Si falla: diagnosticar (chat_id incorrecto, runtime no arrancado, persona file no encontrado). Skip si necesario.

### Test 3 — Generar primera daily note

```
/morning
```

Esperado: el comando lee context files, calendar, working memory; genera daily note en `02. Areas/personal/diario/01. Daily/{{today}}.md` con TOP 2 + Quick Win.

Si la daily note se genera correctamente y el usuario aprueba el contenido → ✅.

### Test 4 — Procesar una reunión Fireflies

Si el usuario tiene meetings recientes:

```
/process-meeting
```

Esperado: el comando lista las últimas reuniones, el usuario elige una, el sistema clasifica (cliente/interna/idea) y procesa.

Si no hay meetings: skip.

### Test 5 — Capturar conocimiento

Pide al usuario una URL o un párrafo de texto:

```
/capture <texto o URL>
```

Esperado: librarian genera atomic note en `00. Inbox/`, sugiere tags y conexiones.

### Test 6 — Selenia nocturno

Cargar el cron de Selenia (si no está aún):

```
launchctl load ~/Library/LaunchAgents/com.{{user}}.selenia-nightly.plist
```

O si Hermes-agent runtime: verificar que el cron `selenia_nightly` esté registrado.

Pide al usuario:
> "Selenia se ejecuta a las 23:00. Mañana por la mañana mira `${LIFEOS_ROOT}/${VAULT_NAME}/00. Inbox/selenia/` — debería haber un report de lo que pasó hoy."

### Test 7 — Working memory write-back

Manda al esbirrillo (DM Telegram) un mensaje informativo:
> "He cerrado el deal con X por 5k"

Esperado: esbirrillo registra en working memory (sección domain agent o esbirrillo, según). El SessionEnd hook actualiza el archivo.

Verificar que la línea apareció en `${USER_CLAUDE_DIR}/memory/working-memory.md`.

## Output: setup-completed.md

Si todos los tests verde (o skips conocidos):

`${USER_CLAUDE_DIR}/memory/setup-completed.md`:

```markdown
# Setup completed — {{user_firstname}}

**Fecha:** {{date}}
**Tiempo total invertido:** {{total_minutes}} min, distribuidos en {{n_sessions}} sesiones.

## Generated

### Agentes core
- esbirrillo
- librarian
- techy
- reviewer

### Agentes de dominio
{{domain_agents_list}}

### Context files
{{context_files_list}}

### Frameworks
{{frameworks_completed}}

### Notion DBs registradas
{{notion_dbs_list}}

### Telegram
- Bot: {{bot_name}}
- Grupos: {{n_groups}}
- chat_ids registrados: {{n_chat_ids}}

## Tests

| Test | Status |
|---|---|
| Helios healthcheck | ✅ / ⚠️ |
| Telegram round-trip | ✅ / ⚠️ |
| /morning | ✅ |
| /process-meeting | ✅ / skip |
| /capture | ✅ |
| Selenia cron | ✅ |
| Working memory | ✅ |

## Pending fixes

{{pending_fixes_list}}

## Next steps

1. **Mañana por la mañana:** ejecuta `/morning` en Telegram o CLI. Empieza tu primer día con el sistema.
2. **Esta semana:** intenta usar `/process-meeting`, `/capture`, `/reflect` cada día.
3. **Domingo:** ejecuta `/weekly-review`. Va a leer todo lo que hayas generado durante la semana.
4. **En 7 días:** ejecuta `/setup-wizard --review` para refinar lo que descubras.
5. **Si algo no funciona:** habla con `techy` por Telegram o ejecuta `/helios-healthcheck`.

## Soporte

- `docs/INSTALL.md` — referencia del setup técnico.
- `docs/TROUBLESHOOTING.md` — soluciones a problemas comunes.
- `audit/` — auditoría del sistema fuente y arquitectura.
```

## Closing message al usuario

```
"🎉 Setup completo.

Has invertido ~{{total_minutes}} minutos. Lo que tienes ahora:

✓ {{n_agents}} agentes (4 core + {{n_domain}} de dominio)
✓ {{n_context_files}} context files que el sistema lee antes de cada operación
✓ {{n_frameworks}} frameworks personales sintetizando tu norte
✓ Notion conectado con {{n_dbs}} DBs
✓ Telegram con {{n_groups}} grupos
✓ Selenia activado, te dejará un report cada noche en `00. Inbox/selenia/`

Mañana por la mañana, abre Telegram y escribe al esbirrillo:
'¿Qué tengo hoy?'

Te sorprenderá lo bien que te conoce ya. Y va a ir mejorando — cada
conversación, cada review, cada reflexión añade contexto.

¿Alguna pregunta antes de cerrar la sesión?"
```

## Self-annealing

| Date | Issue/Learning | Resolution |
|---|---|---|
