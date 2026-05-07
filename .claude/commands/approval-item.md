---
description: Crea un item pendiente de aprobación para acciones L2/L3/L4. No ejecuta la acción.
---

# /approval-item

Crea un item en la cola de approvals.

## Uso

```bash
python3 ${LIFEOS_ROOT}/.claude/execution/approval_item.py <<'JSON'
{
  "owner_agent": "stark",
  "permission_level": "L3",
  "action_type": "send_email",
  "proposed_action": "$ARGUMENTS",
  "why_it_matters": "Necesita decisión explícita de {{USER_FIRSTNAME}} antes de comunicación externa.",
  "risk": "Comunicación externa con impacto reputacional/comercial.",
  "rollback_or_safe_alternative": "Mantener como borrador hasta que {{USER_FIRSTNAME}} apruebe.",
  "approval_options": ["aprobar", "editar", "rechazar"]
}
JSON
```

## Reglas

- No ejecuta nada.
- Solo escribe en `${VAULT_NAME}/00. Inbox/approvals.md` y `.claude/logs/approvals/`.
- Usar para L2 ambiguo, L3 siempre, L4 siempre.
- Si hay duda, crear approval item en vez de actuar.
