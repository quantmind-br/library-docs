---
title: Cursor Up (CUU) - CSI
url: https://ghostty.org/docs/vt/csi/cuu
source: crawler
fetched_at: 2026-02-11T01:43:26.607745-03:00
rendered_js: true
word_count: 122
summary: This document explains the CSI CUU escape sequence used to move the terminal cursor upward by a specified number of cells, detailing parameter defaults and behavior regarding margins.
tags:
    - ansi-escape-codes
    - terminal-emulation
    - cursor-movement
    - csi-sequences
    - vt100
category: reference
---

Move the cursor \`n\` cells up.

1. 0x1B
   
   ESC
2. 0x5B
   
   [
3. \_\_\__
   
   n
4. 0x41
   
   A

The parameter `n` must be an integer greater than or equal to 1. If `n` is less than or equal to 0, adjust `n` to be 1. If `n` is omitted, `n` defaults to 1.

This sequence always unsets the pending wrap state.

If the current cursor position is at or below the [top margin](#TODO), the highest point the cursor can move is the top margin. If the current cursor position is above the top margin, the highest point the cursor can move is the first row.

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "\033[3;1H"
printf "A"
printf "\033[2A" # cursor up
printf "X"
```

```
|_Xc_______|
|__________|
|A_________|
```

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "\n\n\n\n" # screen is 4 high
printf "\033[2;4r" # set scrolling region
printf "\033[3;1H"
printf "A"
printf "\033[5A" # cursor up
printf "X"
```

```
|__________|
|_Xc_______|
|A_________|
|__________|
```

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "\n\n\n\n\n" # screen is 5 high
printf "\033[3;5r" # set scrolling region
printf "\033[3;1H"
printf "A"
printf "\033[2;1H" # move above region
printf "\033[5A" # cursor up
printf "X"
```

```
|Xc________|
|__________|
|A_________|
|__________|
|__________|
```

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/csi/cuu.mdx)

- [Validation](#validation)
- [CUU V-1: Cursor Up](#cuu-v-1:-cursor-up)
- [CUU V-2: Cursor Up Below Top Margin](#cuu-v-2:-cursor-up-below-top-margin)
- [CUU V-3: Cursor Up Above Top Margin](#cuu-v-3:-cursor-up-above-top-margin)