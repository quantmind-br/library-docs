---
title: Repeat (REP) - CSI
url: https://ghostty.org/docs/vt/csi/rep
source: crawler
fetched_at: 2026-03-03T08:23:38.852932-03:00
rendered_js: true
word_count: 149
summary: This document explains the usage and behavior of the Repeat Previous Character (REP) control sequence, which consists of ESC [ n b, used to repeat the last printed character a specified number of times.
tags:
    - terminal-control
    - csi-sequence
    - repeat-character
    - escape-sequence
    - vt100
category: reference
---

## Repeat Previous Character (REP)

Repeat the previously printed character \`n\` times.

1. 0x1B
   
   ESC
2. 0x5B
   
   [
3. \_\_\__
   
   n
4. 0x62
   
   b

The parameter `n` must be an integer greater than or equal to 1. If `n` is less than or equal to 0, adjust `n` to be 1. If `n` is omitted, `n` defaults to 1.

In xterm, only characters with single byte (less than decimal 256) are supported. In most other mainstream terminals, any character is supported.

Each repeated character behaves identically to if it was manually typed in. Therefore, soft-wrapping, margins, etc. all behave the same as if the character was typed.

The previously printed character is any character that is printed through any means. The previously printed character is not limited to characters a user manually types. If there is no previously typed character, this sequence does nothing.

```bash
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "A"
printf "\033[b"

|AAc_______|
```

```bash
cols=$(tput cols)
printf "\033[1;1H" # move to top-left
printf "\033[0J" # clear screen
printf "\033[${cols}G"
printf "A"
printf "\033[b"

|_________A|
|Ac________|
```

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/csi/rep.mdx)

- [Validation](#validation)
- [REP V-1: Simple Usage](#rep-v-1:-simple-usage)
- [REP V-2: Soft-Wrap](#rep-v-2:-soft-wrap)