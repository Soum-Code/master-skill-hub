# homelab-network-readiness

> Readiness checklist for homelab VLAN segmentation, local DNS filtering (Pi-hole, AdGuard Home), and WireGuard-style remote access. Use when planning or reviewing home network changes — splitting a flat network into trusted, IoT, guest, or management VLANs, moving DHCP to a local resolver, or adding VPN access — before changing router, firewall, DHCP, or VPN configuration.

| | |
|---|---|
| **ID** | `affaan-m/ECC:homelab-network-readiness` |
| **Pack** | Careers, Jobs & Hiring |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 171 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when planning or reviewing home network changes — splitting a flat network into trusted, IoT, guest, or management VLANs, moving DHCP to a local resolver, or adding VPN access — before changing router, firewall, DHCP, or VPN configuration.

## What it says up front

> Use this skill before changing a home or small-lab network that mixes VLANs, Pi-hole or another local DNS resolver, firewall rules, and remote VPN access.

## How it is structured

The skill's own section headings, in order:

- When to Use
- Safety Rules
- Required Inventory
- VLAN And Trust-Zone Plan
- DNS Filtering Readiness
- Remote Access Readiness
- Change Sequence
- Review Checklist
- Anti-Patterns
- See Also

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:homelab-vlan-segmentation](affaan-m-ecc-homelab-vlan-segmentation.md) - Segmenting home networks into VLANs for IoT, guest, trusted, and server traffic using UniFi, pfSense/OPNsense,
- [affaan-m/ECC:homelab-network-setup](affaan-m-ecc-homelab-network-setup.md) - Practical home and homelab network planning for gateways, switches, access points, IP ranges, DHCP reservation
- [affaan-m/ECC:network-config-validation](affaan-m-ecc-network-config-validation.md) - Pre-deployment checks for router and switch configuration, including dangerous commands, duplicate addresses, 

## Invoke / install

- Invoke: `/affaan-m/ECC:homelab-network-readiness`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/homelab-network-readiness --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree c7f8434474a40076cd97fa17250fc34de0e4b9a898b415a0945dcbc7d3b90d3c --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
