# customer-research

> Multi-source research on a customer question or topic with source attribution. Use when a customer asks something you need to look up, investigating whether a bug has been reported before, checking what was previously told to a specific account, or gathering background before drafting a response.

| | |
|---|---|
| **ID** | `anthropics/knowledge-work-plugins:customer-research` |
| **Pack** | Product Management (also: Research & Learning) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 253 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when a customer asks something you need to look up, investigating whether a bug has been reported before, checking what was previously told to a specific account, or gathering background before drafting a response.

## What it says up front

> Multi-source research on a customer question, product topic, or account-related inquiry. Synthesizes findings from all available sources with clear attribution and confidence scoring.

## How it is structured

The skill's own section headings, in order:

- Usage
- Workflow
  - 1. Parse the Research Request
  - 2. Search Available Sources
  - 3. Synthesize Findings
  - 4. Handle Insufficient Sources
  - 5. Customer-Facing Considerations
  - 6. Knowledge Capture
- Source Prioritization and Confidence
  - Confidence by Source Tier
  - Confidence Levels
  - Handling Contradictions
- When to Escalate vs. Answer Directly
  - Answer Directly When:
  - Escalate or Verify When:
  - Escalation Path:
- Research Documentation for Team Knowledge Base
  - When to Document:
  - Documentation Format:
  - Knowledge Base Hygiene:

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:notion-research-documentation](openai-skills-notion-research-documentation.md) - Research across Notion and synthesize into structured documentation; use when gathering info from multiple Not
- [legal:brief](legal-brief.md) - Generate contextual briefings for legal work — daily summary, topic research, or incident response. Use when s

## Invoke / install

- Invoke: `/anthropics/knowledge-work-plugins:customer-research`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/knowledge-work-plugins --path customer-support/skills/customer-research --commit 33d3dea41a341b341d4f5da2e8801ae0c89be2b8 --expect-tree 235eb88d75ff71105bbbf1a2a2b6723acf1c53d58fc95328bcf6e06a64b75d61 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
