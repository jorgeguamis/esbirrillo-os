---
description: Stage 3 of /setup-wizard. Generates the context files (Personal, business, health, learning, finances) that agents read before producing output. Each context file is the "AI memory" for that life area. ~60-90 minutes.
---

# setup-context-files — Memoria del sistema por área

Stage 3 of the wizard. ~60–90 minutes. Generates one context file per life area. Each agent reads its corresponding context before generating any output.

## Goal

Context files are **the AI memory** of each life area. They contain priorities, current state, recent wins/blockers, energy patterns, strategic goals. When an agent generates output (daily brief, review, sales prep), it **first reads the relevant context file**.

## Why this matters

Without good context files, the system is generic. With good context files, it speaks your language and knows what matters to you right now.

## Files generated

| Area | File | Owner agent |
|---|---|---|
| Personal | `02. Areas/personal/Personal.md` | `reviewer` |
| Each business | `02. Areas/{business_slug}/Context.md` | domain agent (created in Stage 2) |
| Health | `02. Areas/health/Health.md` | `reviewer` |
| Learning | `02. Areas/learning/Learning.md` | `librarian` |
| Finances | `02. Areas/finances/Finances.md` | finance domain agent (or `reviewer`) |

## Tone

- Asume que el usuario ya completó Stage 1. Referencia sus respuestas. No repitas preguntas básicas.
- Profundiza en presente: el context file refleja "dónde estás AHORA", no "dónde quieres llegar" (eso es el North Star).
- Pregunta una sola cosa cada vez. Espera respuesta. Profundiza si es vaga.

## Protocol — Personal

### Block 1 — Estado actual (10 min)

```
1. ¿Cómo es tu energía base estas últimas semanas en escala 1-10?
2. ¿Cuál es tu foco principal este trimestre? (UNA cosa, no tres).
3. ¿Hay algo que estés evitando hacer estas semanas?
4. ¿Hay alguna decisión pendiente que se te ha quedado abierta >2 semanas?
5. Tres wins de los últimos 30 días.
6. Tres frustraciones / fricciones de los últimos 30 días.
```

### Block 2 — Hábitos y rutinas (10 min)

```
1. Tu mañana ideal vs tu mañana real ahora mismo.
2. Tu noche ideal vs tu noche real.
3. Hábitos instalados (que ya no requieren willpower).
4. Hábitos en construcción (los que estás tratando de instalar).
5. Hábitos rotos (los que sabes que están mal y no estás trabajando).
6. ¿Cuántas horas duermes en promedio? ¿A qué hora te acuestas?
7. Comida y movimiento: estado actual en una frase.
```

### Block 3 — Trabajo profundo (5 min)

```
1. ¿Cuándo trabajas mejor? (mañana, tarde, noche).
2. ¿Cuándo NO debes trabajar en cosas duras? (post-comida, viernes tarde).
3. ¿Cuántas horas de deep work logras en una buena semana?
4. ¿Cuál es tu mayor distractor actual?
```

### Block 4 — Output

Genera `02. Areas/personal/Personal.md` con esta estructura (sobre el draft de Stage 1, lo enriquece):

```markdown
---
tags: [type/context, area/personal]
created: ...
updated: ...
---

# Personal

## Identidad (de Stage 1)
{{...}}

## Estado actual ({{date}})
- Energía base: {{X}}/10
- Foco trimestral: {{...}}
- Decisiones abiertas:
  - {{...}}
- Wins recientes (últimos 30d):
  - {{...}}
- Fricciones recientes:
  - {{...}}

## Hábitos
### Instalados
- {{...}}
### En construcción
- {{...}}
### Rotos / pendientes
- {{...}}

## Sleep & energy
- Horas: {{...}}
- Bedtime: {{...}}
- Movement: {{...}}
- Food: {{...}}

## Deep work
- Mejores horas: {{...}}
- Mayor distractor: {{...}}
- Horas/semana en buena semana: {{...}}

## Patrones (de Stage 1, mantener actualizado)
{{patterns}}

## Norte (síntesis — full version en North Star.md)
- 1 año: {{...}}
- 3 años: {{...}}
- 10 años: {{...}}
```

