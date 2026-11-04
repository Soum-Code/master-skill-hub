# ito-training

> Inspect the availability of ML training on a completed Itô compute booking and, when the canonical backend becomes available, hand off an explicitly confirmed training manifest. Use after ito-compute has booked GPU nodes and the user wants pre-training, fine-tuning, or RL on that metal. ECC implements no training stack of its own.

| | |
|---|---|
| **ID** | `affaan-m/ECC:ito-training` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 124 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> `ito-training` is the canonical ECC skill for training on Itô compute. ECC never runs a trainer, scheduler, or data pipeline of its own; it never books, reserves, or spends. This skill chains off a **completed booking** from `ito-compute`.

## How it is structured

The skill's own section headings, in order:

- Current production boundary
- Required entitlement
- Future CLI and API contract
- Confirmation and execution gates
- Lifecycle and recovery
- Proposed backend stages

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:ito-inference](affaan-m-ecc-ito-inference.md) - Inspect the availability of model serving on a completed Itô compute booking and, when the canonical backend b
- [affaan-m/ECC:ito-compute](affaan-m-ecc-ito-compute.md) - Query live GPU inventory, submit an authenticated Itô fixed-rate RFQ, inspect RFQ or procurement status, revok
- [affaan-m/ECC:manim-video](affaan-m-ecc-manim-video.md) - Build reusable Manim explainers for technical concepts, graphs, system diagrams, and product walkthroughs, the

## Invoke / install

- Invoke: `/affaan-m/ECC:ito-training`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/ito-training --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 5ba4bc280916711306bd14a0d33e32694b664eae51753074bc586ea6300f2cd9 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
