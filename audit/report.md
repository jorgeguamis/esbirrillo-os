# Audit Report — Esbirrillo OS extraction

Total files scanned: **2329**

## Summary by category

| Category | Count | Action |
|---|---|---|
| CLEAN | 1602 | Drop into kit as-is |
| NEEDS_CLEANUP | 252 | Parametrize and include |
| PERSONAL | 475 | Exclude or rewrite from scratch |

## Summary by layer

| Layer | CLEAN | NEEDS_CLEANUP | PERSONAL | Total |
|---|---|---|---|---|
| L1-context | 0 | 2 | 24 | 26 |
| L1-hook | 2 | 0 | 2 | 4 |
| L1-meta | 0 | 0 | 1 | 1 |
| L1-script | 6 | 16 | 10 | 32 |
| L1-template | 10 | 2 | 4 | 16 |
| L2-command | 10 | 40 | 6 | 56 |
| L2-skill | 80 | 12 | 56 | 148 |
| L3-agent | 6 | 4 | 12 | 22 |
| L5-context-file | 1330 | 102 | 206 | 1638 |
| L5-framework-filled | 2 | 1 | 5 | 8 |
| L5-journal | 8 | 18 | 109 | 135 |
| other | 148 | 55 | 40 | 243 |

## Top 30 most personal files (highest hit count)

| File | Layer | Hits | Top categories |
|---|---|---|---|
| `Life OS/00. Inbox/fireflies/2026-05-02 Jorge Javier Semanal - Fireflies.md` | other | 1620 | jorge(1008), people(612) |
| `Life OS/00. Inbox/fireflies/2026-05-02 Jorge Javier Semanal - Fireflies.json` | other | 1619 | jorge(1007), people(612) |
| `Life OS/02. Areas/business_360/clientes/archivo/Davide Bonomi/Onboarding- Davide Bonomi.json` | L5-context-file | 915 | jorge(914), revolutia(1) |
| `Life OS/.smart-env/smart_env.json` | other | 190 | clients_360(190) |
| `Life OS/02. Areas/business_360/clientes/archivo/Spain Is Excellence/SIE - Transcript Reu Adriana - 17-04-2026.md` | L5-context-file | 158 | jorge(76), people(73), clients_360(7) |
| `.claude/config/hermes-crons-v1.json` | L1-context | 110 | jorge(65), hardcoded_paths(32), revolutia(7) |
| `Life OS/.claude/config/hermes-crons-v1.json` | L1-context | 110 | jorge(65), hardcoded_paths(32), revolutia(7) |
| `Life OS/02. Areas/business_revolutia/Revolutia IA PRO - OFERTA PRINCIPAL.md` | L5-context-file | 109 | revolutia(91), jorge(18) |
| `.claude/settings.local.json` | other | 102 | jorge(41), hardcoded_paths(36), business_360(11) |
| `Life OS/.claude/settings.local.json` | other | 102 | jorge(41), hardcoded_paths(36), business_360(11) |
| `Life OS/02. Areas/business_Monk/roadmaps/Análisis Estratégico - Playbooks aplicados a Monk.md` | L5-context-file | 85 | monk(82), jorge(2), business_360(1) |
| `Life OS/02. Areas/business_360/clientes/activos/LabArmonia/04. Diagnóstico/Auditoría de Procesos/consolidado/Roadmap.md` | L5-context-file | 82 | business_360(49), jorge(20), clients_360(13) |
| `Life OS/02. Areas/personal/diario/02. Weekly/2026-W03.md` | L5-journal | 79 | revolutia(43), business_360(30), clients_360(4) |
| `Life OS/02. Areas/business_360/clientes/archivo/Spain Is Excellence/SIE - Estructura Formación Excelenc-IA.md` | L5-context-file | 76 | jorge(40), people(29), clients_360(4) |
| `Life OS/02. Areas/business_Monk/roadmaps/Roadmap Producto.md` | L5-context-file | 76 | monk(75), jorge(1) |
| `CLAUDE.md` | L1-meta | 73 | business_360(27), revolutia(23), jorge(11) |
| `Life OS/02. Areas/personal/diario/02. Weekly/2026-W06.md` | L5-journal | 72 | clients_360(38), revolutia(21), business_360(8) |
| `Life OS/02. Areas/personal/diario/02. Weekly/2026-W02.md` | L5-journal | 71 | business_360(37), revolutia(33), monk(1) |
| `Life OS/02. Areas/personal/diario/01. Daily/07-05-2026.md` | L5-journal | 69 | clients_360(26), people(16), revolutia(12) |
| `Life OS/02. Areas/personal/diario/01. Daily/06-05-2026.md` | L5-journal | 67 | clients_360(28), people(14), revolutia(13) |
| `Life OS/03. Sistema/stack.md` | other | 67 | revolutia(25), jorge(21), business_360(16) |
| `Life OS/02. Areas/business_revolutia/Revolutia.md` | L5-context-file | 63 | revolutia(36), jorge(19), business_360(6) |
| `Life OS/02. Areas/personal/diario/01. Daily/21-04-2026.md` | L5-journal | 63 | clients_360(35), jorge(9), people(8) |
| `Life OS/02. Areas/business_360/clientes/activos/Burrito Blanco/03. Upsell Imágenes IA/Script Onboarding - Burrito Blanco 21-04-2026.md` | L5-context-file | 58 | people(28), jorge(20), clients_360(5) |
| `.claude/commands/morning.md` | L2-command | 57 | business_360(23), jorge(20), revolutia(12) |
| `Life OS/.claude/commands/morning.md` | L2-command | 57 | business_360(23), jorge(20), revolutia(12) |
| `.claude/LIFE-OS.md` | other | 56 | jorge(22), business_360(18), revolutia(16) |
| `Life OS/.claude/LIFE-OS.md` | other | 56 | jorge(22), business_360(18), revolutia(16) |
| `Life OS/02. Areas/personal/diario/02. Weekly/2026-W16.md` | L5-journal | 56 | clients_360(19), jorge(11), monk(8) |
| `Life OS/00. Inbox/selenia/Selenia Report - 2026-05-03.md` | other | 55 | jorge(36), hardcoded_paths(19) |

## CLEAN files (drop in as-is) by layer

### L1-hook (2 files)

- `.claude/hooks/validate-tags-after-edit.sh`
- `Life OS/.claude/hooks/validate-tags-after-edit.sh`

### L1-script (6 files)

- `.claude/execution/README.md`
- `.claude/execution/approval_item.schema.json`
- `.claude/scripts/get_youtube_transcript.py`
- `Life OS/.claude/execution/README.md`
- `Life OS/.claude/execution/approval_item.schema.json`
- `Life OS/.claude/scripts/get_youtube_transcript.py`

### L1-template (10 files)

- `Life OS/03. Sistema/templates/Base Note.md`
- `Life OS/03. Sistema/templates/Book Note.md`
- `Life OS/03. Sistema/templates/Future Self Interview - Template.md`
- `Life OS/03. Sistema/templates/Ideal Life Costing - Template.md`
- `Life OS/03. Sistema/templates/Identity and Values Interview - Template.md`
- `Life OS/03. Sistema/templates/KoreNote Template.md`
- `Life OS/03. Sistema/templates/Life Map - Template.md`
- `Life OS/03. Sistema/templates/Output - Newsletter Outline.md`
- `Life OS/03. Sistema/templates/Source Note.md`
- `Life OS/03. Sistema/templates/Vivid Vision Framework - Template.md`

### L2-command (10 files)

- `.claude/commands/capture.md`
- `.claude/commands/create-atomic.md`
- `.claude/commands/digital-cleanup.md`
- `.claude/commands/quarterly-review.md`
- `.claude/commands/weekly-plan.md`
- `Life OS/.claude/commands/capture.md`
- `Life OS/.claude/commands/create-atomic.md`
- `Life OS/.claude/commands/digital-cleanup.md`
- `Life OS/.claude/commands/quarterly-review.md`
- `Life OS/.claude/commands/weekly-plan.md`

### L2-skill (80 files)

