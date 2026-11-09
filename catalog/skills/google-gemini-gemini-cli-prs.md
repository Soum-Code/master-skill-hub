# prs

> Expertise in managing the Git and GitHub Pull Request lifecycle, including staging changes, generating PR descriptions, and branch management.

| | |
|---|---|
| **ID** | `google-gemini/gemini-cli:prs` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| **License** | Apache-2.0 |
| **Size** | 52 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Standardize how the Gemini CLI Bot stages its changes, generates Pull Request descriptions, and manages the lifecycle of both new and existing PRs.

## How it is structured

The skill's own section headings, in order:

- Goal
- Staging & Patch Preparation (MANDATORY)
- Unblocking & PR Updates (Recovery)

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [vercel-labs/skills:pr-labeling](vercel-labs-skills-pr-labeling.md) - Classify a skills CLI pull request from its description and patch, while respecting existing labels.
- [google-gemini/gemini-cli:pr-creator](google-gemini-gemini-cli-pr-creator.md) - Use this skill when asked to create a pull request (PR). It ensures all PRs follow the repository's establishe
- [google-gemini/gemini-cli:pr-address-comments](google-gemini-gemini-cli-pr-address-comments.md) - Use this skill if the user asks you to help them address GitHub PR comments for their current branch of the Ge
- [affaan-m/ECC:git-workflow](affaan-m-ecc-git-workflow.md) - Git workflow patterns including branching strategies, commit conventions, keeping history clean and readable, 

## Invoke / install

- Invoke: `/google-gemini/gemini-cli:prs`
- Install: `python skills/skill-vetter/scripts/install.py google-gemini/gemini-cli --path tools/gemini-cli-bot/.gemini/skills/prs --commit 62bab5b232c15b925d31e655ce844ab939c882b7 --expect-tree ededf5f2a73bfa1d90adc8b41112ee3442d158274458fa7bcc07a58766cbf342 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
