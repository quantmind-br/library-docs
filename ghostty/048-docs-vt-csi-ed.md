---
title: Erase in Display (ED) - CSI
url: https://ghostty.org/docs/vt/csi/ed
source: crawler
fetched_at: 2026-02-11T01:43:30.136221-03:00
rendered_js: true
word_count: 393
summary: This document explains the technical specification and behavior of the Erase Display (ED) terminal escape sequence, detailing how different parameters clear portions of the screen or scrollback buffer.
tags:
    - terminal-emulation
    - escape-sequences
    - csi-j
    - erase-display
    - vt-specification
category: reference
---

Erase display contents with behavior depending on the command \`n\`.

1. 0x1B
   
   ESC
2. 0x5B
   
   [
3. \_\_\__
   
   n
4. 0x4A
   
   J

If `n` is unset, the value of `n` is 0. The only valid values for `n` are 0, 1, 2, or 3. If any other value of `n` is given, do not execute this sequence. The remainder of the sequence documentation assumes a valid value of `n`.

For all valid values of `n` except 3, this sequence unsets the pending wrap state. The cursor position will remain unchanged under all circumstances throughout this sequence.

If [Select Character Selection Attribute (DECSCA)](#TODO) is enabled or was the most recently enabled protection mode on the currently active screen, protected attributes are ignored. Otherwise, protected attributes will be respected. For more details on this specific logic for protected attribute handling, see [Erase Character (ECH)](https://ghostty.org/docs/vt/csi/ech).

For all operations, if a multi-cell character would be split, erase the full multi-cell character. For example, if "橋" is printed and the erase would only erase the first or second cell of the two-cell character, both cells should be erased.

This sequence does not respect any scroll regions (top, bottom, left, or right). The boundaries of the operation are the full visible screen.

If `n` is `0`, perform an **erase display below** operation. Erase all cells to the right and below the cursor. The background color of erased cells is colored according to the current SGR state.

If `n` is `1`, perform an **erase display above** operation. Erase all cells to the left and above the cursor. The background color of erased cells is colored according to the current SGR state.

If `n` is `2`, **erase the entire display**. This is the equivalent of erase above (`n = 1`) and erase below (`n = 0`) both being executed.

If `n` is `3`, **erase only the scrollback region**. This does not affect the visible display of the screen and does not move the cursor. The scrollback region is the region of the terminal that is currently above the visible area of the screen when the screen is scrolled completely to the bottom.

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "ABC\n"
printf "DEF\n"
printf "GHI\n"
printf "\033[2;2H"
printf "\033[0J"
```

```
|ABC_____|
|Dc______|
|________|
```

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "ABC\n"
printf "DEF\n"
printf "GHI\n"
printf "\033[2;2H"
printf "\033[41m"
printf "\033[0J"
```

```
|ABC_____|
|Dc______|
|________|
```

All the cells right and below of the cursor should be colored red.

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "AB橋C\n"
printf "DE橋F\n"
printf "GH橋I\n"
printf "\033[2;4H"
printf "\033[0J"
```

```
|AB橋C___|
|DE_c____|
|________|
```

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "ABC\n"
printf "DEF\n"
printf "GHI\n"
printf "\033[2;2H"
printf "\033[1J"
```

```
|________|
|_cF_____|
|GHI_____|
```

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "ABC\n"
printf "DEF\n"
printf "GHI\n"
printf "\033[2;2H"
printf "\033[2J"
```

```
|________|
|_c______|
|________|
```

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/csi/ed.mdx)

- [Validation](#validation)
- [ED V-1: Simple Erase Below](#ed-v-1:-simple-erase-below)
- [ED V-2: Erase Below SGR State](#ed-v-2:-erase-below-sgr-state)
- [ED V-3: Erase Below Multi-Cell Character](#ed-v-3:-erase-below-multi-cell-character)
- [ED V-4: Simple Erase Above](#ed-v-4:-simple-erase-above)
- [ED V-5: Simple Erase Complete](#ed-v-5:-simple-erase-complete)