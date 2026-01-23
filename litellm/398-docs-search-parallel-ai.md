---
title: Parallel AI Search | liteLLM
url: https://docs.litellm.ai/docs/search/parallel_ai
source: sitemap
fetched_at: 2026-01-21T19:54:32.091144282-03:00
rendered_js: false
word_count: 33
summary: This document provides instructions for integrating Parallel AI Search with LiteLLM using the Python SDK and the AI Gateway, including configuration steps and provider-specific parameters.
tags:
    - litellm
    - parallel-ai
    - python-sdk
    - ai-gateway
    - search-api
    - api-integration
category: tutorial
---

**Get API Key:** [https://www.parallel.ai](https://www.parallel.ai)

## LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

Parallel AI Search

```
import os
from litellm import search

os.environ["PARALLEL_AI_API_KEY"]="..."

response = search(
    query="latest AI developments",
    search_provider="parallel_ai",
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
-search_tool_name: parallel-search
litellm_params:
search_provider: parallel_ai
api_key: os.environ/PARALLEL_AI_API_KEY
```

### 2. Start the proxy[​](#2-start-the-proxy "Direct link to 2. Start the proxy")

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

### 3. Test the search endpoint[​](#3-test-the-search-endpoint "Direct link to 3. Test the search endpoint")

Test Request

```
curl http://0.0.0.0:4000/v1/search/parallel-search \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "latest AI developments",
    "max_results": 5
  }'
```

## Provider-specific Parameters[​](#provider-specific-parameters "Direct link to Provider-specific Parameters")

Parallel AI Search with Provider-specific Parameters

```
import os
from litellm import search

os.environ["PARALLEL_AI_API_KEY"]="..."

response = search(
    query="latest developments in quantum computing",
    search_provider="parallel_ai",
    max_results=5,
# Parallel AI-specific parameters
    processor="pro",# 'base' or 'pro'
    max_chars_per_result=500# Max characters per result
)
```