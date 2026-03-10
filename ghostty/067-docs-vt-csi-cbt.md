---
title: Cursor Backward Tabulation (CBT) - CSI
url: https://ghostty.org/docs/vt/csi/cbt
source: crawler
fetched_at: 2026-03-10T06:35:35.115679-03:00
rendered_js: true
word_count: 148
summary: This document details the Control Sequence (CSI) command for moving the cursor backward to the preceding tab stop or the leftmost valid column, known as Cursor Backward Tabulate (CBT). It explains the sequence of bytes required and the rules governing cursor movement relative to tab stops and margins.
tags:
    - terminal-control
    - escape-sequences
    - cursor-movement
    - cbt
    - tab-stops
category: reference
---

Move the cursor \`n\` tabs left.

1. 0x1B
   
   ESC
2. 0x5B
   
   [
3. \_\_\__
   
   n
4. 0x5A
   
   Z

The leftmost valid column for this operation is the first column. If [origin mode](#TODO) is enabled, then the leftmost valid column for this operation is the [left margin](#TODO).

Move the cursor left until the cursor position is on a tabstop. If the cursor would move past the leftmost valid column, the cursor remains at the leftmost valid column and the operation completes. Repeat this process `n` times.

Tabstops are dynamic and can be set with escape sequences such as [horizontal tab set (HTS)](#TODO), [tab clear (TBC)](https://ghostty.org/docs/vt/csi/tbc), etc. A terminal emulator may default tabstops at any interval, though an interval of 8 spaces is most common.

```bash
printf "\033[?5W" # reset tab stops
printf "\033[10Z"
printf "A"

|Ac________|
```

```bash
printf "\033[?5W" # reset tab stops
printf "\033[1;10H"
printf "X"
printf "\033[Z"
printf "A"

|________AX|
```

```bash
printf "\033[?5W" # reset tab stops
printf "\033[1;9H"
printf "X"
printf "\033[1;9H"
printf "\033[Z"
printf "A"

|A_______X_|
```

```bash
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "\033[?5W" # reset tab stops
printf "\033[?6h" # enable origin mode
printf "\033[?69h" # enable left/right margins
printf "\033[3;6s" # scroll region left/right
printf "\033[1;2H" # move cursor in region
printf "X"
printf "\033[Z"
printf "A"

|__AX______|
```

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/csi/cbt.mdx)

- [Validation](#validation)
- [CBT V-1: Left Beyond First Column](#cbt-v-1:-left-beyond-first-column)
- [CBT V-2: Left Starting After Tab Stop](#cbt-v-2:-left-starting-after-tab-stop)
- [CBT V-3: Left Starting on Tabstop](#cbt-v-3:-left-starting-on-tabstop)
- [CBT V-4: Left Margin with Origin Mode](#cbt-v-4:-left-margin-with-origin-mode)