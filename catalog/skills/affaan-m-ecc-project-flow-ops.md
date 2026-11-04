# project-flow-ops

> Operate execution flow across GitHub and Linear by triaging issues and pull requests, linking active work, and keeping GitHub public-facing while Linear remains the internal execution layer. Use when the user wants backlog control, PR triage, or GitHub-to-Linear coordination.

| | |
|---|---|
| **ID** | `affaan-m/ECC:project-flow-ops` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 113 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user wants backlog control, PR triage, or GitHub-to-Linear coordination.

## What it says up front

> This skill turns disconnected GitHub issues, PRs, and Linear tasks into one execution flow.

## How it is structured

The skill's own section headings, in order:

- When to Use
- Operating Model
- Core Workflow
  - 1. Read the public surface first
  - 2. Classify the work
  - 3. Decide whether Linear is warranted
  - 4. Keep the two systems consistent
- Review Rules
- Output Format
- Good Use Cases

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:linear](openai-skills-linear.md) - Manage issues, projects & team workflows in Linear. Use when the user wants to read, create or updates tickets
- [openai/skills:yeet](openai-skills-yeet.md) - Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow usin
- [vercel-labs/skills:pr-labeling](vercel-labs-skills-pr-labeling.md) - Classify a skills CLI pull request from its description and patch, while respecting existing labels.
- [bm:inbox](bm-inbox.md) - Triage and review all open GitHub issues and PRs against project templates and contribution guidelines

## Invoke / install

- Invoke: `/affaan-m/ECC:project-flow-ops`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/project-flow-ops --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 903469b76b389ec45733179c2bdd286c1b49d452bf45ff50e735b048facd120a --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
