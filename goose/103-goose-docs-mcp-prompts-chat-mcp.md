---
title: prompts.chat Extension | goose
url: https://block.github.io/goose/docs/mcp/prompts-chat-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:41.202010893-03:00
rendered_js: true
word_count: 162
summary: This tutorial explains how to integrate the prompts.chat MCP Server as an extension in goose to search and utilize a library of AI prompts.
tags:
    - goose-extension
    - prompts-chat
    - mcp-server
    - ai-prompts
    - installation-guide
category: tutorial
---

This tutorial covers how to add the [prompts.chat MCP Server](https://prompts.chat) as a goose extension to enable access to thousands of AI prompts directly in your AI assistant.

TLDR

- goose Desktop
- goose CLI

**Environment Variable (Optional)**

```
PROMPTS_API_KEY: <YOUR_API_KEY>
```

## Configuration[​](#configuration "Direct link to Configuration")

info

Note that you'll need [Node.js](https://nodejs.org/) installed on your system to run this command, as it uses `npx`.

- goose Desktop
- goose CLI

<!--THE END-->

1. [Launch the installer](goose://extension?cmd=npx&arg=-y&arg=%40fkadev%2Fprompts.chat-mcp%40latest&id=prompts-chat-mcp&name=prompts.chat&description=Access%20thousands%20of%20AI%20prompts%20directly%20in%20your%20AI%20assistant&env=PROMPTS_API_KEY%3DAPI%20Key%20to%20save%20and%20list%20private%20prompts%20on%20prompts.chat%20%28optional%29)
2. Click `Yes` to confirm the installation
3. Get your [prompts.chat API Key](https://prompts.chat) and paste it in
4. Click `Add Extension`
5. Click the button in the top-left to open the sidebar
6. Navigate to the chat

## Example Usage[​](#example-usage "Direct link to Example Usage")

The prompts.chat extension provides access to a curated library of AI prompts that you can search and use directly within goose. This is useful when you need inspiration or want to leverage proven prompt patterns for specific tasks.

- goose Desktop
- goose CLI

<!--THE END-->

1. Open a new session in goose Desktop

### Searching for Prompts[​](#searching-for-prompts "Direct link to Searching for Prompts")

#### goose Prompt[​](#goose-prompt "Direct link to goose Prompt")

```
Search for prompts about code review
```

#### goose Output[​](#goose-output "Direct link to goose Output")

```
I found several prompts related to code review:

1. **Code Review Assistant** - A comprehensive prompt for reviewing code quality, 
   security, and best practices
2. **Pull Request Reviewer** - Helps analyze pull requests and suggest improvements
3. **Security Code Audit** - Focuses on identifying security vulnerabilities

Would you like me to retrieve any of these prompts?
```

### Using a Prompt[​](#using-a-prompt "Direct link to Using a Prompt")

#### goose Prompt[​](#goose-prompt-1 "Direct link to goose Prompt")

```
Get the Code Review Assistant prompt and use it to review my current file
```

#### goose Output[​](#goose-output-1 "Direct link to goose Output")

```
I've retrieved the Code Review Assistant prompt. Let me apply it to analyze your code...

[Applying prompt guidelines to review your code]

Here's my review based on the prompt's framework:

✅ Code structure and organization
✅ Naming conventions
⚠️ Consider adding error handling for edge cases
⚠️ Documentation could be improved for public methods

Would you like me to help address any of these findings?
```