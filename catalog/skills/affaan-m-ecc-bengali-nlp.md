# bengali-nlp

> Bengali (Bangla) text processing patterns including Unicode normalization, script detection, tokenization, conjunct handling, and Bangla-specific NLP best practices for AI applications.

| | |
|---|---|
| **ID** | `affaan-m/ECC:bengali-nlp` |
| **Pack** | Operations & Business |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 463 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Best practices for processing, storing, and displaying Bengali text in software applications and AI systems.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Bengali Unicode and Script Handling
  - Unicode Range
  - Normalization
  - Conjunct Consonants (যুক্তবর্ণ)
  - Bengali Digits
- Tokenization
  - Word Boundary Detection
  - Using bnlp Toolkit
  - Handling Postpositions and Case Markers
- Text Processing Patterns
  - Script Detection
  - Stop Words
  - Sorting and Collation
  - Search with Normalization
- Bengali in AI/LLM Applications
  - Prompt Engineering for Bengali
  - Handling Banglish (Mixed Bengali-English)
  - Dataset Preparation
- Database and Storage
- Common Anti-Patterns
  - Don't: Split on Code Points for Display Length
  - Don't: Skip Normalization Before Comparison
  - Don't: Assume `isdigit()` Means ASCII
  - Don't: Use ASCII Transliteration When Unicode Is Available
  - Don't: Ignore Zero-Width Characters in Web-Scraped Text
- Best Practices
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:rust-patterns](affaan-m-ecc-rust-patterns.md) - Idiomatic Rust patterns, ownership, error handling, traits, concurrency, and best practices for building safe,
- [affaan-m/ECC:perl-patterns](affaan-m-ecc-perl-patterns.md) - Modern Perl 5.36+ idioms, best practices, and conventions for building robust, maintainable Perl applications.
- [affaan-m/ECC:golang-patterns](affaan-m-ecc-golang-patterns.md) - Idiomatic Go patterns, best practices, and conventions for building robust, efficient, and maintainable Go app
- [affaan-m/ECC:dotnet-patterns](affaan-m-ecc-dotnet-patterns.md) - Idiomatic C# and .NET patterns, conventions, dependency injection, async/await, and best practices for buildin

## Invoke / install

- Invoke: `/affaan-m/ECC:bengali-nlp`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/bengali-nlp --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree eff93243abd8d8919b74856d105507c63a9513bc094884a58a7b8d0efe435d52 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
