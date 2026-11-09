# pr-address-comments

> Use this skill if the user asks you to help them address GitHub PR comments for their current branch of the Gemini CLI. Requires `gh` CLI tool.

| | |
|---|---|
| **ID** | `google-gemini/gemini-cli:pr-address-comments` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| **License** | Apache-2.0 |
| **Size** | 14 lines in SKILL.md, 2 file(s) |

## When to use it

- Use this skill if the user asks you to help them address GitHub PR comments for their current branch of the Gemini CLI.

## What it says up front

> You are helping the user address comments on their Pull Request. These comments may have come from an automated review agent or a team member.

## What it bundles

- scripts: `scripts/fetch-pr-info.js`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [openai/skills:gh-address-comments](openai-skills-gh-address-comments.md) - Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth f
- [openai/skills:yeet](openai-skills-yeet.md) - Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow usin
- [affaan-m/ECC:issue-review](affaan-m-ecc-issue-review.md) - Review a GitHub issue the way /code-review reviews a PR. Fetches the issue with the gh CLI, checks the report 
- [google-gemini/gemini-cli:skill-creator](google-gemini-gemini-cli-skill-creator.md) - Guide for creating effective skills. This skill should be used when users want to create a new skill (or updat

## Invoke / install

- Invoke: `/google-gemini/gemini-cli:pr-address-comments`
- Install: `python skills/skill-vetter/scripts/install.py google-gemini/gemini-cli --path .gemini/skills/pr-address-comments --commit 62bab5b232c15b925d31e655ce844ab939c882b7 --expect-tree fa4f4a4a89c936ae88628d2183690008ebeb5f072c2ad3a18e3075ffc4e2c1c0 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
