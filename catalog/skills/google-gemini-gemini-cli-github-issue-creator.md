# github-issue-creator

> Use this skill when asked to create a GitHub issue. It handles different issue types (bug, feature, etc.) using repository templates and ensures proper labeling.

| | |
|---|---|
| **ID** | `google-gemini/gemini-cli:github-issue-creator` |
| **Pack** | Claude / Skills / Plugin Tooling (also: MLOps / DevOps / Cloud) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| **License** | Apache-2.0 |
| **Size** | 77 lines in SKILL.md, 1 file(s) |

## When to use it

- Use this skill when asked to create a GitHub issue.

## What it says up front

> This skill guides the creation of high-quality GitHub issues that adhere to the repository's standards and use the appropriate templates.

## How it is structured

The skill's own section headings, in order:

- Workflow
- Principles

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [google-gemini/gemini-cli:pr-creator](google-gemini-gemini-cli-pr-creator.md) - Use this skill when asked to create a pull request (PR). It ensures all PRs follow the repository's establishe
- [bm:inbox](bm-inbox.md) - Triage and review all open GitHub issues and PRs against project templates and contribution guidelines
- [google-gemini/gemini-cli:critique](google-gemini-gemini-cli-critique.md) - Expertise in auditing and fixing repository scripts and GitHub Actions workflows to ensure technical robustnes
- [affaan-m/ECC:skill-scout](affaan-m-ecc-skill-scout.md) - Search existing local, marketplace, GitHub, and web skill sources before creating a new skill. Use when the us

## Invoke / install

- Invoke: `/google-gemini/gemini-cli:github-issue-creator`
- Install: `python skills/skill-vetter/scripts/install.py google-gemini/gemini-cli --path .gemini/skills/github-issue-creator --commit 62bab5b232c15b925d31e655ce844ab939c882b7 --expect-tree 49c83cec4ef8b96bd4ab4921012ab59f3055d4f9637ae7b63be2f573bdc30cd3 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
