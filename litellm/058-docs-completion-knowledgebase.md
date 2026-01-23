---
title: Using Vector Stores (Knowledge Bases) | liteLLM
url: https://docs.litellm.ai/docs/completion/knowledgebase
source: sitemap
fetched_at: 2026-01-21T19:44:29.784252439-03:00
rendered_js: false
word_count: 1135
summary: This document explains how to integrate and manage various vector stores with LiteLLM to provide models with access to organizational data for retrieval-augmented generation.
tags:
    - litellm
    - vector-stores
    - rag-integration
    - bedrock-knowledge-base
    - openai-vector-stores
    - vertex-ai-rag
    - pg-vector
category: guide
---

Use Vector Stores with any LiteLLM supported model

LiteLLM integrates with vector stores, allowing your models to access your organization's data for more accurate and contextually relevant responses.

## Supported Vector Stores[​](#supported-vector-stores "Direct link to Supported Vector Stores")

- [Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/)
- [OpenAI Vector Stores](https://platform.openai.com/docs/api-reference/vector-stores/search)
- [Azure Vector Stores](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/file-search?tabs=python#vector-stores) (Cannot be directly queried. Only available for calling in Assistants messages.)
- [Azure AI Search](https://docs.litellm.ai/docs/providers/azure_ai_vector_stores) (Vector search with Azure AI Search indexes)
- [Vertex AI RAG API](https://cloud.google.com/vertex-ai/generative-ai/docs/rag-overview)
- [Gemini File Search](https://ai.google.dev/gemini-api/docs/file-search)
- [RAGFlow Datasets](https://docs.litellm.ai/docs/providers/ragflow_vector_store) (Dataset management only, search not supported)

## Quick Start[​](#quick-start "Direct link to Quick Start")

In order to use a vector store with LiteLLM, you need to

- Initialize litellm.vector\_store\_registry
- Pass tools with vector\_store\_ids to the completion request. Where `vector_store_ids` is a list of vector store ids you initialized in litellm.vector\_store\_registry

### LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

LiteLLM's allows you to use vector stores in the [OpenAI API spec](https://platform.openai.com/docs/api-reference/chat/create) by passing a tool with vector\_store\_ids you want to use

Basic Bedrock Knowledge Base Usage

```
import os
import litellm

from litellm.vector_stores.vector_store_registry import VectorStoreRegistry, LiteLLM_ManagedVectorStore

# Init vector store registry
litellm.vector_store_registry = VectorStoreRegistry(
    vector_stores=[
        LiteLLM_ManagedVectorStore(
            vector_store_id="T37J8R4WTM",
            custom_llm_provider="bedrock"
)
]
)


# Make a completion request with vector_store_ids parameter
response =await litellm.acompletion(
    model="anthropic/claude-3-5-sonnet",
    messages=[{"role":"user","content":"What is litellm?"}],
    tools=[
{
"type":"file_search",
"vector_store_ids":["T37J8R4WTM"]
}
],
)

print(response.choices[0].message.content)
```

### LiteLLM Proxy[​](#litellm-proxy "Direct link to LiteLLM Proxy")

#### 1. Configure your vector\_store\_registry[​](#1-configure-your-vector_store_registry "Direct link to 1. Configure your vector_store_registry")

In order to use a vector store with LiteLLM, you need to configure your vector\_store\_registry. This tells litellm which vector stores to use and api provider to use for the vector store.

- config.yaml
- LiteLLM UI

config.yaml

```
model_list:
-model_name: claude-3-5-sonnet
litellm_params:
model: anthropic/claude-3-5-sonnet
api_key: os.environ/ANTHROPIC_API_KEY

vector_store_registry:
-vector_store_name:"bedrock-litellm-website-knowledgebase"
litellm_params:
vector_store_id:"T37J8R4WTM"
custom_llm_provider:"bedrock"
vector_store_description:"Bedrock vector store for the Litellm website knowledgebase"
vector_store_metadata:
source:"https://www.litellm.com/docs"

```

#### 2. Make a request with vector\_store\_ids parameter[​](#2-make-a-request-with-vector_store_ids-parameter "Direct link to 2. Make a request with vector_store_ids parameter")

- Curl
- OpenAI Python SDK

Curl Request to LiteLLM Proxy

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
            "vector_store_ids": ["T37J8R4WTM"]
        }
    ]
  }'
```

## Provider Specific Guides[​](#provider-specific-guides "Direct link to Provider Specific Guides")

This section covers how to add your vector stores to LiteLLM. If you want support for a new provider, please file an issue [here](https://github.com/BerriAI/litellm/issues).

### Bedrock Knowledge Bases[​](#bedrock-knowledge-bases "Direct link to Bedrock Knowledge Bases")

**1. Set up your Bedrock Knowledge Base**

Ensure you have a Bedrock Knowledge Base created in your AWS account with the appropriate permissions configured.

**2. Add to LiteLLM UI**

1. Navigate to **Tools &gt; Vector Stores &gt; "Add new vector store"**
2. Select **"Bedrock"** as the provider
3. Enter your Bedrock Knowledge Base ID in the **"Vector Store ID"** field

### Vertex AI RAG Engine[​](#vertex-ai-rag-engine "Direct link to Vertex AI RAG Engine")

**1. Get your Vertex AI RAG Engine ID**

1. Navigate to your RAG Engine Corpus in the [Google Cloud Console](https://console.cloud.google.com/vertex-ai/rag/corpus)
2. Select the **RAG Engine** you want to integrate with LiteLLM

<!--THE END-->

3. Click the **"Details"** button and copy the UUID for the RAG Engine
4. The ID should look like: `6917529027641081856`

**2. Add to LiteLLM UI**

1. Navigate to **Tools &gt; Vector Stores &gt; "Add new vector store"**
2. Select **"Vertex AI RAG Engine"** as the provider
3. Enter your Vertex AI RAG Engine ID in the **"Vector Store ID"** field

### PG Vector[​](#pg-vector "Direct link to PG Vector")

**1. Deploy the litellm-pg-vector-store connector**

LiteLLM provides a server that exposes OpenAI-compatible `vector_store` endpoints for PG Vector. The LiteLLM Proxy server connects to your deployed service and uses it as a vector store when querying.

1. Follow the deployment instructions for the litellm-pg-vector-store connector [here](https://github.com/BerriAI/litellm-pgvector)
2. For detailed configuration options, see the [configuration guide](https://github.com/BerriAI/litellm-pgvector?tab=readme-ov-file#configuration)

**Example .env configuration for deploying litellm-pg-vector-store:**

```
DATABASE_URL="postgresql://neondb_owner:xxxx"
SERVER_API_KEY="sk-1234"
HOST="0.0.0.0"
PORT=8001
EMBEDDING__MODEL="text-embedding-ada-002"
EMBEDDING__BASE_URL="http://localhost:4000"
EMBEDDING__API_KEY="sk-1234"
EMBEDDING__DIMENSIONS=1536
DB_FIELDS__ID_FIELD="id"
DB_FIELDS__CONTENT_FIELD="content"
DB_FIELDS__METADATA_FIELD="metadata"
DB_FIELDS__EMBEDDING_FIELD="embedding"
DB_FIELDS__VECTOR_STORE_ID_FIELD="vector_store_id"
DB_FIELDS__CREATED_AT_FIELD="created_at"
```

**2. Add to LiteLLM UI**

Once your litellm-pg-vector-store is deployed:

1. Navigate to **Tools &gt; Vector Stores &gt; "Add new vector store"**
2. Select **"PG Vector"** as the provider
3. Enter your **API Base URL** and **API Key** for your `litellm-pg-vector-store` container
   
   - The API Key field corresponds to the `SERVER_API_KEY` from your .env configuration

### OpenAI Vector Stores[​](#openai-vector-stores "Direct link to OpenAI Vector Stores")

**1. Set up your OpenAI Vector Store**

1. Create your Vector Store on the [OpenAI platform](https://platform.openai.com/storage/vector_stores)
2. Note your Vector Store ID (format: `vs_687ae3b2439881918b433cb99d10662e`)

**2. Add to LiteLLM UI**

1. Navigate to **Tools &gt; Vector Stores &gt; "Add new vector store"**
2. Select **"OpenAI"** as the provider
3. Enter your **Vector Store ID** in the corresponding field
4. Enter your **OpenAI API Key** in the API Key field

## Advanced[​](#advanced "Direct link to Advanced")

### Logging Vector Store Usage[​](#logging-vector-store-usage "Direct link to Logging Vector Store Usage")

LiteLLM allows you to view your vector store usage in the LiteLLM UI on the `Logs` page.

After completing a request with a vector store, navigate to the `Logs` page on LiteLLM. Here you should be able to see the query sent to the vector store and corresponding response with scores.

LiteLLM Logs Page: Vector Store Usage

### Listing available vector stores[​](#listing-available-vector-stores "Direct link to Listing available vector stores")

You can list all available vector stores using the /vector\_store/list endpoint

**Request:**

List all available vector stores

```
curl -X GET "http://localhost:4000/vector_store/list" \
  -H "Authorization: Bearer $LITELLM_API_KEY"
```

**Response:**

The response will be a list of all vector stores that are available to use with LiteLLM.

```
{
"object":"list",
"data":[
{
"vector_store_id":"T37J8R4WTM",
"custom_llm_provider":"bedrock",
"vector_store_name":"bedrock-litellm-website-knowledgebase",
"vector_store_description":"Bedrock vector store for the Litellm website knowledgebase",
"vector_store_metadata":{
"source":"https://www.litellm.com/docs"
},
"created_at":"2023-05-03T18:21:36.462Z",
"updated_at":"2023-05-03T18:21:36.462Z",
"litellm_credential_name":"bedrock_credentials"
}
],
"total_count":1,
"current_page":1,
"total_pages":1
}
```

### Always on for a model[​](#always-on-for-a-model "Direct link to Always on for a model")

**Use this if you want vector stores to be used by default for a specific model.**

In this config, we add `vector_store_ids` to the claude-3-5-sonnet-with-vector-store model. This means that any request to the claude-3-5-sonnet-with-vector-store model will always use the vector store with the id `T37J8R4WTM` defined in the `vector_store_registry`.

Always on for a model

```
model_list:
-model_name: claude-3-5-sonnet-with-vector-store
litellm_params:
model: anthropic/claude-3-5-sonnet
vector_store_ids:["T37J8R4WTM"]

vector_store_registry:
-vector_store_name:"bedrock-litellm-website-knowledgebase"
litellm_params:
vector_store_id:"T37J8R4WTM"
custom_llm_provider:"bedrock"
vector_store_description:"Bedrock vector store for the Litellm website knowledgebase"
vector_store_metadata:
source:"https://www.litellm.com/docs"
```

## How It Works[​](#how-it-works "Direct link to How It Works")

If your request includes a `vector_store_ids` parameter where any of the vector store ids are found in the `vector_store_registry`, LiteLLM will automatically use the vector store for the request.

1. You make a completion request with the `vector_store_ids` parameter and any of the vector store ids are found in the `litellm.vector_store_registry`
2. LiteLLM automatically:
   
   - Uses your last message as the query to retrieve relevant information from the Knowledge Base
   - Adds the retrieved context to your conversation
   - Sends the augmented messages to the model

#### Example Transformation[​](#example-transformation "Direct link to Example Transformation")

When you pass `vector_store_ids=["YOUR_KNOWLEDGE_BASE_ID"]`, your request flows through these steps:

**1. Original Request to LiteLLM:**

```
{
"model":"anthropic/claude-3-5-sonnet",
"messages":[
{"role":"user","content":"What is litellm?"}
],
"vector_store_ids":["YOUR_KNOWLEDGE_BASE_ID"]
}
```

**2. Request to AWS Bedrock Knowledge Base:**

```
{
"retrievalQuery":{
"text":"What is litellm?"
}
}
```

This is sent to: `https://bedrock-agent-runtime.{aws_region}.amazonaws.com/knowledgebases/YOUR_KNOWLEDGE_BASE_ID/retrieve`

**3. Final Request to LiteLLM:**

```
{
"model":"anthropic/claude-3-5-sonnet",
"messages":[
{"role":"user","content":"What is litellm?"},
{"role":"user","content":"Context: \n\nLiteLLM is an open-source SDK to simplify LLM API calls across providers (OpenAI, Claude, etc). It provides a standardized interface with robust error handling, streaming, and observability tools."}
]
}
```

This process happens automatically whenever you include the `vector_store_ids` parameter in your request.

## Accessing Search Results (Citations)[​](#accessing-search-results-citations "Direct link to Accessing Search Results (Citations)")

When using vector stores, LiteLLM automatically returns search results in `provider_specific_fields`. This allows you to show users citations for the AI's response.

### Key Concept[​](#key-concept "Direct link to Key Concept")

Search results are always in: `response.choices[0].message.provider_specific_fields["search_results"]`

For streaming: Results appear in the **final chunk** when `finish_reason == "stop"`

### Non-Streaming Example[​](#non-streaming-example "Direct link to Non-Streaming Example")

**Non-Streaming Response with search results:**

```
{
"id":"chatcmpl-abc123",
"choices":[{
"index":0,
"message":{
"role":"assistant",
"content":"LiteLLM is a platform...",
"provider_specific_fields":{
"search_results":[{
"search_query":"What is litellm?",
"data":[{
"score":0.95,
"content":[{"text":"...","type":"text"}],
"filename":"litellm-docs.md",
"file_id":"doc-123"
}]
}]
}
},
"finish_reason":"stop"
}]
}
```

- Python SDK
- TypeScript SDK

```
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:4000",
    api_key="your-litellm-api-key"
)

response = client.chat.completions.create(
    model="claude-3-5-sonnet",
    messages=[{"role":"user","content":"What is litellm?"}],
    tools=[{"type":"file_search","vector_store_ids":["T37J8R4WTM"]}]
)

# Get AI response
print(response.choices[0].message.content)

# Get search results (citations)
search_results = response.choices[0].message.provider_specific_fields.get("search_results",[])

for result_page in search_results:
for idx, item inenumerate(result_page['data'],1):
print(f"[{idx}] {item.get('filename','Unknown')} (score: {item['score']:.2f})")
```

### Streaming Example[​](#streaming-example "Direct link to Streaming Example")

**Streaming Response with search results (final chunk):**

```
{
"id":"chatcmpl-abc123",
"choices":[{
"index":0,
"delta":{
"provider_specific_fields":{
"search_results":[{
"search_query":"What is litellm?",
"data":[{
"score":0.95,
"content":[{"text":"...","type":"text"}],
"filename":"litellm-docs.md",
"file_id":"doc-123"
}]
}]
}
},
"finish_reason":"stop"
}]
}
```

- Python SDK
- TypeScript SDK

```
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:4000",
    api_key="your-litellm-api-key"
)

stream = client.chat.completions.create(
    model="claude-3-5-sonnet",
    messages=[{"role":"user","content":"What is litellm?"}],
    tools=[{"type":"file_search","vector_store_ids":["T37J8R4WTM"]}],
    stream=True
)

for chunk in stream:
# Stream content
if chunk.choices[0].delta.content:
print(chunk.choices[0].delta.content, end="", flush=True)

# Get citations in final chunk
if chunk.choices[0].finish_reason =="stop":
        search_results =getattr(chunk.choices[0].delta,'provider_specific_fields',{}).get('search_results',[])
if search_results:
print("\n\nSources:")
for page in search_results:
for idx, item inenumerate(page['data'],1):
print(f"  [{idx}] {item.get('filename','Unknown')} ({item['score']:.2f})")
```

### Search Result Fields[​](#search-result-fields "Direct link to Search Result Fields")

FieldTypeDescription`search_query`stringThe query used to search the vector store`data`arrayArray of search results`data[].score`floatRelevance score (0-1, higher is more relevant)`data[].content`arrayContent chunks with `text` and `type``data[].filename`stringName of the source file (optional)`data[].file_id`stringIdentifier for the source file (optional)`data[].attributes`objectProvider-specific metadata (optional)

## API Reference[​](#api-reference "Direct link to API Reference")

### LiteLLM Completion Knowledge Base Parameters[​](#litellm-completion-knowledge-base-parameters "Direct link to LiteLLM Completion Knowledge Base Parameters")

When using the Knowledge Base integration with LiteLLM, you can include the following parameters:

ParameterTypeDescription`vector_store_ids`List\[str]List of Knowledge Base IDs to query

### VectorStoreRegistry[​](#vectorstoreregistry "Direct link to VectorStoreRegistry")

The `VectorStoreRegistry` is a central component for managing vector stores in LiteLLM. It acts as a registry where you can configure and access your vector stores.

#### What is VectorStoreRegistry?[​](#what-is-vectorstoreregistry "Direct link to What is VectorStoreRegistry?")

`VectorStoreRegistry` is a class that:

- Maintains a collection of vector stores that LiteLLM can use
- Allows you to register vector stores with their credentials and metadata
- Makes vector stores accessible via their IDs in your completion requests

#### Using VectorStoreRegistry in Python[​](#using-vectorstoreregistry-in-python "Direct link to Using VectorStoreRegistry in Python")

```
from litellm.vector_stores.vector_store_registry import VectorStoreRegistry, LiteLLM_ManagedVectorStore

# Initialize the vector store registry with one or more vector stores
litellm.vector_store_registry = VectorStoreRegistry(
    vector_stores=[
        LiteLLM_ManagedVectorStore(
            vector_store_id="YOUR_VECTOR_STORE_ID",# Required: Unique ID for referencing this store
            custom_llm_provider="bedrock"# Required: Provider (e.g., "bedrock")
)
]
)
```

#### LiteLLM\_ManagedVectorStore Parameters[​](#litellm_managedvectorstore-parameters "Direct link to LiteLLM_ManagedVectorStore Parameters")

Each vector store in the registry is configured using a `LiteLLM_ManagedVectorStore` object with these parameters:

ParameterTypeRequiredDescription`vector_store_id`strYesUnique identifier for the vector store`custom_llm_provider`strYesThe provider of the vector store (e.g., "bedrock")`vector_store_name`strNoA friendly name for the vector store`vector_store_description`strNoDescription of what the vector store contains`vector_store_metadata`dict or strNoAdditional metadata about the vector store`litellm_credential_name`strNoName of the credentials to use for this vector store

#### Configuring VectorStoreRegistry in config.yaml[​](#configuring-vectorstoreregistry-in-configyaml "Direct link to Configuring VectorStoreRegistry in config.yaml")

For the LiteLLM Proxy, you can configure the same registry in your `config.yaml` file:

Vector store configuration in config.yaml

```
vector_store_registry:
-vector_store_name:"bedrock-litellm-website-knowledgebase"# Optional friendly name
litellm_params:
vector_store_id:"T37J8R4WTM"# Required: Unique ID  
custom_llm_provider:"bedrock"# Required: Provider
vector_store_description:"Bedrock vector store for the Litellm website knowledgebase"
vector_store_metadata:
source:"https://www.litellm.com/docs"
```

The `litellm_params` section accepts all the same parameters as the `LiteLLM_ManagedVectorStore` constructor in the Python SDK.