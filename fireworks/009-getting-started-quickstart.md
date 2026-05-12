---
title: Serverless Quickstart - Fireworks AI Docs
url: https://docs.fireworks.ai/getting-started/quickstart
source: sitemap
fetched_at: 2026-04-27T20:15:14.215760974-03:00
rendered_js: false
word_count: 294
summary: This document provides a quickstart guide detailing how to begin using open models via Fireworks API, covering setup, making initial API calls in various languages (Python and JavaScript), and demonstrating advanced features like streaming responses and function calling.
tags:
    - serverless
    - api-quickstart
    - model-interaction
    - fireworks-ai
    - sdk-guide
    - streaming-response
    - function-calling
category: tutorial
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Serverless is the fastest way to get started with open models. This quickstart walks you through your first API call in minutes.

## Step 1: Create and export an API key

Create an API key in the [Fireworks dashboard](https://app.fireworks.ai/settings/users/api-keys). Export it as an environment variable:

```bash
export FIREWORKS_API_KEY="your_api_key_here"   # macOS / Linux
setx FIREWORKS_API_KEY "your_api_key_here"     # Windows
```

## Step 2: Make your first Serverless API call

Install the [[094-tools-sdks-python-sdk]] first, then choose your SDK:

| SDK | Package | Base URL |
|---|---|---|
| Fireworks Python | `pip install fireworks` | `https://api.fireworks.ai/inference/v1` |
| OpenAI Python | `pip install openai` | `https://api.fireworks.ai/inference/v1` |
| Anthropic Python | `pip install anthropic` | `https://api.fireworks.ai/inference` |
| OpenAI JS/TS | `npm install openai` | `https://api.fireworks.ai/inference/v1` |
| Anthropic JS/TS | `npm install @anthropic-ai/sdk` | `https://api.fireworks.ai/inference` |
| curl | — | — |

```python
from fireworks import Fireworks

client = Fireworks()

response = client.chat.completions.create(
  model="accounts/fireworks/models/deepseek-v3p1",
  messages=[{"role": "user", "content": "Say hello in Spanish"}],
)

print(response.choices[0].message.content)
# → "¡Hola!"
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
    messages=[{"role": "user", "content": "Say hello in Spanish"}],
)

print(response.choices[0].message.content)
```

```python
import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.environ.get("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference"
)

response = client.messages.create(
    model="accounts/fireworks/models/deepseek-v3p1",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Say hello in Spanish"}],
)

print(response.content[0].text)
```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.FIREWORKS_API_KEY,
  baseURL: "https://api.fireworks.ai/inference/v1",
});

const response = await client.chat.completions.create({
  model: "accounts/fireworks/models/deepseek-v3p1",
  messages: [{ role: "user", content: "Say hello in Spanish" }],
});

console.log(response.choices[0].message.content);
```

```javascript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.FIREWORKS_API_KEY,
  baseURL: "https://api.fireworks.ai/inference",
});

const response = await client.messages.create({
  model: "accounts/fireworks/models/deepseek-v3p1",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Say hello in Spanish" }],
});

console.log(response.content[0].text);
```

```bash
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "accounts/fireworks/models/deepseek-v3p1",
    "messages": [{"role": "user", "content": "Say hello in Spanish"}]
  }'
```

## Common use cases

### Streaming responses

Stream token-by-token with `stream=True`:

```python
from fireworks import Fireworks

client = Fireworks()

stream = client.chat.completions.create(
  model="accounts/fireworks/models/deepseek-v3p1",
  messages=[{"role": "user", "content": "Tell me a short story"}],
  stream=True
)

for chunk in stream:
  if chunk.choices[0].delta.content:
    print(chunk.choices[0].delta.content, end="")
```

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference/v1"
)

stream = client.chat.completions.create(
    model="accounts/fireworks/models/deepseek-v3p1",
    messages=[{"role": "user", "content": "Tell me a short story"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

```python
import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.environ.get("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference"
)

with client.messages.stream(
    model="accounts/fireworks/models/deepseek-v3p1",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Tell me a short story"}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.FIREWORKS_API_KEY,
  baseURL: "https://api.fireworks.ai/inference/v1",
});

const stream = await client.chat.completions.create({
  model: "accounts/fireworks/models/deepseek-v3p1",
  messages: [{ role: "user", content: "Tell me a short story" }],
  stream: true,
});

for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content || "");
}
```

```javascript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.FIREWORKS_API_KEY,
  baseURL: "https://api.fireworks.ai/inference",
});

