# runbook

> Create or update an operational runbook for a recurring task or procedure. Use when documenting a task that on-call or ops needs to run repeatably, turning tribal knowledge into exact step-by-step commands, adding troubleshooting and rollback steps to an existing procedure, or writing escalation paths for when things go wrong.

| | |
|---|---|
| **ID** | `operations:runbook` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `operations` v1.3.0 - [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | not declared |
| **Size** | 88 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when documenting a task that on-call or ops needs to run repeatably, turning tribal knowledge into exact step-by-step commands, adding troubleshooting and rollback steps to an existing procedure, or writing escalation paths for when things go wrong.

## How it is structured

The skill's own section headings, in order:

- Usage
- Output
- If Connectors Available
- Tips

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [engineering:documentation](engineering-documentation.md) - Write and maintain technical documentation. Trigger with "write docs for", "document this", "create a README",
- [anthropic-skills:schedule](anthropic-skills-schedule.md) - Create or update a scheduled task that runs automatically. Use when the user says things like "every day", "ea
- [operations:change-request](operations-change-request.md) - Create a change management request with impact analysis and rollback plan. Use when proposing a system or proc
- [anthropics/claude-code:Writing Hookify Rules](anthropics-claude-code-writing-hookify-rules.md) - This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hooki

## Invoke / install

- Invoke: `/operations:runbook`  (Skill tool: `operations:runbook`)
- Install: `bundled with Claude desktop (Cowork plugin 'operations'); source: github.com/anthropics/knowledge-work-plugins`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
