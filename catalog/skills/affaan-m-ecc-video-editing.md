# video-editing

> AI-assisted video editing workflows for cutting, structuring, and augmenting real footage. Covers the full pipeline from raw capture through FFmpeg, Remotion, ElevenLabs, fal.ai, and final polish in Descript or CapCut. Use when the user wants to edit video, cut footage, create vlogs, or build video content.

| | |
|---|---|
| **ID** | `affaan-m/ECC:video-editing` |
| **Pack** | Documents, Writing & Content (also: Creative & Media) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 338 lines in SKILL.md, 13 file(s) |

## When to use it

- Use when the user wants to edit video, cut footage, create vlogs, or build video content.

## What it says up front

> AI-assisted editing for real footage. Not generation from prompts. Editing existing video fast.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Core Thesis
- The Pipeline
- Layer 1: Capture (Screen Studio / Raw Footage)
- Layer 2: Organization (Claude / Codex)
- Layer 3: Deterministic Cuts (FFmpeg)
  - Extract segment by timestamp
  - Batch cut from edit decision list
  - Concatenate segments
  - Create proxy for faster editing
  - Extract audio for transcription
  - Normalize audio levels
- Layer 4: Programmable Composition (Remotion)
  - When to use Remotion
  - Basic Remotion composition
  - Render output
- Layer 5: Generated Assets (ElevenLabs / fal.ai)
  - Voiceover with ElevenLabs
  - Music and SFX with fal.ai
  - Generated visuals with fal.ai
  - VideoDB generative audio
- Layer 6: Final Polish (Descript / CapCut)
- Social Media Reframing
  - Reframe with FFmpeg
  - Reframe with VideoDB
- Scene Detection and Auto-Cut
  - FFmpeg scene detection
  - Silence detection for auto-cut
  - Highlight extraction
- What Each Tool Does Best

## What it bundles

- 12 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:brand-voice](affaan-m-ecc-brand-voice.md) - Build a source-derived writing style profile from real posts, essays, launch notes, docs, or site copy, then r
- [affaan-m/ECC:taste-application](affaan-m-ecc-taste-application.md) - Generate new video against a distilled style pack and cut it into a finished piece - plan takes from the refer
- [affaan-m/ECC:fal-ai-media](affaan-m-ecc-fal-ai-media.md) - Unified media generation via fal.ai MCP — image, video, and audio. Covers text-to-image (Nano Banana), text/im
- [affaan-m/ECC:skill-scout](affaan-m-ecc-skill-scout.md) - Search existing local, marketplace, GitHub, and web skill sources before creating a new skill. Use when the us

## Invoke / install

- Invoke: `/affaan-m/ECC:video-editing`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/video-editing --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 4a96d9b9f7312c6e2b030e98b0a950798589ec5bcddd48e6c531ce9ec8a059dc --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
