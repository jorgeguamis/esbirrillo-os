# Architecture — Esbirrillo OS

## 5 capas

```
┌─────────────────────────────────────────────────────────┐
│ Capa 5 — IDENTIDAD                                       │
│ Vacía al instalar. Se llena con onboarding agéntico.    │
│ working-memory, context files, agentes propios usuario  │
└─────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────┐
│ Capa 4 — ONBOARDING AGÉNTICO                             │
│ /setup-wizard, /create-my-agent, /create-context-file   │
│ Skills que entrevistan y construyen Capa 5              │
└─────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────┐
│ Capa 3 — AGENTES CORE GENÉRICOS                          │
│ esbirrillo (orquestador), librarian (knowledge),        │
│ techy (sistema/config), reviewer (selenia/patterns)     │
└─────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────┐
│ Capa 2 — SKILLS Y COMMANDS GENÉRICOS                     │
│ /morning, /reflect, /weekly-review, /process-meeting,   │
│ /capture, /knowledge-digest, /process-youtube-video,    │
│ obsidian-*, helios/selenia infra                        │
└─────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────┐
│ Capa 1 — INFRAESTRUCTURA                                 │
│ Hermes-agent runtime, Claude Code, MCPs, hooks,         │
│ execution scripts, logging, approval queue,             │
│ Telegram bridge, vault structure                        │
└─────────────────────────────────────────────────────────┘
```

## Capa 1 — Infraestructura

### Runtime: dos paths

**Path A — Hermes-agent (recomendado)**
- Repo: `NousResearch/hermes-agent`
- Stack: Python 3.12, venv aislado
- Lanza launchd `ai.hermes.gateway.plist`
- Capacidades: gateway multiplataforma, scheduler nativo, skill creation, multi-modelo, multi-backend (local/Docker/SSH/Modal/Daytona)

**Path B — Claude Code + plugin Telegram (lite)**
- Stack: solo Claude Code CLI con plugin official
- Lanza launchd `com.<user>.claude-telegram.plist`
- Capacidades: chat Telegram, sin scheduler nativo (depende de CronCreate de Claude Code)

El kit instala uno u otro según preferencia del usuario.

### MCPs base (configurables por usuario)

- **Notion** (operativo, CRM, tasks, finanzas)
- **Fireflies** (transcripciones de reuniones)
- **NotebookLM** (knowledge bases con sources)
- **Filesystem** (ops locales seguras)
- **Memory Bank** (persistencia per-project)
- **Sequential Thinking** (razonamiento step-by-step)
- **Playwright** (browser automation, opcional)

Cada usuario configura los MCPs con SUS credenciales. El kit aporta `.mcp.json.template` parametrizable.

### Logging y approval

- `logs/executions/*.jsonl` — events sanitizados
- `logs/telegram/*.jsonl` — señales Telegram
- `logs/approvals/*.jsonl` — approval items
- `logs/selenia/*.jsonl` — runs internos Selenia

L0/L1 se ejecutan automáticamente. L2+ van a approval queue. Reglas en `.claude/context/permissions-matrix.md`.

### Hooks

- `log-context-changes.sh` — registra escrituras en vault
- `validate-tags-after-edit.sh` — valida frontmatter
- SessionEnd — actualiza working-memory

## Capa 2 — Skills y commands genéricos

Skills que entran al kit (lista completa en `audit/report.md`):

**Reviews y reflexión:**
- `weekly-review` `monthly-review` `quarterly-review` `daily-reflection`

**Reuniones y conocimiento:**
- `meeting-processor` `process-youtube-video` `reading-capture` `knowledge-digest`

**Vault (Obsidian):**
- `obsidian-markdown` `obsidian-bases` `json-canvas`
- `tag-note` `retag-atomic-notes` `find-broken-links` `create-hub-index`

**Sistema:**
- `digital-cleanup` `update-dashboard`
- `selenia-nightly-report`

**Automation (opcional):**
- `n8n-*` (5 skills si el usuario usa n8n)

Commands: `/morning` `/reflect` `/process-meeting` `/capture` `/knowledge-digest` `/weekly-review` `/monthly-review` `/quarterly-review` `/digital-cleanup` `/process-inbox` `/route-task` `/helios-healthcheck` `/selenia-nightly` `/telegram-signal` `/approval-item` `/update-context`.

**No entran al kit:** skills/commands específicos del autor (sus negocios, sus clientes, sus DBs).

## Capa 3 — Agentes core (4 universales)

