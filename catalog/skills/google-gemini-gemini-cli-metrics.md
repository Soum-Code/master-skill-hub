# metrics

> Expertise in analyzing time-series repository health metrics, investigating root causes, and proposing proactive workflow improvements.

| | |
|---|---|
| **ID** | `google-gemini/gemini-cli:metrics` |
| **Pack** | Data & Analytics (also: Product Management) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| **License** | Apache-2.0 |
| **Size** | 113 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Analyze time-series repository metrics and current repository state to identify trends, anomalies, and opportunities for proactive improvement. You are empowered to formulate hypotheses, rigorously investigate root causes, and propose changes that safely improve repository health, productivity, and

## How it is structured

The skill's own section headings, in order:

- Goal
- Context
- Repo Policy Priorities
- LLM-Powered Classification
- Instructions
  - 1. Read & Identify Trends (Time-Series Analysis)
  - 2. Hypothesis Testing & Deep Dive
  - 3. Maintainer Workload Assessment
  - 4. Actor-Aware Bottleneck Identification
  - 5. Policy Critique & Evaluation
  - 6. Investigation Conclusion

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [google-gemini/gemini-cli:critique](google-gemini-gemini-cli-critique.md) - Expertise in auditing and fixing repository scripts and GitHub Actions workflows to ensure technical robustnes
- [anthropics/knowledge-work-plugins:analyze](anthropics-knowledge-work-plugins-analyze.md) - Answer data questions -- from quick lookups to full analyses. Use when looking up a single metric, investigati

## Invoke / install

- Invoke: `/google-gemini/gemini-cli:metrics`
- Install: `python skills/skill-vetter/scripts/install.py google-gemini/gemini-cli --path tools/gemini-cli-bot/.gemini/skills/metrics --commit b9776560ea5710bc673891499aaec68c737d160a --expect-tree 767601ca34e900d8c0bcb18e60f8fef3028c321975c05f698679f913edf3f58c --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
