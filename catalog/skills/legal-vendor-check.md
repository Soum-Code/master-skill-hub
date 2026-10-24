# vendor-check

> Check the status of existing agreements with a vendor across all connected systems — CLM, CRM, email, and document storage — with gap analysis and upcoming deadlines. Use when onboarding or renewing a vendor, when you need a consolidated view of what's signed and what's missing (MSA, DPA, SOW), or when checking for approaching expirations and surviving obligations.

| | |
|---|---|
| **ID** | `legal:vendor-check` |
| **Pack** | Legal & Compliance (also: Operations & Business) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `legal` v1.3.0 - [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 160 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when onboarding or renewing a vendor, when you need a consolidated view of what's signed and what's missing (MSA, DPA, SOW), or when checking for approaching expirations and surviving obligations.

## What it says up front

> Check the status of existing agreements with a vendor across all connected systems. Provides a consolidated view of the legal relationship.

## How it is structured

The skill's own section headings, in order:

- Invocation
- Workflow
  - Step 1: Identify the Vendor
  - Step 2: Search Connected Systems
  - Step 3: Compile Agreement Status
  - Step 4: Gap Analysis
  - Step 5: Generate Report
  - Step 6: Handle Missing Sources
- Notes

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/knowledge-work-plugins:design-system](anthropics-knowledge-work-plugins-design-system.md) - Audit, document, or extend your design system. Use when checking for naming inconsistencies or hardcoded value

## Invoke / install

- Invoke: `/legal:vendor-check`  (Skill tool: `legal:vendor-check`)
- Install: `bundled with Claude desktop (Cowork plugin 'legal'); source: github.com/anthropics/knowledge-work-plugins`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
