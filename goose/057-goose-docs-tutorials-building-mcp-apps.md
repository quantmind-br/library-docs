---
title: Building MCP Apps | goose
url: https://block.github.io/goose/docs/tutorials/building-mcp-apps
source: github_pages
fetched_at: 2026-01-22T22:16:09.925984401-03:00
rendered_js: true
word_count: 339
summary: This tutorial explains how to build and integrate interactive MCP Apps into the goose chat interface using Node.js and the Model Context Protocol.
tags:
    - mcp-apps
    - model-context-protocol
    - goose-desktop
    - node-js
    - javascript
    - extension-development
    - interactive-ui
category: tutorial
---

MCP Apps let MCP servers return interactive UIs that render directly inside the goose chat interface, rather than responding with text alone. This allows users to express intent through interaction, which is useful for workflows that require input, iteration, or visual feedback.

Experimental

MCP Apps support in goose is experimental and based on a draft specification. The implementation is minimal and may change, and does not yet support advanced capabilities or persistent app windows.

In this tutorial, you will build an MCP App using JavaScript and Node.js. The app includes an interactive counter, stays in sync with the host theme, and sends messages back to the chat, showing how user intent flows from UI to agent.

Prerequisites

- Node.js 18+ installed
- goose Desktop 1.19.1+ installed

* * *

## Step 1: Initialize Your Project[​](#step-1-initialize-your-project "Direct link to Step 1: Initialize Your Project")

Create a new directory and initialize a Node.js project:

```
mkdir mcp-app-demo
cd mcp-app-demo
npm init -y
```

Install the MCP SDK:

```
npm install @modelcontextprotocol/sdk
```

Update your `package.json` to use ES modules by adding `"type": "module"`:

```
{
  "name": "mcp-app-demo",
  "version": "1.0.0",
  "type": "module",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "@modelcontextprotocol/sdk": "^1.0.0"
  }
}
```

* * *

## Step 2: Create the MCP Server[​](#step-2-create-the-mcp-server "Direct link to Step 2: Create the MCP Server")

Create `server.js` - this is the MCP server that loads and serves your HTML:

server.js

* * *

## Step 3: Create the App HTML[​](#step-3-create-the-app-html "Direct link to Step 3: Create the App HTML")

Create `index.html` - this is your interactive UI:

index.html

* * *

## Step 4: Add to goose Desktop[​](#step-4-add-to-goose-desktop "Direct link to Step 4: Add to goose Desktop")

1. Click the button in the top-left to open the sidebar
2. Click `Extensions`
3. Click `Add custom extension`
4. Fill in the details:
   
   - **Type**: `Standard IO`
   - **ID**: `mcp-app-demo`
   - **Name**: `MCP App Demo`
   - **Command**: `node /full/path/to/mcp-app-demo/server.js`
5. Click `Add`

For more options, see [Adding Extensions](https://block.github.io/goose/docs/getting-started/using-extensions#adding-extensions).

* * *

## Step 5: Test Your App[​](#step-5-test-your-app "Direct link to Step 5: Test Your App")

1. Restart goose to load the new extension
2. Prompt goose: "Show me the demo app"
3. goose will call the `show_demo_app` tool
4. Your interactive app will render in the chat!

Try:

- Clicking the counter buttons
- Typing a message and clicking "Send"
- Switching goose between light/dark mode

* * *

## How It Works[​](#how-it-works "Direct link to How It Works")

```
┌──────────────────────────────────────┐
│           Your MCP App               │  HTML/JS in sandboxed iframe
└──────────────────┬───────────────────┘
                   │ postMessage
┌──────────────────▼───────────────────┐
│          goose Desktop               │  Renders UI, routes messages
└──────────────────┬───────────────────┘
                   │ MCP Protocol
┌──────────────────▼───────────────────┐
│          Your MCP Server             │  Serves HTML via resources
└──────────────────────────────────────┘
```

Your server returns a `ui://` resource URI, goose fetches the HTML and renders it in an iframe. The app communicates back via `postMessage`—requesting theme info, sending messages to chat, or resizing itself.

MCP Apps run sandboxed with CSP restrictions. See the [MCP Apps Specification](https://github.com/modelcontextprotocol/ext-apps) for details on security and the full protocol.