# kb-article

> Draft a knowledge base article from a resolved issue or common question. Use when a ticket resolution is worth documenting for self-service, the same question keeps coming up, a workaround needs to be published, or a known issue should be communicated to customers.

| | |
|---|---|
| **ID** | `anthropics/knowledge-work-plugins:kb-article` |
| **Pack** | Documents, Writing & Content |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 352 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when a ticket resolution is worth documenting for self-service, the same question keeps coming up, a workaround needs to be published, or a known issue should be communicated to customers.

## What it says up front

> Draft a publish-ready knowledge base article from a resolved support issue, common question, or documented workaround. Structures the content for searchability and self-service.

## How it is structured

The skill's own section headings, in order:

- Usage
- Workflow
  - 1. Understand the Source Material
  - 2. Draft the Article
  - 3. Generate the Article
  - 4. Offer Next Steps
- Article Structure and Formatting Standards
  - Universal Article Elements
  - Formatting Rules
- Writing for Searchability
  - Title Best Practices
  - Keyword Optimization
  - Opening Sentence Formula
- Article Type Templates
  - How-to Articles
  - Troubleshooting Articles
  - FAQ Articles
  - Known Issue Articles
- Review and Maintenance Cadence
  - Article Lifecycle
  - When to Update vs. Create New
- Linking and Categorization Taxonomy
  - Category Structure
  - Linking Best Practices
- KB Writing Best Practices

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/knowledge-work-plugins:ticket-triage](anthropics-knowledge-work-plugins-ticket-triage.md) - Triage and prioritize a support ticket or customer issue. Use when a new ticket comes in and needs categorizat

## Invoke / install

- Invoke: `/anthropics/knowledge-work-plugins:kb-article`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/knowledge-work-plugins --path customer-support/skills/kb-article --commit 33d3dea41a341b341d4f5da2e8801ae0c89be2b8 --expect-tree 75ff7b8b860c94675d86e6210b3669bf277584dde9a2d99eee52a2ecd984ec76 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
