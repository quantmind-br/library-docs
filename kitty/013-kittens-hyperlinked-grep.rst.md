---
title: Hyperlinked grep
url: https://github.com/kovidgoyal/kitty/blob/master/docs/kittens/hyperlinked_grep.rst
source: git
fetched_at: 2026-05-04T15:57:59.477208007-03:00
rendered_js: false
word_count: 158
summary: Search files with ripgrep and click results to open directly in your editor at the matching line.
tags:
    - kitty-terminal
    - ripgrep
    - text-editor-integration
    - command-line-tools
optimized: true
optimized_at: 2026-05-04T18:00:00Z
---
# Hyperlinked grep

*Clickable ripgrep results that open in your editor at the matching line*

> [!note]
> ripgrep 13.0+ supports hyperlinks natively. Add `alias rg="rg --hyperlink-format=kitty"` instead of using this kitten.

## Setup

Create `~/.config/kitty/open-actions.conf`:

```conf
# Open files with fragment in vim (fragments from hyperlink-grep kitten)
protocol file
fragment_matches [0-9]+
action launch --type=overlay --cwd=current vim +${FRAGMENT} -- ${FILE_PATH}

# Open text files without fragments in editor
protocol file
mime text/*
action launch --type=overlay --cwd=current -- ${EDITOR} -- ${FILE_PATH}
```

## Usage

```bash
# Search
kitten hyperlinked-grep something

# Click any result line (hold Ctrl+Shift) to open in vim at that line

# Or use keyboard: open_selected_hyperlink action

# Alias
alias hg="kitten hyperlinked-grep"
hg some-search-term
```

See [[040-open-actions|open-actions]] for customizing URL click actions.

## Hyperlink Control

Control which ripgrep output parts get linked via `--kitten hyperlink`:

| Value | Effect |
|-------|--------|
| `matching_lines` | Only match lines linked |
| `file_headers,context_lines` | File headers + context lines linked, not matches |
| `none` | Pass through to `rg` directly, no hyperlinking |
| (default) | All of the above linked |

`--kitten hyperlink` can be specified multiple times.

## ripgrep Options

Forward any `rg` CLI option to the kitten. **Do not** use options that change output format (the kitten parses rg output).

Unsupported options:
- `--context-separator`
- `--field-context-separator`
- `--field-match-separator`
- `--json`
- `-I --no-filename`
- `-0 --null`
- `--null-data`
- `--path-separator`

#kitty-terminal #ripgrep #text-editor-integration
