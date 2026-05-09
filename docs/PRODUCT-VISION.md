---
title: "Esbirrillo OS — Product Vision"
status: draft
last_updated: 2026-05-09
audience: founders, partners, investors, prospective clients
---

# Esbirrillo OS — Product Vision

> **Heads-up**: el código que vive en este repositorio hoy es scaffolding inicial. Lo que describe este documento es la visión hacia la que ese código debe converger. Cuando el producto esté terminado, el scaffolding actual nos parecerá primitivo. Es deliberado: este PRD apunta a la estrella, no al satélite.

[1. North Star](#1-north-star) · [2. Origen](#2-origen-y-convergencia) · [3. Target users](#3-target-users) · [4. Value prop](#4-value-proposition) · [5. Arquitectura](#5-arquitectura-visión) · [6. Módulos & Connectors](#6-módulos-custom-y-connectors) · [7. Hosting](#7-hosting) · [8. Pricing](#8-pricing) · [9. Decisiones pendientes](#9-decisiones-pendientes) · [10. Riesgos](#10-riesgos) · [11. Métricas](#11-métricas-de-éxito) · [12. Roadmap](#12-roadmap)

---

## 1. North Star

**Esbirrillo OS** es una plataforma agéntica que da a un usuario (founder o empresa) un asistente real: una **interfaz conversacional** que entiende su rol, sus prioridades y su stack; un **orquestador** que decide qué hacer; un **motor de skills** que ejecutan tareas atómicas; un **backend relacional** —inspirado en la arquitectura de Odoo— sobre el que se construyen módulos verticales (CRM, finanzas, RRHH, ventas, ops); y una **capa de connectors** que conecta a los sistemas existentes del cliente sin obligarle a migrar.

**Para quién**

- **Hoy (V1)**: solo-founder / CEO con 1-3 negocios. Quiere su propio "Jarvis" sin tener que reconstruirlo a mano cada vez.
- **Mañana (V2)**: PYME (10-200 empleados) con un cerebro agéntico organizacional, módulos por departamento y connectors a su stack. Segmentado en V2-A (low-tech) y V2-B (digitalizada).

**Por qué ahora**

- Claude Code y los agentes han madurado lo suficiente para soportar uso real continuo.
- Hermes-agent (runtime open-source) estabiliza el "siempre-on" sin construir desde cero.
- La ola de adopción IA en PYME ha llegado, pero las herramientas siguen siendo: a) ChatGPT genérico, b) SaaS verticales rígidos, c) automatizaciones tipo n8n. Hay hueco entre los tres.
- Ventana de oportunidad antes de que las grandes plataformas (OpenAI Apps, Google, MS Copilot) comoditicen este espacio.

---

## 2. Origen y convergencia

Tres hilos están convergiendo hacia este producto:

1. **Scaffolding inicial** (mayo 2026): un kit replicable para llevar el sistema agéntico personal de Jorge a otros founders. Caso 0 = Juan Santacruz (CEO Revolutia). Apuesta = el tío de Juan, CEO de empresas grandes. Plan operativo detallado en [`glittery-seeking-bengio.md`](../../../../.claude/plans/glittery-seeking-bengio.md). El código actual es desechable: arquitectura provisional sobre la que se va a iterar agresivamente.
2. **Roadmap SAAS Revolutia (febrero 2025)**: una propuesta de "Second Brain para consultores" (CRM + propuestas + facturación + tasks + dashboard + portal cliente) que nunca llegó a construirse. Era SaaS tradicional pre-LLM. **Hoy se reencarna como inspiración para los módulos custom de la V2 Enterprise.** El concepto sigue siendo válido; lo que cambia es el UX (agéntico) y el stack (backend relacional + skills + workers).
3. **Conversación con Dani de AinexiQ (08-05-2026)**: aporta visión enterprise — departamentalidad estilo ERP, control de accesos, compliance, SQL+vectorial híbrido, no desplazar sistemas existentes sino digitalizar lo que el cliente ya usa. Reunión próxima pendiente para definir si hay colaboración formal (D-DANI).

**Aprendizajes que reescriben la visión inicial**

Durante el diseño emergieron varias correcciones de arquitectura críticas:

