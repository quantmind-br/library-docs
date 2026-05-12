---
title: Mouse pointer shapes
title: Mouse pointer shapes
word_count: 305
summary: Escape code protocol for programmatically changing, querying, and managing mouse pointer shapes with stack-based push/pop.
category: reference
optimized: true
optimized_at: 2026-05-04T20:46:03Z
---
# Mouse pointer shapes

Escape code protocol for terminal programs to change mouse pointer shape (buttons/links, resize, etc.). Based on xterm proposal with system-independent names, stack-based push/pop, and query support.

## Escape code format

```
<OSC> 22 ; <optional first char> <comma-separated list of shape names> <ESC>\
```

`OSC` = `<ESC>]`. Demo all shapes with `kitten mouse-demo`.

### Examples

```sh
<OSC> 22 ; pointer <ESC>\           # Set to pointing hand
<OSC> 22 ; <ESC>\                    # Reset to default
<OSC> 22 ; >wait <ESC>\              # Push shape onto stack
<OSC> 22 ; < <ESC>\                  # Pop from stack
<OSC> 22 ; ?__current__ <ESC>\       # Query current shape
```

## Operations

| First char | Operation |
|------------|-----------|
| `=` or omitted | Set shape |
| `>` | Push shapes onto stack |
| `<` | Pop from stack |
| `?` | Query support |

## Stack behavior

- Stack maintains shapes with last added at top (current shape)
- Minimum stack size: 16
- Full stack evicts bottom entry
- Empty stack = terminal uses default pointer
- Main and alternate screens have separate stacks
- Reset empties both stacks

> [!note]
> Text selection dragging and URL hovering may override shape settings.

## Querying

```sh
# Query current shape
<OSC> 22 ; ?__current__ <ESC>\
# Response: <OSC> 22 ; shape_name <ESC>\

# Check support for shapes
<OSC> 22 ; ?pointer,crosshair,no-such-name,wait <ESC>\
# Response: <OSC> 22 ; 1,1,0,1 <ESC>\
```

### Special query names

| Name | Returns |
|------|---------|
| `__current__` | Currently set shape |
| `__default__` | Default shape name |
| `__grabbed__` | Shape when mouse is grabbed |

## Pointer shape names

All conforming terminals must support these CSS-based names (characters: `a-z0-9_-`):

| | | | | |
|---|---|---|---|---|
| alias | cell | copy | crosshair | default |
| e-resize | ew-resize | grab | grabbing | help |
| move | n-resize | ne-resize | nesw-resize | no-drop |
| not-allowed | ns-resize | nw-resize | nwse-resize | pointer |
| progress | s-resize | se-resize | sw-resize | text |
| vertical-text | w-resize | wait | zoom-in | zoom-out |

> [!tip]
> Run `kitten mouse-demo` to see all shapes.

## xterm compatibility

Original xterm proposal used X11/cursorfont.h names. Terminals may implement these as aliases for CSS names. Basic usage (no leading char, single name) is xterm-compatible.

#terminal-emulator #mouse-pointer #cursor-shapes #xterm-compatibility
