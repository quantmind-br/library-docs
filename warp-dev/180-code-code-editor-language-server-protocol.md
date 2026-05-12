---
title: Language Server Protocol (LSP) | Warp
url: https://docs.warp.dev/code/code-editor/language-server-protocol
source: sitemap
fetched_at: 2026-04-29T15:03:21.333026445-03:00
rendered_js: false
word_count: 330
summary: This document explains how to enable and use Language Server Protocol (LSP) features within the Warp terminal code editor to achieve IDE-like code intelligence.
tags:
    - warp-terminal
    - code-editor
    - language-server-protocol
    - lsp
    - developer-tools
    - ide-features
category: guide
optimized: true
optimized_at: 2026-04-29T15:03:21.333026445-03:00
---
LSP provides IDE-grade code intelligence: hover docs, go-to-definition, find references, inline diagnostics, and format-on-save.

## Supported Languages

Warp ships with support for Rust, Go, Python, TypeScript/JavaScript, and C/C++.

> [!note]
> Request additional languages via [GitHub Issues](https://github.com/warpdotdev/Warp/issues).

## How It Works

`cd` into a workspace with enabled servers → Warp auto-starts them in the background. Features activate after server initialization. Edits sync incrementally. Closing all files/terminals shuts down idle servers.

> [!info]
> Warp uses your shell's `PATH` to locate server binaries. If not found, Warp can install it.

## Enable and Manage Servers

**Per workspace** (Git repository root). When opening a supported file, the editor footer shows an enable option. Alternatively: **Settings** > **Code** > **Indexing and projects**.

### Server Status Indicator (Footer)

| Icon | Status | Action |
|------|--------|--------|
| 🟢 Green | Running | — |
| 🟡 Yellow | Starting/Processing | — |
| 🔴 Red | Failed | Click to see options |
| ⚪ Gray | Stopped | — |

Click the icon for restart, stop, start, or view logs.

### Server Logs

Access via footer menu or **Settings** > **Code** > **Indexing and projects**.

## Editor Features

### Hover Information
Hover over a symbol to see type signature, docs, and rich content.

### Go to Definition
`CMD-click` (macOS) or `CTRL-click` (Windows/Linux). Symbol underlines on hover.

### Find References
`CMD-click` on a symbol at its definition → references card across workspace.

### Inline Diagnostics
Errors/warnings shown as dashed underlines. Hover for full message.

### Format on Save
`CMD + S` / `CTRL + S` triggers server formatting before disk write.

### Right-Click Context Menu
LSP-powered actions when server is connected.

> [!info]
> LSP features sync across [[181-code-code-editor#shared-buffers|shared buffers]].

## Limitations

- **Local sessions only** — not available over SSH or WSL. See [#6831](https://github.com/warpdotdev/Warp/issues/6831) and [#6744](https://github.com/warpdotdev/Warp/issues/6744).
- **One server per language** — no custom server configurations.
- **Project-scoped** — operates at Git repository root level.
- **Feature-dependent** — some features require server support.
