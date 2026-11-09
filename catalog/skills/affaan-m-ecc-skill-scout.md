# skill-scout

> Search existing local, marketplace, GitHub, and web skill sources before creating a new skill. Use when the user wants to create, build, fork, or find a skill for a workflow.

| | |
|---|---|
| **ID** | `affaan-m/ECC:skill-scout` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 142 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user wants to create, build, fork, or find a skill for a workflow.

## What it says up front

> Use this skill before creating a new skill. The goal is to avoid duplicating existing community or marketplace work, while still vetting anything external before adoption.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
  - Step 1 - Capture Intent
  - Step 2 - Search Local Sources
  - Step 3 - Search Remote Sources
  - Step 4 - Vet External Matches
  - Step 5 - Rank Results
  - Step 6 - Present Decision Options
- Examples
  - Result Table
  - User-Facing Summary
- Anti-Patterns
- Related

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [google-gemini/gemini-cli:skill-creator](google-gemini-gemini-cli-skill-creator.md) - Guide for creating effective skills. This skill should be used when users want to create a new skill (or updat
- [affaan-m/ECC:search-first](affaan-m-ecc-search-first.md) - Research-before-coding workflow: search npm/PyPI, MCP servers, skills, and GitHub for existing tools before wr
- [openai/skills:cli-creator](openai-skills-cli-creator.md) - Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an
- [cowork-plugin-management:create-cowork-plugin](cowork-plugin-management-create-cowork-plugin.md) - Guide users through creating a new plugin from scratch in a cowork session. Use when users want to create a pl

## Invoke / install

- Invoke: `/affaan-m/ECC:skill-scout`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/skill-scout --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree f8ea955c097ae4927570e6a3325a4cbe359ea22618046c520a0fad60f047fc71 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
