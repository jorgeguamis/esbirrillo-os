---
description: Procesar reunión. Clasifica en cliente/interna/idea y ejecuta flujo correspondiente (CRM, tareas, ideas).
---

Ejecutar skill de meeting processor.

Lee `.claude/skills/meeting-processor/SKILL.md` y ejecuta el flujo.

## Cómo proporcionar la reunión

**Si hay transcripción en Fireflies:**
- Buscar por nombre de empresa/reunión con `fireflies_search`
- Obtener summary con `fireflies_get_summary`

**Si se pega texto directamente:** Usar directamente.

## Flujo

1. Obtener/recibir transcripción
2. Clasificar: **cliente** | **interna** | **idea**
3. Ejecutar flujo específico:
   - **Cliente** → extraer patrón/tesis/objeciones/próximas acciones + guardar en Agency Notes Notion + actualizar Outreach Status + añadir a daily note
   - **Interna** → extraer tareas, identificar responsable de cada una, mostrar separadas (solo crear las de {{USER_FIRSTNAME}} tras confirmación) + añadir a daily note
   - **Idea** → estructurar y añadir a daily note en sección Ideas

⚠️ CONFIRMACIÓN OBLIGATORIA antes de crear cualquier cosa en Notion.

Agente: Esbirrillo/{{DOMAIN_AGENT_SALES}} según contexto. Español, directo.
