# Plantilla de Delegación a Claude Code

> Uso: cuando Esbirrillo decide que una tarea requiere trabajo profundo, compleja o multiarchivo.

## Preparación por parte de Esbirrillo

1. **Decidir ruta**: confirmar que `route_task.py` recomienda `claude_code`.
2. **Empaquetar contexto**:
   - Objetivo claro (1 frase).
   - Archivos/fuentes relevantes (rutas exactas).
   - Constraints (no tocar X, no enviar antes de aprobación, etc.).
   - Formato esperado del entregable.
   - Nivel de permiso L1/L2/L3/L4.

## Comando típico

```bash
claude -p "ACTÚA COMO CLAUDE CODE OPERADOR PROFUNDO. TAREA: {objetivo}. LEE: {fuentes}. PRODUCE: {entregable}. CONSTRAINTS: {constraints}. LOGUEA con log_event.py si modificas archivos." \
  --allowedTools "Read,Write,Edit,Bash" \
  --max-turns {15-30 según complejidad} \
  --output-format json \
  --workdir ${LIFEOS_ROOT}
```

## Variables

- `{objetivo}`: qué debe producir (ej: "crea un módulo de {{BUSINESS_SECONDARY}} sobre X").
- `{fuentes}`: archivos relevantes separados por comas (ej: `@Life\ OS/02.\ Areas/business_secondary/{{BUSINESS_SECONDARY}}.md`, `@.claude/skills/class-prep/SKILL.md`).
- `{entregable}`: ruta de salida esperada o formato (ej: "guarda en `Life\ OS/02.\ Areas/business_secondary/modulos/modulo-x.md`").
- `{constraints}`: reglas específicas del dominio (ej: "no enviar propuesta antes de la llamada", "usar formato SKILL.md").

## Verificación post-ejecución

1. Revisar `subtype` y `terminal_reason` del JSON.
2. Revisar que los archivos esperados existen.
3. Si faltan, reintentar con más `--max-turns` o permisos.
4. Resumir a {{USER_FIRSTNAME}}: qué hizo Claude Code, qué cambió, siguiente acción.

## Reglas críticas

- Claude Code NO es solo para código: es para trabajo profundo a secas.
- Si la tarea cabe en 2 minutos o 1 archivo: usar Hermes directo o agente Hermes, no Claude Code.
- Siempre usar `--workdir ${LIFEOS_ROOT}`.
- Nunca pasar secretos en el prompt; usar variables de entorno si es necesario.
