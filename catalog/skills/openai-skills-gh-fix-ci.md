# gh-fix-ci

> Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect checks and logs, summarize failure context, draft a fix plan, and implement only after explicit approval. Treat external providers (for example Buildkite) as out of scope and report only the details URL.

| | |
|---|---|
| **ID** | `openai/skills:gh-fix-ci` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 70 lines in SKILL.md, 6 file(s) |

## When to use it

- Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect checks and logs, summarize failure context, draft a fix plan, and implement only after explicit approval.

## How it is structured

The skill's own section headings, in order:

- Overview
- Inputs
- Quick start
- Workflow
- Bundled Resources
  - scripts/inspect_pr_checks.py

## What it bundles

- scripts: `scripts/inspect_pr_checks.py`
- 4 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [openai/skills:yeet](openai-skills-yeet.md) - Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow usin
- [affaan-m/ECC:issue-review](affaan-m-ecc-issue-review.md) - Review a GitHub issue the way /code-review reviews a PR. Fetches the issue with the gh CLI, checks the report 
- [affaan-m/ECC:terminal-ops](affaan-m-ecc-terminal-ops.md) - Evidence-first repo execution workflow for ECC. Use when the user wants a command run, a repo checked, a CI fa
- [google-gemini/gemini-cli:pr-address-comments](google-gemini-gemini-cli-pr-address-comments.md) - Use this skill if the user asks you to help them address GitHub PR comments for their current branch of the Ge

## Invoke / install

- Invoke: `/openai/skills:gh-fix-ci`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/gh-fix-ci --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree e747b1b41702f50d168ef6ec6e61a3fbc92911b50a1e3a83bb692b246795b261 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