- **Odoo es inspiración, no producto.** Odoo Enterprise tiene licencia que prohíbe monetizar SaaS basado en sus features. Decisión: aprender de su backend conceptual (Postgres, modelos relacionales, cómo conecta CRM/facturas/proyectos/usuarios) y **recrear backend custom** con frontend moderno. El frontend de Odoo es viejo; su backend conceptual está muy bien. Cero código forkeado, cero "Odoo bonito reskineado".
- **Para V1, Hermes ya hace casi todo.** Hermes delega tareas, carga skills, crea subagentes, gestiona memoria/configuración. **No construir código para algo que Hermes ya hace.** Las skills son templates; los subagentes hacen spawn on demand; la persistencia vive en memoria/logs/files, no en procesos eternos. Procesos vivos solo para listeners/gateways/crons/watchdogs reales.
- **V1 simplificado**, **V2 separado**. En V1 (founder), interfaz + orquestador son la misma pieza (`Esbirrillo`). En V2 (empresa), conviene separar capas: gateway (interfaz por usuario) · orquestador central · workers · memoria/contexto per user · permisos/auditoría.
- **Many con niveles de permisos** (no auto-mejora genérica): L1 Observación · L2 Recomendación · L3 Auto-fix seguro · L4 Approval requerido.
- **Hermes-first, no Claude Code-first**. Anthropic puede bloquear IPs nuevas en servidores recién creados. Claude Code = brazo ejecutor profundo bajo demanda, no listener crítico. Modelo principal del runtime puede ser Kimi o GPT-5.5 (configurable).
- **Notion vs backend custom**: Notion = capa de pensar (texto, islas de conocimiento). Backend custom = capa de hacer (datos relacionales, ERP/CRM/proyectos). Notion sufre cuando se cruzan muchas DBs/relaciones/permisos.
- **Onboarding 70/30**: ~70% preconfigurado out-of-the-box (Esbirrillo + skills/agentes universales que sirven a cualquier founder o empresa) + ~30% customizado por usuario (la Capa Identidad: working memory, contextos, agentes propios) vía setup-wizard.
- **Estética**: interfaz tipo Apple/Holden — frontend bonito y moderno. Cero apariencia ERP de los 2000s.

---

## 3. Target users

### V1 — Solo-founder / CEO

**Perfil**: 1-3 negocios; equipo 0-15 personas; opera en Mac; ya usa Claude Code o está dispuesto.

**Job-to-be-done**: tener un asistente agéntico personal que ejecuta + recuerda + acompaña, sin tener que reconstruirlo a mano. El sistema entiende su rol, sus prioridades, su agenda, y opera en su día a día.

**Validación**: caso 0 = Juan Santacruz (Revolutia). Operación supervisada de 4-8 semanas con observación de uso real.

**Necesidades del founder en su día a día** (a refinar tras discovery con Juan):

- Procesar reuniones, capturar decisiones, hacer follow-up.
- Mantener visión de pipeline, prioridades, energía.
- Escribir y editar contenido, propuestas, contratos.
- Capturar conocimiento, conectar ideas, leer.
- Gestionar finanzas personales y de negocio.
- Reflexionar, detectar patrones, ajustar rumbo.

### V2 — Empresa (segmentada)

| Segmento | Perfil | Implicaciones para producto |
|---|---|---|
| **V2-A — PYME low-tech** | 10-200 empleados. Excel + email + ERP legacy o ninguno + papel. Procesos no documentados. Cultura digital baja. | Onboarding pesado; alto coste de discovery e integración. Connectors a Excel/email/PDF/parser legacy. Valor: digitaliza lo que ya hacen sin obligarles a migrar. Pricing alto por implantación. |
| **V2-B — PYME digitalizada** | 10-200 empleados. Google Workspace + algún SaaS + ERP cloud (Holded / Odoo / HubSpot). Procesos semi-formales. | Ciclo de venta más corto. Connectors maduros (Notion, GWS, Stripe, Holded). **Target preferente para los primeros clientes V2.** |

Necesidades V2 a definir tras discovery:

- Compartido por ambos: CRM org-wide, gestión documental, automatización de procesos repetitivos, comunicación cliente.
- V2-A necesita además: integraciones legacy, onboarding más asistido, módulos extra (papel → digital).
- V2-B puede partir de skills de V1 con extensiones multi-usuario.

### Anti-target (por ahora)

Corporación >500 empleados, multi-país, requisitos de auditoría tipo SOC2/HIPAA. **V3 si llega.** No diseñamos para eso.

---

## 4. Value proposition

### Vs ChatGPT / Claude.ai estándar

