# azure-advisor

> Use Azure Advisor recommendations. WHEN: "show Advisor recommendations", "service retirements", "update recommendation status". DO NOT USE FOR: fixes or remediation (use azure-advisor-actionability).

| | |
|---|---|
| **ID** | `microsoft/skills:azure-advisor` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 37 lines in SKILL.md, 1 file(s) |

## When to use it

- DO NOT USE FOR: fixes or remediation (use azure-advisor-actionability).

## What it says up front

> Prefer Azure Advisor MCP tools over Resource Graph or generic ARM tools.

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
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/azure-advisor/skills/azure-advisor --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 15a2a586941378a94956cbb9de28141556d7ec5c87630e2ddd016576e44d3fc8 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
