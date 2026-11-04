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

- [affaan-m/ECC:skill-scout](affaan-m-ecc-skill-scout.md) - Search existing local, marketplace, GitHub, and web skill sources before creating a new skill. Use when the us
- [affaan-m/ECC:frontend-design-direction](affaan-m-ecc-frontend-design-direction.md) - Set an ECC-specific frontend design direction for production UI work. Use when building or improving websites,
- [affaan-m/ECC:search-first](affaan-m-ecc-search-first.md) - Research-before-coding workflow: search npm/PyPI, MCP servers, skills, and GitHub for existing tools before wr
- [openai/skills:cli-creator](openai-skills-cli-creator.md) - Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an

## Invoke / install

- Invoke: `/vercel-labs/agent-browser:webmcp-gen`
- Install: `python skills/skill-vetter/scripts/install.py vercel-labs/agent-browser --path skill-data/webmcp-gen --commit 5868f7c05020e047c00e68e4abf9253cce864f41 --expect-tree c97e93bc35148d0700b2e921dfdbbbf21b5da1b7f099fb9c891f48a053e57a7b --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
