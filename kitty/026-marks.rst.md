---
title: Mark text on screen
title: Mark text on screen
word_count: 195
summary: This document explains how to configure and use marker functionality in the kitty terminal emulator to highlight text patterns using regular expressions, custom functions, or simple substrings.
category: guide
optimized: true
optimized_at: 2026-05-04T20:45:24Z
---
# Mark text on screen

Highlight text patterns (regex, substrings, functions) in the terminal. Useful for tracking words/phrases in long-running program output.

## Examples

### Basic substring matching

```conf
map f1 toggle_marker text 1 ERROR
```

Press F1 to toggle highlighting of "ERROR". Press again to disable.

### Case-insensitive matching

```conf
map f1 toggle_marker itext 1 ERROR
```

### Whole-word regex matching

```conf
map f1 toggle_marker regex 1 \\bERROR\\b
```

### Multiple patterns

```conf
map f1 toggle_marker iregex 1 \\bERROR\\b 2 \\bWARNING\\b
```

Kitty supports up to 3 mark groups (numbered 1-3). Configure colors in `kitty.conf`:

```conf
mark1_foreground red
mark1_background gray
mark2_foreground green
# ... etc
```

> [!NOTE]
> Matching is per-line only, triggered when the line changes. Multi-line matches are not supported.

## Dynamic Marker Creation

Create markers at runtime instead of pre-defining them:

```conf
map f1 create_marker
map f2 remove_marker
```

- F1: enter marker definition mode (prompt has history for reuse)
- F2: remove a marker

Also controllable via [[028-remote-control]].

## Scrolling to Marks

Navigate scrollback buffer by marks:

```conf
map ctrl+p scroll_to_mark prev
map ctrl+n scroll_to_mark next
```

Jump to specific mark type:

```conf
map ctrl+1 scroll_to_mark prev 1
```

## Toggle Marker Syntax

```
toggle_marker <marker-type> <group-number> <pattern>
```

| Type | Description |
|------|-------------|
| `text` | Case-sensitive substring |
| `itext` | Case-insensitive substring |
| `regex` | Python regex |
| `iregex` | Case-insensitive Python regex |
| `function` | Custom Python function |

## Custom Marker Functions

Create a Python file with a generator function:

```python
def marker(text):
    # Highlight all letter X
    for i, ch in enumerate(text):
        if ch.lower() == 'x':
            yield i, i, 3  # start, end, group
```

Usage in `kitty.conf`:

```conf
map f1 toggle_marker function /path/to/mymarker.py
```

Or if saved in the kitty config directory:

```conf
map f1 toggle_marker function mymarker.py
```

#kitty-terminal #text-highlighting #regex-matching #configuration #terminal-productivity
