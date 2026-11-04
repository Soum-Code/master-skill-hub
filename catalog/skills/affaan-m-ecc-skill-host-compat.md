# skill-host-compat

> Lint ECC skills for Codex/Cursor-safe frontmatter and Claude-only substitutions before a skill PR.

| | |
|---|---|
| **ID** | `affaan-m/ECC:skill-host-compat` |
| **Pack** | Claude / Skills / Plugin Tooling (also: Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 103 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Run the same host-compat gate CI uses on `skills/` before opening a skill PR. The check is for Codex and Cursor copies, not Claude-only runtime quality.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Core Concepts
- Code Examples
- Anti-Patterns
- Best Practices
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:skill-stocktake](affaan-m-ecc-skill-stocktake.md) - Use when auditing Claude skills and commands for quality. Supports Quick Scan (changed skills only) and Full S
- [affaan-m/ECC:hermes-imports](affaan-m-ecc-hermes-imports.md) - Convert local Hermes operator workflows into sanitized ECC skills and release-pack artifacts. Use when prepari

## Invoke / install

- Invoke: `/affaan-m/ECC:skill-host-compat`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/skill-host-compat --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree f2ec7edaf743b9a664689a434ca90166acff644dc4ffb5f63ffe1a4d6e72c516 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
