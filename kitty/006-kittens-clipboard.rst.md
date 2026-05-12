---
title: Clipboard
url: https://github.com/kovidgoyal/kitty/blob/master/docs/kittens/clipboard.rst
source: git
fetched_at: 2026-05-04T15:57:52.503207256-03:00
rendered_js: false
word_count: 88
summary: Copy/paste to system clipboard from shell scripts, with support for files, STDIN/STDOUT, images, and arbitrary MIME types. Works over SSH.
tags:
    - clipboard-management
    - shell-utilities
    - data-transfer
    - ssh-clipboard
    - mime-types
optimized: true
optimized_at: 2026-05-04T18:00:00Z
---
# clipboard

*Copy/paste to the system clipboard from shell scripts*

Read or write the system clipboard from the shell. Works over SSH.

## Basic Usage

```bash
# Copy STDIN to clipboard
echo hooray | kitten clipboard

# Get clipboard contents to STDOUT
kitten clipboard --get-clipboard
```

> [!note]
> By default kitty asks for permission when a program reads the clipboard. Control via `clipboard_control` kitty.conf option.

## Arbitrary Data Types

The kitten transfers arbitrary MIME types, not just plain text:

```bash
# Copy image to clipboard
kitten clipboard picture.png

# Copy image + text to clipboard
kitten clipboard picture.jpg text.txt

# Copy text from STDIN + image to clipboard
echo hello | kitten clipboard picture.png /dev/stdin

# Copy image to file (no clipboard)
kitten clipboard -g picture.png

# Copy image to file + text to STDOUT
kitten clipboard -g picture.png /dev/stdout

# List available clipboard formats
kitten clipboard -g -m . /dev/stdout
```

## MIME Type Control

By default MIME types are guessed from filenames. Override with `--mime`:

```
kitten clipboard --mime image/png,text/plain picture.png
```

## Protocol

Uses a kitty-specific protocol. See [[044-clipboard|Clipboard protocol]] for details.

#clipboard-management #shell-utilities #ssh-clipboard
