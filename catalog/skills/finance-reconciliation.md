# reconciliation

> Reconcile accounts by comparing GL balances to subledgers, bank statements, or third-party data. Use when performing bank reconciliations, GL-to-subledger recs, intercompany reconciliations, or identifying and categorizing reconciling items.

| | |
|---|---|
| **ID** | `finance:reconciliation` |
| **Pack** | Finance & Accounting (also: Data & Analytics) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `finance` v1.3.0 - [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 176 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when performing bank reconciliations, GL-to-subledger recs, intercompany reconciliations, or identifying and categorizing reconciling items.

## What it says up front

> Methodology and best practices for account reconciliation, including GL-to-subledger, bank reconciliations, and intercompany. Covers reconciling item categorization, aging analysis, and escalation.

## How it is structured

The skill's own section headings, in order:

- Reconciliation Types
  - GL to Subledger Reconciliation
  - Bank Reconciliation
  - Intercompany Reconciliation
- Reconciling Item Categorization
  - Category 1: Timing Differences
  - Category 2: Adjustments Required
  - Category 3: Requires Investigation
- Aging Analysis for Outstanding Items
  - Aging Report Format
  - Trending
- Escalation Thresholds
- Reconciliation Best Practices

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/finance:reconciliation`  (Skill tool: `finance:reconciliation`)
- Install: `bundled with Claude desktop (Cowork plugin 'finance'); source: github.com/anthropics/knowledge-work-plugins`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
