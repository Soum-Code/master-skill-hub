# single-cell-rna-qc

> Performs quality control on single-cell RNA-seq data (.h5ad or .h5 files) using scverse best practices with MAD-based filtering and comprehensive visualizations. Use when users request QC analysis, filtering low-quality cells, assessing data quality, or following scverse/scanpy best practices for single-cell analysis.

| | |
|---|---|
| **ID** | `anthropics/knowledge-work-plugins:single-cell-rna-qc` |
| **Pack** | Data & Analytics |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 176 lines in SKILL.md, 6 file(s) |

## When to use it

- Use when users request QC analysis, filtering low-quality cells, assessing data quality, or following scverse/scanpy best practices for single-cell analysis.

## What it says up front

> Automated QC workflow for single-cell RNA-seq data following scverse best practices.

## How it is structured

The skill's own section headings, in order:

- When to Use This Skill
- Approach 1: Complete QC Pipeline (Recommended for Standard Workflows)
  - Workflow Steps
- Approach 2: Modular Building Blocks (For Custom Workflows)
- Best Practices
- Reference Materials
- Next Steps After QC

## What it bundles

- scripts: `scripts/qc_analysis.py`, `scripts/qc_core.py`, `scripts/qc_plotting.py`
- reference docs: `references/scverse_qc_guidelines.md`
- 1 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [anthropics/knowledge-work-plugins:scvi-tools](anthropics-knowledge-work-plugins-scvi-tools.md) - Deep learning for single-cell analysis using scvi-tools. This skill should be used when users need (1) data in

## Invoke / install

- Invoke: `/anthropics/knowledge-work-plugins:single-cell-rna-qc`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/knowledge-work-plugins --path bio-research/skills/single-cell-rna-qc --commit 33d3dea41a341b341d4f5da2e8801ae0c89be2b8 --expect-tree d4855c2c266ef2dcb1b489574273eaa06abf84a5ee7a9dbc9f04d86832b253ed --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
