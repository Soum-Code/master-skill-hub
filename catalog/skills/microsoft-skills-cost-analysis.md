# cost-analysis

> Analyze actual Azure spend, bill changes, and AKS or AI costs. WHEN: "Azure cost breakdown", "most expensive resources", "why did my bill increase", "cost spike", "unexpected charge", "Cosmos DB charges", "Foundry model costs", "AKS cluster cost", "namespace cost", "enable AKS cost analysis", "idle AKS capacity". DO NOT USE FOR: forecasts, pricing estimates, rightsizing, commitments, or budgets.

| | |
|---|---|
| **ID** | `microsoft/skills:cost-analysis` |
| **Pack** | Data & Analytics (also: Research & Learning) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 47 lines in SKILL.md, 13 file(s) |

## When to use it

- DO NOT USE FOR: forecasts, pricing estimates, rightsizing, commitments, or budgets.

## What it says up front

> Use for spend, anomalies, and AKS or AI allocation.

## How it is structured

The skill's own section headings, in order:

- Quick Reference
- When to Use This Skill
- MCP Tools
- Workflow
- Error Handling

## What it bundles

- reference docs: `references/ai-cost-analysis.md`, `references/aks-anomaly.md`, `references/aks-cost-analysis.md`, `references/aks-enablement.md`, `references/cost-investigation.md`, `references/cost-query/dimensions-by-scope.md`, `references/cost-query/error-handling.md`, `references/cost-query/examples.md` ...

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:cost-estimation](microsoft-skills-cost-estimation.md) - Forecast Azure spend and price planned resources or workloads. WHEN: "forecast Azure spending", "project next 
- [microsoft/skills:cost-optimization](microsoft-skills-cost-optimization.md) - Optimize existing Azure resources and analyze Reservations or Savings Plans. WHEN: "optimize Azure costs", "re
- [microsoft/skills:cost-governance](microsoft-skills-cost-governance.md) - Govern Azure costs with budgets, alerts, tags, and policy restrictions. WHEN: "Azure budget health", "configur

## Invoke / install

- Invoke: `/microsoft/skills:cost-analysis`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/azure-cost/skills/cost-analysis --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree c4e74832073378dcd84a634467c239992efcb710f6d2a3e5497da51c8d6dcd45 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
