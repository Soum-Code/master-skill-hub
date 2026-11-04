# conventional-commit-review

> Reviews staged changes and drafts a Conventional Commits-compliant commit message with the right type, scope, and length. Use before committing, or when the user asks to write, fix, or review a commit message.

| | |
|---|---|
| **ID** | `affaan-m/ECC:conventional-commit-review` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 107 lines in SKILL.md, 1 file(s) |

## When to use it

- Use before committing, or when the user asks to write, fix, or review a commit message.

## What it says up front

> Turns a staged diff into a commit message that follows the Conventional Commits format (`type(scope): subject`) and matches the repository's actual history norms instead of a generic template.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Core Concepts
- Workflow
- Code Examples
- Anti-Patterns
- Best Practices
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:issue-review](affaan-m-ecc-issue-review.md) - Review a GitHub issue the way /code-review reviews a PR. Fetches the issue with the gh CLI, checks the report 
- [bm:code-review-fix](bm-code-review-fix.md) - Auto-fix issues found by code review in REVIEW.md. Spawns fixer agent, commits each fix atomically, produces R
- [openai/skills:gh-fix-ci](openai-skills-gh-fix-ci.md) - Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect 
- [anthropics/claude-plugins-official:claude-security](anthropics-claude-plugins-official-claude-security.md) - Claude Security: scan the codebase (the whole repository or a scoped part of it), scan changes (this branch's 

## Invoke / install

- Invoke: `/affaan-m/ECC:conventional-commit-review`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/conventional-commit-review --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 557a4dff2b1168271386923b8423da7d1a98198003a14e02e5602dab84754d32 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
