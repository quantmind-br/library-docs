---
title: Tab completions | Warp
url: https://docs.warp.dev/terminal/command-completions/completions
source: sitemap
fetched_at: 2026-04-29T15:02:33.051013896-03:00
rendered_js: false
word_count: 157
summary: This document explains how to utilize terminal completions to receive fuzzy search suggestions and command options by using keyboard shortcuts or automatic triggers.
tags:
    - terminal-features
    - fuzzy-search
    - command-completions
    - tab-completion
    - shell-aliases
    - productivity-tools
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Completions provide fuzzy search suggestions for commands, options, and paths using approximate matching.

## How to Access

- Type the beginning of a command and press `TAB`.
- Enable "Open completions menu as you type" in **Settings** > **Features** > **Terminal Input** to auto-open.

## How to Use

1. Type `git checkout` (with the space) and press `TAB`.
2. A menu shows all local branches — select with mouse or `UP` / `DOWN`.

## Completions on Aliases

| Alias Type | Behavior |
|------------|----------|
| Shell alias (e.g., `gc=git checkout`) | Typing `gc` + `TAB` gives the same completions as `git checkout` |
| Command alias (e.g., `git st` → `git status`) | Suggestions work for the expanded command |

> [!tip]
> Configure "Tab key behavior" under **Settings** > **Features** > **Terminal Input**. If `Tab` is not bound to completions, `Ctrl-Space` opens the menu. Also enable "Open completions menu as you type" for auto-triggering.

#command-completions #fuzzy-search
