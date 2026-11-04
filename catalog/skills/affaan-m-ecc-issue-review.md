# issue-review

> Review a GitHub issue the way /code-review reviews a PR. Fetches the issue with the gh CLI, checks the report against the current codebase, searches for duplicates and prior fixes, scores completeness, assigns severity, and writes a triage report plus a draft reply. Posting comments or labels is opt-in only. Use when the user asks to check, triage, validate, or review a GitHub issue.

| | |
|---|---|
| **ID** | `affaan-m/ECC:issue-review` |
| **Pack** | Software Development (also: Documents, Writing & Content) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 314 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user asks to check, triage, validate, or review a GitHub issue.

## What it says up front

> Structured triage of a single GitHub issue: is it valid, is it a duplicate, is it already fixed, what is missing, how severe is it, and what should the maintainer reply. The counterpart of the PR mode in `/code-review`.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Untrusted Content Rule
- How It Works
  - Phase 1: FETCH
  - Phase 2: CONTEXT
  - Phase 3: CLASSIFY
  - Phase 4: VERIFY
  - Phase 5: DUPLICATES
  - Phase 6: ASSESS
  - Phase 7: REPORT
  - Phase 8: PUBLISH (opt-in only)
  - Phase 9: OUTPUT
- Examples
- Edge Cases
- Anti-Patterns
- Related

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:gh-address-comments](openai-skills-gh-address-comments.md) - Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth f
- [code-review](code-review.md) - Review the current diff or a PR number, branch or path for correctness bugs at a chosen effort level; optional
- [openai/skills:gh-fix-ci](openai-skills-gh-fix-ci.md) - Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect 
- [microsoft/playwright-cli:playwright-triage](microsoft-playwright-cli-playwright-triage.md) - Triage and fix one microsoft/playwright-cli issue, or do a maintainer's task, unattended inside the Issue tria

## Invoke / install

- Invoke: `/affaan-m/ECC:issue-review`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/issue-review --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree c127057f4645a8a2dc52fda181e18551426229465616712e5091a847ffb59015 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
