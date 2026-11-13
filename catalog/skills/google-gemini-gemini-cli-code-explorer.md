# code_explorer

> Explores the repository to locate primary source files, coupled UI components, and test files for bug reports or feature requests.

| | |
|---|---|
| **ID** | `google-gemini/gemini-cli:code_explorer` |
| **Pack** | Software Development (also: Web, Frontend & UI Design, Research & Learning) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| **License** | Apache-2.0 |
| **Size** | 34 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Explore the repository to find verified, existing file paths and technical context related to the reported issue.

## How it is structured

The skill's own section headings, in order:

  - Phase 1: Root Exploration & Related Area Discovery
  - Phase 2: Directed Code Exploration & Traversal
  - Phase 3: Test Applicability & Pattern Check
  - Output Format:

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [bm:code-review](bm-code-review.md) - Review source files changed during a phase for bugs, security issues, and code quality problems
- [reverse-engineer-anything](reverse-engineer-anything.md) - Reverse engineer native, managed, Electron/JavaScript, packaged, firmware, and browser targets with REA. Use s
- [affaan-m/ECC:springboot-tdd](affaan-m-ecc-springboot-tdd.md) - Test-driven development for Spring Boot using JUnit 5, Mockito, MockMvc, Testcontainers, and JaCoCo. Use when 
- [affaan-m/ECC:swift-protocol-di-testing](affaan-m-ecc-swift-protocol-di-testing.md) - Protocol-based dependency injection for testable Swift code — mock file system, network, and external APIs usi

## Invoke / install

- Invoke: `/google-gemini/gemini-cli:code_explorer`
- Install: `python skills/skill-vetter/scripts/install.py google-gemini/gemini-cli --path tools/caretaker-agent/cloudrun/triage-worker/.gemini/skills/code_explorer --commit b9776560ea5710bc673891499aaec68c737d160a --expect-tree 25707ef84500db2c8231ae345d3676eb61dddebfd474bf5e635f3866f8d89f34 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
