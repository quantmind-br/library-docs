---
title: Memory Tool (save_memory)
url: https://qwenlm.github.io/qwen-code-docs/en/developers/tools/memory
source: github_pages
fetched_at: 2026-04-09T09:04:57.649841236-03:00
rendered_js: true
word_count: 201
summary: This guide explains the `save_memory` tool for Qwen Code, which allows users to store and recall specific facts across different coding sessions by appending them to a designated context file.
tags:
    - qwen-code
    - memory-saving
    - tool-usage
    - context-management
category: guide
---

Developer Guide

[Tools](https://qwenlm.github.io/qwen-code-docs/en/developers/tools/introduction/ "Tools")

Memory

This document describes the `save_memory` tool for Qwen Code.

## Description[](#description)

Use `save_memory` to save and recall information across your Qwen Code sessions. With `save_memory`, you can direct the CLI to remember key details across sessions, providing personalized and directed assistance.

### Arguments[](#arguments)

`save_memory` takes one argument:

- `fact` (string, required): The specific fact or piece of information to remember. This should be a clear, self-contained statement written in natural language.

## How to use `save_memory` with Qwen Code[](#how-to-use-save_memory-with-qwen-code)

The tool appends the provided `fact` to your context file in the user’s home directory (`~/.qwen/QWEN.md` by default). This filename can be configured via `contextFileName`.

Once added, the facts are stored under a `## Qwen Added Memories` section. This file is loaded as context in subsequent sessions, allowing the CLI to recall the saved information.

Usage:

```
save_memory(fact="Your fact here.")
```

### `save_memory` examples[](#save_memory-examples)

Remember a user preference:

```
save_memory(fact="My preferred programming language is Python.")
```

Store a project-specific detail:

```
save_memory(fact="The project I'm currently working on is called 'qwen-code'.")
```

## Important notes[](#important-notes)

- **General usage:** This tool should be used for concise, important facts. It is not intended for storing large amounts of data or conversational history.
- **Memory file:** The memory file is a plain text Markdown file, so you can view and edit it manually if needed.

Last updated on March 31, 2026

[Web Search](https://qwenlm.github.io/qwen-code-docs/en/developers/tools/web-search/ "Web Search")[MCP Servers](https://qwenlm.github.io/qwen-code-docs/en/developers/tools/mcp-server/ "MCP Servers")