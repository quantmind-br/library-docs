---
title: Cursor Forward (CUF) - CSI
url: https://ghostty.org/docs/vt/csi/cuf
source: crawler
fetched_at: 2026-02-11T01:43:27.414436-03:00
rendered_js: true
word_count: 180
summary: This document details the CSI CUF escape sequence, which moves the terminal cursor a specified number of cells to the right while handling margins and wrap states.
tags:
    - terminal-emulation
    - ansi-escape-codes
    - cursor-movement
    - csi-cuf
    - terminal-control
category: reference
---

Move the cursor \`n\` cells right.

1. 0x1B
   
   ESC
2. 0x5B
   
   [
3. \_\_\__
   
   n
4. 0x43
   
   C

The parameter `n` must be an integer greater than or equal to 1. If `n` is less than or equal to 0, adjust `n` to be 1. If `n` is omitted, `n` defaults to 1.

This sequence always unsets the pending wrap state.

The rightmost boundary the cursor can move to is determined by the current cursor column and the [right margin](#TODO). If the cursor begins to the right of the right margin, modify the right margin to be the rightmost column of the screen for the duration of the sequence. The rightmost column the cursor can be on is the right margin.

Move the cursor `n` cells to the right up to and including the rightmost boundary. This sequence never wraps or modifies cell content. This sequence is not affected by any terminal modes.

```
cols=$(tput cols)
printf "\033[${cols}G" # move to last column
printf "A" # set pending wrap state
printf "\033[C" # move forward one
printf "XYZ"
```

```
|_________X|
|YZ________|
```

```
printf "A"
printf "\033[500C" # forward larger than screen width
printf "B"
```

```
|A________Bc
```

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "\033[?69h" # enable left/right margins
printf "\033[3;5s" # scroll region left/right
printf "\033[1G" # move to left
printf "\033[500C" # forward larger than screen width
printf "X"
```

```
|____X_____|
```

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "\033[?69h" # enable left/right margins
printf "\033[3;5s" # scroll region left/right
printf "\033[6G" # move to right of margin
printf "\033[500C" # forward larger than screen width
printf "X"
```

```
|_________X|
```

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/csi/cuf.mdx)

- [Validation](#validation)
- [CUF V-1: Pending Wrap is Unset](#cuf-v-1:-pending-wrap-is-unset)
- [CUF V-2: Rightmost Boundary with Reverse Wrap Disabled](#cuf-v-2:-rightmost-boundary-with-reverse-wrap-disabled)
- [CUF V-3: Left of the Right Margin](#cuf-v-3:-left-of-the-right-margin)
- [CUF V-4: Right of the Right Margin](#cuf-v-4:-right-of-the-right-margin)