## Protocol — Business (per business)

Para cada business creado en Stage 2:

### Block 1 — Estado del negocio (10 min)

```
1. Una frase sobre dónde está {{business_name}} ahora mismo.
2. Las 3 prioridades que mueven la aguja en {{business_name}} este Q.
3. Métricas clave actuales (revenue, clientes, alumnos, lo que aplique).
4. ¿Está creciendo, manteniéndose, o decreciendo?
5. ¿Cuánto cash flow genera al mes (rango)? ¿Cuánto consume?
```

### Block 2 — Pipeline / proyectos activos (10 min)

```
1. Lista de "deals" / proyectos / clientes activos. Por cada uno:
   - Nombre
   - Estado / fase
   - Próximo step que depende de ti
   - Próximo step que depende del otro lado
2. ¿Hay deals stuck >30 días? ¿Por qué?
3. ¿Algún cliente/partner descontento ahora mismo?
```

### Block 3 — Equipo y operativa (5 min)

```
1. Equipo / partners / freelances. Quién hace qué.
2. ¿Hay alguien que no está rindiendo y lo sabes?
3. SOPs documentados ¿sí/no?
4. ¿Qué partes operas TÚ que deberían estar delegadas?
```

### Block 4 — Output

Genera `02. Areas/{business_slug}/Context.md`:

```markdown
---
tags: [type/context, business/{slug}]
---

# {{business_name}}

## Estado ({{date}})
{{one_liner}}

## Prioridades Q{{current_q}}
1. {{...}}
2. {{...}}
3. {{...}}

## Métricas actuales
- {{key_metric}}: {{value}}
- ARR / MRR / Revenue: {{...}}
- Clientes activos: {{...}}
- Trend: {{growing|flat|declining}}

## Pipeline activo
{{table_of_deals}}

## Stuck / fricción
{{stuck_deals}}

## Equipo
{{team_table}}

## Áreas a delegar
{{ops_to_delegate}}

## Riesgos conocidos
{{...}}
```

## Protocol — Health (5–10 min)

```
1. Goals de salud activos.
2. Movimiento actual (deporte/gym/caminatas).
3. Comida (estado, no dieta).
4. Recovery (sueño, descanso, vacaciones).
5. Mental (terapia, journaling, meditación, pareja, amigos).
6. Algo que el sistema deba flagger si detecta? (ej: "si no voy al gym 3 días seguidos, que me pinche").
```

Output: `02. Areas/health/Health.md`.

## Protocol — Learning (5–10 min)

```
1. Temas activos de aprendizaje (lo que estás estudiando AHORA).
2. Personas que sigues (mentores, autores, podcasts, canales YouTube).
3. Lectura activa (libros que estás leyendo).
4. Skills que quieres desarrollar este Q.
5. Hábitos de input (¿cuánto consumes vs cuánto produces?).
```

Output: `02. Areas/learning/Learning.md`.

## Protocol — Finances (5–10 min)

> Este es opcional. Si el usuario no quiere compartir, skip y dejar template vacío.

```
1. Renta neta mensual aproximada (rango).
2. Gasto mensual aproximado.
3. Ahorro / inversión / fondo de emergencia (alto nivel).
4. Deudas activas (hipoteca, consumo, otras).
5. Objetivo financiero a 12 meses.
6. ¿Hay algo financiero que te quita el sueño?
```

Output: `02. Areas/finances/Finances.md`.

## Confirmación final

Mostrar todos los context files generados al usuario:
> "He creado N archivos en tu vault. Léelos, edítalos a mano si quieres ajustar matices. Si pulsas continuar, vamos a Stage 4 (conectar herramientas)."

## Self-annealing

| Date | Issue/Learning | Resolution |
|---|---|---|
