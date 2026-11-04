# security-bounty-hunter

> Hunt for exploitable, bounty-worthy security issues in repositories. Focuses on remotely reachable vulnerabilities that qualify for real reports instead of noisy local-only findings. Use when hunting reportable, remotely reachable vulnerabilities in a repository.

| | |
|---|---|
| **ID** | `affaan-m/ECC:security-bounty-hunter` |
| **Pack** | Security & Privacy |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 101 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when hunting reportable, remotely reachable vulnerabilities in a repository.

## What it says up front

> Use this when the goal is practical vulnerability discovery for responsible disclosure or bounty submission, not a broad best-practices review.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
- In-Scope Patterns
- Skip These
- Workflow
- Example Triage Loop
- Report Structure
- Quality Gate

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/affaan-m/ECC:security-bounty-hunter`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/security-bounty-hunter --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 8e31e3098061921a1b6bb0fbc6f843a1ad7e001ca33edb3c827b419ca4126cb3 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
