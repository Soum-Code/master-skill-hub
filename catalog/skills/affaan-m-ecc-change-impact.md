# change-impact

> Perform evidence-backed impact analysis before changing code, data, interfaces, or governance documents, then compare the planned impact with the actual diff after implementation. Covers call paths, data and schema, API contracts, tests, documentation, ADRs, deployment, migration, and rollback. Use for cross-module or high-risk changes, database migrations, authentication, public interfaces, blast-radius questions, pre-change checks, and post-implementation alignment.

| | |
|---|---|
| **ID** | `affaan-m/ECC:change-impact` |
| **Pack** | Operations & Business (also: Software Development, Data & Analytics) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 87 lines in SKILL.md, 1 file(s) |

## When to use it

- Use for cross-module or high-risk changes, database migrations, authentication, public interfaces, blast-radius questions, pre-change checks, and post-implementation alignment.

## What it says up front

> Read-only by default. Prove the impact surface from real dependencies and existing documentation before implementation. Mark unknowns explicitly as `unverified`.

## How it is structured

The skill's own section headings, in order:

- Trust Boundary
- When to Activate
- When to Use
- How It Works
- Examples
- Anti-Patterns
- Related Skills
- Before the Change
- Routing Rules
- Output
- Post-Implementation Alignment

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [operations:change-request](operations-change-request.md) - Create a change management request with impact analysis and rollback plan. Use when proposing a system or proc
- [affaan-m/ECC:production-audit](affaan-m-ecc-production-audit.md) - Local-evidence production readiness audit for shipped apps, pre-launch reviews, post-merge checks, and "what b
- [engineering:deploy-checklist](engineering-deploy-checklist.md) - Pre-deployment verification checklist. Use when about to ship a release, deploying a change with database migr
- [affaan-m/ECC:module-regression](affaan-m-ecc-module-regression.md) - Govern cross-module regression in large repositories with a REGRESSION.md ledger that records each module's do

## Invoke / install

- Invoke: `/affaan-m/ECC:change-impact`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/change-impact --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree a2aeb208464e6697183f01b09d902c5079a94357354c663038280bba501d796d --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
