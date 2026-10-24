# transformers-js

> Use Transformers.js to run state-of-the-art machine learning models directly in JavaScript/TypeScript. Supports NLP (text classification, translation, summarization), computer vision (image classification, object detection), audio (speech recognition, audio classification), and multimodal tasks. Works in browsers and server-side runtimes (Node.js, Bun, Deno) with WebGPU/WASM using pre-trained models from Hugging Face Hub.

| | |
|---|---|
| **ID** | `huggingface/skills:transformers-js` |
| **Pack** | AI / ML Engineering |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [huggingface/skills](https://github.com/huggingface/skills) |
| **License** | Apache-2.0 |
| **Size** | 693 lines in SKILL.md, 8 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Transformers.js enables running state-of-the-art machine learning models directly in JavaScript across browsers and server-side runtimes (Node.js, Bun, Deno), with no Python server required.

## How it is structured

The skill's own section headings, in order:

- When to Use This Skill
- Installation
  - NPM Installation
  - Browser Usage (CDN)
- Core Concepts
  - 1. Pipeline API
  - 2. Model Selection
  - 3. Device Selection
  - 4. Quantization Options
- Supported Tasks
  - Natural Language Processing
  - Computer Vision
  - Audio Processing
  - Multimodal
  - Feature Extraction (Embeddings)
- Finding and Choosing Models
  - Browsing the Hugging Face Hub
  - Choosing the Right Model
  - Example: Finding a Text Generation Model
  - Tips for Model Selection
- Advanced Configuration
  - Environment Configuration (`env`)
  - ModelRegistry (v4)
  - Standalone Tokenization (`@huggingface/tokenizers`)
  - Working with Tensors
  - Batch Processing
- Runtime-Specific Considerations
  - WebGPU Usage
  - WASM Performance
  - Progress Tracking & Loading Indicators

## What it bundles

- reference docs: `references/CACHE.md`, `references/CONFIGURATION.md`, `references/EXAMPLES.md`, `references/MODEL_ARCHITECTURES.md`, `references/MODEL_REGISTRY.md`, `references/PIPELINE_OPTIONS.md`, `references/TEXT_GENERATION.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [huggingface/skills:huggingface-vision-trainer](huggingface-skills-huggingface-vision-trainer.md) - Trains and fine-tunes vision models for object detection (D-FINE, RT-DETR v2, DETR, YOLOS), image classificati

## Invoke / install

- Invoke: `/huggingface/skills:transformers-js`
- Install: `python skills/skill-vetter/scripts/install.py huggingface/skills --path skills/transformers-js --commit fabc634a893f62ad5c2039830397efa35fa62715 --expect-tree 86a55d4e08a97843c1e997b1b291e3b18d32fbd27895eade5ed976f1e208e6ce --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
