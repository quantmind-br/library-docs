---
title: Vertex AI Search Datastores | liteLLM
url: https://docs.litellm.ai/docs/pass_through/vertex_ai_search_datastores
source: sitemap
fetched_at: 2026-01-21T19:47:00.292658067-03:00
rendered_js: false
word_count: 104
summary: This document provides instructions on how to integrate and use the Vertex AI Discovery Engine Search API via LiteLLM. It covers setting up credentials, configuring managed vector stores, and performing searches through various endpoints.
tags:
    - vertex-ai
    - discovery-engine
    - search-api
    - litellm-proxy
    - vector-store
    - google-cloud
category: guide
---

Call Vertex AI Discovery Engine Search API through LiteLLM.

Provider Doc: [https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.servingConfigs/search](https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.servingConfigs/search)

## What you get[​](#what-you-get "Direct link to What you get")

- Reference datastores by ID. LiteLLM finds the credentials.
- No project/location in every request.
- Configure credentials once, use everywhere.
- Cost tracking works automatically.

## Quick Start[​](#quick-start "Direct link to Quick Start")

**Step 1. Set credentials**

```
export DEFAULT_VERTEXAI_PROJECT="your-project-id"
export DEFAULT_VERTEXAI_LOCATION="us-central1"
export DEFAULT_GOOGLE_APPLICATION_CREDENTIALS="/path/to/credentials.json"
```

**Step 2. Start proxy**

**Step 3. Search your datastore**

```
curl -X POST \
  "http://localhost:4000/vertex_ai/discovery/v1/projects/my-project/locations/global/collections/default_collection/dataStores/my-datastore/servingConfigs/default_config:search" \
  -H "Content-Type: application/json" \
  -H "x-litellm-api-key: Bearer sk-1234" \
  -d '{
    "query": "How do I authenticate?",
    "pageSize": 10
  }'
```

## Managed Vector Stores (Recommended)[​](#managed-vector-stores-recommended "Direct link to Managed Vector Stores (Recommended)")

Register your datastore once. Reference it by ID.

**In config.yaml:**

```
vector_store_registry:
-vector_store_name:"vertex-ai-litellm-website-knowledgebase"
litellm_params:
vector_store_id:"my-datastore"
custom_llm_provider:"vertex_ai/search_api"
vertex_app_id:"test-litellm-app_1761094730750"
vertex_project:"test-vector-store-db"
vertex_location:"global"
vector_store_description:"Vertex AI vector store for the Litellm website knowledgebase"
vector_store_metadata:
source:"https://www.litellm.com/docs"
```

**How it works:**

LiteLLM sees `dataStores/my-datastore` in your URL. It looks up the vector store. Uses the right project and credentials automatically.

## Endpoint[​](#endpoint "Direct link to Endpoint")

`{PROXY_BASE_URL}/vertex_ai/discovery/{endpoint:path}`

Routes to `https://discoveryengine.googleapis.com`

## Examples[​](#examples "Direct link to Examples")

### Basic Search[​](#basic-search "Direct link to Basic Search")

```
curl -X POST \
  "http://localhost:4000/vertex_ai/discovery/v1/projects/my-project/locations/global/collections/default_collection/dataStores/my-datastore/servingConfigs/default_config:search" \
  -H "Content-Type: application/json" \
  -H "x-litellm-api-key: Bearer sk-1234" \
  -d '{
    "query": "pricing",
    "pageSize": 10
  }'
```

### Search with Filters[​](#search-with-filters "Direct link to Search with Filters")

```
curl -X POST \
  "http://localhost:4000/vertex_ai/discovery/v1/projects/my-project/locations/global/collections/default_collection/dataStores/my-datastore/servingConfigs/default_config:search" \
  -H "Content-Type: application/json" \
  -H "x-litellm-api-key: Bearer sk-1234" \
  -d '{
    "query": "tutorials",
    "pageSize": 20,
    "filter": "category = \"beginner\"",
    "spellCorrectionSpec": {"mode": "AUTO"}
  }'
```

### Python[​](#python "Direct link to Python")

```
import requests

url ="http://localhost:4000/vertex_ai/discovery/v1/projects/my-project/locations/global/collections/default_collection/dataStores/my-datastore/servingConfigs/default_config:search"

response = requests.post(url,
    headers={
"Content-Type":"application/json",
"x-litellm-api-key":"Bearer sk-1234"
},
    json={"query":"pricing","pageSize":10}
)

for result in response.json().get("results",[]):
    data = result["document"]["derivedStructData"]
print(f"{data['title']}: {data['link']}")
```

### Use with Chat Completion[​](#use-with-chat-completion "Direct link to Use with Chat Completion")

```
curl http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $LITELLM_API_KEY" \
  -d '{
    "model": "claude-3-5-sonnet",
    "messages": [{"role": "user", "content": "What is litellm?"}],
    "tools": [
        {
            "type": "file_search",
            "vector_store_ids": ["my-datastore"]
        }
    ]
  }'
```