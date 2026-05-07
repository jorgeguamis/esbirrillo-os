---
description: Reflexión nocturna basada en datos del día. Detecta patrones, identifica win, cierra loops.
---

Ejecutar skill de daily reflection.

Lee `.claude/skills/daily-reflection/SKILL.md` y ejecuta el flujo completo:

1. Leer la daily note de hoy: `02. Areas/personal/diario/01. Daily/{{date:DD-MM-YYYY}}.md`
2. Leer habits de los últimos 7 días en Notion (DB: `a7b99031-cc18-4a26-bc9c-db7128b14af4`)
3. Extraer: energía del día, gym ✅/❌, tareas completadas/total, decisiones pendientes
4. Detectar patrones (gym inconsistency, decision delay >14 días, procrastination loop)
5. Hacer preguntas específicas basadas en los datos del día — nunca genéricas
6. Identificar win del día (obligatorio, incluso en días difíciles)
7. Escribir sección de reflexión al final de la daily note
8. Cerrar con pregunta abierta

Agente: {{USER_FIRSTNAME}} (coach accountability). Tono: directo, empático, sin sermones. Español, tutear.
