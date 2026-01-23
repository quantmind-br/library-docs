---
title: Asana Extension | goose
url: https://block.github.io/goose/docs/mcp/asana-mcp
source: github_pages
fetched_at: 2026-01-22T22:14:41.020665402-03:00
rendered_js: true
word_count: 219
summary: This tutorial provides step-by-step instructions for installing and configuring the Asana MCP server as a goose extension to enable AI-driven task automation and project tracking.
tags:
    - goose-extension
    - asana-integration
    - mcp-server
    - task-automation
    - project-management
category: tutorial
---

This tutorial covers how to add the [Asana MCP Server](https://github.com/roychri/mcp-server-asana) as a goose extension to enable task automation, project tracking, and team collaboration.

TLDR

- goose Desktop
- goose CLI

**Environment Variable**

```
ASANA_ACCESS_TOKEN: <YOUR_TOKEN>
```

## Configuration[​](#configuration "Direct link to Configuration")

info

Note that you'll need [Node.js](https://nodejs.org/) installed on your system to run this command, as it uses `npx`.

- goose Desktop
- goose CLI

<!--THE END-->

1. [Launch the installer](goose://extension?cmd=npx&arg=-y&arg=%40roychri%2Fmcp-server-asana&id=asana&name=Asana&description=Enable%20task%20automation%2C%20project%20tracking%2C%20and%20team%20collaboration&env=ASANA_ACCESS_TOKEN%3DAsana%20Access%20Token)
2. Click `Yes` to confirm the installation
3. Get your [Asana Access Token](https://app.asana.com/0/my-apps) and paste it in
4. Click `Add Extension`
5. Click the button in the top-left to open the sidebar
6. Navigate to the chat

## Example Usage[​](#example-usage "Direct link to Example Usage")

LLM

OpenAI's GPT-4o was used for this task. There's an [open bug](https://github.com/block/goose/issues/1804) for Amazon Bedrock models.

### goose Prompt[​](#goose-prompt "Direct link to goose Prompt")

> *goose, I have one hour. Look through uncompleted tasks assigned to me in Asana and show me ones that you estimate will take an hour or less. Order them by deadline.*

### goose Output[​](#goose-output "Direct link to goose Output")

Note that IDs have been changed to generic ones

CLI

Tool Calls

Here are your uncompleted tasks in Asana estimated to take an hour or less, ordered by their deadline:

1. **Task:** Review team meeting notes
   
   - **Due Date:** 2025-03-21
2. **Task:** Draft quick status update
   
   - **Due Date:** 2025-03-21
3. **Task:** Proofread blog post
   
   - **Due Date:** 2025-03-21
4. **Task:** Send reminder to partners
   
   - **Due Date:** 2025-03-27

Please let me know if you'd like more information or help with any specific task!