- Persiste contexto entre sesiones, días y semanas.
- Opera en background (no requiere abrir un chat para que pase algo).
- Integra con las tools del usuario (Notion, calendar, email, drive, etc.).
- Ejecuta tareas reales con persistencia, no solo conversa.

### Vs n8n / Make / Zapier

- Es **agéntico**: el sistema decide qué hacer; el usuario describe outcomes, no pasos.
- No flujos rígidos: la lógica vive en skills + working memory, no en grafos hardcoded.

### Vs SaaS verticales

- Corre donde el usuario elija (Mac, Mac mini, servidor) con SUS credenciales.
- Cero lock-in vendor; el usuario es dueño de su data y su working memory.

### Vs Odoo Enterprise

- Backend conceptual similar (Postgres + modelos relacionales + módulos), pero:
- Frontend moderno (no estilo ERP de los 2000s).
- Capa agéntica nativa: agentes y skills que **operan los módulos**, no solo formularios y vistas.
- Sin dependencia de licencias Odoo Enterprise.

### Vs construirlo a mano (lo que hizo Jorge para sí mismo)

- Meses de trabajo → semanas de onboarding asistido.
- **Pero al inicio el onboarding es manual y caro deliberadamente**: alto esfuerzo = alto valor percibido = pricing premium. La escalabilidad llega cuando el producto ha sido validado, no antes.

### Vs SaaS de productividad estándar (en V2)

- Backend relacional sólido + agentes que orquestan procesos reales.
- Connectors a sistemas existentes del cliente: digitaliza sin obligar a migrar.
- Marketplace de módulos: el cliente activa solo lo que necesita.

---

## 5. Arquitectura (visión)

> El código del repositorio NO refleja todavía esta arquitectura. Es la visión hacia la que el repo debe converger. Las capas Módulos custom y Capa Identidad son nuevas; las capas Core y Runtime existen parcialmente en el scaffolding pero requieren reescritura.

### V1 — Solo-founder (simplificado)

```
┌──────────────────────────────────────────────────────────┐
│ CAPA IDENTIDAD (la parte 30% custom)                     │
│ Working memory, contextos por área, agentes propios del  │
│ usuario. VACÍA al instalar; el setup-wizard la rellena   │
│ entrevistando al usuario. Aquí vive lo que hace que ESTE │
│ sistema sea de ESTE founder y de nadie más.              │
└──────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────┐
│ CAPA MÓDULOS (backend custom inspirado en Odoo)          │
│ Postgres + modelos relacionales + lógica de módulos.     │
│ V1 trae: agenda, knowledge base, tasks, finanzas         │
│ personales. Frontend moderno (Apple/Holden-style).       │
└──────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────┐
│ CAPA CORE (la parte 70% preconfigurada)                  │
│ Esbirrillo = interfaz conversacional + orquestador,      │
│ unificados, listo out-of-the-box.                        │
│ + Skills/agentes genéricos universales que sirven a      │
│ cualquier founder o empresa: capture, meeting-processor, │
│ weekly-review, knowledge-digest, librarian, reviewer...  │
│ Skills = templates de agentes (spawn workers on demand). │
│ NO jerarquía compleja. NO procesos persistentes salvo    │
│ listeners / crons / watchdogs reales.                    │
└──────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────┐
│ CAPA RUNTIME                                              │
│ Hermes (gateway, scheduler, skill loader, multi-modelo). │
│ Modelo principal: Kimi o GPT-5.5 (configurable).         │
│ Claude Code = brazo ejecutor profundo bajo demanda.      │
│ Many (auto-mejora con permisos L1-L4).                   │
│ Logs JSONL, approval queue, hooks.                       │
└──────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────┐
│ CAPA CONNECTORS (MCPs / APIs)                             │
│ Notion · GWS · Stripe · Slack · WhatsApp · Twilio ·      │
│ Salesforce · HubSpot · Custom API · Excel parser ·       │
│ email parser. Configurables por usuario.                 │
└──────────────────────────────────────────────────────────┘
```

### V2 — Empresa (capas separadas)

