# aks-cost-optimization

> Analyze advanced AKS cost efficiency. WHEN: "AKS NAP readiness", "AKS bin packing", "AKS node scaling bottleneck", "AKS blocked scale-down", "AKS storage cost". DO NOT USE AS DIRECT ENTRY FOR: overall AKS cost assessments or rightsizing/VPA/CAS/Spot (azure-kubernetes); spend/anomalies/commitments (cost-analysis/cost-optimization); incidents (aks-troubleshooting).

| | |
|---|---|
| **ID** | `microsoft/skills:aks-cost-optimization` |
| **Pack** | Operations & Business |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 41 lines in SKILL.md, 14 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Use for advanced existing-cluster analysis requiring scheduling, placement, or verified storage mapping. Route overall AKS cost assessments to `azure-kubernetes`, spend/anomalies to `cost-analysis`, commitments to `cost-optimization`, and incidents to `aks-troubleshooting` when those skills are avai

## How it is structured

The skill's own section headings, in order:

- When to Use This Skill
- MCP Tools
- Workflow/Steps
- Error Handling

## What it bundles

- reference docs: `references/aks-bin-packing.md`, `references/aks-nap.md`, `references/aks-savings-plans-reservations.md`, `references/aks-storage-optimization.md`, `references/bin-packing-evidence.md`, `references/nap-decisions.md`, `references/nap-enablement-and-rollback.md`, `references/nap-evidence-collection.md` ...

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:cost-analysis](microsoft-skills-cost-analysis.md) - Analyze actual Azure spend, bill changes, and AKS or AI costs. WHEN: "Azure cost breakdown", "most expensive r
- [microsoft/skills:cost-estimation](microsoft-skills-cost-estimation.md) - Forecast Azure spend and price planned resources or workloads. WHEN: "forecast Azure spending", "project next 
- [microsoft/skills:cost-optimization](microsoft-skills-cost-optimization.md) - Optimize existing Azure resources and analyze Reservations or Savings Plans. WHEN: "optimize Azure costs", "re
- [microsoft/skills:aks-troubleshooting](microsoft-skills-aks-troubleshooting.md) - Debug live Azure Kubernetes Service (AKS) incidents with a read-only, evidence-first investigation. WHEN: pod 

## Invoke / install

- Invoke: `/microsoft/skills:aks-cost-optimization`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/aks-skills/skills/aks-cost-optimization --commit 3f5b461b2314e01c400564051e92469114c5b68f --expect-tree 0ce6e004834d67b427d55fbeeda261f00e4677ab49925cab6416acee6e150e3a --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
