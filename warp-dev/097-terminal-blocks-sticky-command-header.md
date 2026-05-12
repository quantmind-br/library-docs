---
title: Sticky Command Header | Warp
url: https://docs.warp.dev/terminal/blocks/sticky-command-header
source: sitemap
fetched_at: 2026-04-29T15:02:20.320072978-03:00
rendered_js: false
word_count: 152
summary: This document explains the functionality and configuration of the Sticky Command Header feature in the Warp terminal, which helps track block headers during long-running command output.
tags:
    - warp-terminal
    - sticky-header
    - command-palette
    - ui-features
    - productivity
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
For long-running commands that take up the full screen, the sticky header only appears after you scroll up — preventing it from blocking output for commands like `git log` that simulate full-screen apps.

## Accessing Sticky Command Header

- **Enabled by default.**
- Toggle via **Settings → Features → General → "Show sticky command header"**
- Toggle via [[101-terminal-command-palette|Command Palette]] or `CTRL-CMD-S`
- Toggle in the active pane only with `CTRL-S` (minimizes on active session without disabling globally)

## Using Sticky Command Header

- For blocks with large output (e.g., `seq 1 1000`), the block header appears at the top of the active Window, Tab, or Pane.
- Click the Sticky Command Header to jump to the top of the block.
- Click the UP/DOWN arrow in the middle of the header to minimize it while active.

## How It Works

![](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F4009768362-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPsjNxoJ0NFCXW6rRdHH3%252Fuploads%252Fgit-blob-242f19a3d854b7d78baad1fbfab7eb39e99406c9%252Fsticky-header-toggle-active-demo.gif%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b5191a9a&sv=2)

Toggle active header and Jump to bottom of block demo