| Agente | Rol | Inspirado en |
|---|---|---|
| **esbirrillo** | Orquestador. Routing, inbox, tareas <2 min. | (idem en sistema fuente) |
| **librarian** | Conocimiento. Capturas, atomic notes, conexiones. | dots |
| **techy** | Sistema, config, scripts, automatización. | many |
| **reviewer** | Patterns, accountability, reviews. | jorge agent |

Estos agentes son universales — aplican a cualquier usuario. Los agentes de dominio (sales, finance, product, copy, etc.) NO entran al kit; los construye Capa 4 según necesidad de cada usuario.

## Capa 4 — Onboarding agéntico

`/setup-wizard` orquesta 7 sub-skills:

1. **`extract-identity`** — entrevista: identidad, valores, perfil, idioma.
2. **`create-my-agent`** — para cada negocio/área del usuario, construye un agente custom (no template).
3. **`setup-context-files`** — Personal.md, North Star.md, Health.md, Learning.md, Finances.md, contextos negocio.
4. **`connect-tools`** — Notion (crea DBs estándar), Google Workspace, Fireflies, Telegram, Calendar.
5. **`frameworks-walkthrough`** — Vivid Vision, Life Map, Identity & Values, Future Self, Principles, Winner Worksheet, Ideal Life Costing.
6. **`seed-working-memory`** — primer ~/.claude/memory/working-memory.md con secciones por agente creado.
7. **`validate-system`** — `/helios-healthcheck` + test Telegram + primer `/morning`.

Output: usuario tiene un sistema configurado para SU realidad sin que el autor del kit haya tocado nada.

## Capa 5 — Identidad

Todo lo que se llena en Capa 4. Vive en:

- `~/.claude/memory/working-memory.md`
- `~/.claude/projects/*/memory/MEMORY.md`
- `Vault/02. Areas/*/[Context].md`
- `Vault/02. Areas/personal/North Star.md`, `memory.md`, `frameworks/*.md`
- `.claude/agents/*.md` (creados por Capa 4)
- `.claude/context/notion-registry.md` (DBs propias)
- `.env` (credenciales — NUNCA versionado)

El upstream del kit no toca esta capa. Updates al kit (`git pull upstream main`) actualizan Capas 1-4 sin tocar Capa 5.

## Modelo de hosting

El usuario elige al instalar:

| Path | Para quién | Coste |
|---|---|---|
| **A. Mac propia** | Default. Validación, freelancers, autónomos. | 0€ |
| **B. Mac mini dedicado** | CEOs que quieren siempre-on serio. | ~700€ una vez |
| **C. VPS Linux + Docker** | Usuarios que viajan o trabajan en múltiples máquinas. | ~20€/mes |
| **D. Modal serverless** | Hibernación cuando idle, costes mínimos. | ~5€/mes idle |

Path A es default v0. Paths B-D documentados pero no automatizados al inicio.

## Modelo de actualización

```
esbirrillo-os (upstream, kit)         user-esbirrillo (fork privado del usuario)
├── runtime/                           ├── runtime/         ← se actualiza con git pull upstream
├── .claude/agents/                    ├── .claude/agents/
│   ├── esbirrillo.md                  │   ├── esbirrillo.md   ← upstream
│   ├── librarian.md                   │   ├── librarian.md    ← upstream
│   ├── techy.md                       │   ├── techy.md        ← upstream
│   ├── reviewer.md                    │   ├── reviewer.md     ← upstream
├── .claude/skills/                    │   ├── ceo-mi-empresa.md   ← creado por Capa 4
├── .claude/commands/                  │   └── coach-personal.md   ← creado por Capa 4
├── vault-template/                    ├── .claude/skills/  ← upstream
└── ...                                ├── Vault propio/    ← privado, nunca upstream
                                       ├── .env             ← privado, nunca upstream
                                       └── working-memory   ← privado, nunca upstream
```

Updates del kit → `git pull upstream main` no toca capas 4-5.

## Privacidad y aislamiento

- Sistema vive en máquina del usuario. Cero sync al autor.
- Credenciales en `.env` local, nunca versionadas.
- Logs JSONL locales, nunca exfiltrados.
- MCPs apuntan a instancias del usuario.
- Si el autor entra a soportar: SSH/screen-share supervisado, NO sync.
- Usuario puede revocar acceso autor en cualquier momento.

## Decisiones tomadas

Ver `docs/DECISIONS.md`.
