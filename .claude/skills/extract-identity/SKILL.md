---
description: Stage 1 of /setup-wizard. Interviews the user about identity, role, businesses, north star, patterns, stack, team, and confidentiality preferences. Generates first draft of Personal.md and identity sections of working memory.
---

# extract-identity — Quién eres

Stage 1 of the onboarding wizard. ~45–60 minutes. The depth of these answers is the foundation of everything else — don't rush.

## Goal

By the end of this stage, the system has a **rich first-person model** of the user: who they are, what they do, where they're going, what they avoid, and what data they want kept confidential.

## Tone

- Conversación natural, **no formulario**.
- Si una respuesta es genérica ("quiero ser libre", "quiero impacto"), profundiza con "¿Qué significa eso para ti, concretamente?"
- Si el usuario evita una pregunta, regístralo y vuelve más tarde.
- Idioma: detecta en la primera pregunta y mantén.

## Protocol

### Block 1 — Identidad básica (10 min)

```
1. Nombre completo y cómo prefieres que te llame el sistema.
2. Edad y dónde vives (ciudad, país).
3. Idioma principal (¿cuál? ¿quieres que el sistema te hable solo en este idioma o multilingüe?).
4. Estado vital: ¿pareja? ¿hijos? ¿familia cerca? (sin profundizar — solo contexto).
5. Tu estilo profesional en 1 frase: ¿eres más estratégico, operativo, comercial, técnico, creativo?
6. Si has hecho algún test de personalidad reciente (MBTI, DISC, Big5, Eneagrama), comparte el resultado.
```

**Captura:** name, language, location, family_status (high level), professional_style, personality_profile.

### Block 2 — Roles y negocios (15–20 min)

```
1. ¿En qué trabajas actualmente? Quiero la lista completa, incluso si tienes
   varios proyectos paralelos. Por cada uno:
   - Nombre del proyecto/empresa.
   - Tu rol exacto (CEO, Director, Founder, Empleado, Freelance, Consultor).
   - Modelo de ingresos (proyectos puntuales, retainer, salario, equity, mixto).
   - ¿Qué % de tu tiempo le dedicas?
   - ¿Cuánto te paga (anualizado)?
   - ¿Cuál es la métrica clave que importa? (ARR, clientes activos, alumnos, downloads...)

2. ¿Tienes inversiones, equity en otras empresas, o ingresos pasivos
   relevantes? (no necesito cifras exactas — qué tipo y peso aproximado).

3. ¿Hay algún proyecto/negocio inminente que vas a empezar en 0–3 meses?
   (incluir aunque aún no haya facturado).
```

**Captura:** businesses (list of objects: name, role, revenue_model, time_pct, ann_revenue, key_metric, status), investments_summary, upcoming_projects.

### Block 3 — Norte y motivación (10 min)

```
1. Si visualizas tu vida en 1 año (mismo mes que hoy, +1 año), ¿cómo es?
   Trabajo, dinero, dónde vives, con quién, cómo te sientes. Sé concreto.

2. Igual con 3 años.

3. Y con 10 años.

4. ¿Qué objetivo de ingreso anual marcarías como tu "NOR" — Number Of
   Reference — para 2026? (lo que te daría tranquilidad o salto, no el techo).

5. ¿Hay algún objetivo no monetario igual de importante para ti este año?
   (hábito instalado, cambio de país, relación, salud, aprendizaje).
```

**Captura:** north_star (1y/3y/10y), revenue_target_2026, non_monetary_goals.

### Block 4 — Patrones (10–15 min) ⚠️ Bloque sensible

> Aquí busca honestidad, no respuestas socialmente correctas.

```
1. ¿En qué procrastinas más? (sin filtros — qué cosa intentas evitar más).
2. ¿Bajo qué condiciones rindes mejor? (cuándo, dónde, con qué estímulos).
3. ¿Bajo qué condiciones rindes peor?
4. ¿Hay algún patrón de comportamiento tuyo que te frustra y se repite
   cada pocos meses? (ejemplo: "siempre acabo dropeando el gym", "siempre
   dejo decisiones difíciles 6 semanas").
5. ¿Hay alguna decisión grande que llevas postergando >3 meses? (no es
   prying — el sistema necesita saber dónde están tus zonas de fricción).
6. ¿Cómo prefieres que el sistema te hable cuando detecte uno de estos
   patrones? (suave, directo, brutal).
```

**Captura:** patterns (list of {name, trigger, truth, antidote, severity}), avoidance_decisions, feedback_style_preference.

### Block 5 — Stack y comunicación (5 min)

