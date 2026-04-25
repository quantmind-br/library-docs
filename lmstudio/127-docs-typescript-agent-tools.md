---
title: Tool Definition
url: https://lmstudio.ai/docs/typescript/agent/tools
source: sitemap
fetched_at: 2026-04-07T21:31:58.968305498-03:00
rendered_js: false
word_count: 120
summary: This document explains how to define and pass tools to a model, detailing that these tools can execute external effects like file creation or API calls.
tags:
    - tool-definition
    - llm-agents
    - function-calling
    - api-tools
    - system-prompting
category: guide
---

You can define tools with the `tool()` function and pass them to the model in the `act()` call.

Follow this standard format to define functions as tools:

**Important**: The tool name, description, and the parameter definitions are all passed to the model!

This means that your wording will affect the quality of the generation. Make sure to always provide a clear description of the tool so the model knows how to use it.

Tools can also have external effects, such as creating files or calling programs and even APIs. By implementing tools with external effects, you can essentially turn your LLMs into autonomous agents that can perform tasks on your local machine.

### Tool Definition[](#tool-definition)

### Example code using the `createFile` tool:[](#example-code-using-the-createfile-tool)