- `.claude/skills/json-canvas/SKILL.md`
- `.claude/skills/n8n-code-javascript/BUILTIN_FUNCTIONS.md`
- `.claude/skills/n8n-code-javascript/COMMON_PATTERNS.md`
- `.claude/skills/n8n-code-javascript/DATA_ACCESS.md`
- `.claude/skills/n8n-code-javascript/ERROR_PATTERNS.md`
- `.claude/skills/n8n-code-javascript/README.md`
- `.claude/skills/n8n-code-javascript/SKILL.md`
- `.claude/skills/n8n-code-python/COMMON_PATTERNS.md`
- `.claude/skills/n8n-code-python/DATA_ACCESS.md`
- `.claude/skills/n8n-code-python/ERROR_PATTERNS.md`
- `.claude/skills/n8n-code-python/README.md`
- `.claude/skills/n8n-code-python/SKILL.md`
- `.claude/skills/n8n-code-python/STANDARD_LIBRARY.md`
- `.claude/skills/n8n-expression-syntax/COMMON_MISTAKES.md`
- `.claude/skills/n8n-expression-syntax/EXAMPLES.md`
- `.claude/skills/n8n-expression-syntax/README.md`
- `.claude/skills/n8n-expression-syntax/SKILL.md`
- `.claude/skills/n8n-mcp-tools-expert/README.md`
- `.claude/skills/n8n-mcp-tools-expert/SEARCH_GUIDE.md`
- `.claude/skills/n8n-mcp-tools-expert/SKILL.md`
- `.claude/skills/n8n-mcp-tools-expert/VALIDATION_GUIDE.md`
- `.claude/skills/n8n-mcp-tools-expert/WORKFLOW_GUIDE.md`
- `.claude/skills/n8n-node-configuration/DEPENDENCIES.md`
- `.claude/skills/n8n-node-configuration/OPERATION_PATTERNS.md`
- `.claude/skills/n8n-node-configuration/README.md`
- `.claude/skills/n8n-node-configuration/SKILL.md`
- `.claude/skills/n8n-validation-expert/ERROR_CATALOG.md`
- `.claude/skills/n8n-validation-expert/FALSE_POSITIVES.md`
- `.claude/skills/n8n-validation-expert/README.md`
- `.claude/skills/n8n-validation-expert/SKILL.md`
- `.claude/skills/n8n-workflow-patterns/README.md`
- `.claude/skills/n8n-workflow-patterns/SKILL.md`
- `.claude/skills/n8n-workflow-patterns/ai_agent_workflow.md`
- `.claude/skills/n8n-workflow-patterns/database_operations.md`
- `.claude/skills/n8n-workflow-patterns/http_api_integration.md`
- `.claude/skills/n8n-workflow-patterns/scheduled_tasks.md`
- `.claude/skills/n8n-workflow-patterns/webhook_processing.md`
- `.claude/skills/obsidian-bases/SKILL.md`
- `.claude/skills/obsidian-markdown/SKILL.md`
- `.claude/skills/reading-capture/SKILL.md`
- `Life OS/.claude/skills/json-canvas/SKILL.md`
- `Life OS/.claude/skills/n8n-code-javascript/BUILTIN_FUNCTIONS.md`
- `Life OS/.claude/skills/n8n-code-javascript/COMMON_PATTERNS.md`
- `Life OS/.claude/skills/n8n-code-javascript/DATA_ACCESS.md`
- `Life OS/.claude/skills/n8n-code-javascript/ERROR_PATTERNS.md`
- `Life OS/.claude/skills/n8n-code-javascript/README.md`
- `Life OS/.claude/skills/n8n-code-javascript/SKILL.md`
- `Life OS/.claude/skills/n8n-code-python/COMMON_PATTERNS.md`
- `Life OS/.claude/skills/n8n-code-python/DATA_ACCESS.md`
- `Life OS/.claude/skills/n8n-code-python/ERROR_PATTERNS.md`
- … and 30 more

### L3-agent (6 files)

- `.claude/agents/connections-agent.md`
- `.claude/agents/tagging-agent.md`
- `.claude/agents/validate-frontmatter.md`
- `Life OS/.claude/agents/connections-agent.md`
- `Life OS/.claude/agents/tagging-agent.md`
- `Life OS/.claude/agents/validate-frontmatter.md`

### L5-context-file (1330 files)

- `Life OS/02. Areas/aprendizaje/cursos/Agentic Workflows - Maker School - Nick Saraev.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/_index.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/01-onboarding-guide/01-welcome-to-make-money-with-make.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/01-onboarding-guide/02-best-of-make-money-with-make.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/01-onboarding-guide/03-community-structure-events.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/01-onboarding-guide/04-tool-stack-affiliates-discounts.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/01-onboarding-guide/05-daily-checklist-to-grow-quickly.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/01-ai-content-generator-flow.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/02-upwork-rss-feed-customization.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/03-email-autoresponder.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/04-webhook-slides-proposal-generator.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/05-the-basic-crm-automations-clickup.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/06-connect-any-api-to-make-example.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/07-automate-slack-with-make-example.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/08-7-figure-hiring-system.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/09-how-to-scrape-websites-w-make.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/10-iterators-aggregators-example.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/11-photography-crm-build.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/12-hidden-api-masterclass.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/13-blandai-voice-bot-flow.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/14-instagram-scraper.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/15-contractor-payroll-hourly-contract-flat-salary.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/16-g-drive-email-enrich-flow.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/17-youtube-to-blog-post-generator.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/18-newsletter-to-mp3-generator.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/19-automatic-lead-magnet-generator.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/20-slack-button-approval-system.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/21-twitter-parasite-flow.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/22-indeed-resume-customizer-flow.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/23-scrape-ig-daily-add-to-looker.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/24-ai-parasite-seo-system.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/25-generate-images-with-bannerbear.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/26-onboarding-create-trello-board.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/27-search-rows-generate-wp-posts.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/28-social-media-syndicator-flow.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/29-watch-payment-intent-update-cu.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/30-clickup-status-send-invoice.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/31-the-100-automated-newsletter-reddit-scraper.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/32-community-blueprints.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/33-curated-mmwm-text-resources.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/34-calendar-booking-crm-upsert-ai-autoresponse.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/35-call-transcript-ai-generated-proposal-recap.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/36-payment-onboarding-welcome-barrage-crm-update.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/37-claude-code-instant-workflows-setup.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/38-n8n-infinite-data-scraper-ai-extraction.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/39-n8n-reddit-product-idea-generator.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/40-instantlyai-autoreply-bot-in-n8n.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/41-end-to-end-clickup-typeform-n8n-hiring-pipeline.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/42-automated-bookkeeper.md`
- `Life OS/02. Areas/aprendizaje/cursos/nick-saraev-skool/make-money-with-make/02-template-library/43-deep-content-generator.md`
- … and 1280 more

### L5-framework-filled (2 files)

- `Life OS/02. Areas/personal/frameworks/Principles.md`
- `Life OS/02. Areas/personal/frameworks/Winner Worksheet.md`

### L5-journal (8 files)

- `Life OS/02. Areas/personal/diario/00. Themed/Revisión de Desarrollo Personal 16-11-2025.md`
- `Life OS/02. Areas/personal/diario/01. Daily/10-11-2025.md`
- `Life OS/02. Areas/personal/diario/01. Daily/11-11-2025.md`
- `Life OS/02. Areas/personal/diario/01. Daily/17-11-2025.md`
- `Life OS/02. Areas/personal/diario/01. Daily/30-07-2025.md`
- `Life OS/02. Areas/personal/diario/01. Daily/31-07-2025.md`
- `Life OS/02. Areas/personal/diario/01. Daily/31-07-2025_night.md`
- `Life OS/02. Areas/personal/diario/02. Weekly/Weekly Reflection 13_10_25 - 19_10_25.md`

### other (148 files)

