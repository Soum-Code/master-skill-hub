#!/usr/bin/env bash
# Installs the hub skills for Claude Code (all projects): copies them into ~/.claude/skills.
# Safe to re-run. Replaced folders are moved to ~/.claude/skill-hub/backup, never deleted.
# Do not use this if you installed the plugin (claude plugin install skill-hub@master-skill-hub): you would get duplicates.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
dest="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
hub="${SKILL_HUB_DIR:-$HOME/.claude/skill-hub}"
mkdir -p "$dest" "$hub/backup"
for s in master-skill skill-vetter job-search-copilot ml-interview-prep; do
  [ -d "$here/skills/$s" ] || { echo "missing skills/$s - run from a clone of the repo" >&2; exit 1; }
  if [ -d "$dest/$s" ]; then
    mv "$dest/$s" "$hub/backup/$s-$(date +%Y%m%d%H%M%S)"
    echo "backed up existing $s"
  fi
  cp -R "$here/skills/$s" "$dest/$s"
  find "$dest/$s" -name __pycache__ -type d -prune -exec rm -rf {} +
  echo "installed $s -> $dest/$s"
done
if [ ! -f "$hub/profile.txt" ]; then
  echo "${SKILL_HUB_PROFILE:-general}" > "$hub/profile.txt"
  echo "profile set to $(cat "$hub/profile.txt"). Options: ai-engineer software-developer data-scientist job-seeker designer product-manager founder-operator finance-legal general"
  echo "change it: echo ai-engineer > $hub/profile.txt"
fi
echo "done. Restart Claude Code (or start a new session) to load the skills."
