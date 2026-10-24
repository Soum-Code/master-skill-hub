# figma-create-new-file

> Create a new blank Figma file. Use when the user wants to create a new Figma design or FigJam file, or when you need a new file before calling use_figma. Handles plan resolution via whoami if needed. Usage — /figma-create-new-file [editorType] [fileName] (e.g. /figma-create-new-file figjam My Whiteboard)

| | |
|---|---|
| **ID** | `openai/skills:figma-create-new-file` |
| **Pack** | Web, Frontend & UI Design |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 69 lines in SKILL.md, 7 file(s) |

## When to use it

- Use when the user wants to create a new Figma design or FigJam file, or when you need a new file before calling use_figma.

## How it is structured

The skill's own section headings, in order:

- Skill Arguments
- Workflow
  - Step 1: Resolve the planKey
  - Step 2: Call create_new_file
  - Step 3: Use the result
- Important Notes

## What it bundles

- 6 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:figma-code-connect-components](openai-skills-figma-code-connect-components.md) - Connects Figma design components to code components using Code Connect mapping tools. Use when user says "code
- [engineering:testing-strategy](engineering-testing-strategy.md) - Design test strategies and test plans. Trigger with "how should we test", "test strategy for", "write tests fo
- [openai/skills:figma-implement-design](openai-skills-figma-implement-design.md) - Translates Figma designs into production-ready application code with 1:1 visual fidelity. Use when implementin
- [openai/skills:figma-generate-library](openai-skills-figma-generate-library.md) - Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create

## Invoke / install

- Invoke: `/openai/skills:figma-create-new-file`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/figma-create-new-file --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree 57a2f2456dfec45e9e7d7e06c19c228fcb4943ab7e43f49722c244d3955de5f4 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
