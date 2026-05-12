---
title: Codex IDE extension settings
url: https://developers.openai.com/codex/ide/settings.md
source: llms
fetched_at: 2026-04-30T10:15:43.750051714-03:00
rendered_js: false
word_count: 203
summary: This document provides instructions for configuring the Codex IDE extension settings within the editor and outlines the purpose of various available configuration parameters.
tags:
    - ide-extension
    - configuration-settings
    - codex-cli
    - vs-code
    - development-tools
category: configuration
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Codex IDE extension settings

Customize the Codex IDE extension.

## Change a setting

1. Open your editor settings.
2. Search for `Codex` or the setting name.
3. Update the value.

The IDE extension uses the Codex CLI. Configure default model, approvals, and sandbox settings in the shared `~/.codex/config.toml` instead of editor settings. See [[055-config-basic|Config basics]].

The extension also honors VS Code's built-in chat font settings for Codex conversation surfaces.

## Settings reference

| Setting | Description |
|---------|-------------|
| `chat.fontSize` | Chat text in Codex sidebar, including conversation content and composer |
| `chat.editor.fontSize` | Code-rendered content in Codex conversations (code snippets, diffs) |
| `chatgpt.cliExecutable` | Development only: path to Codex CLI executable. Don't set unless actively developing the CLI |
| `chatgpt.commentCodeLensEnabled` | Show CodeLens above to-do comments for Codex completion |
| `chatgpt.localeOverride` | Preferred language for Codex UI. Leave empty for auto-detect |
| `chatgpt.openOnStartup` | Focus Codex sidebar when extension finishes starting |
| `chatgpt.runCodexInWindowsSubsystemForLinux` | Windows only: run Codex in WSL when available. Use when repositories and tooling live in WSL2 or you need Linux-native tooling. Otherwise, Codex runs natively on Windows with the Windows sandbox. Changing reloads VS Code |

#ide #vscode #settings #configuration #codex