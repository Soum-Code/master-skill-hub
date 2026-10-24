# playwright-cli

> Automate browser interactions, test web pages and work with Playwright tests.

| | |
|---|---|
| **ID** | `microsoft/playwright-cli:playwright-cli` |
| **Pack** | Browser & Web Automation |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) |
| **License** | Apache-2.0 |
| **Size** | 490 lines in SKILL.md, 11 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Some pages register their own tools for agents through the experimental WebMCP API. When a page has them, the page status says so, and the snapshot lists them at the top. Run `webmcp-list` to get the same list and schemas without taking a snapshot:

## How it is structured

The skill's own section headings, in order:

- Quick start
- Commands
  - Core
  - Navigation
  - Keyboard
  - Mouse
  - Save as
  - Tabs
  - Storage
  - Emulation
  - Network
  - DevTools
  - WebMCP
- Raw output
- Open parameters
- URLs with `&` on Windows
- Snapshots
- Targeting elements
- Browser Sessions
- Installation
- Example: Form submission
- Example: Multi-tab workflow
- Example: Debugging with DevTools
- Example: Interactive session
- Attaching screenshots and videos to pull requests
- Specific tasks

## What it bundles

- reference docs: `references/element-attributes.md`, `references/playwright-tests.md`, `references/pr-attachments.md`, `references/request-mocking.md`, `references/running-code.md`, `references/session-management.md`, `references/storage-state.md`, `references/test-generation.md` ...

## Permissions and risk notes

- Pre-approved tools: `Bash(playwright-cli:*)`, `Bash(npx`, `playwright:*)`, `Bash(npx`, `--no-install`, `playwright:*)`

## Related skills

- [playwright-cli](playwright-cli.md) - Official Microsoft browser automation CLI (@playwright/cli). Use when the user asks to automate browser intera
- [example-skills:webapp-testing](example-skills-webapp-testing.md) - Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend 
- [openai/skills:playwright-interactive](openai-skills-playwright-interactive.md) - Persistent browser and Electron interaction through `js_repl` for fast iterative UI debugging.
- [agent-browser](agent-browser.md) - Fast browser automation CLI for AI agents (vercel-labs/agent-browser). Use when the user asks to interact with

## Invoke / install

- Invoke: `/microsoft/playwright-cli:playwright-cli`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/playwright-cli --path skills/playwright-cli --commit b1a5903c5b633b8c9f843ad7b629c2a78437040c --expect-tree 7aeb3b814f01f5bdedbe91a1ecd6b650430faa8c56e6b8ecf5e4e9351a406ee8 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
