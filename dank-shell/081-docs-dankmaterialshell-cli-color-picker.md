---
title: Color Picker | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/cli-color-picker
source: sitemap
fetched_at: 2026-04-26T08:38:41.740933878-03:00
rendered_js: false
word_count: 84
summary: This document describes the dms color pick command-line utility for Wayland, which allows users to capture pixel colors and export them in various customizable formats.
tags:
    - cli-tool
    - color-picker
    - wayland
    - command-line
    - color-formats
    - scripting
category: reference
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

`dms color pick` launches an interactive color picker for Wayland. Click any pixel to capture its color.

- Press **Escape** to cancel.
- Only one format flag at a time. Default is `--hex`.
- Returns all color formats in a single JSON object.
- Use `-o` with placeholders `{0}`, `{1}`, `{2}` (and `{3}` for CMYK) for custom output.

```bash
# CSS rgb() function
dms color pick --rgb -o "rgb({0}, {1}, {2})"
# Output: rgb(255, 128, 64)
# CSS hsl() function
dms color pick --hsl -o "hsl({0}, {1}%, {2}%)"
# Output: hsl(24, 75%, 60%)
# Hex without hash
dms color pick -o "{0}{1}{2}"
# Output: FF8040
# Custom CMYK format
dms color pick --cmyk -o "C={0} M={1} Y={2} K={3}"
# Output: C=0 M=50 Y=75 K=0
# CSS custom properties (modern syntax)
dms color pick --hsl -o "hsl({0}deg {1}% {2}%)" -a
# rgba with full opacity
dms color pick --rgb -o "rgba({0}, {1}, {2}, 1)" -a
```

See [[072-docs-1.2-dankmaterialshell-cli-color-picker]] for detailed format documentation.

#wayland #color-picker #cli-tool
