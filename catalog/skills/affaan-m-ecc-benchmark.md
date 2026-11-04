# benchmark

> Measure performance baselines and detect regressions across browser Core Web Vitals (LCP, INP, CLS, page weight), API endpoint latency percentiles, and build/test feedback times, with before/after comparison stored in git-tracked .ecc/benchmarks JSON. Use when checking page speed, responding to 'it feels slow' reports, verifying launch performance targets, or comparing stack alternatives.

| | |
|---|---|
| **ID** | `affaan-m/ECC:benchmark` |
| **Pack** | AI / ML Engineering (also: Software Development, Browser & Web Automation) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 96 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when checking page speed, responding to 'it feels slow' reports, verifying launch performance targets, or comparing stack alternatives.

## What it says up front

> Measures real browser metrics via browser MCP:

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
  - Mode 1: Page Performance
  - Mode 2: API Performance
  - Mode 3: Build Performance
  - Mode 4: Before/After Comparison
- Output
- Integration

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:browser-qa](affaan-m-ecc-browser-qa.md) - Run automated post-deploy UI verification with a browser automation MCP (claude-in-chrome, Playwright, or Pupp
- [affaan-m/ECC:verification-loop](affaan-m-ecc-verification-loop.md) - Run a six-phase verification of a Claude Code session's work — build, type check, lint, tests with coverage, s

## Invoke / install

- Invoke: `/affaan-m/ECC:benchmark`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/benchmark --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 76cdd69cdf2bc97350b92df3b0d3e73d46d8494df8550d70d5c4a831332b4b20 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
