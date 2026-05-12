---
title: Terminal Block basics | Warp
url: https://docs.warp.dev/terminal/blocks/block-basics
source: sitemap
fetched_at: 2026-04-29T15:02:17.154243839-03:00
rendered_js: false
word_count: 282
summary: This document explains how to interact with and manage command-line blocks in the Warp terminal, including how to create, select, and navigate through command outputs.
tags:
    - warp-terminal
    - command-blocks
    - terminal-navigation
    - keyboard-shortcuts
    - user-interface
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Blocks group each command with its output. They grow from bottom to top, with a sticky command header when output is truncated.

> [!tip]
> Blocks with a non-zero exit code have a red background and red sidebar. Try running `xyz` to see.

## Create a Block

Execute any command (e.g., `ls`, `echo hello`) in the input editor. Warp groups the command and output into a new block placed directly above the editor.

## Select a Single Block

| Method | Action |
|--------|--------|
| Mouse | Click the block |
| Keyboard | `CMD-UP` / `CMD-DOWN` to select the most recent block; `UP` / `DOWN` to navigate |

For long blocks, click "Jump to the bottom of this block", or use `SHIFT-CMD-UP` / `SHIFT-CMD-DOWN` to scroll to the top/bottom. The Command Palette also has "Scroll to the top/bottom of selected block".

## Select Multiple Blocks

- `CMD-click` another block to toggle selection.
- `SHIFT-click` to select a range.
- `SHIFT-UP` / `SHIFT-DOWN` to expand the active selection.

## Navigate Blocks

| Shortcut | Action |
|----------|--------|
| `UP` / `DOWN` | Move between blocks |
| `PAGE UP` / `PAGE DOWN` | Scroll by one page |
| `HOME` / `END` | Jump to top/bottom |
| `SHIFT-CMD-UP` / `SHIFT-CMD-DOWN` | Scroll to top/bottom of selected block |
| Mouse / trackpad / scrollbar | Scroll |

When output is truncated, the Sticky Command Header stays pinned at the top — click it to scroll to the block start.

> [!note]
> During long-running or full-screen commands, `PAGE UP`, `PAGE DOWN`, `HOME`, and `END` are forwarded to the running program. See the full list on the [Keyboard Shortcuts](https://docs.warp.dev/getting-started/keyboard-shortcuts) page.

#command-blocks #terminal-navigation
