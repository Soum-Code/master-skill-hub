# healthcare-phi-compliance

> Protected Health Information (PHI) and PII compliance patterns for healthcare applications: data classification, row-level access control, tamper-proof audit trails, schema tagging, and common leak vectors such as logs, URLs, and browser storage. Use when code touches patient or clinician data, when implementing HIPAA or GDPR access controls, or when auditing a healthcare system for data exposure.

| | |
|---|---|
| **ID** | `affaan-m/ECC:healthcare-phi-compliance` |
| **Pack** | Legal & Compliance |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 147 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when code touches patient or clinician data, when implementing HIPAA or GDPR access controls, or when auditing a healthcare system for data exposure.

## What it says up front

> Patterns for protecting patient data, clinician data, and financial data in healthcare applications. Applicable to HIPAA (US), DISHA (India), GDPR (EU), and general healthcare data protection.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
  - Data Classification
  - Access Control: Row-Level Security
  - Audit Trail
  - Common Leak Vectors
  - Database Schema Tagging
  - Deployment Checklist
- Examples
  - Example 1: Safe vs Unsafe Error Handling
  - Example 2: RLS Policy for Multi-Facility Isolation
  - Example 3: Safe Logging

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:healthcare-eval-harness](affaan-m-ecc-healthcare-eval-harness.md) - Patient safety evaluation harness for healthcare application deployments. Automated test suites for CDSS accur

## Invoke / install

- Invoke: `/affaan-m/ECC:healthcare-phi-compliance`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/healthcare-phi-compliance --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree fe02cec9bccda9a16bd6c587e20ae74d110eaf16ec04377e74337e1bf1a2d256 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
