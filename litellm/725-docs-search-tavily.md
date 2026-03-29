---
title: Tavily Search | liteLLM
url: https://docs.litellm.ai/docs/search/tavily
source: sitemap
fetched_at: 2026-01-21T19:54:35.924576231-03:00
rendered_js: false
word_count: 31
summary: This document provides instructions and code examples for integrating Tavily Search using the LiteLLM Python SDK and AI Gateway.
tags:
    - litellm
    - tavily-search
    - python-sdk
    - ai-gateway
    - search-api
    - api-integration
category: guide
---

**Get API Key:** [https://tavily.com](https://tavily.com)

## LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

Tavily Search

```
import os
from litellm import search

os.environ["TAVILY_API_KEY"]="tvly-..."

response = search(
    query="latest AI developments",
    search_provider="tavily",
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
-search_tool_name: tavily-search
litellm_params:
search_provider: tavily
api_key: os.environ/TAVILY_API_KEY
```

### 2. Start the proxy[​](#2-start-the-proxy "Direct link to 2. Start the proxy")

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

### 3. Test the search endpoint[​](#3-test-the-search-endpoint "Direct link to 3. Test the search endpoint")

Test Request

```
curl http://0.0.0.0:4000/v1/search/tavily-search \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "latest AI developments",
    "max_results": 5
  }'
```

## Provider-specific Parameters[​](#provider-specific-parameters "Direct link to Provider-specific Parameters")

Tavily Search with Provider-specific Parameters

```
import os
from litellm import search

os.environ["TAVILY_API_KEY"]="tvly-..."

response = search(
    query="latest tech news",
    search_provider="tavily",
    max_results=5,
# Tavily-specific parameters
    topic="news",# 'general', 'news', 'finance'
    search_depth="advanced",# 'basic', 'advanced'
    include_answer=True,# Include AI-generated answer
    include_raw_content=True# Include raw HTML content
)
```