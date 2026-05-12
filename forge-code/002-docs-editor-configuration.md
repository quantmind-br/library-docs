---
title: "Editor Configuration for ForgeCode Prompts"
url: https://forgecode.dev/docs/editor-configuration/
source: sitemap
fetched_at: 2026-04-30T14:09:06.345177969-03:00
rendered_js: false
word_count: 270
summary: "Use the `:edit` command to compose complex prompts in your preferred editor before sending them to ForgeCode."
tags:
  - forgecode
  - cli-tools
  - editor-configuration
  - environment-variables
  - productivity-tools
category: guide
optimized: true
---
# Editor Configuration for ForgeCode Prompts

> **TL;DR**
> Use `:edit` to compose prompts in your editor of choice. Set `FORGE_EDITOR` or `EDITOR` to configure your preferred editor.

## Why Use `:edit`?
- **Structure**: Easily compose multi-line prompts with steps, lists, or code snippets.
- **Iteration**: Draft, review, and refine prompts before sending.
- **Pasting**: Organize logs, stack traces, or code blocks naturally.

## Editor Configuration

### Supported Editors
| Editor | Command | Notes |
|--------|---------|-------|
| VS Code | `code --wait` | Required for blocking behavior |
| Vim/Neovim | `vim` | Blocks by default |
| nano | `nano` | Blocks by default |
| Sublime Text | `subl --wait` | Use `--wait` flag |
| IntelliJ IDEA | `idea --wait` | Use `--wait` flag |
| Zed | `zed --wait` | Use `--wait` flag |
| Emacs (GUI) | `emacsclient -c` | GUI mode |
| Emacs (Terminal) | `emacs -nw` | Terminal mode |

### Environment Variables
ForgeCode checks these variables in order:
1. `FORGE_EDITOR` (ForgeCode-only)
2. `EDITOR` (System-wide)

> **Priority**: `FORGE_EDITOR` overrides `EDITOR`.

#### Setting Variables
| Method | Scope | Example |
|--------|-------|---------|
| `~/.env` | Persistent, ForgeCode-only | `FORGE_EDITOR="code --wait"` |
| `~/.zshrc`/`~/.bashrc` | Persistent, system-wide | `export EDITOR=vim` |
| Inline | Temporary | `export FORGE_EDITOR=nano` |

> **Note**: Reload your shell (`source ~/.zshrc`) or open a new terminal after editing.

## When to Use `:edit`
- **Complex prompts**: Multi-paragraph, structured, or iterative content.
- **Pasting content**: Logs, code blocks, or external data.
- **Long-form drafting**: When inline composition becomes cumbersome.

> **Tip**: Pair with [multiline input](https://forgecode.dev/docs/zsh-support/#multiline-text) for shorter structured prompts.