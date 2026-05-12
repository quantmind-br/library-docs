---
title: Built-in code editor | Warp
url: https://docs.warp.dev/code/code-editor
source: sitemap
fetched_at: 2026-04-29T15:03:19.882323337-03:00
rendered_js: false
word_count: 245
summary: This document provides an overview of the native code editor integrated into Warp, explaining how to open, manage, and edit files directly within the terminal environment.
tags:
    - warp-terminal
    - code-editor
    - file-management
    - syntax-highlighting
    - lsp-integration
    - editor-configuration
category: guide
optimized: true
optimized_at: 2026-04-29T15:03:19.882323337-03:00
---
A native code editor for quick in-flow edits alongside Agent conversations. Features: syntax highlighting, tabbed viewer, find/replace, Vim keybindings, file tree.

## Open Files

1. Click a file path in terminal output or AI conversation → "Open in Warp"
2. Command Palette (`CMD + O` / `CTRL + SHIFT + O`) in Git-tracked repos
3. Magnifying glass icon in the pane coding toolbelt

**Save**: `CMD + S` (macOS) / `CTRL + S` (Windows/Linux)

## Tabbed File Viewer

- Enabled by default for new users (toggle: **Settings** > **Features** > **General** > **Group files into a single editor pane**)
- Reorder, close, or drag tabs between panes
- Drag pane into another to merge

## File Layout Options

**Settings** > **Features** > **General** > **Choose a layout to open files in Warp**:

- **Split pane** — new files alongside current editor
- **New tab** — new files in own tabbed viewer

## Supported Languages

Rust, Go, YAML, Python, JavaScript/TypeScript, JSX/TSX, Java/Groovy, C++, Shell/Bash, C#, HTML, CSS, C, JSON, HCL/Terraform, Lua, Ruby, PHP, TOML, Swift, Kotlin, Starlark, SQL, Powershell, Elixir.

## Shared Buffers

Opening the same file in multiple tabs/panes keeps them in sync. Edits and external changes (e.g., branch switch) reflect across all views.

## Other Features

- [[180-code-code-editor-language-server-protocol|Language Server Protocol (LSP)]] — hover, go-to-definition, find references, inline diagnostics, format-on-save
- [[179-code-code-editor-find-and-replace|Find and Replace]] — regex, case sensitivity, smart case preservation
- [[177-code-code-editor-code-editor-vim-keybindings|Vim Keybindings]] — modal editing
- [[178-code-code-editor-file-tree|File Tree]] — project browsing and context attachment
