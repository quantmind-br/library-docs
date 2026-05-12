---
title: Terminal comparisons | Warp
url: https://docs.warp.dev/terminal/comparisons
source: sitemap
fetched_at: 2026-04-29T15:03:14.840993531-03:00
rendered_js: false
word_count: 110
summary: This document provides an overview of the Warp terminal, highlighting its unique features, architectural benefits, and performance comparisons with other terminal emulators.
tags:
    - warp-terminal
    - terminal-emulator
    - rust
    - gpu-rendering
    - cli-tools
    - performance-benchmarks
category: concept
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp is a modern terminal built in Rust with GPU rendering, agent support, and a code-editor-style input. See how Warp stacks up against other terminals on raw performance and feature coverage.

## How Warp differs

- **Built-in agents** — Warp Agent (powered by Oz) and third-party CLI agents (Claude Code, Codex, Gemini CLI) run in the same terminal.
- **Modern editing** — Cursor placement, multi-line input, block-based output, and integrated code review work like a text editor.
- **Cross-platform Rust core** — Single Rust + GPU-rendered codebase ships on macOS, Linux, and Windows.

## Benchmarks

[[225-terminal-comparisons-performance|Performance benchmarks]] — VTE and Termbench results comparing Warp against Terminal.app, iTerm2, Alacritty, and WezTerm.