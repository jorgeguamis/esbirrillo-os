---
description: Captura de lectura. Convierte lo que leíste hoy en una nota atómica accionable con conexiones y 1 acción concreta.
---

Ejecutar skill de reading capture con librarian.

Lee `.claude/skills/reading-capture/SKILL.md` y ejecuta el flujo.

## Flujo

1. Preguntar: "¿Qué has leído/estudiado hoy?"
2. Capturar 2-5 ideas clave (max 5 bullets)
3. Grep en vault para buscar conexiones con notas existentes:
   - Buscar en `01. Atomic Notes/`
   - Buscar en `02. Areas/aprendizaje/libros/notas/`
4. Definir 1 acción concreta — validar que sea específica
5. Crear nota en `00. Inbox/[titulo-kebab].md` con frontmatter correcto

Si es domingo: revisar notas de Inbox de la semana y elegir 1 idea para aplicar.

Agente: librarian. Anti-acumulación. Español, tutear.
