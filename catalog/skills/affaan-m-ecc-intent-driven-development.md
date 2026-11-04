# intent-driven-development

> Turn ambiguous or high-impact product and engineering changes into scoped, verifiable acceptance criteria before or alongside implementation. Use when a user asks to clarify a feature, define acceptance criteria, de-risk a security/data/migration/integration change, prepare implementation requirements for another agent, or make a complex request testable. Do not trigger for trivial edits, straightforward fixes, active debugging, code review, or implementation requests whose acceptance conditions are already clear unless the user explicitly invokes this skill.

| | |
|---|---|
| **ID** | `affaan-m/ECC:intent-driven-development` |
| **Pack** | Software Development (also: Operations & Business, Product Management) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 361 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when a user asks to clarify a feature, define acceptance criteria, de-risk a security/data/migration/integration change, prepare implementation requirements for another agent, or make a complex request testable.
- Do not trigger for trivial edits, straightforward fixes, active debugging, code review, or implementation requests whose acceptance conditions are already clear unless the user explici.

## What it says up front

> Produce useful acceptance criteria without turning specification into ceremony. Inspect available context first, expose genuine ambiguity, and choose verification methods that fit the work and its risk.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- How It Works
- Examples
- Operating Rules
- Choose The Depth
  - Quick Capture
  - Full Acceptance Brief
  - Existing Specification Review
- Workflow
  - 1. Establish Goal And Risk
  - 2. Discover Context
  - 3. Define Scope
  - 4. Write Acceptance Criteria
  - 5. Cover Only Relevant Boundaries
  - 6. Present And Continue
- Output Template
- Pass/Fail Examples
  - Pass/Fail Rubric
- Quality Check
- Handoff

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:security-best-practices](openai-skills-security-best-practices.md) - Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only 
- [anthropics/claude-plugins-official:claude-security](anthropics-claude-plugins-official-claude-security.md) - Claude Security: scan the codebase (the whole repository or a scoped part of it), scan changes (this branch's 
- [engineering:code-review](engineering-code-review.md) - Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this be
- [product-management:write-spec](product-management-write-spec.md) - Write a feature spec or PRD from a problem statement or feature idea. Use when turning a vague idea or user re

## Invoke / install

- Invoke: `/affaan-m/ECC:intent-driven-development`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/intent-driven-development --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 2752349ca7fd83909fa21a0c135d18076034a456958a29f4b2c2eb6af9616163 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
