# docs-changelog

> Generates and formats changelog files for a new release based on provided version and raw changelog data.

| | |
|---|---|
| **ID** | `google-gemini/gemini-cli:docs-changelog` |
| **Pack** | Software Development (also: Claude / Skills / Plugin Tooling, MLOps / DevOps / Cloud) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| **License** | Apache-2.0 |
| **Size** | 169 lines in SKILL.md, 5 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> To standardize the process of updating changelog files (`latest.md`, `preview.md`, `index.md`) based on automated release information.

## How it is structured

The skill's own section headings, in order:

- Objective
- Inputs
- Guidelines for `latest.md` and `preview.md` Highlights
- Initial Processing
- Path A: New Minor Version
  - A.1: Stable Release (e.g., `v0.28.0`)
  - A.2: Preview Release (e.g., `v0.29.0-preview.0`)
- Path B: Patch Version
  - B.1: Stable Patch (e.g., `v0.28.1`)
  - B.2: Preview Patch (e.g., `v0.29.0-preview.3`)
- Finalize

## What it bundles

- reference docs: `references/highlights_examples.md`, `references/index_template.md`, `references/latest_template.md`, `references/preview_template.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [bm:docs-update](bm-docs-update.md) - Generate or update project documentation verified against the codebase
- [bm:update](bm-update.md) - Update GSD to latest version with changelog display
- [bm:add-tests](bm-add-tests.md) - Generate tests for a completed phase based on UAT criteria and implementation

## Invoke / install

- Invoke: `/google-gemini/gemini-cli:docs-changelog`
- Install: `python skills/skill-vetter/scripts/install.py google-gemini/gemini-cli --path .gemini/skills/docs-changelog --commit 62bab5b232c15b925d31e655ce844ab939c882b7 --expect-tree 5c895bc92b6a34d778d486f5d7d40f1799ba85b35b4cde7972a44ff56762ec85 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
