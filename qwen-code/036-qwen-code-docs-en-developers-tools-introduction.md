---
title: Qwen Code tools
url: https://qwenlm.github.io/qwen-code-docs/en/developers/tools/introduction
source: github_pages
fetched_at: 2026-04-09T09:04:40.039520097-03:00
rendered_js: true
word_count: 727
summary: This guide explains that Qwen Code uses built-in tools to enhance its capabilities beyond simple text generation by allowing it to interact with local files, execute shell commands, and fetch web content. It details the process of tool use and emphasizes security confirmations.
tags:
    - qwen-code
    - developer-guide
    - tool-usage
    - local-environment
    - cli-interaction
category: guide
---

Developer Guide

Tools

Introduction

Qwen Code includes built-in tools that the model uses to interact with your local environment, access information, and perform actions. These tools enhance the CLI’s capabilities, enabling it to go beyond text generation and assist with a wide range of tasks.

## Overview of Qwen Code tools[](#overview-of-qwen-code-tools)

In the context of Qwen Code, tools are specific functions or modules that the model can request to be executed. For example, if you ask the model to “Summarize the contents of `my_document.txt`,” it will likely identify the need to read that file and will request the execution of the `read_file` tool.

The core component (`packages/core`) manages these tools, presents their definitions (schemas) to the model, executes them when requested, and returns the results to the model for further processing into a user-facing response.

These tools provide the following capabilities:

- **Access local information:** Tools allow the model to access your local file system, read file contents, list directories, etc.
- **Execute commands:** With tools like `run_shell_command`, the model can run shell commands (with appropriate safety measures and user confirmation).
- **Interact with the web:** Tools can fetch content from URLs.
- **Take actions:** Tools can modify files, write new files, or perform other actions on your system (again, typically with safeguards).
- **Ground responses:** By using tools to fetch real-time or specific local data, responses can be more accurate, relevant, and grounded in your actual context.

## How to use Qwen Code tools[](#how-to-use-qwen-code-tools)

To use Qwen Code tools, provide a prompt to the CLI. The process works as follows:

1. You provide a prompt to the CLI.
2. The CLI sends the prompt to the core.
3. The core, along with your prompt and conversation history, sends a list of available tools and their descriptions/schemas to the configured model API.
4. The model analyzes your request. If it determines that a tool is needed, its response will include a request to execute a specific tool with certain parameters.
5. The core receives this tool request, validates it, and (often after user confirmation for sensitive operations) executes the tool.
6. The output from the tool is sent back to the model.
7. The model uses the tool’s output to formulate its final answer, which is then sent back through the core to the CLI and displayed to you.

You will typically see messages in the CLI indicating when a tool is being called and whether it succeeded or failed.

## Security and confirmation[](#security-and-confirmation)

Many tools, especially those that can modify your file system or execute commands (`write_file`, `edit`, `run_shell_command`), are designed with safety in mind. Qwen Code will typically:

- **Require confirmation:** Prompt you before executing potentially sensitive operations, showing you what action is about to be taken.
- **Utilize sandboxing:** All tools are subject to restrictions enforced by sandboxing (see [Sandboxing in Qwen Code](https://qwenlm.github.io/qwen-code-docs/en/developers/sandbox/)). This means that when operating in a sandbox, any tools (including MCP servers) you wish to use must be available *inside* the sandbox environment. For example, to run an MCP server through `npx`, the `npx` executable must be installed within the sandbox’s Docker image or be available in the `sandbox-exec` environment.

It’s important to always review confirmation prompts carefully before allowing a tool to proceed.

## Learn more about Qwen Code’s tools[](#learn-more-about-qwen-codes-tools)

Qwen Code’s built-in tools can be broadly categorized as follows:

- **[File System Tools](https://qwenlm.github.io/qwen-code-docs/en/developers/tools/file-system/):** For interacting with files and directories (reading, writing, listing, searching, etc.).
- **[Shell Tool](https://qwenlm.github.io/qwen-code-docs/en/developers/tools/shell/) (`run_shell_command`):** For executing shell commands.
- **[Web Fetch Tool](https://qwenlm.github.io/qwen-code-docs/en/developers/tools/web-fetch/) (`web_fetch`):** For retrieving content from URLs.
- **[Web Search Tool](https://qwenlm.github.io/qwen-code-docs/en/developers/tools/web-search/) (`web_search`):** For searching the web.
- **[Multi-File Read Tool](https://qwenlm.github.io/qwen-code-docs/en/developers/tools/multi-file/) (`read_many_files`):** A specialized tool for reading content from multiple files or directories, often used by the `@` command.
- **[Memory Tool](https://qwenlm.github.io/qwen-code-docs/en/developers/tools/memory/) (`save_memory`):** For saving and recalling information across sessions.
- **[Todo Write Tool](https://qwenlm.github.io/qwen-code-docs/en/developers/tools/todo-write/) (`todo_write`):** For creating and managing structured task lists during coding sessions.
- **[Task Tool](https://qwenlm.github.io/qwen-code-docs/en/developers/tools/task/) (`task`):** For delegating complex tasks to specialized subagents.
- **[Exit Plan Mode Tool](https://qwenlm.github.io/qwen-code-docs/en/developers/tools/exit-plan-mode/) (`exit_plan_mode`):** For exiting plan mode and proceeding with implementation.

Additionally, these tools incorporate:

- [**MCP servers**](https://qwenlm.github.io/qwen-code-docs/en/developers/tools/mcp-server/): MCP servers act as a bridge between the model and your local environment or other services like APIs.
  
  - [**MCP Quick Start Guide**](https://qwenlm.github.io/qwen-code-docs/en/developers/mcp-quick-start/): Get started with MCP in 5 minutes with practical examples
  - [**MCP Example Configurations**](https://qwenlm.github.io/qwen-code-docs/en/developers/mcp-example-configs/): Ready-to-use configurations for common scenarios
  - [**MCP Testing & Validation**](https://qwenlm.github.io/qwen-code-docs/en/developers/mcp-testing-validation/): Test and validate your MCP server setups
- [**Sandboxing**](https://qwenlm.github.io/qwen-code-docs/en/developers/sandbox/): Sandboxing isolates the model and its changes from your environment to reduce potential risk.

Last updated on March 31, 2026

[Java SDK(alpha)](https://qwenlm.github.io/qwen-code-docs/en/developers/sdk-java/ "Java SDK(alpha)")[File System](https://qwenlm.github.io/qwen-code-docs/en/developers/tools/file-system/ "File System")