const stream = client.messages.stream({
  model: "accounts/fireworks/models/deepseek-v3p1",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Tell me a short story" }],
});

stream.on("text", (text) => process.stdout.write(text));
await stream.finalMessage();
```

```bash
curl https://api.fireworks.ai/inference/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $FIREWORKS_API_KEY" \
    -d '{
      "model": "accounts/fireworks/models/deepseek-v3p1",
      "messages": [{"role": "user", "content": "Tell me a short story"}],
      "stream": true
    }'
```

### Function calling

Connect models to external tools and APIs:

```python
from fireworks import Fireworks

client = Fireworks()

response = client.chat.completions.create(
    model="accounts/fireworks/models/kimi-k2-instruct-0905",
    messages=[{"role": "user", "content": "What's the weather in Paris?"}],
    tools=[
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get the current weather for a location",
                "parameters": {
                    "type": "object",
                    "properties": {"location": {"type": "string", "description": "City name, e.g. San Francisco"}},
                    "required": ["location"],
                },
            },
        },
    ],
)

print(response.choices[0].message.tool_calls)
```

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference/v1",
)

response = client.chat.completions.create(
    model="accounts/fireworks/models/kimi-k2-instruct-0905",
    messages=[{"role": "user", "content": "What's the weather in Paris?"}],
    tools=[
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get the current weather for a location",
                "parameters": {
                    "type": "object",
                    "properties": {"location": {"type": "string", "description": "City name, e.g. San Francisco"}},
                    "required": ["location"],
                },
            },
        },
    ],
)

print(response.choices[0].message.tool_calls)
```

```python
import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.environ.get("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference"
)

response = client.messages.create(
    model="accounts/fireworks/models/kimi-k2-instruct-0905",
    max_tokens=1024,
    messages=[{"role": "user", "content": "What's the weather in Paris?"}],
    tools=[
        {
            "name": "get_weather",
            "description": "Get the current weather for a location",
            "input_schema": {
                "type": "object",
                "properties": {"location": {"type": "string", "description": "City name, e.g. San Francisco"}},
                "required": ["location"],
            },
        },
    ],
)

for block in response.content:
    if block.type == "tool_use":
        print(f"Tool: {block.name}, Input: {block.input}")
```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.FIREWORKS_API_KEY,
  baseURL: "https://api.fireworks.ai/inference/v1",
});

const tools = [
  {
    type: "function",
    function: {
      name: "get_weather",
      description: "Get the current weather for a location",
      parameters: {
        type: "object",
        properties: { location: { type: "string", description: "City name, e.g. San Francisco" } },
        required: ["location"],
      },
    },
  },
];

const response = await client.chat.completions.create({
  model: "accounts/fireworks/models/kimi-k2-instruct-0905",
  messages: [{ role: "user", content: "What's the weather in Paris?" }],
  tools: tools,
});

console.log(response.choices[0].message.tool_calls);
```

```javascript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.FIREWORKS_API_KEY,
  baseURL: "https://api.fireworks.ai/inference",
});

const response = await client.messages.create({
  model: "accounts/fireworks/models/kimi-k2-instruct-0905",
  max_tokens: 1024,
  messages: [{ role: "user", content: "What's the weather in Paris?" }],
  tools: [
    {
      name: "get_weather",
      description: "Get the current weather for a location",
      input_schema: {
        type: "object",
        properties: { location: { type: "string", description: "City name, e.g. San Francisco" } },
        required: ["location"],
      },
    },
  ],
});

for (const block of response.content) {
  if (block.type === "tool_use") {
    console.log(`Tool: ${block.name}, Input:`, block.input);
  }
}
```

```bash
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "accounts/fireworks/models/kimi-k2-instruct-0905",
    "messages": [{"role": "user", "content": "What'\''s the weather in Paris?"}],
    "tools": [{"type": "function", "function": {"name": "get_weather", "description": "Get the current weather for a location", "parameters": {"type": "object", "properties": {"location": {"type": "string", "description": "City name, e.g. San Francisco"}}, "required": ["location"]}}}]
  }'
```

> [!tip]
> [Learn more about function calling →]([[069-guides-function-calling]])

### Structured outputs (JSON mode)

Get reliable JSON responses matching your schema:

```python
from fireworks import Fireworks

client = Fireworks()

