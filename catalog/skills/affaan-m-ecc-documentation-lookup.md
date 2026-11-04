# documentation-lookup

> Use up-to-date library and framework docs via Context7 MCP instead of training data. Activates for setup questions, API references, code examples, or when the user names a framework (e.g. React, Next.js, Prisma).

| | |
|---|---|
| **ID** | `affaan-m/ECC:documentation-lookup` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 92 lines in SKILL.md, 1 file(s) |

## When to use it

- Activates for setup questions, API references, code examples, or when the user names a framework (e.g.

## What it says up front

> When the user asks about libraries, frameworks, or APIs, fetch current documentation via the Context7 MCP (tools `resolve-library-id` and `query-docs`) instead of relying on training data.

## How it is structured

The skill's own section headings, in order:

- Core Concepts
- When to use
- How it works
  - Step 1: Resolve the Library ID
  - Step 2: Select the Best Match
  - Step 3: Fetch the Documentation
  - Step 4: Use the Documentation
- Examples
  - Example: Next.js middleware
  - Example: Prisma query
  - Example: Supabase auth methods
- Best Practices

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:exa-search](affaan-m-ecc-exa-search.md) - Neural search via Exa MCP for web, code, and company research. Use when the user needs web search, code exampl
- [openai/skills:openai-docs](openai-skills-openai-docs.md) - Use when the user asks how to build with OpenAI products or APIs, asks about Codex itself or choosing Codex su
- [bm:new-ddd](bm-new-ddd.md) - Initialize a new project using Documentation-Driven Development. Research, then write user-facing docs (SPEC.m
- [affaan-m/ECC:backend-patterns](affaan-m-ecc-backend-patterns.md) - Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js, 

## Invoke / install

- Invoke: `/affaan-m/ECC:documentation-lookup`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/documentation-lookup --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 5c33016081bcc3c77349611a0026801ce2cf8e83fa5aa53034f39972c001ee45 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
