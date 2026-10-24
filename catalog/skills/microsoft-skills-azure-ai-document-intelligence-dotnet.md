# azure-ai-document-intelligence-dotnet

> Azure AI Document Intelligence SDK for .NET. Extract text, tables, and structured data from documents using prebuilt and custom models. Use for invoice processing, receipt extraction, ID document analysis, and custom document models. Triggers: "Document Intelligence", "DocumentIntelligenceClient", "form recognizer", "invoice extraction", "receipt OCR", "document analysis .NET".

| | |
|---|---|
| **ID** | `microsoft/skills:azure-ai-document-intelligence-dotnet` |
| **Pack** | AI / ML Engineering (also: Documents, Writing & Content, MLOps / DevOps / Cloud) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 349 lines in SKILL.md, 1 file(s) |

## When to use it

- Use for invoice processing, receipt extraction, ID document analysis, and custom document models.

## What it says up front

> Extract text, tables, and structured data from documents using prebuilt and custom models.

## How it is structured

The skill's own section headings, in order:

- Installation
- Environment Variables
- Authentication
  - Microsoft Entra Token Credential
  - API Key
- Client Types
- Prebuilt Models
- Core Workflows
  - 1. Analyze Invoice
  - 2. Extract Layout (Text, Tables, Structure)
  - 3. Analyze Receipt
  - 4. Build Custom Model
  - 5. Build Document Classifier
  - 6. Classify Document
  - 7. Manage Models
- Key Types Reference
- Build Modes
- Best Practices
- Error Handling
- Related SDKs
- Reference Links

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:azure-ai-projects-dotnet](microsoft-skills-azure-ai-projects-dotnet.md) - Azure AI Projects SDK for .NET. High-level client for Azure AI Foundry projects including agents, connections,
- [microsoft/skills:azure-ai-openai-dotnet](microsoft-skills-azure-ai-openai-dotnet.md) - Azure OpenAI SDK for .NET. Client library for Azure OpenAI and OpenAI services. Use for chat completions, embe
- [microsoft/skills:azure-ai-agents-persistent-dotnet](microsoft-skills-azure-ai-agents-persistent-dotnet.md) - Azure AI Agents Persistent SDK for .NET. Low-level SDK for creating and managing AI agents with threads, messa
- [microsoft/skills:azure-identity-dotnet](microsoft-skills-azure-identity-dotnet.md) - Azure Identity library for .NET. Authentication library for Azure SDK clients using Microsoft Entra ID. Use fo

## Invoke / install

- Invoke: `/microsoft/skills:azure-ai-document-intelligence-dotnet`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/azure-sdk-dotnet/skills/azure-ai-document-intelligence-dotnet --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 070ce58fc71983fd60a319498d0a927f4aa11c415cb0d53f62266af4f008c1cc --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
