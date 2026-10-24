# yeet

> Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using the GitHub CLI (`gh`).

| | |
|---|---|
| **ID** | `openai/skills:yeet` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 133 lines in SKILL.md, 5 file(s) |

## When to use it

- Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using the GitHub CLI (`gh`).

## How it is structured

The skill's own section headings, in order:

- Prerequisites
- Naming conventions
- PR template discovery
- Workflow
- Determining the PR
- PR Title
  - Example
- PR Body Contents
  - Suggested PR Body Shape

## What it bundles

- 4 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:gh-address-comments](openai-skills-gh-address-comments.md) - Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth f
- [openai/skills:gh-fix-ci](openai-skills-gh-fix-ci.md) - Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect 
- [vercel-labs/skills:pr-labeling](vercel-labs-skills-pr-labeling.md) - Classify a skills CLI pull request from its description and patch, while respecting existing labels.
- [anthropics/claude-plugins-official:claude-security](anthropics-claude-plugins-official-claude-security.md) - Claude Security: scan the codebase (the whole repository or a scoped part of it), scan changes (this branch's 

## Invoke / install

- Invoke: `/openai/skills:yeet`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/yeet --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree c19923cf0817720091364aef0a067e75e6c5e618c0dee53f1327e9eb93882cdd --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
