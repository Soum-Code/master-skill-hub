# azure-advisor

> Use Azure Advisor. WHEN: "show recommendations", "top Advisor actions", "prioritize recommendations", "service retirements", "update status". DO NOT USE FOR: fixes (use azure-advisor-actionability).

| | |
|---|---|
| **ID** | `microsoft/skills:azure-advisor` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 39 lines in SKILL.md, 1 file(s) |

## When to use it

- DO NOT USE FOR: fixes (use azure-advisor-actionability).

## What it says up front

> Prefer Azure Advisor MCP tools. Use their current schemas for parameters and limits; discover unfamiliar parameters rather than inventing them.

## How it is structured

The skill's own section headings, in order:

- Quick reference
- Workflow
- Safety

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:azure-advisor-actionability](microsoft-skills-azure-advisor-actionability.md) - Remediate Azure Advisor recommendations. WHEN: "fix Advisor recommendation".

## Invoke / install

- Invoke: `/microsoft/skills:azure-advisor`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/azure-advisor/skills/azure-advisor --commit 0696600436a9669184ce47e8d8b2ceac62e4bfac --expect-tree 451240444e0150e07d25d643e3981354bcb99fa6ce0986e8bc4604f9c5818d36 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
