# customer-escalation

> Package an escalation for engineering, product, or leadership with full context. Use when a bug needs engineering attention beyond normal support, multiple customers report the same issue, a customer is threatening to churn, or an issue has sat unresolved past its SLA.

| | |
|---|---|
| **ID** | `anthropics/knowledge-work-plugins:customer-escalation` |
| **Pack** | Product Management |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 249 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when a bug needs engineering attention beyond normal support, multiple customers report the same issue, a customer is threatening to churn, or an issue has sat unresolved past its SLA.

## What it says up front

> Package a support issue into a structured escalation brief for engineering, product, or leadership. Gathers context, structures reproduction steps, assesses business impact, and identifies the right escalation target.

## How it is structured

The skill's own section headings, in order:

- Usage
- Workflow
  - 1. Understand the Issue
  - 2. Gather Context
  - 3. Assess Business Impact
  - 4. Determine Escalation Target
  - 5. Structure Reproduction Steps (for bugs)
  - 6. Generate Escalation Brief
  - 7. Offer Next Steps
- When to Escalate vs. Handle in Support
  - Handle in Support When:
  - Escalate When:
- Escalation Tiers
  - L1 → L2 (Support Escalation)
  - L2 → Engineering
  - L2 → Product
  - Any → Security
  - Any → Leadership
- Business Impact Assessment
  - Impact Dimensions
  - Severity Shorthand
- Writing Reproduction Steps
- Follow-up Cadence After Escalation
  - Follow-up Actions
- De-escalation
- Escalation Best Practices

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/anthropics/knowledge-work-plugins:customer-escalation`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/knowledge-work-plugins --path customer-support/skills/customer-escalation --commit 33d3dea41a341b341d4f5da2e8801ae0c89be2b8 --expect-tree 76cbe08aa4f6d796589d8981d8cc351966357dedc24cd6077d03e5aa58e71c86 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
