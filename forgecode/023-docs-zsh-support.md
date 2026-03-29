---
title: ForgeCode
url: https://forgecode.dev/docs/zsh-support/
source: sitemap
fetched_at: 2026-03-29T16:30:51.315541-03:00
rendered_js: false
word_count: 519
summary: This document explains how to interact with ForgeCode directly from a native shell session using sentinel commands to manage agents, conversations, and file context.
tags:
    - cli-tool
    - shell-integration
    - ai-workflow
    - command-line-interface
    - terminal-productivity
category: guide
---

ForgeCode's interactive mode runs in its own environment. That means your ZSH aliases, custom functions, and shell tooling don't work inside it. You're stuck choosing between AI help and your own productivity setup.

The `:` sentinel character solves this. It lets you send prompts to ForgeCode from your native ZSH session — no environment switch, no lost context, no broken aliases.

Shell commands and AI prompts live in the same workflow. Context carries across both.

Press `TAB` after `:`

Type `:` then immediately press **`TAB`** to open the command completion list — switch agents, start a new conversation, open the editor, and more.

### Basic Prompts[​](#basic-prompts "Direct link to Basic Prompts")

Prompts go to your last-used agent. If this is your first interaction, it defaults to ForgeCode. The conversation continues across prompts until you run `:new`.

### Agent Selection[​](#agent-selection "Direct link to Agent Selection")

Switch agents by prefixing the agent name after `:`:

ForgeCode prints a confirmation and updates your terminal's right-hand prompt (RPROMPT):

All subsequent bare `:` prompts now go to sage:

You can also pass a prompt inline as a shortcut — this switches the agent and sends the prompt in one step:

Don't know the agent name?

Run `:agent` to pick from a list of all configured agents.

### Starting a New Conversation[​](#starting-a-new-conversation "Direct link to Starting a New Conversation")

ForgeCode carries conversation context forward indefinitely within a session, until a terminal window is closed. When you move to a different task and don't want the previous context bleeding in, run `:new`:

This clears the conversation history and starts fresh. The active agent stays the same.

You can also pass a prompt directly — `:new` starts the fresh conversation and sends it in one step:

### Switching Conversations[​](#switching-conversations "Direct link to Switching Conversations")

To switch to a different existing conversation, run `:conversation`:

This opens a list of your saved conversations. Select one to switch to it.

To jump back to the last conversation you were in, use the `-` shorthand:

### File Tagging[​](#file-tagging "Direct link to File Tagging")

Tag files in your prompts with `@` followed by a partial name, then press **`TAB`** :

Press `TAB` after `@` to pick a file

After typing `@` and a few characters, press **`TAB`** to open a fuzzy file picker. Type to filter, arrow keys to navigate, `Enter` to select. The full file path is inserted into your prompt automatically. `.gitignore` is respected.

If `fd` and `fzf` aren't installed, use the full path directly:

### Multiline Text[​](#multiline-text "Direct link to Multiline Text")

When your prompt needs structure (lists, steps, logs), insert line breaks directly in the prompt composer:

- **Windows/Linux:** `Shift+Enter`
- **macOS:** `Option+Enter`

This lets you write multiline prompts without sending early.

### `:edit` as an Alternative[​](#edit-as-an-alternative "Direct link to edit-as-an-alternative")

For longer prompts, use `:edit` instead of typing everything inline:

This opens your configured editor from `$FORGE_EDITOR` or `$EDITOR`. Write your prompt, save, and close the editor to send it.

Example (VS Code):

### Retrying a Request[​](#retrying-a-request "Direct link to Retrying a Request")

If you cancel a prompt mid-flight with `Ctrl+C` and want to run it again, use `:retry`:

This resends the last request without you having to retype it. Most useful after an accidental interrupt or a timeout.

Start with these two commands — they cover most issues:

If both run cleanly and things still aren't working, join us on [Discord](https://discord.gg/kRZBPpkgwq) and we'll help you sort it out.