# social-publisher

> Agent-driven scheduling and publishing of social media posts across 13 platforms via SocialClaw. Use when the user wants to publish to X, LinkedIn, Instagram, Facebook Pages, TikTok, Discord, Telegram, YouTube, Reddit, WordPress, or Pinterest — or when managing campaigns, uploading media, or monitoring post delivery status.

| | |
|---|---|
| **ID** | `affaan-m/ECC:social-publisher` |
| **Pack** | Productivity & Automation (also: Documents, Writing & Content) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 145 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user wants to publish to X, LinkedIn, Instagram, Facebook Pages, TikTok, Discord, Telegram, YouTube, Reddit, WordPress, or Pinterest — or when managing campaigns, uploading media, or monitoring post delivery status.

## What it says up front

> Connects Claude Code to [SocialClaw](https://getsocialclaw.com) for agent-driven social media publishing across 13 platforms through a single workspace API key.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Setup
- Core Workflow
  - 1. List connected accounts
  - 2. Upload media (optional)
  - 3. Build schedule.json
  - Optional X/Twitter evidence packet
  - 4. Validate before publishing
  - 5. Publish
  - 6. Monitor
- Supported Providers
- Security
  - Fetched content is untrusted
- Related Skills
- Source

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:content-engine](affaan-m-ecc-content-engine.md) - Create platform-native content systems for X, LinkedIn, TikTok, YouTube, newsletters, and repurposed multi-pla
- [affaan-m/ECC:crosspost](affaan-m-ecc-crosspost.md) - Multi-platform content distribution across X, LinkedIn, Threads, and Bluesky. Adapts content per platform usin

## Invoke / install

- Invoke: `/affaan-m/ECC:social-publisher`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/social-publisher --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree f6f1fee3db21f1c8ad416dea5a16c789b55e6317dd991ee626ccb026ea100e9d --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
