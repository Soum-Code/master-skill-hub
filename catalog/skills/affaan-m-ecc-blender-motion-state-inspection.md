# blender-motion-state-inspection

> Use this skill when inspecting Blender characters, rigs, poses, animation retargeting, ground contact, facing direction, or model-vs-motion alignment where screenshots alone are not enough.

| | |
|---|---|
| **ID** | `affaan-m/ECC:blender-motion-state-inspection` |
| **Pack** | Web, Frontend & UI Design |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 166 lines in SKILL.md, 1 file(s) |

## When to use it

- Use this skill when inspecting Blender characters, rigs, poses, animation retargeting, ground contact, facing direction, or model-vs-motion alignment where screenshots alone are not enough.

## What it says up front

> Do not judge animated 3D assets only from screenshots. Screenshots are review evidence, but they hide axis conventions, bone names, object scale, local transforms, parented meshes, material slots, and frame-by-frame contact state.

## How it is structured

The skill's own section headings, in order:

- When to Use
- Core Principle
- How It Works
- Inspection Workflow
- Recommended Report Shape
- Examples
  - Walk Cycle With Foot Sliding
  - Backwards Imported Character
- Practical Thresholds
- Anti-Patterns
- Tooling Notes

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/affaan-m/ECC:blender-motion-state-inspection`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/blender-motion-state-inspection --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree e7da87423f01aaf8d0f4aa10f0f9aef4a8ad8ae3ecdc4044ff38f420870c581e --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
