---
title: Terminal Integration | goose
url: https://block.github.io/goose/docs/guides/terminal-integration
source: github_pages
fetched_at: 2026-01-22T22:14:30.594747588-03:00
rendered_js: true
word_count: 305
summary: This document provides instructions for integrating the goose assistant into terminal environments, including setup for various shells, usage commands, and session management.
tags:
    - terminal-integration
    - cli-tools
    - shell-configuration
    - goose-ai
    - session-management
    - command-line-interface
category: guide
---

Talk to goose directly from your shell prompt. Instead of switching to a separate REPL session, stay in your terminal and call goose when you need it.

## Setup[​](#setup "Direct link to Setup")

- zsh
- bash
- fish
- PowerShell

Add to `~/.zshrc`:

```
eval "$(goose term init zsh)"
```

Restart your terminal or source the config, and that's it!

## Usage[​](#usage "Direct link to Usage")

Just type `@goose` (or `@g` for short) followed by your question:

```
npm install express
    npm ERR! code EACCES
    npm ERR! permission denied

@goose "how do I fix this error?"
```

goose automatically sees the commands you've run since your last question, so you don't need to explain what you've been doing. Use quotes around your prompt if it contains special characters like `?`, `*`, or `'`:

```
@goose "what's in this directory?"
@g "analyze the error: 'permission denied'"
```

## Named Sessions[​](#named-sessions "Direct link to Named Sessions")

By default, each terminal gets its own goose session that lasts until you close it. Named sessions let you continue conversations across terminal restarts and share context between windows.

- zsh
- bash
- fish
- PowerShell

```
eval "$(goose term init zsh --name my-project)"
```

Named sessions persist in goose's database, so they're available anytime, even after restarting your computer. Reopen later and run the same command to continue:

```
# Start debugging
eval "$(goose term init zsh --name auth-bug)"
@goose help me debug this login timeout

# Close terminal, come back later
eval "$(goose term init zsh --name auth-bug)"
@goose "what was the solution we discussed?"
# Continues the same conversation with context
```

## Show Context Status in Your Prompt[​](#show-context-status-in-your-prompt "Direct link to Show Context Status in Your Prompt")

Add `goose term info` to your prompt to see how much context you've used and which model is active during a terminal goose session.

- zsh
- bash
- fish
- PowerShell

```
PROMPT='$(goose term info) %~ $ '
```

Your terminal prompt now shows the context usage and model name (shortened for readability) for the active goose session. For example:

```
●●○○○ sonnet ~/projects $
```

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

**goose doesn't see recent commands:** If you run commands but goose says it doesn't see any recent activity, check if terminal integration is properly [set up in your shell config](#setup). You can also check the id of the goose session in your current terminal:

```
# Check if session ID exists
echo $GOOSE_SESSION_ID
# Should show something like: 20251209_151730
```

To share context across terminal windows, use a [named session](#named-sessions) instead.

**Session getting too full** (prompt shows `●●●●●`): If goose's responses are getting slow or hitting context limits, start a fresh goose session in the terminal. The new goose session sees your command history, but not the conversation history from the previous session.

```
# Start a new goose session in the same shell
eval "$(goose term init zsh)"
```