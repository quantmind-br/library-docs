---
title: Sugar Extension | goose
url: https://block.github.io/goose/docs/mcp/sugar-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:52.470232881-03:00
rendered_js: true
word_count: 289
summary: This document explains how to integrate and use the Sugar MCP Server with the goose extension to delegate development tasks to an autonomous AI system.
tags:
    - goose-extension
    - sugar-mcp
    - autonomous-development
    - ai-task-delegation
    - mcp-server-configuration
    - sugar-cli
category: tutorial
---

This tutorial covers how to add the [Sugar MCP Server](https://github.com/cdnsteve/sugar) as a goose extension to delegate development tasks to an autonomous AI system that runs in the background.

TLDR

- goose Desktop
- goose CLI

## Configuration[​](#configuration "Direct link to Configuration")

info

Note that you'll need [Node.js](https://nodejs.org/) installed on your system to run this command, as it uses `npx`.

info

Sugar requires Python 3.11+ and the Sugar CLI installed in your project. Install with `pip install sugarai` and initialize with `sugar init`.

- goose Desktop
- goose CLI

<!--THE END-->

1. [Launch the installer](goose://extension?cmd=npx&arg=-y&arg=sugarai-mcp&id=sugar&name=Sugar&description=Autonomous%20AI%20development%20system%20-%20delegate%20tasks%20and%20run%2024%2F7&env=SUGAR_PROJECT_ROOT%3DProject%20directory%20%28optional%2C%20defaults%20to%20current%29)
2. Click `Yes` to confirm the installation
3. Set SUGAR\_PROJECT\_ROOT to your project directory (/path/to/your/project), or Sugar will use the current working directory
4. Click `Add Extension`
5. Click the button in the top-left to open the sidebar
6. Navigate to the chat

## Example Usage[​](#example-usage "Direct link to Example Usage")

Sugar lets you delegate development tasks to an autonomous AI that works in the background. Tasks are queued and executed independently, so you can continue working while Sugar handles them.

- goose Desktop
- goose CLI

<!--THE END-->

1. Open a new session in goose Desktop

### goose Prompt[​](#goose-prompt "Direct link to goose Prompt")

> Create a task to add input validation to the user registration form. Priority 4.

### goose Output[​](#goose-output "Direct link to goose Output")

Desktop

I'll create a Sugar task for adding input validation to the user registration form.

-------- createTask -------

Task created successfully:

- **ID**: a1b2c3d4-5678-90ab-cdef-ghijklmnopqr
- **Title**: Add input validation to the user registration form
- **Type**: feature
- **Priority**: P4 (High)
- **Status**: pending

The task has been queued. Sugar will pick it up and work on it autonomously. You can check the status anytime with `getStatus` or `listTasks`.

### Available Tools[​](#available-tools "Direct link to Available Tools")

Sugar exposes the following tools through MCP:

ToolDescription`createTask`Create a new development task`listTasks`List tasks with optional filtering`viewTask`View detailed task information`updateTask`Update task properties`removeTask`Remove a task from the queue`getStatus`Get system status and metrics`runOnce`Execute one autonomous development cycle`initSugar`Initialize Sugar in a project