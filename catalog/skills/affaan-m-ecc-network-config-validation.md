# network-config-validation

> Pre-deployment checks for router and switch configuration, including dangerous commands, duplicate addresses, subnet overlaps, stale references, management-plane risk, and IOS-style security hygiene. Use when reviewing a router or switch configuration before deployment.

| | |
|---|---|
| **ID** | `affaan-m/ECC:network-config-validation` |
| **Pack** | Careers, Jobs & Hiring (also: Claude / Skills / Plugin Tooling, MLOps / DevOps / Cloud) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 212 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when reviewing a router or switch configuration before deployment.

## What it says up front

> Use this skill to review network configuration before a change window or before an automation run touches production devices.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
- Dangerous Command Detection
- Duplicate IPs And Subnet Overlaps
- Management-Plane Checks
- Security Hygiene Checks
- Examples
  - Change-Window Preflight
  - Automation Preflight
- Anti-Patterns
- See Also

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:homelab-network-readiness](affaan-m-ecc-homelab-network-readiness.md) - Readiness checklist for homelab VLAN segmentation, local DNS filtering (Pi-hole, AdGuard Home), and WireGuard-
- [affaan-m/ECC:cisco-ios-patterns](affaan-m-ecc-cisco-ios-patterns.md) - Cisco IOS and IOS-XE review patterns for show commands, config hierarchy, wildcard masks, ACL placement, inter
- [engineering:code-review](engineering-code-review.md) - Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this be
- [affaan-m/ECC:quarkus-verification](affaan-m-ecc-quarkus-verification.md) - Verification loop for Quarkus projects: build, static analysis (Checkstyle, PMD, SpotBugs), tests with JaCoCo 

## Invoke / install

- Invoke: `/affaan-m/ECC:network-config-validation`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/network-config-validation --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 6c825d070752488b1309f18b9a64e3263269a6d7e5b2f8371740e1c378ff2576 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
