# pytorch-patterns

> PyTorch deep learning patterns and best practices for building robust, efficient, and reproducible training pipelines, model architectures, and data loading. Use when writing or reviewing PyTorch training loops, model architectures, or data loading, or when a run will not reproduce.

| | |
|---|---|
| **ID** | `affaan-m/ECC:pytorch-patterns` |
| **Pack** | AI / ML Engineering |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 398 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when writing or reviewing PyTorch training loops, model architectures, or data loading, or when a run will not reproduce.

## What it says up front

> Idiomatic PyTorch patterns and best practices for building robust, efficient, and reproducible deep learning applications.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Core Principles
  - 1. Device-Agnostic Code
  - 2. Reproducibility First
  - 3. Explicit Shape Management
- Model Architecture Patterns
  - Clean nn.Module Structure
  - Proper Weight Initialization
- Training Loop Patterns
  - Standard Training Loop
  - Validation Loop
- Data Pipeline Patterns
  - Custom Dataset
  - Efficient DataLoader Configuration
  - Custom Collate for Variable-Length Data
- Checkpointing Patterns
  - Save and Load Checkpoints
- Performance Optimization
  - Mixed Precision Training
  - Gradient Checkpointing for Large Models
  - torch.compile for Speed
- Quick Reference: PyTorch Idioms
- Anti-Patterns to Avoid

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:golang-patterns](affaan-m-ecc-golang-patterns.md) - Idiomatic Go patterns, best practices, and conventions for building robust, efficient, and maintainable Go app
- [affaan-m/ECC:perl-patterns](affaan-m-ecc-perl-patterns.md) - Modern Perl 5.36+ idioms, best practices, and conventions for building robust, maintainable Perl applications.
- [affaan-m/ECC:kotlin-patterns](affaan-m-ecc-kotlin-patterns.md) - Idiomatic Kotlin patterns, best practices, and conventions for building robust, efficient, and maintainable Ko
- [affaan-m/ECC:python-patterns](affaan-m-ecc-python-patterns.md) - Pythonic idioms, PEP 8 standards, type hints, and best practices for building robust, efficient, and maintaina

## Invoke / install

- Invoke: `/affaan-m/ECC:pytorch-patterns`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/pytorch-patterns --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 3094be52449eac16174b888101f6ce38cc64bf8949678c6e6dce8249859d1984 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
