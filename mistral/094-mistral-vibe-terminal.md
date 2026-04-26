---
title: CLI Introduction | Mistral Docs
url: https://docs.mistral.ai/mistral-vibe/terminal
source: sitemap
fetched_at: 2026-04-26T04:08:26.334854096-03:00
rendered_js: false
word_count: 259
summary: Mistral Vibe is a CLI-based coding assistant that provides a conversational interface for codebase interaction, project management, and automated development tasks.
tags:
    - coding-assistant
    - cli-tool
    - ai-development
    - codebase-management
    - terminal-productivity
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

**Mistral Vibe** is a command-line coding assistant powered by Mistral's models, providing a conversational interface to explore, modify, and interact with your codebase using natural language.

![vibe_logo](https://docs.mistral.ai/img/vibe-logo.svg)

GitHub: [mistralai/mistral-vibe](https://github.com/mistralai/mistral-vibe) (Apache 2.0)

## Features

- **Interactive Chat**: Conversational AI agent that breaks down complex tasks
- **Built-in Toolset**:
  - File manipulation: `read_file`, `write_file`, `search_replace`
  - Shell commands in stateful terminal (`bash`)
  - Code search with ripgrep (`grep`)
  - Todo list for tracking agent work
- **Project-Aware Context**: Scans file structure and Git status automatically
- **Advanced CLI**:
  - Autocompletion for slash commands (`/`) and file paths (`@`)
  - Persistent command history
  - Themes
- **Configurable**: Customize models, providers, tool permissions, UI via `config.toml`
- **Agents & Skills**: Create multiple agents with different skills and permissions
- **Safety**: Tool execution approval required

## Quick Links

- [[094-mistral-vibe-terminal|Installation]]
- [[094-mistral-vibe-terminal|Quickstart]]
- [[133-mistral-vibe-terminal-configuration|Configuration]]
- [[129-mistral-vibe-agents-skills|Agents & Skills]]
- [[093-mistral-vibe-local|Offline / Local]] #coding-assistant #cli-tool #ai-development