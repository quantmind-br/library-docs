---
title: Responses
url: https://lmstudio.ai/docs/developer/openai-compat/responses
source: sitemap
fetched_at: 2026-04-07T21:30:41.084652699-03:00
rendered_js: false
word_count: 52
summary: This document details the different methods for interacting with a response generation endpoint, including non-streaming calls, stateful follow-up using previous response IDs, streaming responses via SSE events, and advanced usage with external tools via Remote MCP.
tags:
    - api-endpoint
    - rest-request
    - openai-api
    - streaming
    - curl-example
category: reference
---

- Method: `POST`
- See OpenAI docs: [https://platform.openai.com/docs/api-reference/responses](https://platform.openai.com/docs/api-reference/responses)

##### cURL (non‑streaming)

```

curl http://localhost:1234/v1/responses \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai/gpt-oss-20b",
    "input": "Provide a prime number less than 50",
    "reasoning": { "effort": "low" }
  }'
```

##### Stateful follow‑up

Use the `id` from a previous response as `previous_response_id`.

```

curl http://localhost:1234/v1/responses \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai/gpt-oss-20b",
    "input": "Multiply it by 2",
    "previous_response_id": "resp_123"
  }'
```

##### Streaming

```

curl http://localhost:1234/v1/responses \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai/gpt-oss-20b",
    "input": "Hello",
    "stream": true
  }'
```

You will receive SSE events such as `response.created`, `response.output_text.delta`, and `response.completed`.

##### Tools and Remote MCP (opt‑in)

Enable Remote MCP in the app (Developer → Settings). Example payload using an MCP server tool:

```

curl http://localhost:1234/v1/responses \
  -H "Content-Type: application/json" \
  -d '{
    "model": "ibm/granite-4-micro",
    "input": "What is the top trending model on hugging face?",
    "tools": [
      {
        "type": "mcp",
        "server_label": "huggingface",
        "server_url": "https://huggingface.co/mcp",
        "allowed_tools": [
          "model_search"
        ]
      }
    ]
  }'
```