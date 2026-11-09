# critique

> Expertise in auditing and fixing repository scripts and GitHub Actions workflows to ensure technical robustness and security.

| | |
|---|---|
| **ID** | `google-gemini/gemini-cli:critique` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| **License** | Apache-2.0 |
| **Size** | 146 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Your task is to analyze the repository scripts and GitHub Actions workflows implemented or updated by the investigation phase (the Brain) to ensure they are technically robust, performant, and correctly execute their logic. You are responsible for applying fixes to the scripts if you detect any issu

## How it is structured

The skill's own section headings, in order:

- Critique Requirements
  - Technical Robustness
  - Logical & Workflow Integrity
  - Security & Payload Awareness
- Implementation Mandate
- Final Verdict & Logging

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [google-gemini/gemini-cli:metrics](google-gemini-gemini-cli-metrics.md) - Expertise in analyzing time-series repository health metrics, investigating root causes, and proposing proacti
- [google-gemini/gemini-cli:github-issue-creator](google-gemini-gemini-cli-github-issue-creator.md) - Use this skill when asked to create a GitHub issue. It handles different issue types (bug, feature, etc.) usin
- [google-gemini/gemini-cli:ci](google-gemini-gemini-cli-ci.md) - A specialized skill for Gemini CLI that provides high-performance, fail-fast monitoring of GitHub Actions work
- [bm:audit-fix](bm-audit-fix.md) - Autonomous audit-to-fix pipeline — find issues, classify, fix, test, commit

## Invoke / install

- Invoke: `/google-gemini/gemini-cli:critique`
- Install: `python skills/skill-vetter/scripts/install.py google-gemini/gemini-cli --path tools/gemini-cli-bot/.gemini/skills/critique --commit 62bab5b232c15b925d31e655ce844ab939c882b7 --expect-tree e4b84ffb18337ba81025b38d05d87acf8a318902e297b021394b460a1b4e2229 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
