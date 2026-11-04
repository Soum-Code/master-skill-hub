# module-governance

> Establish or maintain a business module's local agent instructions, domain-context links, and interface ownership when implementing a new module or changing its responsibilities. Reuse project-level rules and existing ECC workflows; ordinary bug fixes, styling, and read-only design discussions do not start module documentation setup.

| | |
|---|---|
| **ID** | `affaan-m/ECC:module-governance` |
| **Pack** | Operations & Business (also: Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 131 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Connect module-level working rules to existing domain language, contracts, and decisions. This is an orchestration skill, not a second DDD methodology or an automatic documentation generator.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- How It Works
  - 1. Discover the boundary before creating documents
  - 2. Separate project-wide rules from local rules
  - 3. Reuse the existing knowledge owners
  - 4. Maintain only the authorized records
  - 5. Verify both meaning and links
- Examples
- Anti-Patterns
- Delivery
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:docs-governance](affaan-m-ecc-docs-governance.md) - Route broad documentation-governance requests to existing ECC skills and run an opt-in, read-only audit of map
- [simplify](simplify.md) - Review changed code for reuse, simplification, efficiency and altitude cleanups, then apply the fixes. Quality

## Invoke / install

- Invoke: `/affaan-m/ECC:module-governance`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/module-governance --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 9dbaa84ce9a724f0844ee9ffd6bd32c7ec7ed0bcd7c4c68c5709fdc286a5f991 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
