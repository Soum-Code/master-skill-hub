# i18n-sync

> Translate and synchronize application JSON locale files using source-key usage, project terminology, and focused validation. Use when adding keys or languages, updating source copy, or reviewing missing and stale translations.

| | |
|---|---|
| **ID** | `affaan-m/ECC:i18n-sync` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 142 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when adding keys or languages, updating source copy, or reviewing missing and stale translations.

## What it says up front

> Translate application locale files by reading where each string appears in the product. Preserve the project's JSON structure, interpolation syntax, and unrelated translations. Prepare a reviewable patch; apply it through the project's existing serializer or precise file edits, without introducing a

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Scope and Prerequisites
- Workflow
  - 1. Establish the worklist
  - 2. Gather usage context
  - 3. Translate with project tone
  - 4. Prepare, apply, and validate the patch
  - 5. Report
- Optional Locakit Reports
- Hook Integration
- Out of Scope
- Related

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:redis-patterns](affaan-m-ecc-redis-patterns.md) - Redis data structure patterns, caching strategies, distributed locks, rate limiting, pub/sub, and connection m

## Invoke / install

- Invoke: `/affaan-m/ECC:i18n-sync`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/i18n-sync --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 5da229f0d8a71234c63c53b513f4d6d824d0873aac569850026aee21ffd70434 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
