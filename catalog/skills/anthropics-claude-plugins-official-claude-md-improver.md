# claude-md-improver

> Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md files. Scans for all CLAUDE.md files, evaluates quality against templates, outputs quality report, then makes targeted updates. Also use when the user mentions "CLAUDE.md maintenance" or "project memory optimization".

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:claude-md-improver` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 180 lines in SKILL.md, 4 file(s) |

## When to use it

- Use when user asks to check, audit, update, improve, or fix CLAUDE.md files.
- Also use when the user mentions "CLAUDE.md maintenance" or "project memory optimization".

## What it says up front

> Audit, evaluate, and improve CLAUDE.md files across a codebase to ensure Claude Code has optimal project context.

## How it is structured

The skill's own section headings, in order:

- Workflow
  - Phase 1: Discovery
  - Phase 2: Quality Assessment
  - Phase 3: Quality Report Output
  - Phase 4: Targeted Updates
  - Phase 5: Apply Updates
- Templates
- Common Issues to Flag
- User Tips to Share
- What Makes a Great CLAUDE.md

## What it bundles

- reference docs: `references/quality-criteria.md`, `references/templates.md`, `references/update-guidelines.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-plugins-official:claude-security](anthropics-claude-plugins-official-claude-security.md) - Claude Security: scan the codebase (the whole repository or a scoped part of it), scan changes (this branch's 
- [anthropics/claude-code:Plugin Settings](anthropics-claude-code-plugin-settings.md) - This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-conf
- [anthropics/claude-plugins-official:plugin-settings](anthropics-claude-plugins-official-plugin-settings.md) - This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-conf
- [engineering:tech-debt](engineering-tech-debt.md) - Identify, categorize, and prioritize technical debt. Trigger with "tech debt", "technical debt audit", "what s

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:claude-md-improver`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/claude-md-management/skills/claude-md-improver --commit 58267944f92187b7d6a1c822165c96c81c864806 --expect-tree 17bb2eacc2e8d636b056a8fff8ccc2d0ac22f7e118b95bad89b8f1ef5a8d2362 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
