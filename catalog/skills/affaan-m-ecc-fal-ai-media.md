# fal-ai-media

> Unified media generation via fal.ai MCP — image, video, and audio. Covers text-to-image (Nano Banana), text/image-to-video (Seedance, Kling, Veo 3), text-to-speech (CSM-1B), and video-to-audio (ThinkSound). Use when the user wants to generate images, videos, or audio with AI.

| | |
|---|---|
| **ID** | `affaan-m/ECC:fal-ai-media` |
| **Pack** | Creative & Media |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 295 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user wants to generate images, videos, or audio with AI.

## What it says up front

> Generate images, videos, and audio using fal.ai models via MCP.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- MCP Requirement
- MCP Tools
- Image Generation
  - Nano Banana 2 (Fast)
  - Nano Banana Pro (High Fidelity)
  - Common Image Parameters
  - Image Editing
- Video Generation
  - Seedance 1.0 Pro (ByteDance)
  - Kling Video v3 Pro
  - Veo 3 (Google DeepMind)
  - Image-to-Video
  - Video Parameters
- Audio Generation
  - CSM-1B (Conversational Speech)
  - ThinkSound (Video-to-Audio)
  - ElevenLabs (via API, no MCP)
  - VideoDB Generative Audio
- Cost Estimation
- Model Discovery
- Tips
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:transcribe](openai-skills-transcribe.md) - Transcribe audio files to text with optional diarization and known-speaker hints. Use when a user asks to tran
- [microsoft/skills:podcast-generation](microsoft-skills-podcast-generation.md) - Generate AI-powered podcast-style audio narratives using Azure OpenAI's GPT Realtime Mini model via WebSocket.
- [openai/skills:speech](openai-skills-speech.md) - Use when the user asks for text-to-speech narration or voiceover, accessibility reads, audio prompts, or batch
- [affaan-m/ECC:video-editing](affaan-m-ecc-video-editing.md) - AI-assisted video editing workflows for cutting, structuring, and augmenting real footage. Covers the full pip

## Invoke / install

- Invoke: `/affaan-m/ECC:fal-ai-media`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/fal-ai-media --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree b79a2f0e6063451723cafaaf6dd6e955a1758582664237d44a43f004b78c3929 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