- `.claude/launch.json`
- `.claude/settings.json`
- `Life OS/.claude/launch.json`
- `Life OS/.claude/settings.json`
- `Life OS/.mcp.json`
- `Life OS/00. Inbox/$100M Virtual Launch Workshop.md`
- `Life OS/00. Inbox/01.Validación del Problema y Demanda.md`
- `Life OS/00. Inbox/20-02-2026.md`
- `Life OS/00. Inbox/2026-02.md`
- `Life OS/00. Inbox/360º Business Model.md`
- `Life OS/00. Inbox/A Guide to Claude Code 2.0 and getting better at using coding agents.md`
- `Life OS/00. Inbox/AI Agent Org Chart.md`
- `Life OS/00. Inbox/Al cliente no le importas, solo le importa su persona. Y cuando estás en los negocios, lo único que te tiene que importar es tu cliente, resolver su problema y llevarlo a su situación deseada..md`
- `Life OS/00. Inbox/Alannia.md`
- `Life OS/00. Inbox/Alex Hormozi — Writing Guidelines.md`
- `Life OS/00. Inbox/Alternatives Space.md`
- `Life OS/00. Inbox/Caso de éxito alumno revolutia que ha vendido una solución antes de empezar la formación.md`
- `Life OS/00. Inbox/Causa y Efecto.md`
- `Life OS/00. Inbox/Claude Code.md`
- `Life OS/00. Inbox/Claude Cowork The Ultimate Guide.md`
- `Life OS/00. Inbox/Como Crear un Lead Magnet Efectivo.md`
- `Life OS/00. Inbox/Convertir fotos de pinterest en posts para linkedin.md`
- `Life OS/00. Inbox/Creación de presentaciones .md`
- `Life OS/00. Inbox/Datos Necesarios Dream 100.md`
- `Life OS/00. Inbox/Descripción de Perfil Personal - Jorge Guamis.md`
- `Life OS/00. Inbox/Eden – The AI Drive & Canvas.md`
- `Life OS/00. Inbox/Editee - Herramienta.md`
- `Life OS/00. Inbox/Eres 100% responsable de donde estás en la vida. Financiera, física y mentalmente. Es exactamente como TU lo has diseñado..md`
- `Life OS/00. Inbox/Extensión para crear workflows con IA desde n8n.md`
- `Life OS/00. Inbox/Formula M.A.G.I.C.md`
- `Life OS/00. Inbox/Give customers what they want now, so you can give them what they need later.md`
- `Life OS/00. Inbox/Happiness is an attitude. We either make ourselves miserable, or happy and strong. The amount of work is the same..md`
- `Life OS/00. Inbox/Hard Selling Is For Weak Products.md`
- `Life OS/00. Inbox/How to Actually get Ahead with AI .md`
- `Life OS/00. Inbox/How to Automate ANY Content with Poppy and n8n (no code).md`
- `Life OS/00. Inbox/Iván Godia.md`
- `Life OS/00. Inbox/Just focus on getting the next customer..md`
- `Life OS/00. Inbox/La Conciencia.md`
- `Life OS/00. Inbox/La felicidad es una elección.md`
- `Life OS/00. Inbox/Las personas a las que mejor les va no hacen lo que hace todo el mundo..md`
- `Life OS/00. Inbox/Libros sobre comportamiento .md`
- `Life OS/00. Inbox/Make Everyone A Winner..md`
- `Life OS/00. Inbox/Menos trabajadores > Más trabajadores .md`
- `Life OS/00. Inbox/Método de prospección con cartas a mano para negocio local.md`
- `Life OS/00. Inbox/Nadie puede convencer a otro de que cambie. Cada uno custodia una puerta del cambio que solo puede abrirse desde dentro. No podemos abrir la puerta de otro, ni con argumentos ni con apelaciones emocionales..md`
- `Life OS/00. Inbox/No tengas miedo de ser tu y hacer lo que quieras hacer por miedo a no encajar.md`
- `Life OS/00. Inbox/Reality Transurfing Explained In 43 Minutes.md`
- `Life OS/00. Inbox/Si no sacrificas nada no conseguirás nada, pero si sacrificas todo al menos conseguirás algo..md`
- `Life OS/00. Inbox/Skill Stacking.md`
- `Life OS/00. Inbox/Solo tienes que encontrar que quiere la gente y vendérselo.md`
- … and 98 more

## NEEDS_CLEANUP files (parametrize)

