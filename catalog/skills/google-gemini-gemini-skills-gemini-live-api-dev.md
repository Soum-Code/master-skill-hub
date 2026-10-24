# gemini-live-api-dev

> Use this skill when building real-time, bidirectional streaming applications with the Gemini Live API, or migrating legacy Live models (2.0/2.5/3.1) to Gemini 3.8 Live. Covers WebSocket-based audio/video/text streaming, voice activity detection (VAD), background reasoning (extended thinking), asynchronous function calling, session management, ephemeral tokens, live transcription, and live translation. SDKs covered - google-genai (Python), @google/genai (JavaScript/TypeScript).

| | |
|---|---|
| **ID** | `google-gemini/gemini-skills:gemini-live-api-dev` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [google-gemini/gemini-skills](https://github.com/google-gemini/gemini-skills) |
| **License** | Apache-2.0 |
| **Size** | 409 lines in SKILL.md, 2 file(s) |

## When to use it

- Use this skill when building real-time, bidirectional streaming applications with the Gemini Live API, or migrating legacy Live models (2.0/2.5/3.1) to Gemini 3.8 Live.

## What it says up front

> The Live API enables **low-latency, real-time voice and video interactions** with Gemini over WebSockets. It processes continuous streams of audio, video, or text to deliver immediate, human-like spoken responses and background reasoning.

## How it is structured

The skill's own section headings, in order:

- Overview
- Models
  - Current Models (Use These)
- SDKs
- Partner Integrations
- Audio Formats
- Quick Start
  - Authentication
  - Connecting to the Live API
  - Sending Text
  - Sending Audio
  - Sending Video
  - Receiving Audio and Text
- Background Reasoning (Extended Thinking)
- Live Translation (Gemini Live Translate)
  - Model
  - Configuration (`TranslationConfig`)
- Live Streaming Transcription (Gemini Live Transcribe)
  - Model
  - Modes
  - Python
  - JavaScript
  - Raw WebSockets
- Limitations
- Upgrading & Migration
- Best Practices
- Documentation Lookup
  - When MCP is Installed (Preferred)
  - When MCP is NOT Installed (Fallback Only)
  - Key Documentation Pages

## What it bundles

- reference docs: `references/migration.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [google-gemini/gemini-skills:gemini-api-dev](google-gemini-gemini-skills-gemini-api-dev.md) - Use this skill when writing code that calls the Gemini API for text generation, multi-turn chat, multimodal un
- [microsoft/skills:azure-ai-voicelive-dotnet](microsoft-skills-azure-ai-voicelive-dotnet.md) - Azure AI Voice Live SDK for .NET. Build real-time voice AI applications with bidirectional WebSocket communica
- [microsoft/skills:podcast-generation](microsoft-skills-podcast-generation.md) - Generate AI-powered podcast-style audio narratives using Azure OpenAI's GPT Realtime Mini model via WebSocket.
- [microsoft/skills:copilot-sdk](microsoft-skills-copilot-sdk.md) - Build applications powered by GitHub Copilot using the Copilot SDK. Use when creating programmatic integration

## Invoke / install

- Invoke: `/google-gemini/gemini-skills:gemini-live-api-dev`
- Install: `python skills/skill-vetter/scripts/install.py google-gemini/gemini-skills --path skills/gemini-live-api-dev --commit ee9da52195752ca83c2fca701d96bcb5a9c08d2d --expect-tree 690fec1802dcf0700c6edb5b48ed336f6d64b1a87987288d0e61eebf41261c99 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
