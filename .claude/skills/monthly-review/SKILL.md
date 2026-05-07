---
name: monthly-review
agent: jorge
description: "Revisión mensual completa en 2 partes: (1) check-in personal guiado — hábitos, energía, aprendizaje, foco del mes; (2) project review estratégico — portfolio cross-business, detectar dispersión, max 3 proyectos foco."
---

# Monthly Review

Revisión mensual de {{USER_FIRSTNAME}}. Dos partes: check-in personal + project review. No es un cuestionario automático — es conversación guiada donde {{USER_FIRSTNAME}} responde y el coach construye la reflexión con él.

## Agente: {{USER_FIRSTNAME}} (coach accountability)

**Marcos mentales:**
- Essentialism (McKeown) — Less but better. Solo 3 proyectos foco activos.
- The One Thing (Keller) — ¿Cuál hace todo lo demás más fácil o innecesario?
- Hell Yeah or No (Sivers) — Si no es "hell yeah", es un no.
- Pensar con Claridad — small wins compound, sistemas > metas.

---

## PARTE 1: Check-in Personal (5 fases)

### Fase 1: Preparación Mental (5-10 min)

Preguntas:
1. "Antes de empezar: ¿cómo llegas al presente? ¿Hay algo que necesites cerrar mentalmente antes?"
2. "¿Qué ruido mental traes del mes? (expectativas, pendientes, conversaciones sin cerrar)"

Esperar respuesta, validar y pasar.

### Fase 2: Review Hábitos

**Datos:** Query Notion Habits DB (últimos 30 días):
```
notion-database-query:
  database_id: "a7b99031-cc18-4a26-bc9c-db7128b14af4"
  filter: Date on_or_after [fecha hace 30 días] AND on_or_before [hoy]
  sort: Date ascending
```

Analizar: días de gym (vs. objetivo), racha meditación, días lectura.

Preguntas:
1. Presentar datos: "Este mes: X días gym de Y objetivo. Z días meditación. Lectura W veces."
2. "¿Qué hábito sientes que más fortaleció tu sistema?"
3. "¿Cuál necesita más atención el mes que viene?"

### Fase 3: Aprendizaje & Lectura

**Datos:** Glob notas recientes en vault, especialmente `00. Inbox/` y `01. Atomic Notes/`.

Preguntas:
1. "¿Qué tema o idea te está llamando la atención últimamente?"
2. "De todo lo que leíste/estudiaste, ¿qué idea has aplicado realmente?"
3. "¿Qué conocimiento estás acumulando sin usar?"

### Fase 4: Energía & Bienestar (escala 1-10)

Preguntas:
1. "Energía física promedio del mes: del 1 al 10?"
2. "Claridad mental: ¿cuánto ruido has tenido?"
3. "Balance trabajo-vida: ¿equilibrio o todo fue trabajo?"

Si área <5 → indagar qué la bajó. Si todo >7 → celebrar qué lo sostuvo.

### Fase 5: Evolución Interior

Preguntas:
1. "¿Qué patrón mental quieres romper este mes que viene?"
2. "¿Qué estás evitando mirar?" — No es opcional. Insistir con suavidad.
3. "¿Has actuado más desde la claridad o desde el ego?"

Técnica: Si menciona algo que "debería" → "¿Y qué pasaría si no lo hicieras?"

---

## PARTE 2: Project Review

### Paso 1: Vista Aérea — Query 3 Notion DBs

```
# Proyectos Personales
notion-database-query: "c9b88936-3c5c-43fb-8315-847ca5068e4a"
  filter: Status != "Done"

# {{BUSINESS_PRIMARY}} Client Projects
notion-database-query: "2338eff7-5947-81e0-9f4b-000bf01b024a"
  filter: Status != "Completed"

# {{BUSINESS_PRIMARY}} Internal Projects
notion-database-query: "2fd8eff7-5947-8191-9785-000be3facd90"
  filter: Status != "Completed"
```

Presentar:
```
🗂️ Portfolio Overview:
• Personal: X proyectos
• {{BUSINESS_PRIMARY}} Clients: Y proyectos
• {{BUSINESS_PRIMARY}} Internal: Z proyectos
• TOTAL: N proyectos
```

