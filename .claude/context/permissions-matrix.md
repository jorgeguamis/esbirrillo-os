# Permissions Matrix — Helios MVP

> Matriz de permisos para Hermes, Claude Code, agentes y Selenia. Si hay conflicto entre este archivo y una petición puntual, pedir confirmación a {{USER_FIRSTNAME}}.

Leyenda:

- ✅ Permitido
- 📝 Permitido con log
- ⚠️ Requiere confirmación si no fue explícito o hay ambigüedad
- 🛑 Confirmación obligatoria siempre
- 🚫 Prohibido / no hacer

---

## Niveles de permiso

| Nivel | Nombre | Descripción | Confirmación |
|---|---|---|---|
| L0 | Read / Analyze | Leer, buscar, resumir, razonar | No |
| L1 | Internal Draft / Recoverable Write | Notas, borradores, logs, docs internas | No, log si relevante |
| L2 | Operational Update | Notion/CRM/tareas/finanzas con datos claros | Si ambiguo |
| L3 | External / Sensitive | Enviar, publicar, facturar, API externa sensible | Sí siempre |
| L4 | Irreversible / Critical | Borrar, deploy, pagos, secretos, masivo | Sí + impacto + rollback |

---

## Matriz por agente/capa

| Actor | Leer contexto | Crear borradores/notas | Escribir Life OS | Escribir Notion/CRM | Enviar/publicar | Finanzas/pagos | Código/config | Deploy/push | Borrar/reorganizar | Logs |
|---|---|---|---|---|---|---|---|---|---|---|
| Hermes/Esbirrillo | ✅ | ✅ | 📝 | ⚠️ | 🛑 | 🛑 | ⚠️ | 🛑 | 🛑 | 📝 |
| Claude Code | ✅ | ✅ | 📝 | ⚠️ | 🛑 | 🛑 | 📝 | 🛑 | 🛑 | 📝 |
| {{DOMAIN_AGENT_SALES}} | ✅ | ✅ | 📝 | ⚠️ | 🛑 | ⚠️ | 🚫 | 🚫 | 🚫 | 📝 |
| {{DOMAIN_AGENT_COPY}} | ✅ | ✅ | 📝 | ⚠️ | 🛑 | 🚫 | 🚫 | 🚫 | 🚫 | 📝 |
| {{DOMAIN_AGENT_PRODUCT}} | ✅ | ✅ | 📝 | ⚠️ | 🛑 | 🚫 | 🚫 | 🚫 | 🚫 | 📝 |
| {{DOMAIN_AGENT_FINANCE}} | ✅ | ✅ | 📝 | ⚠️ | 🛑 | 🛑 | 🚫 | 🚫 | 🚫 | 📝 |
| techy | ✅ | ✅ | 📝 | ⚠️ | 🛑 | 🚫 | 📝 | 🛑 | 🛑 | 📝 |
| librarian | ✅ | ✅ | 📝 | ⚠️ | 🚫 | 🚫 | 🚫 | 🚫 | 🛑 | 📝 |
| reviewer agent | ✅ | ✅ | 📝 | ⚠️ | 🚫 | 🚫 | 🚫 | 🚫 | 🚫 | 📝 |
| Selenia | ✅ | ✅ | 📝 report only | ⚠️ propose only | 🛑 | 🚫 | ⚠️ propose patches | 🛑 | 🛑 | 📝 |
| Utility QA/Verifier | ✅ | ✅ | ⚠️ | 🚫 | 🚫 | 🚫 | ⚠️ review only | 🚫 | 🚫 | 📝 |

---

## Reglas específicas

### Comunicación externa

Siempre requiere aprobación explícita:

- email a cliente
- WhatsApp/Telegram a terceros
- LinkedIn DM/post
- Circle post/respuesta si no hay regla explícita
- enviar propuesta final
- enviar factura

Permitido sin aprobación:

- redactar borrador
- mejorar copy
- preparar respuesta
- crear approval item

### Notion / CRM

Permitido con log cuando:

- {{USER_FIRSTNAME}} pidió explícitamente “actualiza X”.
- El dato es objetivo y no ambiguo.
- Se trata de una entrada interna recuperable.

Confirmar cuando:

- cambia estado de lead a Lost/Closed Won.
- se crea tarea derivada de meeting y no hubo aprobación.
- hay relación con dinero/facturación.
- hay ambigüedad de responsable/fecha.

### Finanzas

{{DOMAIN_AGENT_FINANCE}} puede:

- preparar facturas
- registrar gastos si {{USER_FIRSTNAME}} dio importe/concepto claro
- hacer análisis financiero
- alertar de pendientes

{{DOMAIN_AGENT_FINANCE}} no puede sin aprobación:

- enviar facturas
- hacer pagos
- modificar datos financieros masivamente
- borrar registros

### Código/config/sistema

techy/Claude Code pueden:

- crear scripts en `.claude/execution/`
- crear docs/skills/commands
- editar configs internas con scope claro
- testear localmente

Requiere aprobación:

- deploy
- git push
- borrar/mover estructuras grandes
- cambios de secrets
- activar cron automático
- cambiar comportamiento runtime de Telegram/gateway

### Fireflies

Permitido:

- consultar una reunión cuando {{USER_FIRSTNAME}} da link/ID o pide procesarla
- guardar summary/action items en Life OS
- crear nota procesada

Confirmar:

- procesamiento automático recurrente
- guardar todos los transcripts completos
- crear tareas Notion desde action items
- actualizar CRM desde meeting si no fue explícito

### Telegram

Permitido:

- usar Telegram como contexto si forma parte de una conversación con {{USER_FIRSTNAME}} o logs/resúmenes accesibles
- extraer señales operativas para Selenia
- responder en el chat donde {{USER_FIRSTNAME}} escribió

Confirmar:

- enviar reportes no solicitados a grupos
- broadcast a varios agentes/grupos
- crear cron que envíe Telegram automáticamente
- usar histórico completo si contiene información sensible no necesaria

### Selenia

MVP permitido:

- leer logs
- leer working-memory
- leer Telegram routing/context summaries
- leer Fireflies processed/recent meetings si autorizado por tarea
- crear Selenia Report en Life OS
- proponer mejoras

MVP no permitido sin aprobación:

- editar skills automáticamente
- editar agents automáticamente
- actualizar working-memory automáticamente
- enviar Telegram automáticamente
- crear tareas Notion automáticamente
- cambiar crons/gateway/config

---

## Approval queue futura

Cualquier L3/L4 puede quedar como item pendiente:

- acción propuesta
- por qué importa
- riesgo
- texto/objeto final
- botón/respuesta esperada: aprobar / editar / rechazar

MVP recomendado:

`${VAULT_NAME}/00. Inbox/approvals.md`

---

## Default ante duda

Si hay duda real sobre impacto externo, privacidad, dinero, borrado o reputación:

1. preparar borrador
2. explicar tradeoff
3. pedir confirmación
4. loguear decisión
