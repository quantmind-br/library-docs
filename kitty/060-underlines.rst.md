---
title: Colored and styled underlines
url: https://github.com/kovidgoyal/kitty/blob/master/docs/underlines.rst
source: git
fetched_at: 2026-05-04T15:58:32.435882715-03:00
rendered_js: false
word_count: 84
summary: ANSI escape codes for implementing and customizing colored, wavy, or styled underlines within the kitty terminal emulator.
tags:
    - ansi-escape-codes
    - terminal-emulator
    - kitty
    - text-formatting
    - terminfo
    - cli-styling
category: reference
optimized: true
optimized_at: 2026-05-04T18:00:00Z
---
# Colored and styled underlines

kitty supports colored and styled (wavy) underlines, useful for terminal text editors to display spelling errors or syntax issues. Uses re-purposed SGR escape codes unused in modern terminals.

## Underline styles

```bash
<ESC>[4:0m   # no underline
<ESC>[4:1m   # straight underline (SGR 4 == 4:1)
<ESC>[4:2m   # double underline
<ESC>[4:3m   # curly underline (wavy)
<ESC>[4:4m   # dotted underline
<ESC>[4:5m   # dashed underline
<ESC>[4m     # straight underline (backwards compat)
<ESC>[24m    # no underline (backwards compat)
```

## Underline color

Set via the `58` SGR parameter family, matching the `38`/`48` foreground/background pattern:

```bash
<ESC>[58:2:<r>:<g>:<b>m    # RGB underline color
<ESC>[58:5:<idx>m          # 256-color underline color
<ESC>[59m                  # reset underline color
```

> [!note]
> Underline color follows the foreground color under reverse video, if set to a specific color it stays unchanged.

## Detection

Query `terminfo` for the `Su` boolean capability to detect support:

```bash
infocmp $TERM | grep -q Su && echo "supported"
```
