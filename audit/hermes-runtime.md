# Hermes Runtime — arquitectura actual + path a kit

## TL;DR

Jorge tiene **dos** orquestadores Telegram corriendo en su Mac:

1. **Hermes-agent** (Nous Research, OSS MIT) — `~/.hermes/hermes-agent/`. El orquestador real. Python, su propio CLI, gateway multiplataforma, scheduler de crons, skill creation, multi-modelo. Lanzado por launchd `ai.hermes.gateway.plist`.
2. **Claude Code + plugin Telegram** — wrapper bash `~/.claude/claude-telegram.sh` que lanza `claude` CLI con `--channels "plugin:telegram@claude-plugins-official"`. Lanzado por launchd `com.jorgeguamis.claude-telegram.plist`. Versión "lite", coexiste con Hermes-agent.

Para el Esbirrillo OS Starter Kit: **NO extraer un Hermes propio.** Adoptar Hermes-agent OSS como pieza core. Setup = instalación de Hermes-agent + configuración con plantillas del kit. El kit aporta: prompts, agentes (.claude/agents/), skills, commands, crons templated, telegram-routing.

---

## Componentes en el sistema actual de Jorge

### 1. Hermes-agent (Nous Research)

- **Ubicación:** `/Users/jorgeguamis/.hermes/hermes-agent/`
- **Repo:** github.com/NousResearch/hermes-agent (MIT)
- **Docs:** hermes-agent.nousresearch.com
- **Stack:** Python 3.12, venv en `~/.hermes/hermes-agent/venv/`
- **Entry:** `python -m hermes_cli.main gateway run --replace`
- **Working dir:** `~/.hermes/hermes-agent/`
- **Env vars:** `HERMES_HOME=~/.hermes`, `VIRTUAL_ENV=~/.hermes/hermes-agent/venv`
- **Logs:** `~/.hermes/logs/gateway.log`, `gateway.error.log`
- **Skills propias:** `~/.hermes/skills/` (separadas de `~/.claude/skills/`). Ej: `productivity/google-workspace/scripts/google_api.py` para los 3 calendarios via OAuth profiles.
- **launchd plist:** `~/Library/LaunchAgents/ai.hermes.gateway.plist` (RunAtLoad + KeepAlive on failure)

Capacidades clave:
- Gateway Telegram/Discord/Slack/WhatsApp/Signal/CLI desde un solo proceso.
- Scheduler de crons nativo con delivery configurable.
- Skill creation/auto-mejora.
- Subagent spawning para paralelización.
- Soporta cualquier modelo (Kimi, GPT, Claude, Llama vía Nous Portal/OpenRouter/etc.).
- Backends: local, Docker, SSH, Daytona, Singularity, Modal.

### 2. Claude Code + Telegram plugin (alternativa lite)

- **Wrapper:** `~/.claude/claude-telegram.sh`:
  ```bash
  cd /Users/jorgeguamis/Desktop
  exec /usr/bin/script -q /dev/null /opt/homebrew/bin/claude \
    --channels "plugin:telegram@claude-plugins-official" \
    --permission-mode auto \
    --append-system-prompt "Eres el agente Life OS de Telegram. Lee /Users/jorgeguamis/Desktop/.claude/telegram-routing.md..."
  ```
- **launchd plist:** `~/Library/LaunchAgents/com.jorgeguamis.claude-telegram.plist`
- **Working dir:** `/Users/jorgeguamis/Desktop`
- **Logs:** `~/.claude/logs/claude-telegram.log`, `.err.log`
- **PTY wrap:** `script(1)` necesario porque launchd no provee TTY y Claude Code lo requiere.

Esta es la versión "más simple" — todo Claude Code, sin runtime Python aparte. Más fácil de instalar pero menos capacidades (no hay scheduler nativo, depende de CronCreate de Claude Code).

### 3. Configuración compartida (vive en `~/.claude/`)

Esto es lo que ambos runtimes leen:
- `.claude/agents/*.md` — personas de los 8 agentes (esbirrillo, stark, revo, jorge, many, dots, penny, shakes).
- `.claude/skills/` — skills Claude Code (33).
- `.claude/commands/` — slash commands (28).
- `.claude/context/` — contexto compartido (system.md, helios-routing.md, etc.).
- `.claude/telegram-routing.md` — mapping `chat_id → agente` (ver tabla abajo).
- `.claude/hermes-esbirrillo-prompt.md` — system prompt persona.
- `.claude/config/hermes-crons-v1.json` — definición de 13 crons (morning_brief, daily_tip, pipeline_pulse, evening_checkin, weekly_review, etc.).
- `.claude/config/hermes-cron-routing-map.md` — mapping cron → agente → destino Telegram.
- `~/.claude/memory/working-memory.md` — memoria compartida operativa.
- `~/.claude/memory/tips-log.md` — log para que Dots no repita conceptos en daily_tip.

