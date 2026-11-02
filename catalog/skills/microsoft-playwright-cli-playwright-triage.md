# playwright-triage

> Triage and fix one microsoft/playwright-cli issue, or do a maintainer's task, unattended inside the Issue triage GitHub Actions workflow (.github/workflows/triage.yml), which a needs-triage, needs-triage-mac or needs-triage-win label starts, or a maintainer starts by hand with an issue, a task or both. Reproduces the issue on the runner, then leaves a verified fix proposal for the workflow to open as a draft PR, in this repo or in microsoft/playwright where the source of the CLI is, or an investigation note for it to post on the issue. Only for that workflow.

| | |
|---|---|
| **ID** | `microsoft/playwright-cli:playwright-triage` |
| **Pack** | Browser & Web Automation (also: MLOps / DevOps / Cloud) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) |
| **License** | Apache-2.0 |
| **Size** | 117 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> You run unattended in the [Issue triage](../../../.github/workflows/triage.yml) workflow of `microsoft/playwright-cli`. First read the shared guide, `$AGENT_GUIDES_DIR/triage.md`, a copy of [microsoft/playwright/.github/actions/run-agent/guides/triage.md](https://github.com/microsoft/playwright/blob

## How it is structured

The skill's own section headings, in order:

- Where the code is
- The checkouts
- Fix in microsoft/playwright
- Published versions
- PRs from third parties

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/playwright-cli:dev](microsoft-playwright-cli-dev.md) - Development workflows for the playwright-cli repository. Use when the user asks about rolling dependencies, re
- [openai/skills:yeet](openai-skills-yeet.md) - Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow usin
- [openai/skills:gh-address-comments](openai-skills-gh-address-comments.md) - Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth f

## Invoke / install

- Invoke: `/microsoft/playwright-cli:playwright-triage`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/playwright-cli --path .claude/skills/playwright-triage --commit c2d8d199459d1480491bebf0a6b3587136b673fa --expect-tree b09987e81527dbecd4450f8a3274ee863f0375f962093a33de42c85b61817ac7 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
