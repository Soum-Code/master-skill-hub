# azure-advisor-actionability

> Remediate Azure Advisor recommendations. WHEN: "fix Advisor recommendation".

| | |
|---|---|
| **ID** | `microsoft/skills:azure-advisor-actionability` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 31 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Present remediation for the customer to run; never execute without explicit confirmation. Require the `recommendationTypeId` GUID and complete affected `resourceId`; reuse known values, ask for missing values, never guess.

## How it is structured

The skill's own section headings, in order:

- Quick reference
- Workflow
- Final response

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:azure-advisor](microsoft-skills-azure-advisor.md) - Use Azure Advisor recommendations. WHEN: "show Advisor recommendations", "service retirements", "update recomm

## Invoke / install

- Invoke: `/microsoft/skills:azure-advisor-actionability`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/azure-advisor/skills/azure-advisor-actionability --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 9bffacafd267cc5102ba950aec54ea250ed5d82d3858828f8f3fdbe41487c04b --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