### 4. Crons (definidos en `hermes-crons-v1.json`)

| Cron | Agente | Schedule | Destino | Phase |
|---|---|---|---|---|
| morning_brief | Esbirrillo | 7:15 daily | Jorge DM | 2 |
| daily_tip | Dots | 8:15 daily | Group Dots | 1 |
| pipeline_pulse | Stark | (ver config) | Group Stark | - |
| circle_digest | Revo | - | Group Revo | - |
| system_health | Many | - | local | - |
| evening_checkin | Jorge | - | Jorge DM | - |
| expense_reminder | Penny | - | Jorge DM | - |
| reading_capture | Dots | - | Group Dots | - |
| weekly_pipeline | Stark | - | Group Stark | - |
| sunday_finance | Penny | - | Group Penny | - |
| weekly_review | Jorge | - | Jorge DM | - |
| weekly_cashflow | Penny | - | Group Penny | - |
| memory_compaction | Esbirrillo | - | local | - |

Cada cron tiene: `key`, `name`, `schedule` (cron syntax), `deliver` (destino), `provider` (kimi-coding, etc.), `model`, `enabled_toolsets` (terminal/file/skills/web/session_search), `prompt` (lo que ejecuta), `workdir`.

### 5. Routing Telegram por chat_id

```
chat_id           agente       persona file
1295530361        Esbirrillo   .claude/agents/esbirrillo.md   (DM directo Jorge)
-5196282334       Jorge        .claude/agents/jorge.md         (group)
-5170932192       Stark        .claude/agents/stark.md         (group)
-5108344284       Revo         .claude/agents/revo.md          (group)
-5109112775       Many         .claude/agents/many.md          (group)
-5246932384       Dots         .claude/agents/dots.md          (group)
-1003892468888    Penny        .claude/agents/penny.md         (group)
```

---

## Acoplamientos al sistema de Jorge

Cosas que están hardcodeadas y hay que parametrizar para hacerlo replicable:

### Paths
- `/Users/jorgeguamis/Desktop` (workdir crons + Claude Code wrapper)
- `/Users/jorgeguamis/.claude/` (config compartida)
- `/Users/jorgeguamis/.hermes/` (Hermes home)
- `/Users/jorgeguamis/.hermes/skills/productivity/google-workspace/scripts/google_api.py` (referenciado en prompts crons)
- `/Users/jorgeguamis/Desktop/Life OS/02. Areas/...` (referenciado en prompts crons)

### chat_ids Telegram
Los 7 chat_ids son específicos de Jorge. Hay que regenerarlos con bot personal del nuevo usuario.

### Prompts crons
Los 13 prompts crons referencian:
- "Jorge" como nombre.
- "360º Consulting", "Revolutia" como negocios.
- DBs Notion específicas.
- Estilos personales de Jorge (formato Telegram, tono).

→ Todos los prompts hay que reescribirlos genéricos parametrizados con `{{user_name}}`, `{{businesses}}`, `{{notion_dbs}}`, `{{tone_preferences}}`.

### Modelos
Jorge usa Kimi K2.6 (`kimi-coding`) en los crons via Hermes. El kit debe ser modelo-agnóstico: el usuario elige (Claude, GPT, Kimi, Llama, etc.) en el setup.

### Working memory
`~/.claude/memory/working-memory.md` está parametrizada por agente, llena de datos Jorge. El kit debe entregar un template vacío con secciones por agente (que la Capa 4 onboarding rellena).

---

## Path a kit (Esbirrillo OS)

### Decisión arquitectónica

**El kit recomienda Hermes-agent como runtime primario.** Razones:
1. Es OSS, mantenido por Nous Research.
2. Capacidades superiores (scheduler nativo, multi-platform, multi-modelo, skill creation).
3. Está pensado para vivir fuera del laptop (VPS/Modal/Docker), lo cual es upsell para futuros clientes.
4. Compatible con `agentskills.io` standard, lo que abre integración con otros sistemas.

**Claude Code + plugin Telegram** = path alternativo "starter" para usuarios que no quieren instalar Python venv extra. Documentado, no recomendado por defecto.

### Estructura en el kit

