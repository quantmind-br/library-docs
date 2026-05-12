---
title: Text Models - Fireworks AI Docs
url: https://docs.fireworks.ai/guides/querying-text-models
source: sitemap
fetched_at: 2026-04-27T20:15:14.189844781-03:00
rendered_js: false
word_count: 344
summary: This document provides a comprehensive guide and reference on accessing Fireworks AI's text models via its OpenAI-compatible APIs. It details methods for querying, including chat completions, enabling multi-turn conversations, streaming responses, handling asynchronous requests, and tracking usage metrics.
tags:
    - api-guide
    - chat-completions
    - text-models
    - openai-compatible
    - python-sdk
    - streaming-requests
    - deployment-options
category: tutorial
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Text Models

Fireworks provides fast, cost-effective access to leading open-source text models via OpenAI-compatible APIs. Query models via the chat completions API (recommended), completions API, or [[080-guides-response-api|responses API]]. [Browse 100+ available models →](https://fireworks.ai/models)

For **Priority** Tier and **Turbo** mode, see [[084-guides-serverless-products|Serverless Priority and Turbo]].

## Chat Completions API

- Python (Fireworks SDK)
- Python (OpenAI SDK)
- JavaScript
- curl

```python
from fireworks import Fireworks

client = Fireworks()

response = client.chat.completions.create(
  model="accounts/fireworks/models/deepseek-v3p1",
  messages=[{"role": "user", "content": "Explain quantum computing in simple terms"}]
)

print(response.choices[0].message.content)
```

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference/v1"
)

response = client.chat.completions.create(
    model="accounts/fireworks/models/deepseek-v3p1",
    messages=[{
        "role": "user",
        "content": "Explain quantum computing in simple terms"
    }]
)

print(response.choices[0].message.content)
```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.FIREWORKS_API_KEY,
  baseURL: "https://api.fireworks.ai/inference/v1",
});

const response = await client.chat.completions.create({
  model: "accounts/fireworks/models/deepseek-v3p1",
  messages: [
    {
      role: "user",
      content: "Explain quantum computing in simple terms",
    },
  ],
});

console.log(response.choices[0].message.content);
```

```bash
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "accounts/fireworks/models/deepseek-v3p1",
    "messages": [
      {
        "role": "user",
        "content": "Explain quantum computing in simple terms"
      }
    ]
  }'
```

## Querying Dedicated Deployments

For consistent performance, guaranteed capacity, or higher throughput, query [[070-guides-ondemand-deployments|on-demand deployments]] instead of serverless:

```
accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>
```

```python
response = client.chat.completions.create(
    model="accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
    messages=[{"role": "user", "content": "Hello"}]
)
```

## Common Patterns

### Multi-Turn Conversations

Include all previous messages to maintain conversation history:

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What's the capital of France?"},
    {"role": "assistant", "content": "The capital of France is Paris."},
    {"role": "user", "content": "What's its population?"}
]

response = client.chat.completions.create(
    model="accounts/fireworks/models/deepseek-v3p1",
    messages=messages
)
```

### System Prompts

Override the default system prompt by setting the first message with `role: "system"`. To completely omit it, set `content` to an empty string.

```python
messages = [
    {"role": "system", "content": "You are a helpful Python expert who provides concise code examples."},
    {"role": "user", "content": "How do I read a CSV file?"}
]
```

### Streaming Responses

Stream tokens as they're generated for real-time, interactive UX (covered in detail in [[009-getting-started-quickstart|Serverless Quickstart]]):

```python
stream = client.chat.completions.create(
    model="accounts/fireworks/models/deepseek-v3p1",
    messages=[{"role": "user", "content": "Tell me a story"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

**Aborting streams:** Close the connection to stop generation and avoid billing for ungenerated tokens:

```python
for chunk in stream:
    print(chunk.choices[0].delta.content, end="")
    if some_condition:
        stream.close()
        break
```

### Async Requests

Use async clients for multiple concurrent requests:

- Python (Fireworks SDK)
- Python (OpenAI SDK)
- JavaScript

```python
from fireworks import AsyncFireworks

client = AsyncFireworks()

async def main():
  response = await client.chat.completions.create(
    model="accounts/fireworks/models/deepseek-v3p1",
    messages=[{"role": "user", "content": "Hello"}]
  )
  print(response.choices[0].message.content)

asyncio.run(main())
```

```python
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key=os.environ.get("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference/v1"
)

async def main():
    response = await client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        messages=[{"role": "user", "content": "Hello"}]
    )
    print(response.choices[0].message.content)

asyncio.run(main())
```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.FIREWORKS_API_KEY,
  baseURL: "https://api.fireworks.ai/inference/v1",
});

async function main() {
  const response = await client.chat.completions.create({
    model: "accounts/fireworks/models/deepseek-v3p1",
    messages: [{ role: "user", content: "Hello" }],
  });
  console.log(response.choices[0].message.content);
}

main();
```

### Usage & Performance Tracking

- **Token usage** (prompt, completion, total tokens) is always included in the response body
- **Performance metrics** (latency, TTFT, etc.) are in response headers for non-streaming requests
- For streaming: use `perf_metrics_in_response` parameter to include metrics in the response body

- Non-streaming
- Streaming (usage only)
- Streaming (with performance metrics)

```python
response = client.chat.completions.create(
    model="accounts/fireworks/models/deepseek-v3p1",
    messages=[{"role": "user", "content": "Hello"}]
)

# Token usage (always included)
print(response.usage.prompt_tokens)       # Tokens in your prompt
print(response.usage.completion_tokens)   # Tokens generated
print(response.usage.total_tokens)        # Total tokens billed
```

```python
stream = client.chat.completions.create(
    model="accounts/fireworks/models/deepseek-v3p1",
    messages=[{"role": "user", "content": "Hello"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
    if chunk.usage:
        print(f"\n\nTokens used: {chunk.usage.total_tokens}")
        print(f"Prompt: {chunk.usage.prompt_tokens}, Completion: {chunk.usage.completion_tokens}")
```

```python
stream = client.chat.completions.create(
    model="accounts/fireworks/models/deepseek-v3p1",
    messages=[{"role": "user", "content": "Hello, world!"}],
    stream=True,
    extra_body={"perf_metrics_in_response": True}
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
    if chunk.choices[0].finish_reason:
        if chunk.usage:
            print(f"\n\nTokens: {chunk.usage.total_tokens}")
        if hasattr(chunk, 'perf_metrics'):
            print(f"Performance: {chunk.perf_metrics}")
```

See the [API reference](https://docs.fireworks.ai/api-reference/post-chatcompletions) for all available metrics.

## Understanding Tokens

Language models process text in chunks called **tokens** (1 character to 1 word in English). Different model families use different tokenizers, so token counts vary by model.

**Why tokens matter:**

- Models have maximum context lengths measured in tokens
- Pricing is based on token usage (prompt + completion)
- Token count affects response time

Use the [Llama tokenizer tool](https://belladoreai.github.io/llama-tokenizer-js/example-demo/build/) to estimate token counts for Llama models. Actual usage is always returned in the `usage` field of every API response.

## OpenAI SDK Migration

Fireworks provides an OpenAI-compatible API. For setup, examples, and compatibility notes, see [[093-tools-sdks-openai-compatibility|OpenAI compatibility guide]].

#api-guide #chat-completions #text-models #openai-compatible #python-sdk #streaming-requests #deployment-options
