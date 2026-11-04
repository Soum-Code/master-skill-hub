# recsys-pipeline-architect

> Design composable recommendation, ranking, and feed pipelines using the six-stage Source→Hydrator→Filter→Scorer→Selector→SideEffect framework popularized by xAI's open-sourced For You algorithm. Use this skill whenever the user is building any system that picks "the top K items for a (user, context)" — social feeds, content CMSs, RAG rerankers, task prioritizers, notification triage, search reranking, ad ranking.

| | |
|---|---|
| **ID** | `affaan-m/ECC:recsys-pipeline-architect` |
| **Pack** | MLOps / DevOps / Cloud (also: Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 116 lines in SKILL.md, 1 file(s) |

## When to use it

- Use this skill whenever the user is building any system that picks "the top K items for a (user, context)" — social feeds, content CMSs, RAG rerankers, task prioritizers, notification triage, search reranking, ad ranking.

## What it says up front

> A spec-and-scaffold skill for building composable recommendation, ranking, and feed pipelines. It encodes the **six-stage pattern** — Source → Hydrator → Filter → Scorer → Selector → SideEffect — popularized by xAI's open-sourced [For You algorithm](https://github.com/xai-org/x-algorithm) (Apache 2.

## How it is structured

The skill's own section headings, in order:

- When to Use
- When NOT to Use
- The six-stage framework
  - Why this exact order
- Workflow when invoked
- Key trade-offs to surface (don't default silently)
  - 1. Single score vs multi-action prediction
  - 2. Candidate isolation in scoring
  - 3. Online vs offline
- Hard rules
- Anti-Patterns
- Upstream contents

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/affaan-m/ECC:recsys-pipeline-architect`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/recsys-pipeline-architect --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 7f3de8bfe75774ee15994f1210f880715ae490f398d7670fa7bd6d9dddbfbb97 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
