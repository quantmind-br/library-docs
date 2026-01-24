---
title: Playwright MCP
url: https://developers.cloudflare.com/browser-rendering/playwright/playwright-mcp/index.md
source: llms
fetched_at: 2026-01-24T14:04:17.895161274-03:00
rendered_js: false
word_count: 444
summary: This document explains how to deploy and use the Cloudflare Playwright MCP server to enable browser automation for LLM agents using Cloudflare Browser Rendering and Workers.
tags:
    - playwright
    - mcp
    - browser-rendering
    - cloudflare-workers
    - llm-agents
    - web-automation
category: guide
---

---
title: Playwright MCP · Cloudflare Browser Rendering docs
description: Deploy a Playwright MCP server that uses Browser Rendering to
  provide browser automation capabilities to your agents.
lastUpdated: 2026-01-12T09:46:29.000Z
chatbotDeprioritize: false
tags: MCP
source_url:
  html: https://developers.cloudflare.com/browser-rendering/playwright/playwright-mcp/
  md: https://developers.cloudflare.com/browser-rendering/playwright/playwright-mcp/index.md
---

[`@cloudflare/playwright-mcp`](https://github.com/cloudflare/playwright-mcp) is a [Playwright MCP](https://github.com/microsoft/playwright-mcp) server fork that provides browser automation capabilities using Playwright and Browser Rendering.

This server enables LLMs to interact with web pages through structured accessibility snapshots, bypassing the need for screenshots or visually-tuned models. Its key features are:

* Fast and lightweight. Uses Playwright's accessibility tree, not pixel-based input.
* LLM-friendly. No vision models needed, operates purely on structured data.
* Deterministic tool application. Avoids ambiguity common with screenshot-based approaches.

Note

The current version of Cloudflare Playwright MCP **v0.0.5** is in sync with upstream Playwright MCP **v0.0.30**.

## Quick start

If you are already familiar with Cloudflare Workers and you want to get started with Playwright MCP right away, select this button:

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/playwright-mcp/tree/main/cloudflare/example)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers. Use this option if you are familiar with Cloudflare Workers, and wish to skip the step-by-step guidance.

Check our [GitHub page](https://github.com/cloudflare/playwright-mcp) for more information on how to build and deploy Playwright MCP.

## Deploying

Follow these steps to deploy `@cloudflare/playwright-mcp`:

1. Install the Playwright MCP [npm package](https://www.npmjs.com/package/@cloudflare/playwright-mcp).

* npm

  ```sh
  npm i -D @cloudflare/playwright-mcp
  ```

* yarn

  ```sh
  yarn add -D @cloudflare/playwright-mcp
  ```

* pnpm

  ```sh
  pnpm add -D @cloudflare/playwright-mcp
  ```

1. Make sure you have the [browser rendering](https://developers.cloudflare.com/browser-rendering/) and [durable object](https://developers.cloudflare.com/durable-objects/) bindings and [migrations](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/) in your wrangler configuration file.

Note

Your Worker configuration must include the `nodejs_compat` compatibility flag and a `compatibility_date` of 2025-09-15 or later.

* wrangler.jsonc

  ```jsonc
  {
    "$schema": "./node_modules/wrangler/config-schema.json",
    "name": "playwright-mcp-example",
    "main": "src/index.ts",
    "compatibility_date": "2025-09-17",
    "compatibility_flags": [
      "nodejs_compat"
    ],
    "browser": {
      "binding": "BROWSER"
    },
    "migrations": [
      {
        "tag": "v1",
        "new_sqlite_classes": [
          "PlaywrightMCP"
        ]
      }
    ],
    "durable_objects": {
      "bindings": [
        {
          "name": "MCP_OBJECT",
          "class_name": "PlaywrightMCP"
        }
      ]
    }
  }
  ```

* wrangler.toml

  ```toml
  name = "playwright-mcp-example"
  main = "src/index.ts"
  compatibility_date = "2025-09-17"
  compatibility_flags = ["nodejs_compat"]


  [browser]
  binding = "BROWSER"


  [[migrations]]
  tag = "v1"
  new_sqlite_classes = ["PlaywrightMCP"]


  [[durable_objects.bindings]]
  name = "MCP_OBJECT"
  class_name = "PlaywrightMCP"
  ```

1. Edit the code.

```ts
import { env } from 'cloudflare:workers';
import { createMcpAgent } from '@cloudflare/playwright-mcp';


export const PlaywrightMCP = createMcpAgent(env.BROWSER);


export default {
  fetch(request: Request, env: Env, ctx: ExecutionContext) {
    const { pathname } = new URL(request.url);


    switch (pathname) {
      case '/sse':
      case '/sse/message':
        return PlaywrightMCP.serveSSE('/sse').fetch(request, env, ctx);
      case '/mcp':
        return PlaywrightMCP.serve('/mcp').fetch(request, env, ctx);
      default:
        return new Response('Not Found', { status: 404 });
    }
  },
};
```

1. Deploy the server.

```bash
npx wrangler deploy
```

The server is now available at `https://[my-mcp-url].workers.dev/sse` and you can use it with any MCP client.

## Using Playwright MCP

![alt text](https://developers.cloudflare.com/_astro/playground-ai-screenshot.v44jFMBu_2abDuJ.webp)

[Cloudflare AI Playground](https://playground.ai.cloudflare.com/) is a great way to test MCP servers using LLM models available in Workers AI.

* Navigate to <https://playground.ai.cloudflare.com/>
* Ensure that the model is set to `llama-3.3-70b-instruct-fp8-fast`
* In **MCP Servers**, set **URL** to `https://[my-mcp-url].workers.dev/sse`
* Click **Connect**
* Status should update to **Connected** and it should list 23 available tools

You can now start to interact with the model, and it will run necessary the tools to accomplish what was requested.

Note

For best results, give simple instructions consisting of one single action, e.g. "Create a new todo entry", "Go to cloudflare site", "Take a screenshot"

Try this sequence of instructions to see Playwright MCP in action:

1. "Go to demo.playwright.dev/todomvc"
2. "Create some todo entry"
3. "Nice. Now create a todo in parrot style"
4. "And create another todo in Yoda style"
5. "Take a screenshot"

You can also use other MCP clients like [Claude Desktop](https://github.com/cloudflare/playwright-mcp/blob/main/cloudflare/example/README.md#use-with-claude-desktop).

Check our [GitHub page](https://github.com/cloudflare/playwright-mcp) for more examples and MCP client configuration options and our developer documentation on how to [build Agents on Cloudflare](https://developers.cloudflare.com/agents/).