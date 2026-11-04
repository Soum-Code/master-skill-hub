# healthcare-eval-harness

> Patient safety evaluation harness for healthcare application deployments. Automated test suites for CDSS accuracy, PHI exposure, clinical workflow integrity, and integration compliance. Blocks deployments on safety failures. Use when a healthcare deployment must be gated on patient-safety tests for CDSS accuracy, PHI exposure, and workflow integrity.

| | |
|---|---|
| **ID** | `affaan-m/ECC:healthcare-eval-harness` |
| **Pack** | AI / ML Engineering (also: MLOps / DevOps / Cloud) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 209 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when a healthcare deployment must be gated on patient-safety tests for CDSS accuracy, PHI exposure, and workflow integrity.

## What it says up front

> Automated verification system for healthcare application deployments. A single CRITICAL failure blocks deployment. Patient safety is non-negotiable.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
  - Eval Categories
  - Pass/Fail Matrix
  - CI/CD Integration
  - Anti-Patterns
- Examples
  - Example 1: Run All Critical Gates Locally
  - Example 2: Check HIGH Gate Pass Rate
  - Example 3: Eval Report

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:healthcare-emr-patterns](affaan-m-ecc-healthcare-emr-patterns.md) - EMR/EHR development patterns for healthcare applications. Clinical safety, encounter workflows, prescription g
- [affaan-m/ECC:healthcare-cdss-patterns](affaan-m-ecc-healthcare-cdss-patterns.md) - Clinical Decision Support System (CDSS) development patterns. Drug interaction checking, dose validation, clin
- [affaan-m/ECC:healthcare-phi-compliance](affaan-m-ecc-healthcare-phi-compliance.md) - Protected Health Information (PHI) and PII compliance patterns for healthcare applications: data classificatio

## Invoke / install

- Invoke: `/affaan-m/ECC:healthcare-eval-harness`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/healthcare-eval-harness --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 712cad75c79e531698fbc4ba9ab957242a7a190240d3ac03aa227c309f02c013 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
