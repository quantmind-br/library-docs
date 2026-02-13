---
title: Device Status Report (DSR) - CSI
url: https://ghostty.org/docs/vt/csi/dsr
source: crawler
fetched_at: 2026-02-11T01:43:34.315888-03:00
rendered_js: true
word_count: 140
summary: This document explains the Device Status Report (DSR) escape sequence used to request operating status and cursor position information from a terminal.
tags:
    - terminal-sequences
    - ansi-escape-codes
    - device-status-report
    - cursor-position
    - csi-sequence
    - vt-emulation
category: reference
---

Request information from the terminal.

1. 0x1B
   
   ESC
2. 0x5B
   
   [
3. \_\_\__
   
   n
4. 0x6E
   
   n

Request information from the terminal depending on the value of `n`.

The possible valid values of `n` are described in the paragraphs below. If any other value of `n` is provided, this sequence does nothing.

If `n = 5`, the *operating status* is requested. The terminal responds to the program with `ESC [ 0 n` to indicate no malfunctions.

If `n = 6`, the *cursor position* is requested. The terminal responds to the program in the format `ESC [ y ; x R` where `y` is the row and `x` is the column, both one-indexed. If [origin mode (DEC Mode 6)](#TODO) is enabled, the reported cursor position is relative to the top-left of the scroll region.

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "\033[5n"
```

```
|^[[0n_____|
```

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "\033[2;4H" # move to top-left
printf "\033[6n"
```

```
^[[2;4R
```

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/csi/dsr.mdx)

- [Validation](#validation)
- [DSR V-1: Operating Status](#dsr-v-1:-operating-status)
- [DSR V-2: Cursor Position](#dsr-v-2:-cursor-position)