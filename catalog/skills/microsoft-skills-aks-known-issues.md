# aks-known-issues

> Lookup documented AKS fixes only when the prompt includes an exact catalog signature and all of its qualifiers: VMCannotFitEphemeralOSDisk; NodePoolMcVersionIncompatible; 'NodeImageVersion is not accepted'; AKS SkuNotAvailable with size, location, and zone; ZonalAllocationFailed with insufficient zone capacity; OverconstrainedAllocationRequest with listed constraints; nested AKS vmssCSE/CSE VMExtensionError_OutboundConnFail, VMExtensionError_K8SAPIServerConnFail, or VMExtensionError_K8SAPIServerDNSLookupFail; or AllocationFailed with the full cataloged internal-error or insufficient-regional-capacity message. Never use for quota errors, code-only or bare wrappers, generic symptoms, incomplete signatures, or failures outside AKS; use aks-troubleshooting or azure-diagnostics.

| | |
|---|---|
| **ID** | `microsoft/skills:aks-known-issues` |
| **Pack** | Operations & Business |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 48 lines in SKILL.md, 2 file(s) |

## When to use it

- Never use for quota errors, code-only or bare wrappers, generic symptoms, incomplete signatures, or failures outside AKS; use aks-troubleshooting or azure-diagnostics.

## What it says up front

> Use the [catalog](references/error-code-map.md).

## How it is structured

The skill's own section headings, in order:

- Quick Reference
- When to Use This Skill
- MCP Tools
- Workflow
- Error Handling

## What it bundles

- reference docs: `references/error-code-map.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:aks-troubleshooting](microsoft-skills-aks-troubleshooting.md) - Debug live Azure Kubernetes Service (AKS) incidents with a read-only, evidence-first investigation. WHEN: pod 

## Invoke / install

- Invoke: `/microsoft/skills:aks-known-issues`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/aks-skills/skills/aks-known-issues --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree a5238e21d6848d00e2a2427ddef7bd2a1096055800fb5ad32ac7af97307a2ec0 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
