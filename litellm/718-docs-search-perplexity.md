---
title: Perplexity AI Search | liteLLM
url: https://docs.litellm.ai/docs/search/perplexity
source: sitemap
fetched_at: 2026-01-21T19:54:32.29004043-03:00
rendered_js: false
word_count: 24
summary: This document provides instructions for integrating Perplexity Search into LiteLLM using the Python SDK and the AI Gateway configuration.
tags:
    - litellm
    - perplexity-ai
    - search-api
    - ai-gateway
    - python-sdk
    - api-configuration
category: guide
---

**Get API Key:** [https://www.perplexity.ai/settings/api](https://www.perplexity.ai/settings/api)

## LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

Perplexity Search

```
import os
from litellm import search

os.environ["PERPLEXITYAI_API_KEY"]="pplx-..."

response = search(
    query="latest AI developments",
    search_provider="perplexity",
    max_results=5
)
```

## LiteLLM AI Gateway[​](#litellm-ai-gateway "Direct link to LiteLLM AI Gateway")

### 1. Setup config.yaml[​](#1-setup-configyaml "Direct link to 1. Setup config.yaml")

config.yaml

```
model_list:
-model_name: gpt-4
litellm_params:
model: gpt-4
api_key: os.environ/OPENAI_API_KEY

search_tools:
-search_tool_name: perplexity-search
litellm_params:
search_provider: perplexity
api_key: os.environ/PERPLEXITYAI_API_KEY
```

### 2. Start the proxy[​](#2-start-the-proxy "Direct link to 2. Start the proxy")

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

### 3. Test the search endpoint[​](#3-test-the-search-endpoint "Direct link to 3. Test the search endpoint")

Test Request

```
curl http://0.0.0.0:4000/v1/search/perplexity-search \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "latest AI developments",
    "max_results": 5
  }'
```