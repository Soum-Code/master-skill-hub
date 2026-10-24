# cost-estimation

> Forecast Azure spend and price planned resources or workloads. WHEN: "forecast Azure spending", "project next month cost", "compare forecast to my planning target", "how much will Azure cost", "estimate VM cost", "compare storage tiers", "compare Azure regions", "retail price", "EA rate card", "negotiated pricesheet". DO NOT USE FOR: configured budget health or alerts, bill analysis, cost spikes, rightsizing, or commitments.

| | |
|---|---|
| **ID** | `microsoft/skills:cost-estimation` |
| **Pack** | Spec-driven Dev Workflow (also: Data & Analytics, Finance & Accounting, MLOps / DevOps / Cloud) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 50 lines in SKILL.md, 8 file(s) |

## When to use it

- DO NOT USE FOR: configured budget health or alerts, bill analysis, cost spikes, rightsizing, or commitments.

## What it says up front

> Use for forecasts, pricing, and planning targets.

## How it is structured

The skill's own section headings, in order:

- Quick Reference
- When to Use This Skill
- MCP Tools
- Workflow
- Error Handling

## What it bundles

- reference docs: `references/cost-forecast/error-handling.md`, `references/cost-forecast/examples.md`, `references/cost-forecast/guardrails.md`, `references/cost-forecast/request-body-schema.md`, `references/cost-forecast/workflow.md`, `references/pricing-estimate.md`, `references/tool-fallback.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:cost-governance](microsoft-skills-cost-governance.md) - Govern Azure costs with budgets, alerts, tags, and policy restrictions. WHEN: "Azure budget health", "configur
- [microsoft/skills:cost-analysis](microsoft-skills-cost-analysis.md) - Analyze actual Azure spend, bill changes, and AKS or AI costs. WHEN: "Azure cost breakdown", "most expensive r
- [microsoft/skills:cost-optimization](microsoft-skills-cost-optimization.md) - Optimize existing Azure resources and analyze Reservations or Savings Plans. WHEN: "optimize Azure costs", "re
- [operations:capacity-plan](operations-capacity-plan.md) - Plan resource capacity — workload analysis and utilization forecasting. Use when heading into quarterly planni

## Invoke / install

- Invoke: `/microsoft/skills:cost-estimation`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/azure-cost/skills/cost-estimation --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 2b85378cdf309f6ea340bb3437ec2746158693ba26bcf5433d8441cf97857d7a --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