```
esbirrillo-os/
├── runtime/
│   ├── hermes/                          # path A: Hermes-agent (recomendado)
│   │   ├── INSTALL.md                   # cómo instalar Hermes-agent
│   │   ├── config-template.toml         # config Hermes parametrizable
│   │   ├── crons-template.json          # 13 crons con prompts genéricos
│   │   └── launchd-template.plist       # launchd plist parametrizado
│   └── claude-code-telegram/            # path B: Claude Code lite
│       ├── INSTALL.md
│       ├── claude-telegram.sh.template
│       └── launchd-template.plist
├── .claude/
│   ├── agents/                          # esbirrillo, librarian, techy, reviewer
│   ├── skills/                          # solo genéricas (Capa 2)
│   ├── commands/                        # solo genéricos
│   ├── context/                         # parametrizables
│   │   ├── system.md.template
│   │   ├── telegram-routing.md.template
│   │   └── notion-registry.md.template
│   ├── execution/
│   ├── hooks/
│   └── hermes-esbirrillo-prompt.md.template
├── vault-template/                      # estructura Obsidian vacía
└── bin/
    ├── install.sh                       # entrypoint
    ├── setup-hermes.sh                  # ruta A
    ├── setup-claude-telegram.sh         # ruta B
    ├── setup-mcps.sh
    └── setup-telegram-bot.md            # guía bot personal
```

### Setup steps (lo que el nuevo usuario corre)

1. **Clone esbirrillo-os** en su Mac, en path elegido (default: `~/Desktop/`).
2. **Run `bin/install.sh`:**
   - Detecta si tiene Python 3.12, Claude CLI, etc.
   - Pregunta: ¿Hermes-agent (recomendado) o Claude Code lite?
   - Pregunta: modelo (Claude/GPT/Kimi/etc.)
   - Pregunta: API keys
3. **Si Hermes-agent:**
   - Clone `NousResearch/hermes-agent` en `~/.hermes/hermes-agent/`.
   - Crea venv, instala deps.
   - Genera `~/.hermes/config.toml` desde template.
   - Symlink `.claude/` del kit a `~/.claude/` (o copia, según preferencia).
   - Genera `~/.hermes/crons.json` desde `crons-template.json` con sustitución de variables.
   - Genera plist launchd parametrizado.
   - `launchctl load` el plist.
4. **Run `/setup-wizard`** dentro del Claude Code interactivo.
   - Esta es la Capa 4 del plan: onboarding agéntico que genera context files, agentes propios, working-memory.
5. **Setup Telegram bot personal** (guía paso a paso vía @BotFather).
6. **Validación:** `/helios-healthcheck` → todo verde.

### Lo que se mantiene de Jorge en el kit (limpiable)

- Los 4 agentes core: `esbirrillo`, `dots → librarian`, `many → techy`, `jorge → reviewer`. Limpiar nombres + datos personales.
- Los 13 cron templates: estructura sí, prompts reescritos genéricos. Algunos no aplican (ej: `pipeline_pulse` asume CRM 360º — generalizar a "review pipeline genérico que el usuario configura en Capa 4").
- Routing template: estructura sí, chat_ids vacíos al instalar.
- Skills/commands genéricos (ya identificados en auditoría).

### Lo que NO entra al kit

- Stark, Penny, Revo, Shakes, Monk → Capa 4 los crea custom.
- 50+ skills/commands específicos 360º/Revolutia.
- working-memory de Jorge.
- Context files de negocios de Jorge.
- chat_ids reales.
- API keys.

---

## Próximos pasos concretos

1. **Validar versión Hermes-agent que corre Jorge** y documentar en `INSTALL.md` el setup exacto que reproduce su entorno (Python 3.12, deps, etc.).
2. **Extraer los 13 prompts cron** y reescribirlos genéricos. Reemplazar:
   - `Jorge` → `{{USER_NAME}}`
   - `360º Consulting / Revolutia` → `{{USER_BUSINESSES}}` (lista de objetos {nombre, scope})
   - DBs Notion → `{{NOTION_DB_REGISTRY}}`
   - Paths → `${LIFEOS_ROOT}` / `${HERMES_HOME}` / `${USER_HOME}`
3. **Auditar `~/.claude/memory/working-memory.md` actual** para generar template vacío bien estructurado.
4. **Crear `bin/install.sh`** con la lógica de las 6 etapas de setup arriba.
5. **Probar el path A (Hermes-agent)** en una segunda Mac/VM con un perfil sintético antes de tocar a Juan.
