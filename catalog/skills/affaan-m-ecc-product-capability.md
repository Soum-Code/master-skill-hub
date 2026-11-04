# product-capability

> Translate PRD intent, roadmap asks, or product discussions into an implementation-ready capability plan that exposes constraints, invariants, interfaces, and unresolved decisions before multi-service work starts. Use when the user needs an ECC-native PRD-to-SRS lane instead of vague planning prose.

| | |
|---|---|
| **ID** | `affaan-m/ECC:product-capability` |
| **Pack** | Product Management |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 143 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user needs an ECC-native PRD-to-SRS lane instead of vague planning prose.

## What it says up front

> This skill turns product intent into explicit engineering constraints.

## How it is structured

The skill's own section headings, in order:

- When to Use
- Canonical Artifact
- Non-Negotiable Rules
- Inputs
- Core Workflow
  - 1. Restate the capability
  - 2. Resolve capability constraints
  - 3. Define the implementation-facing contract
  - 4. Translate into execution
- Output Format
- Good Outcomes

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:define-goal](openai-skills-define-goal.md) - Help the user define a concrete, measurable goal before starting work, especially when they ask to use the goa

## Invoke / install

- Invoke: `/affaan-m/ECC:product-capability`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/product-capability --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 7d860f23a36c39ec8a5a9623d9bdd2f0b333655973619b1d7d5a2a37bf792d8f --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
