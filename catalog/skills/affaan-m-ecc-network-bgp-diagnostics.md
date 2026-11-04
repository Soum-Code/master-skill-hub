# network-bgp-diagnostics

> Diagnostics-only BGP troubleshooting patterns for neighbor state, route exchange, prefix policy, AS path inspection, and safe evidence collection. Use when a BGP neighbor is down, routes are missing, or prefix policy and AS path need inspection.

| | |
|---|---|
| **ID** | `affaan-m/ECC:network-bgp-diagnostics` |
| **Pack** | Careers, Jobs & Hiring (also: Legal & Compliance) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 169 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when a BGP neighbor is down, routes are missing, or prefix policy and AS path need inspection.

## What it says up front

> Use this skill when a BGP session is down, flapping, established with missing routes, or advertising unexpected prefixes. The default workflow is read-only evidence collection; policy and reset actions belong in a reviewed change window.

## How it is structured

The skill's own section headings, in order:

- When to Use
- Read-Only Triage Flow
- State Interpretation
- Transport Checks
- Route Policy Checks
- AS Path And Prefix Review
- Parser Pattern
- Change-Window Only
- Anti-Patterns
- See Also

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:netmiko-ssh-automation](affaan-m-ecc-netmiko-ssh-automation.md) - Safe Python Netmiko patterns for read-only collection, bounded batch SSH, TextFSM parsing, guarded config chan
- [microsoft/skills:aks-network-capture](microsoft-skills-aks-network-capture.md) - Collects bounded packet captures from AKS nodes and Azure network configuration for wire-level evidence. WHEN:

## Invoke / install

- Invoke: `/affaan-m/ECC:network-bgp-diagnostics`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/network-bgp-diagnostics --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 5456af5ca6ef2570842bf6a3a0ed86034fc3eac522acf51c475121d4ef82252c --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
