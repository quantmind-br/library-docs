---
title: Find & replace | Warp
url: https://docs.warp.dev/code/code-editor/find-and-replace
source: sitemap
fetched_at: 2026-04-29T15:03:26.298956665-03:00
rendered_js: false
word_count: 154
summary: This document explains how to utilize the find and replace functionality within the editor, including keyboard shortcuts, navigation controls, and case-sensitive replacement options.
tags:
    - code-editor
    - search-tool
    - text-replacement
    - keyboard-shortcuts
    - regex-search
category: guide
optimized: true
optimized_at: 2026-04-29T15:03:26.298956665-03:00
---
## Find

Open with `CMD-F` (macOS) or `CTRL-SHIFT-F` (Windows/Linux). Matches highlight as you type; the closest match to cursor is selected.

| Action | Shortcut |
|--------|----------|
| Next match | `ENTER` or down arrow |
| Previous match | `SHIFT-ENTER` or up arrow |
| Select all | "Select All" button |

Toggle regex and case-sensitive options in the query editor.

## Replace

Click the dropdown left of the find menu.

| Action | Description |
|--------|-------------|
| Replace selected | `Enter` |
| Replace all | "Replace All" button |
| Preserve Case | keeps original casing |

**Preserve Case examples:**

| Original | Replacement | Result |
|----------|-------------|--------|
| `old` → `new` | `Old` → `New`, `OLD` → `NEW` | |
| `oldValue` → `NewValue` | `newValue` | |
| `OldValue` → `newValue` | `NewValue` | |
| `my-Old-VALUE` → `my-new-value` | `my-New-VALUE` | |

Supports PascalCase, camelCase, hyphens, and underscores.
