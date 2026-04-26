---
title: Adjustable | Mistral Docs
url: https://docs.mistral.ai/studio-api/conversations/reasoning/adjustable
source: sitemap
fetched_at: 2026-04-26T04:12:32.767361357-03:00
rendered_js: false
word_count: 151
summary: Use the reasoning_effort parameter to control model thinking behavior and output traces.
tags:
    - mistral-api
    - reasoning-effort
    - chat-completions
    - model-parameters
    - artificial-intelligence
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Adjustable Reasoning

Available on `mistral-small-latest` via the `reasoning_effort` parameter. Controls how much the model thinks and whether thinking traces appear.

> [!note] For chat completions basics, see [Chat Completions](https://docs.mistral.ai/studio-api/conversations/chat-completion).

## Model Support

| Model | Adjustable Reasoning |
|-------|---------------------|
| `mistral-small-latest` | Yes (via `reasoning_effort`) |

## Reasoning Effort Values

| Value | Behavior |
|-------|----------|
| `"high"` | Full thinking chunk before final answer. Higher token usage |
| `"none"` | Model thinks minimally. Thinking chunk omitted |

## Usage

```python
from mistralai.client import MistralClient

client = MistralClient(api_key="your-api-key")

# High reasoning effort
response = client.chat(
    model="mistral-small-latest",
    messages=[{"role": "user", "content": "Calculate the compound interest on 1000 at 5% for 10 years"}],
    reasoning_effort="high"
)

# No reasoning effort
response = client.chat(
    model="mistral-small-latest",
    messages=[{"role": "user", "content": "What is 2+2?"}],
    reasoning_effort="none"
)
```

## Agents & Conversations API

`reasoning_effort` is available via `completion_args` on:
- [Agents API](https://docs.mistral.ai/api/endpoint/beta/agents)
- [Conversations API](https://docs.mistral.ai/api/endpoint/beta/conversations)

SDK support coming soon.

## Example via API

```bash
curl -X POST "https://api.mistral.ai/v1/chat/completions" \
  -H "Authorization: Bearer your-api-key" \
  -d '{
    "model": "mistral-small-latest",
    "messages": [{"role": "user", "content": "Explain why the sky is blue"}],
    "reasoning_effort": "high"
  }'
```

#mistral-api #reasoning-effort #chat-completions #model-parameters #artificial-intelligence
