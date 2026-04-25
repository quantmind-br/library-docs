---
title: Authentication
url: https://lmstudio.ai/docs/developer/core/authentication
source: sitemap
fetched_at: 2026-04-07T21:29:52.78398597-03:00
rendered_js: false
word_count: 286
summary: This document explains how to enable and manage API Token authentication for the LM Studio server, detailing steps for creating tokens, configuring their permissions, and demonstrating usage across REST API, Python SDK, and TypeScript SDK.
tags:
    - api-token
    - authentication
    - lm-studio
    - rest-api
    - sdk-usage
    - server-settings
category: guide
---

##### Requires [LM Studio 0.4.0](https://lmstudio.ai/download) or newer.

LM Studio supports API Tokens for authentication, providing a secure and convenient way to access the LM Studio API.

### Require Authentication for each request[](#require-authentication-for-each-request)

By default, LM Studio does not require authentication for API requests. To enable authentication so that only requests with a valid API Token are accepted, toggle the switch in the Developers Page &gt; Server Settings.

Once enabled, all requests made through the REST API, Python SDK, or Typescript SDK will need to include a valid API Token. See usage [below](#api-token-usage).

![undefined](https://lmstudio.ai/assets/docs/require-auth.png)

Enable authentication to require valid API tokens for all requests

![undefined](https://lmstudio.ai/assets/docs/multiple-tokens.png)

Managing tokens in the server settings

### Creating API Tokens[](#creating-api-tokens)

To create API Tokens, click on Manage Tokens in the Server Settings. It will open the API Tokens modal where you can create, view, and delete API Tokens.

![undefined](https://lmstudio.ai/assets/docs/tokens-empty-modal.png)

Create a token by clicking on the Create Token button. Provide a name for the token and select the desired permissions.

![undefined](https://lmstudio.ai/assets/docs/create-dave-token.png)

Once created, make sure to copy the token as it will not be shown again.

![undefined](https://lmstudio.ai/assets/docs/created-dave-token.png)

### Configuring API Token Permissions[](#configuring-api-token-permissions)

To edit the permissions of an existing API Token, click on the Edit button next to the token in the API Tokens modal. You can modify the name and permissions of the token.

![undefined](https://lmstudio.ai/assets/docs/edit-token.png)

## API Token Usage[](#api-token-usage "Link to 'API Token Usage'")

### Using API Tokens with REST API:[](#using-api-tokens-with-rest-api)

The example below requires [allowing calling servers from mcp.json](https://lmstudio.ai/docs/developer/core/server/settings) to be enabled and the [Playwright MCP](https://github.com/microsoft/playwright-mcp) in mcp.json.

```

curl -X POST \
  http://localhost:1234/api/v1/chat \
  -H "Authorization: Bearer $LM_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "ibm/granite-4-micro",
    "input": "Open lmstudio.ai",
    "integrations": [
      {
        "type": "plugin",
        "id": "mcp/playwright",
        "allowed_tools": ["browser_navigate"]
      }
    ],
    "context_length": 8000
  }'
```

### Using API Tokens with Python SDK[](#using-api-tokens-with-python-sdk)

To use API tokens with the Python SDK, see the [Python SDK guide](https://lmstudio.ai/docs/python/getting-started/authentication).

### Using API Tokens with TypeScript SDK[](#using-api-tokens-with-typescript-sdk)

To use API tokens with the TypeScript SDK, see the [TS SDK guide](https://lmstudio.ai/docs/typescript/authentication).