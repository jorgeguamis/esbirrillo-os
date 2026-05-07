---
description: Stage 5 of /setup-wizard. Walks the user through the personal frameworks (Vivid Vision, Life Map, Identity & Values, Future Self, Principles, Winner Worksheet, Ideal Life Costing). Templates exist in 03. Sistema/templates/. The wizard is a facilitator, not a form-filler. ~60-90 minutes total.
---

# frameworks-walkthrough — Síntesis estratégica

Stage 5. ~60–90 minutes (tipicamente split en 2 sesiones). Esto es lo más profundo del wizard. La diferencia entre un sistema "AI assistant genérico" y un "AI co-CEO que te conoce" está en la calidad de este stage.

## Goal

Construir los frameworks personales que orientan toda decisión estratégica. El sistema (especialmente `reviewer` agent y commands `/morning`, `/quarterly-review`) referenciará estos archivos.

## Frameworks generados

| Framework | File | Time | Required |
|---|---|---|---|
| North Star | `02. Areas/personal/North Star.md` | 15 min (sintetiza los demás) | ✅ |
| Vivid Vision | `02. Areas/personal/frameworks/Vivid Vision.md` | 20-30 min | ✅ |
| Life Map | `02. Areas/personal/frameworks/Life Map.md` | 15 min | ✅ |
| Identity & Values | `02. Areas/personal/frameworks/Identity and Values.md` | 15 min | ✅ |
| Future Self | `02. Areas/personal/frameworks/Future Self.md` | 15 min | recomendado |
| Principles | `02. Areas/personal/frameworks/Principles.md` | 10 min | recomendado |
| Winner Worksheet | `02. Areas/personal/frameworks/Winner Worksheet.md` | 10 min | opcional |
| Ideal Life Costing | `02. Areas/personal/frameworks/Ideal Life Costing.md` | 10 min | opcional |

## Tone

- **Facilitar, no rellenar.** Tu rol es guiar al usuario para que encuentre sus respuestas, no proponérselas.
- **Pausas si hace falta.** Algunos frameworks requieren reflexión profunda. Si el usuario dice "déjame pensar 15 min", esperar.
- **Honestidad sobre performance.** Si una respuesta suena a "lo que se supone que debo decir", reflejarlo.
- **Construir sobre Stage 1.** Las patrones, north star, businesses ya están capturados. No repetir — profundizar.

## Protocol — Vivid Vision (3 años)

> Concepto de Cameron Herold (Double Double): visualiza tu vida exactamente como será dentro de 3 años, en presente, con detalle sensorial.

### Setup

```
"Vamos a hacer un Vivid Vision. La idea es que describas tu vida dentro
de 3 años, EN PRESENTE, como si ya estuviera ocurriendo. No es un plan
ni una lista de objetivos — es una imagen vívida, sensorial.

Voy a preguntarte sobre 8 dimensiones. Cada una en 2-3 frases. Total
20-30 min. Vamos."
```

### Dimensiones

```
1. Negocio principal: ¿cómo es un día típico en tu negocio principal
   en 3 años? ¿Quién está? ¿Qué tamaño tiene? ¿Cómo se siente?

2. Otros proyectos / fuentes de ingreso: ¿qué más existe? ¿Qué te
   genera dinero pasivo? ¿Qué inversiones?

3. Equipo / partners: ¿con quién trabajas? ¿Cuánta gente? ¿Qué energía
   tiene el equipo?

4. Casa / vivienda: ¿dónde vives? ¿Cómo es la casa? ¿Cómo es la
   habitación donde te despiertas?

5. Pareja / relaciones: ¿cómo es tu vida personal? ¿Pareja, hijos,
   amistades?

6. Cuerpo / salud: ¿cómo te ves físicamente? ¿Cómo te mueves? ¿Qué
   comes? ¿Cómo duermes?

7. Tiempo / agenda: ¿cuánto trabajas a la semana? ¿Qué rutinas tienes?
   ¿Cuántos viajes haces?

8. Identidad: ¿quién eres en esa vida? ¿Cómo te presentas a alguien
   nuevo? ¿Qué dice de ti la gente que te conoce bien?
```

### Output

`02. Areas/personal/frameworks/Vivid Vision.md` con la estructura del template `03. Sistema/templates/Vivid Vision Framework - Template.md`, rellenado con las respuestas del usuario en primera persona presente.

## Protocol — Life Map

> Visión holística de las áreas de tu vida y dónde estás en cada una.

```
"Vamos a mapear las áreas de tu vida. Te voy a leer 8 áreas. Por cada
una, dame:
- Estado actual: 1-10
- Estado deseado en 1 año: 1-10
- ¿Por qué ese gap? (1 frase)
- 1 acción concreta que reduciría el gap"
```

Áreas:
1. Salud física
2. Salud mental
3. Relaciones íntimas (pareja, familia, amigos cercanos)
4. Carrera / negocio
5. Finanzas
6. Aprendizaje / crecimiento
7. Diversión / ocio
8. Contribución / propósito

