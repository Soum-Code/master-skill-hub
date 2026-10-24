# imagegen

> Generate or edit raster images when the task benefits from AI-created bitmap visuals such as photos, illustrations, textures, sprites, mockups, or transparent-background cutouts. Use when Codex should create a brand-new image, transform an existing image, or derive visual variants from references, and the output should be a bitmap asset rather than repo-native code or vector. Do not use when the task is better handled by editing existing SVG/vector/code-native assets, extending an established icon or logo system, or building the visual directly in HTML/CSS/canvas.

| | |
|---|---|
| **ID** | `openai/skills:imagegen` |
| **Pack** | Creative & Media (also: Web, Frontend & UI Design) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 280 lines in SKILL.md, 11 file(s) |

## When to use it

- Use when Codex should create a brand-new image, transform an existing image, or derive visual variants from references, and the output should be a bitmap asset rather than repo-native code or vector.
- Do not use when the task is better handled by editing existing SVG/vector/code-native assets, extending an established icon or logo system, or building the visual directly in HTML/CSS/canvas.

## How it is structured

The skill's own section headings, in order:

- Top-level modes and rules
- When to use
- When not to use
- Decision tree
- Workflow
- Prompt augmentation
  - Specificity policy
- Use-case taxonomy (exact slugs)
- Shared prompt schema
- Examples
  - Generation example (hero image)
  - Edit example (invariants)
- Prompting best practices
- Guidance by asset type
- Fallback CLI mode only
  - Temp and output conventions
  - Dependencies
  - Environment
  - Script-mode notes
- Reference map

## What it bundles

- scripts: `scripts/image_gen.py`
- reference docs: `references/cli.md`, `references/codex-network.md`, `references/image-api.md`, `references/prompting.md`, `references/sample-prompts.md`
- 4 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [taste-skill:brandkit](taste-skill-brandkit.md) - Premium brand-kit image generation skill for creating high-end brand-guidelines boards, logo systems, identity

## Invoke / install

- Invoke: `/openai/skills:imagegen`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.system/imagegen --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree 37e36926cf429a1953eba14989c2cb7180f5341fe5c09c011a229bfeec287832 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
