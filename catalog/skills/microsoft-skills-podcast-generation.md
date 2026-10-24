# podcast-generation

> Generate AI-powered podcast-style audio narratives using Azure OpenAI's GPT Realtime Mini model via WebSocket. Use when building text-to-speech features, audio narrative generation, podcast creation from content, or integrating with Azure OpenAI Realtime API for real audio output. Covers full-stack implementation from React frontend to Python FastAPI backend with WebSocket streaming.

| | |
|---|---|
| **ID** | `microsoft/skills:podcast-generation` |
| **Pack** | AI / ML Engineering (also: Software Development, Creative & Media, MLOps / DevOps / Cloud) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 122 lines in SKILL.md, 4 file(s) |

## When to use it

- Use when building text-to-speech features, audio narrative generation, podcast creation from content, or integrating with Azure OpenAI Realtime API for real audio output.

## What it says up front

> Generate real audio narratives from text content using Azure OpenAI's Realtime API.

## How it is structured

The skill's own section headings, in order:

- Quick Start
- Environment Configuration
- Core Workflow
  - Backend Audio Generation
  - Frontend Audio Playback
- Voice Options
- Realtime API Events
- Audio Format
- References

## What it bundles

- scripts: `scripts/pcm_to_wav.py`
- reference docs: `references/architecture.md`, `references/code-examples.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [openai/skills:speech](openai-skills-speech.md) - Use when the user asks for text-to-speech narration or voiceover, accessibility reads, audio prompts, or batch
- [google-gemini/gemini-skills:gemini-live-api-dev](google-gemini-gemini-skills-gemini-live-api-dev.md) - Use this skill when building real-time, bidirectional streaming applications with the Gemini Live API, or migr
- [google-gemini/gemini-skills:gemini-api-dev](google-gemini-gemini-skills-gemini-api-dev.md) - Use this skill when writing code that calls the Gemini API for text generation, multi-turn chat, multimodal un
- [microsoft/skills:azure-ai-voicelive-dotnet](microsoft-skills-azure-ai-voicelive-dotnet.md) - Azure AI Voice Live SDK for .NET. Build real-time voice AI applications with bidirectional WebSocket communica

## Invoke / install

- Invoke: `/microsoft/skills:podcast-generation`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/skills/podcast-generation --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 8b6f7db7fb5a4b2943390c9beb44175e795b8e5c0ed066f4facbb71117db2e51 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