```
1. ¿Qué herramientas usas en tu día a día?
   - Calendario(s) y cuántas cuentas Google tienes
   - Email principal y secundarios
   - Notion ¿sí/no? — si sí, ¿cuántos workspaces?
   - Fireflies (o equivalente para reuniones)
   - Slack / Discord / Telegram / WhatsApp para qué cosa
   - Vault de notas (Obsidian, Notion docs, Apple Notes)
2. ¿Cuál es tu canal de comunicación preferido para que el sistema te
   hable? (Telegram, CLI, Discord, WhatsApp).
3. ¿Quieres que el sistema te hable de forma proactiva (morning brief,
   evening checkin, alertas) o reactiva (solo cuando preguntas)?
```

**Captura:** stack (calendars[], emails[], notion[], fireflies, comms[], vault), comms_channel, autonomy_pref.

### Block 6 — Equipo y relaciones clave (5 min)

```
1. Lista de personas con las que tienes una relación profesional directa
   activa (socios, partners, key clients, manager, equipo). Por cada uno:
   - Nombre
   - Rol/relación
   - Frecuencia de contacto (diario, semanal, mensual, ad hoc)

2. ¿Hay alguien con quien tengas una conversación recurrente compleja
   (negociación, dispute, partnership en formación)?

3. ¿Hay personas a las que el sistema NO debe registrar/loguear menciones?
   (info confidencial, personas en proceso legal, exparejas, etc.).
```

**Captura:** key_relationships (list of {name, role, cadence}), active_negotiations, redact_list.

### Block 7 — Confidencialidad (5 min)

```
1. ¿Qué tipos de información NO quieres que se loguee aunque pase por el
   sistema? (transcripciones de terapia, info legal sensible, conversaciones
   con abogados, salud médica detallada, etc.).

2. ¿Hay carpetas en tu Mac que el sistema NO debe leer aunque las pueda ver?

3. ¿Aceptas que los logs JSONL contengan resúmenes de tus conversaciones
   con el sistema? (necesarios para Selenia + self-annealing — pero puedes
   decir no y el sistema operará sin memoria persistente).

4. ¿Quién más, además de ti, debería poder leer este sistema? (solo tú es
   la respuesta default; alguna persona específica puede ser válida).
```

**Captura:** redact_topics, redact_paths, logging_consent (bool), shared_access (list).

## Output

### File 1: `${LIFEOS_ROOT}/${VAULT_NAME}/02. Areas/personal/Personal.md`

Markdown con la estructura:

```markdown
---
tags:
  - type/context
  - area/personal
created: {{date:DD-MM-YYYY}}
updated: {{date:DD-MM-YYYY}}
---

# Personal

## Quién soy
{{name}}, {{age}}, {{location}}. {{language}}, {{professional_style}}.
Personalidad: {{personality_profile}}.

## Roles activos
{{roles_summary}}

## Norte (síntesis)
- 1 año: {{north_star_1y_summary}}
- 3 años: {{north_star_3y_summary}}
- 10 años: {{north_star_10y_summary}}
- NOR 2026: {{revenue_target_2026}}

## Patrones conocidos
{{patterns_summary_with_antidotes}}

## Estado actual
- Energía base: {{current_energy_baseline}}
- Foco trimestral: {{current_quarter_focus}}
- Decisiones pendientes: {{pending_decisions}}

## Comunicación con el sistema
- Canal preferido: {{comms_channel}}
- Modo: {{autonomy_pref}}
- Estilo de feedback: {{feedback_style}}

## Confidencialidad
- No loguear: {{redact_topics}}
- Acceso adicional: {{shared_access}}
```

### File 2: `${USER_CLAUDE_DIR}/memory/setup-wizard-state.json` (update)

Agrega bajo `user_summary`:
```json
{
  "name": "...",
  "language": "...",
  "businesses": [...],
  "patterns": [...],
  "stack": {...},
  "redact_topics": [...]
}
```

### File 3: `${LIFEOS_ROOT}/${VAULT_NAME}/02. Areas/personal/memory.md` (initial patterns seed)

```markdown
# Memory — Patterns tracking

> Patrones detectados. Uno = evento. Tres = patrón.

## Patrones conocidos (extraídos en setup)

{{for each pattern}}
### {{pattern_name}}
- **Severidad:** {{severity}}
- **Trigger:** {{trigger}}
- **Verdad:** {{truth}}
- **Antídoto:** {{antidote}}
- **Detectado:** {{date}}
{{/for}}

## Historial de detecciones (rellena en uso)
```

## Confirmación final

Al cerrar el bloque, muestra al usuario un resumen de lo capturado y pregunta:
> "¿Algo importante que falte? ¿Algo que quieras corregir antes de pasar a Stage 2?"

Si el usuario corrige algo, edita el output. Si añade nueva info, ampliar.

## Self-annealing

| Date | Issue/Learning | Resolution |
|---|---|---|
