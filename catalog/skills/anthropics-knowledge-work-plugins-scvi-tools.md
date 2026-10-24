# scvi-tools

> Deep learning for single-cell analysis using scvi-tools. This skill should be used when users need (1) data integration and batch correction with scVI/scANVI, (2) ATAC-seq analysis with PeakVI, (3) CITE-seq multi-modal analysis with totalVI, (4) multiome RNA+ATAC analysis with MultiVI, (5) spatial transcriptomics deconvolution with DestVI, (6) label transfer and reference mapping with scANVI/scArches, (7) RNA velocity with veloVI, or (8) any deep learning-based single-cell method. Triggers include mentions of scVI, scANVI, totalVI, PeakVI, MultiVI, DestVI, veloVI, sysVI, scArches, variational autoencoder, VAE, batch correction, data integration, multi-modal, CITE-seq, multiome, reference mapping, latent space.

| | |
|---|---|
| **ID** | `anthropics/knowledge-work-plugins:scvi-tools` |
| **Pack** | Research & Learning |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 156 lines in SKILL.md, 22 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> This skill provides guidance for deep learning-based single-cell analysis using scvi-tools, the leading framework for probabilistic models in single-cell genomics.

## How it is structured

The skill's own section headings, in order:

- How to Use This Skill
- When to Use This Skill
- Model Selection Guide
- Workflow Reference Files
- CLI Scripts
  - Pipeline Scripts
  - Example Workflow
  - Python Utilities
- Critical Requirements
- Quick Decision Tree
- Key Resources

## What it bundles

- scripts: `scripts/cluster_embed.py`, `scripts/differential_expression.py`, `scripts/integrate_datasets.py`, `scripts/model_utils.py`, `scripts/prepare_data.py`, `scripts/train_model.py`, `scripts/transfer_labels.py`, `scripts/validate_adata.py`
- reference docs: `references/atac_peakvi.md`, `references/batch_correction_sysvi.md`, `references/citeseq_totalvi.md`, `references/data_preparation.md`, `references/environment_setup.md`, `references/label_transfer.md`, `references/multiome_multivi.md`, `references/rna_velocity_velovi.md` ...
- 1 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [anthropics/knowledge-work-plugins:single-cell-rna-qc](anthropics-knowledge-work-plugins-single-cell-rna-qc.md) - Performs quality control on single-cell RNA-seq data (.h5ad or .h5 files) using scverse best practices with MA

## Invoke / install

- Invoke: `/anthropics/knowledge-work-plugins:scvi-tools`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/knowledge-work-plugins --path bio-research/skills/scvi-tools --commit 33d3dea41a341b341d4f5da2e8801ae0c89be2b8 --expect-tree d0c85df195b0e52b0c532958e0825cfb6842d7c1866cd87baa9bb3b2b3818bba --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
