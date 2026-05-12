---
title: Clipboard Manager | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/cli-clipboard
source: sitemap
fetched_at: 2026-04-26T08:38:39.543137404-03:00
rendered_js: false
word_count: 715
summary: This document provides a reference for the `dms cl` command-line utility, which functions as a Wayland clipboard manager featuring history tracking, search capabilities, and configurable settings.
tags:
    - wayland
    - clipboard-manager
    - cli-tools
    - linux-desktop
    - data-control
category: reference
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Version: 1.4

`dms cl` is a Wayland clipboard manager with history, search, and configurable settings. Uses the `ext_data_control_v1` protocol.

## Command Overview

| Command                      | Server Required | Description                              |
|------------------------------|-----------------|------------------------------------------|
| `dms cl copy [text]`         | No              | Copy text to clipboard                   |
| `dms cl paste`               | No              | Paste clipboard contents to stdout        |
| `dms cl watch [cmd]`         | No              | Watch clipboard changes                  |
| `dms cl history`             | Yes             | List clipboard history with previews      |
| `dms cl get <id>`            | Yes             | Get full entry data by ID                |
| `dms cl delete <id>`         | Yes             | Delete history entry by ID               |
| `dms cl clear`               | Yes             | Clear all clipboard history              |
| `dms cl search [query]`      | Yes             | Search history with filters              |
| `dms cl config get`          | Yes             | Get current config                       |
| `dms cl config set`          | Yes             | Update config options                    |

## Quick Start

```bash
# Copy text to clipboard
echo "hello" | dms cl copy
dms cl copy "hello world"
# Paste clipboard contents
dms cl paste
# View clipboard history
dms cl history
# Search history
dms cl search "password"
```

## Commands

### `dms cl copy [text] [flags]`

Copies data to the Wayland clipboard. Forks a background process by default.

| Argument  | Type     | Default                  | Description                      |
|-----------|----------|--------------------------|----------------------------------|
| `text`    | string   | stdin                    | Text to copy (omitted = read stdin) |

| Flag              | Description                              |
|-------------------|------------------------------------------|
| `-d, --download`  | Download URL to clipboard                |
| `-f, --foreground`| Stay in foreground (no fork)           |
| `-o, --paste-once`| Exit after first paste (one-shot copy)  |
| `-t, --type`      | MIME type (default: `text/plain;charset=utf-8`) |

```bash
dms cl copy "Hello, world!"
echo "piped content" | dms cl copy
dms cl copy < file.txt
dms cl copy -t image/png < screenshot.png
dms cl copy -o "temporary secret"
dms cl copy --download "https://example.com/image.png"
```

#### Download Mode

`--download` fetches a URL and copies it to clipboard as `text/uri-list`:

1. Downloads to `~/.cache/dms/clipboard/`
2. Validates as image or video
3. Offers two MIME types:
   - `text/uri-list` — native apps read the file directly
   - `application/vnd.portal.filetransfer` — Flatpaks retrieve via XDG portal

> [!note]
> XDG Desktop Portal's FileTransfer interface lets sandboxed Flatpak apps access downloads securely. Without the portal, only native apps work.

### `dms cl paste`

Reads current clipboard selection, writes to stdout.

```bash
dms cl paste
dms cl paste > output.txt
dms cl paste | wc -l
```

### `dms cl watch [command] [flags]`

Watches for clipboard changes.

| Flag       | Description                               |
|------------|-------------------------------------------|
| `--json`   | Output as JSON objects                    |
| `-s, --store` | Store changes to history database (no server needed) |

```bash
dms cl watch
dms cl watch notify-send
dms cl watch --json
dms cl watch --store
```

**JSON output format:**

```json
{"data":"clipboard content","mimeType":"text/plain","timestamp":1699900000,"size":17}
```

### `dms cl history`

Lists history entries with ID, type, timestamp, and preview. Requires DMS server.

| Flag    | Description          |
|---------|----------------------|
| `--json` | Output as JSON array |

```text
ID       Type        Timestamp            Preview
─────────────────────────────────────────────────────────────
1        text/plain  2024-01-15 10:30:00  Hello, world!
2        image/png   2024-01-15 10:31:00  [image 1920x1080]
3        text/plain  2024-01-15 10:32:00  Some longer text that gets trunca...
```

### `dms cl get <id>`

Retrieves full entry data by ID.

| Flag    | Description          |
|---------|----------------------|
| `--json` | Output full entry as JSON |

