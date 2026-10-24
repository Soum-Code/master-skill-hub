# aks-gpu-inference

> Diagnose Day-2 AKS GPU and KAITO incidents using profile-aware, read-only evidence. WHEN: 'Insufficient nvidia.com/gpu', GPU pod Pending, model-load OOM, DCGM/VRAM, KAITO Workspace not ready, or GPU autoscaling. DO NOT USE FOR: setup (airunway-aks-setup), non-GPU incidents (aks-troubleshooting), standalone VM quota (azure-quotas), or generic cost (cost-analysis or cost-optimization from the optional azure-cost plugin).

| | |
|---|---|
| **ID** | `microsoft/skills:aks-gpu-inference` |
| **Pack** | AI / ML Engineering (also: MLOps / DevOps / Cloud, Claude / Skills / Plugin Tooling) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 69 lines in SKILL.md, 5 file(s) |

## When to use it

- DO NOT USE FOR: setup (airunway-aks-setup), non-GPU incidents (aks-troubleshooting), standalone VM quota (azure-quotas), or generic cost (cost-analysis or cost-optimization from the optional azure-cost plugin).

## What it says up front

> Use for scheduling, VRAM/OOM, KAITO readiness, and workload scaling. Route exclusions as described above.

## How it is structured

The skill's own section headings, in order:

- Quick Reference
- When to Use This Skill
- MCP Tools
- Host Capability Gate
- Workflow
- Error Handling

## What it bundles

- reference docs: `references/gpu-cost-and-scaling.md`, `references/gpu-observability.md`, `references/gpu-scheduling.md`, `references/kaito-workspaces.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:aks-troubleshooting](microsoft-skills-aks-troubleshooting.md) - Debug live Azure Kubernetes Service (AKS) incidents with a read-only, evidence-first investigation. WHEN: pod 
- [microsoft/skills:aks-network-capture](microsoft-skills-aks-network-capture.md) - Collects bounded packet captures from AKS nodes and Azure network configuration for wire-level evidence. WHEN:

## Invoke / install

- Invoke: `/microsoft/skills:aks-gpu-inference`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/aks-skills/skills/aks-gpu-inference --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 9e271cc4611a667381317116c5ec1495eba30218aedb1a26c06ef27f87c2ac4d --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
