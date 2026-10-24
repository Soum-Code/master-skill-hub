# github-issue-creator

> Convert raw notes, error logs, voice dictation, or screenshots into crisp GitHub-flavored markdown issue reports. Use when the user pastes bug info, error messages, or informal descriptions and wants a structured GitHub issue. Supports images/GIFs for visual evidence.

| | |
|---|---|
| **ID** | `microsoft/skills:github-issue-creator` |
| **Pack** | MLOps / DevOps / Cloud (also: Claude / Skills / Plugin Tooling) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 137 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user pastes bug info, error messages, or informal descriptions and wants a structured GitHub issue.

## What it says up front

> Transform messy input (error logs, voice notes, screenshots) into clean, actionable GitHub issues.

## How it is structured

The skill's own section headings, in order:

- Output Template
- Output Location
- Guidelines
- Examples

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:gh-address-comments](openai-skills-gh-address-comments.md) - Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth f
- [product-management:synthesize-research](product-management-synthesize-research.md) - Synthesize user research from interviews, surveys, and feedback into structured insights. Use when you have a 

## Invoke / install

- Invoke: `/microsoft/skills:github-issue-creator`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/skills/github-issue-creator --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 8fbc55b5e2c919d4c13d8ca6376af774d6ac0fc18a275cc6d5027887f8c8b57f --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
