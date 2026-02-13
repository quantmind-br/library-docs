---
title: Reverse Index (RI) - ESC
url: https://ghostty.org/docs/vt/esc/ri
source: crawler
fetched_at: 2026-02-11T01:43:23.117083-03:00
rendered_js: true
word_count: 111
summary: This document explains the Reverse Index (RI) escape sequence, which moves the terminal cursor up one row and triggers a scroll-down operation if the cursor is already at the top margin.
tags:
    - escape-sequence
    - reverse-index
    - cursor-movement
    - terminal-scrolling
    - ansi-vt-control
category: reference
---

Move the cursor up one cell, scrolling if necessary.

1. 0x1B
   
   ESC
2. 0x4D
   
   M

This sequence does not unset the pending wrap state.

If the cursor is exactly on the [top margin](https://ghostty.org/docs/vt/csi/decstbm) and is within [left and right margins](https://ghostty.org/docs/vt/csi/decslrm), invoke [scroll down (SD)](https://ghostty.org/docs/vt/csi/sd) with `n = 1`. The operation is complete.

Otherwise, scrolling isn't necessary. Perform a [cursor up](https://ghostty.org/docs/vt/csi/cuu) operation with `n = 1`.

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "A\n"
printf "B\n"
printf "C\n"
printf "\033[1;1H" # move to top-left
printf "\033M" # reverse index
printf "X"
```

```
|Xc________|
|A_________|
|B_________|
|C_________|
```

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "A\n"
printf "B\n"
printf "C\n"
printf "\033[2;1H"
printf "\033M" # reverse index
printf "X"
```

```
|Xc________|
|B_________|
|C_________|
```

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "A\n"
printf "B\n"
printf "C\n"
printf "\033[2;3r" # scroll region
printf "\033[2;1H"
printf "\033M" # reverse index
```

```
|A_________|
|c_________|
|B_________|
```

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "A\n"
printf "B\n"
printf "C\n"
printf "\033[2;3r" # scroll region
printf "\033[1;1H"
printf "\033M" # reverse index
```

```
|A_________|
|B_________|
|C_________|
```

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "ABC\n"
printf "DEF\n"
printf "GHI\n"
printf "\033[?69h" # enable left/right margins
printf "\033[2;3s" # scroll region left/right
printf "\033[1;2H"
printf "\033M"
```

```
|A_________|
|DBC_______|
|GEF_______|
|_HI_______|
```

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "ABC\n"
printf "DEF\n"
printf "GHI\n"
printf "\033[?69h" # enable left/right margins
printf "\033[2;3s" # scroll region left/right
printf "\033[2;1H"
printf "\033M"
```

```
|ABC_______|
|DEF_______|
|GHI_______|
```

Cursor on the `A`.

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/esc/ri.mdx)

- [Validation](#validation)
- [RI V-1: No Scroll Region, Top of Screen](#ri-v-1:-no-scroll-region-top-of-screen)
- [RI V-2: No Scroll Region, Not Top of Screen](#ri-v-2:-no-scroll-region-not-top-of-screen)
- [RI V-3: Top/Bottom Scroll Region](#ri-v-3:-topbottom-scroll-region)
- [RI V-4: Outside of Top/Bottom Scroll Region](#ri-v-4:-outside-of-topbottom-scroll-region)
- [RI V-5: Left/Right Scroll Region](#ri-v-5:-leftright-scroll-region)
- [RI V-6: Outside Left/Right Scroll Region](#ri-v-6:-outside-leftright-scroll-region)