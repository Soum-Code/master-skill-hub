# design-handoff

> Generate developer handoff specs from a design. Use when a design is ready for engineering and needs a spec sheet covering layout, design tokens, component props, interaction states, responsive breakpoints, edge cases, and animation details.

| | |
|---|---|
| **ID** | `anthropics/knowledge-work-plugins:design-handoff` |
| **Pack** | Web, Frontend & UI Design (also: Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 132 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when a design is ready for engineering and needs a spec sheet covering layout, design tokens, component props, interaction states, responsive breakpoints, edge cases, and animation details.

## What it says up front

> Generate comprehensive developer handoff documentation from a design.

## How it is structured

The skill's own section headings, in order:

- Usage
- What to Include
  - Visual Specifications
  - Interaction Specifications
  - Content Specifications
  - Edge Cases
  - Accessibility
- Principles
- Output
- If Connectors Available
- Tips

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:figma-implement-design](openai-skills-figma-implement-design.md) - Translates Figma designs into production-ready application code with 1:1 visual fidelity. Use when implementin
- [bm:ui-phase](bm-ui-phase.md) - Generate UI design contract (UI-SPEC.md) for frontend phases
- [impeccable:impeccable](impeccable-impeccable.md) - Use when the user wants to design, redesign, shape, critique, audit, polish, clarify, distill, harden, optimiz

## Invoke / install

- Invoke: `/anthropics/knowledge-work-plugins:design-handoff`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/knowledge-work-plugins --path design/skills/design-handoff --commit 33d3dea41a341b341d4f5da2e8801ae0c89be2b8 --expect-tree 1e45edd1daa04faf14f9230c93f5c513032066b5747197b1fc6012fc88e62e32 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
