# azure-local

> Plan, deploy, operate, and troubleshoot Azure Local (formerly Azure Stack HCI): sizing and prerequisites, Arc registration, lifecycle updates, workloads (Azure Local VMs, AKS on Azure Local, images, disks, logical networks), SDN and network security, and failure triage — starting read-only and confirming before risky changes. WHEN: Azure Local, Azure Stack HCI, Arc resource bridge, custom location, Azure Local VM, Arc VM, AKS on Azure Local, AKS hybrid, SDN, Lifecycle Manager, Azure Local update, disconnected site.

| | |
|---|---|
| **ID** | `microsoft/skills:azure-local` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 54 lines in SKILL.md, 10 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Use for Azure Local, Azure Stack HCI, Azure Local VMs, AKS on Azure Local, AKS hybrid, SDN, lifecycle updates, disconnected sites, or troubleshooting. Covers standard deployments (1-16 node hyperconverged, up to 64 disaggregated) and rack-aware clusters.

## How it is structured

The skill's own section headings, in order:

- Quick Reference
- When to Use This Skill
- MCP Tools
- Workflow
- Error Handling

## What it bundles

- reference docs: `references/docs-map.md`, `references/mcp-and-cli-tools.md`, `references/resource-types.md`, `references/safety-rules.md`
- 5 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:azure-local-multi-rack](microsoft-skills-azure-local-multi-rack.md) - Plan, deploy, operate, and troubleshoot multi-rack (rack scale) deployments of Azure Local — preintegrated rac

## Invoke / install

- Invoke: `/microsoft/skills:azure-local`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/azure-local-skills/skills/azure-local --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree fa6e32464267d39a8f47fa58ce46ed0cf80e733a246a674d64b0112d273e7354 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
