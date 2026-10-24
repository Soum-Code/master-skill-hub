# derive-client

> Reverse-engineer a website's internal API by recording browser traffic into a HAR file, then generate a standalone client or CLI that calls the endpoints directly, with no browser needed after the first recording. Use when asked to "derive a client", "build a CLI for ", "reverse engineer this site's API", "record network requests", "turn this site into an API", or when the same site will be automated repeatedly and direct HTTP calls would beat driving the browser every time.

| | |
|---|---|
| **ID** | `vercel-labs/agent-browser:derive-client` |
| **Pack** | Browser & Web Automation (also: Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) |
| **License** | Apache-2.0 |
| **Size** | 87 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when asked to "derive a client", "build a CLI for ", "reverse engineer this site's API", "record network requests", "turn this site into an API", or when the same site will be automated repeatedly and direct HTTP calls would beat driving the browser every.

## What it says up front

> Driving a browser is the right tool for the first visit and the wrong tool for the hundredth. This skill records a site's network traffic once while you use it, then turns the captured requests into a standalone client (script, CLI, or library) that talks to the site's internal API directly.

## How it is structured

The skill's own section headings, in order:

- Workflow
- 1. Record
- 2. Identify endpoints
- 3. Extract shapes and auth
- 4. Generate the client
- 5. Verify
- Caveats

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Bash(agent-browser:*)`, `Bash(npx`, `agent-browser:*)`

## Invoke / install

- Invoke: `/vercel-labs/agent-browser:derive-client`
- Install: `python skills/skill-vetter/scripts/install.py vercel-labs/agent-browser --path skill-data/derive-client --commit 372ac5ce20fab885dbf45ee0c9d510ec8c3b6fdb --expect-tree b94eece089eea1db18670cb44e4b95db9f89e4e3b6ee6b1a7335cf3d3d545352 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