Output: `02. Areas/personal/frameworks/Life Map.md` (usa template).

## Protocol — Identity & Values

```
"Vamos a definir quién eres y qué te importa. Dos preguntas, profundas.

1. Identidad: ¿Cuáles son las 3 cosas que mejor te describen como
   persona? No tu profesión, no tus logros — TÚ. Una palabra cada una.
   Y por cada una, una historia de 30 segundos donde se manifestó.

2. Valores: ¿En qué orden ranquearías estos? Y, ¿qué falta?
   - Libertad
   - Crecimiento
   - Tranquilidad
   - Autenticidad
   - Familia / relaciones
   - Impacto
   - Excelencia
   - Aventura
   - Seguridad
   - Disfrute"
```

Output: `02. Areas/personal/frameworks/Identity and Values.md`. **Importante**: el orden de valores se usa en `reviewer` para detectar cuando una decisión va contra los valores top.

## Protocol — Future Self

> "Si pudieras hablar contigo mismo de aquí a 1/3/10 años, ¿qué le preguntarías?"

```
"Te haces tres preguntas a tu yo del futuro:

1. A tu yo de 1 año: ¿qué le preguntarías sobre lo que estás haciendo
   ahora? ¿Y qué crees que te respondería?

2. A tu yo de 3 años: ¿qué patrón dejaste atrás? ¿Cómo te liberaste?

3. A tu yo de 10 años: cuando mira hacia atrás a este momento, ¿qué
   piensa? ¿De qué se siente más orgulloso?"
```

Output: `02. Areas/personal/frameworks/Future Self.md`.

## Protocol — Principles (10 min, opcional)

```
"Sin pensarlo mucho — tu primera respuesta. Lista 5 principios que rigen
tus decisiones. Frase corta cada uno. Si alguno se contradice con tu
comportamiento real, sé honesto: ¿es aspiracional o real?"
```

Output: `02. Areas/personal/frameworks/Principles.md`.

## Protocol — Winner Worksheet (10 min, opcional)

> Hormozi-style. Tu ventaja competitiva personal.

```
1. ¿Qué haces que casi nadie en tu sector hace? (3 cosas).
2. ¿Qué te dicen los demás que destacas? (no lo que crees tú).
3. ¿Qué combinación rara de skills tienes? (técnico + artístico,
   comercial + ingeniero, etc.).
4. ¿Qué haces que parece esfuerzo para otros y a ti te resulta natural?
5. Tu unfair advantage en 1 frase.
```

Output: `02. Areas/personal/frameworks/Winner Worksheet.md`.

## Protocol — Ideal Life Costing (10 min, opcional)

```
"Calcula cuánto cuesta tu vida ideal mensualmente:
- Vivienda
- Comida + bienestar
- Transporte
- Familia / pareja / hijos
- Hobbies / diversión
- Salud
- Aprendizaje / coaching
- Viajes
- Inversión / ahorro
- Imprevistos / colchón

Total mensual → x12 = NOR anual. Compara con tu revenue target de Stage 1."
```

Output: `02. Areas/personal/frameworks/Ideal Life Costing.md`.

## Síntesis final — North Star

Después de los frameworks anteriores, sintetizar todo en `02. Areas/personal/North Star.md`:

```markdown
# North Star — {{user_name}}

> Síntesis estratégica. Re-leer cada quarterly review.

## Quién eres
{{from Identity and Values}}

## Tres horizontes
- **1 año:** {{from Stage 1 + Vivid Vision short version}}
- **3 años:** {{from Vivid Vision full}}
- **10 años:** {{from Future Self}}

## Valores en orden
1. {{...}}
2. {{...}}
3. {{...}}
...

## Principios de decisión
{{from Principles}}

## Ventaja competitiva
{{from Winner Worksheet — 1 frase}}

## Métrica financiera Norte
- NOR mensual: {{from Ideal Life Costing}}
- NOR anual: {{...}}
- Revenue target {{current_year}}: {{from Stage 1}}

## Patrones a romper
{{from Stage 1 patterns — los priority high}}

## Strengths a doblar
{{from Winner Worksheet}}

## Cómo se usa este archivo
- `reviewer` lo lee en cada `/quarterly-review`.
- `esbirrillo` lo consulta cuando el usuario pregunta "¿debo hacer X?".
- Re-leer y actualizar al menos cada quarter.
```

## Confirmación final

```
"Has completado el bloque más profundo del setup. Tienes:
- Vivid Vision a 3 años
- Life Map de 8 áreas
- Identity & Values
- Future Self
- {{optional ones completed}}
- North Star sintetizado

Te recomiendo releer estos archivos en una sesión tranquila con café —
no ahora. Luego volver y editar a mano lo que no resuene. La síntesis
del sistema es buena, pero TU lenguaje siempre es mejor que el mío.

¿Listos para Stage 6?"
```

## Self-annealing

| Date | Issue/Learning | Resolution |
|---|---|---|
