---
title: kitty-diff
url: https://github.com/kovidgoyal/kitty/blob/master/docs/kittens/diff.rst
source: git
fetched_at: 2026-05-04T15:57:57.46225501-03:00
rendered_js: false
word_count: 247
summary: Fast side-by-side diff tool with syntax highlighting, images, keyboard navigation, and git integration.
tags:
    - kitty-terminal
    - diff-tool
    - version-control
    - git-integration
optimized: true
optimized_at: 2026-05-04T18:00:00Z
---
# kitty-diff

*Fast side-by-side diff with syntax highlighting and images*

## Installation

Install kitty: [[023-binary|Quickstart]]

## Usage

```bash
# Diff two files
kitten diff file1 file2

# Diff directories recursively
kitten diff dir1 dir2

# Short alias
alias d="kitten diff"
d file1 file2
```

## Keyboard Controls

| Action | Shortcut |
|--------|----------|
| Quit | `Q` |
| Scroll line up | `K`, `Up` |
| Scroll line down | `J`, `Down` |
| Scroll page up | `PgUp` |
| Scroll page down | `PgDn` |
| Scroll to top | `Home` |
| Scroll to bottom | `End` |
| Scroll to next page | `Space`, `PgDn`, `Ctrl+F` |
| Scroll to previous page | `PgUp`, `Ctrl+B` |
| Scroll down half page | `Ctrl+D` |
| Scroll up half page | `Ctrl+U` |
| Scroll to next change | `N` |
| Scroll to previous change | `P` |
| Increase context lines | `+` |
| Decrease context lines | `-` |
| All lines of context | `A` |
| Restore default context | `=` |
| Search forwards | `/` |
| Search backwards | `?` |
| Clear search / exit | `Esc` |
| Next match | `>`, `.` |
| Previous match | `<`, `,` |
| Copy selection | `y` |
| Copy or exit | `Ctrl+C` |

## Git Integration

Add to `~/.gitconfig`:

```ini
[diff]
    tool = kitty
    guitool = kitty.gui
[difftool]
    prompt = false
    trustExitCode = true
[difftool "kitty"]
    cmd = kitten diff $LOCAL $REMOTE
[difftool "kitty.gui"]
    cmd = kitten diff $LOCAL $REMOTE
```

Use:

```bash
git difftool --no-symlinks --dir-diff
```

## Why kitty-only?

Uses kitty-specific features: [[049-graphics-protocol|kitty graphics protocol]], [[033-keyboard-protocol|extended keyboard protocol]], terminal program infrastructure. Entire implementation is under 3000 lines of code.

## Configuration

Create `~/.config/kitty/diff.conf`. See the [[011-kittens-diff|sample diff.conf]] for all options.

#kitty-terminal #diff-tool #version-control #git-integration
