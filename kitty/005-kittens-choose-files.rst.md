---
title: Selecting files, fast
title: Selecting files, fast
word_count: 317
summary: This document explains how to use and configure the choose-files kitten, a high-performance fuzzy file selector for the terminal that serves as a keyboard-friendly alternative to GUI file dialogs.
category: guide
optimized: true
optimized_at: 2026-05-04T20:45:08Z
---
# Selecting files, fast

The choose-files kitten provides a high-performance, keyboard-driven file selector for the terminal. It works like [fzf](https://github.com/junegunn/fzf/) but specializes in finding files, with support for filtering by file type, file type icons, content previews, and more. It is a drop-in replacement for GUI file dialogs. On Linux, with [[009-kittens-desktop-ui|desktop-ui]] kitten, most GUI programs can use it instead of regular file dialogs.

```
kitten choose-files
```

Type a few letters from the filename; once it is the top selection, press Enter. Tab selects a directory and moves into it; Shift+Tab moves up one directory level.

To insert a chosen file/directory into the shell prompt at the cursor position, use `insert_chosen_file` / `insert_chosen_directory`. From the command line:

```
some-command $(kitten choose-file)
```

> [!NOTE]
> This may not work in complex pipelines since it needs exclusive TTY access.

## Content preview dependencies

The kitten uses external programs for previews:
- [ffmpeg](https://www.ffmpeg.org/) — video previews
- [calibre](https://calibre-ebook.com) — ebook metadata and cover previews

## Creating shortcuts to favorite directories

In `choose-files.conf`:

```conf
map ctrl+t cd /tmp
map alt+p  cd ~/my/project
```

## Selecting multiple files

Use `--mode=files` to select multiple files. Press Shift+Enter or Ctrl+click to add files to the selection. Alt+click selects a range. Press Enter on the last file to finish. Click or Shift+Enter on a selected file to deselect it.

## Hidden and ignored files

Hidden files (starting with `.`) are hidden by default. Toggle via configuration or the runtime clickable link. The kitten respects `.gitignore` and `.ignore` files (configurable). Git ignore files only apply inside git working trees (requires `.git` directory). Global gitignore patterns can be specified in `choose-files.conf`.

## Selecting non-existent files (save dialogs)

Use `--mode=save-file`. After navigating to the target directory (Tab), press Ctrl+Enter to type a new filename. Alt+Enter modifies the top match's filename instead.

## Selecting directories

Use `--mode=dir`. Press Ctrl+Enter to accept the current directory, or Enter on a descendant directory to select it.

## Configuration

Create `choose-files.conf` in the kitty config directory. See [[037-conf|kitty.conf]] configuration directives.
