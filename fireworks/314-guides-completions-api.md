---
title: Completions API
url: https://docs.fireworks.ai/guides/completions-api
source: sitemap
fetched_at: 2026-04-27T20:18:27.654105863-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - completions-api
    - text-generation
    - prompting-control
category: reference
word_count: 144
---
# Completions API

Raw text generation without automatic message formatting. Use for full control over prompt formatting or base models.

## When to use

- Custom prompt templates with specific formatting requirements
- Base models (non-instruct/non-chat variants)
- Fine-grained control over token-level formatting
- Legacy applications requiring raw completion format

> [!tip]
> For most use cases, use [[075-guides-querying-text-models]] instead — it handles message formatting automatically and works better with instruct-tuned models.

## Basic usage

```python
from fireworks import Fireworks

client = Fireworks()

response = client.completions.create(
    model="accounts/fireworks/models/deepseek-v3p1",
    prompt="Once upon a time"
)

print(response.choices[0].text)
```

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference/v1"
)

response = client.completions.create(
    model="accounts/fireworks/models/deepseek-v3p1",
    prompt="Once upon a time"
)
print(response.choices[0].text)
```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.FIREWORKS_API_KEY,
  baseURL: "https://api.fireworks.ai/inference/v1",
});

const response = await client.completions.create({
  model: "accounts/fireworks/models/deepseek-v3p1",
  prompt: "Once upon a time",
});
console.log(response.choices[0].text);
```

```bash
curl https://api.fireworks.ai/inference/v1/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "accounts/fireworks/models/deepseek-v3p1",
    "prompt": "Once upon a time"
  }'
```

Most models automatically prepend the BOS token (e.g., `<s>`). Verify with `raw_output` parameter if needed.

## Custom prompt template

```python
prompt = """Task: Classify the sentiment of the following text.

Text: I love this product!
Sentiment: Positive

Text: This is terrible.
Sentiment: Negative

Text: The weather is nice today.
Sentiment:"""

response = client.completions.create(
    model="accounts/fireworks/models/deepseek-v3p1",
    prompt=prompt,
    max_tokens=10,
    temperature=0
)
print(response.choices[0].text)  # Output: " Positive"
```

## Common parameters

All [[075-guides-querying-text-models]] parameters work with completions:

- `temperature` — randomness (0–2)
- `max_tokens` — output length limit
- `top_p`, `top_k`, `min_p` — sampling parameters
- `stream` — token-by-token streaming
- `frequency_penalty`, `presence_penalty` — repetition control

## Querying deployments

Use completions with [[070-guides-ondemand-deployments]] by specifying the deployment identifier:

```python
response = client.completions.create(
    model="accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
    prompt="Your prompt here"
)
```