# huggingface-spaces

> Build, deploy, and maintain applications on Hugging Face Spaces — Gradio / Docker / Static SDKs, ZeroGPU and dedicated hardware, model loading, debugging, buckets, inference providers, community grants. Use whenever the user asks to create or host an app on Hugging Face, port code onto ZeroGPU, fix a Space that won't build or run, or otherwise work with `hf spaces …`, `@spaces.GPU`, Space README frontmatter, or the `spaces` Python package.

| | |
|---|---|
| **ID** | `huggingface/skills:huggingface-spaces` |
| **Pack** | AI / ML Engineering |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [huggingface/skills](https://github.com/huggingface/skills) |
| **License** | Apache-2.0 |
| **Size** | 243 lines in SKILL.md, 15 file(s) |

## When to use it

- Use whenever the user asks to create or host an app on Hugging Face, port code onto ZeroGPU, fix a Space that won't build or run, or otherwise work with `hf spaces …`, `@spaces.GPU`, Space README frontmatter, or the `spaces` Python package.

## What it says up front

> Hugging Face Spaces host machine-learning applications. There are 1M+ today; each Space is a git repo. This skill covers creating, building, debugging, and maintaining them.

## How it is structured

The skill's own section headings, in order:

- 0. Getting ready
- 1. What a Space is
  - Hardware tiers
- 2. Look for an existing demo first
- 3. Decide SDK and hardware
  - Sourcing the model
- 4. Create the Space
- 5. Build the app
  - README.md frontmatter
  - Minimal ZeroGPU Gradio app
  - Examples, docstrings, and MCP
  - requirements.txt
  - Per-SDK depth
- 6. Iterate on the Space, not locally
- 7. Verify
- 8. Permanent storage (buckets)
- 9. When things break
- Reference index

## What it bundles

- reference docs: `references/3d-cuda-extensions.md`, `references/3d-generation.md`, `references/3d-gsplat.md`, `references/3d-models.md`, `references/3d-outputs.md`, `references/buckets.md`, `references/debugging.md`, `references/gradio.md` ...
- 1 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [huggingface/skills:huggingface-lora-space-builder](huggingface-skills-huggingface-lora-space-builder.md) - Build and publish a Gradio demo on Hugging Face Spaces for a user-provided LoRA. Use when someone asks to crea
- [huggingface/skills:huggingface-zerogpu](huggingface-skills-huggingface-zerogpu.md) - AI demos and GPU compute with Gradio Spaces and Hugging Face Spaces ZeroGPU. Use when writing or reviewing cod
- [huggingface/skills:huggingface-community-evals](huggingface-skills-huggingface-community-evals.md) - Run evaluations for Hugging Face Hub models using inspect-ai and lighteval on local hardware. Use for backend 
- [huggingface/skills:hf-mem](huggingface-skills-hf-mem.md) - Hugging Face CLI to estimate the required memory to load Safetensors or GGUF model weights for inference from 

## Invoke / install

- Invoke: `/huggingface/skills:huggingface-spaces`
- Install: `python skills/skill-vetter/scripts/install.py huggingface/skills --path skills/huggingface-spaces --commit fabc634a893f62ad5c2039830397efa35fa62715 --expect-tree 96a109f250da2115070c532e9b65a2bebd8b9f3bd2fa3b58850c32f8f442a02f --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
