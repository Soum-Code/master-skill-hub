# computer-use

> Read this skill before the first step of any request to do something in an app on the person's own computer (Notes, Finder, System Settings, any desktop app), to look at their screen, or for "computer use". Computer use (desktop control) lets Claude take screenshots of the person's desktop and control it with clicks, typing and scrolling through the Claude desktop app; its tools are named mcp__computer-use__* when the session runs in the desktop app and mcp__remote-devices__computer_* when a cloud session is linked to the person's computer; before computer use is turned on for a conversation there may be no such tools, only an enable__mcp__remote-devices__computer tool, which turns it on. It covers turning it on, picking the right tool, the access flow, and the safety rules for tiered apps, links and financial actions. It is not for websites, which go through Claude in Chrome or the built-in browser and their own skills.

| | |
|---|---|
| **ID** | `anthropic-skills:computer-use` |
| **Pack** | Claude / Skills / Plugin Tooling (also: AI / ML Engineering, Browser & Web Automation) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `anthropic-skills` |
| **License** | Proprietary. LICENSE.txt has complete terms |
| **Size** | 68 lines in SKILL.md, 2 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Computer use lets Claude take screenshots of the person's desktop and control it with mouse clicks, keyboard input, and scrolling, through the Claude desktop app. Its tools are named `mcp__computer-use__*` (for example `request_access`, `screenshot`) when the session runs inside the desktop app, and

## How it is structured

The skill's own section headings, in order:

- Turning computer use on from a chat
- Separate filesystems
- Pick the right tool for the app
- Look before asserting
- Loading via ToolSearch
- Access flow
- Tiered apps
- Link safety
- Financial actions

## What it bundles

- 1 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropic-skills:built-in-browser](anthropic-skills-built-in-browser.md) - Read this skill before the first step that uses the built-in browser, the browser pane inside the Claude deskt
- [anthropic-skills:chrome-browser](anthropic-skills-chrome-browser.md) - Read this skill before the first step that uses Claude in Chrome, the browser extension whose tools are named 
- [anthropic-skills:docs](anthropic-skills-docs.md) - docs (editable docs people share and comment on; the default for any document, named as a doc or not: a docume
- [agent-browser](agent-browser.md) - Fast browser automation CLI for AI agents (vercel-labs/agent-browser). Use when the user asks to interact with

## Invoke / install

- Invoke: `/anthropic-skills:computer-use`  (Skill tool: `anthropic-skills:computer-use`)
- Install: `built into the Claude desktop app / claude.ai`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
