# cisco-ios-patterns

> Cisco IOS and IOS-XE review patterns for show commands, config hierarchy, wildcard masks, ACL placement, interface hygiene, and safe change-window verification. Use when reading, writing, or reviewing Cisco IOS / IOS-XE configuration or planning a change window.

| | |
|---|---|
| **ID** | `affaan-m/ECC:cisco-ios-patterns` |
| **Pack** | Operations & Business (also: Software Development, Spec-driven Dev Workflow) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 165 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when reading, writing, or reviewing Cisco IOS / IOS-XE configuration or planning a change window.

## What it says up front

> Use this skill when reviewing Cisco IOS or IOS-XE snippets, building a change-window checklist, or explaining how to collect evidence from a router or switch without making the incident worse.

## How it is structured

The skill's own section headings, in order:

- When to Use
- Operating Rules
- Mode Reference
- Read-Only Collection
- Wildcard Masks
- ACL Placement Review
- Interface Hygiene
- Change-Window Verification
- Anti-Patterns
- See Also

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:network-config-validation](affaan-m-ecc-network-config-validation.md) - Pre-deployment checks for router and switch configuration, including dangerous commands, duplicate addresses, 
- [affaan-m/ECC:typescript-patterns](affaan-m-ecc-typescript-patterns.md) - TypeScript patterns for strict, type-safe, maintainable code in modern TypeScript and JavaScript applications.
- [affaan-m/ECC:netmiko-ssh-automation](affaan-m-ecc-netmiko-ssh-automation.md) - Safe Python Netmiko patterns for read-only collection, bounded batch SSH, TextFSM parsing, guarded config chan
- [affaan-m/ECC:rust-patterns](affaan-m-ecc-rust-patterns.md) - Idiomatic Rust patterns, ownership, error handling, traits, concurrency, and best practices for building safe,

## Invoke / install

- Invoke: `/affaan-m/ECC:cisco-ios-patterns`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/cisco-ios-patterns --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree c9c6a6a88a6cf7df4d7d77115786a3eaf7dcdfb5960de92660ec0022c34f657e --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
