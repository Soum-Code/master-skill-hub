# ito-compute

> Query live GPU inventory, submit an authenticated Itô fixed-rate RFQ, inspect RFQ or procurement status, revoke device credentials, and run explicitly gated node qualification through the separately installed canonical CLI. Use when a user asks to find H100/H200 capacity, request a fixed compute rate, check Itô compute status, validate GPU nodes, revoke Itô access, or rent or purchase GPU compute and needs the supported boundary explained.

| | |
|---|---|
| **ID** | `affaan-m/ECC:ito-compute` |
| **Pack** | Operations & Business |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 166 lines in SKILL.md, 2 file(s) |

## When to use it

- Use when a user asks to find H100/H200 capacity, request a fixed compute rate, check Itô compute status, validate GPU nodes, revoke Itô access, or rent or purchase GPU compute and needs the supported boundary explained.

## What it says up front

> Use the canonical Itô compute CLI or MCP server. ECC does not implement a parallel client, local simulation, reservation, workload runner, or inference server. ECC itself does no browser automation.

## How it is structured

The skill's own section headings, in order:

- Install the canonical local package
- CLI workflow
- Live node qualification
- MCP workflow
- Rent or purchase semantics
- Unsupported operations

## What it bundles

- 1 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:nasiko-control-plane](affaan-m-ecc-nasiko-control-plane.md) - Manage the experimental Nasiko CLI lifecycle through ECC — read-only status checks, consent-gated install of t
- [affaan-m/ECC:ito-inference](affaan-m-ecc-ito-inference.md) - Inspect the availability of model serving on a completed Itô compute booking and, when the canonical backend b
- [affaan-m/ECC:ito-training](affaan-m-ecc-ito-training.md) - Inspect the availability of ML training on a completed Itô compute booking and, when the canonical backend bec

## Invoke / install

- Invoke: `/affaan-m/ECC:ito-compute`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/ito-compute --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree be0977812fa8ad44a6912edb3d980a1237bd962a87109bfd2dd44ff19eb789ac --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
