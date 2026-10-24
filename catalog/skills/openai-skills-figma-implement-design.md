# figma-implement-design

> Translates Figma designs into production-ready application code with 1:1 visual fidelity. Use when implementing UI code from Figma files, when user mentions "implement design", "generate code", "implement component", provides Figma URLs, or asks to build components matching Figma specs. For Figma canvas writes via `use_figma`, use `figma-use`.

| | |
|---|---|
| **ID** | `openai/skills:figma-implement-design` |
| **Pack** | Web, Frontend & UI Design (also: Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 259 lines in SKILL.md, 6 file(s) |

## When to use it

- Use when implementing UI code from Figma files, when user mentions "implement design", "generate code", "implement component", provides Figma URLs, or asks to build components matching Figma specs.

## How it is structured

The skill's own section headings, in order:

- Overview
- Skill Boundaries
- Prerequisites
- Required Workflow
  - Step 1: Get Node ID
  - Step 2: Fetch Design Context
  - Step 3: Capture Visual Reference
  - Step 4: Download Required Assets
  - Step 5: Translate to Project Conventions
  - Step 6: Achieve 1:1 Visual Parity
  - Step 7: Validate Against Figma
- Implementation Rules
  - Component Organization
  - Design System Integration
  - Code Quality
- Examples
  - Example 1: Implementing a Button Component
  - Example 2: Building a Dashboard Layout
- Best Practices
  - Always Start with Context
  - Incremental Validation
  - Document Deviations
  - Reuse Over Recreation
  - Design System First
- Common Issues and Solutions
  - Issue: Figma output is truncated
  - Issue: Design doesn't match after implementation
  - Issue: Assets not loading
  - Issue: Design token values differ from Figma
- Understanding Design Implementation

## What it bundles

- 5 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:figma-code-connect-components](openai-skills-figma-code-connect-components.md) - Connects Figma design components to code components using Code Connect mapping tools. Use when user says "code
- [openai/skills:figma-generate-design](openai-skills-figma-generate-design.md) - Use this skill alongside figma-use when the task involves translating an application page, view, or multi-sect
- [openai/skills:figma](openai-skills-figma.md) - Use the Figma MCP server to fetch design context, screenshots, variables, and assets from Figma, and to transl
- [bm:ui-phase](bm-ui-phase.md) - Generate UI design contract (UI-SPEC.md) for frontend phases

## Invoke / install

- Invoke: `/openai/skills:figma-implement-design`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/figma-implement-design --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree 3f0430cc9b95f11630fee6d1e5651e41892ea3003c46abfa6dafef91316340bd --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
