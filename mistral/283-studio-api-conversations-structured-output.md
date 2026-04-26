---
title: Structured Outputs | Mistral Docs
url: https://docs.mistral.ai/studio-api/conversations/structured-output
source: sitemap
fetched_at: 2026-04-26T04:12:36.888548677-03:00
rendered_js: false
word_count: 184
summary: Utilize structured outputs in LLM workflows, comparing standard JSON mode with custom schema enforcement for reliable data formatting.
tags:
    - structured-outputs
    - llm-agents
    - json-mode
    - data-formatting
    - api-integration
    - prompt-engineering
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Structured Outputs

When using LLMs as agents or in pipelines, outputs often need to follow a specific structured format — typically JSON.

> [!note] For chat completions basics, see [Chat Completions](https://docs.mistral.ai/studio-api/conversations/chat-completion).

## Methods

| Method | Reliability | Use Case |
|--------|-------------|----------|
| **JSON Mode** | Good | Flexible JSON output with structure |
| **Custom Structured Outputs** | Best | Enforce specific schema format |

> [!tip] Iterate on prompts regardless of method. Use JSON mode for flexibility, custom for stricter reliability.

## JSON Mode

Set `response_format` to `{"type": "json_object"}`. Still recommend explicitly asking for JSON in your prompt.

```python
response = client.chat(
    model="mistral-large-latest",
    messages=[{"role": "user", "content": "Return a JSON object with user name and email"}],
    response_format={"type": "json_object"}
)
```

See [JSON Mode](https://docs.mistral.ai/studio-api/conversations/structured-output/json_mode) for details.

## Custom Structured Outputs

Define your own schema using Pydantic, Zod, or JSON Schema. More reliable for enforced format requirements.

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str

response = client.chat(
    model="mistral-large-latest",
    messages=[{"role": "user", "content": "Extract user info from: John Doe, john@example.com"}],
    response_format=User
)
```

See [Custom Structured Outputs](https://docs.mistral.ai/studio-api/conversations/structured-output/custom) for details.

#structured-outputs #llm-agents #json-mode #data-formatting #api-integration #prompt-engineering
