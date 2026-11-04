# perl-patterns

> Modern Perl 5.36+ idioms, best practices, and conventions for building robust, maintainable Perl applications. Use when writing or reviewing modern Perl 5.36+ code.

| | |
|---|---|
| **ID** | `affaan-m/ECC:perl-patterns` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 506 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when writing or reviewing modern Perl 5.36+ code.

## What it says up front

> Idiomatic Perl 5.36+ patterns and best practices for building robust, maintainable applications.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- How It Works
- Core Principles
  - 1. Use `v5.36` Pragma
  - 2. Subroutine Signatures
  - 3. Context Sensitivity
  - 4. Postfix Dereferencing
  - 5. The `isa` Operator (5.32+)
- Error Handling
  - eval/die Pattern
  - Try::Tiny (Reliable Exception Handling)
  - Native try/catch (5.40+)
- Modern OO with Moo
  - Moo Roles
  - Native `class` Keyword (5.38+, Corinna)
- Regular Expressions
  - Named Captures and `/x` Flag
  - Precompiled Patterns
- Data Structures
  - References and Safe Deep Access
- File I/O
  - Three-Argument Open
  - Path::Tiny for File Operations
- Module Organization
  - Standard Project Layout
  - Exporter Patterns
- Tooling
  - perltidy Configuration (.perltidyrc)
  - perlcritic Configuration (.perlcriticrc)
  - Dependency Management (cpanfile + carton)

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:golang-patterns](affaan-m-ecc-golang-patterns.md) - Idiomatic Go patterns, best practices, and conventions for building robust, efficient, and maintainable Go app
- [affaan-m/ECC:kotlin-patterns](affaan-m-ecc-kotlin-patterns.md) - Idiomatic Kotlin patterns, best practices, and conventions for building robust, efficient, and maintainable Ko
- [affaan-m/ECC:python-patterns](affaan-m-ecc-python-patterns.md) - Pythonic idioms, PEP 8 standards, type hints, and best practices for building robust, efficient, and maintaina
- [affaan-m/ECC:dotnet-patterns](affaan-m-ecc-dotnet-patterns.md) - Idiomatic C# and .NET patterns, conventions, dependency injection, async/await, and best practices for buildin

## Invoke / install

- Invoke: `/affaan-m/ECC:perl-patterns`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/perl-patterns --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 1ccb383e7619522d9f8867f8f2593e6781ac382b4bf08a150039f632ea8c0815 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
