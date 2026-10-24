# azure-ai-voicelive-dotnet

> Azure AI Voice Live SDK for .NET. Build real-time voice AI applications with bidirectional WebSocket communication. Use for voice assistants, conversational AI, real-time speech-to-speech, and voice-enabled chatbots. Triggers: "voice live", "real-time voice", "VoiceLiveClient", "VoiceLiveSession", "voice assistant .NET", "bidirectional audio", "speech-to-speech".

| | |
|---|---|
| **ID** | `microsoft/skills:azure-ai-voicelive-dotnet` |
| **Pack** | MLOps / DevOps / Cloud (also: AI / ML Engineering) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 276 lines in SKILL.md, 1 file(s) |

## When to use it

- Use for voice assistants, conversational AI, real-time speech-to-speech, and voice-enabled chatbots.

## What it says up front

> Real-time voice AI SDK for building bidirectional voice assistants with Azure AI.

## How it is structured

The skill's own section headings, in order:

- Installation
- Environment Variables
- Authentication
  - Microsoft Entra Token Credential
  - API Key
- Client Hierarchy
- Core Workflow
  - 1. Start Session and Configure
  - 2. Process Events
  - 3. Send User Message
  - 4. Function Calling
- Voice Options
- Supported Models
- Key Types Reference
- Best Practices
- Error Handling
- Audio Configuration
- Related SDKs
- Reference Links

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:azure-ai-openai-dotnet](microsoft-skills-azure-ai-openai-dotnet.md) - Azure OpenAI SDK for .NET. Client library for Azure OpenAI and OpenAI services. Use for chat completions, embe
- [microsoft/skills:azure-eventhub-dotnet](microsoft-skills-azure-eventhub-dotnet.md) - Azure Event Hubs SDK for .NET. Use for high-throughput event streaming: sending events (EventHubProducerClient
- [google-gemini/gemini-skills:gemini-live-api-dev](google-gemini-gemini-skills-gemini-live-api-dev.md) - Use this skill when building real-time, bidirectional streaming applications with the Gemini Live API, or migr
- [microsoft/skills:azure-ai-projects-dotnet](microsoft-skills-azure-ai-projects-dotnet.md) - Azure AI Projects SDK for .NET. High-level client for Azure AI Foundry projects including agents, connections,

## Invoke / install

- Invoke: `/microsoft/skills:azure-ai-voicelive-dotnet`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/azure-sdk-dotnet/skills/azure-ai-voicelive-dotnet --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 6e81899a41c44bb93cef80907dbbf0d70ba7af46f848aea3ac0260e48acd627f --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
