# webapp-testing

> Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.

| | |
|---|---|
| **ID** | `example-skills:webapp-testing` |
| **Pack** | Browser & Web Automation (also: Software Development) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `example-skills` v3b3fad96af16 - [anthropics/skills](https://github.com/anthropics/skills) |
| **License** | Complete terms in LICENSE.txt |
| **Size** | 96 lines in SKILL.md, 6 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> To test local web applications, write native Python Playwright scripts.

## How it is structured

The skill's own section headings, in order:

- Decision Tree: Choosing Your Approach
- Example: Using with_server.py
- Reconnaissance-Then-Action Pattern
- Common Pitfall
- Best Practices
- Reference Files

## What it bundles

- scripts: `examples/console_logging.py`, `examples/element_discovery.py`, `examples/static_html_automation.py`, `scripts/with_server.py`
- 1 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [microsoft/playwright-cli:playwright-cli](microsoft-playwright-cli-playwright-cli.md) - Automate browser interactions, test web pages and work with Playwright tests.
- [openai/skills:playwright-interactive](openai-skills-playwright-interactive.md) - Persistent browser and Electron interaction through `js_repl` for fast iterative UI debugging.
- [openai/skills:playwright](openai-skills-playwright.md) - Use when the task requires automating a real browser from the terminal (navigation, form filling, snapshots, s
- [agent-browser](agent-browser.md) - Fast browser automation CLI for AI agents (vercel-labs/agent-browser). Use when the user asks to interact with

## Invoke / install

- Invoke: `/example-skills:webapp-testing`  (Skill tool: `example-skills:webapp-testing`)
- Install: `claude plugin marketplace add anthropics/skills && claude plugin install example-skills@anthropic-agent-skills`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
