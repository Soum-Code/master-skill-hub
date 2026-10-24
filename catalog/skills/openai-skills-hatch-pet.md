# hatch-pet

> Create, repair, validate, visually QA, and package Codex-compatible animated pets and pet spritesheets from character art, generated images, company or prospect brand cues, or visual references. Use when a user wants a lightweight-worker Codex pet workflow, a non-pixel custom pet style, a prospect or company mascot pet, or a full 8x9 animated pet atlas with transparent unused cells, QA contact sheets, and pet.json packaging. This skill composes the installed $imagegen system skill for visual generation and uses bundled scripts for deterministic spritesheet assembly.

| | |
|---|---|
| **ID** | `openai/skills:hatch-pet` |
| **Pack** | Web, Frontend & UI Design (also: Creative & Media, Claude / Skills / Plugin Tooling) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 540 lines in SKILL.md, 14 file(s) |

## When to use it

- Use when a user wants a lightweight-worker Codex pet workflow, a non-pixel custom pet style, a prospect or company mascot pet, or a full 8x9 animated pet atlas with transparent unused cells, QA contact sheets, and pet.json packaging.

## How it is structured

The skill's own section headings, in order:

- Overview
- Generation Delegation
- Storage Controls
- Brand Discovery
- Pet-Safe Styles
- Transparency And Effects
- Visible Progress Plan
- Default Workflow
- Lightweight Visual Workers
- Subagent Delegation
- Repair Workflow
- Rules
- Acceptance Criteria

## What it bundles

- scripts: `scripts/compose_atlas.py`, `scripts/derive_running_left_from_running_right.py`, `scripts/extract_strip_frames.py`, `scripts/inspect_frames.py`, `scripts/make_contact_sheet.py`, `scripts/prepare_pet_run.py`, `scripts/render_animation_previews.py`, `scripts/validate_atlas.py`
- reference docs: `references/animation-rows.md`, `references/codex-pet-contract.md`, `references/qa-rubric.md`
- 2 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [openai/skills:figma-generate-design](openai-skills-figma-generate-design.md) - Use this skill alongside figma-use when the task involves translating an application page, view, or multi-sect

## Invoke / install

- Invoke: `/openai/skills:hatch-pet`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/hatch-pet --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree 55570d94020340b2f1867f44453c79b78d63de4124facaa085475a6b12b0eac1 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
