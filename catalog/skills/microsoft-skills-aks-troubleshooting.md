# aks-troubleshooting

> Debug live Azure Kubernetes Service (AKS) incidents with a read-only, evidence-first investigation. WHEN: pod crashes or Pending, CrashLoopBackOff, OOMKilled, ImagePullBackOff, node NotReady, DNS or ingress failure, connectivity timeout, network policy, SNAT exhaustion, node-pool scaling blocked by QuotaExceeded or InsufficientVCPUQuota, upgrade stuck, spot or zone disruption, a bare VMExtensionProvisioningError or AllocationFailed wrapper, an uncataloged capacity symptom, or 'investigate my AKS cluster'. DO NOT USE FOR: packet capture (use aks-network-capture); GPU or model-serving issues (use aks-gpu-inference); cluster creation or provisioning (use azure-kubernetes); cost (use cost-analysis from the optional azure-cost plugin); pod rightsizing (use azure-kubernetes); a fully qualified documented AKS signature with every required nested qualifier (use aks-known-issues); standalone failures on non-AKS Azure resources (use azure-diagnostics). Unqualified errors and open-ended incidents stay here only for AKS.

| | |
|---|---|
| **ID** | `microsoft/skills:aks-troubleshooting` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 109 lines in SKILL.md, 20 file(s) |

## When to use it

- DO NOT USE FOR: packet capture (use aks-network-capture); GPU or model-serving issues (use aks-gpu-inference); cluster creation or provisioning (use azure-kubernetes); cost (use cost-analysis from the optional azure-cost plugin); pod rightsizing (use azure-kub.

## What it says up front

> Root-cause live AKS incidents with a read-only, evidence-first investigation. This skill covers the full Day-2 troubleshooting surface — workloads, nodes, networking, ingress, upgrades, and spot/zone disruptions — and produces a structured incident report.

## How it is structured

The skill's own section headings, in order:

- Operating rules
- Route by symptom
- Scripts
- AKS-specific gotchas
- Log discipline
- Deep diagnostics
- Report
- Reference

## What it bundles

- scripts: `scripts/cluster-snapshot.sh`, `scripts/pod-deep-dive.sh`
- reference docs: `references/api-server-webhooks-tunnel.md`, `references/auto-upgrade-evidence.md`, `references/azure-mcp.md`, `references/azure-network-path.md`, `references/command-flows.md`, `references/inspektor-gadget.md`, `references/report-template.md`, `references/structured-input-modes.md` ...
- 8 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [microsoft/skills:aks-gpu-inference](microsoft-skills-aks-gpu-inference.md) - Diagnose Day-2 AKS GPU and KAITO incidents using profile-aware, read-only evidence. WHEN: 'Insufficient nvidia
- [microsoft/skills:aks-known-issues](microsoft-skills-aks-known-issues.md) - Lookup documented AKS fixes only when the prompt includes an exact catalog signature and all of its qualifiers
- [microsoft/skills:aks-network-capture](microsoft-skills-aks-network-capture.md) - Collects bounded packet captures from AKS nodes and Azure network configuration for wire-level evidence. WHEN:

## Invoke / install

- Invoke: `/microsoft/skills:aks-troubleshooting`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/aks-skills/skills/aks-troubleshooting --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree d6cf72df51daa6be4a865fc210132c87212a36ae6d95876534e99aed3a7a27d0 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
