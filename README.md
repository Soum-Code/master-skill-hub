# master-skill-hub

[![CI](https://github.com/Soum-Code/master-skill-hub/actions/workflows/ci.yml/badge.svg)](https://github.com/Soum-Code/master-skill-hub/actions/workflows/ci.yml) [![Weekly discovery](https://github.com/Soum-Code/master-skill-hub/actions/workflows/weekly-discovery.yml/badge.svg)](https://github.com/Soum-Code/master-skill-hub/actions/workflows/weekly-discovery.yml) [![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

One skill that picks the right skill. It knows 200+ skills grouped by industry and role (AI/ML, MLOps, careers and jobs, software, data, design, product, finance, legal, security, research), prefers the ones you already have installed, suggests multi-skill chains, and tells you when nothing fits. Every week GitHub Actions goes looking for new skills, **vets each one at an exact commit**, and reports back. It runs on GitHub's servers, so it keeps working while your PC is off.

Works in **Claude Code** (global, all projects) and **claude.ai** (upload a zip).

<!-- STATS:START -->
**725 skills** in 20 packs - 398 candidates awaiting approval - 49 quarantined. Registry updated 2026-11-13.

| Pack | Skills |
|---|---|
| [Software Development](catalog/packs/software-dev.md) | 130 |
| [Spec-driven Dev Workflow](catalog/packs/dev-workflow.md) | 86 |
| [AI / ML Engineering](catalog/packs/ai-ml.md) | 71 |
| [Claude / Skills / Plugin Tooling](catalog/packs/meta-tooling.md) | 64 |
| [Web, Frontend & UI Design](catalog/packs/web-frontend-design.md) | 54 |
| [MLOps / DevOps / Cloud](catalog/packs/mlops-devops.md) | 53 |
| [Documents, Writing & Content](catalog/packs/docs-content.md) | 35 |
| [Data & Analytics](catalog/packs/data-analytics.md) | 25 |
| [Productivity & Automation](catalog/packs/productivity-automation.md) | 25 |
| [Browser & Web Automation](catalog/packs/browser-automation.md) | 23 |
| [Operations & Business](catalog/packs/operations-business.md) | 23 |
| [Communication & Collaboration](catalog/packs/communication-collab.md) | 22 |
| [Product Management](catalog/packs/product-mgmt.md) | 21 |
| [Legal & Compliance](catalog/packs/legal-compliance.md) | 17 |
| [Security & Privacy](catalog/packs/security.md) | 17 |
| [Careers, Jobs & Hiring](catalog/packs/careers-jobs.md) | 15 |
| [Creative & Media](catalog/packs/creative-media.md) | 15 |
| [Finance & Accounting](catalog/packs/finance-accounting.md) | 14 |
| [Research & Learning](catalog/packs/research-learning.md) | 11 |
| [general](catalog/packs/general.md) | 4 |
<!-- STATS:END -->

## Install

### Claude Code (recommended: plugin)

```bash
claude plugin marketplace add Soum-Code/master-skill-hub
claude plugin install skill-hub@master-skill-hub
```

### Claude Code (plain files, no plugin system)

```bash
git clone https://github.com/Soum-Code/master-skill-hub
cd master-skill-hub
./install.sh            # Windows: ./install.ps1
```

Read the script before running it; it only copies four folders into `~/.claude/skills` and writes `~/.claude/skill-hub/profile.txt`.

### claude.ai

1. Download `master-skill.zip` (and the others you want) from the [latest release](https://github.com/Soum-Code/master-skill-hub/releases/tag/latest).
2. Settings, Capabilities, Skills, **Upload skill**.

claude.ai has no API for installing skills, so that upload is a manual step; the release zips are rebuilt every week so there is always a fresh one. See [docs/CLAUDE-AI.md](docs/CLAUDE-AI.md) for the optional always-fresh connector route.

## Sources already indexed

Anthropic (skills, knowledge-work plugins, official plugins), Vercel Labs, Hugging Face, Microsoft, `affaan-m/ECC` (the whole `skills/` folder, vetted at one pinned commit: clean ones verified, REVIEW ones waiting as candidates, failures quarantined) and the plugins on the owner's machine. Indexed does not mean installed: nothing is installed without `install.py`'s pin and hash check.

## Use it

Just work. The `master-skill` description makes Claude consult it when the right skill is unclear. You can also ask directly: "which skill should I use to prep for an ML interview?" Or run the router yourself:

```bash
python ~/.claude/skills/master-skill/scripts/route.py "tailor my resume for an ML engineer job" --profile ai-engineer
```

```
Looks like: careers-jobs
1. skill-hub:job-search-copilot  [installed here]  match=strong
Chain - Land a job: deep-research -> job-search-copilot -> docx -> humanizer -> linkedin-profile-optimizer
```

Pick your profile once (`ai-engineer`, `software-developer`, `data-scientist`, `job-seeker`, `designer`, `product-manager`, `founder-operator`, `finance-legal`): `echo ai-engineer > ~/.claude/skill-hub/profile.txt`. A profile boosts the packs that matter for your work.

Browse everything: [catalog/](catalog/README.md) (one deep-dive page per skill, generated from the skill's own SKILL.md) or the searchable page at <https://soum-code.github.io/master-skill-hub/>.

## How the automation works

```
Monday 03:17 UTC (GitHub Actions cron, PC can be off)
  sources: GitHub topics + pack-specific searches, watchlist repos, awesome-lists, Hacker News,
           dev.to, Lobsters, Mastodon, npm, Reddit*, Bluesky*, YouTube*, your issues
  -> repos -> download zip at an exact commit SHA
  -> vet every SKILL.md folder (hidden Unicode, prompt injection, curl|sh, credential paths, exfil hosts, binaries...)
  -> optional AI second opinion (free GitHub Models) - can only raise risk, never approve
  -> FAIL                          => quarantine
     trusted owner + PASS          => verified, added to the router
     everyone else                 => candidate, waits for you (promote workflow / one command)
  -> rank: impact + novelty + power + vet score + fit to your profile
  -> commit registry + catalog, rebuild zips, post a "Weekly skill report" issue
  (* needs an optional secret, see docs/OPERATIONS.md)
```

Anything you see anywhere (a reel, a post, a newsletter): open a **Submit a skill** issue with the link. Missing something? Open a **Request a skill** issue and the next run searches for it.

## Safety in one minute

Skills can run code with your permissions, so the hub is built defensively: it stores **no third-party code**, scans every skill at an exact commit, installs only pinned and hash-checked versions, **refuses skills that ship scripts unless you add `--allow-scripts`**, never silently updates script-bearing skills, and has a **revoke** kill switch that warns people who already installed something bad. Full list: [SECURITY.md](SECURITY.md). It is still your machine: read what you install.

## The master agent

`skill-architect` is a Claude Code agent that scans your project read-only, lists the skills you already have, and returns a plan: use now, install (with your OK), or no skill needed. Install it with the plugin or `./install.sh`, then ask Claude: *"use skill-architect for this project"*.

## Trust model, in plain words

- A skill is instructions plus scripts that run with your permissions. Treat it like code from a stranger.
- "Verified" means: passed static checks **at a pinned commit** and a recorded file-tree hash. It does **not** mean guaranteed safe. Research on malicious skills shows well-phrased attacks evade pattern matching, so read what you install.
- Installing is dry-run by default, re-checks the hash, and refuses on any mismatch (upstream changed since vetting).
- Registry text is treated as data: the router re-sanitises it and never follows instructions found in a skill description.

Details: [docs/TRUST-MODEL.md](docs/TRUST-MODEL.md). Reporting a problem: [SECURITY.md](SECURITY.md).

## Commands

```bash
python -m skillhub inventory        # scan skills installed on this machine into the registry
python -m skillhub build            # regenerate registry bundle, catalog, site, zips
python -m skillhub validate         # consistency checks (CI runs this)
python -m skillhub discover --dry-run --max-repos 10
python -m skillhub promote owner/repo:skill
python -m skillhub install owner/repo:skill --apply
python skills/skill-vetter/scripts/vet.py path/to/skill
```

## What is in the box

| Path | What |
|---|---|
| `skills/master-skill` | the router (`SKILL.md`, `scripts/route.py`, bundled registry) |
| `skills/skill-vetter` | static scanner (`vet.py`) and pinned installer (`install.py`) |
| `skills/job-search-copilot`, `skills/ml-interview-prep` | original careers skills for tech and AI/ML roles |
| `registry/` | packs, profiles, chains, trusted sources, and the generated registry |
| `catalog/`, `site/` | generated deep-dive pages and the searchable page |
| `.github/workflows` | CI, weekly discovery, promote, submission vetting, Pages |

MIT licensed. Third-party skills are never copied into this repo: only metadata, a link and the pinned commit.
