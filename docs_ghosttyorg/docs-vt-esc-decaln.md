---
title: Screen Alignment Test (DECALN) - ESC
url: https://ghostty.org/docs/vt/esc/decaln
source: crawler
fetched_at: 2026-03-03T08:23:32.65871-03:00
rendered_js: true
word_count: 102
summary: This document details the function and usage of the DECALN control sequence, which resets margins, moves the cursor to the top-left, and fills the screen with the character 'E'.
tags:
    - terminal-control
    - escape-sequence
    - decaln
    - cursor-control
    - screen-fill
category: reference
---

Reset margins, move cursor to the top left, and fill the screen with \`E\`.

1. 0x1B
   
   ESC
2. 0x23
   
   \#
3. 0x38
   
   8

Reset the top, bottom, left, and right margins and unset [origin mode](#TODO). The cursor is moved to the top-left corner of the screen.

All stylistic SGR attributes are unset, such as bold, blink, etc. SGR foreground and background colors are preserved. The [protected attribute](#TODO) is not unset.

The entire screen is filled with the character `E`. The letter `E` ignores the current SGR settings and is written with no styling.

```bash
printf "\033#8"

|EEEEEEEE|
|EEEEEEEE|
|EEEEEEEE|
```

```bash
printf "\033[2;3r" # scroll region top/bottom
printf "\033#8"
printf "\033[T"

|c_______|
|EEEEEEEE|
|EEEEEEEE|
```

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/esc/decaln.mdx)

- [Validation](#validation)
- [DECALN V-1: Simple Usage](#decaln-v-1:-simple-usage)
- [DECALN V-2: Reset Margins](#decaln-v-2:-reset-margins)