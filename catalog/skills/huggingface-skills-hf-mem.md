# hf-mem

> Hugging Face CLI to estimate the required memory to load Safetensors or GGUF model weights for inference from the Hugging Face Hub

| | |
|---|---|
| **ID** | `huggingface/skills:hf-mem` |
| **Pack** | Productivity & Automation (also: AI / ML Engineering) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [huggingface/skills](https://github.com/huggingface/skills) |
| **License** | Apache-2.0 |
| **Size** | 80 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> `hf_mem` estimates the required memory for inference, including model weights and an optional KV cache, for Safetensors and GGUF for models on the Hugging Face Hub using HTTP Range requests i.e., without downloading or loading any weights locally.

## How it is structured

The skill's own section headings, in order:

- When to use?
- What are the requirements?
- How to run?
- Examples

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [huggingface/skills:hf-mcp](huggingface-skills-hf-mcp.md) - Use Hugging Face Hub via MCP server tools. Search models, datasets, Spaces, papers. Get repo details, fetch do
- [huggingface/skills:huggingface-community-evals](huggingface-skills-huggingface-community-evals.md) - Run evaluations for Hugging Face Hub models using inspect-ai and lighteval on local hardware. Use for backend 
- [huggingface/skills:huggingface-paper-publisher](huggingface-skills-huggingface-paper-publisher.md) - Publish and manage research papers on Hugging Face Hub. Supports creating paper pages, linking papers to model
- [huggingface/skills:huggingface-spaces](huggingface-skills-huggingface-spaces.md) - Build, deploy, and maintain applications on Hugging Face Spaces — Gradio / Docker / Static SDKs, ZeroGPU and d

## Invoke / install

- Invoke: `/huggingface/skills:hf-mem`
- Install: `python skills/skill-vetter/scripts/install.py huggingface/skills --path skills/hf-mem --commit fabc634a893f62ad5c2039830397efa35fa62715 --expect-tree 5e74b1ae7d0e15c61532382e881906139d14500650189662e46f0fadf93e05d7 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
