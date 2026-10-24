# huggingface-papers

> Look up and read Hugging Face paper pages in markdown, and use the papers API for structured metadata such as authors, linked models/datasets/spaces, Github repo and project page. Use when the user shares a Hugging Face paper page URL, an arXiv URL or ID, or asks to summarize, explain, or analyze an AI research paper.

| | |
|---|---|
| **ID** | `huggingface/skills:huggingface-papers` |
| **Pack** | Research & Learning (also: AI / ML Engineering) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [huggingface/skills](https://github.com/huggingface/skills) |
| **License** | Apache-2.0 |
| **Size** | 239 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user shares a Hugging Face paper page URL, an arXiv URL or ID, or asks to summarize, explain, or analyze an AI research paper.

## What it says up front

> Hugging Face Paper pages (hf.co/papers) is a platform built on top of arXiv (arxiv.org), specifically for research papers in the field of artificial intelligence (AI) and computer science. Hugging Face users can submit their paper at hf.co/papers/submit, which features it on the Daily Papers feed (h

## How it is structured

The skill's own section headings, in order:

- When to Use
- Parsing the paper ID
  - Fetch the paper page as markdown
  - Paper Pages API Endpoints
- Error Handling
  - Fallbacks
- Notes

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [huggingface/skills:huggingface-paper-publisher](huggingface-skills-huggingface-paper-publisher.md) - Publish and manage research papers on Hugging Face Hub. Supports creating paper pages, linking papers to model
- [huggingface/skills:hf-mcp](huggingface-skills-hf-mcp.md) - Use Hugging Face Hub via MCP server tools. Search models, datasets, Spaces, papers. Get repo details, fetch do
- [huggingface/skills:huggingface-datasets](huggingface-skills-huggingface-datasets.md) - Use this skill for Hugging Face Dataset Viewer API workflows that fetch subset/split metadata, paginate rows, 
- [openai/skills:netlify-deploy](openai-skills-netlify-deploy.md) - Deploy web projects to Netlify using the Netlify CLI (`npx netlify`). Use when the user asks to deploy, host, 

## Invoke / install

- Invoke: `/huggingface/skills:huggingface-papers`
- Install: `python skills/skill-vetter/scripts/install.py huggingface/skills --path skills/huggingface-papers --commit fabc634a893f62ad5c2039830397efa35fa62715 --expect-tree 2b35a6245d16186543d5f1c82e5e1d28197909f5bf61fb6d8da6668ff772614b --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
