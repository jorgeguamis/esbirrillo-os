---
description: Master skill that walks the user through Esbirrillo OS first-run setup. Interviews them and builds Capa 5 (identity layer) from scratch — context files, domain agents, working memory, Notion DBs, frameworks. Run once after install.
---

# setup-wizard — Onboarding agéntico

This is the **heart of Esbirrillo OS**. When a new user installs the kit, they run `/setup-wizard` and the system interviews them to build their identity layer (Capa 5). At the end, the user has a system configured for their reality, with their agents, their context files, their Notion DBs, their working memory.

## When to run

- Once after first install.
- After major life changes (new business, new role, new fiscal residence) — runs in "update" mode.

## Time required

3–5 hours total, distributed across 2–3 sessions. Do **not** try to complete in one sitting — the depth of the answers matters more than speed.

## Orchestration

This skill orchestrates 7 sub-skills with checkpoints between them. The user can pause/resume between sub-skills. State is tracked in `${USER_CLAUDE_DIR}/memory/setup-wizard-state.json`.

```
/setup-wizard
   │
   ├─ STAGE 1: extract-identity        (45–60 min)
   │       ↓ generates: Personal.md (draft), identity context
   ├─ STAGE 2: create-my-agent         (15 min × N businesses/areas)
   │       ↓ generates: .claude/agents/{name}.md per domain
   ├─ STAGE 3: setup-context-files     (60–90 min)
   │       ↓ generates: 02. Areas/*/Context.md
   ├─ STAGE 4: connect-tools           (30–60 min)
   │       ↓ creates Notion DBs, registers IDs, validates Calendar/Fireflies
   ├─ STAGE 5: frameworks-walkthrough  (60–90 min)
   │       ↓ generates: North Star.md, Vivid Vision, Life Map, Identity, Future Self
   ├─ STAGE 6: seed-working-memory     (15 min)
   │       ↓ generates: ~/.claude/memory/working-memory.md
   └─ STAGE 7: validate-system         (15 min)
           ↓ runs /helios-healthcheck, tests Telegram, generates first /morning
```

## State machine

The skill maintains state in `setup-wizard-state.json`:

```json
{
  "started_at": "2026-05-07T10:00:00Z",
  "current_stage": "extract-identity",
  "completed_stages": [],
  "interrupted_at": null,
  "user_summary": {
    "name": null,
    "language": null,
    "businesses": [],
    "patterns": []
  }
}
```

Each sub-skill updates this file with its own outputs and marks itself complete.

## Process

### Pre-flight (do before stage 1)

1. **Welcome message:**
   ```
   Bienvenido a Esbirrillo OS. Voy a entrevistarte durante las próximas
   3–5 horas (puedes pausar cuando quieras). Al final, este sistema te
   conocerá tan bien como tú mismo, y podrá ayudarte a tomar decisiones,
   procesar reuniones, y mantenerte alineado con lo que importa.

   Vamos en 7 etapas. ¿Empezamos?
   ```

2. **Check for existing state:**
   - If `setup-wizard-state.json` exists → ask "Veo que empezaste el setup el {{started_at}}, ¿continuar desde {{current_stage}}?"
   - If not → create fresh state file.

3. **Confirm prereqs:**
   - Check that `bin/install.sh` was run successfully (look for `.installed` marker).
   - Check that user has Claude API key configured.
   - Check that vault path exists.

### Stage transitions

Between each stage:

1. Save state (`current_stage` advances).
2. Show summary of what was generated.
3. Ask: "¿Continúas con la siguiente etapa o paramos aquí?"
4. If pause → exit cleanly, log resumption point.

### Final delivery

After Stage 7:

1. Write `setup-completed.md` to `${USER_CLAUDE_DIR}/memory/` with full summary.
2. Show the user:
   - Total time invested
   - Agents created
   - Context files generated
   - Notion DBs connected
   - Frameworks completed
   - Next steps (run `/morning` tomorrow, talk to Esbirrillo on Telegram)
3. Suggest a 1-week feedback loop: "En 7 días, ejecuta `/setup-wizard --review` para refinar lo que descubras usando el sistema."

## Tone for the entire wizard

- **Conversacional, no formulario.** No leas listas mecánicamente — adapta cada pregunta al contexto previo.
- **Profundo cuando importa.** "¿Por qué eso?" cuando una respuesta es superficial.
- **Eficiente cuando ya hay info.** Si el usuario ya dijo algo, no lo preguntes de nuevo.
- **Honesto.** Si una respuesta del usuario suena performativa, refléjalo: "Eso suena a lo que crees que deberías decir, ¿es lo que realmente piensas?"
- **Idioma:** detectar en stage 1 y mantener.

## Sub-skill invocation

To invoke a sub-skill, the master loads its `SKILL.md` and follows its protocol. Each sub-skill is also accessible standalone via slash command (`/extract-identity`, `/create-my-agent`, etc.) for re-runs.

## Outputs

After full run:
- `${LIFEOS_ROOT}/${VAULT_NAME}/02. Areas/personal/Personal.md`
- `${LIFEOS_ROOT}/${VAULT_NAME}/02. Areas/personal/North Star.md`
- `${LIFEOS_ROOT}/${VAULT_NAME}/02. Areas/personal/memory.md` (initial patterns)
- `${LIFEOS_ROOT}/${VAULT_NAME}/02. Areas/personal/frameworks/Vivid Vision.md`
- `${LIFEOS_ROOT}/${VAULT_NAME}/02. Areas/personal/frameworks/Life Map.md`
- `${LIFEOS_ROOT}/${VAULT_NAME}/02. Areas/personal/frameworks/Identity and Values.md`
- `${LIFEOS_ROOT}/${VAULT_NAME}/02. Areas/personal/frameworks/Future Self.md`
- `${LIFEOS_ROOT}/${VAULT_NAME}/02. Areas/{business_slug}/Context.md` × N
- `${LIFEOS_ROOT}/.claude/agents/{custom-agent}.md` × N
- `${LIFEOS_ROOT}/.claude/context/notion-registry.md` (IDs registered)
- `${LIFEOS_ROOT}/.claude/context/system.md` (filled from template)
- `${USER_CLAUDE_DIR}/memory/working-memory.md` (seeded)
- `${USER_CLAUDE_DIR}/memory/setup-completed.md` (summary)

## Self-annealing

Track in this section any observations the wizard accumulates while running.

| Date | Issue/Learning | Resolution |
|---|---|---|

## Known Issues

- Wizard is non-interactive in cron contexts — only runs in CLI/Claude Code interactive sessions.
- Stage 5 (frameworks) takes 60–90 min and users frequently want to split it across multiple days. Honor the resume logic.
- Stage 4 (connect-tools) requires Notion integration to be authorized first. If MCP fails, prompt the user to set it up before retrying.
