---
title: Files, links, & scripts | Warp
url: https://docs.warp.dev/terminal/more-features/files-and-links
source: sitemap
fetched_at: 2026-04-29T15:03:03.900318124-03:00
rendered_js: false
word_count: 269
summary: This document explains how to interact with files, folders, URLs, and scripts within the Warp terminal, including configuration of default editors and link handling.
tags:
    - warp-terminal
    - file-navigation
    - workflow-automation
    - editor-integration
    - terminal-features
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
## Files & Links

Warp opens files, folders, and URLs from Blocks. Supports `https`, `ftp`, `file`, and other protocols. Files open in configured editors; web links open in your default browser.

> [!info]
> Warp supports iTerm2 and Kitty Image protocols on macOS and Linux. Some tools require `$TERM=kitty`; set this before the command if needed.

### File Path Parsing

Warp parses relative and absolute paths, capturing line/column numbers in these formats:

- `file_name:line_num`
- `file_name:line_num:column_num`
- `file_name[line_num, column_num]`
- `file_name(line_num, column_num)`
- `file_name, line: line_num, column: column_num`
- `file_name, line: line_num, in`

### Opening Links

1. `CMD`-click a hovered link to open directly.
2. Click normally to show "Open File/Folder/Link" tooltip.
3. Right-click for context menu with Copy absolute path/URL.

### Additional File Opening Methods

- Drag-drop folder/file onto Warp dock icon opens new tab in that directory.
- Right-click folder/file in Finder → Services → "Open new Warp Tab | Window here".
- Configure default editor via **Settings** → **Features** → **General** → **Choose an editor to open file links**. Select "Default App" for system defaults.

### Supported Editors

> Non-exhaustive list. Submit additions via [GitHub feedback](https://docs.warp.dev/support-and-community/troubleshooting-and-support/sending-us-feedback#sending-warp-feedback).

1. `$EDITOR`
2. Visual Studio Code
3. JetBrains IDEs (WebStorm, PhpStorm, GoLand, PyCharm, DataGrip, DataSpell, Rider, RubyMine)
4. Zed and Zed Preview
5. Cursor
6. Windsurf
7. Sublime Text
8. Android Studio

![Files & Links Demo](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F4009768362-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPsjNxoJ0NFCXW6rRdHH3%252Fuploads%252Fgit-blob-4b35a52c9e42ce96877811f1ce788c85411727f5%252Ffiles-links-demo.gif%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=a54aacfb&sv=2)

## Scripts

Warp opens `.command` and Unix Executable files from Finder directly.

1. Find a `.command` or Shell script in Finder.
2. Right-click and open with Warp.

> [!warning]
> Ensure executable permissions before running (e.g., `chmod +x script.command`).

![Scripts Demo](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F4009768362-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPsjNxoJ0NFCXW6rRdHH3%252Fuploads%252Fgit-blob-f7a1e04f36dc80e8840fd8b556d1e2ab92d933be%252Fscript-demo.gif%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=df5b55f3&sv=2)

#warp-terminal #file-navigation #workflow-automation
