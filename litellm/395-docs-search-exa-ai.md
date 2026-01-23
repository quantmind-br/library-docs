---
title: Exa AI Search | liteLLM
url: https://docs.litellm.ai/docs/search/exa_ai
source: sitemap
fetched_at: 2026-01-21T19:54:28.260590587-03:00
rendered_js: false
word_count: 33
summary: This document provides instructions and code examples for integrating Exa AI Search with LiteLLM using both the Python SDK and the AI Gateway proxy.
tags:
    - litellm
    - exa-ai
    - search-api
    - ai-gateway
    - python-sdk
    - api-integration
category: guide
---

**Get API Key:** [https://exa.ai](https://exa.ai)

## LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

Exa AI Search

```
import os
from litellm import search

os.environ["EXA_API_KEY"]="exa-..."

response = search(
    query="latest AI developments",
    search_provider="exa_ai",
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
-search_tool_name: exa-search
litellm_params:
search_provider: exa_ai
api_key: os.environ/EXA_API_KEY
```

### 2. Start the proxy[​](#2-start-the-proxy "Direct link to 2. Start the proxy")

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

### 3. Test the search endpoint[​](#3-test-the-search-endpoint "Direct link to 3. Test the search endpoint")

Test Request

```
curl http://0.0.0.0:4000/v1/search/exa-search \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "latest AI developments",
    "max_results": 5
  }'
```

## Provider-specific Parameters[​](#provider-specific-parameters "Direct link to Provider-specific Parameters")

Exa AI Search with Provider-specific Parameters

```
import os
from litellm import search

os.environ["EXA_API_KEY"]="exa-..."

response = search(
    query="AI research papers",
    search_provider="exa_ai",
    max_results=10,
    search_domain_filter=["arxiv.org"],
# Exa-specific parameters
type="neural",# 'neural', 'keyword', or 'auto'
    contents={"text":True},# Request text content
    use_autoprompt=True# Enable Exa's autoprompt
)
```