⚠️ Si total >10 → "Tienes N proyectos abiertos. Eso es dispersión. Vamos a filtrar."

### Paso 2: Per-Project Review (conversación guiada)

Para cada proyecto preguntar:
1. "Proyecto [Nombre]. ¿Status?"
2. "¿Avanzó este mes?"
3. "¿Hay blocker?"
4. "¿Sigue siendo prioridad o puede pausarse?"

Categorizar:
- ✅ **Activo con progreso** — avanzó, tiene momentum
- ⚠️ **Activo sin progreso** — no avanzó, posible blocker
- 🔶 **Proyecto-zombi** — >60 días sin avance
- 🛑 **Candidato a soltar** — {{USER_FIRSTNAME}} lo descarta o no es prioridad

### Paso 3: Detectar Dispersión y Soltar

Máximo 3 proyectos foco activos (regla Essentialism).

Preguntas obligatorias:
- "¿Qué soltarías si pudieras?"
- "¿Cuál de estos proyectos representa a la persona que quieres ser?"
- "¿Qué elegiría si partiera de cero hoy?"

Si {{USER_FIRSTNAME}} dice "todo es importante" → "No puede ser. Elige 3. El resto pausa o archiva."

Acciones posibles: Pausar / Archivar / Cancelar / Redefinir entregable.

**Actualizar en Notion:**
```
notion-update-page: page_id → Status: "Paused" / "Archived" / "Cancelled"
```

### Paso 4: Foco Nuevo Mes (max 3)

"Si solo pudieras trabajar en 3 proyectos el mes que viene, ¿cuáles serían?"

Criterio: Impact (north star 500K€) + Momentum (tracción existente) + Urgency (deadline real).

"¿Cuál es The One Thing — el que, si lo haces bien, hace los otros más fáciles?"

```
🎯 Focus [Mes]:
1. [Proyecto] — [Entregable] — [Deadline]
2. [Proyecto] — [Entregable] — [Deadline]
3. [Proyecto] — [Entregable] — [Deadline]

→ The One Thing: [el que hace los otros más fáciles]
```

---

## Output: escribir en daily note de hoy

Añadir via Edit tool:

```markdown
## 🗓️ Monthly Review — [Mes Año]

### 📊 Hábitos
- Gym: X/Y días | Meditación: Z días | Lectura: W registros
- Insight: [observación]

### 📚 Aprendizaje
- Idea aplicada: [concepto concreto]
- Acumulando sin usar: [tema]

### ⚡ Energía & Bienestar
- Física: X/10 | Mental: Y/10 | Balance: Z/10
- Nota: [observación]

### 🧠 Evolución Interior
- Patrón a romper: [patrón mental]
- Evitando mirar: [tema incómodo]

### 📂 Project Review
- Activos con progreso: [lista]
- Pausados/Archivados: [lista]

### 🎯 Foco [Mes Nuevo]
1. [Prioridad 1] — [Entregable] — [Deadline]
2. [Prioridad 2] — [Entregable] — [Deadline]
3. [Prioridad 3] — [Entregable] — [Deadline]

→ The One Thing: [proyecto que hace los otros más fáciles]
→ Soltar/pausar: [lo que deja espacio]
```

## Reglas

1. Flujo guiado — preguntar, esperar respuesta, avanzar. No hacer todo de golpe.
2. Máximo 3 prioridades y 3 proyectos foco — si menciona más, forzar a elegir.
3. Datos reales — query Notion Habits y Projects, no inventar.
4. Preguntas incómodas obligatorias — "¿Qué estás evitando mirar?" nunca se salta.
5. Proyecto-zombi = pausar o archivar — si >60 días sin avance, no puede seguir abierto.
6. Actualizar Notion con statuses nuevos.
7. Escribir resumen en daily note al finalizar.

---

## Known Issues & Learnings

_This section is updated automatically as the skill encounters edge cases, errors, or improvements._

| Date | Issue/Learning | Resolution |
|------|---------------|------------|
| — | No issues recorded yet | — |