```
                    ↓ usuario per departamento ↓
┌──────────────────────────────────────────────────────────┐
│ KAIROS — Gateway / interfaz por usuario                   │
│ Carga preferencias, voz, contexto del rol del empleado.  │
│ Persona conversacional adaptada (no único Esbirrillo).   │
└──────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────┐
│ HELIOS — Orquestador central                              │
│ Recibe intent enriquecido por Kairos. Decide ruta,       │
│ descompone, delega. "Ojo de Sauron" del sistema.         │
│ Aplica permisos por rol y departamento.                  │
└──────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────┐
│ WORKERS / SUBAGENTES — Ejecución especializada            │
│ Spawn on demand desde skills (templates).                │
│ Por dominio: ventas, finanzas, ops, RRHH, IT, marketing. │
└──────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────┐
│ MEMORIA / CONTEXTO PER USER                               │
│ Working memory por persona. Context por rol.             │
│ Audit log compartido por organización.                   │
└──────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────┐
│ MÓDULOS + CONNECTORS (igual que V1 pero org-wide)         │
└──────────────────────────────────────────────────────────┘
```

### Naming

- **Interno V1**: `Esbirrillo` (interfaz + orquestador unificados), `Many` (auto-mejora L1-L4).
- **Interno V2**: `Kairos` (gateway/interfaz), `Helios` (orquestador central), workers genéricos, `Many`.
- **Comercial**: D-NAMING abierta. Buscamos un concepto con doble lectura. Propuestas iniciales:
  - `Esbirrill.os` (Esbirrillo + .os de operating system)
  - `Sol.OS` (Solo-founder + OS, también lee "Solos")
  - `FoundIA` (Founder + IA)
  - `SelenIA` (Selena + IA)
  - `CompañIA` (Compañía + IA — perfecto en castellano para V2)
  - `Org.OS` (Organización + OS para V2)

Decisión por confirmar.

---

## 6. Módulos custom y Connectors

Cada módulo del producto = **backend custom relacional (Postgres, inspirado en la arquitectura de Odoo) + skills agénticas + workers que lo operan**. NO es un fork de Odoo. NO es Odoo Enterprise reskineado. Inspiración arquitectónica, no derivación de código.

### Módulos planeados

| Módulo | Estado | Inspiración |
|---|---|---|
| **Knowledge base** | V1 (Vault Obsidian + atomic notes) | Existe en sistema actual de Jorge |
| **Agenda / Meetings** | V1 (GWS connector + meeting-processor) | Existe |
| **Tasks** | V1 (Postgres tasks + route-task) | Notion sufre con relaciones — refactor a backend propio |
| **Finanzas personales** | V1 (Postgres + Stripe / Holded connector) | Existe parcialmente |
| **CRM** | V2 (modelo CRM relacional + workers ventas) | Inspirado Odoo CRM |
| **Facturación** | V2 (modelo facturas + Stripe + Holded connector) | Inspirado Odoo Accounting |
| **Proyectos / Timesheets** | V2 (modelo proyectos + horas) | Inspirado Odoo Project + Timesheets |
| **Propuestas / Contratos / Firmas** | V2 (templates + e-sign) | Inspirado Odoo Sign |
| **RRHH / Asistencia** | V2 (modelo empleados + horas) | Inspirado Odoo HR |
| **Tienda / Suscripciones** | V2 (productos + Stripe) | Inspirado Odoo Sale + Subscriptions |
| **Cold calling / Voz IP** | V2 (Twilio o similar + scoring + transcripción) | Add-on nuevo no presente en SaaS Revolutia 2025 |
| **Dashboard org-wide** | V2 (vistas custom de los módulos) | Inspirado Odoo Studio |
| **Portal cliente** | V2.5 (multi-user + roles) | Inspirado Odoo Portal |

### Connectors clave

| Categoría | Connectors |
|---|---|
| Operativo | Notion · Google Workspace · Slack · Discord · WhatsApp Business |
| CRM externo | Salesforce · HubSpot · Pipedrive |
| Facturación | Stripe · QuickBooks · Holded |
| ERPs legacy (V2 enterprise) | SAP · NetSuite · verticales sectoriales |
| Voz IP | Twilio · Aircall |
| Genéricos | Custom API connector · Excel parser · email parser (V2-A) |

V1 trae solo Capa Identidad + Core + Runtime + 1-2 connectors básicos (Notion, Google Workspace). Los módulos custom llegan progresivamente desde V1.5.

---

## 7. Hosting

Tres modos, configurables al instalar:

