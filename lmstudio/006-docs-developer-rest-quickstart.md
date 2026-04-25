---
title: Get up and running with the LM Studio API
url: https://lmstudio.ai/docs/developer/rest/quickstart
source: sitemap
fetched_at: 2026-04-07T21:30:12.583994759-03:00
rendered_js: false
word_count: 322
summary: This document provides instructions on setting up the local server, managing API authentication, using the chat endpoint to interact with models, integrating MCP servers via API, and downloading necessary models.
tags:
    - server-setup
    - api-authentication
    - chat-endpoint
    - mcp-servers
    - model-downloading
category: guide
---

## Start the server[](#start-the-server "Link to 'Start the server'")

[Install](https://lmstudio.ai/download) and launch LM Studio.

Then ensure the server is running through the toggle at the top left of the Developer page, or through [lms](https://lmstudio.ai/docs/cli) in the terminal:


By default, the server is available at `http://localhost:1234`.

If you don't have a model downloaded yet, you can download the model:

```

lms get ibm/granite-4-micro
```

## API Authentication[](#api-authentication "Link to 'API Authentication'")

By default, the LM Studio API server does **not** require authentication. You can configure the server to require authentication by API token in the [server settings](https://lmstudio.ai/docs/developer/core/server/settings) for added security.

To authenticate API requests, generate an API token from the Developer page in LM Studio, and include it in the `Authorization` header of your requests as follows: `Authorization: Bearer $LM_API_TOKEN`. Read more about authentication [here](https://lmstudio.ai/docs/developer/core/authentication).

## Chat with a model[](#chat-with-a-model "Link to 'Chat with a model'")

Use the chat endpoint to send a message to a model. By default, the model will be automatically loaded if it is not already.

The `/api/v1/chat` endpoint is stateful, which means you do not need to pass the full history in every request. Read more about it [here](https://lmstudio.ai/docs/developer/rest/stateful-chats).

See the full [chat](https://lmstudio.ai/docs/developer/rest/chat) docs for more details.

## Use MCP servers via API[](#use-mcp-servers-via-api "Link to 'Use MCP servers via API'")

Enable the model interact with ephemeral Model Context Protocol (MCP) servers in `/api/v1/chat` by specifying servers in the `integrations` field.

You can also use locally configured MCP plugins (from your `mcp.json`) via the `integrations` field. Using locally run MCP plugins requires authentication via an API token passed through the `Authorization` header. Read more about authentication [here](https://lmstudio.ai/docs/developer/core/authentication).

See the full [chat](https://lmstudio.ai/docs/developer/rest/chat) docs for more details.

## Download a model[](#download-a-model "Link to 'Download a model'")

Use the download endpoint to download models by identifier from the [LM Studio model catalog](https://lmstudio.ai/models), or by Hugging Face model URL.

The response will return a `job_id` that you can use to track download progress.

See the [download](https://lmstudio.ai/docs/developer/rest/download) and [download status](https://lmstudio.ai/docs/developer/rest/download-status) docs for more details.