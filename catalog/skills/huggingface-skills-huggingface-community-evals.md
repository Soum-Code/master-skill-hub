# huggingface-community-evals

> Run evaluations for Hugging Face Hub models using inspect-ai and lighteval on local hardware. Use for backend selection, local GPU evals, and choosing between vLLM / Transformers / accelerate. Not for HF Jobs orchestration, model-card PRs, .eval_results publication, or community-evals automation.

| | |
|---|---|
| **ID** | `huggingface/skills:huggingface-community-evals` |
| **Pack** | AI / ML Engineering |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [huggingface/skills](https://github.com/huggingface/skills) |
| **License** | Apache-2.0 |
| **Size** | 208 lines in SKILL.md, 6 file(s) |

## When to use it

- Use for backend selection, local GPU evals, and choosing between vLLM / Transformers / accelerate.

## What it says up front

> This skill is for **running evaluations against models on the Hugging Face Hub on local hardware**.

## How it is structured

The skill's own section headings, in order:

- Option A: inspect-ai with local inference providers path
- Option B: inspect-ai on Local GPU
- Option C: lighteval on Local GPU

## What it bundles

- scripts: `scripts/inspect_eval_uv.py`, `scripts/inspect_vllm_uv.py`, `scripts/lighteval_vllm_uv.py`
- 2 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [huggingface/skills:hf-mcp](huggingface-skills-hf-mcp.md) - Use Hugging Face Hub via MCP server tools. Search models, datasets, Spaces, papers. Get repo details, fetch do
- [huggingface/skills:huggingface-vision-trainer](huggingface-skills-huggingface-vision-trainer.md) - Trains and fine-tunes vision models for object detection (D-FINE, RT-DETR v2, DETR, YOLOS), image classificati
- [huggingface/skills:huggingface-spaces](huggingface-skills-huggingface-spaces.md) - Build, deploy, and maintain applications on Hugging Face Spaces — Gradio / Docker / Static SDKs, ZeroGPU and d
- [huggingface/skills:hf-mem](huggingface-skills-hf-mem.md) - Hugging Face CLI to estimate the required memory to load Safetensors or GGUF model weights for inference from 

## Invoke / install

- Invoke: `/huggingface/skills:huggingface-community-evals`
- Install: `python skills/skill-vetter/scripts/install.py huggingface/skills --path skills/huggingface-community-evals --commit fabc634a893f62ad5c2039830397efa35fa62715 --expect-tree 196abedecc0807880376765525f4821e37c532d22a4f77fce994e56174f7b2fb --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
