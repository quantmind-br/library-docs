---
title: Performance benchmarks | Warp
url: https://docs.warp.dev/terminal/comparisons/performance
source: sitemap
fetched_at: 2026-04-29T15:03:16.037446948-03:00
rendered_js: false
word_count: 321
summary: This document provides a performance comparison between the Warp terminal emulator and several popular alternatives using industry-standard benchmarking tools. It details the methodology, test environments, and quantitative results for input and output processing speeds.
tags:
    - terminal-emulator
    - performance-benchmarking
    - software-comparison
    - vtebench
    - termbench
    - mac-os-tools
category: other
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp was benchmarked against 4 other terminal emulators using industry-standard tools.

## Terminal apps selected

| Terminal | Reason for inclusion |
|---|---|
| Terminal.app | Default macOS terminal |
| iTerm2 | Most popular macOS third-party terminal |
| Alacritty | Rust-based, known for speed |
| WezTerm | Rust-based, known for speed |

## Versions & settings

| Terminal | Version | Size (cols × rows) |
|---|---|---|
| Warp | v0.2022.04.01.01.37.stable_03 | — |
| Alacritty | 0.10.1 (2844606) | — |

> [!note]
> These benchmarks are not exhaustive. They measure how each app handles heavy input/output. Latency testing (keypress-to-screen) may be added in the future. Source code is linked for reproducibility.

## VTE benchmark

Benchmark code: [vtebench](https://github.com/alacritty/vtebench) (commit `93bcc32b6e0f7560e9b1a5a8b0998c04fbf9b50d`). Results in milliseconds.

### Average time

| Test | Warp | Terminal.app | iTerm | Alacritty | WezTerm |
|---|---|---|---|---|---|
| scrolling_bottom_small_region | — | — | — | — | — |
| scrolling_top_small_region | — | — | — | — | — |

![VTEbench average results (logarithmic scale)](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F4009768362-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPsjNxoJ0NFCXW6rRdHH3%252Fuploads%252Fgit-blob-4fd6246c4ec142bffccc1c34655a39f5c89114d4%252Fvtebench_avg.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=4d1ab9d4&sv=2)

### P90

| Test | Warp | Terminal.app | iTerm | Alacritty | WezTerm |
|---|---|---|---|---|---|
| scrolling_bottom_small_region | — | — | — | — | — |
| scrolling_top_small_region | — | — | — | — | — |

![VTEbench p90 results (logarithmic scale)](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F4009768362-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPsjNxoJ0NFCXW6rRdHH3%252Fuploads%252Fgit-blob-2ff8b633d0763421572f9dc4ef9351c6a060108d%252Fvtebench_p90.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=f735c544&sv=2)

## Termbench

Benchmark code: [termbench](https://github.com/cmuratori/termbench) (commit `82afbc69256b4e22de913f0f02f82e0480f3dac5`). Results in seconds.

> [!note]
> Terminal.app only participated in the small test.

### Small test size

| Terminal | Result (s) |
|---|---|
| Warp | — |
| Terminal.app | — |
| iTerm | — |
| Alacritty | — |
| WezTerm | — |

![Termbench small results (logarithmic scale)](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F4009768362-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPsjNxoJ0NFCXW6rRdHH3%252Fuploads%252Fgit-blob-f9dfb0234c73af1b47538533968399d9c21ec150%252Ftermbench_small.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=1188002a&sv=2)

### Regular test size

| Terminal | Result (s) |
|---|---|
| Warp | — |
| iTerm | — |
| Alacritty | — |
| WezTerm | — |

![Termbench results (logarithmic scale)](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F4009768362-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPsjNxoJ0NFCXW6rRdHH3%252Fuploads%252Fgit-blob-fed348f024a20663fe457c7e217090d1b8722764%252Ftermbench_regular.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=aab0b1f7&sv=2)

#performance-benchmarking #terminal-emulator #software-comparison