- **Mac del usuario** — V1, cero infra extra, latencia local, privacidad máxima. Limitación: si la mac está apagada, no hay crons.
- **Mac mini dedicado** (~700€ M4 + setup) — V1.5/V2, siempre-on, separado del laptop personal. Upsell para usuarios que no quieren depender de su laptop.
- **Servidor / VPS dedicado** (~32-64GB RAM si va con módulos custom + Hermes + DBs) — V2 / enterprise, siempre-on, multi-usuario, mejor para módulos serios. **Stack backend custom requiere servidor**, no corre cómodo en Mac.

El instalador detecta el modo y configura crons, paths y MCPs apropiados. La elección no es bloqueante; se puede migrar entre modos.

---

## 8. Pricing

Hipótesis de partida, refinable tras los primeros 1-3 clientes.

### V1 — Solo-founder

- **Setup**: 8-15k€ — refleja el alto esfuerzo manual de discovery + onboarding asistido + valor de tener el sistema operando en su día a día.
- **Retainer**: 1.5-3k€/mes — mantenimiento, nuevas skills, ajustes de working memory, soporte.

El pricing alto al inicio es deliberado:

1. Refleja el valor real (un asistente agéntico personalizado).
2. Compensa el coste de servicio manual (V1 no es escalable y tampoco lo pretende).
3. Filtra clientes serios desde el primer minuto.

### V2 — Empresa

TBD. Múltiplo del V1 según tamaño de organización + módulos activos. Posibles revenue shares con partners (TBD por D-DANI).

---

## 9. Decisiones pendientes

| ID | Decisión | Quién decide | Cuándo | Bloquea |
|---|---|---|---|---|
| D-NAMING | Nombre comercial V1 y V2 (con doble lectura) | Jorge | Pre-PRD final público | PRD final |
| D-DANI | Rol de Dani: partner / proveedor / inspiración | Jorge tras próx. reunión | TBD (esta semana o sig.) | Estrategia V2 |
| D-VAULT | Vault default = Obsidian o Notion por tier | Jorge + Juan en sem 4 | Sem 4 | Setup-wizard |
| D-FIRST-MODULE | Primer módulo custom tras la base V1 | Jorge | Sem 8+ | Roadmap V1.5 |
| D-PRICING | Setup + retainer V1 definitivo | Jorge | Sem 7 | Conversación tío |
| D-MARKETPLACE | Modelo del marketplace de módulos (private / public / curated) | Jorge | V1.5 | V2 estrategia |
| D-BACKEND-STACK | Tecnología del backend custom (Python+FastAPI / Node / Go / framework alto-nivel) | Jorge + asesor técnico | Sem 1-2 | Capa Módulos |
| D-CORE-AGENTS | Set definitivo de workers V1 vs V2 | Jorge tras discovery + análisis cruzado | Sem 2-3 | Capa Core |
| D-MODELS | Modelo principal definitivo (Kimi vs GPT-5.5 vs híbrido) y reglas de selección | Jorge | Sem 1 | Capa Runtime |

> **Decisiones ya cerradas**: Hermes-first como runtime; Odoo solo como inspiración arquitectónica; V1 unificado vs V2 separado; Many con niveles L1-L4; ratio onboarding 70/30.

---

## 10. Riesgos

- **R1 — Scaffolding lejos de la visión**: el código actual está más lejos de lo que pensábamos. Rehacer cuesta más que parchear.
- **R2 — Dependencia Anthropic**: cambios en pricing, limits o IP-bans afectan el brazo ejecutor profundo. Mitigación: Hermes-first con modelos alternativos (Kimi, GPT) como principales; Claude solo bajo demanda.
- **R3 — Caso 0 falla**: si Juan no usa el sistema, no hay caso de estudio para el tío ni V1 validado. Mitigación: training en vivo, term sheet con compromiso de uso, check-ins diarios primeras 2 sem.
- **R4 — Backend custom es costosísimo**: construir un Postgres + modelos relacionales + frontend moderno + capa agéntica es exponencialmente más complejo de lo que parece. Cuello de botella técnico.
- **R5 — Comoditización por grandes plataformas**: OpenAI Apps, Google AI Studio, MS Copilot Studio comoditizan el espacio antes de que tengamos tracción.
- **R6 — Target V1 estrecho**: solo-founder/CEO con apetito por self-hosted agéntico puede ser un mercado más pequeño de lo previsto.
- **R7 — Calidad del setup-wizard**: la Capa Core + Capa Identidad genera outputs con errores e inconsistencias frecuentes. La calidad del onboarding agéntico es el cuello de botella técnico real (no la arquitectura).
- **R8 — V2-A destruye márgenes**: PYME low-tech requiere tanto trabajo manual de discovery e integración que destruye márgenes si no se prices alto o se evita.
- **R9 — Riesgo legal Odoo**: si en algún momento se forkea o copia código de Odoo Enterprise sin licencia, problema legal serio. **Mitigación: backend SE INSPIRA en Odoo, NO se forkea / copia / reskina. Cero código Odoo en el repositorio.**
- **R10 — Many con permisos abiertos**: si Many opera con permisos demasiado abiertos, degrada el sistema en lugar de mejorarlo. **Mitigación: niveles L1-L4 estrictos desde día 1; cada nivel requiere logs y revisión.**

