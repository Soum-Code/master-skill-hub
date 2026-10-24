# figma-generate-library

> Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create variables/tokens, build component libraries, set up theming (light/dark modes), document foundations, or reconcile gaps between code and Figma. This skill teaches WHAT to build and in WHAT ORDER — it complements the `figma-use` skill which teaches HOW to call the Plugin API. Both skills should be loaded together.

| | |
|---|---|
| **ID** | `openai/skills:figma-generate-library` |
| **Pack** | Web, Frontend & UI Design (also: Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 315 lines in SKILL.md, 23 file(s) |

## When to use it

- Use when the user wants to create variables/tokens, build component libraries, set up theming (light/dark modes), document foundations, or reconcile gaps between code and Figma.

## How it is structured

The skill's own section headings, in order:

- 1. The One Rule That Matters Most
- 2. Mandatory Workflow
- 3. Critical Rules
- 4. State Management (Required for Long Workflows)
- 5. search_design_system — Reuse Decision Matrix
- 6. User Checkpoints
- 7. Naming Conventions
- 8. Token Architecture
- 9. Per-Phase Anti-Patterns
- 10. Reference Docs
- 11. Scripts

## What it bundles

- scripts: `scripts/bindVariablesToComponent.js`, `scripts/cleanupOrphans.js`, `scripts/createComponentWithVariants.js`, `scripts/createDocumentationPage.js`, `scripts/createSemanticTokens.js`, `scripts/createVariableCollection.js`, `scripts/inspectFileStructure.js`, `scripts/rehydrateState.js` ...
- reference docs: `references/code-connect-setup.md`, `references/component-creation.md`, `references/discovery-phase.md`, `references/documentation-creation.md`, `references/error-recovery.md`, `references/naming-conventions.md`, `references/token-creation.md`
- 6 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [openai/skills:figma-generate-design](openai-skills-figma-generate-design.md) - Use this skill alongside figma-use when the task involves translating an application page, view, or multi-sect
- [openai/skills:figma-code-connect-components](openai-skills-figma-code-connect-components.md) - Connects Figma design components to code components using Code Connect mapping tools. Use when user says "code
- [openai/skills:figma-create-design-system-rules](openai-skills-figma-create-design-system-rules.md) - Generates custom design system rules for the user's codebase. Use when user says "create design system rules",
- [openai/skills:figma-implement-design](openai-skills-figma-implement-design.md) - Translates Figma designs into production-ready application code with 1:1 visual fidelity. Use when implementin

## Invoke / install

- Invoke: `/openai/skills:figma-generate-library`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/figma-generate-library --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree c728e0c6cf94c502aa23a260b2775aab48016d7af42f9fc9f0ec2d556b87b128 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
