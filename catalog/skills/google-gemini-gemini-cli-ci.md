# ci

> A specialized skill for Gemini CLI that provides high-performance, fail-fast monitoring of GitHub Actions workflows and automated local verification of CI failures. It handles run discovery automatically—simply provide the branch name.

| | |
|---|---|
| **ID** | `google-gemini/gemini-cli:ci` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| **License** | Apache-2.0 |
| **Size** | 67 lines in SKILL.md, 2 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> This skill enables the agent to efficiently monitor GitHub Actions, triage failures, and bridge remote CI errors to local development. It defaults to **automatic replication** of failures to streamline the fix cycle.

## How it is structured

The skill's own section headings, in order:

- Core Capabilities
- Workflow
  - 1. CI Replicate (`replicate`) - DEFAULT
  - 1. CI Status (`status`)
- Failure Categories & Actions
- Noise Filtering

## What it bundles

- scripts: `scripts/ci.mjs`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [google-gemini/gemini-cli:pr-address-comments](google-gemini-gemini-cli-pr-address-comments.md) - Use this skill if the user asks you to help them address GitHub PR comments for their current branch of the Ge
- [google-gemini/gemini-cli:skill-creator](google-gemini-gemini-cli-skill-creator.md) - Guide for creating effective skills. This skill should be used when users want to create a new skill (or updat
- [openai/skills:gh-fix-ci](openai-skills-gh-fix-ci.md) - Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect 
- [affaan-m/ECC:skill-scout](affaan-m-ecc-skill-scout.md) - Search existing local, marketplace, GitHub, and web skill sources before creating a new skill. Use when the us

## Invoke / install

- Invoke: `/google-gemini/gemini-cli:ci`
- Install: `python skills/skill-vetter/scripts/install.py google-gemini/gemini-cli --path .gemini/skills/ci --commit 62bab5b232c15b925d31e655ce844ab939c882b7 --expect-tree 3db57df8dff61cceab6c5ad10dc151d8cae66e95af8eab16d65c7860a7a7c799 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
