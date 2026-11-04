# ecc-recipes

> Map a described workflow to the right ECC command group with run-order and stop condition, or browse all command-group recipe families read live from the commands directory. Advisory only — never executes. Use when asked which commands run a workflow, the command sequence for a task, or to list ECC pipelines; not for executing the task (route to the command itself), single-command docs (use ecc-guide), or prompt rewrites (use prompt-optimizer).

| | |
|---|---|
| **ID** | `affaan-m/ECC:ecc-recipes` |
| **Pack** | MLOps / DevOps / Cloud (also: AI / ML Engineering, Claude / Skills / Plugin Tooling, Operations & Business) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 151 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when asked which commands run a workflow, the command sequence for a task, or to list ECC pipelines; not for executing the task (route to the command itself), single-command docs (use ecc-guide), or prompt rewrites (use prompt-optimizer).

## What it says up front

> One entry point for "which group of ECC slash-commands runs my workflow, in what order, and when do I stop." Also browses every command-group recipe family.

## How it is structured

The skill's own section headings, in order:

- When to Activate
  - Do Not Use When
- Core Principle
  - Live reads
- Family Classification (by prefix)
- How It Works
  - Catalog mode (no description)
  - Match mode (description given)
- Output Template (match mode)
- Examples
- Non-Goals

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:prompt-optimizer](affaan-m-ecc-prompt-optimizer.md) - Analyze draft prompts, detect intent and missing context, match ECC commands, skills, and agents, and output a
- [affaan-m/ECC:ecc-guide](affaan-m-ecc-ecc-guide.md) - Answer questions about ECC by reading the live repo surface — agents, skills, commands, hooks, rules, install 
- [affaan-m/ECC:docs-governance](affaan-m-ecc-docs-governance.md) - Route broad documentation-governance requests to existing ECC skills and run an opt-in, read-only audit of map

## Invoke / install

- Invoke: `/affaan-m/ECC:ecc-recipes`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/ecc-recipes --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree fa9d39d31e6b8cd38477a78f59e0a2843fd2820ab3e9748d24ba35dad99b6d10 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