response = client.chat.completions.create(
  model="accounts/fireworks/models/deepseek-v3p1",
  messages=[{"role": "user", "content": "Extract the name and age from: John is 30 years old"}],
  response_format={
    "type": "json_schema",
    "json_schema": {
      "name": "person",
      "schema": {
        "type": "object",
        "properties": {"name": {"type": "string"}, "age": {"type": "number"}},
        "required": ["name", "age"],
      },
    },
  },
)

print(response.choices[0].message.content)
```

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference/v1",
)

response = client.chat.completions.create(
    model="accounts/fireworks/models/deepseek-v3p1",
    messages=[{"role": "user", "content": "Extract the name and age from: John is 30 years old"}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "person",
            "schema": {
                "type": "object",
                "properties": {"name": {"type": "string"}, "age": {"type": "number"}},
                "required": ["name", "age"],
            },
        },
    },
)

print(response.choices[0].message.content)
```

```python
import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.environ.get("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference"
)

response = client.messages.create(
    model="accounts/fireworks/models/deepseek-v3p1",
    max_tokens=1024,
    output_config={
        "format": {
            "type": "json_schema",
            "schema": {
                "type": "object",
                "properties": {"name": {"type": "string"}, "age": {"type": "number"}},
                "required": ["name", "age"],
            },
        }
    },
    messages=[{"role": "user", "content": "Extract the name and age from: John is 30 years old"}],
)

print(response.content[0].text)
```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.FIREWORKS_API_KEY,
  baseURL: "https://api.fireworks.ai/inference/v1",
});

const response = await client.chat.completions.create({
  model: "accounts/fireworks/models/deepseek-v3p1",
  messages: [{ role: "user", content: "Extract the name and age from: John is 30 years old" }],
  response_format: {
    type: "json_schema",
    json_schema: {
      name: "person",
      schema: {
        type: "object",
        properties: { name: { type: "string" }, age: { type: "number" } },
        required: ["name", "age"],
      },
    },
  },
});

console.log(response.choices[0].message.content);
```

```javascript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.FIREWORKS_API_KEY,
  baseURL: "https://api.fireworks.ai/inference",
});

const response = await client.messages.create({
  model: "accounts/fireworks/models/deepseek-v3p1",
  max_tokens: 1024,
  output_config: {
    format: {
      type: "json_schema",
      schema: {
        type: "object",
        properties: { name: { type: "string" }, age: { type: "number" } },
        required: ["name", "age"],
      },
    },
  },
  messages: [{ role: "user", content: "Extract the name and age from: John is 30 years old" }],
});

console.log(response.content[0].text);
```

```bash
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "accounts/fireworks/models/deepseek-v3p1",
    "messages": [{"role": "user", "content": "Extract the name and age from: John is 30 years old"}],
    "response_format": {"type": "json_schema", "json_schema": {"name": "person", "schema": {"type": "object", "properties": {"name": {"type": "string"}, "age": {"type": "number"}}, "required": ["name", "age"]}}}
  }'
```

> [!tip]
> [Learn more about structured outputs →]([[088-structured-responses-structured-response-formatting]])

### Reasoning

Some models expose their internal reasoning process before giving the final answer. Reasoning content is returned in a separate field:

```python
from fireworks import Fireworks

client = Fireworks()

response = client.chat.completions.create(
    model="accounts/fireworks/models/deepseek-v3p2",
    messages=[{"role": "user", "content": "What is 25 * 37? Show your work."}],
    reasoning_effort="medium",
)

msg = response.choices[0].message
if msg.reasoning_content:
    print("Reasoning:", msg.reasoning_content)
print("Answer:", msg.content)
```

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference/v1",
)

response = client.chat.completions.create(
    model="accounts/fireworks/models/deepseek-v3p2",
    messages=[{"role": "user", "content": "What is 25 * 37? Show your work."}],
    extra_body={"reasoning_effort": "medium"},
)

msg = response.choices[0].message
# Reasoning content is returned in a separate field
reasoning = getattr(msg, "reasoning_content", None)
if reasoning is None and hasattr(msg, "model_extra"):
    reasoning = msg.model_extra.get("reasoning_content")

if reasoning:
    print("Reasoning:", reasoning)
print("Answer:", msg.content)
```

The Anthropic SDK uses the `thinking` parameter:

```python
import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.environ.get("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference"
)

response = client.messages.create(
    model="accounts/fireworks/models/deepseek-v3p2",
    max_tokens=16000,
    thinking={"type": "enabled", "budget_tokens": 4096},
    messages=[{"role": "user", "content": "What is 25 * 37? Show your work."}],
)

for block in response.content:
    if block.type == "thinking":
        print("Thinking:", block.thinking)
    elif block.type == "text":
        print("Answer:", block.text)
```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.FIREWORKS_API_KEY,
  baseURL: "https://api.fireworks.ai/inference/v1",
});

