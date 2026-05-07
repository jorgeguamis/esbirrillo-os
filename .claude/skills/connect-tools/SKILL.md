---
description: Stage 4 of /setup-wizard. Walks the user through connecting Notion (creates standard DBs), Google Workspace (calendars, email), Fireflies, Telegram bot, and any other tools they configured in Stage 1. Registers IDs in notion-registry.md. ~30-60 minutes.
---

# connect-tools — Cablea las integraciones

Stage 4. ~30–60 minutes. Each tool the user mentioned in Stage 1 is connected, validated, and registered.

## Goal

Move from "the user has accounts somewhere" to "the system can read/write through MCPs". At the end, every integration responds to a healthcheck.

## Prerequisites

- Stage 1 captured the user's stack (calendars, emails, Notion workspace count, Fireflies, etc.).
- `bin/install.sh` has the MCP scaffolding in place (`.mcp.json.template`).
- User has API keys / OAuth ability for each service.

## Tone

- Operativo, no teórico. Cada paso tiene un test "verde/rojo".
- Si una integración falla, registra el motivo y permite skip — no bloquees al usuario en este stage.
- Resumir al final qué quedó conectado vs pendiente.

## Protocol

### 1 — Notion (15–25 min)

#### 1a. Authorization

```
1. Pide al usuario crear (o reutilizar) una "internal integration" en
   notion.so/profile/integrations.
2. Copiar el secret token.
3. Pegarlo en `.env` como `NOTION_TOKEN_PRIMARY=secret_xxx`.
4. Compartir las páginas/DBs relevantes con la integration en Notion.
5. Si el usuario tiene multi-workspace, repetir para cada uno
   (`NOTION_TOKEN_<WORKSPACE_NAME>`).
```

Test: `mcp__notion__API-get-self` — debe responder con la integration user.

#### 1b. Create standard DBs

Pregunta cuáles de las DBs estándar quiere crear:

```
- Tasks (recommended)
- Projects
- Habits
- Goals & Objectives
- Areas
- Accounts (finance)
- Expenses (finance)
- Incomes (finance)
- CRM Companies (if user has sales pipeline)
- CRM Contacts
- Notes / Books / Notebooks (if no Obsidian, or for ground-truth)
```

Por cada DB que el usuario quiere:
1. Pide la página parent en Notion (donde vivirá la DB).
2. Crea la DB con `mcp__notion__API-create-a-data-source` con properties estándar.
3. Captura `data_source_id` y registra en `notion-registry.md`.

#### 1c. Map existing DBs

Si el usuario ya tiene DBs en Notion para alguno de estos roles:
1. Búscalas (`notion-search`).
2. Confirma con el usuario que esa es la DB correcta.
3. Registra el ID.

#### 1d. Domain DBs

Por cada domain agent creado en Stage 2 que requiera Notion:
1. Pregunta qué DBs específicas usa.
2. Búsca/crea según corresponda.
3. Añade al agent file y a `notion-registry.md`.

### 2 — Google Workspace (10 min)

#### 2a. OAuth

```
1. El usuario debe correr `bin/setup-mcps.sh google-workspace`.
2. Esto abre un browser para OAuth de cada cuenta Google.
3. Por cada cuenta, generar un "profile" en MCP config.
```

#### 2b. Identify calendars

Por cada cuenta Google del usuario:
- ¿Cuál es el calendar primario para esta cuenta?
- ¿Qué calendarios secundarios incluyen eventos relevantes? (compartidos del equipo, eventos de partner, etc.)
- Registrar en `.env` como `GOOGLE_CAL_PROFILE_<NAME>=...`.

Test: `mcp__google-workspace__list_calendars` por cada profile.

#### 2c. Email read-only

Confirma con el usuario:
- ¿Permites lectura de email? (mucha gente prefiere no).
- Si sí, qué cuenta(s).

### 3 — Fireflies (5 min)

```
1. Usuario obtiene API key en fireflies.ai/settings/api-keys.
2. Pegarla en `.env` como `FIREFLIES_API_KEY=...`.
```

Test: `mcp__fireflies__fireflies_get_user` — debe responder con el user account.

Pregunta:
- ¿Qué meetings filtrar como "mine" vs "todos"? (relevante para skills como `meeting-processor`).
- ¿Hay etiquetas / channels Fireflies que mapear a domain agents?

### 4 — Telegram bot (10–15 min)

#### 4a. Create bot

```
1. En Telegram, abrir conversación con @BotFather.
2. /newbot, seguir flujo, elegir nombre y handle.
3. Copiar token, pegar en `.env` como `TELEGRAM_BOT_TOKEN=...`.
```

#### 4b. Create groups (one per agent)

Por cada agente del kit (esbirrillo, librarian, techy, reviewer) y cada domain agent:
1. Crear un grupo Telegram.
2. Añadir el bot al grupo.
3. Mandar un mensaje en el grupo.
4. Obtener `chat_id` (vía `getUpdates` de Telegram API o helper).
5. Registrar en `.claude/context/telegram-routing.md` (sustituyendo placeholders del template).

Para el DM directo del usuario con el esbirrillo:
- El usuario manda `/start` al bot.
- Capturar su user `chat_id`.
- Registrar como `1295530361` equivalent en routing.

### 5 — Hermes-agent setup (si user eligió Path A)

Si el usuario seleccionó Hermes-agent en `bin/install.sh`:

1. Verificar que `~/.hermes/hermes-agent/` está clonado.
2. Verificar venv y deps.
3. Generar `~/.hermes/config.toml` con:
   - `bot_token` desde `.env`.
   - `model` (Claude/Kimi/etc.) elegido en install.
   - paths a `.claude/` del kit.
4. Generar crons desde `crons-template.json` con sustitución de variables.
5. Cargar plist launchd.
6. `launchctl load ~/Library/LaunchAgents/ai.hermes.gateway.plist`.
7. Verificar `~/.hermes/logs/gateway.log` muestra arranque limpio.

### 6 — Validación final

Run `/helios-healthcheck`:

```
✓ Notion (primary): connected
✓ Notion (secondary): connected | not configured
✓ Google Workspace (X profiles): connected
✓ Fireflies: connected
✓ Telegram: bot active, N chat_ids registered
✓ Hermes-agent: gateway running | not running
✓ Filesystem MCP: ok
✓ Memory Bank MCP: ok
```

Si algo falla:
- Diagnosticar la causa (token equivocado, permisos, OAuth caducado).
- Documentar en `setup-wizard-state.json` como "pending".
- Permitir continuar al Stage 5 — esto no bloquea.

## Output

- `${LIFEOS_ROOT}/.claude/context/notion-registry.md` — populated with real IDs.
- `${LIFEOS_ROOT}/.claude/context/telegram-routing.md` — populated with real chat_ids.
- `~/.env` — populated with tokens (gitignored).
- `~/.hermes/config.toml` — if Hermes-agent path.
- `~/Library/LaunchAgents/*.plist` — if Hermes path.
- `setup-wizard-state.json` updated with `connected_services[]` y `pending_services[]`.

## Self-annealing

| Date | Issue/Learning | Resolution |
|---|---|---|
