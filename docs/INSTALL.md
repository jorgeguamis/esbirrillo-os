# Install — Esbirrillo OS

> Status: skeleton. Las secciones marcadas TODO se completan en sem 1-2.

## Pre-requisitos

- macOS (Linux soporte futuro)
- Python 3.12+
- Git
- Claude Code CLI ([install](https://docs.claude.com/en/docs/claude-code/quickstart))
- Anthropic API key (o equivalente del provider que elijas)
- Cuenta Telegram + capacidad de crear bot via @BotFather

## Paso 1 — Clone del kit

```bash
git clone <repo-url> ~/Desktop/esbirrillo-os
cd ~/Desktop/esbirrillo-os
```

## Paso 2 — Run installer

```bash
./bin/install.sh
```

El installer pregunta:
1. Runtime: Hermes-agent (recomendado) o Claude Code lite.
2. Modelo provider.
3. Vault path.
4. Lanza setup de runtime correspondiente.

## Paso 3a — Setup Hermes-agent (Path A)

> TODO sem 1: detallar setup completo.

Pasos altos:
1. Clone NousResearch/hermes-agent en `~/.hermes/hermes-agent/`.
2. Crear venv + instalar deps.
3. Generar `~/.hermes/config.toml` desde template.
4. Symlink/copiar `.claude/` del kit a `~/.claude/`.
5. Generar crons desde `crons-template.json`.
6. Configurar launchd plist.
7. `launchctl load ~/Library/LaunchAgents/ai.hermes.gateway.plist`.

## Paso 3b — Setup Claude Code lite (Path B)

> TODO sem 1: detallar setup completo.

Pasos altos:
1. Instalar plugin oficial Telegram en Claude Code.
2. Symlink `.claude/` del kit a `~/.claude/`.
3. Configurar `claude-telegram.sh` con tu workdir.
4. Configurar launchd plist `com.<usuario>.claude-telegram.plist`.
5. `launchctl load`.

## Paso 4 — Setup Telegram bot

> TODO sem 2: guía con screenshots.

1. Crear bot via @BotFather en Telegram.
2. Guardar token en `.env`.
3. Crear los 7 grupos (uno por agente core + DM para esbirrillo).
4. Añadir el bot a cada grupo.
5. Obtener chat_ids (`getUpdates` o el helper que provee Hermes-agent).
6. Registrar chat_ids en `.claude/context/telegram-routing.md`.

## Paso 5 — Setup MCPs

> TODO sem 1.

Configurar `.mcp.json` con:
- Notion (integration token + workspace ID)
- Fireflies (API key)
- NotebookLM (OAuth)
- Filesystem (paths permitidos)
- Memory Bank (per-project)

## Paso 6 — First run de /setup-wizard

```bash
cd ~/Desktop/esbirrillo-os
claude
```

Dentro de Claude Code:
```
/setup-wizard
```

El wizard te entrevista en 7 sub-fases (~3-5h totales, distribuidas):

1. **Identity** — quién eres, valores, idioma, perfil personalidad.
2. **Create my agents** — para cada negocio/área, construye un agente custom.
3. **Context files** — Personal, business, health, learning, finances.
4. **Connect tools** — crea DBs Notion, conecta Calendar, Fireflies.
5. **Frameworks** — Vivid Vision, Life Map, Identity Interview, Future Self.
6. **Seed working memory** — primer working-memory.md por agente.
7. **Validate** — `/helios-healthcheck` + test Telegram + primer `/morning`.

## Paso 7 — Validación

```bash
/helios-healthcheck
```

Debería reportar todo verde. Test:
- En Telegram, escribe al esbirrillo: "qué tengo hoy".
- Genera daily note: `/morning`.
- Procesa una reunión Fireflies: `/process-meeting`.

## Troubleshooting

Ver `docs/TROUBLESHOOTING.md`.

## Soporte

Ver `docs/SUPPORT.md` (TBD).
