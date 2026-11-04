# healthcare-cdss-patterns

> Clinical Decision Support System (CDSS) development patterns. Drug interaction checking, dose validation, clinical scoring (NEWS2, qSOFA), alert severity classification, and integration into EMR workflows. Use when building clinical decision support — drug interaction checks, dose validation, clinical scoring, or alert severity.

| | |
|---|---|
| **ID** | `affaan-m/ECC:healthcare-cdss-patterns` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 247 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when building clinical decision support — drug interaction checks, dose validation, clinical scoring, or alert severity.

## What it says up front

> Patterns for building Clinical Decision Support Systems that integrate into EMR workflows. CDSS modules are patient safety critical — zero tolerance for false negatives.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
  - Drug Interaction Checking
  - Dose Validation
  - Clinical Scoring: NEWS2
  - Alert Severity and UI Behavior
  - Testing CDSS (Zero Tolerance for False Negatives)
  - Anti-Patterns
- Examples
  - Example 1: Drug Interaction Check
  - Example 2: Dose Validation
  - Example 3: NEWS2 Scoring

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:healthcare-emr-patterns](affaan-m-ecc-healthcare-emr-patterns.md) - EMR/EHR development patterns for healthcare applications. Clinical safety, encounter workflows, prescription g
- [affaan-m/ECC:healthcare-eval-harness](affaan-m-ecc-healthcare-eval-harness.md) - Patient safety evaluation harness for healthcare application deployments. Automated test suites for CDSS accur

## Invoke / install

- Invoke: `/affaan-m/ECC:healthcare-cdss-patterns`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/healthcare-cdss-patterns --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 840cfbf88b4a09565c6f0bf2d649476f43971a2a9ee16ffd8737a10d7124e59c --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
