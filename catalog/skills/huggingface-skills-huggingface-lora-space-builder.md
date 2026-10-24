# huggingface-lora-space-builder

> Build and publish a Gradio demo on Hugging Face Spaces for a user-provided LoRA. Use when someone asks to create, generate, ship, or publish a Space, demo, Gradio app, or playground for a LoRA — including LoRAs for Qwen-Image, Qwen-Image-Edit, LTX-Video, Wan, FLUX, SDXL, or other diffusion base models. Also triggers when someone describes a LoRA they trained or hosts on the Hub and wants to share it. Covers picking the right base pipeline and `diffusers` inference recipe, designing a UI tailored to the LoRA's task and inputs (Union/multi-task control, edit, video, image, etc.), respecting model-card recommendations (trigger words, steps, guidance, LoRA scale, example inputs), and shipping to ZeroGPU hardware as a private Space by default.

| | |
|---|---|
| **ID** | `huggingface/skills:huggingface-lora-space-builder` |
| **Pack** | AI / ML Engineering |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [huggingface/skills](https://github.com/huggingface/skills) |
| **License** | Apache-2.0 |
| **Size** | 394 lines in SKILL.md, 8 file(s) |

## When to use it

- Use when someone asks to create, generate, ship, or publish a Space, demo, Gradio app, or playground for a LoRA — including LoRAs for Qwen-Image, Qwen-Image-Edit, LTX-Video, Wan, FLUX, SDXL, or other diffusion base models.
- Also triggers when someone describes a LoRA they trained or hosts on the Hub and wants to share it.

## What it says up front

> Build and publish a Gradio demo on Hugging Face Spaces that runs inference with a user-provided LoRA. Use whenever someone asks to create, generate, ship, or publish "a Space", "a demo", "a Gradio app", or "a playground" for a LoRA — whether the base model is Qwen-Image, Qwen-Image-Edit, LTX, or ano

## How it is structured

The skill's own section headings, in order:

- What "good" looks like for these demos
- Workflow
- Phase 1 — Gather LoRA info
- Phase 2 — Pick the base pipeline
- Phase 3 — Design the UI for this LoRA
- Phase 4 — Write the Space files
  - `app.py`
  - `requirements.txt`
  - `README.md`
  - Single batched approval — order of operations matters
- Phase 5 — Publish the Space
- Phase 6 — Smoke-test the Space
- What to avoid

## What it bundles

- reference docs: `references/adapting-to-the-lora.md`, `references/base-models/krea-2.md`, `references/base-models/ltx.md`, `references/base-models/qwen-image.md`, `references/creative-mode.md`, `references/tasks.md`, `references/zerogpu-and-publishing.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [huggingface/skills:huggingface-spaces](huggingface-skills-huggingface-spaces.md) - Build, deploy, and maintain applications on Hugging Face Spaces — Gradio / Docker / Static SDKs, ZeroGPU and d
- [huggingface/skills:huggingface-tool-builder](huggingface-skills-huggingface-tool-builder.md) - Use this skill when the user wants to build tool/scripts or achieve a task where using data from the Hugging F
- [huggingface/skills:hf-cloud-sagemaker-deployment-planner](huggingface-skills-hf-cloud-sagemaker-deployment-planner.md) - Plan and coordinate the deployment of a model to Amazon SageMaker AI. Use this skill whenever the user wants t
- [huggingface/skills:huggingface-zerogpu](huggingface-skills-huggingface-zerogpu.md) - AI demos and GPU compute with Gradio Spaces and Hugging Face Spaces ZeroGPU. Use when writing or reviewing cod

## Invoke / install

- Invoke: `/huggingface/skills:huggingface-lora-space-builder`
- Install: `python skills/skill-vetter/scripts/install.py huggingface/skills --path skills/huggingface-lora-space-builder --commit fabc634a893f62ad5c2039830397efa35fa62715 --expect-tree 64a99d1529027d675ca953f546604bf7c3d6b8efb33b34c0bfe0a75f3972a7bf --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
