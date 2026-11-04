# taste-application

> Generate new video against a distilled style pack and cut it into a finished piece - plan takes from the reference's cut rhythm, generate on fal, grade with the pack's measured LUT, cut at the measured cadence, weave in existing footage, composite overlay plates, mint 3D props, and verify the result numerically. Use when the user wants to make a video in a captured style, supplement existing footage, or assemble generated clips into a real edit.

| | |
|---|---|
| **ID** | `affaan-m/ECC:taste-application` |
| **Pack** | Web, Frontend & UI Design (also: Creative & Media) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 353 lines in SKILL.md, 81 file(s) |

## When to use it

- Use when the user wants to make a video in a captured style, supplement existing footage, or assemble generated clips into a real edit.

## What it says up front

> The second half of the pipeline. **taste-distillation** measures references into a style pack; this generates against that pack and cuts the result.

## How it is structured

The skill's own section headings, in order:

- Execution and Delivery Contract
- When to Activate
- Division of Labour
- Generate TAKES, Not Shots
- Cutting Rules
- Grading Rules
- Recovered fal Platform Behavior
  - Endpoint picks
- The 3D Branch
- Verify, Then Believe
- Full Chain
- Anti-Patterns
- Borrowed Footage Carries the Capture App's UI
- Overlay Plates Are Elements, Not Washes
- Downstream Handoff (Resolve / Blender)
- Bundled Code

## What it bundles

- scripts: `scripts/apply.py`, `scripts/blender_prop.py`, `scripts/distill.py`, `scripts/falapi.py`, `scripts/forge.py`, `scripts/mint.py`, `scripts/mint3d.py`, `scripts/pipeline.py` ...
- 60 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [affaan-m/ECC:taste-distillation](affaan-m-ecc-taste-distillation.md) - Measure a set of reference videos into a reusable style pack - colour grade as a 3D LUT, cut rhythm as a shot-
- [affaan-m/ECC:video-editing](affaan-m-ecc-video-editing.md) - AI-assisted video editing workflows for cutting, structuring, and augmenting real footage. Covers the full pip
- [affaan-m/ECC:tasteforge-video](affaan-m-ecc-tasteforge-video.md) - Use for file-driven multimodal image, video, and 3D-asset discovery; taste interviews; distill or apply workfl

## Invoke / install

- Invoke: `/affaan-m/ECC:taste-application`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/taste-application --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree e829b6886a4be76ec40563d94ffb5fe4a29d74e4487cdc1006d164f1413d1b1f --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
