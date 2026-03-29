---
title: Bedrock Knowledge Bases | liteLLM
url: https://docs.litellm.ai/docs/providers/bedrock_vector_store
source: sitemap
fetched_at: 2026-01-21T19:48:32.56353009-03:00
rendered_js: false
word_count: 166
summary: This document explains how to integrate and use AWS Bedrock Knowledge Bases as a vector store within LiteLLM for retrieval-augmented generation.
tags:
    - aws-bedrock
    - knowledge-bases
    - litellm
    - vector-store
    - rag
    - file-search
category: guide
---

AWS Bedrock Knowledge Bases allows you to connect your LLM's to your organization's data, letting your models retrieve and reference information specific to your business.

PropertyDetailsDescriptionBedrock Knowledge Bases connects your data to LLM's, enabling them to retrieve and reference your organization's information in their responses.Provider Route on LiteLLM`bedrock` in the litellm vector\_store\_registryProvider Doc[AWS Bedrock Knowledge Bases ↗](https://aws.amazon.com/bedrock/knowledge-bases/)

## Quick Start[​](#quick-start "Direct link to Quick Start")

### LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

Example using LiteLLM Python SDK

```
import os
import litellm

from litellm.vector_stores.vector_store_registry import VectorStoreRegistry, LiteLLM_ManagedVectorStore

# Init vector store registry with your Bedrock Knowledge Base
litellm.vector_store_registry = VectorStoreRegistry(
    vector_stores=[
        LiteLLM_ManagedVectorStore(
            vector_store_id="YOUR_KNOWLEDGE_BASE_ID",# KB ID from AWS Bedrock
            custom_llm_provider="bedrock"
)
]
)

# Make a completion request using your Knowledge Base
response =await litellm.acompletion(
    model="anthropic/claude-3-5-sonnet",
    messages=[{"role":"user","content":"What does our company policy say about remote work?"}],
    tools=[
{
"type":"file_search",
"vector_store_ids":["YOUR_KNOWLEDGE_BASE_ID"]
}
],
)

print(response.choices[0].message.content)
```

### LiteLLM Proxy[​](#litellm-proxy "Direct link to LiteLLM Proxy")

#### 1. Configure your vector\_store\_registry[​](#1-configure-your-vector_store_registry "Direct link to 1. Configure your vector_store_registry")

- config.yaml
- LiteLLM UI

```
model_list:
-model_name: claude-3-5-sonnet
litellm_params:
model: anthropic/claude-3-5-sonnet
api_key: os.environ/ANTHROPIC_API_KEY

vector_store_registry:
-vector_store_name:"bedrock-company-docs"
litellm_params:
vector_store_id:"YOUR_KNOWLEDGE_BASE_ID"
custom_llm_provider:"bedrock"
vector_store_description:"Bedrock Knowledge Base for company documents"
vector_store_metadata:
source:"Company internal documentation"
```

#### 2. Make a request with vector\_store\_ids parameter[​](#2-make-a-request-with-vector_store_ids-parameter "Direct link to 2. Make a request with vector_store_ids parameter")

- Curl
- OpenAI Python SDK

```
curl http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $LITELLM_API_KEY" \
  -d '{
    "model": "claude-3-5-sonnet",
    "messages": [{"role": "user", "content": "What does our company policy say about remote work?"}],
    "tools": [
        {
            "type": "file_search",
            "vector_store_ids": ["YOUR_KNOWLEDGE_BASE_ID"]
        }
    ]
  }'
```

## Filter Results[​](#filter-results "Direct link to Filter Results")

Filter by metadata attributes.

**Operators** (OpenAI-style, auto-translated):

- `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`

**AWS operators** (use directly):

- `equals`, `notEquals`, `greaterThan`, `greaterThanOrEquals`, `lessThan`, `lessThanOrEquals`, `in`, `notIn`, `startsWith`, `listContains`, `stringContains`

<!--THE END-->

- Single Filter
- AND
- OR
- AWS Operators
- Proxy

```
response =await litellm.acompletion(
    model="anthropic/claude-3-5-sonnet",
    messages=[{"role":"user","content":"What are the latest updates?"}],
    tools=[{
"type":"file_search",
"vector_store_ids":["YOUR_KNOWLEDGE_BASE_ID"],
"filters":{
"key":"category",
"value":"updates",
"operator":"eq"
}
}]
)
```

## Accessing Search Results[​](#accessing-search-results "Direct link to Accessing Search Results")

See how to access vector store search results in your response:

- [Accessing Search Results (Non-Streaming & Streaming)](https://docs.litellm.ai/docs/completion/knowledgebase#accessing-search-results-citations)

## Further Reading[​](#further-reading "Direct link to Further Reading")

Vector Stores:

- [Always on Vector Stores](https://docs.litellm.ai/docs/completion/knowledgebase#always-on-for-a-model)
- [Listing available vector stores on litellm proxy](https://docs.litellm.ai/docs/completion/knowledgebase#listing-available-vector-stores)
- [How LiteLLM Vector Stores Work](https://docs.litellm.ai/docs/completion/knowledgebase#how-it-works)