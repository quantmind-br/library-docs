---
title: goose for VS Code Extension | goose
url: https://block.github.io/goose/docs/experimental/vs-code-extension
source: github_pages
fetched_at: 2026-01-22T22:13:19.746325226-03:00
rendered_js: true
word_count: 273
summary: This guide explains how to install and use the goose extension for VS Code, covering setup requirements, code context sharing, and core features of the AI-powered chat interface.
tags:
    - vscode-extension
    - goose-ai
    - installation-guide
    - developer-tools
    - ai-assistant
    - context-sharing
category: guide
---

The [goose for VS Code extension](https://marketplace.visualstudio.com/items?itemName=block.vscode-goose) lets you interact with goose directly within VS Code.

Experimental Feature

goose for VS Code is in active development. Behavior and configuration may change in future releases.

The extension uses the [Agent Client Protocol (ACP)](https://block.github.io/goose/docs/guides/acp-clients) to communicate with goose.

## Install the Extension[​](#install-the-extension "Direct link to Install the Extension")

Prerequisites

- [VS Code](https://code.visualstudio.com/) version 1.95.0 or higher
- [goose CLI](https://block.github.io/goose/docs/getting-started/installation) version 1.16.0 or higher

<!--THE END-->

1. Go to [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=block.vscode-goose)
2. Click `Install`
3. On the popup window, click `Open Visual Studio Code`
4. In Visual Studio Code, click `Install`
5. Click the icon in the Activity Bar to open the side panel and start chatting with goose

There are two ways to provide context to goose.

### Send Selected Code[​](#send-selected-code "Direct link to Send Selected Code")

1. Select the code you want to discuss in your editor
2. Send the selection to goose:
   
   - macOS: `Cmd+Shift+G`
   - Windows/Linux: `Ctrl+Shift+G`
   - Right-click and choose `Send to goose`

The selected code will appear as a context chip above the chat input.

### Attach Files with @ Mentions[​](#attach-files-with--mentions "Direct link to Attach Files with @ Mentions")

1. Type `@` in the chat input and start typing the file name
2. Select the file:
   
   - Use the arrow keys (↑/↓) to select the file and press `Enter`
   - Use your mouse to select the file

The attached file will appear as a context chip above the chat input.

## Example Usage[​](#example-usage "Direct link to Example Usage")

The goose for VS Code extension connects directly to your editor, letting you manage files, projects, and workflows with AI. It includes the following features:

- Interactive chat UI with streaming responses
- Access to goose's AI capabilities and enabled extensions
- Session management with history replay
- Context sharing and visual context chips in the chat UI
- Clipboard tools to copy code snippets/responses for easy sharing

### goose Prompt[​](#goose-prompt "Direct link to goose Prompt")

```
Update the contributing guide at /goose/CONTRIBUTING.md with instructions on how to start docusaurus dev server
```

### goose Output[​](#goose-output "Direct link to goose Output")

```

I'll help you update the CONTRIBUTING.md file with instructions for starting the Docusaurus dev server. First, let me check the current content of the file.

─── developer__text_editor | view ──────────────────────────

I'll now update the CONTRIBUTING.md file to include instructions for starting the Docusaurus dev server. I'll add this information in a new section under the Node section.

─── developer__text_editor | str_replace ──────────────────────────

I've successfully updated the CONTRIBUTING.md file to include instructions for starting the Docusaurus dev server. I added a new "Documentation" section right after the Node section, which provides clear step-by-step instructions for:

Navigating to the docs directory
Installing dependencies
Starting the development server
I also included helpful information about the hot-reloading feature and the local server URL. The formatting is consistent with the rest of the document, using proper markdown syntax for code blocks and headers.

Is there anything else you'd like me to add or modify in the contributing guide?

```