const response = await client.chat.completions.create({
  model: "accounts/fireworks/models/deepseek-v3p2",
  messages: [{ role: "user", content: "What is 25 * 37? Show your work." }],
  reasoning_effort: "medium",
});

const msg = response.choices[0].message;
if (msg.reasoning_content) {
  console.log("Reasoning:", msg.reasoning_content);
}
console.log("Answer:", msg.content);
```

```javascript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.FIREWORKS_API_KEY,
  baseURL: "https://api.fireworks.ai/inference",
});

const response = await client.messages.create({
  model: "accounts/fireworks/models/deepseek-v3p2",
  max_tokens: 16000,
  thinking: { type: "enabled", budget_tokens: 4096 },
  messages: [{ role: "user", content: "What is 25 * 37? Show your work." }],
});

for (const block of response.content) {
  if (block.type === "thinking") {
    console.log("Thinking:", block.thinking);
  } else if (block.type === "text") {
    console.log("Answer:", block.text);
  }
}
```

```bash
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "accounts/fireworks/models/deepseek-v3p2",
    "messages": [{"role": "user", "content": "What is 25 * 37? Show your work."}],
    "reasoning_effort": "medium"
  }'
```

> [!tip]
> [Learn more about reasoning →]([[078-guides-reasoning]])

### Vision models

Analyze images with vision-language models:

```python
from fireworks import Fireworks

client = Fireworks()

response = client.chat.completions.create(
  model="accounts/fireworks/models/qwen2p5-vl-32b-instruct",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What's in this image?"},
        {
          "type": "image_url",
          "image_url": {"url": "https://storage.googleapis.com/fireworks-public/image_assets/fireworks-ai-wordmark-color-dark.png"},
        },
      ],
    }
  ],
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
    model="accounts/fireworks/models/qwen2p5-vl-32b-instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {"url": "https://storage.googleapis.com/fireworks-public/image_assets/fireworks-ai-wordmark-color-dark.png"},
                },
            ],
        }
    ],
)

print(response.choices[0].message.content)
```

```python
import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.environ.get("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference"
)

response = client.messages.create(
    model="accounts/fireworks/models/qwen2p5-vl-32b-instruct",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image",
                    "source": {
                        "type": "url",
                        "url": "https://storage.googleapis.com/fireworks-public/image_assets/fireworks-ai-wordmark-color-dark.png",
                    },
                },
            ],
        }
    ],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.FIREWORKS_API_KEY,
  baseURL: "https://api.fireworks.ai/inference/v1",
});

const response = await client.chat.completions.create({
  model: "accounts/fireworks/models/qwen2p5-vl-32b-instruct",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "What's in this image?" },
        { type: "image_url", image_url: { url: "https://storage.googleapis.com/fireworks-public/image_assets/fireworks-ai-wordmark-color-dark.png" } },
      ],
    },
  ],
});

console.log(response.choices[0].message.content);
```

```javascript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.FIREWORKS_API_KEY,
  baseURL: "https://api.fireworks.ai/inference",
});

const response = await client.messages.create({
  model: "accounts/fireworks/models/qwen2p5-vl-32b-instruct",
  max_tokens: 1024,
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "What's in this image?" },
        { type: "image", source: { type: "url", url: "https://storage.googleapis.com/fireworks-public/image_assets/fireworks-ai-wordmark-color-dark.png" } },
      ],
    },
  ],
});

for (const block of response.content) {
  if (block.type === "text") console.log(block.text);
}
```

```bash
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "accounts/fireworks/models/qwen2p5-vl-32b-instruct",
    "messages": [{"role": "user", "content": [{"type": "text", "text": "What'\''s in this image?"}, {"type": "image_url", "image_url": {"url": "https://storage.googleapis.com/fireworks-public/image_assets/fireworks-ai-wordmark-color-dark.png"}}]}]
  }'
```

> [!tip]
> [Learn more about vision models →]([[076-guides-querying-vision-language-models]])

## Serverless model lifecycle

Serverless models are managed by the Fireworks team and may be updated or deprecated as new models are released. Fireworks provides **at least 2 weeks advance notice** before removing any model, with longer notice for popular models.

> [!warning]
> **For production workloads requiring long-term model stability**, use [[070-guides-ondemand-deployments]] for full control over model versions and updates.
