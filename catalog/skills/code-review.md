# code-review

> Review the current diff or a PR number, branch or path for correctness bugs at a chosen effort level; optionally post inline PR comments or apply fixes.

| | |
|---|---|
| **ID** | `code-review` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | builtin |
| **License** | not declared |
| **Size** | 5 lines in SKILL.md, 0 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [simplify](simplify.md) - Review changed code for reuse, simplification, efficiency and altitude cleanups, then apply the fixes. Quality
- [affaan-m/ECC:issue-review](affaan-m-ecc-issue-review.md) - Review a GitHub issue the way /code-review reviews a PR. Fetches the issue with the gh CLI, checks the report 
- [bm:pr-branch](bm-pr-branch.md) - Create a clean PR branch by filtering out .planning/ commits — ready for code review
- [openai/skills:gh-address-comments](openai-skills-gh-address-comments.md) - Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth f

## Invoke / install

- Invoke: `/code-review`
- Install: `built into Claude Code`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
