# data-scraper-agent

> Build a fully automated AI-powered data collection agent for any public source — job boards, prices, news, GitHub, sports, anything. Runs on a schedule, enriches data with a free LLM (Gemini Flash), stores results in Notion/Sheets/Supabase, and learns from user feedback. Runs 100% free on GitHub Actions. Use when the user wants to monitor, collect, or track any public data automatically.

| | |
|---|---|
| **ID** | `affaan-m/ECC:data-scraper-agent` |
| **Pack** | AI / ML Engineering (also: Data & Analytics, MLOps / DevOps / Cloud) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 777 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user wants to monitor, collect, or track any public data automatically.

## What it says up front

> Build a production-ready, AI-powered data collection agent for any public data source. Runs on a schedule, enriches results with a free LLM, stores to a database, and improves over time.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Core Concepts
  - The Three Layers
  - Free Stack
  - AI Model Fallback Chain
  - Batch API Calls for Efficiency
- Untrusted Scraped Data
- Workflow
  - Step 1: Understand the Goal
  - Step 2: Design the Collection Architecture
  - Step 3: Build the Source Connector
  - Step 4: Build the Gemini AI Client
  - Step 5: Build the AI Pipeline (Batch)
  - Step 6: Build the Feedback Learning System
  - Step 7: Build Storage (Notion example)
  - Step 8: Orchestrate in main.py
  - Step 9: GitHub Actions Workflow
  - Step 10: config.yaml Template
- Common Scraping Patterns
  - Pattern 1: REST API (easiest)
  - Pattern 2: HTML Scraping
  - Pattern 3: RSS Feed
  - Pattern 4: Paginated API
  - Pattern 5: JS-Rendered Pages (Playwright)
- Anti-Patterns to Avoid
- Free Tier Limits Reference
- Requirements Template
- Quality Checklist
- Real-World Examples
- Reference Implementation

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/affaan-m/ECC:data-scraper-agent`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/data-scraper-agent --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 952ad3126726786b2eae94f2646cbd43d57e36ccce4445815c3cd0388ef583cb --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
