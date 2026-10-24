# azure-local-multi-rack

> Plan, deploy, operate, and troubleshoot multi-rack (rack scale) deployments of Azure Local — preintegrated racks scaling to hundreds of machines, built on Network Fabric Controller, Cluster Manager, SAN storage, and managed network fabric. Use for the Microsoft.NetworkCloud and Microsoft.ManagedNetworkFabric control plane. NOT for standard 1-16 node Azure Local, and NOT for rack-aware clusters (two racks as availability zones, up to 8 nodes, synchronous replication) — those are standard scale. WHEN: multi-rack, rack scale Azure Local, aggregation rack, compute rack, Network Fabric Controller, NFC, Cluster Manager, network fabric, isolation domain, az networkcloud, az networkfabric, multi-rack logical network, multi-rack Arc VM.

| | |
|---|---|
| **ID** | `microsoft/skills:azure-local-multi-rack` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 55 lines in SKILL.md, 9 file(s) |

## When to use it

- Use for the Microsoft.NetworkCloud and Microsoft.ManagedNetworkFabric control plane.

## What it says up front

> Use when the deployment is multi-rack / rack scale: preintegrated racks, an aggregation rack, a Network Fabric Controller, a Cluster Manager, SAN storage, or the `networkcloud` / `managednetworkfabric` CLI extensions.

## How it is structured

The skill's own section headings, in order:

- Quick Reference
- When to Use This Skill
- MCP Tools
- Workflow
- Error Handling

## What it bundles

- reference docs: `references/cli-and-prereqs.md`, `references/docs-map.md`, `references/resource-types.md`, `references/safety-rules.md`
- 4 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:azure-local](microsoft-skills-azure-local.md) - Plan, deploy, operate, and troubleshoot Azure Local (formerly Azure Stack HCI): sizing and prerequisites, Arc 

## Invoke / install

- Invoke: `/microsoft/skills:azure-local-multi-rack`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/azure-local-skills/skills/azure-local-multi-rack --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 4fc36d383a0fa10578d2658ed7c4502058b9d297262912c56047935037cabea8 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
