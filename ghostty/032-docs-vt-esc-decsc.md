---
title: Save Cursor (DECSC) - ESC
url: https://ghostty.org/docs/vt/esc/decsc
source: crawler
fetched_at: 2026-02-11T01:43:22.856854-03:00
rendered_js: true
word_count: 111
summary: This document explains the Save Cursor (DECSC) escape sequence, detailing which terminal attributes are stored and how the saved state behaves across different screen buffers.
tags:
    - ansi-escape-sequences
    - terminal-emulation
    - cursor-management
    - vt100
    - decsc
category: reference
---

Save various cursor-related state that can be restored with Restore Cursor (DECRC).

1. 0x1B
   
   ESC
2. 0x37
   
   7

The following attributes are saved:

- Cursor row and column in absolute screen coordinates
- Character sets
- Pending wrap state
- SGR attributes
- [Origin mode (DEC Mode 6)](#TODO)

Only one cursor can be saved at any time. If save cursor is repeated, the previously save cursor is overwritten.

Primary and alternate screens have separate saved cursor state. A cursor saved on the primary screen is inaccessible from the alternate screen and vice versa.

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "\033[1;5H"
printf "A"
printf "\0337" # Save Cursor
printf "\033[1;1H"
printf "B"
printf "\0338" # Restore Cursor
printf "X"
```

```
|B___AX____|
```

```
cols=$(tput cols)
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "\033[${cols}G"
printf "A"
printf "\0337" # Save Cursor
printf "\033[1;1H"
printf "B"
printf "\0338" # Restore Cursor
printf "X"
```

```
|B________A|
|X_________|
```

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "\033[1;4;33;44m"
printf "A"
printf "\0337" # Save Cursor
printf "\033[0m"
printf "B"
printf "\0338" # Restore Cursor
printf "X"
```

```
|AX________|
```

The "A" and "X" should have identical styling.

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/esc/decsc.mdx)

- [Validation](#validation)
- [SC V-1: Cursor Position](#sc-v-1:-cursor-position)
- [SC V-2: Pending Wrap State](#sc-v-2:-pending-wrap-state)
- [SC V-3: SGR Attributes](#sc-v-3:-sgr-attributes)