---
title: Manual update
url: https://github.com/gsd-build/get-shit-done/blob/main/docs/manual-update.md
source: git
fetched_at: 2026-04-16T16:20:55.753683866-03:00
rendered_js: false
word_count: 272
summary: This document provides instructions for manually updating the get-shit-done software from source when the standard npm installation method is unavailable.
tags:
    - manual-installation
    - cli-tools
    - software-update
    - source-code
    - runtime-configuration
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Manual Update (Non-npm Install)

Use this procedure when `npx get-shit-done-cc@latest` is unavailable — e.g. during a publish outage or if you are working directly from the source repo.

**Prerequisites:** Node.js installed, repo cloned locally (`git clone https://github.com/gsd-build/get-shit-done`)

## Steps

```bash
# 1. Pull latest code
git pull --rebase origin main

# 2. Build the hooks dist (required — hooks/dist/ is generated, not checked in as source)
node scripts/build-hooks.js

# 3. Run the installer directly
node bin/install.js --claude --global

# 4. Clear the update cache so the statusline indicator resets
rm -f ~/.cache/gsd/gsd-update-check.json
```

**Step 5 — Restart your runtime** to pick up the new commands and agents.

## Runtime Flags

Replace `--claude` with the flag for your runtime:

| Runtime | Flag |
|---------|------|
| Claude Code | `--claude` |
| Gemini CLI | `--gemini` |
| OpenCode | `--opencode` |
| Kilo | `--kilo` |
| Codex | `--codex` |
| Copilot | `--copilot` |
| Cursor | `--cursor` |
| Windsurf | `--windsurf` |
| Augment | `--augment` |
| All runtimes | `--all` |

Use `--local` instead of `--global` for a project-scoped install.

## What the Installer Replaces

The installer performs a clean wipe-and-replace of GSD-managed directories only:

- `~/.claude/get-shit-done/` — workflows, references, templates
- `~/.claude/commands/gsd/` — slash commands
- `~/.claude/agents/gsd-*.md` — GSD agents
- `~/.claude/hooks/dist/` — compiled hooks

**What is preserved:**
- Custom agents not prefixed with `gsd-`
- Custom commands outside `commands/gsd/`
- Your `CLAUDE.md` files
- Custom hooks

> [!warning]
> Locally modified GSD files are automatically backed up to `gsd-local-patches/` before the install. Run `/gsd-reapply-patches` after updating to merge your modifications back in.

#manual-installation #cli-tools #software-update
