# ticket-triage

> Triage and prioritize a support ticket or customer issue. Use when a new ticket comes in and needs categorization, assigning P1-P4 priority, deciding which team should handle it, or checking whether it's a duplicate or known issue before routing.

| | |
|---|---|
| **ID** | `anthropics/knowledge-work-plugins:ticket-triage` |
| **Pack** | Communication & Collaboration |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 276 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when a new ticket comes in and needs categorization, assigning P1-P4 priority, deciding which team should handle it, or checking whether it's a duplicate or known issue before routing.

## What it says up front

> Categorize, prioritize, and route an incoming support ticket or customer issue. Produces a structured triage assessment with a suggested initial response.

## How it is structured

The skill's own section headings, in order:

- Usage
- Workflow
  - 1. Parse the Issue
  - 2. Categorize and Prioritize
  - 3. Check for Duplicates and Known Issues
  - 4. Determine Routing
  - 5. Generate Triage Output
  - 6. Offer Next Steps
- Category Taxonomy
  - Category Determination Tips
- Priority Framework
  - P1 — Critical
  - P2 — High
  - P3 — Medium
  - P4 — Low
  - Priority Escalation Triggers
- Routing Rules
- Duplicate Detection
- Auto-Response Templates by Category
  - Bug — Initial Response
  - How-to — Initial Response
  - Feature Request — Initial Response
  - Billing — Initial Response
  - Security — Initial Response
- Triage Best Practices

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/knowledge-work-plugins:kb-article](anthropics-knowledge-work-plugins-kb-article.md) - Draft a knowledge base article from a resolved issue or common question. Use when a ticket resolution is worth
- [openai/skills:linear](openai-skills-linear.md) - Manage issues, projects & team workflows in Linear. Use when the user wants to read, create or updates tickets

## Invoke / install

- Invoke: `/anthropics/knowledge-work-plugins:ticket-triage`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/knowledge-work-plugins --path customer-support/skills/ticket-triage --commit 33d3dea41a341b341d4f5da2e8801ae0c89be2b8 --expect-tree afe6cac98d23a452de13536b8f745fe3f3464739b2e3844376642f13ac0ec9e0 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
