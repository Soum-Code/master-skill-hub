# webmcp-gen

> Build and validate experimental WebMCP tools for an existing web page. Use when an agent needs to expose a site's real workflows as page tools, create webmcp.init.js, define deterministic checks, or compare WebMCP with accessibility-tree automation.

| | |
|---|---|
| **ID** | `vercel-labs/agent-browser:webmcp-gen` |
| **Pack** | Browser & Web Automation (also: Web, Frontend & UI Design) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) |
| **License** | Apache-2.0 |
| **Size** | 53 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when an agent needs to expose a site's real workflows as page tools, create webmcp.init.js, define deterministic checks, or compare WebMCP with accessibility-tree automation.

## What it says up front

> Create a durable artifact that exposes a real page workflow through WebMCP and proves that the tool behaves like the existing UI.

## How it is structured

The skill's own section headings, in order:

- Output
- Workflow
- Safety
- Completion

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Bash(agent-browser:*)`

## Related skills

- [openai/skills:cli-creator](openai-skills-cli-creator.md) - Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an
- [vercel-labs/agent-skills:web-design-guidelines](vercel-labs-agent-skills-web-design-guidelines.md) - Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility

## Invoke / install

- Invoke: `/vercel-labs/agent-browser:webmcp-gen`
- Install: `python skills/skill-vetter/scripts/install.py vercel-labs/agent-browser --path skill-data/webmcp-gen --commit 04ba5264dade678062c3cdcce0f4f293e748249f --expect-tree c97e93bc35148d0700b2e921dfdbbbf21b5da1b7f099fb9c891f48a053e57a7b --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
