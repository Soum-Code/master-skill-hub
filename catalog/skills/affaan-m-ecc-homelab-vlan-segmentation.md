# homelab-vlan-segmentation

> Segmenting home networks into VLANs for IoT, guest, trusted, and server traffic using UniFi, pfSense/OPNsense, and MikroTik — including switch trunk config, firewall rules, and wireless SSID mapping. Use when splitting a home network into IoT, guest, trusted, and server VLANs on UniFi, pfSense/OPNsense, or MikroTik.

| | |
|---|---|
| **ID** | `affaan-m/ECC:homelab-vlan-segmentation` |
| **Pack** | Careers, Jobs & Hiring |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 313 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when splitting a home network into IoT, guest, trusted, and server VLANs on UniFi, pfSense/OPNsense, or MikroTik.

## What it says up front

> How to split a home network into isolated VLANs so IoT devices, guests, and your main PCs cannot talk to each other. The most impactful security upgrade for a home network.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
- VLAN Design Template
- Examples
- UniFi Configuration
  - Create Networks in UniFi Controller
  - Map SSIDs to VLANs (UniFi)
  - UniFi Firewall Rules (Traffic Rules)
- pfSense / OPNsense Configuration
  - Create VLANs
  - DHCP for Each VLAN
  - Firewall Rules (pfSense/OPNsense)
- MikroTik Configuration
- Switch Trunk vs Access Ports
- Anti-Patterns
- Best Practices
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:homelab-network-readiness](affaan-m-ecc-homelab-network-readiness.md) - Readiness checklist for homelab VLAN segmentation, local DNS filtering (Pi-hole, AdGuard Home), and WireGuard-
- [affaan-m/ECC:homelab-network-setup](affaan-m-ecc-homelab-network-setup.md) - Practical home and homelab network planning for gateways, switches, access points, IP ranges, DHCP reservation

## Invoke / install

- Invoke: `/affaan-m/ECC:homelab-vlan-segmentation`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/homelab-vlan-segmentation --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree a73845642b212e27c7220649b78606adecfd6f304b809cdd2ff565375d461e41 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
