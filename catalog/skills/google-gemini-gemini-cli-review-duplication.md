# review-duplication

> Use this skill during code reviews to proactively investigate the codebase for duplicated functionality, reinvented wheels, or failure to reuse existing project best practices and shared utilities.

| | |
|---|---|
| **ID** | `google-gemini/gemini-cli:review-duplication` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| **License** | Apache-2.0 |
| **Size** | 70 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> This skill provides a structured workflow for investigating a codebase during a code review to identify duplicated logic, reinvented utilities, and missed opportunities to reuse established patterns. By executing this workflow, you ensure that new code integrates seamlessly with the existing project

## How it is structured

The skill's own section headings, in order:

- Overview
- Workflow: Investigating for Duplication
  - 1. Extract Core Logic
  - 2. Hypothesize Existing Locations & Trace Dependencies
  - 3. Investigate the Codebase (Sub-Agent Delegation)
  - 4. Evaluate Best Practices
  - 5. Formulate Constructive Feedback

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:vue-patterns](affaan-m-ecc-vue-patterns.md) - Vue.js 3 Composition API patterns, component architecture, reactivity best practices, Pinia state management, 
- [affaan-m/ECC:csharp-testing](affaan-m-ecc-csharp-testing.md) - C# and .NET testing patterns with xUnit, FluentAssertions, mocking, integration tests, and test organization b
- [affaan-m/ECC:perl-patterns](affaan-m-ecc-perl-patterns.md) - Modern Perl 5.36+ idioms, best practices, and conventions for building robust, maintainable Perl applications.
- [affaan-m/ECC:golang-patterns](affaan-m-ecc-golang-patterns.md) - Idiomatic Go patterns, best practices, and conventions for building robust, efficient, and maintainable Go app

## Invoke / install

- Invoke: `/google-gemini/gemini-cli:review-duplication`
- Install: `python skills/skill-vetter/scripts/install.py google-gemini/gemini-cli --path .gemini/skills/review-duplication --commit 62bab5b232c15b925d31e655ce844ab939c882b7 --expect-tree 50fae3137e910b9bcf1ae589a7f63a7f94fc140ab7991be7d3530199d8b5b229 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
