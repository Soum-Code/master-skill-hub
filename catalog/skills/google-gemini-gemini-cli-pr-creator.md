# pr-creator

> Use this skill when asked to create a pull request (PR). It ensures all PRs follow the repository's established templates and standards.

| | |
|---|---|
| **ID** | `google-gemini/gemini-cli:pr-creator` |
| **Pack** | Claude / Skills / Plugin Tooling (also: MLOps / DevOps / Cloud) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| **License** | Apache-2.0 |
| **Size** | 94 lines in SKILL.md, 1 file(s) |

## When to use it

- Use this skill when asked to create a pull request (PR).

## What it says up front

> This skill guides the creation of high-quality Pull Requests that adhere to the repository's standards.

## How it is structured

The skill's own section headings, in order:

- Workflow
- Principles

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [google-gemini/gemini-cli:github-issue-creator](google-gemini-gemini-cli-github-issue-creator.md) - Use this skill when asked to create a GitHub issue. It handles different issue types (bug, feature, etc.) usin
- [vercel-labs/skills:pr-labeling](vercel-labs-skills-pr-labeling.md) - Classify a skills CLI pull request from its description and patch, while respecting existing labels.
- [google-gemini/gemini-cli:prs](google-gemini-gemini-cli-prs.md) - Expertise in managing the Git and GitHub Pull Request lifecycle, including staging changes, generating PR desc
- [google-gemini/gemini-cli:string-reviewer](google-gemini-gemini-cli-string-reviewer.md) - Use this skill when asked to review text and user-facing strings within the codebase. It ensures that these st

## Invoke / install

- Invoke: `/google-gemini/gemini-cli:pr-creator`
- Install: `python skills/skill-vetter/scripts/install.py google-gemini/gemini-cli --path .gemini/skills/pr-creator --commit 62bab5b232c15b925d31e655ce844ab939c882b7 --expect-tree 8127a16bc3f8e2b1b68d9f8efaea6141888ff156552705ecefb06887864e79db --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
