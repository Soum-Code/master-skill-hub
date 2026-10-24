# gemini-api-dev

> Use this skill when writing code that calls the Gemini API for text generation, multi-turn chat, multimodal understanding, image generation, video generation, speech generation (TTS), voice design, voice replication, streaming responses, background research tasks, function calling, structured output, or migrating from the old generateContent API. Covers SDK usage and best practices for Gemini models and agents in Python and TypeScript.

| | |
|---|---|
| **ID** | `google-gemini/gemini-skills:gemini-api-dev` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [google-gemini/gemini-skills](https://github.com/google-gemini/gemini-skills) |
| **License** | Apache-2.0 |
| **Size** | 444 lines in SKILL.md, 2 file(s) |

## When to use it

- Use this skill when writing code that calls the Gemini API for text generation, multi-turn chat, multimodal understanding, image generation, video generation, speech generation (TTS), voice design, voice replication, streaming responses, background research ta.

## What it says up front

> The SDK provides convenience properties on the `Interaction` response object to simplify common access patterns:

## How it is structured

The skill's own section headings, in order:

- Critical Rules (Always Apply)
  - Current Models (Use These)
  - Current Agents
  - Current SDKs
- Important Additional Notes
- Quick Start
  - Python
  - JavaScript/TypeScript
- Response Helpers
- Stateful Conversation
  - Python
  - JavaScript/TypeScript
- Deep Research Agent
  - Python
  - JavaScript/TypeScript
- Managed Agents
  - Antigravity Agent
  - Custom Agents
- Streaming
  - Python
  - JavaScript/TypeScript
- Documentation Pages
- Data Model
  - Step Types
  - Content types (inside `content` array on `model_output` and `user_input` steps)
  - Streaming Event Types
  - Delta Types
- Gemini Live API

## What it bundles

- reference docs: `references/migration.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [google-gemini/gemini-skills:gemini-live-api-dev](google-gemini-gemini-skills-gemini-live-api-dev.md) - Use this skill when building real-time, bidirectional streaming applications with the Gemini Live API, or migr
- [microsoft/skills:podcast-generation](microsoft-skills-podcast-generation.md) - Generate AI-powered podcast-style audio narratives using Azure OpenAI's GPT Realtime Mini model via WebSocket.
- [google-gemini/gemini-skills:gemini-omni-flash-api](google-gemini-gemini-skills-gemini-omni-flash-api.md) - Use this skill for generative video editing, text-to-video, image-referenced video generation, first-frame-to-
- [microsoft/skills:azure-ai-agents-persistent-dotnet](microsoft-skills-azure-ai-agents-persistent-dotnet.md) - Azure AI Agents Persistent SDK for .NET. Low-level SDK for creating and managing AI agents with threads, messa

## Invoke / install

- Invoke: `/google-gemini/gemini-skills:gemini-api-dev`
- Install: `python skills/skill-vetter/scripts/install.py google-gemini/gemini-skills --path skills/gemini-api-dev --commit ee9da52195752ca83c2fca701d96bcb5a9c08d2d --expect-tree 6a7da49395ede3eefc0b9048562f5c12dccb9049544be353cba580db490408a2 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
