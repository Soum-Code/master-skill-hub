# rules-distill

> Scan skills to extract cross-cutting principles and distill them into rules — append, revise, or create new rule files. Use when the same principle keeps recurring across skills and belongs in a rule file instead.

| | |
|---|---|
| **ID** | `affaan-m/ECC:rules-distill` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 266 lines in SKILL.md, 3 file(s) |

## When to use it

- Use when the same principle keeps recurring across skills and belongs in a rule file instead.

## What it says up front

> Scan installed skills, extract cross-cutting principles that appear in multiple skills, and distill them into rules — appending to existing rule files, revising outdated content, or creating new rule files.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
  - Phase 1: Inventory (Deterministic Collection)
  - Phase 2: Cross-read, Match & Verdict (LLM Judgment)
  - Phase 3: User Review & Execution
- Example
  - End-to-end run
- Design Principles

## What it bundles

- scripts: `scripts/scan-rules.sh`, `scripts/scan-skills.sh`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [anthropics/claude-code:Writing Hookify Rules](anthropics-claude-code-writing-hookify-rules.md) - This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hooki
- [anthropics/claude-plugins-official:writing-hookify-rules](anthropics-claude-plugins-official-writing-hookify-rules.md) - This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hooki

## Invoke / install

- Invoke: `/affaan-m/ECC:rules-distill`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/rules-distill --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 30c73467dbf19fcb6ec369ad435544062a8bad991135df344f811f1d2a9d6b40 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
