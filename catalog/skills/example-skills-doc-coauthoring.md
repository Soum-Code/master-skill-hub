# doc-coauthoring

> Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs, or similar structured content. This workflow helps users efficiently transfer context, refine content through iteration, and verify the doc works for readers. Trigger when user mentions writing docs, creating proposals, drafting specs, or similar documentation tasks.

| | |
|---|---|
| **ID** | `example-skills:doc-coauthoring` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `example-skills` v3b3fad96af16 - [anthropics/skills](https://github.com/anthropics/skills) |
| **License** | not declared |
| **Size** | 376 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when user wants to write documentation, proposals, technical specs, decision docs, or similar structured content.
- Trigger when user mentions writing docs, creating proposals, drafting specs, or similar documentation tasks.

## How it is structured

The skill's own section headings, in order:

- When to Offer This Workflow
- Stage 1: Context Gathering
  - Initial Questions
  - Info Dumping
- Stage 2: Refinement & Structure
  - Step 1: Clarifying Questions
  - Step 2: Brainstorming
  - Step 3: Curation
  - Step 4: Gap Check
  - Step 5: Drafting
  - Step 6: Iterative Refinement
  - Quality Checking
  - Near Completion
- Stage 3: Reader Testing
  - Testing Approach
  - Step 1: Predict Reader Questions
  - Step 2: Test with Sub-Agent
  - Step 3: Run Additional Checks
  - Step 4: Report and Fix
  - Step 1: Predict Reader Questions
  - Step 2: Setup Testing
  - Step 3: Additional Checks
  - Step 4: Iterate Based on Results
  - Exit Condition (Both Approaches)
- Final Review
- Tips for Effective Guidance

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [engineering:documentation](engineering-documentation.md) - Write and maintain technical documentation. Trigger with "write docs for", "document this", "create a README",
- [bm:new-ddd](bm-new-ddd.md) - Initialize a new project using Documentation-Driven Development. Research, then write user-facing docs (SPEC.m

## Invoke / install

- Invoke: `/example-skills:doc-coauthoring`  (Skill tool: `example-skills:doc-coauthoring`)
- Install: `claude plugin marketplace add anthropics/skills && claude plugin install example-skills@anthropic-agent-skills`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
