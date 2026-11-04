# living-docs-governance

> Keep a long-lived project's documentation from rotting by assigning existing project docs clear constitution, map, status, and history roles, then wiring the active agent harness to those canonical sources. Use in the maintain phase when docs drift from code, agents lose context between sessions, or intentional removals keep being recreated. Prefer adopting the repository's current docs structure over creating new root files. 中文触发：文档治理、活文档、项目状态追踪、防文档漂移、项目地图、健康仪表盘、删除区、长期项目治理

| | |
|---|---|
| **ID** | `affaan-m/ECC:living-docs-governance` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 148 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Long-lived projects often rot at the documentation layer first: the README describes an old pipeline, architecture notes describe a refactor that never shipped, and every new session re-derives context that should already be available.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- How It Works
  - 1. Inventory before creating anything
  - 2. Assign four roles
  - 3. Wire the active harness honestly
  - 4. Treat documentation as evidence, not executable truth
  - 5. Update only the role affected
  - Module-local maintenance
- Lightweight Adoption Template
- Examples

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:docs-governance](affaan-m-ecc-docs-governance.md) - Route broad documentation-governance requests to existing ECC skills and run an opt-in, read-only audit of map

## Invoke / install

- Invoke: `/affaan-m/ECC:living-docs-governance`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/living-docs-governance --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 72f532155c2a0ecb680f17d9436240f0073b707996de668ffec0cd8a7f818f91 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
