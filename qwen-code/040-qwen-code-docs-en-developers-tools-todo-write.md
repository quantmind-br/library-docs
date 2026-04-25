---
title: Todo Write Tool (todo_write)
url: https://qwenlm.github.io/qwen-code-docs/en/developers/tools/todo-write
source: github_pages
fetched_at: 2026-04-09T09:04:47.714518013-03:00
rendered_js: true
word_count: 281
summary: This document serves as a developer guide detailing the `todo_write` tool, which helps manage and track structured task lists for complex coding sessions within Qwen Code.
tags:
    - developer-guide
    - tool-usage
    - task-management
    - coding-session
    - qwen-code
category: guide
---

Developer Guide

[Tools](https://qwenlm.github.io/qwen-code-docs/en/developers/tools/introduction/ "Tools")

Todo Write

This document describes the `todo_write` tool for Qwen Code.

## Description[](#description)

Use `todo_write` to create and manage a structured task list for your current coding session. This tool helps the AI assistant track progress and organize complex tasks, providing you with visibility into what work is being performed.

### Arguments[](#arguments)

`todo_write` takes one argument:

- `todos` (array, required): An array of todo items, where each item contains:
  
  - `content` (string, required): The description of the task.
  - `status` (string, required): The current status (`pending`, `in_progress`, or `completed`).
  - `activeForm` (string, required): The present continuous form describing what is being done (e.g., “Running tests”, “Building the project”).

## How to use `todo_write` with Qwen Code[](#how-to-use-todo_write-with-qwen-code)

The AI assistant will automatically use this tool when working on complex, multi-step tasks. You don’t need to explicitly request it, but you can ask the assistant to create a todo list if you want to see the planned approach for your request.

The tool stores todo lists in your home directory (`~/.qwen/todos/`) with session-specific files, so each coding session maintains its own task list.

## When the AI uses this tool[](#when-the-ai-uses-this-tool)

The assistant uses `todo_write` for:

- Complex tasks requiring multiple steps
- Feature implementations with several components
- Refactoring operations across multiple files
- Any work involving 3 or more distinct actions

The assistant will not use this tool for simple, single-step tasks or purely informational requests.

### `todo_write` examples[](#todo_write-examples)

Creating a feature implementation plan:

```
todo_write(todos=[
  {
    "content": "Create user preferences model",
    "status": "pending",
    "activeForm": "Creating user preferences model"
  },
  {
    "content": "Add API endpoints for preferences",
    "status": "pending",
    "activeForm": "Adding API endpoints for preferences"
  },
  {
    "content": "Implement frontend components",
    "status": "pending",
    "activeForm": "Implementing frontend components"
  }
])
```

## Important notes[](#important-notes)

- **Automatic usage:** The AI assistant manages todo lists automatically during complex tasks.
- **Progress visibility:** You’ll see todo lists updated in real-time as work progresses.
- **Session isolation:** Each coding session has its own todo list that doesn’t interfere with others.

Last updated on March 31, 2026

[Shell](https://qwenlm.github.io/qwen-code-docs/en/developers/tools/shell/ "Shell")[Task](https://qwenlm.github.io/qwen-code-docs/en/developers/tools/task/ "Task")