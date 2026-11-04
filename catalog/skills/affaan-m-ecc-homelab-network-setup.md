# homelab-network-setup

> Practical home and homelab network planning for gateways, switches, access points, IP ranges, DHCP reservations, DNS, cabling, and common beginner mistakes. Use when planning or fixing a home or homelab network — gateway, switch, AP, IP ranges, DHCP, DNS, or cabling.

| | |
|---|---|
| **ID** | `affaan-m/ECC:homelab-network-setup` |
| **Pack** | Careers, Jobs & Hiring (also: Claude / Skills / Plugin Tooling) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 131 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when planning or fixing a home or homelab network — gateway, switch, AP, IP ranges, DHCP, DNS, or cabling.

## What it says up front

> Use this skill to design a home or small-lab network that can grow without needing a full rebuild.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
- IP Plan
- DHCP And DNS
- Cabling And Wi-Fi
- Examples
  - Beginner Upgrade
  - VLAN-Ready Plan
- Anti-Patterns
- See Also

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:homelab-network-readiness](affaan-m-ecc-homelab-network-readiness.md) - Readiness checklist for homelab VLAN segmentation, local DNS filtering (Pi-hole, AdGuard Home), and WireGuard-
- [affaan-m/ECC:homelab-vlan-segmentation](affaan-m-ecc-homelab-vlan-segmentation.md) - Segmenting home networks into VLANs for IoT, guest, trusted, and server traffic using UniFi, pfSense/OPNsense,

## Invoke / install

- Invoke: `/affaan-m/ECC:homelab-network-setup`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/homelab-network-setup --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree cd794d73e21c98279ed195602a788d34d9bf69778e5c70f0c09b7f2a06368ed3 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
