# code-reviewer

> Use this skill to review code. It supports both local changes (staged or working tree) and remote Pull Requests (by ID or URL). It focuses on correctness, maintainability, and adherence to project standards.

| | |
|---|---|
| **ID** | `google-gemini/gemini-cli:code-reviewer` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| **License** | Apache-2.0 |
| **Size** | 66 lines in SKILL.md, 1 file(s) |

## When to use it

- Use this skill to review code.

## What it says up front

> This skill guides the agent in conducting professional and thorough code reviews for both local development and remote Pull Requests.

## How it is structured

The skill's own section headings, in order:

- Workflow
  - 1. Determine Review Target
  - 2. Preparation
  - 3. In-Depth Analysis
  - 4. Provide Feedback
  - 5. Cleanup (Remote PRs only)

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:coding-standards](affaan-m-ecc-coding-standards.md) - Baseline cross-project coding conventions for naming, readability, immutability, and code-quality review. Use 
- [engineering:code-review](engineering-code-review.md) - Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this be
- [google-gemini/gemini-cli:pr-creator](google-gemini-gemini-cli-pr-creator.md) - Use this skill when asked to create a pull request (PR). It ensures all PRs follow the repository's establishe
- [google-gemini/gemini-cli:review-duplication](google-gemini-gemini-cli-review-duplication.md) - Use this skill during code reviews to proactively investigate the codebase for duplicated functionality, reinv

## Invoke / install

- Invoke: `/google-gemini/gemini-cli:code-reviewer`
- Install: `python skills/skill-vetter/scripts/install.py google-gemini/gemini-cli --path .gemini/skills/code-reviewer --commit b9776560ea5710bc673891499aaec68c737d160a --expect-tree 994cf34027b7fd45b2c231e4132ab6e44fda251877fe261f19125037f8588a0d --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
