---
title: Container Use Extension | goose
url: https://block.github.io/goose/docs/mcp/container-use-mcp
source: github_pages
fetched_at: 2026-01-22T22:14:55.383756349-03:00
rendered_js: true
word_count: 524
summary: This tutorial explains how to integrate the Container Use MCP Server with the goose AI agent to enable automated tasks and code modifications within isolated Docker environments.
tags:
    - goose-ai
    - mcp-server
    - container-use
    - docker
    - isolated-environments
    - automation
category: tutorial
---

🎥Plug & Play

Watch the demo

* * *

This tutorial covers how to add the [Container Use MCP Server](https://container-use.com) as a goose extension enabling goose to work in an isolated environment.

TLDR

- goose Desktop
- goose CLI

## Configuration[​](#configuration "Direct link to Configuration")

info

You'll need [Docker](https://www.docker.com/) installed on your system. If you want to use the remote MCP server, you'll also need [Node.js](https://nodejs.org/) installed.

- Remote MCP
- Local MCP

<!--THE END-->

- goose Desktop
- goose CLI

<!--THE END-->

1. [Launch the installer](goose://extension?cmd=npx&arg=-y&arg=mcp-remote&arg=https%3A%2F%2Fcontainer-use.com%2Fmcp&id=container-use&name=Container%20Use&description=Run%20container%20automation%20with%20container-use)
2. Click `Yes` to confirm the installation
3. Click the button in the top-left to open the sidebar
4. Navigate to the chat

## Example Usage[​](#example-usage "Direct link to Example Usage")

Here's a simple example of updating a file-based to-do app to use a SQLite database plus full testing - all within an isolated container environment.

#### Prompt[​](#prompt "Direct link to Prompt")

```
Run a container agent to add a feature to save my to-do list data in sqlite, build and run tests, but use a separate Git branch so my main code stays safe.
```

#### goose Output[​](#goose-output "Direct link to goose Output")

```
I'll help you create a container environment to add SQLite functionality to your to-do list application on a separate Git branch. Let me start by creating the environment and examining your current code structure.
─── environment_create | containeruse ──────────────────────────
environment_source: ./examples/todo-list
explanation: ...
title: ...

Now let me set up the environment with the necessary tools and then proceed with the SQLite feature development:
─── environment_config | containeruse ──────────────────────────
config:
    base_image: python:3.11-slim
    setup_commands:
        -
            [REDACTED: 63 chars]
        -
            pip install pytest pytest-cov

environment_id: thankful-whale
environment_source: ./examples/todo-list
explanation: ...

Let me install pytest after the environment is running:

---

Great! I've created a container environment for safely adding SQLite functionality to your to-do list app. Let me first explore the current code structure and then create a new Git branch.

---

Now I'll create the SQLite-based storage implementation. First, let me create a new version of the TaskManager with SQLite support:

---

## ✅ SQLite Feature Successfully Added!

I've successfully created a container environment and added SQLite functionality to your to-do list application! Here's what was accomplished:

### 🎯 **Features Implemented**

1. **SQLite Database Storage**
   - Replaced plain text file storage with SQLite database
   - Created proper database schema with auto-incrementing IDs

2. **Enhanced Task Management**
   - All original functionality preserved (add, list, mark done/undone, delete, clear)
   - Added new **statistics feature** showing completion rates
   - Improved task display with database IDs

3. **Two Implementation Versions**
   - `taskman_sqlite.py` - Full-featured with Rich UI
   - `taskman_sqlite_simple.py` - Simplified without external dependencies

### 🧪 **Testing Completed**

- ✅ Created comprehensive test suite (`test_taskman_sqlite.py`)
- ✅ Built simple test runner (`test_simple.py`)
- ✅ All tests pass successfully
- ✅ Manual testing confirms functionality works perfectly

### 📊 **Live Demo Results**

  # Added tasks successfully
  ✓ Added task: Buy groceries
  ✓ Added task: Walk the dog

  # Listed tasks with SQLite IDs
  📋 Task List (SQLite)
  #   ID   Status   Task
  1   1    ✓ Done   Buy groceries
  2   2    ○ Todo   Walk the dog

  # Statistics working
  Task Statistics:
  Total tasks: 2
  Completed: 1
  Pending: 1
  Completion rate: 50.0%

  # Database verified
  sqlite3 tasks.db "SELECT * FROM tasks;"
  1|Buy groceries|1
  2|Walk the dog|0


### 🔒 **Safe Development**

- ✅ Used separate container environment
- ✅ All changes isolated from your main code
- ✅ Original implementation preserved
- ✅ Backward compatibility maintained

### 📁 **Files Created**

- `taskman_sqlite_simple.py` - Main SQLite implementation
- `test_simple.py` - Test suite
- `SQLITE_FEATURE_README.md` - Comprehensive documentation
- `tasks.db` - SQLite database file

The SQLite implementation is fully functional and ready for use! The original file-based version remains untouched, so you can safely evaluate the new SQLite features without any risk to your existing code.

```