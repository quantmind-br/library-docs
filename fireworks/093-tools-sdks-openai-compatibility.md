---
title: OpenAI compatibility - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/openai-compatibility
source: sitemap
fetched_at: 2026-04-27T20:12:43.74788865-03:00
rendered_js: false
word_count: 159
summary: This document serves as a guide detailing how to use the Fireworks AI API by leveraging existing OpenAI client libraries. It explains methods for initializing the client using direct parameters or environment variables, and demonstrates usage for both simple completion and chat completion endpoints.
tags:
    - fireworks-ai
    - openai-python
    - api-client
    - completion
    - chat-completion
    - environment-variables
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Use the [OpenAI Python client library](https://github.com/openai/openai-python) to interact with Fireworks. For Anthropic SDK support, see [[089-tools-sdks-anthropic-compatibility]].

## Initialize the Client

### Direct Parameters

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key="<YOUR_FIREWORKS_API_KEY>",
)
```

### Environment Variables

```bash
export OPENAI_API_BASE="https://api.fireworks.ai/inference/v1"
export OPENAI_API_KEY="<YOUR_FIREWORKS_API_KEY>"
```

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url=os.environ.get("OPENAI_API_BASE", "https://api.fireworks.ai/inference/v1"),
    api_key=os.environ.get("OPENAI_API_KEY"),
)
```

### Alternative (process-wide effect)

```python
import openai

openai.api_base = "https://api.fireworks.ai/inference/v1"
openai.api_key = "<YOUR_FIREWORKS_API_KEY>"
```

## Usage

Ensure the `model` parameter refers to a [Fireworks model](https://fireworks.ai/models).

### Completion

Simple completion API that doesn't modify the provided prompt:

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key="<YOUR_FIREWORKS_API_KEY>",
)

completion = client.completions.create(
    model="accounts/fireworks/models/llama-v3p1-8b-instruct",
    prompt="The quick brown fox",
)
print(completion.choices[0].text)
```

### Chat Completion

Works best for models fine-tuned for conversation (e.g., llama*-chat variants):

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key="<YOUR_FIREWORKS_API_KEY>",
)

chat_completion = client.chat.completions.create(
    model="accounts/fireworks/models/llama-v3p1-8b-instruct",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Say this is a test"},
    ],
)
print(chat_completion.choices[0].message.content)
```

## Differences from OpenAI

### max_tokens Behavior

If `prompt`/`messages` plus `max_tokens` exceeds the model's context window, Fireworks automatically adjusts `max_tokens` downward by default. Control this with `context_length_exceeded_behavior`:

| Value | Behavior |
|---|---|
| `truncate` (default) | Automatically adjusts `max_tokens` to fit within the context window |
| `error` | Returns an error like OpenAI does |

### Token Usage for Streaming Responses

OpenAI doesn't return usage stats for streaming responses (see [forum post](https://community.openai.com/t/chat-completion-stream-api-token-usage/352964)). Fireworks returns usage stats in both cases—included in the very last chunk (the one with `finish_reason` set):

```bash
curl --request POST \
     --url https://api.fireworks.ai/inference/v1/completions \
     --header "accept: application/json" \
     --header "authorization: Bearer $API_KEY" \
     --header "content-type: application/json" \
     --data '{"model": "accounts/fireworks/models/starcoder-16b-w8a16", "prompt": "def say_hello_world():", "max_tokens": 100, "stream": true}'

data: {"choices":[{"text":"\n  print('Hello,","index":0,"finish_reason":null,"logprobs":null}],"usage":null}
data: {"choices":[{"text":" World!')\n\n\n","index":0,"finish_reason":null,"logprobs":null}],"usage":null}
data: {"choices":[{"text":"say_hello_","index":0,"finish_reason":null,"logprobs":null}],"usage":null}
data: {"choices":[{"text":"world()\n","index":0,"finish_reason":"stop","logprobs":null}],"usage":{"prompt_tokens":7,"total_tokens":24,"completion_tokens":17}}
data: [DONE]
```

#openai-compatibility #api-client #completion
