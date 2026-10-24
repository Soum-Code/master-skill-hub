# huggingface-tool-builder

> Use this skill when the user wants to build tool/scripts or achieve a task where using data from the Hugging Face API would help. This is especially useful when chaining or combining API calls or the task will be repeated/automated. This Skill creates a reusable script to fetch, enrich or process data.

| | |
|---|---|
| **ID** | `huggingface/skills:huggingface-tool-builder` |
| **Pack** | AI / ML Engineering (also: Data & Analytics, Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [huggingface/skills](https://github.com/huggingface/skills) |
| **License** | Apache-2.0 |
| **Size** | 121 lines in SKILL.md, 8 file(s) |

## When to use it

- Use this skill when the user wants to build tool/scripts or achieve a task where using data from the Hugging Face API would help.

## What it says up front

> Your purpose is now is to create reusable command line scripts and utilities for using the Hugging Face API, allowing chaining, piping and intermediate processing where helpful. You can access the API directly, as well as use the `hf` command line tool. Model and Dataset cards can be accessed from r

## How it is structured

The skill's own section headings, in order:

- Script Rules
- Sample Scripts
- High Level Endpoints
- Accessing the API
- Using the HF command line tool

## What it bundles

- scripts: `references/baseline_hf_api.py`, `references/baseline_hf_api.sh`, `references/find_models_by_paper.sh`, `references/hf_enrich_models.sh`, `references/hf_model_card_frontmatter.sh`, `references/hf_model_papers_auth.sh`
- reference docs: `references/baseline_hf_api.py`, `references/baseline_hf_api.sh`, `references/baseline_hf_api.tsx`, `references/find_models_by_paper.sh`, `references/hf_enrich_models.sh`, `references/hf_model_card_frontmatter.sh`, `references/hf_model_papers_auth.sh`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [huggingface/skills:huggingface-datasets](huggingface-skills-huggingface-datasets.md) - Use this skill for Hugging Face Dataset Viewer API workflows that fetch subset/split metadata, paginate rows, 
- [openai/skills:cli-creator](openai-skills-cli-creator.md) - Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an
- [openai/skills:figma-generate-library](openai-skills-figma-generate-library.md) - Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create
- [huggingface/skills:huggingface-lora-space-builder](huggingface-skills-huggingface-lora-space-builder.md) - Build and publish a Gradio demo on Hugging Face Spaces for a user-provided LoRA. Use when someone asks to crea

## Invoke / install

- Invoke: `/huggingface/skills:huggingface-tool-builder`
- Install: `python skills/skill-vetter/scripts/install.py huggingface/skills --path skills/huggingface-tool-builder --commit fabc634a893f62ad5c2039830397efa35fa62715 --expect-tree 982cf1bca604ef49c2823fd10260eecc34b8d08029525e7b95d6a82298a5ecfc --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
