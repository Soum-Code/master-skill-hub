# gemini-omni-flash-api

> Use this skill for generative video editing, text-to-video, image- and video-referenced video generation, first-frame-to-video, first-and-last-frame transitions, and video extensions using Gemini Omni 1.2 Flash (gemini-omni-1.2-flash) via the official google-genai SDK. Includes workflows for pre-processing/optimizing high-resolution or long source videos with ffmpeg, stripping audio for full sound regeneration, and handling turn-by-turn video editing and parallel execution.

| | |
|---|---|
| **ID** | `google-gemini/gemini-skills:gemini-omni-flash-api` |
| **Pack** | Creative & Media (also: Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [google-gemini/gemini-skills](https://github.com/google-gemini/gemini-skills) |
| **License** | Apache-2.0 |
| **Size** | 413 lines in SKILL.md, 5 file(s) |

## When to use it

- Use this skill for generative video editing, text-to-video, image- and video-referenced video generation, first-frame-to-video, first-and-last-frame transitions, and video extensions using Gemini Omni 1.2 Flash (gemini-omni-1.2-flash) via the official google-g.

## What it says up front

> This skill uses the Gemini Omni 1.2 Flash model (`gemini-omni-1.2-flash`) to perform text-to-video generation, image-to-video generation (first-frame and two-frame keyframe transitions), reference-to-video (R2V) generation, video extensions (3s–10s per turn, up to 30s total), and video editing.

## How it is structured

The skill's own section headings, in order:

- Core capabilities
- Workflow
- Reference Documentation
- Dependencies and Prerequisites
- Available scripts
- Audio handling in video editing
- Prompting Gemini Omni 1.2 Flash
  - Single scene
  - Removing unwanted elements
  - Prompts for editing
  - Prompting the audio
  - Timing events
  - Meta prompting
  - Text in videos
  - Prompts for extending a video
  - Video extension & reference constraints
  - Binding uploaded images and videos with natural language

## What it bundles

- scripts: `scripts/upload_file.py`, `scripts/video/generate_video.py`, `scripts/video/inspect_video.py`, `scripts/video/prep_video.py`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [google-gemini/gemini-skills:gemini-api-dev](google-gemini-gemini-skills-gemini-api-dev.md) - Use this skill when writing code that calls the Gemini API for text generation, multi-turn chat, multimodal un
- [google-gemini/gemini-skills:gemini-live-api-dev](google-gemini-gemini-skills-gemini-live-api-dev.md) - Use this skill when building real-time, bidirectional streaming applications with the Gemini Live API, or migr
- [affaan-m/ECC:fal-ai-media](affaan-m-ecc-fal-ai-media.md) - Unified media generation via fal.ai MCP — image, video, and audio. Covers text-to-image (Nano Banana), text/im

## Invoke / install

- Invoke: `/google-gemini/gemini-skills:gemini-omni-flash-api`
- Install: `python skills/skill-vetter/scripts/install.py google-gemini/gemini-skills --path skills/gemini-omni-flash-api --commit 7cfc690ba9c8efe36a5316e6d4000e2b6aa25dbf --expect-tree 40340e0fc146d132faa4622895477960bdddf1ae17686f009eaabff211910b50 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
