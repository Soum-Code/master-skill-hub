# videodb

> Ingest, index, search, edit, and monitor video and audio with the VideoDB Python SDK — upload from files, URLs, or RTSP feeds, build spoken and scene indexes with timestamped search and playable clips, transcode and reframe, do timeline edits (subtitles, overlays, dubbing), and run real-time alerts on live streams or desktop capture. Use when working with video search, transcription, clipping, transcoding, streaming, or live video alerts.

| | |
|---|---|
| **ID** | `affaan-m/ECC:videodb` |
| **Pack** | Creative & Media (also: Documents, Writing & Content) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 379 lines in SKILL.md, 12 file(s) |

## When to use it

- Use when working with video search, transcription, clipping, transcoding, streaming, or live video alerts.

## What it says up front

> Before running any VideoDB code, change to the project directory and load environment variables:

## How it is structured

The skill's own section headings, in order:

- When to use
  - Desktop Perception
  - Video ingest + stream
  - Index + search (timestamps + evidence)
  - Timeline editing + generation
  - Live streams (RTSP) + monitoring
- How it works
  - Common inputs
  - Common outputs
  - Running Python code
  - Setup
  - 1. Install SDK
  - 2. Configure API key
  - Quick Reference
  - Upload media
  - Transcript + subtitle
  - Search inside videos
  - Scene search
  - Timeline editing
  - Transcode video (resolution / quality change)
  - Reframe aspect ratio (for social platforms)
  - Generative media
- Error handling
  - Common pitfalls
- Examples
  - Canonical prompts
  - Screen Recording (Desktop Capture)
- Additional docs
  - When to use what
- Provenance

## What it bundles

- scripts: `scripts/ws_listener.py`
- reference docs: `reference/api-reference.md`, `reference/capture-reference.md`, `reference/capture.md`, `reference/editor.md`, `reference/generative.md`, `reference/rtstream-reference.md`, `reference/rtstream.md`, `reference/search.md` ...

## Permissions and risk notes

- Pre-approved tools: `Read`, `Grep`, `Glob`, `Bash(python:*)`
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [google-gemini/gemini-skills:gemini-live-api-dev](google-gemini-gemini-skills-gemini-live-api-dev.md) - Use this skill when building real-time, bidirectional streaming applications with the Gemini Live API, or migr
- [microsoft/skills:azure-ai-voicelive-dotnet](microsoft-skills-azure-ai-voicelive-dotnet.md) - Azure AI Voice Live SDK for .NET. Build real-time voice AI applications with bidirectional WebSocket communica

## Invoke / install

- Invoke: `/affaan-m/ECC:videodb`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/videodb --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 16816a1e9ea4b4e846f8bbfa9718afba0d429d7612533cd794ca07649986f039 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
