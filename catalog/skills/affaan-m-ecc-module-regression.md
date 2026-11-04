# module-regression

> Govern cross-module regression in large repositories with a REGRESSION.md ledger that records each module's downstream consumers and executable acceptance command. After a change, run the changed module and every affected downstream command, and use observed exit codes as regression evidence under the project's delivery policy. Use for module regression, regression ledgers, impact audits, downstream verification, and changes where modifying A may break B.

| | |
|---|---|
| **ID** | `affaan-m/ECC:module-regression` |
| **Pack** | Spec-driven Dev Workflow (also: Finance & Accounting) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 100 lines in SKILL.md, 2 file(s) |

## When to use it

- Use for module regression, regression ledgers, impact audits, downstream verification, and changes where modifying A may break B.

## What it says up front

> In large projects, modules depend on one another. People and agents often verify only the changed module while downstream consumers fail silently. The defect appears days later when an aggregate, export, or external behavior is wrong.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Anti-Patterns
- Related Skills
- Problem
- Three Required Fields per Module
- Connection to TESTS.md
- Ledger Discipline
- Audit Flow
- Four Invariants
- Boundary with Adjacent Methods
- Progressive Adoption

## What it bundles

- 1 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:test-collaboration](affaan-m-ecc-test-collaboration.md) - Inventory and govern a project's test assets. Connect requirements, business rules, risks, bugs, and cross-bou
- [affaan-m/ECC:change-impact](affaan-m-ecc-change-impact.md) - Perform evidence-backed impact analysis before changing code, data, interfaces, or governance documents, then 

## Invoke / install

- Invoke: `/affaan-m/ECC:module-regression`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/module-regression --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree c0dab9ac59cc123679d67795042e1779f308916d273e14f6e046e2f81cc0bf1a --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
