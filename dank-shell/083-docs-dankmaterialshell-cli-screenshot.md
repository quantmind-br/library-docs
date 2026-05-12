---
title: Screenshot | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/cli-screenshot
source: sitemap
fetched_at: 2026-04-26T08:38:51.651988111-03:00
rendered_js: false
word_count: 41
summary: This document provides usage instructions for the dms screenshot command, explaining how to capture Wayland display screenshots with options for output formats and clipboard integration.
tags:
    - wayland
    - screenshot
    - cli-tool
    - image-capture
    - clipboard-integration
category: reference
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

`dms screenshot` captures screenshots from Wayland displays with multiple capture modes, output formats, and clipboard integration.

- Press **Escape** to cancel region selection.
- Use `--format` or `-f` to specify output format. Default is `png`.

```bash
# Interactive selection, save file + clipboard
dms screenshot
# File only, no clipboard
dms screenshot --no-clipboard
# Clipboard only, no file
dms screenshot --no-file
```

See [[081-docs-dankmaterialshell-cli-color-picker]] for the companion color picker tool.

#wayland #screenshot #cli-tool #image-capture
