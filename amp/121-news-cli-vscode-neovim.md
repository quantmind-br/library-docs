---
title: Amp CLI connects to VS Code and Neovim
url: https://ampcode.com/news/cli-vscode-neovim
source: crawler
fetched_at: 2026-02-06T02:08:30.924171543-03:00
rendered_js: false
word_count: 108
summary: This document explains how to integrate the Amp CLI with VS Code and Neovim to enable direct file access and editing within the IDE.
tags:
    - amp-cli
    - ide-integration
    - vs-code
    - neovim
    - development-tools
    - code-editing
category: guide
---

You can now connect the [Amp CLI](https://ampcode.com/manual#getting-started-command-line-interface) to VS Code and Neovim.

This allows Amp to access your current file, selected text, and diagnostics. It also enables Amp to edit files directly through your IDE.

All that's required is the latest version of the Amp CLI, and either the [Neovim plugin](https://github.com/sourcegraph/amp.nvim) or the [Amp VS Code extension](https://marketplace.visualstudio.com/items?itemName=sourcegraph.amp). Then you can run `amp --ide` from your project root and the CLI will connect to the IDE in the current workspace.

Here, for example, is the Amp CLI connected to Neovim:

And here is the Amp CLI connected to VS Code:

Learn more about the new integration in the [manual](https://ampcode.com/manual#ide).