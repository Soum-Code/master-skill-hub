# healthcare-emr-patterns

> EMR/EHR development patterns for healthcare applications. Clinical safety, encounter workflows, prescription generation, clinical decision support integration, and accessibility-first UI for medical data entry. Use when building EMR or EHR features such as encounter workflows, prescription generation, or clinical data entry UI.

| | |
|---|---|
| **ID** | `affaan-m/ECC:healthcare-emr-patterns` |
| **Pack** | Claude / Skills / Plugin Tooling (also: MLOps / DevOps / Cloud, Operations & Business, Web, Frontend & UI Design) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 161 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when building EMR or EHR features such as encounter workflows, prescription generation, or clinical data entry UI.

## What it says up front

> Patterns for building Electronic Medical Record (EMR) and Electronic Health Record (EHR) systems. Prioritizes patient safety, clinical accuracy, and practitioner efficiency.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
  - Patient Safety First
  - Single-Page Encounter Flow
  - Smart Template System
  - Medication Safety Pattern
  - Locked Encounter Pattern
  - UI Patterns for Clinical Data
  - Accessibility for Healthcare
  - Anti-Patterns
- Examples
  - Example 1: Patient Encounter Flow
  - Example 2: Medication Safety Workflow
  - Example 3: Locked Encounter + Addendum

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:healthcare-cdss-patterns](affaan-m-ecc-healthcare-cdss-patterns.md) - Clinical Decision Support System (CDSS) development patterns. Drug interaction checking, dose validation, clin
- [affaan-m/ECC:healthcare-eval-harness](affaan-m-ecc-healthcare-eval-harness.md) - Patient safety evaluation harness for healthcare application deployments. Automated test suites for CDSS accur
- [affaan-m/ECC:react-patterns](affaan-m-ecc-react-patterns.md) - React 18/19 patterns including hooks discipline, server/client component boundaries, Suspense + error boundari
- [affaan-m/ECC:frontend-patterns](affaan-m-ecc-frontend-patterns.md) - Frontend development patterns for React, Next.js, state management, performance optimization, and UI best prac

## Invoke / install

- Invoke: `/affaan-m/ECC:healthcare-emr-patterns`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/healthcare-emr-patterns --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 6224333daa41e26144939e416aca1f94dce442fa32ecd80f3e4fd0afd8aa5e88 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
