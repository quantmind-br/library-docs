---
title: Delete Character (DCH) - CSI
url: https://ghostty.org/docs/vt/csi/dch
source: crawler
fetched_at: 2026-02-11T01:43:31.533026-03:00
rendered_js: true
word_count: 267
summary: This document defines the behavior of the Delete Character (DCH) escape sequence, detailing how it shifts cell contents within defined scroll regions and handles multi-cell characters.
tags:
    - ansi-escape-sequences
    - terminal-emulation
    - csi-sequences
    - dch
    - vt-commands
    - character-manipulation
category: reference
---

Delete \`n\` characters at the current cursor position and shift existing cell contents left.

1. 0x1B
   
   ESC
2. 0x5B
   
   [
3. \_\_\__
   
   n
4. 0x50
   
   P

The parameter `n` must be an integer greater than or equal to 1. If `n` is less than or equal to 0, adjust `n` to be 1. If `n` is omitted, `n` defaults to 1.

If the current cursor position is outside of the current scroll region, this sequence does nothing. The cursor is outside of the current scroll region if it is left of the [left margin](#TODO), or right of the [right margin](#TODO).

This sequence unsets the pending wrap state. This sequence does *not* unset the pending wrap state if the cursor position is outside of the current scroll region. This has to be called out explicitly because this behavior differs from [Insert Character (ICH)](https://ghostty.org/docs/vt/csi/ich).

Only cells within the scroll region are deleted or shifted. Cells to the right of the right margin are unmodified. The blank cells inserted from the right margin are blank with the background color colored according to the current SGR state.

If a multi-cell character (such as "橋") is shifted so that the cell is split in half, the multi-cell character can either be clipped or erased. Typical behavior is to clip at the right edge of the screen and erase at a right margin, but either behavior is acceptable.

```
printf "ABC123"
printf "\033[3G"
printf "\033[2P"
```

```
|AB23____|
```

```
printf "ABC123"
printf "\033[3G"
printf "\033[41m"
printf "\033[2P"
```

```
|AB23____|
```

The two rightmost cells should have a red background color.

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "ABC123"
printf "\033[?69h" # enable left/right margins
printf "\033[3;5s" # scroll region left/right
printf "\033[2G"
printf "\033[P"
```

```
|ABC123__|
```

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "ABC123"
printf "\033[?69h" # enable left/right margins
printf "\033[3;5s" # scroll region left/right
printf "\033[4G"
printf "\033[P"
```

```
|ABC2_3__|
```

```
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "A橋123"
printf "\033[3G"
printf "\033[P"
```

```
|A_123_____|
```

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/csi/dch.mdx)

- [Validation](#validation)
- [DCH V-1: Simple Delete Character](#dch-v-1:-simple-delete-character)
- [DCH V-2: SGR State](#dch-v-2:-sgr-state)
- [DCH V-3: Outside Left/Right Scroll Region](#dch-v-3:-outside-leftright-scroll-region)
- [DCH V-4: Inside Left/Right Scroll Region](#dch-v-4:-inside-leftright-scroll-region)
- [DCH V-5: Split Wide Character](#dch-v-5:-split-wide-character)