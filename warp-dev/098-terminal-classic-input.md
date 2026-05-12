---
title: Classic Input | Warp
url: https://docs.warp.dev/terminal/classic-input
source: sitemap
fetched_at: 2026-04-29T15:02:11.128328464-03:00
rendered_js: false
word_count: 571
summary: This document explains how to configure and use Classic Input mode in Warp, along with the functionality and interaction patterns for Agent Mode.
tags:
    - warp-terminal
    - classic-input
    - agent-mode
    - shell-configuration
    - ai-integration
    - terminal-settings
category: guide
optimized: true
optimized_at: 2026-04-29T15:02:11.128328464-03:00
---
# Classic Input

Classic Input corresponds to the **Shell (PS1)** option under **Settings** → **Appearance** → **Input**. It provides a traditional terminal experience with support for PS1 prompts, oh-my-zsh themes, same-line prompts, and shell customizations.

Warp's default uses [[213-agent-platform-warp-agents-interacting-with-agents-terminal-and-agent-modes]], which provide a clean terminal and dedicated conversation view. Classic Input is an alternative for users who prefer a traditional terminal.

[[079-agent-platform-warp-agents-interacting-with-agents]] works in Classic Input with minor differences from the default.

## Features

Classic Input supports all core terminal features:

- **Prompt** — Customizable Warp prompt or shell prompt (PS1/same-line)
- **Input Position** — Choose where input appears
- **Modern Text Editing** — Rich editing like a modern IDE
- **Command Entry** — Command history, synchronized inputs, YAML workflows
- **Text Selection** — Smart or rectangular (column) selection

## How to enter Agent Mode

- Type any natural language in the terminal input — Warp auto-detects and prepares your query
- Keyboard shortcut: `⌘+I` or `*+Space`
- Click the "AI" sparkles icon in the menu bar — opens a new pane starting in Agent Mode
- From a block: click the sparkles icon in the toolbelt, or "Attach block(s) to AI query" in the block context menu

When in Agent Mode, a ✨ sparkles icon displays in line with your terminal input.

## Auto-detection for natural language

The auto-detection feature is completely local — no input is sent to AI unless you press `Enter` in Agent Mode.

### Troubleshooting false detections

If certain shell commands are falsely detected as natural language, add them to the denylist:

**Settings** → **Agents** → **Warp Agent** → **Natural language denylist**

Or disable autodetection entirely:

**Settings** → **Agents** → **Warp Agent** → **Autodetect agent prompts in terminal input**

A banner is shown the first time you enter Agent Mode with the option to disable auto-detection.

## Input hints

Warp occasionally shows hints in the input editor (light grey text) to help users learn features. Enabled by default. Toggle via:

- **Settings** → **Agents** → **Warp Agent** → **Show input hint text**
- Search "Input hint text" in the [[101-terminal-command-palette]]
- Right-click on the input editor

## How to exit Agent Mode

- `Esc` or `Ctrl+C`
- `⌘+I` to toggle out of Agent Mode

## How to run commands in Agent Mode

Press `Enter` to execute your AI query. Agent Mode sends your request to the agent and streams output as an AI block. Unlike a chat panel, Agent Mode completes tasks by running commands directly in your session.

### Command suggestions

If Agent Mode finds a suitable command, it:
- Describes the command in the AI block
- Fills your terminal input with the command so you can press `Enter` to run

When you run a suggested command, it works like a standard terminal command — no data sent back to AI.

### Agent Mode requested commands

If Agent Mode lacks context, it asks permission to run a command and read the output:

1. You must explicitly agree and press `Enter` to run the requested command
2. Both the command input and output are sent to the agent
3. Click **Cancel** or `Ctrl+C` to exit without sending

If a requested command fails, Agent Mode self-corrects and requests another command until the task is complete.

## Model choice

Warp lets you choose from curated LLMs. Default is **Auto (Responsive)**, which routes to the highest-quality, fastest available model. See [[039-agent-platform-warp-agents-capabilities-overview-model-choice]] for the full list.

#tags #classic-input #agent-mode #shell-configuration
