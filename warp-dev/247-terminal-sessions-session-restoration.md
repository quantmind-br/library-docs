---
title: "Session restoration"
url: https://docs.warp.dev/terminal/sessions/session-restoration
source: sitemap
fetched_at: 2026-04-29T15:02:44-03:00
rendered_js: false
word_count: 161
summary: This document explains the functionality of session restoration in Warp, including how to configure the feature, how the underlying SQLite database operates, and how to manage or clear session history.
tags:
    - session-restoration
    - terminal-productivity
    - warp-settings
    - sqlite-database
    - data-persistence
category: configuration
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
# Session Restoration

Session restoration restores your terminal state — windows, tabs, and panes — on app startup.

## Enable / Disable

Enabled by default. Toggle off at **Settings** > **Features** > **Restore windows, tabs, and panes on startup**.

> [!info]
> On Linux, opening windows at a specific position is not supported in Wayland.

> [!warning]
> Toggling off Session Restoration does not clear the SQLite database; Warp stops recording new output.

## How It Works

![Session Restoration Demo](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F4009768362-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPsjNxoJ0NFCXW6rRdHH3%252Fuploads%252Fgit-blob-eea5d549c432c9c124c175120bc2b901b1add9fb%252Fsessions-block_restoration.gif%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=2bbfa94a&sv=2)

Warp saves session state to a SQLite database on your computer. Each quit overwrites the previous session.

## SQLite Database

Inspect the database directly:

```bash
sqlite3 "$HOME/Library/Group Containers/2BBY89MBSN.dev.warp/Library/Application Support/dev.warp.Warp-Stable/warp.sqlite"
```

## Clearing the Database

> [!danger]
> This is destructive and will delete all sessions and block history. It also interferes with the running session's ability to save content; close Warp before running removal commands.

Two options:

- **In-app:** Clear blocks from your running Warp session with `CMD-K`.
- **Filesystem:** Delete the SQLite file:

```bash
rm -f "$HOME/Library/Group Containers/2BBY89MBSN.dev.warp/Library/Application Support/dev.warp.Warp-Stable/warp.sqlite"
```

#terminal #session-restoration #sqlite-database
