# figma

> Use the Figma MCP server to fetch design context, screenshots, variables, and assets from Figma, and to translate Figma nodes into production code. Trigger when a task involves Figma URLs, node IDs, design-to-code implementation, or Figma MCP setup and troubleshooting.

| | |
|---|---|
| **ID** | `openai/skills:figma` |
| **Pack** | Web, Frontend & UI Design |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 43 lines in SKILL.md, 8 file(s) |

## When to use it

- Trigger when a task involves Figma URLs, node IDs, design-to-code implementation, or Figma MCP setup and troubleshooting.

## How it is structured

The skill's own section headings, in order:

- Figma MCP Integration Rules
  - Required flow (do not skip)
  - Implementation rules
  - Asset handling
  - Link-based prompting
- References

## What it bundles

- reference docs: `references/figma-mcp-config.md`, `references/figma-tools-and-prompts.md`
- 5 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:figma-implement-design](openai-skills-figma-implement-design.md) - Translates Figma designs into production-ready application code with 1:1 visual fidelity. Use when implementin
- [openai/skills:figma-generate-design](openai-skills-figma-generate-design.md) - Use this skill alongside figma-use when the task involves translating an application page, view, or multi-sect
- [openai/skills:figma-create-design-system-rules](openai-skills-figma-create-design-system-rules.md) - Generates custom design system rules for the user's codebase. Use when user says "create design system rules",
- [openai/skills:figma-code-connect-components](openai-skills-figma-code-connect-components.md) - Connects Figma design components to code components using Code Connect mapping tools. Use when user says "code

## Invoke / install

- Invoke: `/openai/skills:figma`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/figma --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree 3e0eb599c6269a18d85c16858af3df907520b330598db93bcefad20165e5cb25 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
