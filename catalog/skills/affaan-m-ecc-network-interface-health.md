# network-interface-health

> Diagnose interface errors, drops, CRCs, duplex mismatches, flapping, speed negotiation issues, and counter trends on routers, switches, and Linux hosts. Use when an interface shows errors, drops, CRCs, flapping, or a duplex or speed mismatch.

| | |
|---|---|
| **ID** | `affaan-m/ECC:network-interface-health` |
| **Pack** | Careers, Jobs & Hiring (also: Productivity & Automation) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 154 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when an interface shows errors, drops, CRCs, flapping, or a duplex or speed mismatch.

## What it says up front

> Use this skill when a network symptom might be caused by a physical link, switch port, cable, transceiver, duplex setting, or congested interface.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
- Counter Reference
- Diagnosis Flow
  - CRCs Or Input Errors
  - Drops
  - Duplex And Speed
- Safe Parser Example
- Examples
  - CRCs On One Switch Port
  - Internet Slow But LAN Is Fine
- Anti-Patterns
- See Also

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [bm:health](bm-health.md) - Diagnose planning directory health and optionally repair issues

## Invoke / install

- Invoke: `/affaan-m/ECC:network-interface-health`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/network-interface-health --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 86c3792cb9236ad50751dccb33af4d65bbcd5f8168f1321add3bbee52947a3ae --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
