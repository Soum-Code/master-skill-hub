# cli-creator

> Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an admin tool, or a local script. Use when the user wants Codex to create a command-line tool that can run from any repo, expose composable read/write commands, return stable JSON, manage auth, and pair with a companion skill.

| | |
|---|---|
| **ID** | `openai/skills:cli-creator` |
| **Pack** | Software Development (also: Claude / Skills / Plugin Tooling) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 161 lines in SKILL.md, 4 file(s) |

## When to use it

- Use when the user wants Codex to create a command-line tool that can run from any repo, expose composable read/write commands, return stable JSON, manage auth, and pair with a companion skill.

## How it is structured

The skill's own section headings, in order:

- Start
- Choose the Runtime
- Command Contract
- Auth and Config
- Build Workflow
- Rust Defaults
- TypeScript/Node Defaults
- Python Defaults
- Companion Skill

## What it bundles

- reference docs: `references/agent-cli-patterns.md`
- 2 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [huggingface/skills:huggingface-tool-builder](huggingface-skills-huggingface-tool-builder.md) - Use this skill when the user wants to build tool/scripts or achieve a task where using data from the Hugging F
- [bm:new-ddd](bm-new-ddd.md) - Initialize a new project using Documentation-Driven Development. Research, then write user-facing docs (SPEC.m
- [engineering:documentation](engineering-documentation.md) - Write and maintain technical documentation. Trigger with "write docs for", "document this", "create a README",
- [anthropics/claude-plugins-official:build-mcp-server](anthropics-claude-plugins-official-build-mcp-server.md) - This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integrati

## Invoke / install

- Invoke: `/openai/skills:cli-creator`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/cli-creator --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree aeee8a367f1c3b212c1a5342bbeeafae597e1c1cf3cb7a8d037c22f08c409a94 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
