# cost-optimization

> Optimize existing Azure resources and analyze Reservations or Savings Plans. WHEN: "optimize Azure costs", "reduce cloud spending", "rightsize resources", "find idle resources", "orphaned disk", "deleted VM still charged", "public IP still charging", "reservation utilization", "Savings Plan coverage", "commitment recommendation", "why is pay-as-you-go still charged". DO NOT USE FOR: cost spikes, forecasts, pricing estimates, budgets, or governance.

| | |
|---|---|
| **ID** | `microsoft/skills:cost-optimization` |
| **Pack** | Operations & Business (also: MLOps / DevOps / Cloud, Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 45 lines in SKILL.md, 9 file(s) |

## When to use it

- DO NOT USE FOR: cost spikes, forecasts, pricing estimates, budgets, or governance.

## What it says up front

> Use for waste, rightsizing, and commitments.

## How it is structured

The skill's own section headings, in order:

- Quick Reference
- When to Use This Skill
- MCP Tools
- Workflow
- Error Handling

## What it bundles

- reference docs: `references/commitments.md`, `references/optimization.md`, `references/report-template.md`, `references/resource-graph.md`, `references/services/redis.md`, `references/services/storage-lifecycle.md`, `references/services/storage.md`, `references/tool-fallback.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:cost-analysis](microsoft-skills-cost-analysis.md) - Analyze actual Azure spend, bill changes, and AKS or AI costs. WHEN: "Azure cost breakdown", "most expensive r
- [microsoft/skills:cost-estimation](microsoft-skills-cost-estimation.md) - Forecast Azure spend and price planned resources or workloads. WHEN: "forecast Azure spending", "project next 
- [microsoft/skills:cost-governance](microsoft-skills-cost-governance.md) - Govern Azure costs with budgets, alerts, tags, and policy restrictions. WHEN: "Azure budget health", "configur

## Invoke / install

- Invoke: `/microsoft/skills:cost-optimization`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/azure-cost/skills/cost-optimization --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 9bb60cccb8846095b9c5e318ce2b62571ba5546726a9e2681ae84d46cbfff70c --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
