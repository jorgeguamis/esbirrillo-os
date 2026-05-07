# Decisions log — Esbirrillo OS

ADRs (Architectural Decision Records) lite. Cada decisión: contexto + opciones + elección + razones.

---

## D1 — Runtime de orquestación

**Fecha:** 2026-05-07

**Contexto:** Sistema fuente (autor del kit) tiene dos runtimes Telegram corriendo: `Hermes-agent` (Nous Research, OSS Python) y `Claude Code + Telegram plugin`. Hay que elegir cuál es el path principal del kit.

**Opciones:**
- A. Hermes-agent (OSS, Nous Research, Python venv aparte)
- B. Solo Claude Code + plugin Telegram official
- C. Stack custom (Anthropic SDK, multi-mes de trabajo)

**Decisión:** **A primario, B alternativo lite.** C descartado para v0.

**Razones:**
- Hermes-agent ya existe, MIT, mantenido. No tiene sentido reinventarlo.
- Capacidades superiores: scheduler nativo, multi-platform, multi-modelo, multi-backend.
- Compatible con `agentskills.io` (estándar abierto que va a crecer).
- B se mantiene como alternativa para usuarios que no quieran Python venv extra.

---

## D2 — Hosting

**Fecha:** 2026-05-07

**Decisión:** **Mac propia para v0.** Documentar paths Mac mini / VPS / Modal como upgrade.

**Razones:**
- Cero infra, latencia local, máxima privacidad.
- Path natural para validar concepto.
- Mac mini (~700€) y Modal serverless documentados como roadmap para usuarios que necesitan siempre-on.

---

## D3 — Comunicación

**Fecha:** 2026-05-07

**Decisión:** **Telegram bot personal v0.** WhatsApp Business documentado como roadmap.

**Razones:**
- Telegram: gratis, soporte multi-grupo (un grupo por agente), API estable, soportado nativamente por Hermes-agent.
- WhatsApp Business requiere número dedicado + setup mayor + costes. Probable upsell para usuarios enterprise.

---

## D4 — Sistema de notas

**Fecha:** 2026-05-07

**Decisión:** **Híbrido. Obsidian opcional, Notion como capa operativa.**

**Razones:**
- Obsidian: ideal para knowledge profundo (markdown, wikilinks, plugins). No todos lo quieren.
- Notion: lo usan todos los CEOs. Es donde vive lo operativo (CRM, tasks, finanzas).
- Sistema soporta ambos vía MCPs. Usuario decide en setup si activa vault Obsidian o no.

---

## D5 — Modelo de almacenamiento de capacidades

**Fecha:** 2026-05-07

**Decisión:** **Repo per-user con upstream común.** Híbrido C.

**Razones:**
- Usuario tiene su fork privado (`<user>-esbirrillo`).
- Upstream (`esbirrillo-os`) actualizable con `git pull upstream main`.
- Capa 5 (identidad) gitignored del upstream — nunca sincroniza.
- Updates al kit no rompen identidad del usuario.

---

## D6 — Plazos del primer caso

**Fecha:** 2026-05-07

**Decisión:** **8 semanas:** auditoría + build + test interno + 4 semanas con primer usuario real.

**Razones:**
- Discovery sólido evita re-trabajo.
- 4 semanas con usuario real permiten medir adopción, no solo setup.

---

## D7 — Capa 4 (Onboarding agéntico) vs fork manual

**Fecha:** 2026-05-07

**Contexto:** Plan inicial proponía un fork manual personalizando el sistema fuente para cada usuario. Refinement: el sistema es replicable solo si la personalización es agéntica.

**Decisión:** **Capa 4 — onboarding agéntico (`/setup-wizard`).** Construir 7 sub-skills que entrevistan al usuario y generan Capa 5 desde cero.

**Razones:**
- Hace el sistema replicable a N usuarios sin re-trabajo del autor.
- El usuario tiene SUS agentes (no copia de los del autor).
- Validación temprana del enfoque antes de escalar a más casos.

**Riesgo asumido:** complejidad mayor en la fase de build. Fallback: discovery manual asistido si la Capa 4 no madura a tiempo.
