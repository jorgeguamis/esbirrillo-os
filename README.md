# Esbirrillo OS

Sistema agéntico personal replicable. Un orquestador siempre-on en Telegram + skills + agentes + vault, que se autoconfigura para cada usuario mediante onboarding agéntico.

> **Status:** v0 en construcción. Primer caso 0: Juan Santacruz (CEO Revolutia), ETA 8 semanas.

## Qué es esto

Tu propio Jarvis: un orquestador (Esbirrillo) en Telegram que entiende tu rol, tus negocios, tus prioridades, tu agenda. Puedes hablarle como hablarías con un asistente humano. Procesa tus reuniones, prepara tus reviews, captura tu conocimiento, te recuerda lo que toca cada día.

No es un producto SaaS. Es un kit que se instala en tu Mac, lee tu vault de Obsidian (opcional), conecta a tu Notion/Google/Fireflies, y construye un asistente con tu identidad — no con la mía.

## Arquitectura (5 capas)

```
Capa 5 — Identidad        ← vacía al instalar, se rellena en onboarding
Capa 4 — Onboarding       ← /setup-wizard entrevista al usuario y construye Capa 5
Capa 3 — Agentes core     ← esbirrillo, librarian, techy, reviewer (universales)
Capa 2 — Skills/commands  ← /morning, /reflect, /weekly-review, /process-meeting...
Capa 1 — Infraestructura  ← Hermes-agent runtime + MCPs + hooks + Claude Code
```

Ver [ARCHITECTURE.md](./ARCHITECTURE.md) para el detalle completo.

## Stack

- **Runtime primario:** [Hermes-agent](https://github.com/NousResearch/hermes-agent) (Nous Research, MIT). Gateway multiplataforma, scheduler de crons, multi-modelo.
- **Runtime alternativo "lite":** Claude Code + plugin Telegram official.
- **Modelo:** agnóstico (Claude / GPT / Kimi / Llama / Nous Portal / OpenRouter). Eliges en setup.
- **Comunicación:** Telegram bot personal (Discord/Slack/WhatsApp opcional vía Hermes).
- **Vault:** Obsidian (opcional). Operativo: Notion. Reuniones: Fireflies.
- **MCPs base:** Notion, Fireflies, NotebookLM, Filesystem, Memory Bank.

## Instalación rápida

```bash
git clone <repo> ~/Desktop/esbirrillo-os
cd ~/Desktop/esbirrillo-os
./bin/install.sh
```

El instalador te pregunta runtime, modelo, credenciales y arranca. Después corres `/setup-wizard` dentro de Claude Code para que el sistema te entreviste y construya tus contextos, agentes y working memory.

Setup completo: ~3-5h distribuidas en sesiones.

Ver [docs/INSTALL.md](./docs/INSTALL.md) para detalles.

## Estructura del repo

```
esbirrillo-os/
├── runtime/
│   ├── hermes/                # path A: Hermes-agent setup (recomendado)
│   └── claude-code-telegram/  # path B: Claude Code lite
├── .claude/                   # capa 1+2+3 limpia, replicable
│   ├── agents/                # 4 agentes core genéricos
│   ├── skills/                # solo skills genéricas
│   ├── commands/              # solo commands genéricos
│   ├── context/               # templates parametrizables
│   ├── execution/             # scripts deterministas (DOE)
│   ├── hooks/                 # hooks Claude Code
│   └── config/                # crons templates
├── vault-template/            # estructura Obsidian vacía
├── bin/                       # scripts de instalación
├── docs/                      # INSTALL, TROUBLESHOOTING, DECISIONS
└── audit/                     # auditoría del sistema fuente (autor del kit)
```

## Cómo funciona el onboarding agéntico

El kit no entrega "los agentes del autor". Entrega los 4 agentes universales (Capa 3) y un agente especial: el **setup-wizard**, que te entrevista para construir TUS agentes propios.

Si eres CEO de una edtech, el setup-wizard creará un agente "ceo-mi-empresa" con tu scope, voz y fuentes. Si eres consultor freelance, creará un "client-manager" diferente. No reciclas los agentes del autor del kit.

## Privacidad

Todo vive en tu Mac. Logs locales en JSONL. Credenciales en `.env` no versionado. Los repos se hostean en cuentas a tu nombre. Nada se sincroniza al sistema del autor.

## Licencia

TBD. Probablemente MIT (alineado con Hermes-agent). El contenido del kit (skills, prompts, templates) sí es del autor.

## Roadmap

- v0 (sem 1-3): kit base + onboarding agéntico testeado con perfil sintético.
- v0.1 (sem 4-8): caso 0 con Juan Santacruz.
- v0.5 (mes 3-6): caso 1+ (post-intro al tío).
- v1 (mes 6+): producto vendible — onboarding pulido, multi-stack, casos públicos.
