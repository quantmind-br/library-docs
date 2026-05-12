---
title: Modern text editing | Warp
url: https://docs.warp.dev/terminal/editor
source: sitemap
fetched_at: 2026-04-29T15:02:20.898533074-03:00
rendered_js: false
word_count: 114
summary: Soft wrapping, copy-on-select, and automatic bracket/quote completion features in the Warp input editor.
tags:
    - text-editing
    - terminal-configuration
    - soft-wrapping
    - copy-on-select
    - autocomplete
    - input-editor
category: configuration
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
# Modern Text Editing

Warp's input editor supports soft wrapping, copy-on-select, and IDE-style bracket/quote completion.

## Soft Wrapping

When an autosuggestion goes off-screen, the input editor scrolls horizontally. Some operations treat soft-wrapped lines as a single logical line (`TRIPLE-CLICK`); others treat them as visible separate lines (`UP`/`DOWN`, `SHIFT-UP`/`SHIFT-DOWN`).

## Copy on Select

Automatically copies selected text within [[224-terminal-blocks|Blocks]].

- **Settings** → **Features** → **Terminal** → toggle **Copy on select**
- [[101-terminal-command-palette|Command Palette]] → search "Copy on select"

## Autocomplete Quotes, Parentheses, and Brackets

Automatically completes quotes, brackets, and parentheses like an IDE.

- **Settings** → **Features** → **Text Editing** → toggle **Autocomplete quotes**
- [[101-terminal-command-palette|Command Palette]] → search "Autocomplete quotes"

![Text Editor Input Demo](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F4009768362-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPsjNxoJ0NFCXW6rRdHH3%252Fuploads%252Fgit-blob-example%252Ftext-editor-demo.gif%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=example&sv=2)
