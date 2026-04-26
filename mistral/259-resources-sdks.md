---
title: SDKs | Mistral Docs
url: https://docs.mistral.ai/resources/sdks
source: sitemap
fetched_at: 2026-04-26T04:11:44.710399125-03:00
rendered_js: false
word_count: 85
summary: Official Mistral AI SDK clients for Python and TypeScript as simplified interfaces for API interaction.
tags:
    - sdk-client
    - python-sdk
    - typescript-sdk
    - api-integration
    - mistral-ai
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# SDK Clients

SDK Clients provide clean, simple interfaces to Mistral AI API endpoints. Use official SDKs to interact with APIs.

## Official SDKs

- **Python** — [GitHub](https://github.com/mistralai/client-python) | `pip install mistralai`
- **TypeScript** — [GitHub](https://github.com/mistralai/client-typescript)

Third-party non-official SDKs exist for other languages.

## Installation

```bash
pip install mistralai
```

## Quick Example

```python
from mistralai.client import MistralClient

client = MistralClient(api_key="your-api-key")

chat_response = client.chat(
    model="mistral-large-latest",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

More examples available in the [Python client examples](https://github.com/mistralai/client-python/tree/main/examples).

#sdk-client #python-sdk #typescript-sdk #api-integration #mistral-ai
