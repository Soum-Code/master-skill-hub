# codebase-onboarding

> Analyze an unfamiliar codebase and generate a structured onboarding guide with architecture map, key entry points, conventions, and a starter CLAUDE.md. Use when joining a new project or setting up Claude Code for the first time in a repo.

| | |
|---|---|
| **ID** | `affaan-m/ECC:codebase-onboarding` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 235 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when joining a new project or setting up Claude Code for the first time in a repo.

## What it says up front

> Systematically analyze an unfamiliar codebase and produce a structured onboarding guide. Designed for developers joining a new project or setting up Claude Code in an existing repo for the first time.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
  - Phase 1: Reconnaissance
  - Phase 2: Architecture Mapping
  - Phase 3: Convention Detection
  - Phase 4: Generate Onboarding Artifacts
- Best Practices
- Anti-Patterns to Avoid
- Examples
  - Example 1: First time in a new repo
  - Example 2: Generate CLAUDE.md for existing project
  - Example 3: Enhance existing CLAUDE.md

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [init](init.md) - Initialize a project with a CLAUDE.md that documents the codebase for future sessions.
- [affaan-m/ECC:inherit-legacy-style](affaan-m-ecc-inherit-legacy-style.md) - Prevent AI style drift on legacy projects by scanning the codebase for implicit conventions, resolving conflic
- [openai/skills:figma-create-design-system-rules](openai-skills-figma-create-design-system-rules.md) - Generates custom design system rules for the user's codebase. Use when user says "create design system rules",
- [claude-code-setup:claude-automation-recommender](claude-code-setup-claude-automation-recommender.md) - Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use

## Invoke / install

- Invoke: `/affaan-m/ECC:codebase-onboarding`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/codebase-onboarding --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 8f99f7c3d3a752a3c93e6c37a4e8aac9dc13d54e64bb861eda1377ff99eb0b29 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
