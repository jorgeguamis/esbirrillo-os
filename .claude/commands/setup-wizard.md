---
description: First-run onboarding. Interviews you and builds your custom Esbirrillo OS — context files, domain agents, working memory, Notion DBs, frameworks. Run once after install. ~3-5h distributed across 2-3 sessions.
---

Run the master onboarding skill.

## What this does

Walks you through 7 stages that turn the kit (Capa 1-3) into a system configured for your reality (Capa 4 generating Capa 5):

1. **extract-identity** (45-60 min) — Who you are, what you do, where you're going, your patterns.
2. **create-my-agent** (15 min × N) — Builds custom agents for each business/domain.
3. **setup-context-files** (60-90 min) — Generates context files (Personal, business, health, learning, finances).
4. **connect-tools** (30-60 min) — Connects Notion, Google Workspace, Fireflies, Telegram.
5. **frameworks-walkthrough** (60-90 min) — Vivid Vision, Life Map, Identity & Values, Future Self, Principles.
6. **seed-working-memory** (15 min) — Initial working memory per agent.
7. **validate-system** (15 min) — Healthcheck + Telegram round-trip + first /morning.

## How to use

```
/setup-wizard           # start or resume
/setup-wizard --review  # re-run a specific stage to refine
/setup-wizard --status  # show progress + remaining stages
```

State is tracked in `~/.claude/memory/setup-wizard-state.json`. You can pause between any two stages and resume later.

## When to invoke

- **Once after install** (first run).
- After major life changes (new business, role pivot, fiscal residence change).
- Re-running individual stages with `--review` if your situation evolves.

## Tone

Conversational, deep when it matters, efficient when context is already there. Honest if answers sound performative.

## Outputs

After full run:
- `~/.claude/memory/working-memory.md` (seeded)
- `~/.claude/memory/setup-completed.md` (summary)
- `02. Areas/personal/Personal.md`
- `02. Areas/personal/North Star.md`
- `02. Areas/personal/memory.md` (initial patterns)
- `02. Areas/personal/frameworks/*.md` (5-8 framework files)
- `02. Areas/{business}/Context.md` × N
- `02. Areas/{health|learning|finances}/*.md`
- `.claude/agents/{custom}.md` × N domain agents
- `.claude/context/notion-registry.md` (real DB IDs)
- `.claude/context/system.md` (filled from template)
- `.claude/context/telegram-routing.md` (real chat_ids)

## Prerequisites

- `bin/install.sh` ran successfully
- Anthropic API key configured
- Vault path exists (or user opted out of Obsidian)
- Notion + Telegram bot ready to be created/connected

## Safety

- Anything destructive requires explicit confirmation.
- Notion DB creation can be skipped per-DB if user prefers existing ones.
- Telegram bot setup is opt-in (user creates via @BotFather, system reads token).
- `.env` is git-ignored — credentials never leave the user's machine.

## Output format

The wizard runs in conversational mode. Each stage produces files (markdown + JSON state). At the end, the user has a working system and a summary file in `~/.claude/memory/setup-completed.md`.
