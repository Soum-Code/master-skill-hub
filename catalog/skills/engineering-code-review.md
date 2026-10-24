# code-review

> Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this before I merge", "is this code safe?", or when checking a change for N+1 queries, injection risks, missing edge cases, or error handling gaps.

| | |
|---|---|
| **ID** | `engineering:code-review` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `engineering` v1.2.0 - [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | not declared |
| **Size** | 119 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## How it is structured

The skill's own section headings, in order:

- Usage
- How It Works
- Review Dimensions
  - Security
  - Performance
  - Correctness
  - Maintainability
- Output
- If Connectors Available
- Tips

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [code-review](code-review.md) - Review the current diff or a PR number, branch or path for correctness bugs at a chosen effort level; optional
- [security-review](security-review.md) - Security review of the pending changes on the current branch.
- [bm:code-review](bm-code-review.md) - Review source files changed during a phase for bugs, security issues, and code quality problems
- [bm:ship](bm-ship.md) - Create PR, run review, and prepare for merge after verification passes

## Invoke / install

- Invoke: `/engineering:code-review`  (Skill tool: `engineering:code-review`)
- Install: `bundled with Claude desktop (Cowork plugin 'engineering'); source: github.com/anthropics/knowledge-work-plugins`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
