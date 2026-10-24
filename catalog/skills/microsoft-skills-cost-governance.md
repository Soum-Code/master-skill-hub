# cost-governance

> Govern Azure costs with budgets, alerts, tags, and policy restrictions. WHEN: "Azure budget health", "configured budget overrun", "list Azure budgets", "create Azure budget", "budget alerts", "budget coverage", "missing CostCenter tags", "allowed VM SKUs", "allowed Azure regions", "would this SKU be denied", "cost guardrails". DO NOT USE FOR: planning-target forecasts, bill investigations, pricing, rightsizing, or commitments.

| | |
|---|---|
| **ID** | `microsoft/skills:cost-governance` |
| **Pack** | Finance & Accounting (also: MLOps / DevOps / Cloud) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 47 lines in SKILL.md, 5 file(s) |

## When to use it

- DO NOT USE FOR: planning-target forecasts, bill investigations, pricing, rightsizing, or commitments.

## What it says up front

> Use for budgets, alerts, tags, and policy.

## How it is structured

The skill's own section headings, in order:

- Quick Reference
- When to Use This Skill
- MCP Tools
- Workflow
- Error Handling

## What it bundles

- reference docs: `references/budget-health.md`, `references/budget-setup.md`, `references/guardrails.md`, `references/tool-fallback.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:cost-estimation](microsoft-skills-cost-estimation.md) - Forecast Azure spend and price planned resources or workloads. WHEN: "forecast Azure spending", "project next 
- [microsoft/skills:cost-optimization](microsoft-skills-cost-optimization.md) - Optimize existing Azure resources and analyze Reservations or Savings Plans. WHEN: "optimize Azure costs", "re
- [microsoft/skills:cost-analysis](microsoft-skills-cost-analysis.md) - Analyze actual Azure spend, bill changes, and AKS or AI costs. WHEN: "Azure cost breakdown", "most expensive r

## Invoke / install

- Invoke: `/microsoft/skills:cost-governance`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/azure-cost/skills/cost-governance --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree d375d0335dc01d5adff2caddaef2f495ce9471c9596928b12e703e5792470939 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
