---
description: Stage 6 of /setup-wizard. Generates ~/.claude/memory/working-memory.md with sections per agent (core + domain). Each section is seeded with current state from Stages 1-5. ~15 minutes.
---

# seed-working-memory — Memoria operativa inicial

Stage 6. ~15 minutes. Genera el archivo de memoria operativa que TODOS los agentes leen al arrancar cualquier conversación o cron.

## Goal

Working memory es la **memoria de corto plazo** del sistema: el estado operativo actual que cambia semanalmente. Mientras los context files son la "memoria semántica" (quién soy, qué importa), working memory es la "memoria episódica" (qué está pasando esta semana, qué decisiones penden).

## File location

`${USER_CLAUDE_DIR}/memory/working-memory.md`

## Structure

```markdown
# Working Memory — {{user_firstname}}

> Memoria operativa compartida. SessionEnd hook la actualiza. Cada agente
> mantiene su sección. Re-leer entera antes de operar.

> Última actualización: {{date}}
> Compactación pendiente: nightly cron

---

## Coordinación cross-agente

> Prioridades de la semana, decisiones pendientes que tocan a varios
> agentes, blockers transversales.

### Esta semana ({{week}})
- Top focus: {{from Personal.md current_quarter_focus}}
- Decisiones pendientes:
  - {{from Stage 1 avoidance_decisions}}
- Blockers:
  - {{...}}

### Patrones activos esta semana
{{from memory.md — active patterns to watch}}

---

## Esbirrillo (orquestador)

### Inbox abierto
- {{...}}

### Routing notes
- {{...}}

### Tareas <2 min pendientes
- {{...}}

---

## Reviewer (coach/accountability)

### Patrones detectados esta semana
{{from active patterns}}

### Decisiones que el usuario ha postergado
- {{...}}

### Promesas pendientes (a sí mismo, en daily notes)
- {{...}}

### Energía esta semana
- Promedio: {{...}}/10
- Trend: {{up/flat/down}}

---

## Librarian (conocimiento)

### Temas activos de estudio
{{from Learning.md}}

### Lectura activa
{{from Learning.md}}

### Atomic notes pendientes de procesar (en `00. Inbox/`)
- {{...}}

### Tips dados (no repetir)
- {{...}}

---

## Techy (sistema)

### Healthcheck status
- Última run: {{...}}
- Servicios verde/rojo: {{...}}

### Crons activos
{{from Hermes config or Claude Code crons}}

### Pendientes técnicos
- {{...}}

---

{{for each domain agent created in Stage 2}}

## {{agent_name}}

### Estado actual del negocio
{{from {{business}}/Context.md highlights}}

### Pipeline / proyectos activos
{{from Context.md}}

### Decisiones pendientes en este dominio
- {{...}}

### Métricas última semana
- {{key_metric}}: {{value}}

### Stuck deals / fricciones
- {{...}}

{{/for}}

---

## Fechas y dates clave

> Compromisos y deadlines críticos próximos 30 días.

| Fecha | Item | Owner | Tipo |
|---|---|---|---|
| {{date}} | {{...}} | {{agent}} | deadline / decision / payment |

---

## Reglas para los agentes

1. **Lee esta memoria antes de cada respuesta operativa.**
2. **Actualízala** cuando:
   - Un cron genera datos nuevos.
   - El usuario te da info relevante (ej: "hoy gasté 50€ en X").
   - Completas una tarea que cambia el estado.
   - Al final de una conversación significativa.
3. **Mantén cada sección concisa** (~5-10 líneas). Elimina info obsoleta.
4. **No dupliques** info que vive en context files o `memory.md`. Aquí solo "estado de la semana".
5. **Compactación nightly**: Selenia comprime esta memoria automáticamente.
```

## Process

1. **Read all artifacts from Stages 1–5:**
   - `setup-wizard-state.json`
   - `02. Areas/personal/Personal.md`
   - `02. Areas/personal/memory.md`
   - `02. Areas/personal/North Star.md`
   - All `02. Areas/{business}/Context.md`
   - All `02. Areas/{health|learning|finances}/*.md`

2. **Synthesize per section:**
   - Para cada agente core (esbirrillo, reviewer, librarian, techy), generar sección con seed inicial.
   - Para cada domain agent, generar sección con datos del business.
   - "Coordinación cross-agente" pone top focus de Personal.md.

3. **Show the user the generated file:**
   ```
   "He generado tu working memory inicial. Léela. Si algo no te suena
   actual o real, edítala a mano. Esto se actualiza solo a partir de
   ahora con SessionEnd hook + Selenia."
   ```

4. **Configure SessionEnd hook:**
   - Verificar que el hook está en `settings.json`.
   - El hook llama a una skill `update-working-memory` que añade resúmenes al final de la sesión.

## Output

- `${USER_CLAUDE_DIR}/memory/working-memory.md` populado.
- `${USER_CLAUDE_DIR}/memory/tips-log.md` (vacío con header) — usado por `librarian` para no repetir conceptos.
- `setup-wizard-state.json` con `current_stage = "validate-system"`.

## Self-annealing

| Date | Issue/Learning | Resolution |
|---|---|---|
