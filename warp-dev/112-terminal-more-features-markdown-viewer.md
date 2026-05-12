---
title: Markdown viewer | Warp
url: https://docs.warp.dev/terminal/more-features/markdown-viewer
source: sitemap
fetched_at: 2026-04-29T15:03:04.182495833-03:00
rendered_js: false
word_count: 211
summary: This document explains how to use Warp's built-in Markdown viewer and editor, including how to open files, toggle between views, and execute shell commands directly from Markdown code blocks.
tags:
    - warp-terminal
    - markdown-viewer
    - shell-commands
    - terminal-productivity
    - file-editing
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp edits and renders `.md`/`.markdown` files in a [[110-terminal-more-features-blocks-output|split pane]]. Enable **Settings** → **Features** → **General** → **Open Markdown files in Warp's Markdown viewer by default** to set viewer as default; otherwise files open in the editor.

### Opening File Links

`CMD`-click a Markdown file link, use the link tooltip, or right-click context menu.

### Markdown-Viewing Commands

Running `cat myfile.md` (or `glow`/`less`) shows a banner with a button to open the Markdown file.

### Opening from Finder

Right-click a Markdown file → "Open With" → Warp.

### Editor/Viewer Toggle

Toggle via the pane overflow menu.

## Shell Commands in Markdown Files

Click the run icon `>_` in code blocks to insert commands into the terminal.

> [!info]
> Commands must be in triple-backtick code blocks, not inline code.

### Keyboard Navigation

- Click a shell block or press `CMD-UP`/`CMD-DOWN` to enter keyboard mode.
- `CMD-ENTER` inserts the command into terminal input.
- `UP`/`DOWN`/`CMD-UP`/`CMD-DOWN` navigate between blocks.
- `CMD-L` returns focus to terminal without inserting.

### Workflow Arguments

Commands using `{{param}}` syntax become Workflow arguments. See [[105-terminal-ai-features|Warp workflows]].

### Supported Block Languages

Code blocks without a language or with one of `sh`, `shell`, `bash`, `fish`, `zsh`, `warp-runnable-command` are treated as shell commands.

All code blocks have a copy button.

#warp-terminal #markdown-viewer #shell-commands
