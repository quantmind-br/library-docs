---
title: Command history | Warp
url: https://docs.warp.dev/terminal/entry/command-history
source: sitemap
fetched_at: 2026-04-29T15:02:27.244937262-03:00
rendered_js: false
word_count: 87
summary: This document explains how the Warp terminal manages shell command history across sessions and provides instructions on how to access and search historical commands.
tags:
    - command-history
    - shell-session
    - terminal-productivity
    - fuzzy-search
    - warp-terminal
category: concept
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
## What is it

Warp isolates history per shell session. Commands in one Split Pane do not populate history in another; history merges on session close. Each entry stores rich metadata: exit code, directory, thread, runtime, last run time.

## How to access it

- `↑` in the [[227-terminal-entry-command-history|Input Editor]] opens history with prefix search.
- `CTRL-R` opens [[228-terminal-entry-command-search|Command Search]] panel, initiating a fuzzy search of Command History. Type to filter; Warp bolds matching text.

## How it works

Command History Demo

Last updated 2 months ago