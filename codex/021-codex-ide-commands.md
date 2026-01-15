---
title: Codex IDE extension commands
url: https://developers.openai.com/codex/ide/commands.md
source: llms
fetched_at: 2026-01-13T18:59:51.413891444-03:00
rendered_js: false
word_count: 157
summary: This document provides a reference for Codex IDE extension commands, listing their IDs, default key bindings, and instructions for assigning custom keyboard shortcuts.
tags:
    - ide-extension
    - vs-code
    - key-bindings
    - command-palette
    - codex-commands
category: reference
---

# Codex IDE extension commands

Use these commands to control Codex from the VS Code Command Palette. You can also bind them to keyboard shortcuts.

## Assign a key binding

To assign or change a key binding for a Codex command:

1. Open the Command Palette (**Cmd+Shift+P** on macOS or **Ctrl+Shift+P** on Windows/Linux).
2. Run **Preferences: Open Keyboard Shortcuts**.
3. Search for `Codex` or the command ID (for example, `chatgpt.newChat`).
4. Select the pencil icon, then enter the shortcut you want.

## Extension commands

| Command                 | Default key binding                        | Description                                               |
| ----------------------- | ------------------------------------------ | --------------------------------------------------------- |
| `chatgpt.addToThread`   | -                                          | Add selected text range as context for the current thread |
| `chatgpt.newChat`       | macOS: `Cmd+N`<br/>Windows/Linux: `Ctrl+N` | Create a new thread                                       |
| `chatgpt.implementTodo` | -                                          | Ask Codex to address the selected TODO comment            |
| `chatgpt.newCodexPanel` | -                                          | Create a new Codex panel                                  |
| `chatgpt.openSidebar`   | -                                          | Opens the Codex sidebar panel                             |