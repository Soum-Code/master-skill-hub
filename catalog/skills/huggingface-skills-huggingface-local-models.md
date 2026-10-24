# huggingface-local-models

> Use to select models to run locally with llama.cpp and GGUF on CPU, Mac Metal, CUDA, or ROCm. Covers finding GGUFs, quant selection, running servers, exact GGUF file lookup, conversion, and OpenAI-compatible local serving.

| | |
|---|---|
| **ID** | `huggingface/skills:huggingface-local-models` |
| **Pack** | AI / ML Engineering |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [huggingface/skills](https://github.com/huggingface/skills) |
| **License** | Apache-2.0 |
| **Size** | 114 lines in SKILL.md, 4 file(s) |

## When to use it

- Use to select models to run locally with llama.cpp and GGUF on CPU, Mac Metal, CUDA, or ROCm.

## What it says up front

> Search the Hugging Face Hub for llama.cpp-compatible GGUF repos, choose the right quant, and launch the model with `llama-cli` or `llama-server`.

## How it is structured

The skill's own section headings, in order:

- Default Workflow
- Quick Start
  - Install llama.cpp
  - Authenticate for gated repos
  - Search the Hub
  - Run directly from the Hub
  - Run an exact GGUF file
  - Convert only when no GGUF is available
  - Smoke test a local server
- Quant Choice
- Load References
- Resources

## What it bundles

- reference docs: `references/hardware.md`, `references/hub-discovery.md`, `references/quantization.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/huggingface/skills:huggingface-local-models`
- Install: `python skills/skill-vetter/scripts/install.py huggingface/skills --path skills/huggingface-local-models --commit fabc634a893f62ad5c2039830397efa35fa62715 --expect-tree 65ce32dd79dcc86c29a159a5e51992d85d03b1f0ea225f447920dfeb5432e6aa --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
