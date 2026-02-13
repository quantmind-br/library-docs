---
title: Tab Clear (TBC) - CSI
url: https://ghostty.org/docs/vt/csi/tbc
source: crawler
fetched_at: 2026-02-11T01:43:34.239756-03:00
rendered_js: true
word_count: 83
summary: This document explains how to use the Tab Clear (TBC) escape sequence to clear individual or all tab stops in a terminal emulator.
tags:
    - ansi-escape-codes
    - vt-sequences
    - terminal-control
    - tab-stops
    - tbc-command
category: reference
---

Clear one or all tab stops.

1. 0x1B
   
   ESC
2. 0x5B
   
   [
3. \_\_\__
   
   n
4. 0x67
   
   g

The parameter `n` must be `0` or `3`. If `n` is omitted, `n` defaults to `0`.

If the parameter `n` is `0`, the cursor column position is marked as not a tab stop. If the column was already not a tab stop, this does nothing.

If the parameter `n` is `3`, all tab stops are cleared.

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "\033[?5W" # reset tabs
printf "\t"
printf "\033[g"
printf "\033[1G"
printf "\t"
```

```
|_______________c_______|
```

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "\033[?5W" # reset tabs
printf "\033[3g"
printf "\033[1G"
printf "\t"
```

```
|______________________c|
```

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/csi/tbc.mdx)

- [Validation](#validation)
- [TBC V-1: Tab Clear Single](#tbc-v-1:-tab-clear-single)
- [TBC V-3: Clear All Tabstops](#tbc-v-3:-clear-all-tabstops)