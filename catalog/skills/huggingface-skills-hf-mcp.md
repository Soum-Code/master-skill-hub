# hf-mcp

> Use Hugging Face Hub via MCP server tools. Search models, datasets, Spaces, papers. Get repo details, fetch documentation, run compute jobs, and use Gradio Spaces as AI tools. Available when connected to the HF MCP server.

| | |
|---|---|
| **ID** | `huggingface/skills:hf-mcp` |
| **Pack** | AI / ML Engineering (also: Claude / Skills / Plugin Tooling) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [huggingface/skills](https://github.com/huggingface/skills) |
| **License** | Apache-2.0 |
| **Size** | 179 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Connect AI assistants to the Hugging Face Hub. Setup: https://huggingface.co/settings/mcp

## How it is structured

The skill's own section headings, in order:

- Use Cases & Examples
  - Find the Best Model for a Task
  - Compare Models from Different Providers
  - Find Training Datasets
  - Discover AI Tools (MCP Spaces)
  - Generate Images
  - Research a Topic
  - Learn How to Use a Library
  - Run a Quick GPU Job
  - Train a Model on Cloud GPU
  - Check Job Status
  - Explore What's Trending
  - Get Model Card Details
  - Find Quantized Models
  - Use a Gradio Space as a Tool
  - Schedule Recurring Jobs
- Tool Selection Guide
- Tips

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [huggingface/skills:huggingface-community-evals](huggingface-skills-huggingface-community-evals.md) - Run evaluations for Hugging Face Hub models using inspect-ai and lighteval on local hardware. Use for backend 
- [huggingface/skills:huggingface-papers](huggingface-skills-huggingface-papers.md) - Look up and read Hugging Face paper pages in markdown, and use the papers API for structured metadata such as 
- [huggingface/skills:huggingface-paper-publisher](huggingface-skills-huggingface-paper-publisher.md) - Publish and manage research papers on Hugging Face Hub. Supports creating paper pages, linking papers to model
- [huggingface/skills:hf-mem](huggingface-skills-hf-mem.md) - Hugging Face CLI to estimate the required memory to load Safetensors or GGUF model weights for inference from 

## Invoke / install

- Invoke: `/huggingface/skills:hf-mcp`
- Install: `python skills/skill-vetter/scripts/install.py huggingface/skills --path hf-mcp/skills/hf-mcp --commit fabc634a893f62ad5c2039830397efa35fa62715 --expect-tree 031a63abe84b82b41fa5fbdc9c9a324974217350752c7e6668f9c79bf4f475b9 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
