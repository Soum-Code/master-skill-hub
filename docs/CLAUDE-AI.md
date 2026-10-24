# Using the hub in claude.ai

## Skills (works today)

1. Open the [latest release](https://github.com/Soum-Code/master-skill-hub/releases/tag/latest) and download `master-skill.zip`. Add `skill-vetter.zip`, `job-search-copilot.zip`, `ml-interview-prep.zip` if you want them.
2. In claude.ai: **Settings, Capabilities, Skills, Upload skill**. Custom skills need a paid plan with code execution enabled; they belong to your account, not to an organisation.

What to expect:

- The router script needs code execution. With it off, the skill falls back to the bundled `references/index.md` and `references/packs/*.md`, which Claude reads like any other file.
- claude.ai does not know which skills you have installed elsewhere, so the router recommends from the catalog and does not mark anything "installed here".
- The zips are rebuilt weekly. claude.ai offers no API to update an uploaded skill, so re-uploading a newer zip is manual. The registry inside the zip is a snapshot; the catalog on GitHub is always current.

## Optional: a connector that is always current

A small read-only MCP server can serve the live registry to claude.ai (custom connector) and to Claude Code. It exposes `search_skills`, `get_skill` and `list_packs`, and carries the same sanitised registry as the router. See `connector/` if present in this repo. It is optional because it needs a public endpoint; the zip route needs nothing.