---

## 11. Métricas de éxito

### V1 (sem 0-8)

- Caso 0 Juan operando 5 días/sem mínimo durante 4 sem consecutivas.
- Repo reescrito según visión, instalable end-to-end por un tercero.
- 1 intro cualificada al tío en sem 8.
- PRD compartido con 3 personas distintas (Juan, Dani si aplica, otro lead) sin que pidan aclaraciones grandes sobre qué es el producto.

### V1.5 (mes 3-6)

- 3 usuarios pagantes V1 (setup 8-15k€ + retainer 1.5-3k€/mes).
- Primer módulo custom V2 funcionando en al menos 1 cliente.
- Backlog priorizado de módulos = roadmap producto público.

### V2 (mes 6-12)

- Decisión D-DANI cristalizada (partner formal o no).
- Marketplace de módulos (private o curated) con ≥3 módulos disponibles.
- 1-2 clientes V2-B pagantes en producción.

---

## 12. Roadmap

> Plan de ejecución detallado vivo en [`glittery-seeking-bengio.md`](../../../../.claude/plans/glittery-seeking-bengio.md). Necesitará segunda iteración para alinearse con la visión de este PRD.

| Fase | Objetivo |
|---|---|
| **Sem 0** | Auditoría + cierre de decisiones operativas. Cerrar D-BACKEND-STACK + D-MODELS. |
| **Sem 1-2** | Reescritura Capa Identidad + Core + Runtime alineadas con visión Hermes-first. |
| **Sem 3** | Test sintético del onboarding manual (70/30) con perfil ficticio. |
| **Sem 4-5** | Discovery + instalación con Juan. |
| **Sem 6-7** | Operación supervisada Juan. Iteración rápida sobre fricciones. |
| **Sem 8** | Caso de estudio + intro cualificada al tío. |
| **Mes 3+** | V1.5: 3 usuarios pagantes + primer módulo custom V2. |
| **Mes 6+** | Marketplace de módulos + cristalización D-DANI. |
| **Mes 12+** | V2 con clientes en producción. Decisión sobre V3 enterprise. |

---

## Apéndice A — Glosario

- **Skill**: template de capacidad atómica (markdown con instrucciones). Una skill puede spawnear un worker on demand.
- **Worker / subagente**: instancia de ejecución especializada, viva solo durante la ejecución de una skill.
- **Connector**: MCP o API que conecta a un sistema externo (Notion, Stripe, Twilio, etc.).
- **Hermes**: el runtime open-source que orquesta el sistema (gateway, scheduler, skill loader). No es un nodo del flujo, es la mesa sobre la que pasa todo.
- **Listener / cron / watchdog**: los únicos procesos persistentes legítimos. El resto del sistema vive en memoria/logs/files.
- **Capa Identidad**: la parte 30% customizada por usuario (working memory, context files, agentes propios).
- **Capa Core**: la parte 70% preconfigurada (Esbirrillo + skills/agentes genéricos universales).
- **Working memory**: archivo markdown con el estado operativo del usuario; se actualiza con cada acción significativa.

## Apéndice B — Vínculos

- [README del repo](../README.md)
- [ARCHITECTURE.md](../ARCHITECTURE.md) (refleja el scaffolding actual; este PRD presenta hacia dónde converge)
- [INSTALL.md](./INSTALL.md)
- [DECISIONS.md](./DECISIONS.md)
- Plan operativo: `~/.claude/plans/glittery-seeking-bengio.md`
- Canvas runtime: `Life OS/Boards/Producto Agéntico — Runtime Flow.canvas`

---

*Última actualización: 2026-05-09. Este documento es la fuente de verdad de la visión de producto. Si hay conflicto con código del repositorio, gana este documento.*
