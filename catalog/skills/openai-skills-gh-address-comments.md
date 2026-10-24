# gh-address-comments

> Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth first and prompt the user to authenticate if not logged in.

| | |
|---|---|
| **ID** | `openai/skills:gh-address-comments` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 26 lines in SKILL.md, 6 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## How it is structured

The skill's own section headings, in order:

- 1) Inspect comments needing attention
- 2) Ask the user for clarification
- 3) If user chooses comments

## What it bundles

- scripts: `scripts/fetch_comments.py`
- 4 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [openai/skills:yeet](openai-skills-yeet.md) - Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow usin
- [code-review](code-review.md) - Review the current diff or a PR number, branch or path for correctness bugs at a chosen effort level; optional
- [bm:inbox](bm-inbox.md) - Triage and review all open GitHub issues and PRs against project templates and contribution guidelines
- [security-review](security-review.md) - Security review of the pending changes on the current branch.

## Invoke / install

- Invoke: `/openai/skills:gh-address-comments`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/gh-address-comments --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree c78892b8a66471e3ae174b92b30345d967ceba0f0c912604526591e039d047bb --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
