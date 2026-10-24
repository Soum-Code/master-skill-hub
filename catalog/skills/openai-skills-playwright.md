# playwright

> Use when the task requires automating a real browser from the terminal (navigation, form filling, snapshots, screenshots, data extraction, UI-flow debugging) via `playwright-cli` or the bundled wrapper script.

| | |
|---|---|
| **ID** | `openai/skills:playwright` |
| **Pack** | Browser & Web Automation |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 148 lines in SKILL.md, 9 file(s) |

## When to use it

- Use when the task requires automating a real browser from the terminal (navigation, form filling, snapshots, screenshots, data extraction, UI-flow debugging) via `playwright-cli` or the bundled wrapper script.

## How it is structured

The skill's own section headings, in order:

- Prerequisite check (required)
- Skill path (set once)
- Quick start
- Core workflow
- When to snapshot again
- Recommended patterns
  - Form fill and submit
  - Debug a UI flow with traces
  - Multi-tab work
- Wrapper script
- References
- Guardrails

## What it bundles

- scripts: `scripts/playwright_cli.sh`
- reference docs: `references/cli.md`, `references/workflows.md`
- 5 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [agent-browser](agent-browser.md) - Fast browser automation CLI for AI agents (vercel-labs/agent-browser). Use when the user asks to interact with
- [playwright-cli](playwright-cli.md) - Official Microsoft browser automation CLI (@playwright/cli). Use when the user asks to automate browser intera
- [example-skills:webapp-testing](example-skills-webapp-testing.md) - Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend 
- [openai/skills:playwright-interactive](openai-skills-playwright-interactive.md) - Persistent browser and Electron interaction through `js_repl` for fast iterative UI debugging.

## Invoke / install

- Invoke: `/openai/skills:playwright`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/playwright --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree 686558d2ff4cb6e09b64ee39888d86484c069e8620a9f3d04d18dcfbed71dcc5 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
