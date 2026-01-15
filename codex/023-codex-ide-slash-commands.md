---
title: Codex IDE extension slash commands
url: https://developers.openai.com/codex/ide/slash-commands.md
source: llms
fetched_at: 2026-01-13T18:59:52.295550626-03:00
rendered_js: false
word_count: 181
summary: This document lists and describes the available slash commands for the Codex IDE extension, which enable users to control settings, toggle modes, and access support features directly from the chat interface.
tags:
    - codex-ide
    - slash-commands
    - chat-interface
    - code-review
    - cloud-mode
    - local-mode
category: reference
---

# Codex IDE extension slash commands

Slash commands let you control Codex without leaving the chat input. Use them to check status, switch between local and cloud mode, or send feedback.

## Use a slash command

1. In the Codex chat input, type `/`.
2. Select a command from the list, or keep typing to filter (for example, `/status`).
3. Press **Enter**.

## Available slash commands

| Slash command        | Description                                                                            |
| -------------------- | -------------------------------------------------------------------------------------- |
| `/auto-context`      | Turn Auto Context on or off to include recent files and IDE context automatically.     |
| `/cloud`             | Switch to cloud mode to run the task remotely (requires cloud access).                 |
| `/cloud-environment` | Choose the cloud environment to use (available only in cloud mode).                    |
| `/feedback`          | Open the feedback dialog to submit feedback and optionally include logs.               |
| `/local`             | Switch to local mode to run the task in your workspace.                                |
| `/review`            | Start code review mode to review uncommitted changes or compare against a base branch. |
| `/status`            | Show the thread ID, context usage, and rate limits.                                    |