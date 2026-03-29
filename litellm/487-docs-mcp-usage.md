---
title: Using your MCP | liteLLM
url: https://docs.litellm.ai/docs/mcp_usage
source: sitemap
fetched_at: 2026-01-21T19:45:45.391200421-03:00
rendered_js: false
word_count: 0
summary: This document provides a curl command example for making a streaming request to an API endpoint that utilizes Model Context Protocol (MCP) tools.
tags:
    - api-request
    - mcp-tools
    - litellm-proxy
    - curl-command
    - streaming-api
    - tool-calling
category: reference
---

```
curl --location 'http://localhost:4000/v1/responses' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer sk-1234" \
--data '{
    "model": "gpt-5",
    "input": [
    {
      "role": "user",
      "content": "give me TLDR of what BerriAI/litellm repo is about",
      "type": "message"
    }
  ],
    "tools": [
        {
            "type": "mcp",
            "server_label": "litellm",
            "server_url": "litellm_proxy/mcp",
            "require_approval": "never",
            "allowed_tools": ["GitMCP-fetch_litellm_documentation"]
        }
    ],
    "stream": true,
    "tool_choice": "required"
}'
```