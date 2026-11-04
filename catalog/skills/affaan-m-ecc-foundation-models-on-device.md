# foundation-models-on-device

> Apple FoundationModels framework for on-device LLM — text generation, guided generation with @Generable, tool calling, and snapshot streaming in iOS 26+. Use when adding on-device LLM features with Apple FoundationModels on iOS 26+.

| | |
|---|---|
| **ID** | `affaan-m/ECC:foundation-models-on-device` |
| **Pack** | AI / ML Engineering |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 244 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when adding on-device LLM features with Apple FoundationModels on iOS 26+.

## What it says up front

> Patterns for integrating Apple's on-device language model into apps using the FoundationModels framework. Covers text generation, structured output with `@Generable`, custom tool calling, and snapshot streaming — all running on-device for privacy and offline support.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Core Pattern — Availability Check
- Core Pattern — Basic Session
- Core Pattern — Guided Generation with @Generable
  - 1. Define a Generable Type
  - 2. Request Structured Output
  - Supported @Guide Constraints
- Core Pattern — Tool Calling
  - 1. Define a Tool
  - 2. Create Session with Tools
  - 3. Handle Tool Errors
- Core Pattern — Snapshot Streaming
  - SwiftUI Integration
- Key Design Decisions
- Best Practices
- Anti-Patterns to Avoid
- When to Use

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [claude-api](claude-api.md) - Reference for the Claude API and Anthropic SDKs - model ids, pricing, streaming, tool use, MCP, agents, prompt
- [microsoft/skills:podcast-generation](microsoft-skills-podcast-generation.md) - Generate AI-powered podcast-style audio narratives using Azure OpenAI's GPT Realtime Mini model via WebSocket.

## Invoke / install

- Invoke: `/affaan-m/ECC:foundation-models-on-device`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/foundation-models-on-device --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 24b12226e57c0612518faf904d5553190269aa4581164e4985ea0c6af2b48bcb --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
