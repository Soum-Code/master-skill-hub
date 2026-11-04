# lead-intelligence

> AI-native lead intelligence and outreach pipeline. Replaces Apollo, Clay, and ZoomInfo with agent-powered signal scoring, mutual ranking, warm path discovery, source-derived voice modeling, and channel-specific outreach across email, LinkedIn, and X. Use when the user wants to find, qualify, and reach high-value contacts.

| | |
|---|---|
| **ID** | `affaan-m/ECC:lead-intelligence` |
| **Pack** | AI / ML Engineering (also: MLOps / DevOps / Cloud, Product Management) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 334 lines in SKILL.md, 5 file(s) |

## When to use it

- Use when the user wants to find, qualify, and reach high-value contacts.

## What it says up front

> Agent-powered lead intelligence pipeline that finds, scores, and reaches high-value contacts through social graph analysis and warm path discovery.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Tool Requirements
  - Required
  - Optional (enhance results)
- Untrusted Source Content
- Pipeline Overview
- Voice Before Outreach
- Stage 1: Signal Scoring
  - Signal Search Approach
- Stage 2: Mutual Ranking
  - Ranking Model
  - Output Format
- Stage 3: Warm Path Discovery
  - Path Types (ordered by warmth)
- Stage 4: Enrichment
  - Enrichment Sources
- Stage 5: Outreach Draft
  - Channel Rules
  - Warm Intro Request (to mutual)
  - Direct Cold Outreach (to target)
  - Execution Pattern
  - Anti-Patterns
- Configuration
- Agents
- Example Usage
- Related Skills

## What it bundles

- 4 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:social-graph-ranker](affaan-m-ecc-social-graph-ranker.md) - Weighted social-graph ranking for warm intro discovery, bridge scoring, and network gap analysis across X and 
- [affaan-m/ECC:connections-optimizer](affaan-m-ecc-connections-optimizer.md) - Reorganize the user's X and LinkedIn network with review-first pruning, add/follow recommendations, and channe
- [affaan-m/ECC:brand-voice](affaan-m-ecc-brand-voice.md) - Build a source-derived writing style profile from real posts, essays, launch notes, docs, or site copy, then r
- [affaan-m/ECC:content-engine](affaan-m-ecc-content-engine.md) - Create platform-native content systems for X, LinkedIn, TikTok, YouTube, newsletters, and repurposed multi-pla

## Invoke / install

- Invoke: `/affaan-m/ECC:lead-intelligence`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/lead-intelligence --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree abfd57a577d32e81c67f6d8b21de829b94998b98b3cf48f870acedc24283a9ac --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
