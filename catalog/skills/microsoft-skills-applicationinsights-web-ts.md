# applicationinsights-web-ts

> Instrument browser/web apps with the Application Insights JavaScript SDK (@microsoft/applicationinsights-web). Use for Real User Monitoring (RUM) — page views, clicks, AJAX/fetch dependencies, exceptions, custom events, and browser-side GenAI agent traces correlated to backend OpenTelemetry traces. Covers SDK Loader Script and npm setup, framework extensions (React, React Native, Angular), Click Analytics, telemetry initializers, and OTel GenAI semantic conventions for agent/tool/model spans emitted from the browser.

| | |
|---|---|
| **ID** | `microsoft/skills:applicationinsights-web-ts` |
| **Pack** | Browser & Web Automation |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 466 lines in SKILL.md, 4 file(s) |

## When to use it

- Use for Real User Monitoring (RUM) — page views, clicks, AJAX/fetch dependencies, exceptions, custom events, and browser-side GenAI agent traces correlated to backend OpenTelemetry traces.

## What it says up front

> Real User Monitoring (RUM) for browser apps with `@microsoft/applicationinsights-web`. Auto-collects page views, AJAX/fetch dependencies, unhandled exceptions, and (with the Click Analytics plugin) clicks. Supports custom events, metrics, and **GenAI agent traces** that follow OpenTelemetry GenAI se

## How it is structured

The skill's own section headings, in order:

- Before Implementation
- Packages
- Installation
- Connection String
- Quick Start (npm)
- Quick Start (SDK Loader Script)
- Core Tracking APIs
- Telemetry Initializers (enrichment & filtering)
- Click Analytics
- SPA Route Tracking
- Distributed Tracing (correlate to backend)
- GenAI Agent Traces (OTel semantic conventions)
  - Required attribute keys (use the OTel names verbatim)
  - Pattern: invoke_agent + nested tool/model spans
  - KQL: query GenAI traces in App Insights
- React (TypeScript)
- React Native
- Performance — Web Vitals
- Cookies & Privacy
- Sampling
- Offline / Send-on-Unload
- Common Pitfalls
- Bundle Size
- Key Types
- Best Practices
- References

## What it bundles

- reference docs: `references/agent-traces.md`, `references/configuration.md`, `references/framework-extensions.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/microsoft/skills:applicationinsights-web-ts`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/skills/applicationinsights-web-ts --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree ebcc58f8f6aac8011d8ad54ec8fa9728a7f249f986a7a21d9c6d8b859e3ade67 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
