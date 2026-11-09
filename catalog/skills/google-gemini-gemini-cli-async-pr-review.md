# async-pr-review

> Trigger this skill when the user wants to start an asynchronous PR review, run background checks on a PR, or check the status of a previously started async PR review.

| | |
|---|---|
| **ID** | `google-gemini/gemini-cli:async-pr-review` |
| **Pack** | Software Development (also: MLOps / DevOps / Cloud) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| **License** | Apache-2.0 |
| **Size** | 45 lines in SKILL.md, 4 file(s) |

## When to use it

- Trigger this skill when the user wants to start an asynchronous PR review, run background checks on a PR, or check the status of a previously started async PR review.

## What it says up front

> This skill provides a set of tools to asynchronously review a Pull Request. It will create a background job to run the project's preflight checks, execute Gemini-powered test plans, and perform a comprehensive code review using custom prompts.

## How it is structured

The skill's own section headings, in order:

- Workflow
  - Start Review
  - Check Status

## What it bundles

- scripts: `scripts/async-review.sh`, `scripts/check-async-review.sh`
- 1 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [anthropics/claude-plugins-official:configure](anthropics-claude-plugins-official-configure.md) - Set up the Discord channel — save the bot token and review access policy. Use when the user pastes a Discord b
- [engineering:code-review](engineering-code-review.md) - Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this be
- [google-gemini/gemini-cli:pr-address-comments](google-gemini-gemini-cli-pr-address-comments.md) - Use this skill if the user asks you to help them address GitHub PR comments for their current branch of the Ge
- [google-gemini/gemini-cli:string-reviewer](google-gemini-gemini-cli-string-reviewer.md) - Use this skill when asked to review text and user-facing strings within the codebase. It ensures that these st

## Invoke / install

- Invoke: `/google-gemini/gemini-cli:async-pr-review`
- Install: `python skills/skill-vetter/scripts/install.py google-gemini/gemini-cli --path .gemini/skills/async-pr-review --commit 62bab5b232c15b925d31e655ce844ab939c882b7 --expect-tree 60bcdd7eb2eaf1dcfa676fb592e36534e8e825b08b39a2e9e55ad571677ffd73 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
