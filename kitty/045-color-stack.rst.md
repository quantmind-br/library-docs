---
title: Color control
title: Color control
word_count: 376
summary: Terminal color management protocol using OSC 30001/30101 for push/pop stack operations and OSC 21 for querying and setting colors with string keys.
optimized: true
optimized_at: 2026-05-04T20:45:41Z
---
# Color control

## Saving and restoring colors

Full-screen applications with custom themes can save/restore colors using kitty's push/pop escape codes:

```
<ESC>]30001<ESC>\  # push onto stack
<ESC>]30101<ESC>\  # pop from stack
```

This saves/restores: default foreground, background, selection colors, cursor color, and the full 256-color ANSI table.

> [!note]
> In July 2020, xterm copied this protocol using incompatible codes (XTPUSHCOLORS, XTPOPCOLORS, XTREPORTCORS) without acknowledgement. kitty now supports xterm's codes for interoperability and saves the entire ANSI table.

## Querying and setting colors

kitty uses a single-number protocol with string keys (unlike XTerm's fragmented OSC 4/5/6/10-19/104/105/106/110-119 approach).

**Format:**
```
<OSC> 21 ; key=value ; key=value ; ... <ST>
```

Where `<OSC>` is `0x1b 0x5d`, `<ST>` is `0x07` or `0x1b 0x5c`.

**Keys:**
| Key | Meaning | Dynamic behavior |
|-----|---------|------------------|
| `0`-`255` | ANSI color table entries | Not allowed |
| `foreground` | Default foreground color | N/A |
| `background` | Default background color | N/A |
| `selection_background` | Selection background color | Reverse video |
| `selection_foreground` | Selection foreground color | Reverse video |
| `cursor` | Text cursor color | Uses foreground color |
| `cursor_text` | Text under cursor color | Uses background color |
| `visual_bell` | Visual bell color | Auto-selects based on screen |
| `transparent_background_color1`...`7` | Background with specified opacity | Unset (uses `background_opacity`) |

### Querying colors

Send `?` as the value:

```
<OSC> 21 ; foreground=? ; cursor=? <ST>
```

Terminal responds with the encoded color value (or empty if dynamic):

```
<OSC> 21 ; foreground=rgb:ff/00/00 ; cursor= <ST>
```

If a color has no defined value (e.g., reverse video effect), respond with only the key and `=`.

### Setting colors

Set a color to an encoded value or empty string (dynamic):

```
<OSC> 21 ; foreground=green ; cursor= ; background <ST>
```

- `foreground=green` sets to green
- `cursor=` sets cursor to dynamic (takes text color)
- `background` (no `=`) resets background to default

Combine set and query in one escape code:

```
<OSC> 21 ; foreground=white ; foreground=? <ST>
```

## Color value encoding

**Three RGB formats:**

1. `rgb:<red>/<green>/<blue>` where each component is `h`, `hh`, `hhh`, or `hhhh` (4/8/12/16 bits, scaled)

2. `#<h...>` — hex shorthand:
   - `#RGB` (4 bits each)
   - `#RRGGBB` (8 bits each)
   - `#RRRGGGBBB` (12 bits each)
   - `#RRRRGGGGBBBB` (16 bits each)
   
   Unlike `rgb:`, values are taken as most significant bits, not scaled.

3. `rgbi:<red>/<green>/<blue>` — floating-point 0.0 to 1.0

**Alpha component:** Append `@number` (0-1) to any format:
```
red@0.5 rgb:ff0000@0.1 #ff0000@0.3
```

Default alpha is `1.0`. Values outside 0-1 are clipped.

Standard color names (case-insensitive) are also accepted.

#terminal-emulation #escape-sequences #color-management
