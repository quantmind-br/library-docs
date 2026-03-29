---
title: Code Mode | goose
url: https://block.github.io/goose/docs/guides/managing-tools/code-mode
source: github_pages
fetched_at: 2026-01-22T22:14:07.175579176-03:00
rendered_js: true
word_count: 332
summary: This document explains Code Mode, a method for programmatically interacting with MCP tools to improve context window efficiency and enable batched tool execution.
tags:
    - mcp
    - code-mode
    - tool-calling
    - context-window
    - meta-tools
    - programmatic-execution
category: concept
---

Code Mode is a method of interacting with MCP tools programmatically instead of calling them directly. Code Mode is particularly useful when working with many enabled extensions, as it can help manage context window usage more efficiently.

Code Mode controls how tools are discovered and called:

- Tools from enabled extensions are discovered on-demand and loaded into context as needed
- Multiple tool calls are batched in one execution
- Intermediate results are chained (output from one tool as input to the next)

## How Code Mode Works[​](#how-code-mode-works "Direct link to How Code Mode Works")

The [Code Execution extension](https://block.github.io/goose/docs/mcp/code-execution-mcp) is an MCP server that uses the MCP protocol to expose three foundational meta-tools. When Code Execution is enabled, goose switches to Code Mode. For every request, the LLM writes JavaScript code that goose runs in a sandbox environment to:

- Discover available tools from your enabled extensions (if needed)
- Learn how to work with the tools it needs for the current task
- Call those tools programmatically to complete the task

### Traditional vs. Code Mode Tool Calling[​](#traditional-vs-code-mode-tool-calling "Direct link to Traditional vs. Code Mode Tool Calling")

Traditional MCP tool calling and Code Mode are two different approaches to the same goal: giving goose access to tools.

AspectTraditionalCode Mode**Tool Discovery**All tools from enabled extensions, for example:  
• `developer.shell`  
• `developer.text_editor`  
• `github.list_issues`  
• `github.get_pull_request`  
• `slack.send_message`  
• ... *potentially many more*Code Execution extension's meta-tools:  
• `search_modules`  
• `read_module`  
• `execute_code`

The LLM uses these tools to discover tools from other enabled extensions as needed

**Tool Calling**• Sequential tool calls  
• Each result sent to the LLM before the next call• May require tool discovery calls  
• Multiple tool calls batched in one execution  
• Intermediate results are chained and processed locally**Context Window**Every LLM call includes all tool definitions from enabled extensionsEvery LLM call includes the 3 meta-tool definitions, plus any tool definitions previously discovered in the session**Best For**• 1-3 enabled extensions  
• Simple tasks using 1-2 tools• 5+ extensions  
• Well-defined multi-step workflows

Text-Only Results

Code Mode only supports text content from tool results. Images, binary data, and other content types are ignored.

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")