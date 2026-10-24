# Operations

## What runs where

| Job | Trigger | Needs |
|---|---|---|
| `CI` | push, PR | nothing |
| `Weekly discovery` | Mondays 03:17 UTC and manual | nothing (optional secrets below) |
| `Promote candidate` | manual | repo write access |
| `Submitted skill or request` | issue opened with `submit-skill` / `skill-request` label by a collaborator | nothing |
| `Pages` | called by the weekly job | Pages enabled with "GitHub Actions" as source |

Everything runs on GitHub's runners, so it is independent of your PC.

## Keeping the schedule alive

GitHub switches off scheduled workflows in a public repository after 60 days without repository activity. The weekly job commits `registry/last-run.json` every run, and Dependabot opens action-update PRs, so there is always activity. If a run is ever missed, check **Actions** and use **Run workflow** on *Weekly discovery*.

## Secrets (all optional)

Add under *Settings, Secrets and variables, Actions*. The hub never needs you to paste a secret into chat or a file.

| Secret | Unlocks | Cost |
|---|---|---|
| none | GitHub, Hacker News, dev.to, Lobsters, Mastodon, npm, awesome-lists, issues, free AI second opinion (GitHub Models via the built-in token) | free |
| `ANTHROPIC_API_KEY` | Claude as the second-opinion reviewer instead of GitHub Models | paid per token |
| `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET` | Reddit. Anonymous Reddit access is blocked from cloud IPs, and new API apps need Reddit's approval, so without these the Reddit source reports `blocked` and the run continues | free if approved |
| `BSKY_HANDLE`, `BSKY_APP_PASSWORD` | Bluesky search (create an *app password* in Bluesky settings; never your main password) | free |
| `YOUTUBE_API_KEY` | YouTube search for video descriptions with GitHub links | free quota |

**Using your Claude subscription instead of an API key:** run `claude setup-token` locally and store the result as `CLAUDE_CODE_OAUTH_TOKEN`; this works with Anthropic's `claude-code-action`. The shipped workflows do not need it, so it is not wired in; add it if you want Claude-written summaries.

## Why not Instagram

Instagram has no public search API. The Graph API only exposes accounts you own, and scraping logged-in pages breaks its terms and your account. Instead: when you see a skill in a reel or post, open a **Submit a skill** issue with the GitHub link. It goes through the same vetting as everything else.

## Approving a candidate

The weekly issue lists candidates with a ready-to-run line. Either:

- Actions, *Promote candidate*, Run workflow, paste the id; or
- `python -m skillhub promote owner/repo:skill` locally, commit the result.

`REVIEW` verdicts need `--accept-review` after you have read the findings. `FAIL` verdicts need `--override-fail <rule,rule>` and are recorded in the registry.

## Installing a verified external skill

```bash
python skills/skill-vetter/scripts/install.py owner/repo --path skills/x --commit <sha> --expect-tree <sha256>          # dry run
python skills/skill-vetter/scripts/install.py owner/repo --path skills/x --commit <sha> --expect-tree <sha256> --apply
```

## Changing what it hunts for

- `registry/packs.yml`: industries and roles, their keywords and weekly search queries.
- `registry/sources.yml`: trusted owners, watchlist, awesome-lists, topics, per-source settings.
- `registry/profiles.yml`: which packs a role cares about (also drives candidate ranking).
- `registry/chains.yml`: multi-skill workflows.
- `registry/overrides.yml`: manual pack corrections.

## Limitations and what was done instead

| Limitation | Approach |
|---|---|
| One file with all skills would flood the context | Router with a compact index; the full skill loads only when invoked |
| Auto-installing third-party skills is risky | Always vet, pin the commit, hash-check; auto-verify only trusted owners on a clean vet; humans promote the rest; installs are dry-run by default |
| Instagram cannot be searched | Submit-a-skill issue template for anything seen on any platform; ten other sources |
| claude.ai cannot install skills by API | Weekly-refreshed zips on a rolling release; optional connector in [CLAUDE-AI.md](CLAUDE-AI.md) |
| API keys cost money | Free GitHub Models via the Actions token; subscription token or API key optional |
| Licences vary | Only metadata, links and pinned commits are stored; summary text is kept only for permissively licensed skills |
