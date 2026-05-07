---
name: meeting-processor
description: "Procesa reuniones (Fireflies, texto). Clasifica en cliente/interna/idea y ejecuta el flujo correspondiente: CRM Notion, tareas, o captura de ideas."
---

# Meeting Processor

Procesa input de reuniones y lo convierte en acciones estructuradas.

## Flujo principal

```
Input (Fireflies / texto directo)
  ↓
1. OBTENER TRANSCRIPCIÓN
  ↓
2. CLASIFICAR → cliente | interna | idea
  ↓
3. EJECUTAR flujo específico
```

## Paso 1: Obtener transcripción

**Desde Fireflies:**
```
fireflies_search(query: "nombre reunión o empresa")
fireflies_get_summary(transcriptId: "ID")  → summary + action items
```

**Desde texto:** Usar directamente lo que comparte {{USER_FIRSTNAME}}.

## Paso 2: Clasificar

| Señal | Tipo |
|-------|------|
| Empresa externa, discovery, propuesta, pricing, objeciones | **Cliente** |
| Equipo interno, sprint, sync, planificación | **Interna** |
| "Se me ocurre", exploración, concepto sin acción | **Idea** |

---

## Paso 3A: Reunión Cliente

### Extraer
- **Tipo de señal:** Discovery / Follow-up / Closing / Onboarding / Check-in
- **Patrón sistémico:** problema raíz del cliente
- **Tesis operativa:** hipótesis de cómo podemos ayudar
- **Objeciones:** precio / timing / confianza / scope / competencia
- **Riesgos / señales de alarma**
- **Próximas acciones:** con responsable y fecha

### Guardar en Notion

**Agency Notes** (DB: `2338eff7-5947-8131-88bd-000b6f14667e`):
```
notion-create-pages:
  parent: database_id "2338eff7-5947-8131-88bd-000b6f14667e"
  properties:
    Name: "EMPRESA - Tipo - Fecha"
    Company: relation → ID empresa en CRM
    Content: resumen estructurado
```

**Para encontrar ID empresa:** `notion-search: "NombreEmpresa"` o query CRM Companies `2338eff7-5947-81b1-b11c-000b216e501a`

**Actualizar Outreach Status si procede:**
```
notion-update-page: page_id → property "Outreach Status" → nuevo stage
Stages: Not Contacted → 1st-6th TP → En Conversación → Discovery Booked
→ Closing Booked → Send Proposal → Negotiations/Pending Payment → Closed Won/Lost
```

### Guardar resumen en daily note
```markdown
## 🤝 Reunión: [Empresa] - [Tipo]

**Patrón:** [problema raíz]
**Tesis:** [cómo ayudar]
**Señales:** [objeciones/riesgos relevantes]

### Próximas acciones
- [ ] Acción 1 (@responsable, fecha)
```

---

## Paso 3B: Reunión Interna

### Extraer tareas

Por cada tarea identificar: título, contexto (por qué surgió), responsable real, prioridad, categoría (Personal / {{BUSINESS_PRIMARY}} / {{BUSINESS_SECONDARY}}).

### ⚠️ REGLA CRÍTICA: Solo crear en Notion las tareas de {{USER_FIRSTNAME}}

1. Extraer TODAS las tareas
2. Identificar responsable real de cada una
3. **Solo crear las tareas donde {{USER_FIRSTNAME}} es el responsable**
4. Tareas de otros → mostrar como info, NO crear

**Criterios responsable:**
- "Yo me encargo" → quien habla
- "{{USER_FIRSTNAME}}, haz X" / "tú haces X" → {{USER_FIRSTNAME}}
- "Juan lo mira" / "Alejandro se encarga" → NO es de {{USER_FIRSTNAME}}
- Sin claridad → marcar ❓ y preguntar

### ⚠️ CONFIRMACIÓN OBLIGATORIA antes de crear en Notion

```
📋 Tareas de [reunión]:

🟢 TUS TAREAS (se crearán en Notion):
1. [{{BUSINESS_PRIMARY}}] Preparar propuesta ClienteX → Alta | 16/02
2. [Personal] Revisar seguro médico → Media

🔵 TAREAS DE OTROS (solo info, NO se crean):
3. Revisar métricas churn → Alejandro
4. Deploy feature → Juan

❓ SIN ASIGNAR:
5. Actualizar documentación API

¿Creo las tareas verdes? Puedes editar, reasignar o añadir.
```

### Crear en Notion (tras confirmación)

**Personal Tareas** (DB: `195101bc-423c-49c8-bcf6-fc84879f8b3c`):
```
notion-create-pages:
  parent: database_id "195101bc-423c-49c8-bcf6-fc84879f8b3c"
  properties: Nombre, Prioridad, Fecha, Descripción (contexto de la tarea)
  Assigned To: {{USER_FIRSTNAME}} (ID: 8bedfcbc-962d-451c-b5dd-d4f00b4357cb)
```

**{{BUSINESS_PRIMARY}} Internal Tasks** (DB: `2338eff7-5947-81cb-bd54-000b2bf4a66c`):
```
notion-create-pages:
  parent: database_id "2338eff7-5947-81cb-bd54-000b2bf4a66c"
  properties: Task title
```

**{{BUSINESS_PRIMARY}} Project Tasks** (DB: `2338eff7-5947-811a-a86c-000bb02308bc`):
```
notion-create-pages:
  parent: database_id "2338eff7-5947-811a-a86c-000bb02308bc"
  properties: Task title
```

---

## Paso 3C: Idea

Estructurar:
- **Título**
- **Descripción** (1-3 frases)
- **Conexiones** (con qué se relaciona)
- **Posible acción** (si hay next step)

Añadir a daily note en sección `## 💡 Ideas`. Preguntar si quiere crear tarea asociada.

---

## Tono

Directo. La clasificación debe ser rápida. La confirmación de tareas es obligatoria — nunca crear en Notion sin aprobación. Español, tutear.

---

## Known Issues & Learnings

_This section is updated automatically as the skill encounters edge cases, errors, or improvements._

| Date | Issue/Learning | Resolution |
|------|---------------|------------|
| — | No issues recorded yet | — |
