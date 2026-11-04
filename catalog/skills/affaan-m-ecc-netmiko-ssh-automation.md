# netmiko-ssh-automation

> Safe Python Netmiko patterns for read-only collection, bounded batch SSH, TextFSM parsing, guarded config changes, timeouts, and network automation error handling. Use when automating network device access with Python Netmiko, whether collecting state or pushing guarded config changes.

| | |
|---|---|
| **ID** | `affaan-m/ECC:netmiko-ssh-automation` |
| **Pack** | Browser & Web Automation |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 175 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when automating network device access with Python Netmiko, whether collecting state or pushing guarded config changes.

## What it says up front

> Use this skill when writing or reviewing Python automation that connects to network devices with Netmiko. Keep the default path read-only; config changes need a separate change window, peer review, and rollback plan.

## How it is structured

The skill's own section headings, in order:

- When to Use
- Safety Defaults
- Read-Only Connection Pattern
- Batch Collection
- Structured Parsing
- Guarded Config Pattern
- Review Checklist
- Anti-Patterns
- See Also

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:network-bgp-diagnostics](affaan-m-ecc-network-bgp-diagnostics.md) - Diagnostics-only BGP troubleshooting patterns for neighbor state, route exchange, prefix policy, AS path inspe
- [affaan-m/ECC:dart-flutter-patterns](affaan-m-ecc-dart-flutter-patterns.md) - Production-ready Dart and Flutter patterns covering null safety, immutable state with Freezed, async compositi
- [affaan-m/ECC:cisco-ios-patterns](affaan-m-ecc-cisco-ios-patterns.md) - Cisco IOS and IOS-XE review patterns for show commands, config hierarchy, wildcard masks, ACL placement, inter
- [microsoft/skills:aks-network-capture](microsoft-skills-aks-network-capture.md) - Collects bounded packet captures from AKS nodes and Azure network configuration for wire-level evidence. WHEN:

## Invoke / install

- Invoke: `/affaan-m/ECC:netmiko-ssh-automation`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/netmiko-ssh-automation --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree e2218b6282e530c03265db12fe686ff2ab66541770e45f35056de2250908db08 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
