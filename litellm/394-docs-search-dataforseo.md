---
title: DataForSEO Search | liteLLM
url: https://docs.litellm.ai/docs/search/dataforseo
source: sitemap
fetched_at: 2026-01-21T19:54:25.637155334-03:00
rendered_js: false
word_count: 71
summary: This document explains how to integrate and use the DataForSEO search provider with LiteLLM via the Python SDK and AI Gateway.
tags:
    - dataforseo
    - litellm
    - search-api
    - python-sdk
    - ai-gateway
    - api-configuration
category: guide
---

**Get API Access:** [DataForSEO](https://dataforseo.com/)

## Setup[​](#setup "Direct link to Setup")

1. Go to [DataForSEO](https://dataforseo.com/) and create an account
2. Navigate to your account dashboard
3. Generate API credentials:
   
   - You'll receive a **login** (username)
   - You'll receive a **password**
4. Set up your environment variables:
   
   - `DATAFORSEO_LOGIN` - Your DataForSEO login/username
   - `DATAFORSEO_PASSWORD` - Your DataForSEO password

## LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

DataForSEO Search

```
import os
from litellm import search

os.environ["DATAFORSEO_LOGIN"]="your-login"
os.environ["DATAFORSEO_PASSWORD"]="your-password"

response = search(
    query="latest AI developments",
    search_provider="dataforseo",
    max_results=10
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
-search_tool_name: dataforseo-search
litellm_params:
search_provider: dataforseo
api_key:"os.environ/DATAFORSEO_LOGIN:os.environ/DATAFORSEO_PASSWORD"
```

### 2. Start the proxy[​](#2-start-the-proxy "Direct link to 2. Start the proxy")

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

### 3. Test the search endpoint[​](#3-test-the-search-endpoint "Direct link to 3. Test the search endpoint")

Test Request

```
curl http://0.0.0.0:4000/v1/search/dataforseo-search \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "latest AI developments",
    "max_results": 10
  }'
```

## Provider-specific Parameters[​](#provider-specific-parameters "Direct link to Provider-specific Parameters")

DataForSEO Search with Provider-specific Parameters

```
import os
from litellm import search

os.environ["DATAFORSEO_LOGIN"]="your-login"
os.environ["DATAFORSEO_PASSWORD"]="your-password"

response = search(
    query="AI developments",
    search_provider="dataforseo",
    max_results=10,
# DataForSEO-specific parameters
    country="United States",# Country name for location_name
    language_code="en",# Language code
    depth=20,# Number of results (max 700)
    device="desktop",# Device type ('desktop', 'mobile', 'tablet')
    os="windows"# Operating system
)
```