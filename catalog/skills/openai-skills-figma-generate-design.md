# figma-generate-design

> Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Triggers: 'write to Figma', 'create in Figma from code', 'push page to Figma', 'take this app/page and build it in Figma', 'create a screen', 'build a landing page in Figma', 'update the Figma screen to match code'. This is the preferred workflow skill whenever the user wants to build or update a full page, screen, or view in Figma from code or a description. Discovers design system components, variables, and styles via search_design_system, imports them, and assembles screens incrementally section-by-section using design system tokens instead of hardcoded values.

| | |
|---|---|
| **ID** | `openai/skills:figma-generate-design` |
| **Pack** | Web, Frontend & UI Design |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 342 lines in SKILL.md, 7 file(s) |

## When to use it

- Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma.

## How it is structured

The skill's own section headings, in order:

- Skill Boundaries
- Prerequisites
- Parallel Workflow with generate_figma_design (Web Apps Only)
- Required Workflow
  - Step 1: Understand the Screen
  - Step 2: Discover Design System — Components, Variables, and Styles
  - Step 3: Create the Page Wrapper Frame First
  - Step 4: Build Each Section Inside the Wrapper
  - Step 5: Validate the Full Screen
  - Step 6: Updating an Existing Screen
- Reference Docs
- Error Recovery
- Best Practices

## What it bundles

- 6 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:figma-generate-library](openai-skills-figma-generate-library.md) - Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create
- [openai/skills:figma-implement-design](openai-skills-figma-implement-design.md) - Translates Figma designs into production-ready application code with 1:1 visual fidelity. Use when implementin
- [openai/skills:figma-code-connect-components](openai-skills-figma-code-connect-components.md) - Connects Figma design components to code components using Code Connect mapping tools. Use when user says "code
- [openai/skills:figma-create-design-system-rules](openai-skills-figma-create-design-system-rules.md) - Generates custom design system rules for the user's codebase. Use when user says "create design system rules",

## Invoke / install

- Invoke: `/openai/skills:figma-generate-design`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/figma-generate-design --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree d5ec79bc5590daef30c9afb91ae8e2d6a6d85ada8770c40874df84eb08aae7e5 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
