# aks-network-capture

> Collects bounded packet captures from AKS nodes and Azure network configuration for wire-level evidence. WHEN: "capture packets on an AKS node", "take a pcap", "run tcpdump on AKS", "prove where packets drop". Use for explicit packet-capture intent after read-only diagnostics, not general AKS connectivity or ingress troubleshooting.

| | |
|---|---|
| **ID** | `microsoft/skills:aks-network-capture` |
| **Pack** | Careers, Jobs & Hiring |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 64 lines in SKILL.md, 13 file(s) |

## When to use it

- Use for explicit packet-capture intent after read-only diagnostics, not general AKS connectivity or ingress troubleshooting.

## What it says up front

> Use for explicit packet capture after read-only checks, not generic connectivity failures.

## How it is structured

The skill's own section headings, in order:

- Quick Reference
- When to Use This Skill
- MCP Tools
- Host Capability Gate
- Workflow/Steps
- Error Handling

## What it bundles

- scripts: `scripts/collect-azure-network-info.ps1`, `scripts/collect-azure-network-info.sh`, `scripts/create-capture.ps1`, `scripts/create-capture.sh`, `scripts/generate-test-traffic.ps1`, `scripts/generate-test-traffic.sh`, `scripts/retrieve-captures.ps1`, `scripts/retrieve-captures.sh` ...
- reference docs: `references/capture-authorization.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [microsoft/skills:aks-troubleshooting](microsoft-skills-aks-troubleshooting.md) - Debug live Azure Kubernetes Service (AKS) incidents with a read-only, evidence-first investigation. WHEN: pod 
- [microsoft/skills:aks-gpu-inference](microsoft-skills-aks-gpu-inference.md) - Diagnose Day-2 AKS GPU and KAITO incidents using profile-aware, read-only evidence. WHEN: 'Insufficient nvidia

## Invoke / install

- Invoke: `/microsoft/skills:aks-network-capture`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/aks-skills/skills/aks-network-capture --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 8b5d9d98653606aeccc1eeaa376f8006aaaa4c3ac1b71507d14b85fc46a1b893 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
