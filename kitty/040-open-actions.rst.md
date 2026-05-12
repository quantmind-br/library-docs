---
title: Scripting the mouse click
title: Scripting the mouse click
word_count: 382
summary: Customize terminal hyperlink behaviors and external file opening actions in kitty using open-actions.conf matching criteria and action definitions.
optimized: true
optimized_at: 2026-05-04T20:45:41Z
---
# Scripting the mouse click

kitty supports terminal hyperlinks and can take arbitrarily complex actions when links are clicked. Create `~/.config/kitty/open-actions.conf` to define behaviors.

## Quick example

```conf
# Open any image full-screen by ctrl+shift+clicking
protocol file
mime image/*
action launch --type=overlay kitten icat --hold -- ${FILE_PATH}
```

Run `ls --hyperlink=auto` and ctrl+shift+click an image filename.

> [!note]
> macOS `ls` lacks hyperlink support. Install [GNU Coreutils](https://www.gnu.org/software/coreutils/) via [Homebrew](https://formulae.brew.sh/formula/coreutils/) (provides `gls`).

## Entry structure

Each entry in `open-actions.conf` has:
1. One or more **matching criteria** (`protocol`, `mime`, etc.)
2. One or more **action** entries

Entries are separated by blank lines. Processing stops at the first match; put specific criteria first.

### Example: Multiple actions

```conf
# Tail a log file in a new OS Window with reduced font size
protocol file
ext log
action launch --title ${FILE} --type=os-window tail -f -- ${FILE_PATH}
action change_font_size current -2
```

> [!tip]
> Use `action_alias` in kitty.conf to define reusable action shortcuts.

## Available variables

| Variable | Description |
|----------|-------------|
| `URL` | Full URL being opened |
| `FILE_PATH` | Path portion of URL (unquoted) |
| `FILE` | Filename portion of path (unquoted) |
| `FRAGMENT` | Fragment after `#` in URL, or empty string |
| `NETLOC` | Hostname from URL, or empty string |
| `URL_PATH` | Path, query, and fragment portions, without unquoting |
| `EDITOR` | Configured terminal-based text editor |
| `SHELL` | Configured shell path, without arguments |

## Matching criteria

| Criterion | Format | Example |
|-----------|--------|---------|
| `protocol` | comma-separated list | `http, https` |
| `url` | regex matching entire (unquoted) URL | `^https://example\.com` |
| `fragment_matches` | regex matching fragment after `#` | `section-.*` |
| `mime` | comma-separated MIME types | `text/*, image/*, application/pdf` |
| `ext` | comma-separated file extensions | `jpeg, tar.gz` |
| `file` | shell glob pattern matching filename | `image-??.png` |

> [!note]
> MIME type for directories is `inode/directory`. Add custom MIME types by creating `mime.types` in the kitty config directory (one definition per line, e.g., `text/plain rst md`).

## File opening on different platforms

### macOS

- Use **Open With** in Finder
- Drag and drop files/URLs onto the kitty dock icon
- Set URL scheme handlers:
  ```sh
  kitty +runpy 'from kitty.fast_data_types import cocoa_set_url_handler; import sys; cocoa_set_url_handler(*sys.argv[1:]); print("OK")' ssh
  ```

### Linux

- Associate file types to open in kitty via desktop integration
- Default actions: text files in editor, images with icat, shell scripts in shell, SSH URLs via `ssh` command

### Command line

```sh
kitty +open file_or_url another_url ...

# macOS only
open -a kitty.app file_or_url another_url ...
```

## Custom launch actions

Create `launch-actions.conf` in the kitty config directory (same syntax as `open-actions.conf`) to customize how files are opened.

#kitty-terminal #terminal-emulator #hyperlinks #configuration
