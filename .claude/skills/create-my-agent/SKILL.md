---
description: Stage 2 of /setup-wizard. For each business or domain area the user has, interviews them and constructs a custom agent prompt (.claude/agents/{slug}.md). Not a template fill — a real prompt designed for their specific role, voice, and sources.
---

# create-my-agent — Construye TUS agentes

Stage 2 of the wizard. ~15 minutes per agent. Run once per business/area the user identified in Stage 1.

## Goal

Each user has different agents than every other user. A solo consultant has a "client manager" agent. A SaaS CEO has a "product agent" and a "fundraising agent". A community-driven creator has a "audience agent". This skill **constructs the agent**, not from a template, but from a focused interview about scope, voice, and sources.

## When to invoke

After Stage 1 (`extract-identity`). The wizard reads the `businesses` list from `setup-wizard-state.json` and invokes this skill **once per business/domain**.

For each domain, this skill produces one file: `${LIFEOS_ROOT}/.claude/agents/{slug}.md`.

## Tone

- The user has just spent 45 min telling you about their world. Don't ask redundant questions.
- Reference their previous answers explicitly: "Antes mencionaste que en {{business_X}} eres CEO y que la métrica que te importa es ARR. Voy a construir un agente para esto. Confírmame algunas cosas."

## Protocol per agent

### Step 1 — Confirmar contexto del dominio

Lee de state: nombre, rol, modelo, métrica, % tiempo. Confirma con el usuario:

```
"Voy a crear un agente para {{business_name}}. Tengo de Stage 1:
- Tu rol: {{role}}
- Modelo: {{revenue_model}}
- Métrica clave: {{key_metric}}
- Tiempo asignado: {{time_pct}}%
¿Algo que ajustar antes de seguir?"
```

### Step 2 — Scope del agente

```
1. ¿Cuáles son las decisiones recurrentes que tomas en {{business_name}}?
   (ejemplo: "qué cliente atender primero", "qué precio poner", "qué
   contratar / despedir", "qué deal aceptar"). Lista 5–10.

2. ¿Qué propones tú mismo y qué te gustaría que el agente proponga primero?
   (ejemplo: "yo decido pricing, pero quiero que el agente me proponga
   3 opciones razonadas").

3. ¿Qué cosas debe el agente solo informar (sin opinar)?
   (ejemplo: "lista de tareas overdue, KPIs semanales").

4. ¿Qué cosas el agente NO debe hacer aunque pueda? (líneas rojas).

5. ¿Cuánta autonomía? (L0–L4, default L0–L1).
```

### Step 3 — Fuentes del agente

```
1. ¿Qué fuentes consulta este agente para tener contexto?
   - Notion DBs específicas? Lista.
   - Fireflies (qué meetings? todos los del business o filtro?)
   - Calendar (qué calendar account?)
   - Vault (qué carpeta — `02. Areas/{this_business}/`?)
   - Email (qué cuenta? ¿solo lectura?)
   - APIs externas (Stripe, Linear, Slack, otra?)
   - Otros documentos / dashboards.

2. ¿Hay un "playbook" o documento maestro que define cómo opera este negocio
   en tu cabeza? Si existe, ¿dónde vive? Lo enlazaremos.

3. ¿Hay un equipo / partners / contactos clave para este negocio? Lista
   con rol y frecuencia de comunicación.
```

### Step 4 — Voz del agente

```
1. ¿Cómo quieres que te hable este agente? (formal, directo, con humor,
   técnico, comercial). Da un ejemplo de cómo te respondería al pedirle
   "¿qué hago hoy en {{business_name}}?".

2. ¿Tiene un nombre/personalidad este agente? (puede ser un nombre real
   tipo un nombre propio, o solo descriptivo tipo "ceo-saas-acme"). Importa porque
   será el chat_id Telegram que recibirá los mensajes.

3. ¿Idioma del agente? Default = idioma del usuario, pero quizá tu equipo
   de un país requiere inglés.

4. Tres palabras que NUNCA debe usar (jerga corporativa que detestas).

5. Tres palabras / frases que sí te resuenan.
```

### Step 5 — Skills disponibles para este agente

Lista las skills genéricas del kit y pregunta cuáles aplican:

```
"Para este agente, ¿cuáles de estas skills tendrían sentido?
- meeting-processor (procesar reuniones del business)
- weekly-review (review semanal específico del business)
- monthly-review (review mensual)
- knowledge-digest (digest de conocimiento del sector)
- selenia-nightly-report (revisión nocturna)
- update-dashboard (refrescar dashboard del business)
- Otras (custom skills que vas a necesitar — captura como roadmap)"
```

Captura: skills_active[], skills_to_build[].

### Step 6 — Generar el agente

A partir de toda la info, construye el archivo `${LIFEOS_ROOT}/.claude/agents/{slug}.md` con esta estructura:

```markdown
# {{agent_display_name}} — {{role_descriptor}}

Eres **{{agent_name}}**, {{role_oneliner}}.

## Rol
{{scope_summary_in_prose}}

## Personalidad
- {{trait_1}}
- {{trait_2}}
- {{trait_3}}
- Idioma: {{agent_language}}.
- Palabras a evitar: {{avoid_words}}.

## Qué decide / propone / informa
**Decide tú:** {{user_decisions}}
**Propone (con razonamiento):** {{agent_proposes}}
**Informa solo:** {{agent_informs}}

## Líneas rojas
- {{red_line_1}}
- {{red_line_2}}

## Permisos por defecto
{{permission_default}}

## Fuentes que consulta

### Notion DBs
{{for db in notion_dbs}}
- `{{db.name}}` (id `{{db.data_source_id}}`)
{{/for}}

### Vault
- `${LIFEOS_ROOT}/${VAULT_NAME}/02. Areas/{{business_slug}}/`

### Calendar
- {{calendar_id}}

### Fireflies
- Filter: {{fireflies_filter}}

### Otros
{{other_sources}}

## Equipo y contactos clave
{{key_contacts_table}}

## Métricas clave
{{key_metrics}}

## Skills habilitadas
{{enabled_skills}}

## Skills pendientes de crear
{{skills_to_build}}

## Working memory
Lee `${USER_CLAUDE_DIR}/memory/working-memory.md` sección **{{agent_name}}** antes de operar.
```

### Step 7 — Validar

Antes de cerrar, mostrar al usuario el agente generado y preguntar:
> "Aquí está {{agent_name}}. ¿Te suena? ¿Algo a ajustar?"

Si confirma → guardar archivo, marcar agente como creado.
Si pide ajustes → iterar hasta confirmación.

## Step 8 — Registrar en system

1. Append agent name a `setup-wizard-state.json` `user_summary.domain_agents[]`.
2. Append a `${LIFEOS_ROOT}/.claude/context/system.md` en la sección "Agentes de dominio".
3. Si hay routing keywords claros, append a `routing_rules.json` (con `permission` que el usuario confirmó).

## Bucle

Repetir Step 1–8 para cada business/area en `state.businesses`. El usuario puede saltar áreas que no quiere agente para ahora — quedan registradas como "to do" en state.

## Output final del stage

- N archivos `${LIFEOS_ROOT}/.claude/agents/{slug}.md`
- `system.md` actualizado con tabla de domain agents
- `routing_rules.json` actualizado con N entradas nuevas
- `state.json` con `current_stage = "setup-context-files"` y `domain_agents` poblado

## Self-annealing

| Date | Issue/Learning | Resolution |
|---|---|---|
