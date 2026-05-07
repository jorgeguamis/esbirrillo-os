# 02. Areas

Áreas de tu vida y negocio. Cada área tiene un **context file** (markdown) que es la "AI memory" para esa área. Los agentes y skills leen estos archivos antes de generar output.

## Estructura

```
02. Areas/
├── personal/
│   ├── Personal.md              ← context file (creado por /setup-wizard)
│   ├── North Star.md            ← orientación 1/3/10 años
│   ├── memory.md                ← patterns tracking
│   ├── frameworks/              ← Vivid Vision, Life Map, Identity, etc.
│   ├── diario/                  ← daily / weekly / monthly / quarterly / annual
│   ├── relaciones/              ← gente con la que tienes relación directa
│   └── objetivos/               ← goals 1y / 3y / 10y
├── business/                    ← un subfolder por negocio (creado por /setup-wizard)
├── health/
├── learning/
└── finances/
```

Las carpetas de área se rellenan al ejecutar `/setup-wizard`. Cada una recibe un `Context.md` (`Personal.md`, `Health.md`, etc.) con preguntas guiadas que tú respondes.

## Cómo se usan

Antes de generar:
- Daily briefs (`/morning`)
- Reviews (`/weekly-review`, `/monthly-review`, `/quarterly-review`)
- Coaching (`/reflect`)
- Decisiones estratégicas

Los agentes **leen primero los context files relevantes**. Mantén estos archivos actualizados.

## Cuándo actualizar

- Cuando cambien tus prioridades.
- Después de un quarterly review.
- Cuando descubras un patrón nuevo (registrar en `memory.md`).
- Con `/update-context` cuando un patrón se repite en daily notes.
