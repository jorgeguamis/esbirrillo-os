# Execution Layer (DOE Framework)

> Capa de ejecución determinística. Scripts que los skills invocan para operaciones repetitivas sin juicio del LLM.

## Qué es esto

En el framework DOE (Directive-Orchestration-Execution):
- **Directive** = Skills (`.claude/skills/`) — qué hacer y cómo
- **Orchestration** = Agents (`.claude/agents/`) — quién lo hace
- **Execution** = Scripts (`.claude/execution/`) — código determinístico que hace el trabajo

Esta carpeta contiene scripts de negocio que ejecutan operaciones concretas contra APIs externas (Notion, etc.). A diferencia de `.claude/scripts/` (utilidades genéricas como `get_youtube_transcript.py`), estos scripts son invocados directamente por skills para eliminar variabilidad del LLM.

## Convenciones

### Naming
```
{accion}_{servicio}.py
```
Ejemplos:
- `notion_create_expense.py` — Crear gasto en Notion
- `notion_create_income.py` — Crear ingreso en Notion
- `notion_update_lead.py` — Actualizar lead en CRM

### Estructura de cada script

```python
"""
Script: nombre_del_script.py
Skill: skill que lo invoca
Descripción: qué hace en una línea
"""

import os
import json
import sys

def main():
    # 1. Leer argumentos (JSON via stdin o args)
    # 2. Validar campos requeridos
    # 3. Ejecutar operación (API call)
    # 4. Retornar resultado (JSON a stdout)
    pass

if __name__ == "__main__":
    main()
```

### I/O Standard
- **Input:** JSON via stdin o argumentos CLI
- **Output:** JSON a stdout con `{"success": true/false, "data": {...}, "error": "..."}`
- **Errores:** Exit code 1 + JSON con campo `error`

## Cuándo crear un script

**SÍ crear script cuando:**
- Operación repetida 3+ veces
- 100% determinística (mismos inputs → mismos outputs)
- No requiere juicio ni interpretación del LLM
- Interactúa con API externa (Notion, Calendar, etc.)

**NO crear script cuando:**
- Requiere interpretación de contexto
- Varía significativamente entre ejecuciones
- Operación one-shot o rara
- El LLM necesita decidir qué hacer (eso es un skill)

## Cómo los skills referencian scripts

En el SKILL.md, añadir sección:
```markdown
## Execution Scripts
- `notion_create_expense.py` — Crear registro en DB Expenses
```

Y en el proceso del skill:
```
3. Ejecutar: `.claude/execution/notion_create_expense.py` con datos confirmados
```

## Variables de entorno

Los scripts leen API keys de variables de entorno (nunca hardcoded):
- `NOTION_API_KEY` — API key de Notion
- Configurar en `.env` del proyecto o exportar en shell
