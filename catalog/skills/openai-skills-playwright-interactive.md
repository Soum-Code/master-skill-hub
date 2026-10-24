# playwright-interactive

> Persistent browser and Electron interaction through `js_repl` for fast iterative UI debugging.

| | |
|---|---|
| **ID** | `openai/skills:playwright-interactive` |
| **Pack** | Browser & Web Automation |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 694 lines in SKILL.md, 6 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## How it is structured

The skill's own section headings, in order:

- Preconditions
- One-time setup
- Core Workflow
- Bootstrap (Run Once)
- Choose Session Mode
- Start or Reuse Web Session
  - Desktop Web Context
  - Mobile Web Context
  - Native-Window Web Pass
- Start or Reuse Electron Session
- Reuse Sessions During Iteration
- Checklists
  - Session Loop
  - Reload Decision
  - Functional QA
  - Visual QA
  - Signoff
- Screenshot Examples
  - Model-bound screenshots (default)
  - Web CSS normalization
  - Electron CSS normalization
  - Raw Screenshot Exception Examples
- Viewport Fit Checks (Required)
- Dev Server
- Cleanup
- Common Failure Modes

## What it bundles

- 5 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/playwright-cli:playwright-cli](microsoft-playwright-cli-playwright-cli.md) - Automate browser interactions, test web pages and work with Playwright tests.
- [example-skills:webapp-testing](example-skills-webapp-testing.md) - Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend 
- [openai/skills:playwright](openai-skills-playwright.md) - Use when the task requires automating a real browser from the terminal (navigation, form filling, snapshots, s
- [bm:debug](bm-debug.md) - Systematic debugging with persistent state across context resets

## Invoke / install

- Invoke: `/openai/skills:playwright-interactive`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/playwright-interactive --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree 35ee18f48e8ca2febac7e93487fa5b56263fd55841bf38f4b017918b72fbf8a1 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
