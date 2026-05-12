---
title: Text selection | Warp
url: https://docs.warp.dev/terminal/more-features/text-selection
source: sitemap
fetched_at: 2026-04-29T15:03:06.355218715-03:00
rendered_js: false
word_count: 125
summary: This document explains advanced text selection features in the terminal, specifically smart selection for common data patterns and rectangular selection for vertical column blocks.
tags:
    - terminal-usage
    - text-selection
    - productivity-tools
    - user-interface
    - keyboard-shortcuts
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
## Smart Selection

Smart selection treats common patterns (URLs, file paths) as single units, not separated by punctuation.

![Using smart selection to select a file path by double clicking](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F4009768362-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPsjNxoJ0NFCXW6rRdHH3%252Fuploads%252Fgit-blob-193352c4cee174eebbcff3d530b604da8c917e52%252Fsmart-selection.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7b8e7c1a&sv=2)

Double-click in the input or blocklist. Recognized patterns:

1. URLs
2. File paths
3. Email addresses
4. IP addresses
5. Floating point numbers (including scientific notation)

Toggle at **Settings** → **Features** → **Terminal** → **Double-click smart selection**. Disable to manually select punctuation within word boundaries.

## Rectangular Selection

Select text in vertical columns (box selection) for copying output/logs without unwanted characters.

![Using rectangular selection to select by columns in the block output](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F4009768362-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPsjNxoJ0NFCXW6rRdHH3%252Fuploads%252Fgit-blob-98d2d2b41c2b0e0cc6cd62bf31087c63f1643a0a%252Frectangular-selection.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7f214c35&sv=2)

Hold modifier keys while dragging:

| Platform | Keys |
|----------|------|
| macOS | `CMD-OPT` |
| Windows/Linux | `CTRL-ALT` |

#terminal-usage #text-selection #productivity-tools
