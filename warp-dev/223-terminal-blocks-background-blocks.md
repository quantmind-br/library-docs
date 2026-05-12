---
title: Background blocks | Warp
url: https://docs.warp.dev/terminal/blocks/background-blocks
source: sitemap
fetched_at: 2026-04-29T15:02:18.586101684-03:00
rendered_js: false
word_count: 133
summary: This document explains how background processes are handled in the Warp terminal, describing how output is captured into independent background blocks and identifying potential limitations.
tags:
    - terminal-emulator
    - background-process
    - command-line
    - process-management
    - warp-terminal
category: concept
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
## What is it

Commands can start background processes that continue running after the shell exits. Background blocks capture output from these processes, acting like regular blocks without an associated command. All Warp block features—sharing, bookmarking, etc.—apply.

## How to use it

Background blocks are created automatically as needed, interleaved between regular blocks. If a command runs while background output is still streaming, output is split across multiple blocks.

## How it works

Create Background Blocks

## Troubleshooting

Warp cannot distinguish which process produced output, causing these limitations:

- Background output arriving while a foreground command runs is captured in the foreground block.
- Multiple simultaneous background processes may have interleaved output.
- Typeahead editing in bash versions older than 4.0 may be mistaken for background output (commonly from deleting and retyping characters).