```bash
dms cl get 42
dms cl get 42 --json
dms cl get 42 > image.png
```

### `dms cl delete <id>`

Delete a history entry by ID. Requires DMS server.

### `dms cl clear`

Clear all clipboard history. Requires DMS server.

### `dms cl search [query] [flags]`

Search history with text matching and filters. Requires DMS server.

| Flag            | Default | Description                       |
|-----------------|---------|-----------------------------------|
| `-l, --limit`  | 50      | Max results (max: 500)            |
| `-o, --offset` | 0       | Result offset for pagination       |
| `-m, --mime`   | —       | Filter by MIME type substring     |
| `--images`      | —       | Only image entries                |
| `--text`        | —       | Only text entries                 |
| `--json`        | —       | Output as JSON                    |

```bash
dms cl search "password"
dms cl search --images
dms cl search --text "http"
dms cl search --limit 10 --offset 20
dms cl search -m "image/png"
```

## Configuration

### `dms cl config get`

Get current clipboard manager configuration as JSON.

### `dms cl config set [flags]`

| Flag                  | Description                          |
|-----------------------|--------------------------------------|
| `--max-history <n>`   | Max history entries to keep          |
| `--auto-clear-days <n>`| Delete entries older than N days     |
| `--clear-at-startup`  | Clear history on server start        |
| `--no-clear-at-startup` | Do not clear on startup            |
| `--disable`           | Disable clipboard manager entirely   |
| `--enable`            | Enable clipboard manager             |
| `--disable-history`   | Disable history persistence          |
| `--enable-history`    | Enable history persistence           |

```bash
dms cl config set --max-history 500
dms cl config set --auto-clear-days 7
dms cl config set --disable-history
dms cl config set --clear-at-startup
```

### Configuration File

Stored at `$XDG_CONFIG_HOME/DankMaterialShell/clsettings.json` (default: `~/.config/DankMaterialShell/clsettings.json`).

### Configuration Options

| Field            | Type | Default     | Description                                |
|------------------|------|-------------|--------------------------------------------|
| `disabled`       | bool | `false`     | Disable clipboard manager entirely          |
| `disableHistory` | bool | `false`     | Don't persist clipboard to database         |
| `maxHistory`     | int  | `100`       | Max entries to keep in history              |
| `maxEntrySize`   | int  | `10485760`  | Max single entry size in bytes (10MB)      |
| `autoClearDays`  | int  | `0`         | Auto-delete entries older than N days (0=disabled) |
| `clearAtStartup` | bool | `false`    | Clear history when server starts           |

**JSON schema:**

```json
{
  "disabled": false,
  "disableHistory": false,
  "maxHistory": 100,
  "maxEntrySize": 10485760,
  "autoClearDays": 0,
  "clearAtStartup": false
}
```

## IPC Methods

Programmatic access via JSON-RPC over the DMS IPC socket.

| Method                                   | Params                                        | Description                    |
|------------------------------------------|-----------------------------------------------|--------------------------------|
| `clipboard.getHistory`                   | none                                          | Get all history entries        |
| `clipboard.getEntry`                     | `{id: uint64}`                                | Get entry by ID                |
| `clipboard.deleteEntry`                  | `{id: uint64}`                                | Delete entry by ID             |
| `clipboard.clearHistory`                | none                                          | Clear all history              |
| `clipboard.search`                       | `{query?, limit?, offset?, mimeType?, isImage?}` | Search history           |
| `clipboard.getConfig`                    | none                                          | Get current config             |
| `clipboard.setConfig`                    | config fields                                 | Update config                 |

```bash
dms ipc call clipboard.search '{"query": "hello", "limit": 10}'
```

## Command Reference

| Command            | Description                |
|--------------------|----------------------------|
| `copy [text]`      | Copy to clipboard          |
| `paste`            | Paste from clipboard       |
| `watch [cmd]`      | Watch clipboard changes    |
| `history`          | List clipboard history     |
| `get <id>`         | Get entry by ID            |
| `delete <id>`      | Delete entry by ID         |
| `clear`            | Clear all history          |
| `search [query]`   | Search history             |
| `config get`       | Get configuration          |
| `config set`       | Update configuration       |

| Global Flag             | Description                    |
|-------------------------|--------------------------------|
| `-c, --config <path>`  | Custom DMS config directory    |
| `-h, --help`            | Show help                      |
