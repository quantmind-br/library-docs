---
title: Scroll Down (SD) - CSI
url: https://ghostty.org/docs/vt/csi/sd
source: crawler
fetched_at: 2026-03-10T06:35:34.393387-03:00
rendered_js: true
word_count: 67
summary: This document details the terminal control sequence 'SD' (Scroll Down), which inserts 'n' lines at the top of the current scroll region, shifting existing content down while preserving the cursor position.
tags:
    - terminal-sequence
    - csi
    - scroll-down
    - line-insertion
    - vt100
category: reference
---

Insert \`n\` lines at the top of the scroll region and shift existing lines down.

1. 0x1B
   
   ESC
2. 0x5B
   
   [
3. \_\_\__
   
   n
4. 0x54
   
   T

This sequence is functionally identical to [Insert Line (IL)](https://ghostty.org/docs/vt/csi/il) with the cursor position set to the top of the scroll region. The cursor position after the operation must be unchanged from when SD was invoked.

This sequence unsets the pending wrap state.

```bash
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "ABC\n"
printf "DEF\n"
printf "GHI\n"
printf "\033[3;4r" # scroll region top/bottom
printf "\033[2;2H"
printf "\033[T"

|ABC_____|
|DEF_____|
|________|
|GHI_____|
```

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/csi/sd.mdx)