# tasteforge-video

> Use for file-driven multimodal image, video, and 3D-asset discovery; taste interviews; distill or apply workflows; style-pack validation; editable EDL/FCPXML export; provenance audits; and offline planning that must fail closed before provider generation.

| | |
|---|---|
| **ID** | `affaan-m/ECC:tasteforge-video` |
| **Pack** | Creative & Media |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 257 lines in SKILL.md, 1 file(s) |

## When to use it

- Use for file-driven multimodal image, video, and 3D-asset discovery; taste interviews; distill or apply workflows; style-pack validation; editable EDL/FCPXML export; provenance audits; and offline planning that must fail closed before provider generation.

## What it says up front

> For the complete standalone creative pipeline, use `taste-distillation` then `taste-application`. Those ECC skills ship their Python scripts directly: measure references, generate or pass through existing takes, grade, cut, composite, verify, and hand off to Blender and Resolve. No separate video re

## How it is structured

The skill's own section headings, in order:

- When to Use
- Local Deterministic Operations vs Provider Generation
- Canonical Implementation
- Chaining the Creative Skills
- Workflow
  - Applying Real Footage Without Repeated Sources
- File-Driven Multimodal Contract
- Example Session

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:taste-application](affaan-m-ecc-taste-application.md) - Generate new video against a distilled style pack and cut it into a finished piece - plan takes from the refer

## Invoke / install

- Invoke: `/affaan-m/ECC:tasteforge-video`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/tasteforge-video --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 2172fdd799d16d8c2ecdf7a45c5d0ed62236828186b5dd6c8f77647fa859f3a8 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
