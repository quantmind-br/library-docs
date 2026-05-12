---
title: Build Warp's Own Input Component | Guides | Warp
url: https://docs.warp.dev/guides/build-an-app-in-warp/building-warps-input-with-warp
source: sitemap
fetched_at: 2026-04-29T15:06:59.61854347-03:00
rendered_js: false
word_count: 170
summary: This document describes a workflow where a product designer uses AI-powered coding tools to locate and modify codebase UI elements independently during resource-constrained periods.
tags:
    - ai-coding-assistant
    - ui-redesign
    - workflow-automation
    - codebase-navigation
    - developer-productivity
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
A product designer used Warp AI to fix a one-pixel UI bug in Warp's Rust codebase without needing engineering support.

## The Challenge

Redesigning the input component — used all day, every day — required multiple Figma iterations. Once the team landed on a version, engineering was stretched thin on agent-mode quality and the Agentic Development Environment.

## Step 1: Locating the Git Diff Chip Code

The Git Diff chip (shows current branch + open changes) was one pixel too tall. Warp searched the entire codebase and found references in:

- `displaychip.rs`
- Related render and configuration files

Used semantic search, code indexing, and grep.

## Step 2: Modifying the Font Size

Warp reduced font size by 1 pixel, changing `system_font_size - 1` → `system_font_size - 2`.

Reviewed diffs to confirm changes.

## Step 3: Building and Testing

```
cargo build --release
```

Warp auto-fixed compile issues, verified visually in-app.

## Recap

- Located chip code with semantic search
- Modified font size, reviewed diffs
- Built, auto-fixed issues, tested

#ai-coding-assistant #ui-redesign #workflow-automation #codebase-navigation #developer-productivity
