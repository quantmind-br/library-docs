---
title: Carriage Return (CR) - Control
url: https://ghostty.org/docs/vt/control/cr
source: crawler
fetched_at: 2026-02-11T01:43:21.575383-03:00
rendered_js: true
word_count: 117
summary: This document defines the behavior of the Carriage Return (CR) control character, detailing how it affects cursor positioning and the pending wrap state within terminal emulators.
tags:
    - terminal-emulation
    - control-sequences
    - carriage-return
    - cursor-movement
    - vt100
    - terminal-margins
category: reference
---

Move the cursor to the leftmost column.

1. 0x0D
   
   CR

This sequence always unsets the pending wrap state.

If [origin mode (mode 6)](#TODO) is enabled, the cursor is set to the [left margin](#TODO) of the scroll region and the operation is complete.

If origin mode is *not* set and the cursor is on or to the right of the left margin, the cursor is set to the left margin. If the cursor is to the left of the left margin, the cursor is moved to the leftmost column in the terminal.

```
cols=$(tput cols)
printf "\033[${cols}G" # move to last column
printf "A" # set pending wrap state
printf "\r"
printf "X"
echo
```

```
|X________A|
|c_________|
```

```
cols=$(tput cols)
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "\033[?69h" # enable left/right margin mode
printf "\033[2;5s" # set left/right margin
printf "\033[4G"
printf "A"
printf "\r"
printf "X"
```

```
|_XcA______|
```

```
cols=$(tput cols)
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "\033[?69h" # enable left/right margin mode
printf "\033[2;5s" # set left/right margin
printf "\033[4G"
printf "A"
printf "\033[1G"
printf "\r"
printf "X"
```

```
|Xc_A______|
```

```
cols=$(tput cols)
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "\033[?6h" # enable origin mode
printf "\033[?69h" # enable left/right margin mode
printf "\033[2;5s" # set left/right margin
printf "\033[4G"
printf "A"
printf "\033[1G"
printf "\r"
printf "X"
```

```
|_XcA______|
```

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/control/cr.mdx)

- [Validation](#validation)
- [CR V-1: Pending Wrap is Unset](#cr-v-1:-pending-wrap-is-unset)
- [CR V-2: Left Margin](#cr-v-2:-left-margin)
- [CR V-3: Left of Left Margin](#cr-v-3:-left-of-left-margin)
- [CR V-3: Left Margin with Origin Mode](#cr-v-3:-left-margin-with-origin-mode)