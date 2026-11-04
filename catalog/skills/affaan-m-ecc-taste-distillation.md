# taste-distillation

> Measure a set of reference videos into a reusable style pack - colour grade as a 3D LUT, cut rhythm as a shot-length distribution, hero stills, screen-blend overlay plates, and a text spec for a generative model. Use when the user wants to capture the look of reference footage, build a repeatable look, mint assets from references, or reproduce someone's grade and pacing.

| | |
|---|---|
| **ID** | `affaan-m/ECC:taste-distillation` |
| **Pack** | Web, Frontend & UI Design (also: Creative & Media) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 201 lines in SKILL.md, 15 file(s) |

## When to use it

- Use when the user wants to capture the look of reference footage, build a repeatable look, mint assets from references, or reproduce someone's grade and pacing.

## What it says up front

> This standalone skill ships its implementation in `scripts/`; use `taste-application` for the subsequent generated or local-take edit. Keep each named genre in its own pack. Measurements from Flash Ethereal must not be silently reused for Fluid Sketch or 3D Cyber Glitch. A measured zero is valid dat

## How it is structured

The skill's own section headings, in order:

- When to Activate
- The Core Finding
- What a Pack Contains
- Running It
- The Measurements That Matter
  - Chroma by luminance zone, not globally
  - Median + MAD, never mean + std
  - Contrast is std(L\*), not white minus black
  - Background share is a first-class statistic
  - Mask the interface before measuring
  - Cadence needs an adaptive threshold
- Overlay Plates: Assets, Not Screenshots
- Grounding the VLM
- LUT Baking Gotchas
- Anti-Patterns
- Handoff
- Bundled Code

## What it bundles

- scripts: `scripts/distill.py`, `scripts/mint.py`, `scripts/taste/__init__.py`, `scripts/taste/assemble.py`, `scripts/taste/cadence.py`, `scripts/taste/falapi.py`, `scripts/taste/frames.py`, `scripts/taste/grade.py` ...
- 2 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [affaan-m/ECC:taste-application](affaan-m-ecc-taste-application.md) - Generate new video against a distilled style pack and cut it into a finished piece - plan takes from the refer
- [affaan-m/ECC:video-editing](affaan-m-ecc-video-editing.md) - AI-assisted video editing workflows for cutting, structuring, and augmenting real footage. Covers the full pip

## Invoke / install

- Invoke: `/affaan-m/ECC:taste-distillation`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/taste-distillation --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree cbaddcf5d23acbfc7b6c5153093ae41eb1f293fb7a7be37c34c1efb591212320 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
