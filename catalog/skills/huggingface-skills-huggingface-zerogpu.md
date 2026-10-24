# huggingface-zerogpu

> AI demos and GPU compute with Gradio Spaces and Hugging Face Spaces ZeroGPU. Use when writing or reviewing code that uses `@spaces.GPU`, configuring `python_version` or `requirements.txt` for a ZeroGPU Space, or handling ZeroGPU-specific code constraints — pickle-based process isolation, `gr.State` semantics across the worker boundary, no `torch.compile` (use AoTI instead), CUDA wheel-only builds (no `nvcc` at build or runtime), large vs xlarge sizing, and dynamic duration callables. Make sure to use this skill whenever the user mentions ZeroGPU, `@spaces.GPU`, or the `spaces` Python package, or hits ZeroGPU-specific code errors like `PicklingError` across the worker boundary, `illegal duration`, or `flash-attn` wheel-build failures — even when the user does not explicitly ask for ZeroGPU coding guidance. Trigger on `import spaces` or `@spaces.GPU` in code.

| | |
|---|---|
| **ID** | `huggingface/skills:huggingface-zerogpu` |
| **Pack** | AI / ML Engineering (also: Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [huggingface/skills](https://github.com/huggingface/skills) |
| **License** | Apache-2.0 |
| **Size** | 290 lines in SKILL.md, 5 file(s) |

## When to use it

- Use when writing or reviewing code that uses `@spaces.GPU`, configuring `python_version` or `requirements.txt` for a ZeroGPU Space, or handling ZeroGPU-specific code constraints — pickle-based process isolation, `gr.State` semantics across the worker boundary,.

## What it says up front

> Rules and patterns for ML demos on Hugging Face Spaces with **ZeroGPU** hardware. Covers `@spaces.GPU`, duration and quota tuning, process isolation, the CUDA availability model, concurrency safety, and CUDA build constraints.

## How it is structured

The skill's own section headings, in order:

- Scope
- Reference Files
- Hardware
- Basic Pattern
- CUDA Availability Model
  - Device selection idiom still works
  - Eager loading is the right default
- Local Development: Just Install `spaces`
  - Anti-pattern
  - Do this instead
- Duration and Quota
  - Dynamic duration for variable workloads
- Process Isolation and Pickle
  - `gr.State` semantics across the boundary
- Concurrency
- Call Granularity
- CUDA Build Constraints
- Example Caching
- Dependency Management
  - `python_version` pin in README frontmatter
  - Do not pin `spaces` in `requirements.txt`
  - Pin `torch` to match wheel tags

## What it bundles

- reference docs: `references/concurrency.md`, `references/cuda-and-deps.md`, `references/how-quota-works.md`, `references/how-zerogpu-works.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [huggingface/skills:huggingface-spaces](huggingface-skills-huggingface-spaces.md) - Build, deploy, and maintain applications on Hugging Face Spaces — Gradio / Docker / Static SDKs, ZeroGPU and d
- [openai/skills:security-best-practices](openai-skills-security-best-practices.md) - Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only 
- [huggingface/skills:huggingface-lora-space-builder](huggingface-skills-huggingface-lora-space-builder.md) - Build and publish a Gradio demo on Hugging Face Spaces for a user-provided LoRA. Use when someone asks to crea

## Invoke / install

- Invoke: `/huggingface/skills:huggingface-zerogpu`
- Install: `python skills/skill-vetter/scripts/install.py huggingface/skills --path skills/huggingface-zerogpu --commit fabc634a893f62ad5c2039830397efa35fa62715 --expect-tree 9a3c54c8ab88948559de65d021c0f4918120f905e11d9f0ccc4b83ee9c99073b --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
