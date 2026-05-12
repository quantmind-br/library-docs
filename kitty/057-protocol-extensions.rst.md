---
title: Terminal protocol extensions
url: https://github.com/kovidgoyal/kitty/blob/master/docs/protocol-extensions.rst
source: git
fetched_at: 2026-05-04T15:58:23.387775757-03:00
rendered_js: false
word_count: 195
summary: Custom extensions to the terminal protocol enabling advanced features while maintaining compatibility with standard TTY byte stream processing.
tags:
    - terminal-emulator
    - protocol-extensions
    - tty
    - escape-codes
    - kitty-terminal
    - terminal-specification
category: reference
optimized: true
optimized_at: 2026-05-04T18:00:00Z
---
# Terminal protocol extensions

kitty extends the legacy terminal protocol to enable advanced features. Extensions are typically new or re-purposed escape codes.

## Design goals

- **Small and unobtrusive**: fill gaps in the xterm protocol without re-imagining the TTY.
- **Byte-stream compatible**: the TTY remains a device for efficiently processing text as a simple byte stream.
- **Easy to implement**: minimal extra functionality moved into the terminal program itself, encouraging adoption.

## Extensions overview

| Extension | Spec | Purpose |
|----------|------|---------|
| Graphics protocol | [[049-graphics-protocol]] | PNG/GIF rendering, image placement |
| Text sizing | [[059-text-sizing-protocol]] | Programmatic font size changes |
| Color control | [[045-color-stack]] | Foreground/background color stack |
| Colored underlines | [[060-underlines]] | Wavy, colored, styled underlines |
| Multiple cursors | [[055-multiple-cursors-protocol]] | Terminal-wide multi-cursor support |
| File transfer | [[048-file-transfer-protocol]] | Transfer files over TTY |
| Remote control | [[058-rc-protocol]] | Control kitty from scripts |
| Extended mouse | [[054-misc-protocol]] | SGR pixel mouse, window leave events |
| Feline UI | [[054-misc-protocol]] | Layout queries, cursor shape reports |

## Contributing

Discuss extensions, propose additions or changes via the [GitHub issue tracker](https://github.com/kovidgoyal/kitty/issues).
