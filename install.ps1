# Installs the hub skills for Claude Code (all projects): copies them into ~\.claude\skills.
# Safe to re-run. Replaced folders are moved to ~\.claude\skill-hub\backup, never deleted.
# Do not use this if you installed the plugin (claude plugin install skill-hub@master-skill-hub): you would get duplicates.
param(
  [string]$Dest = (Join-Path $HOME ".claude\skills"),
  [string]$Hub = (Join-Path $HOME ".claude\skill-hub"),
  [string]$Profile = "general"
)
$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
New-Item -ItemType Directory -Force -Path $Dest, (Join-Path $Hub "backup") | Out-Null
foreach ($s in "master-skill", "skill-vetter", "job-search-copilot", "ml-interview-prep") {
  $src = Join-Path $here "skills\$s"
  if (-not (Test-Path $src)) { throw "missing skills\$s - run from a clone of the repo" }
  $target = Join-Path $Dest $s
  if (Test-Path $target) {
    Move-Item $target (Join-Path $Hub ("backup\$s-" + (Get-Date -Format "yyyyMMddHHmmss")))
    Write-Host "backed up existing $s"
  }
  Copy-Item -Recurse $src $target
  Get-ChildItem $target -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force
  Write-Host "installed $s -> $target"
}
$pf = Join-Path $Hub "profile.txt"
if (-not (Test-Path $pf)) {
  Set-Content -Path $pf -Value $Profile
  Write-Host "profile set to $Profile. Options: ai-engineer software-developer data-scientist job-seeker designer product-manager founder-operator finance-legal general"
}
Write-Host "done. Restart Claude Code (or start a new session) to load the skills."
