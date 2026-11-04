# regex-vs-llm-structured-text

> Decision framework for parsing structured text (quizzes, forms, invoices, receipts, tables) with a hybrid regex-first pipeline — regex extraction handles 95%+ cheaply, a confidence scorer flags low-confidence items, and an LLM validator fixes only the edge cases. Use when choosing between regex and LLM for text extraction, building a cheap document parser, or optimizing extraction cost and accuracy.

| | |
|---|---|
| **ID** | `affaan-m/ECC:regex-vs-llm-structured-text` |
| **Pack** | AI / ML Engineering |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 222 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when choosing between regex and LLM for text extraction, building a cheap document parser, or optimizing extraction cost and accuracy.

## What it says up front

> A practical decision framework for parsing structured text (quizzes, forms, invoices, documents). The key insight: regex handles 95-98% of cases cheaply and deterministically. Reserve expensive LLM calls for the remaining edge cases.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Decision Framework
- Architecture Pattern
- Implementation
  - 1. Regex Parser (Handles the Majority)
  - 2. Confidence Scoring
  - 3. LLM Validator (Edge Cases Only)
  - 4. Hybrid Pipeline
- Real-World Metrics
- Best Practices
- Anti-Patterns to Avoid
- When to Use

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:azure-ai-document-intelligence-dotnet](microsoft-skills-azure-ai-document-intelligence-dotnet.md) - Azure AI Document Intelligence SDK for .NET. Extract text, tables, and structured data from documents using pr

## Invoke / install

- Invoke: `/affaan-m/ECC:regex-vs-llm-structured-text`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/regex-vs-llm-structured-text --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 14809e5b7ad3bfa9a272f131b88f55dd98106fc1a015ce3f3c74e5988fab73a5 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
