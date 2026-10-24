# huggingface-paper-publisher

> Publish and manage research papers on Hugging Face Hub. Supports creating paper pages, linking papers to models/datasets, claiming authorship, and generating professional markdown-based research articles.

| | |
|---|---|
| **ID** | `huggingface/skills:huggingface-paper-publisher` |
| **Pack** | Research & Learning (also: AI / ML Engineering) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [huggingface/skills](https://github.com/huggingface/skills) |
| **License** | Apache-2.0 |
| **Size** | 625 lines in SKILL.md, 8 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> This skill provides comprehensive tools for AI engineers and researchers to publish, manage, and link research papers on the Hugging Face Hub. It streamlines the workflow from paper creation to publication, including integration with arXiv, model/dataset linking, and authorship management.

## How it is structured

The skill's own section headings, in order:

- Integration with HF Ecosystem
- 1. Paper Page Management
- 2. Link Papers to Artifacts
- 3. Research Article Creation
- 4. Metadata Management
  - Prerequisites
  - Method 1: Index Paper from arXiv
  - Method 2: Link Paper to Model/Dataset
  - Method 3: Claim Authorship
  - Method 4: Manage Paper Visibility
  - Method 5: Create Research Article
  - Paper Template Structure
  - Commands Reference
  - YAML Metadata Format
  - Integration Examples
  - Best Practices
  - Advanced Usage
  - Error Handling
  - Troubleshooting
  - Resources and References
  - Integration with tfrere's Research Template
  - Common Patterns
  - API Integration
  - Future Enhancements

## What it bundles

- scripts: `scripts/paper_manager.py`
- reference docs: `references/quick_reference.md`
- 5 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [huggingface/skills:huggingface-papers](huggingface-skills-huggingface-papers.md) - Look up and read Hugging Face paper pages in markdown, and use the papers API for structured metadata such as 
- [huggingface/skills:hf-mcp](huggingface-skills-hf-mcp.md) - Use Hugging Face Hub via MCP server tools. Search models, datasets, Spaces, papers. Get repo details, fetch do
- [huggingface/skills:hf-mem](huggingface-skills-hf-mem.md) - Hugging Face CLI to estimate the required memory to load Safetensors or GGUF model weights for inference from 
- [huggingface/skills:huggingface-community-evals](huggingface-skills-huggingface-community-evals.md) - Run evaluations for Hugging Face Hub models using inspect-ai and lighteval on local hardware. Use for backend 

## Invoke / install

- Invoke: `/huggingface/skills:huggingface-paper-publisher`
- Install: `python skills/skill-vetter/scripts/install.py huggingface/skills --path skills/huggingface-paper-publisher --commit fabc634a893f62ad5c2039830397efa35fa62715 --expect-tree 17f6f6d8f9a5fba40d88260e7800ed1974c2e4a6f9afff27f64a2d6c76a09878 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
