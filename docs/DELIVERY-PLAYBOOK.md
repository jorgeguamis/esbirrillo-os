# Delivery Playbook — Esbirrillo OS

> Operativa de Jorge instalando el sistema a un cliente. NO es la documentación técnica para el cliente final (esa está en `INSTALL.md`). Esto es **el manual del consultor**.

**Audiencia:** Jorge (y futuros consultores que entreguen el sistema).
**Cuándo leerlo:** antes del kick-off con cualquier cliente. Re-leer al inicio de cada semana del delivery.

---

## Tabla de contenidos

1. [Inventario de herramientas (cliente + consultor)](#1-inventario-de-herramientas)
2. [Pre-flight checklist (antes del kick-off)](#2-pre-flight-checklist)
3. [Roadmap delivery (8 semanas, día por día)](#3-roadmap-delivery)
4. [Session scripts (qué hacer en cada reunión)](#4-session-scripts)
5. [Communication templates](#5-communication-templates)
6. [Troubleshooting](#6-troubleshooting)
7. [Captura para caso de éxito](#7-captura-para-caso-de-éxito)
8. [Pricing y term sheet](#8-pricing-y-term-sheet)

---

## 1. Inventario de herramientas

### Tier 0 — Imprescindibles (sin esto el sistema no arranca)

| Herramienta | Para qué | Quién lo paga | Coste mensual | Tiempo setup | URL |
|---|---|---|---|---|---|
| **Claude API key** (Anthropic) | Modelo principal de los agentes | Cliente | ~30-150€ según uso | 5 min | console.anthropic.com |
| **Claude Code CLI** | IDE/terminal del sistema | Cliente | Gratis (consume API key) | 10 min | docs.claude.com/claude-code |
| **Telegram bot personal** | Capa conversacional | Cliente | Gratis | 15 min | @BotFather en Telegram |
| **Notion + Internal Integration** | Capa operativa (CRM, tasks, finance) | Cliente | Plan pagado recomendado (~10€/mes) | 20 min | notion.so/profile/integrations |
| **Mac propia del cliente** | Donde corre el sistema | Cliente | (ya la tiene) | — | — |

### Tier 1 — Muy recomendados (sin esto el sistema queda parcial)

| Herramienta | Para qué | Coste | Setup | Notas |
|---|---|---|---|---|
| **Hermes-agent** (Nous Research, OSS) | Runtime siempre-on, scheduler crons | Gratis | 30 min | github.com/NousResearch/hermes-agent |
| **Fireflies** | Transcripciones automáticas reuniones | 10-19$/mes | 10 min | fireflies.ai |
| **Google Workspace** (Cal+Gmail+Drive) | Calendar(s) + email + storage | 6-12€/mes/cuenta | 5 min | el cliente probablemente ya lo tiene |
| **GitHub privado** | Versionar config personal del cliente | Gratis (cuenta personal) | 5 min | github.com |

### Tier 2 — Opcionales (depende del cliente)

| Herramienta | Para qué | Coste | Cuando activar |
|---|---|---|---|
| **Obsidian** | Vault de notas markdown | Gratis | Si quiere knowledge management profundo |
| **NotebookLM** | Knowledge bases con sources | Gratis | Si maneja mucho material de research |
| **Discord/Slack/WhatsApp Business** | Capa conversacional alternativa | Variable | Si Telegram no es su canal natural |
| **N8N** | Automatizaciones extra | 0-20€/mes selfhost / 24€ cloud | Si quiere flows complejos |
| **Mac mini dedicado** | Hosting siempre-on independiente | ~700€ una vez | Cliente que viaja o quiere aislar |

### Herramientas QUE TÚ (Jorge) necesitas tener listas

| Item | Para qué | Ya lo tienes? |
|---|---|---|
| Repo `esbirrillo-os` clonado en tu Mac | Para mostrarle al cliente y debuggear | ✅ |
| Acceso al repo del cliente (read-only por defecto) | Para soportar en remoto si autoriza | establecer en sem 4 |
| Tu propio Hermes-agent funcionando | Para demostrar visualmente el output esperado | ✅ |
| Cuenta de prueba Notion separada | Para hacer demos sin tocar tu workspace | crear |
| Cuenta de prueba Telegram | Para validar bots de cliente sin contaminar | crear |
| Plantillas de comunicación (sección 5 de este doc) | Email kick-off, recap, handoff | ver abajo |

### Estimación de coste mensual TOTAL para el cliente

| Tier | Coste mensual |
|---|---|
| **Mínimo** (Tier 0 solo, uso ligero) | ~40-60€ |
| **Recomendado** (Tier 0 + Fireflies + Google Workspace) | ~70-110€ |
| **Pro** (todo Tier 1 + Mac mini amortizado) | ~120-200€ |

**Para Juan:** target ~80€/mes (Tier 0 + Fireflies, asume Google Workspace ya pagado por Revolutia).

---

## 2. Pre-flight checklist

> Confirmar TODO antes de la primera reunión con el cliente. Si falla algún ítem aquí, mover el kick-off una semana.

### Checklist contigo (Jorge) — semana 0

- [ ] El kit `esbirrillo-os` corre en tu Mac (clone fresco, run `bin/install.sh`).
- [ ] El repo está en GitHub privado tuyo (para fork del cliente).
- [ ] Tu Hermes-agent local responde en Telegram.
- [ ] Tienes el playbook actualizado (este doc).
- [ ] Has reservado bloques de tiempo en tu calendar para las 8 semanas.

### Checklist con el cliente — semana 4 día 1 (kick-off)

Mandar al cliente 1 semana antes del kick-off un email con esta lista:

- [ ] **Hardware:** ¿usa Mac? Versión de macOS.
- [ ] **Anthropic account:** crear cuenta + API key. ~30-50€ de crédito inicial.
- [ ] **Notion account:** plan personal o team. Crear "Internal Integration" (instrucciones detalladas en email kick-off).
- [ ] **Telegram:** instalar app móvil + desktop si no la tiene.
- [ ] **GitHub:** cuenta personal (no de la empresa).
- [ ] **Time blocking:** reservar 8 sesiones de 60-90 min en su calendar (sem 4-7).
- [ ] **Email contacto principal:** decir qué email usaremos para coordinación (no el de empresa si quiere separar).
- [ ] **Term sheet firmado:** acuerdo de uso + intro al tío + revenue share (sección 8).

### Checklist técnico antes de la primera sesión

- [ ] Cliente tiene homebrew instalado (`brew --version`).
- [ ] Cliente tiene Python 3.12+ (`python3 --version`).
- [ ] Cliente tiene git (`git --version`).
- [ ] Cliente tiene Claude Code CLI instalado y funciona en su terminal.
- [ ] Cliente puede crear `~/.env` y entiende que NO se versiona.
- [ ] Cliente tiene un editor (VSCode recomendado, también Cursor o terminal-only).

Si cualquiera falla → 30 min de pre-setup técnico antes de empezar discovery. No empieces discovery con bloqueo técnico — mata el momentum.

---

## 3. Roadmap delivery

8 semanas, día por día. Asume cliente trabaja 5 días/semana, sesiones de 60-90 min cuando aplique.

### Semana 0 — Tu prep (sin cliente)

**Tu trabajo:** verificar que el kit funciona limpio, preparar materials para el cliente.

| Día | Acción |
|---|---|
| L | Run `bin/install.sh` en una segunda Mac/VM o directorio aislado para validar |
| M | Test fictional `/setup-wizard` con perfil sintético — verificar outputs |
| X | Pulir bugs detectados |
| J | Preparar email kick-off + term sheet |
| V | Send kick-off email al cliente con checklist pre-flight |

### Semana 1-3 — Tu trabajo solo (cliente no entra aún)

Esto SOLO aplica si vas por path "Starter Kit reutilizable + caso 0". Si vas directo a Juan: salta a semana 4.

| Sem | Foco |
|---|---|
| 1 | Construir kit (ya hecho — Sem 1 commit `12d19ce`) |
| 2 | Construir Capa 4 setup-wizard (ya hecho — Sem 2 commit) |
| 3 | Test interno con perfil sintético, iterar bugs |

### Semana 4 — Discovery con cliente

Ya el cliente entra. **3 sesiones de 60-90 min repartidas en la semana**, NO seguidas.

| Día | Sesión | Duración | Output |
|---|---|---|---|
| L | Sesión 1 — Identidad y norte | 90 min | Personal.md draft + North Star draft |
| X | Sesión 2 — Negocios y rol | 60 min | Business contexts drafts + agent specs |
| V | Sesión 3 — Stack y operativa | 45 min | Stack map + lista credenciales a configurar |

Entre sesiones: **deja al cliente hacer "homework"** (rellenar Vivid Vision, listar contactos clave). 60-90 min de tu tiempo entre sesiones revisando lo que él rellena.

**Output sem 4:** term sheet firmado, drafts de Personal.md/North Star/business contexts en su mac, lista de credenciales por configurar.

### Semana 5 — Setup técnico + onboarding agéntico

Cliente activamente operando contigo en sesiones largas.

| Día | Sesión | Duración | Output |
|---|---|---|---|
| L | Sesión 4 — Install kit en su Mac | 90 min | Kit clonado, deps instaladas, Anthropic key + Notion auth funcionando |
| M | Sesión 5 — Telegram bot + Hermes-agent | 60 min | Bot creado, grupos por agente, Hermes corriendo, healthcheck verde |
| X | Sesión 6 — `/setup-wizard` Stage 1+2 | 90 min | extract-identity completo, primeros agentes de dominio creados |
| J | Sesión 7 — `/setup-wizard` Stage 3+4 | 90 min | Context files + Notion DBs creadas |
| V | Sesión 8 — `/setup-wizard` Stage 5 | 90 min | Frameworks (Vivid Vision, Life Map, Identity, Future Self) |

Fin de semana: cliente hace homework de frameworks (relee y edita a mano).

### Semana 6 — Closing setup + training

| Día | Sesión | Duración | Output |
|---|---|---|---|
| L | Sesión 9 — `/setup-wizard` Stage 6+7 | 60 min | Working memory + healthcheck final pasa |
| M | Training 1 — Daily flow | 60 min | Cliente sabe usar `/morning`, `/reflect` |
| X | Training 2 — Reuniones | 60 min | Cliente sabe procesar Fireflies con `/process-meeting` |
| J | Training 3 — Knowledge | 45 min | Cliente sabe usar `/capture`, `/knowledge-digest` |
| V | Training 4 — Reviews | 45 min | Cliente sabe correr `/weekly-review` |

Daily check-in por Telegram (5 min/día): "¿Has usado X?" "¿Qué pasó cuando intentaste Y?".

### Semana 7 — Operación supervisada

Cliente opera autónomo, tú monitorizas y refinas.

| Día | Tu trabajo |
|---|---|
| L-V | 30 min/día revisando logs JSONL y Selenia reports del cliente |
| L-V | Daily check-in por Telegram con cliente |
| Mié | Sesión 10 — Refinement (60 min): qué necesita y aún no tiene |
| Vie | Sesión 11 — Skill nueva si pidió alguna específica (60 min) |

**Output sem 7:** N skills/agentes nuevos según necesidades reales del cliente. Estos se incorporan al `esbirrillo-os` upstream si son genéricos.

### Semana 8 — Handoff + caso de éxito + venta al tío

| Día | Acción |
|---|---|
| L | Recopilar métricas (sesión 12, 60 min con cliente): reuniones procesadas, decisiones delegadas, tiempo recuperado, momentos "wow" |
| M | Grabar vídeo demo 15 min con el cliente operando el sistema en flujos reales |
| X | Escribir doc "Antes/Después: 8 semanas con Esbirrillo OS" |
| J | One-pager comercial para enseñar al tío + leads futuros |
| V | **Meeting Jorge + cliente + tío** (90 min). Cliente demuestra el sistema. Tú cierras. |

---

## 4. Session scripts

### Sesión 1 — Identidad y norte (90 min)

**Antes:** confirma que el cliente leyó el email kick-off y completó el checklist técnico. Si no, primero arregla eso (no entres a discovery sin pre-flight).

**Durante:**

```
0-5 min   — Bienvenida. "Vamos a invertir 90 min en construir el modelo
            que el sistema tendrá de ti. La calidad de las respuestas aquí
            determina la calidad de todo lo que viene. Vamos sin prisa."

5-15 min  — Block 1 extract-identity (Identidad básica).
15-35 min — Block 2 (Roles y negocios) — bloque más largo, no acortar.
35-55 min — Block 3 (Norte y motivación) — usa templates Vivid Vision Q1.
55-75 min — Block 4 (Patrones) — bloque sensible, no rusheas.
75-85 min — Block 5+6 (Stack y equipo).
85-90 min — Cierre. "Voy a procesar esto, te mando el draft de Personal.md
            y North Star.md mañana por email. Léelos y márcame qué ajustar."
```

**Después (1-2h tu tiempo):**
- Procesar las respuestas en draft de `Personal.md` y `North Star.md`.
- Mandarle email con los drafts + 3-5 preguntas de aclaración.
- Schedule sesión 2 cuando confirme.

### Sesión 2 — Negocios y rol (60 min)

**Antes:** revisa que el cliente respondió a las preguntas de aclaración del draft de Personal.md.

**Durante:**

```
0-10 min  — Confirma drafts. Aplica correcciones in-session.
10-50 min — Block 2 + create-my-agent Step 1-3 para CADA business:
            - 10 min por business para confirmar scope/decisiones/fuentes
            - Cliente con 2-3 negocios = 30-40 min aquí
50-60 min — Cierre. "Para sesión 3 prepara: lista de 10 contactos clave,
            lista de tools concretos que usas hoy, screenshot de un día
            típico de tu calendar."
```

### Sesión 3 — Stack y operativa (45 min)

**Durante:**

```
0-15 min  — Stack walk-through: por cada tool que usa, decidir si entra
            al sistema o no.
15-30 min — Listar credenciales que va a tener que generar/reutilizar:
            Anthropic, Notion, Fireflies, Google.
30-40 min — Term sheet review + firma.
40-45 min — Schedule sesiones de sem 5 (5 sesiones, 60-90 min cada una).
            Bloquear su calendar AHORA, no más tarde.
```

### Sesión 4 — Install kit en su Mac (90 min)

**Antes:** confirma que tiene homebrew, python3, git, claude CLI, VSCode, y los API keys creados (Anthropic + Notion integration token).

**Durante (operativa screen-share):**

```
0-15 min  — Clone repo en su Mac. cd, ls. Explicar estructura.
15-30 min — Run bin/install.sh. Responder prompts: runtime path A, modelo
            Anthropic, paths.
30-45 min — Crear .env con API keys. Validar gitignore.
45-60 min — Setup .mcp.json con Notion + Filesystem + Memory Bank básicos.
60-75 min — Test: claude → /helios-healthcheck → debe ser verde excepto
            Telegram (siguiente sesión) y Hermes (sesión 5 también).
75-90 min — Si algo falla: debug en vivo o documentar fallback.
```

**Riesgos:** Notion auth puede fallar por permisos. Solución: el cliente debe compartir la página padre con la integration ANTES de la sesión.

### Sesión 5 — Telegram bot + Hermes-agent (60 min)

```
0-15 min  — Crear bot via @BotFather. Token a .env.
15-30 min — Crear grupos Telegram (uno por agente core). Añadir bot.
            Capturar chat_ids (helper script). Registrar en
            telegram-routing.md.
30-50 min — Setup Hermes-agent: clone NousResearch/hermes-agent en
            ~/.hermes/, crear venv, install deps, generar config.toml,
            generar plist launchd, launchctl load.
50-60 min — Validar: mandar "hola" al bot en DM → debe responder. Si no,
            check logs ~/.hermes/logs/gateway.log.
```

**Si Hermes-agent falla setup:** fallback a path B (Claude Code + plugin Telegram). Documentado en INSTALL.md. Velocidad similar, capacidades menores.

### Sesiones 6-9 — `/setup-wizard` stages

Cada sesión tú haces de **facilitador silencioso**: el wizard hace las preguntas, tú solo intervienes si:
- El cliente da una respuesta vaga y el wizard no profundiza lo suficiente.
- El cliente pregunta qué hacer cuando una opción no le encaja.
- Algo técnico falla (error de Notion, MCP caído).

Tu rol = consultor, no operador. El sistema hace el trabajo.

### Sesiones 10-12 — Training, refinement, handoff

Ver detalles en sección 3 (roadmap).

---

## 5. Communication templates

### Email kick-off (semana 4 día -7)

```
Asunto: Esbirrillo OS — pre-flight checklist (próximo lunes empezamos)

Hola {{NOMBRE}},

Vamos a empezar el lunes {{FECHA}} la implementación de Esbirrillo OS en
tu mac. Para que la primera sesión sea productiva, necesito que tengas
las siguientes cosas listas:

== Cuentas a crear (~30 min) ==

1. Anthropic API
   - Ve a console.anthropic.com → crea cuenta.
   - En "API Keys" → crea una key nueva. Guarda en sitio seguro.
   - Carga ~50€ de crédito inicial.

2. Notion Internal Integration
   - Ve a notion.so/profile/integrations → "+ New integration".
   - Tipo: Internal. Nombre: "Esbirrillo".
   - Capabilities: Read, Update, Insert, Delete (todas).
   - Guarda el "Internal Integration Secret".
   - DESPUÉS de la sesión 4 te enseño a compartir páginas con esta
     integration.

3. (Opcional pero recomendado) Fireflies — fireflies.ai → cuenta + API key.

== Software a instalar (~30 min) ==

```bash
# Si no los tienes:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python@3.12 git
brew install --cask visual-studio-code

# Claude Code CLI:
# https://docs.claude.com/en/docs/claude-code/quickstart
```

== Tiempo bloqueado ==

He propuesto 5 sesiones esta semana en tu calendar. Confírmame que las
ves y te van bien:
- Lunes 10-12h
- Martes 11-12h
- Miércoles 10-12h
- Jueves 10-12h
- Viernes 10-12h

== Pre-trabajo (15 min, antes del lunes) ==

Lee el doc adjunto "Vivid Vision en 30 min" y empieza a esbozar tu
visión a 3 años. No tiene que estar terminada — la trabajamos en
sesión 1.

Cualquier duda, escríbeme aquí o por Telegram.

Saludos,
Jorge
```

### Email recap post-sesión

```
Asunto: Recap sesión {{N}} — {{TEMA}}

{{NOMBRE}},

Sesión de hoy en 5 puntos:

1. {{lo que cubrimos}}
2. {{outputs concretos: archivos generados, configs, etc.}}
3. {{decisiones tomadas}}
4. {{preguntas abiertas que quedaron}}
5. {{tu homework antes de la próxima sesión}}

Próxima sesión: {{fecha}} a las {{hora}}.

Si quieres profundizar en algo en concreto antes, mándame mensaje.

Saludos,
Jorge
```

### Weekly progress update (sem 6-8)

```
Asunto: Esbirrillo OS — semana {{N}} progreso

{{NOMBRE}},

Esto va por buen camino. Resumen semana {{N}}:

== Lo que hiciste tú ==
- {{N}} `/morning` ejecutados
- {{N}} reuniones procesadas con `/process-meeting`
- {{N}} atomic notes creadas
- {{otros usos}}

== Lo que el sistema detectó ==
- {{patrones nuevos}}
- {{decisiones que el reviewer flag}}

== Próxima semana ==
- {{focus}}
- {{si algo a mejorar}}

== Métrica de adopción ==
{{X}} días de los últimos 7 con uso real. {{✅/⚠️}}

Sesión de refinement el {{día}}.
```

### Email handoff final (semana 8)

```
Asunto: Cierre Esbirrillo OS — siguiente fase

{{NOMBRE}},

Han sido 8 semanas. El sistema ya es tuyo. Resumen:

== Lo que tienes hoy ==
- {{4 + N}} agentes activos
- {{N}} skills funcionando
- Working memory con {{N}} líneas de contexto sobre ti
- {{N}} reviews semanales generados
- {{N}} reuniones procesadas

== Métricas del periodo ==
- Tiempo recuperado estimado: {{N}}h/semana
- Decisiones delegadas al sistema: {{N}}
- {{otros}}

== Tu próxima fase ==
1. Operas solo durante 30 días.
2. Reuniones de refinement opcionales mensuales (60 min).
3. Si quieres skills nuevas o cambios estructurales, retainer mensual
   {{X}}€/mes.

== El próximo paso comercial que hablamos ==
La meeting con tu tío está agendada para {{fecha}}. Te mando el
one-pager comercial el día anterior.

Gracias por confiar en el sistema desde la versión 0.1.

Jorge
```

---

## 6. Troubleshooting

### Hermes-agent no arranca

```bash
# Check launchd:
launchctl list | grep hermes

# Si no aparece:
launchctl load ~/Library/LaunchAgents/ai.hermes.gateway.plist

# Si falla:
tail -50 ~/.hermes/logs/gateway.error.log
```

Causas comunes:
- venv no activado en config — regenerar plist con paths absolutos.
- API key del modelo no en `.env`.
- Telegram bot token mal pegado (espacio extra, comilla).

### Telegram bot no responde

```
1. Verifica que el bot recibe mensajes:
   curl https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/getUpdates
2. Si no llegan: bot bloqueado por usuario o token incorrecto.
3. Si llegan pero no responde: Hermes/Claude Code no está corriendo
   o no tiene permisos auto.
4. Check logs gateway.log en busca de errores model API (rate limit,
   invalid key).
```

### Notion auth falla

```
1. La integration debe estar añadida a la página parent que el sistema
   intenta leer. En Notion: ... menu → "Add connections" → seleccionar
   "Esbirrillo".
2. Si la DB ya existía antes de crear la integration, hay que añadir
   permiso explícitamente — no se hereda.
3. Test manual:
   mcp__notion__API-get-self
```

### Cliente abandona

Si en sem 6 detectas que el cliente usa el sistema <3 días/semana:

1. **Conversación honesta**: ¿qué le frena? ¿UX, falta de tiempo, no le aporta valor?
2. **Si es UX**: identificar fricción específica, fix en 1-2 días, push update.
3. **Si es tiempo**: reducir scope. Quizá solo `/morning` y `/reflect` durante 1 mes, después añadir.
4. **Si no aporta valor**: difícil rescatar. Honest conversación: ¿quieres que sigamos? Si no, cierre amistoso, pierdes la apuesta del tío.

### Cliente quiere cosas que rompen privacidad

Si el cliente pide compartir contigo el log de su sistema, o sincronizar con tu mac, o que tú tengas acceso a su working-memory:

→ NO lo aceptes aunque insista. Documenta por escrito (email) que rechazaste por safeguard. Lo último que quieres es ser responsable de una fuga de datos del sistema.

### El tío no aparece en sem 8

Si la intro no se materializa:
1. Pregunta qué bloqueó al cliente. ¿Su tío está en mal momento? ¿Cliente tiene reservas?
2. Si es timing: reagendar para sem 10-12.
3. Si es reservas: aceptar, no forzar. El kit y el caso de estudio quedan como activos para venta a OTROS leads.

---

## 7. Captura para caso de éxito

A capturar **durante todo el proceso**, no al final:

### Datos cuantitativos (semana a semana)

Crear sheet `case-study-metrics.csv` desde sem 4:

```
date,session,duration_min,output,client_pain_point,client_aha_moment,blocker,resolution
2026-XX-XX,Discovery 1,90,Personal.md+North Star drafts,calendar overload,realized 60% meetings non-strategic,,
```

### Datos cualitativos (capture momentos)

Cada sesión, **al final**, anotar 1-2 frases del cliente que muestran:
- Aha moment ("no me había dado cuenta de X")
- Resistencia inicial → conversión ("pensaba que no iba a usar Telegram, pero...")
- Comparación pre/post ("antes tardaba 30 min en preparar morning, ahora 5")

Estas frases son ORO para vender al tío. Pídele permiso al cliente para usarlas (con/sin nombre, según prefiera).

### Vídeos demo (sem 7-8)

Capturar **3 vídeos cortos** (90 segundos cada uno) del cliente operando:

1. **Daily flow**: cliente abre Telegram, escribe "qué tengo hoy", recibe brief.
2. **Reunión procesada**: cliente termina una llamada, sube a Fireflies, runs `/process-meeting`, ve action items en su Notion.
3. **Weekly review**: cliente runs `/weekly-review` un domingo, ve patrones detectados.

Estos vídeos son la herramienta de venta más poderosa que vas a tener. Dedícales tiempo.

### Documento "Antes/Después: 8 semanas con Esbirrillo OS"

Estructura sugerida (max 2 páginas):

```
## El cliente
{{nombre + cargo + breve}}

## El antes (sem 0)
- {{X}} meetings/semana sin procesar
- {{Y}} min/día en planificación manual
- {{Z}} decisiones postergadas
- 3 frases del cliente describiendo su frustración

## La intervención (sem 4-8)
- {{N}} sesiones, {{horas}} totales
- {{lista de skills/agentes implementados}}

## El después (sem 8)
- {{X'}} reuniones procesadas automáticamente
- {{Y'}} min/día (delta vs antes)
- {{Z'}} decisiones cerradas + {{W}} delegadas al sistema
- 3 frases del cliente describiendo el cambio

## Métrica clave
{{una métrica que ROI clara — tiempo recuperado, deals movidos, etc.}}

## Quote final
{{frase del cliente describiendo el sistema en 2 frases}}
```

### One-pager comercial (sem 8 viernes)

Documento PDF dark theme (estilo proposals 360º) con:
- Logo / branding Esbirrillo OS
- 3 frases que describen qué es
- 5 capabilities con icono
- Caso de éxito (link al doc anterior)
- Pricing (sección 8)
- CTA: agendar discovery call

---

## 8. Pricing y term sheet

### Tier 0 — Caso de éxito (Juan)

```
Precio:                      0€
Compromiso del cliente:      uso 5 días/semana mín., 8 sem
Compromiso del consultor:    delivery completo (sem 4-8) + supervisión
                             sem 7-8
Contraprestación:            intro cualificada al tío en sem 8
Revenue share:               15% del primer año si el tío contrata
                             (alternativa: flat 5k€ referral fee)
Permiso uso del caso:        sí, con/sin anonimato según cliente prefiera
Cláusula de salida:          si en sem 4 cliente abandona uso (<3d/sem),
                             consultor puede pausar
```

### Tier 1 — Comercial (tío y futuros)

```
Setup fee:                   8.000-15.000€ (one-time)
                             - 8k: consultor solo founder
                             - 12k: CEO mediana empresa
                             - 15k: CEO con equipo + multi-business
Pago:                        50% al firmar, 50% en sem 5
Retainer:                    1.500-3.000€/mes (después del setup)
                             - 1.5k: 4h/mes de iteración
                             - 3k: 8h/mes + skills nuevas
Plazo:                       8 semanas setup, retainer mes 2+
Stay rate:                   90% objetivo (cliente sigue 6+ meses)
SLA:                         24h respuesta a issues, 72h a feature requests
Cancelación:                 1 mes de aviso
```

### Tier 2 — Enterprise (futuro, sin precio aún)

```
Sub-cliente: empresa con C-suite quiere instalar para multiple
ejecutivos. Setup multi-user + governance layer + branding personalizado.
Precio TBD post primer caso.
```

### Term sheet — template (Juan version)

```markdown
# Term Sheet — Esbirrillo OS, caso 0

**Entre:** Jorge Guamis ("Consultor")
**Y:**    {{NOMBRE_CLIENTE}} ("Usuario")

**Objeto:** instalación y operación supervisada de Esbirrillo OS, sistema
agéntico personal, en la máquina del Usuario, durante 8 semanas + extensión
4 semanas.

**Contraprestación económica:** 0€. Este es un acuerdo de caso de éxito,
no un servicio remunerado.

**Contraprestación del Usuario:**
1. Compromiso de uso 5 días/semana mínimo durante el periodo.
2. Disponibilidad para 12 sesiones de 60-90 min en sem 4-8.
3. En sem 8, intro cualificada (meeting de 60 min con los 3) a
   {{NOMBRE_TÍO}} para presentar el sistema.
4. Si {{NOMBRE_TÍO}} contrata el sistema dentro de 6 meses, el Usuario
   acepta un revenue share del 15% del primer año del contrato (o flat
   5.000€ referral fee, lo que el Usuario prefiera).
5. Permiso para usar el caso (anonimizado según preferencia del Usuario)
   en venta posterior a otros leads.

**Confidencialidad:** El Consultor no replicará, sincronizará, ni
exportará datos del sistema del Usuario. Acceso de soporte solo bajo
SSH/screen-share supervisado y consentido. El Usuario puede revocar
acceso en cualquier momento.

**Salida del Consultor:** Si en sem 4 el Usuario ha usado el sistema
<3 días/semana, el Consultor puede pausar la entrega. Si el Usuario
ha cumplido el compromiso de uso, el Consultor finaliza las 8 semanas
sin coste adicional.

**Vigencia:** {{fecha_inicio}} a {{fecha_inicio + 8 semanas}}.

**Firmas:**

Consultor: ___________________ Fecha: ___________
Usuario:   ___________________ Fecha: ___________
```

---

## Cierre

Este playbook se actualiza con cada cliente. Después de Juan, **vuelve aquí y añade**:

- Nuevas troubleshooting items.
- Refinements en session scripts.
- Templates de comunicación que el cliente respondió mejor.
- Errores que cometiste y cómo los evitarías.

El playbook v0 (este) está sin testear con cliente real. El playbook v1 lo será post-Juan.
