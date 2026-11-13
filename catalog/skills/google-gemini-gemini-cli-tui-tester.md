# tui-tester

> Expert guidance for testing Gemini CLI behavior and visual output using terminal automation.

| | |
|---|---|
| **ID** | `google-gemini/gemini-cli:tui-tester` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| **License** | Apache-2.0 |
| **Size** | 66 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> This skill provides the operational manual for verifying Gemini CLI behavioral changes and visual output using terminal automation.

## How it is structured

The skill's own section headings, in order:

- Core Responsibilities
- Critical Protocol
  - 1. Initialization
  - 2. Environment Setup (macOS / Parallel Safe)
  - 3. Session Management
  - 4. Gemini CLI Specifics
- Workflow Example
- Error Recovery

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/playwright-cli:playwright-cli](microsoft-playwright-cli-playwright-cli.md) - Automate browser interactions, test web pages and work with Playwright tests.
- [obra/superpowers:systematic-debugging](obra-superpowers-systematic-debugging.md) - Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes

## Invoke / install

- Invoke: `/google-gemini/gemini-cli:tui-tester`
- Install: `python skills/skill-vetter/scripts/install.py google-gemini/gemini-cli --path .gemini/skills/tui-tester --commit 62bab5b232c15b925d31e655ce844ab939c882b7 --expect-tree c12a1ede9b22682943afcfc03497afa00a482c26fd26aeb1415a67b40e80ce2e --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
