# string-reviewer

> Use this skill when asked to review text and user-facing strings within the codebase. It ensures that these strings follow rules on clarity, usefulness, brevity and style.

| | |
|---|---|
| **ID** | `google-gemini/gemini-cli:string-reviewer` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| **License** | Apache-2.0 |
| **Size** | 99 lines in SKILL.md, 3 file(s) |

## When to use it

- Use this skill when asked to review text and user-facing strings within the codebase.

## What it says up front

> Act as a Senior UX Writer. Look for user-facing strings that are too long, unclear, or inconsistent. This includes inline text, error messages, and other user-facing text.

## How it is structured

The skill's own section headings, in order:

- Instructions
- Core voice principles
- The writing checklist
  - Identity and voice
  - Structural scannability
  - Technical accuracy and humility
  - Agentic error recovery
  - Use consistent terminology
- Ensure consistent style for settings
- Output format

## What it bundles

- reference docs: `references/settings.md`, `references/word-list.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [google-gemini/gemini-cli:pr-creator](google-gemini-gemini-cli-pr-creator.md) - Use this skill when asked to create a pull request (PR). It ensures all PRs follow the repository's establishe
- [google-gemini/gemini-cli:async-pr-review](google-gemini-gemini-cli-async-pr-review.md) - Trigger this skill when the user wants to start an asynchronous PR review, run background checks on a PR, or c
- [vercel-labs/agent-skills:writing-guidelines](vercel-labs-agent-skills-writing-guidelines.md) - Review docs/prose for Writing Guidelines compliance. Use when asked to "review my docs", "check writing style"

## Invoke / install

- Invoke: `/google-gemini/gemini-cli:string-reviewer`
- Install: `python skills/skill-vetter/scripts/install.py google-gemini/gemini-cli --path .gemini/skills/string-reviewer --commit b9776560ea5710bc673891499aaec68c737d160a --expect-tree 26cc912ee4ee9a5974e777b5a2172242f8a4e2c13eb93910eedc7ec611dd02f3 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
