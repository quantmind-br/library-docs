---
title: Messages
url: https://lmstudio.ai/docs/developer/anthropic-compat/messages
source: sitemap
fetched_at: 2026-04-07T21:30:50.245142623-03:00
rendered_js: false
word_count: 40
summary: This document provides examples demonstrating how to interact with the `/v1/messages` endpoint using cURL for different use cases, including standard requests, streaming responses, and tool calling.
tags:
    - api-endpoint
    - message-creation
    - curl-example
    - streaming
    - tool-calling
category: reference
---

- Method: `POST`
- Endpoint: `/v1/messages`
- See Anthropic docs: [https://platform.claude.com/docs/en/api/messages/create](https://platform.claude.com/docs/en/api/messages/create)

##### cURL example

```

curl http://localhost:1234/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: $LM_API_TOKEN" \
  -d '{
    "model": "ibm/granite-4-micro",
    "max_tokens": 256,
    "messages": [
      {"role": "user", "content": "Say hello from LM Studio."}
    ]
  }'
```

If you have not enabled Require Authentication, the `x-api-key` header is optional.

##### cURL (streaming)

```

curl http://localhost:1234/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: $LM_API_TOKEN" \
  -d '{
    "model": "ibm/granite-4-micro",
    "messages": [{"role": "user", "content": "Hello"}],
    "max_tokens": 256,
    "stream": true
  }'
```

You will receive SSE events such as `message_start`, `content_block_start`, `content_block_delta`, `content_block_stop`, `message_delta`, and `message_stop`.

##### cURL (tools)

```

curl http://localhost:1234/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: $LM_API_TOKEN" \
  -d '{
    "model": "ibm/granite-4-micro",
    "max_tokens": 1024,
    "tools": [
      {
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "input_schema": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g. San Francisco, CA"
            }
          },
          "required": ["location"]
        }
      }
    ],
    "tool_choice": {"type": "any"},
    "messages": [
      {
        "role": "user",
        "content": "What is the weather like in San Francisco?"
      }
    ]
  }'
```