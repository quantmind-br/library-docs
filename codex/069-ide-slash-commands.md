---
title: Codex IDE extension slash commands
url: https://developers.openai.com/codex/ide/slash-commands.md
source: llms
fetched_at: 2026-04-30T10:15:44.58868572-03:00
rendered_js: false
word_count: 118
summary: This document provides an overview of the slash commands available in the Codex IDE extension to manage chat sessions, environment modes, and feedback.
tags:
    - codex-ide
    - slash-commands
    - developer-tools
    - ide-extensions
    - workflow-automation
category: reference
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Codex IDE extension slash commands

Control Codex from the chat input without leaving the editor.

**Usage:** Type `/` in the Codex chat input, select or filter commands (e.g., `/status`), press **Enter**.

| Command | Description |
|---------|-------------|
| `/auto-context` | Toggle Auto Context (recent files + IDE context) |
| `/cloud` | Switch to cloud mode (requires cloud access) |
| `/cloud-environment` | Choose cloud environment (cloud mode only) |
| `/feedback` | Open feedback dialog, optionally include logs |
| `/local` | Switch to local mode (workspace execution) |
| `/review` | Review uncommitted changes or compare against base branch |
| `/status` | Show thread ID, context usage, and rate limits |

#slash-commands #ide #codex