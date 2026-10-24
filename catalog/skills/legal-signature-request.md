# signature-request

> Prepare and route a document for e-signature — run a pre-signature checklist, configure signing order, and send for execution. Use when a contract is finalized and ready to sign, when verifying entity names, exhibits, and signature blocks before sending, or when setting up an envelope with sequential or parallel signers.

| | |
|---|---|
| **ID** | `legal:signature-request` |
| **Pack** | Legal & Compliance (also: Operations & Business) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `legal` v1.3.0 - [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 105 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when a contract is finalized and ready to sign, when verifying entity names, exhibits, and signature blocks before sending, or when setting up an envelope with sequential or parallel signers.

## What it says up front

> Prepare a document for electronic signature — verify completeness, set signing order, and route for execution.

## How it is structured

The skill's own section headings, in order:

- Usage
- Workflow
  - Step 1: Accept the Document
  - Step 2: Pre-Signature Checklist
  - Step 3: Configure Signing
  - Step 4: Route for Signature
- Output
- Tips

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [engineering:deploy-checklist](engineering-deploy-checklist.md) - Pre-deployment verification checklist. Use when about to ship a release, deploying a change with database migr

## Invoke / install

- Invoke: `/legal:signature-request`  (Skill tool: `legal:signature-request`)
- Install: `bundled with Claude desktop (Cowork plugin 'legal'); source: github.com/anthropics/knowledge-work-plugins`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
