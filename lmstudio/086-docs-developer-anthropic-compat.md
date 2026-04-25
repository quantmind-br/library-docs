---
title: Anthropic Compatibility Endpoints
url: https://lmstudio.ai/docs/developer/anthropic-compat
source: sitemap
fetched_at: 2026-04-07T21:30:48.861204089-03:00
rendered_js: false
word_count: 143
summary: This document provides technical instructions and examples detailing how to configure API calls to point to a local LM Studio server when using Anthropic-compatible models. It shows necessary environment variable settings and working cURL and Python code snippets for interacting with the messaging endpoint.
tags:
    - api-integration
    - local-llm
    - anthropic-compatibility
    - base-url-setting
    - authentication
category: guide
---

### Supported endpoints[](#supported-endpoints)

EndpointMethodDocs`/v1/messages`POST[Messages](https://lmstudio.ai/docs/developer/anthropic-compat/messages)

* * *

## Using Claude Code with LM Studio[](#using-claude-code-with-lm-studio "Link to 'Using Claude Code with LM Studio'")

For a full walkthrough, see: [Use Claude Code with LM Studio](https://lmstudio.ai/docs/integrations/claude-code).

```

export ANTHROPIC_BASE_URL=http://localhost:1234
export ANTHROPIC_AUTH_TOKEN=lmstudio
claude --model openai/gpt-oss-20b
```

When Require Authentication is enabled, LM Studio accepts both `x-api-key` and the standard `Authorization: Bearer <token>` header. To learn more about enabling auth in LM Studio, checkout [Authentication](https://lmstudio.ai/docs/developer/core/authentication).

## Set the base URL to point to LM Studio[](#set-the-base-url-to-point-to-lm-studio "Link to 'Set the base URL to point to LM Studio'")

Point your Anthropic client (or any HTTP request) at your local LM Studio server.

Note: The following examples assume the server port is `1234`.

### cURL example[](#curl-example)

```

- curl https://api.anthropic.com/v1/messages \
+ curl http://localhost:1234/v1/messages \
   -H "Content-Type: application/json" \
+  -H "x-api-key: $LM_API_TOKEN" \
   -d '{
-    "model": "claude-4-5-sonnet",
+    "model": "ibm/granite-4-micro",
     "max_tokens": 256,
     "messages": [
       {"role": "user", "content": "Write a haiku about local LLMs."}
     ]
   }'
```

### Python example[](#python-example)

```

from anthropic import Anthropic

client = Anthropic(
    base_url="http://localhost:1234",
    api_key="lmstudio",
)

message = client.messages.create(
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Hello from LM Studio",
        }
    ],
    model="ibm/granite-4-micro",
)

print(message.content)
```

If you have not enabled Require Authentication, the `x-api-key` header is optional. For the Python example, you can also omit `api_key` when authentication is disabled.

If you're running into trouble, hop onto our [Discord](https://discord.gg/lmstudio) and enter the developers channel.