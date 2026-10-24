# figma-code-connect-components

> Connects Figma design components to code components using Code Connect mapping tools. Use when user says "code connect", "connect this component to code", "map this component", "link component to code", "create code connect mapping", or wants to establish mappings between Figma designs and code implementations. For canvas writes via `use_figma`, use `figma-use`.

| | |
|---|---|
| **ID** | `openai/skills:figma-code-connect-components` |
| **Pack** | Web, Frontend & UI Design |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 350 lines in SKILL.md, 8 file(s) |

## When to use it

- Use when user says "code connect", "connect this component to code", "map this component", "link component to code", "create code connect mapping", or wants to establish mappings between Figma designs and code implementations.

## How it is structured

The skill's own section headings, in order:

- Overview
- Skill Boundaries
- Prerequisites
- Required Workflow
  - Step 1: Get Code Connect Suggestions
  - Step 2: Scan Codebase for Matching Components
  - Step 3: Present Matches to User
  - Step 4: Create Code Connect Mappings
- Examples
  - Example 1: Connecting a Button Component
  - Example 2: Multiple Components with Partial Selection
  - Example 3: Component Needs Creation
- Best Practices
  - Proactive Component Discovery
  - Accurate Structure Matching
  - Clear Communication
  - Handle Ambiguity
  - Graceful Degradation
- Common Issues and Solutions
  - Issue: "No published components found in this selection"
  - Issue: "Code Connect is only available on Organization and Enterprise plans"
  - Issue: No matching component found in codebase
  - Issue: "Published component not found" (CODE_CONNECT_ASSET_NOT_FOUND)
  - Issue: "Component is already mapped to code" (CODE_CONNECT_MAPPING_ALREADY_EXISTS)
  - Issue: "Insufficient permissions to create mapping" (CODE_CONNECT_INSUFFICIENT_PERMISSIONS
  - Issue: Code Connect mapping fails with URL errors
  - Issue: Multiple similar components found
- Understanding Code Connect
- Additional Resources

## What it bundles

- scripts: `scripts/normalize_node_id.py`
- reference docs: `references/mapping-checklist.md`
- 5 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [openai/skills:figma-implement-design](openai-skills-figma-implement-design.md) - Translates Figma designs into production-ready application code with 1:1 visual fidelity. Use when implementin
- [openai/skills:figma-create-design-system-rules](openai-skills-figma-create-design-system-rules.md) - Generates custom design system rules for the user's codebase. Use when user says "create design system rules",
- [openai/skills:figma-create-new-file](openai-skills-figma-create-new-file.md) - Create a new blank Figma file. Use when the user wants to create a new Figma design or FigJam file, or when yo
- [openai/skills:figma-generate-library](openai-skills-figma-generate-library.md) - Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create

## Invoke / install

- Invoke: `/openai/skills:figma-code-connect-components`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/figma-code-connect-components --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree bf53c381d17d3deedcd2f50c0e377fd3aa8268f6c3d542be92aaa20ef1272165 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
