---
title: How to check if a model is available on serverless? - Fireworks AI Docs
url: https://docs.fireworks.ai/faq-new/models-inference/how-to-check-if-a-model-is-available-on-serverless
source: sitemap
fetched_at: 2026-04-27T20:12:52.581960654-03:00
rendered_js: false
word_count: 58
summary: This document explains how to programmatically retrieve all models supported by serverless infrastructure using the Fireworks AI API, providing examples in both Python and cURL.
tags:
    - api-reference
    - list-models
    - serverless
    - python-sdk
    - curl
    - fireworks
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# How to check if a model is available on serverless?

## Web UI

Go to [https://app.fireworks.ai/models?filter=LLM&serverless=true](https://app.fireworks.ai/models?filter=LLM&serverless=true)

## API

Retrieve all serverless models using the [[216-api-reference-list-models|List Models API]] with `supports_serverless=true` filter.

### Python (Fireworks SDK)

```python
from fireworks import Fireworks

client = Fireworks()

# List all serverless models
models = client.models.list(filter="supports_serverless=true")

for model in models:
    print(model.name)
```

### cURL

```bash
curl "https://api.fireworks.ai/v1/accounts/fireworks/models?filter=supports_serverless%3Dtrue" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY"
```

### Pagination

```python
models = client.models.list(
    filter="supports_serverless=true",
    page_size=50,
)

for model in models:
    print(f"{model.name}: {model.display_name}")
```

```bash
curl "https://api.fireworks.ai/v1/accounts/fireworks/models?filter=supports_serverless%3Dtrue&pageSize=50" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY"
```

> [!info]
> The filter uses [AIP-160 filter syntax](https://google.aip.dev/160). The `supports_serverless` field indicates serverless availability.

#serverless #api-reference #python-sdk #curl
