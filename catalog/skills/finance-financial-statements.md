# financial-statements

> Generate financial statements (income statement, balance sheet, cash flow) with period-over-period comparison and variance analysis. Use when preparing a monthly or quarterly P&L, closing the books and need to flag material variances, comparing actuals to budget, building a financial summary for leadership review, or looking up GAAP presentation requirements and period-end adjustments.

| | |
|---|---|
| **ID** | `finance:financial-statements` |
| **Pack** | Finance & Accounting |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `finance` v1.3.0 - [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 336 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when preparing a monthly or quarterly P&L, closing the books and need to flag material variances, comparing actuals to budget, building a financial summary for leadership review, or looking up GAAP presentation requirements and period-end adjustments.

## What it says up front

> Generate financial statements with period-over-period comparison and variance analysis. The workflow below walks through income statement generation; balance sheet and cash flow statement reference formats, GAAP presentation requirements (ASC 220/210/230), and common period-end adjustments are inclu

## How it is structured

The skill's own section headings, in order:

- Usage
  - Arguments
- Workflow
  - 1. Gather Financial Data
  - 2. Generate Income Statement
  - 3. Variance Analysis
  - 4. Key Metrics Summary
  - 5. Material Variance Summary
  - 6. Output
- GAAP Presentation Requirements
  - Income Statement (ASC 220 / IAS 1)
  - Balance Sheet (ASC 210 / IAS 1)
  - Cash Flow Statement (ASC 230 / IAS 7)
- Balance Sheet Reference Format
- Cash Flow Statement Reference Format (Indirect Method)
- Common Adjustments and Reclassifications
  - Period-End Adjustments
  - Reclassifications

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [finance:variance-analysis](finance-variance-analysis.md) - Decompose financial variances into drivers with narrative explanations and waterfall analysis. Use when analyz

## Invoke / install

- Invoke: `/finance:financial-statements`  (Skill tool: `finance:financial-statements`)
- Install: `bundled with Claude desktop (Cowork plugin 'finance'); source: github.com/anthropics/knowledge-work-plugins`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