| File | Layer | Hits | Sample line |
|---|---|---|---|
| `.claude/commands/monthly-review.md` | L2-command | 5 | L12: 2. **Hábitos** — query Notion Habits DB (DB: `a7b99031-cc18-4a26-bc9c-db712 |
| `.claude/commands/route-task.md` | L2-command | 5 | L2: description: Recomienda la ruta Helios para una tarea: Hermes directo, Claud |
| `.claude/commands/telegram-signal.md` | L2-command | 5 | L20: python3 /Users/jorgeguamis/Desktop/.claude/execution/telegram_signal.py <<' |
| `.claude/commands/weekly-review.md` | L2-command | 5 | L32: - `02. Areas/business_360/360 Consulting.md` |
| `.claude/execution/helios_healthcheck.py` | L1-script | 5 | L19: WORKSPACE = Path(os.environ.get("JORGE_WORKSPACE", "/Users/jorgeguamis/Desk |
| `Life OS/.claude/commands/monthly-review.md` | L2-command | 5 | L12: 2. **Hábitos** — query Notion Habits DB (DB: `a7b99031-cc18-4a26-bc9c-db712 |
| `Life OS/.claude/commands/route-task.md` | L2-command | 5 | L2: description: Recomienda la ruta Helios para una tarea: Hermes directo, Claud |
| `Life OS/.claude/commands/telegram-signal.md` | L2-command | 5 | L20: python3 /Users/jorgeguamis/Desktop/.claude/execution/telegram_signal.py <<' |
| `Life OS/.claude/commands/weekly-review.md` | L2-command | 5 | L32: - `02. Areas/business_360/360 Consulting.md` |
| `Life OS/.claude/execution/helios_healthcheck.py` | L1-script | 5 | L19: WORKSPACE = Path(os.environ.get("JORGE_WORKSPACE", "/Users/jorgeguamis/Desk |
| `Life OS/01. Atomic Notes/Indirect Messaging Strategy.md` | other | 5 | L41: ## Aplicación para Jorge |
| `Life OS/02. Areas/aprendizaje/_README.md` | L5-context-file | 5 | L7: Funciona como la base de conocimiento que alimenta tanto el crecimiento pers |
| `Life OS/02. Areas/business_360/clientes/activos/CPD Electricidad/03. Onboarding/Contrato CPD Electricidad 360 Consulting.md` | L5-context-file | 5 | L7: **DAVID FERNÁNDEZ COLADO**, autónomo con NIF **44518490N**, con domicilio en |
| `Life OS/02. Areas/business_360/clientes/activos/Cuchillas Castillo/01. Discovery/Cuchillas Castillo - Discovery Call Script.md` | L5-context-file | 5 | L7: company: Cuchillas Castillo |
| `Life OS/02. Areas/business_360/clientes/activos/Cuchillas Castillo/04. Diagnóstico/Auditoría de Procesos/empleados/Jorge Escoda Motilla.md` | L5-context-file | 5 | L9: # Jorge Escoda Motilla — Comercial (Jordi) |
| `Life OS/02. Areas/business_360/clientes/activos/Cuchillas Castillo/05. Sensibilización/Handout 1 Página.md` | L5-context-file | 5 | L7: company: Cuchillas Castillo |
| `Life OS/02. Areas/business_360/clientes/activos/LabArmonia/04. Diagnóstico/Auditoría de Procesos/empleados/Almudena Jimenez.md` | L5-context-file | 5 | L42: - También hace tareas fuera de su rol: fichas PrestaShop, banners web, edic |
| `Life OS/02. Areas/business_360/clientes/leads (pipeline)/Quality Energy Consulting/Quality Energy Consulting - Discovery Call.md` | L5-context-file | 5 | L104: "Ángel, ¿qué tal? Soy Jorge, de 360 Consulting. |
| `Life OS/02. Areas/business_360/sops/Script Discovery Call - Base.md` | L5-context-file | 5 | L11: # Script Discovery Call - 360º Consulting |
| `Life OS/02. Areas/business_revolutia/clases/2026-05-06 - Jornada Bienvenida - Guion Rápido Jorge.md` | L5-context-file | 5 | L2: ## Guion Rápido para Jorge |
| `Life OS/02. Areas/business_revolutia/proyectos/Auditoría de Procesos/consolidado/Mapa de Procesos.md` | L5-context-file | 5 | L4: - business/revolutia |
| `Life OS/02. Areas/business_revolutia/proyectos/Auditoría de Procesos/empleados/Cristina Rojas - Administrativo.md` | L5-context-file | 5 | L2: tags: [revolutia, auditoría, empleado] |
| `Life OS/02. Areas/business_revolutia/proyectos/Validar SAAS Revolutia/Workshop Materials/Scripts/Script-Cold-Call.md` | L5-context-file | 5 | L40: "Hola [Nombre], soy [Tu Nombre] de Revolutia. |
| `Life OS/02. Areas/personal/diario/01. Daily/12-04-2026.md` | L5-journal | 5 | L22: **Current state:** Domingo W15, de vuelta en Valencia. Calendario VACÍO. Se |
| `Life OS/02. Areas/personal/diario/01. Daily/25-01-2026.md` | L5-journal | 5 | L45: ## 💼 Business - 360º Consulting |
| `.claude/agents/shakes.md` | L3-agent | 4 | L1: # Shakes — Copywriter 360º |
| `.claude/commands/approval-item.md` | L2-command | 4 | L12: python3 /Users/jorgeguamis/Desktop/.claude/execution/approval_item.py <<'JS |
| `.claude/commands/class-prep.md` | L2-command | 4 | L2: description: "Preparar clase de Revolutia Academy. Consulta calendario, revi |
| `.claude/commands/financial-review.md` | L2-command | 4 | L12: Expenses: notion-database-query DB "2d21320d-44b1-4a17-8311-fc92269b018e" ( |
| `.claude/commands/helios-healthcheck.md` | L2-command | 4 | L12: python3 /Users/jorgeguamis/Desktop/.claude/execution/helios_healthcheck.py |
| `.claude/commands/invoice.md` | L2-command | 4 | L2: description: Generar factura 360º Consulting. Busca cliente en CRM, genera n |
| `.claude/commands/new-lead.md` | L2-command | 4 | L2: description: Añadir nuevo lead al CRM de 360º — research, Notion, y nota en  |
| `.claude/context/constraints.md` | L1-context | 4 | L19: - Secretos/API keys: no mostrarlos en respuestas, no guardarlos en memoria, |
| `.claude/execution/approval_item.py` | L1-script | 4 | L21: WORKSPACE = Path(os.environ.get("JORGE_WORKSPACE", "/Users/jorgeguamis/Desk |
| `.claude/scripts/claude-telegram.sh` | L1-script | 4 | L5: cd /Users/jorgeguamis/Desktop |
| `.claude/skills/daily-reflection/SKILL.md` | L2-skill | 4 | L3: agent: jorge |
| `Life OS/.claude/agents/shakes.md` | L3-agent | 4 | L1: # Shakes — Copywriter 360º |
| `Life OS/.claude/commands/approval-item.md` | L2-command | 4 | L12: python3 /Users/jorgeguamis/Desktop/.claude/execution/approval_item.py <<'JS |
| `Life OS/.claude/commands/class-prep.md` | L2-command | 4 | L2: description: "Preparar clase de Revolutia Academy. Consulta calendario, revi |
| `Life OS/.claude/commands/financial-review.md` | L2-command | 4 | L12: Expenses: notion-database-query DB "2d21320d-44b1-4a17-8311-fc92269b018e" ( |
| `Life OS/.claude/commands/helios-healthcheck.md` | L2-command | 4 | L12: python3 /Users/jorgeguamis/Desktop/.claude/execution/helios_healthcheck.py |
| `Life OS/.claude/commands/invoice.md` | L2-command | 4 | L2: description: Generar factura 360º Consulting. Busca cliente en CRM, genera n |
| `Life OS/.claude/commands/new-lead.md` | L2-command | 4 | L2: description: Añadir nuevo lead al CRM de 360º — research, Notion, y nota en  |
| `Life OS/.claude/context/constraints.md` | L1-context | 4 | L19: - Secretos/API keys: no mostrarlos en respuestas, no guardarlos en memoria, |
| `Life OS/.claude/execution/approval_item.py` | L1-script | 4 | L21: WORKSPACE = Path(os.environ.get("JORGE_WORKSPACE", "/Users/jorgeguamis/Desk |
| `Life OS/.claude/scripts/claude-telegram.sh` | L1-script | 4 | L5: cd /Users/jorgeguamis/Desktop |
| `Life OS/.claude/skills/daily-reflection/SKILL.md` | L2-skill | 4 | L3: agent: jorge |
| `Life OS/00. Inbox/selenia/Overnight Bootstrap - 2026-05-03.md` | other | 4 | L8: - Healthcheck report: /Users/jorgeguamis/Desktop/Life OS/00. Inbox/selenia/H |
| `Life OS/00. Inbox/selenia/Overnight Cycle - 2026-05-06-1251.md` | other | 4 | L42: - Jorge genera señales manualmente vía comando `/telegram-signal`. |
| `Life OS/01. Atomic Notes/Content Dialectics.md` | other | 4 | L46: ## Aplicación para Jorge |
| `Life OS/01. Atomic Notes/Pioneer Trademark Marketing.md` | other | 4 | L46: ## Aplicación para Jorge |
| `Life OS/01. Atomic Notes/Self-Driving Community Model.md` | other | 4 | L7: - area/business-revolutia |
| `Life OS/01. Atomic Notes/Trust Economy.md` | other | 4 | L43: ## Aplicación para Jorge |
| `Life OS/01. Atomic Notes/Visual-Verbal Branding Sync.md` | other | 4 | L45: ## Aplicación para Jorge |
| `Life OS/02. Areas/business_360/clientes/activos/CPD Electricidad/01. Discovery/CPD Electricidad - David Fernandez - Sales Call Script.md` | L5-context-file | 4 | L7: company: CPD Electricidad |
| `Life OS/02. Areas/business_360/clientes/activos/Cuchillas Castillo/04. Diagnóstico/Auditoría de Procesos/consolidado/Mapa de Procesos.md` | L5-context-file | 4 | L10: # Mapa de Procesos — Cuchillas Castillo |
| `Life OS/02. Areas/business_360/clientes/activos/LabArmonia/04. Diagnóstico/Auditoría de Procesos/empleados/Jorge Olmedo.md` | L5-context-file | 4 | L8: # Jorge Olmedo Díaz — Responsable Departamento Ventas Nacional |
| `Life OS/02. Areas/business_360/clientes/activos/LabArmonia/04. Diagnóstico/Auditoría de Procesos/empleados/Marina Fernando Ferrando.md` | L5-context-file | 4 | L13: **Entrevista:** 17-03-2026 (54 min) — Jorge Guamis vía Google Meet |
| `Life OS/02. Areas/business_360/clientes/activos/LabArmonia/04. Diagnóstico/Auditoría de Procesos/seguimiento/Plan Touchpoints Alfonso - 22-04-2026.md` | L5-context-file | 4 | L8: client: LabArmonia |
| `Life OS/02. Areas/business_360/clientes/archivo/Calzados Keslem/Calzados Keslem - Génesis - Discovery Call.md` | L5-context-file | 4 | L464: **2. Actualizar CRM (Notion 360º)** |
| `Life OS/02. Areas/business_360/clientes/archivo/Noctorial/Noctorial - Jaime - Discovery Call.md` | L5-context-file | 4 | L5: - revolutia |
| `Life OS/02. Areas/business_360/clientes/archivo/SINBLAT/SINBLAT - Discovery Call Prep.md` | L5-context-file | 4 | L31: 4. **Validar fit** - ¿Son buen cliente para 360º? ¿Tienen budget, autoridad |
| `Life OS/02. Areas/business_360/clientes/leads (pipeline)/Querkus/Querkus - Discovery Call.md` | L5-context-file | 4 | L144: "José Luis, Paola, ¿qué tal? Soy Jorge, de 360 Consulting. |
| `Life OS/02. Areas/business_revolutia/proyectos/Auditoría de Procesos/consolidado/Cuellos de Botella.md` | L5-context-file | 4 | L4: - business/revolutia |
| `Life OS/02. Areas/business_revolutia/proyectos/Auditoría de Procesos/consolidado/Mapa de Herramientas.md` | L5-context-file | 4 | L4: - business/revolutia |
| `Life OS/02. Areas/business_revolutia/proyectos/Auditoría de Procesos/iniciativas/Doc Maestro Lanzamiento/06 - Biblioteca de Angles y Hooks.md` | L5-context-file | 4 | L4: - business/revolutia |
| `Life OS/02. Areas/business_revolutia/proyectos/FigJam - Cambios Manuales Pendientes.md` | L5-context-file | 4 | L3: - revolutia |
| `Life OS/02. Areas/investigacion/proyectos/VISUAL AI SOFTWARE/00. Fundamentos/Patrones de Éxito y Fracaso en Software - Análisis para Visual AI.md` | L5-context-file | 4 | L33: - **Founder-market fit:** Jorge es el usuario ideal (multipotencial, visual |
| `Life OS/02. Areas/personal/diario/01. Daily/06-03-2026.md` | L5-journal | 4 | L44: ## 💼 Business - 360º Consulting |
| `Life OS/02. Areas/personal/diario/01. Daily/07-03-2026.md` | L5-journal | 4 | L44: ## 💼 Business - 360º Consulting |
| `Life OS/02. Areas/personal/diario/01. Daily/20-02-2026.md` | L5-journal | 4 | L44: ## 💼 Business - 360º Consulting |
| `Life OS/02. Areas/personal/diario/01. Daily/21-02-2026.md` | L5-journal | 4 | L44: ## 💼 Business - 360º Consulting |
| `Life OS/02. Areas/personal/diario/01. Daily/24-02-2026.md` | L5-journal | 4 | L44: ## 💼 Business - 360º Consulting |
| `Life OS/02. Areas/personal/diario/01. Daily/24-03-2026.md` | L5-journal | 4 | L44: ## 💼 Business - 360º Consulting |
| `Life OS/02. Areas/personal/diario/01. Daily/28-03-2026.md` | L5-journal | 4 | L44: ## 💼 Business - 360º Consulting |
| `Life OS/02. Areas/personal/relaciones/_README.md` | L5-context-file | 4 | L20: - **Alex Gimeno** — Socio 360º Consulting, amigo cercano |
| `Life OS/03. Sistema/templates/Daily Note.md` | L1-template | 4 | L44: ## 💼 Business - 360º Consulting |
| `.claude/commands/expense.md` | L2-command | 3 | L14: - `"cobré 5000 de ArmoniaBio"` → ingreso |
| `.claude/commands/pipeline.md` | L2-command | 3 | L2: description: Ver estado actual del pipeline de ventas de 360º Consulting |
| `.claude/commands/proposal-to-html.md` | L2-command | 3 | L6: 3. Genera el HTML con el design system 360º (dark theme, animaciones reveal, |
| `.claude/skills/audit-processor/SKILL.md` | L2-skill | 3 | L3: description: "Procesa auditorías de procesos empresariales (360º Consulting) |
| `.claude/skills/content-pipeline/SKILL.md` | L2-skill | 3 | L62: **Checkpoint:** ⚠️ Presentar lista a Jorge para que elija cuáles crear |
| `Life OS/.claude/commands/expense.md` | L2-command | 3 | L14: - `"cobré 5000 de ArmoniaBio"` → ingreso |
| `Life OS/.claude/commands/pipeline.md` | L2-command | 3 | L2: description: Ver estado actual del pipeline de ventas de 360º Consulting |
| `Life OS/.claude/commands/proposal-to-html.md` | L2-command | 3 | L6: 3. Genera el HTML con el design system 360º (dark theme, animaciones reveal, |
| `Life OS/.claude/skills/audit-processor/SKILL.md` | L2-skill | 3 | L3: description: "Procesa auditorías de procesos empresariales (360º Consulting) |
| `Life OS/.claude/skills/content-pipeline/SKILL.md` | L2-skill | 3 | L62: **Checkpoint:** ⚠️ Presentar lista a Jorge para que elija cuáles crear |
| `Life OS/00. Inbox/selenia/Overnight Cycle - 2026-05-03-0052.md` | other | 3 | L14: 1. **Ruta canónica de `.claude` como symlink:** `log_event.py` fue ajustado |
| `Life OS/01. Atomic Notes/Atomic Note.md` | other | 3 | L7: - business/[360\|revolutia\|both] |
| `Life OS/01. Atomic Notes/Clawdbot.md` | other | 3 | L119: \| **Proactividad** \| Detecta patrones y alerta automáticamente \| Reacti |
| `Life OS/01. Atomic Notes/Glosario de Términos de IA.md` | other | 3 | L8: - area/business-revolutia |
| `Life OS/01. Atomic Notes/Storytelling Fantasy Loop.md` | other | 3 | L50: ## Aplicación para Jorge |
| `Life OS/02. Areas/business_360/100M Playbooks - Diagnóstico de Negocio.md` | L5-context-file | 3 | L10: related: "[[100M Playbooks]], [[360 Consulting]]" |
| `Life OS/02. Areas/business_360/clientes/activos/Cuchillas Castillo/03. Onboarding/Contrato Cuchillas Castillo 360 Consulting.md` | L5-context-file | 3 | L192: Todos los entregables son propiedad exclusiva del Cliente para su uso en e |
| `Life OS/02. Areas/business_360/clientes/activos/Cuchillas Castillo/04. Diagnóstico/Auditoría de Procesos/Cuchillas Castillo - Update Nacho 13-03-2026.md` | L5-context-file | 3 | L6: # Cuchillas Castillo — Update para Nacho \| 13-03-2026 |
| `Life OS/02. Areas/business_360/clientes/activos/Cuchillas Castillo/04. Diagnóstico/Auditoría de Procesos/consolidado/Mapa de Herramientas.md` | L5-context-file | 3 | L10: # Mapa de Herramientas — Cuchillas Castillo |
| `Life OS/02. Areas/business_360/clientes/activos/Cuchillas Castillo/04. Diagnóstico/Auditoría de Procesos/empleados/Ignacio Sáez.md` | L5-context-file | 3 | L21: "De todo un poco." — Sin rol formal definido. **Ampliado en entrevista:** J |
| `Life OS/02. Areas/business_360/clientes/activos/Cuchillas Castillo/04. Diagnóstico/Auditoría de Procesos/empleados/Paula Marco Manzanares.md` | L5-context-file | 3 | L103: "Teletrabajar." — Confirmado en entrevista: motivación personal/laboral. I |
| `Life OS/02. Areas/business_360/clientes/activos/Cuchillas Castillo/05. Sensibilización/Casos de Uso Detallados.md` | L5-context-file | 3 | L7: company: Cuchillas Castillo |
| `Life OS/02. Areas/business_360/clientes/activos/Cuchillas Castillo/05. Sensibilización/Prep Checklist.md` | L5-context-file | 3 | L7: company: Cuchillas Castillo |
| `Life OS/02. Areas/business_360/clientes/archivo/Calzados Keslem/Calzados Keslem - Call Log 2026-02-11.md` | L5-context-file | 3 | L3: **Participantes:** Jorge Guamis, Génesis (Keslem) |
| `Life OS/02. Areas/business_360/clientes/archivo/Tictacarea/Tictacarea - Juan Angel.md` | L5-context-file | 3 | L66: ## Análisis para 360º |
| `Life OS/02. Areas/business_Monk/operativa/Notion Monk - Areas Registry.md` | L5-context-file | 3 | L10: # Notion Monk — Areas Registry |
| `Life OS/02. Areas/business_Monk/sops/SOP - Reuniones L+V.md` | L5-context-file | 3 | L10: # SOP — Reuniones Monk L+V |
| `Life OS/02. Areas/business_revolutia/proyectos/Auditoría de Procesos/empleados/Ernesto Bueno - Mediabuyer.md` | L5-context-file | 3 | L2: tags: [revolutia, auditoría, empleado] |
| `Life OS/02. Areas/business_revolutia/proyectos/Auditoría de Procesos/empleados/Ezequiel Martín - Social Media.md` | L5-context-file | 3 | L2: tags: [revolutia, auditoría, empleado] |
| `Life OS/02. Areas/business_revolutia/proyectos/Auditoría de Procesos/empleados/Pablo Cortés - Content & Audiovisual.md` | L5-context-file | 3 | L2: tags: [revolutia, auditoría, empleado] |
| `Life OS/02. Areas/business_revolutia/proyectos/Validar SAAS Revolutia/Workshop Materials/Workshops/Workshop-1-Prospecting-Discovery.md` | L5-context-file | 3 | L209: *"Hola [Nombre], soy [Tu Nombre] de Revolutia. Te llamé un par de veces. E |
| `Life OS/02. Areas/business_revolutia/reportes/2026-03-17 - Comparativa Lanzamientos ENE-FEB-MAR 2026.md` | L5-context-file | 3 | L2: ## Revolutia IA Pro — Análisis y Proyección |
| `Life OS/02. Areas/personal/diario/01. Daily/02-02-2026.md` | L5-journal | 3 | L24: **Current state:** Último día ski Formigal. Evento 3 Revolutia ayer fue un  |
| `Life OS/02. Areas/personal/frameworks/Personal Profile.md` | L5-framework-filled | 3 | L113: **Formador y Director de Producto \| Revolutia \| Actual** |
| `Life OS/03. Sistema/Squad Board.md` | other | 3 | L13: \| 🔴 Blocked \| Re-auth gog (3 cuentas Google) \| 15-mar \| Requiere Jorge  |
| `.claude/Life OS/02. Areas/business_360/clientes/leads (pipeline)/Oche Barber/Oche Barber - Propuesta IA para Yeazy.md` | L5-context-file | 2 | L5: **Preparado por:** 360º Consulting |
| `.claude/agents/many.md` | L3-agent | 2 | L24: - No das coaching personal (eso es Jorge) |
| `.claude/commands/audit.md` | L2-command | 2 | L2: description: "Procesar auditoría de procesos empresariales (360º Conducting  |
| `.claude/commands/process-inbox.md` | L2-command | 2 | L92: - Look for: "revolutia", "academy", "student", "workshop" → `area/business- |
| `.claude/commands/reflect.md` | L2-command | 2 | L10: 2. Leer habits de los últimos 7 días en Notion (DB: `a7b99031-cc18-4a26-bc9 |
| `.claude/commands/update-lead.md` | L2-command | 2 | L2: description: Actualizar un lead existente en el CRM de 360º post-llamada o i |
| `.claude/scripts/create_hermes_crons_from_config.py` | L1-script | 2 | L10: ap.add_argument('config', nargs='?', default='/Users/jorgeguamis/Desktop/.c |
| `.claude/scripts/git_backup_vault.sh` | L1-script | 2 | L2: cd "/Users/jorgeguamis/Desktop/Life OS" |
| `.claude/skills/csv-to-notion-crm/SKILL.md` | L2-skill | 2 | L3: description: Migrar listados CSV/Excel de leads al CRM Notion 360º con mapeo |
| `.claude/skills/find-broken-links/SKILL.md` | L2-skill | 2 | L138: - [File.md:42] `[[02. Areas/business_360/360 Consulting.md]]` |
| `Life OS/.claude/Life OS/02. Areas/business_360/clientes/leads (pipeline)/Oche Barber/Oche Barber - Propuesta IA para Yeazy.md` | L5-context-file | 2 | L5: **Preparado por:** 360º Consulting |
| `Life OS/.claude/agents/many.md` | L3-agent | 2 | L24: - No das coaching personal (eso es Jorge) |
| `Life OS/.claude/commands/audit.md` | L2-command | 2 | L2: description: "Procesar auditoría de procesos empresariales (360º Conducting  |
| `Life OS/.claude/commands/process-inbox.md` | L2-command | 2 | L92: - Look for: "revolutia", "academy", "student", "workshop" → `area/business- |
| `Life OS/.claude/commands/reflect.md` | L2-command | 2 | L10: 2. Leer habits de los últimos 7 días en Notion (DB: `a7b99031-cc18-4a26-bc9 |
| `Life OS/.claude/commands/update-lead.md` | L2-command | 2 | L2: description: Actualizar un lead existente en el CRM de 360º post-llamada o i |
| `Life OS/.claude/scripts/create_hermes_crons_from_config.py` | L1-script | 2 | L10: ap.add_argument('config', nargs='?', default='/Users/jorgeguamis/Desktop/.c |
| `Life OS/.claude/scripts/git_backup_vault.sh` | L1-script | 2 | L2: cd "/Users/jorgeguamis/Desktop/Life OS" |
| `Life OS/.claude/skills/csv-to-notion-crm/SKILL.md` | L2-skill | 2 | L3: description: Migrar listados CSV/Excel de leads al CRM Notion 360º con mapeo |
| `Life OS/.claude/skills/find-broken-links/SKILL.md` | L2-skill | 2 | L138: - [File.md:42] `[[02. Areas/business_360/360 Consulting.md]]` |
| `Life OS/00. Inbox/selenia/Morning Handoff - 2026-05-03.md` | other | 2 | L39: ## 3. Qué requiere aprobación de Jorge |
| `Life OS/00. Inbox/selenia/Overnight Cycle - 2026-05-03-1055.md` | other | 2 | L14: 1. **Ruta canónica de `.claude` como symlink:** Resuelto. `log_event.py` re |
| `Life OS/00. Inbox/selenia/Overnight Cycle - 2026-05-03-1559.md` | other | 2 | L26: - **Consolidación de approvals:** 3 approvals pendientes acumulados; recome |
| `Life OS/00. Inbox/selenia/Overnight Cycle - 2026-05-03-1631.md` | other | 2 | L29: 2. **Activar delivery Telegram piloto** (L3) — permitir a Selenia enviar re |
| `Life OS/00. Inbox/selenia/Overnight Cycle - 2026-05-06-1455.md` | other | 2 | L15: - Rutas Helios: implementación Fireflies → claude_code, follow-up INCOTEC → |
| `Life OS/01. Atomic Notes/01. List Building- Flujo de Trabajo Content Architect.md` | other | 2 | L7: - area/business-revolutia |
| `Life OS/01. Atomic Notes/02. Construcción de relaciones - Flujo de Trabajo Content Architect.md` | other | 2 | L8: - area/business-revolutia |
| `Life OS/01. Atomic Notes/03. Follow Ups - Flujo de Trabajo Content Architect.md` | other | 2 | L7: - area/business-revolutia |
| `Life OS/01. Atomic Notes/Hábitos Clave para un buen Prompting.md` | other | 2 | L86: **📘 Plantilla Revolutia – Bitácora de Iteración de Prompts** |
| `Life OS/01. Atomic Notes/Instagram Growth Schedule.md` | other | 2 | L69: ## Aplicación para Jorge |
| `Life OS/02. Areas/aprendizaje/libros/notas/100M Leads.md` | L5-context-file | 2 | L148: - ❌ "Hola, soy Jorge" |
| `Life OS/02. Areas/aprendizaje/youtube/Podcast Worldcast x Jon Hernandez.md` | L5-context-file | 2 | L233: **Consultoría (360º):** |
| `Life OS/02. Areas/business_360/clientes/activos/CPD Electricidad/01. Discovery/David Fernández - Electricista - Discovery Call Prep.md` | L5-context-file | 2 | L476: Jorge |
| `Life OS/02. Areas/business_360/clientes/activos/Cuchillas Castillo/04. Diagnóstico/Auditoría de Procesos/empleados/Pedro Guerrero Cerezo.md` | L5-context-file | 2 | L131: Consultas técnicas de afilado muy específicas: qué muela usar para un tipo |
| `Life OS/02. Areas/business_360/clientes/activos/Cuchillas Castillo/04. Diagnóstico/Auditoría de Procesos/seguimiento/Preguntas Pendientes.md` | L5-context-file | 2 | L1: # Seguimiento Entrevistas — Cuchillas Castillo |
| `Life OS/02. Areas/business_360/clientes/activos/LabArmonia/01. Discovery/LabArmonia - Alfonso Higón - Sales Call Script.md` | L5-context-file | 2 | L7: company: LabArmonia |
| `Life OS/02. Areas/business_360/clientes/activos/LabArmonia/03. Onboarding/Contrato LabArmonia 360 Consulting.md` | L5-context-file | 2 | L306: Nombre: Jorge Guamis |
| `Life OS/02. Areas/business_360/clientes/activos/LabArmonia/04. Diagnóstico/Auditoría de Procesos/empleados/Aldo Galvani.md` | L5-context-file | 2 | L54: - Distribuidores internacionales: él es su único punto de contacto con LabA |
| `Life OS/02. Areas/business_360/clientes/activos/LabArmonia/04. Diagnóstico/Auditoría de Procesos/empleados/Elisa Munoz.md` | L5-context-file | 2 | L185: **Entrevista:** Son **127 referencias** en el catálogo. Elisa confirmó que |
| `Life OS/02. Areas/business_360/clientes/activos/LabArmonia/04. Diagnóstico/Auditoría de Procesos/empleados/Maria Gomez.md` | L5-context-file | 2 | L13: **Entrevista:** 19-03-2026 \| 58 min \| Jorge Guamis |
| `Life OS/02. Areas/business_360/clientes/archivo/Grupo Marjal/Grupo Marjal - Rosalía Sanz - Discovery Call Prep.md` | L5-context-file | 2 | L515: **2. Actualizar CRM (Notion 360º)** |
| `Life OS/02. Areas/business_360/clientes/archivo/Rascanya Consulting/Rascanya Consulting — Follow-up Sales Call Script.md` | L5-context-file | 2 | L29: 2. **Posicionar 360º:** Lo que Inmatic NO resuelve es donde aportamos valor |
| `Life OS/02. Areas/business_360/clientes/archivo/SINBLAT/SINBLAT - Sales Call Script.md` | L5-context-file | 2 | L687: **Action items para Jorge:** |
| `Life OS/02. Areas/business_360/clientes/archivo/Spain Is Excellence/Contrato Spain Is Excellence 360 Consulting.md` | L5-context-file | 2 | L294: Nombre: Jorge Guamis |
| `Life OS/02. Areas/business_360/clientes/archivo/Tictacarea/Tictacarea - Juan Angel - Sales Call Script.md` | L5-context-file | 2 | L22: **Referido por:** Alex Gimeno |
| `Life OS/02. Areas/business_360/clientes/leads (pipeline)/Quality Energy Consulting/Quality Energy Consulting — Closing Call Script.md` | L5-context-file | 2 | L293: - **Marcos (referido) es socio de Ángel en AbarcaIA.** También conectado c |
| `Life OS/02. Areas/business_360/cold-outreach/Análisis Listados.md` | L5-context-file | 2 | L13: Análisis de los dos Excels de leads brutos en `02. Business/360º Consulting |
| `Life OS/02. Areas/business_revolutia/cursos/Modulo Prompting - Revolutia.md` | L5-context-file | 2 | L1: #Revolutia |
| `Life OS/02. Areas/business_revolutia/formacion/capacitacion-claude-abril-2026/_research-verificado-ecosistema-claude.md` | L5-context-file | 2 | L5: - business/revolutia |
| `Life OS/02. Areas/business_revolutia/modulos/Módulo LLMs - Elige tu Pokémon IA.md` | L5-context-file | 2 | L5: - business/revolutia |
| `Life OS/02. Areas/business_revolutia/proyectos/Auditoría de Procesos/Template Auditoría de Procesos.md` | L5-context-file | 2 | L3: - revolutia |
| `Life OS/02. Areas/business_revolutia/proyectos/Auditoría de Procesos/iniciativas/Doc Maestro Lanzamiento/02 - Blackbook Template.md` | L5-context-file | 2 | L4: - business/revolutia |
| `Life OS/02. Areas/business_revolutia/proyectos/Validar SAAS Revolutia/Boceto Kit de Ventas - Validar SAAS Revolutia.md` | L5-context-file | 2 | L98: - Soporte: Cuándo y cómo solicitar ayuda a Revolutia |
| `Life OS/02. Areas/business_revolutia/proyectos/webinar-abril-2026/04-discurso-ia-agentes-chatbots-asistentes.md` | L5-context-file | 2 | L5: - business/revolutia |
| `Life OS/02. Areas/business_revolutia/proyectos/webinar-abril/Herramientas clave Revolutia - Material Webinar.md` | L5-context-file | 2 | L4: - business/revolutia |
| `Life OS/02. Areas/business_revolutia/proyectos/webinar-abril/Problemas frecuentes en empresas - Material Webinar.md` | L5-context-file | 2 | L4: - business/revolutia |
| `Life OS/02. Areas/business_revolutia/proyectos/webinar-abril/Recomendaciones LLM - Material Webinar.md` | L5-context-file | 2 | L4: - business/revolutia |
| `Life OS/02. Areas/business_revolutia/reportes/2026-02-27 - Reporte Lanzamientos ENE vs FEB 2026.md` | L5-context-file | 2 | L2: ## Enero 2026 vs Febrero 2026 — Revolutia IA Pro |
| `Life OS/02. Areas/personal/_README.md` | L5-context-file | 2 | L337: - **Business-360 & Business-Revolutia:** Decisiones empresariales se aline |
| `Life OS/02. Areas/personal/diario/02. Weekly/2026-W04.md` | L5-journal | 2 | L80: ### 360º Consulting |
| `Life OS/02. Areas/personal/diario/02. Weekly/2026-W05.md` | L5-journal | 2 | L80: ### 360º Consulting |
| `Life OS/02. Areas/salud/_README.md` | L5-context-file | 2 | L147: - **Business-360 & Business-Revolutia:** Salud mental afecta calidad de tr |
| `Life OS/03. Sistema/Cadencia Operativa.md` | other | 2 | L127: - **Cada hora:** Monitorea formularios de auditoría Revolutia en Notion —  |
| `Life OS/03. Sistema/Mission Control - AI Agent Squad.md` | other | 2 | L42: - [x] 6 agentes configurados (main, 360-ventas, coach, finanzas, revolutia, |
| `Life OS/03. Sistema/media/excalidraw/Revolutia Negotiation.md` | other | 2 | L19: Ingresos "estables" -> Pero bajos. He ganado más en un mes con mi negocio q |
| `Life OS/03. Sistema/templates/Hub Index.md` | L1-template | 2 | L106: - Para Business-Revolutia: `business/revolutia` |
| `.claude/Life OS/02. Areas/business_360/clientes/leads (pipeline)/Oche Barber/Oche Barber - Discovery Call.md` | L5-context-file | 1 | L164: ## 8. INSIGHTS PARA JORGE |
| `.claude/Life OS/02. Areas/business_360/clientes/leads (pipeline)/Oche Barber/Oche Barber - Perfil y Contexto.md` | L5-context-file | 1 | L22: ## 2. HISTORIAL CON 360º |
| `.claude/commands/circle.md` | L2-command | 1 | L2: description: "Comunidad Circle de Revolutia. Digest diario o responder a pos |
| `.claude/commands/knowledge-digest.md` | L2-command | 1 | L13: - **Insight del día** — Si no hay input específico, seleccionar concepto re |
| `.claude/commands/process-meeting.md` | L2-command | 1 | L23: - **Interna** → extraer tareas, identificar responsable de cada una, mostra |
| `.claude/execution/log_event.schema.json` | L1-script | 1 | L63: "description": "Whether Jorge confirmed the action, or confirmation note." |
| `.claude/execution/notion_create_expense.py` | L1-script | 1 | L20: EXPENSES_DB = "2d21320d-44b1-4a17-8311-fc92269b018e" |
| `.claude/execution/telegram_signal.schema.json` | L1-script | 1 | L14: "enum": ["esbirrillo", "stark", "revo", "penny", "many", "dots", "jorge", " |
| `.claude/skills/scrape-skool-course/SKILL.md` | L2-skill | 1 | L7: - Jorge purchases a new course on Skool |
| `Life OS/.claude/Life OS/02. Areas/business_360/clientes/leads (pipeline)/Oche Barber/Oche Barber - Discovery Call.md` | L5-context-file | 1 | L164: ## 8. INSIGHTS PARA JORGE |
| `Life OS/.claude/Life OS/02. Areas/business_360/clientes/leads (pipeline)/Oche Barber/Oche Barber - Perfil y Contexto.md` | L5-context-file | 1 | L22: ## 2. HISTORIAL CON 360º |
| `Life OS/.claude/commands/circle.md` | L2-command | 1 | L2: description: "Comunidad Circle de Revolutia. Digest diario o responder a pos |
| `Life OS/.claude/commands/knowledge-digest.md` | L2-command | 1 | L13: - **Insight del día** — Si no hay input específico, seleccionar concepto re |
| `Life OS/.claude/commands/process-meeting.md` | L2-command | 1 | L23: - **Interna** → extraer tareas, identificar responsable de cada una, mostra |
| `Life OS/.claude/execution/log_event.schema.json` | L1-script | 1 | L63: "description": "Whether Jorge confirmed the action, or confirmation note." |
| `Life OS/.claude/execution/notion_create_expense.py` | L1-script | 1 | L20: EXPENSES_DB = "2d21320d-44b1-4a17-8311-fc92269b018e" |
| `Life OS/.claude/execution/telegram_signal.schema.json` | L1-script | 1 | L14: "enum": ["esbirrillo", "stark", "revo", "penny", "many", "dots", "jorge", " |
| `Life OS/.claude/skills/scrape-skool-course/SKILL.md` | L2-skill | 1 | L7: - Jorge purchases a new course on Skool |
| `Life OS/00. Inbox/Ofrecer la lanzadera de Revolutia como un upsell y si consiguen su objetivo se les devuelve el dinero. - 100M money models .md` | other | 1 | L1: Ofrecer la lanzadera de Revolutia como un upsell y si consiguen su objetivo  |
| `Life OS/00. Inbox/selenia/Healthcheck - 2026-05-03.md` | other | 1 | L22: ### PASS — route:prepara follow-up para INCOTEC |
| `Life OS/00. Inbox/selenia/Healthcheck - 2026-05-06.md` | other | 1 | L22: ### PASS — route:prepara follow-up para INCOTEC |
| `Life OS/00. Inbox/selenia/Healthcheck - 2026-05-07.md` | other | 1 | L22: ### PASS — route:prepara follow-up para INCOTEC |
| `Life OS/00. Inbox/selenia/Overnight Cycle - 2026-05-03-1315.md` | other | 1 | L19: - **Normalizar esquema Telegram:** Ya documentado como approval item `schem |
| `Life OS/00. Inbox/selenia/Overnight Cycle - 2026-05-06-1230.md` | other | 1 | L10: 2. Routing de tareas de ejemplo: `implementa script para Fireflies` → claud |
| `Life OS/00. Inbox/selenia/Selenia Report - 2026-05-06.md` | other | 1 | L36: - selenia → Jorge should review 2 pending approvals from 2026-05-03: activa |
| `Life OS/01. Atomic Notes/All Meetings And Calls Provide Opportunities To Make More Offers..md` | other | 1 | L25: “Pero Jorge, vender no es ayudar” |
| `Life OS/01. Atomic Notes/Bitácora de Iteración de Prompts – Revolutia.md` | other | 1 | L1: #Revolutia |
| `Life OS/01. Atomic Notes/Chain-of-Thought Prompting.md` | other | 1 | L31: - [[Modulo Prompting - Revolutia]] |
| `Life OS/01. Atomic Notes/Context Engineering.md` | other | 1 | L56: - **Context files** (`Personal.md`, `360 Consulting.md`) actuan como Projec |
| `Life OS/01. Atomic Notes/Descomposición de tareas en el prompting.md` | other | 1 | L99: - [[Modulo Prompting - Revolutia]] |
| `Life OS/01. Atomic Notes/Detección de Errores en Prompts.md` | other | 1 | L117: - [[Modulo Prompting - Revolutia]] |
| `Life OS/01. Atomic Notes/Elementos de un prompt efectivo.md` | other | 1 | L57: - [[Modulo Prompting - Revolutia]] |
| `Life OS/01. Atomic Notes/Evaluación de Resultados de un Prompt.md` | other | 1 | L99: - [[Modulo Prompting - Revolutia]] |
| `Life OS/01. Atomic Notes/Few-Shot Prompting.md` | other | 1 | L34: - [[Modulo Prompting - Revolutia]] |
| `Life OS/01. Atomic Notes/GSD Framework (Get Stuff Done).md` | other | 1 | L73: > Para proyectos grandes de 360 Consulting, implementar GSD formalmente cre |
| `Life OS/01. Atomic Notes/Instructional Prompting.md` | other | 1 | L26: - [[Modulo Prompting - Revolutia]] |
| `Life OS/01. Atomic Notes/Malas prácticas en el prompting.md` | other | 1 | L126: - [[Modulo Prompting - Revolutia]] |
| `Life OS/01. Atomic Notes/One-Shot Prompting.md` | other | 1 | L24: - [[Modulo Prompting - Revolutia]] |
| `Life OS/01. Atomic Notes/Patrones de diseño de prompts.md` | other | 1 | L125: - [[Modulo Prompting - Revolutia]] |
| `Life OS/01. Atomic Notes/Principios Clave del Prompting.md` | other | 1 | L96: - [[Modulo Prompting - Revolutia]] |
| `Life OS/01. Atomic Notes/Role Prompting.md` | other | 1 | L23: - [[Modulo Prompting - Revolutia]] |
| `Life OS/01. Atomic Notes/Señales de que un prompt simple no es suficiente.md` | other | 1 | L92: - [[Modulo Prompting - Revolutia]] |
| `Life OS/01. Atomic Notes/Sunday Reflection Fast.md` | other | 1 | L48: ## Aplicación para Jorge |
| `Life OS/01. Atomic Notes/Técnicas de Optimización de Prompts.md` | other | 1 | L126: - [[Modulo Prompting - Revolutia]] |
| `Life OS/01. Atomic Notes/Tipos de Prompting.md` | other | 1 | L15: - [[Modulo Prompting - Revolutia]] |
| `Life OS/01. Atomic Notes/Zero-Shot Prompting.md` | other | 1 | L29: - [[Modulo Prompting - Revolutia]] |
| `Life OS/02. Areas/aprendizaje/cursos/notas/Consulting.com Accelerator.md` | L5-context-file | 1 | L332: En realidad lo más importante son las necesidades y deseos de los mercados |
| `Life OS/02. Areas/aprendizaje/youtube/03-03-2026 Claude Code Mastery.md` | L5-context-file | 1 | L83: - [[Life OS]] - El propio sistema de Jorge implementa muchos de estos patro |
| `Life OS/02. Areas/business_360/clientes/activos/Burrito Blanco/01. Proyecto Fichas (Cerrado)/fix-longitudes/INSTRUCCIONES.md` | L5-context-file | 1 | L62: > "Obtiene las directrices SEO oficiales para fichas de producto de Burrito |
| `Life OS/02. Areas/business_360/clientes/activos/Cuchillas Castillo/04. Diagnóstico/Auditoría de Procesos/Template Auditoría de Procesos.md` | L5-context-file | 1 | L9: # Framework Auditoría de Procesos — Cuchillas Castillo |
| `Life OS/02. Areas/business_360/clientes/activos/Cuchillas Castillo/04. Diagnóstico/Auditoría de Procesos/empleados/Anderson Vinicius Dos Santos Lopis.md` | L5-context-file | 1 | L154: **Accion pendiente Anderson:** Grabar video paso a paso del proceso de cre |
| `Life OS/02. Areas/business_360/clientes/activos/Cuchillas Castillo/04. Diagnóstico/Auditoría de Procesos/empleados/Eleazar Cobos.md` | L5-context-file | 1 | L144: - [ ] ¿Qué resultado esperas del proyecto con 360º? ¿Qué cambio concreto t |
| `Life OS/02. Areas/business_360/clientes/activos/Cuchillas Castillo/04. Diagnóstico/Auditoría de Procesos/empleados/Juan Francisco Carrion.md` | L5-context-file | 1 | L70: Combinacion de trabajo planificado (cierres trimestrales, impuestos) y urge |
| `Life OS/02. Areas/business_360/clientes/activos/Cuchillas Castillo/04. Diagnóstico/Auditoría de Procesos/empleados/Juan Vicente Lorente Carbonell.md` | L5-context-file | 1 | L73: Las ofertas técnicas de maquinaria se las pasa directamente a Toni, que es  |
| `Life OS/02. Areas/business_360/clientes/activos/Cuchillas Castillo/04. Diagnóstico/Auditoría de Procesos/empleados/Vanesa Tadeo.md` | L5-context-file | 1 | L146: > "Propone reestructurar sus tareas para evitar fragmentación y mejorar fo |
| `Life OS/02. Areas/business_360/clientes/archivo/Alannia/06. Despliegue/Weekly Log 2026-02-11.md` | L5-context-file | 1 | L14: ## Action Items Jorge |
| `Life OS/02. Areas/business_360/clientes/archivo/Alannia/Script Llamada Cierre Final - Alannia.md` | L5-context-file | 1 | L196: No es parte de lo que hacemos en 360º. Pero os puedo recomendar perfiles d |
| `Life OS/02. Areas/business_360/clientes/archivo/Rascanya Consulting/Rascanya Consulting — Research Técnico.md` | L5-context-file | 1 | L98: 3. **Valor de 360º:** No vendemos Inmatic (eso lo pueden comprar solos). Ve |
| `Life OS/02. Areas/business_360/clientes/leads (pipeline)/Querkus/Querkus - José Luis o Paola.md` | L5-context-file | 1 | L33: ## Análisis para 360º |
| `Life OS/02. Areas/business_360/cold-outreach/Mapeo CRM Notion.md` | L5-context-file | 1 | L14: DB ID: `2338eff7-5947-81b1-b11c-000b216e501a` |
| `Life OS/02. Areas/business_360/cold-outreach/Plan Enriquecimiento.md` | L5-context-file | 1 | L121: ## Decisiones pendientes con Jorge |
| `Life OS/02. Areas/business_revolutia/proyectos/Auditoría de Procesos/empleados/Hector Soria - Closer.md` | L5-context-file | 1 | L2: tags: [revolutia, auditoría, empleado] |
| `Life OS/02. Areas/business_revolutia/proyectos/Auditoría de Procesos/empleados/Vero Barreiro - CMO.md` | L5-context-file | 1 | L2: tags: [revolutia, auditoría, empleado] |
| `Life OS/02. Areas/business_revolutia/proyectos/Auditoría de Procesos/seguimiento/Preguntas Pendientes.md` | L5-context-file | 1 | L2: tags: [revolutia, auditoría, seguimiento] |
| `Life OS/02. Areas/business_revolutia/proyectos/Revisión de Avatares/Avatares Revolutia.md` | L5-context-file | 1 | L3: - Revolutia |
| `Life OS/02. Areas/business_revolutia/proyectos/Validar SAAS Revolutia/Workshop Materials/Reference/One-Pager-Producto.md` | L5-context-file | 1 | L297: **Powered by Revolutia Academy** |
| `Life OS/02. Areas/investigacion/Research.md` | L5-context-file | 1 | L88: - Research skills transferable to 360º client projects |
| `Life OS/02. Areas/investigacion/proyectos/VISUAL AI SOFTWARE/Estructura de Research Completo - Visual AI.md` | L5-context-file | 1 | L24: - [x] **Willingness to pay**: ✅ $20-50/mes uso personal, $100+/mes uso con  |
| `Life OS/02. Areas/personal/diario/01. Daily/01-03-2026.md` | L5-journal | 1 | L21: - Falleció el abuelo — abuela tranquila, Jorge tranquilo |
| `Life OS/02. Areas/personal/diario/01. Daily/02-08-2025.md` | L5-journal | 1 | L12: - quiero ser mi mejor versión, trabajar en mi marca personal y en 360º, ya  |
| `Life OS/02. Areas/personal/diario/01. Daily/03-11-2025.md` | L5-journal | 1 | L15: - Estoy contento de haber acabado la clase de revolutia pese a que no me en |
| `Life OS/02. Areas/personal/diario/01. Daily/04-11-2025.md` | L5-journal | 1 | L26: - Me he puesto a leer mis reflexiones y el feedback de mis clases de revolu |
| `Life OS/02. Areas/personal/diario/01. Daily/07-11-2025.md` | L5-journal | 1 | L17: - He acabado los videos de la nueva metodología de #Revolutia |
| `Life OS/02. Areas/personal/diario/02. Weekly/Weekly Reflection 11_11_25-16_11_25.md` | L5-journal | 1 | L23: > Mi negocio sigue desarrollandose, revolutia parece que se estabiliza y em |

