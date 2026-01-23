---
title: /batches | liteLLM
url: https://docs.litellm.ai/docs/batches
source: sitemap
fetched_at: 2026-01-21T19:44:06.735384508-03:00
rendered_js: false
word_count: 411
summary: This document explains how to manage batch completions and file uploads using LiteLLM, including support for multi-account model-based routing and automated credential handling.
tags:
    - batch-processing
    - file-management
    - model-routing
    - multi-account
    - litellm-proxy
    - api-integration
category: guide
---

Covers Batches, Files

FeatureSupportedNotesSupported ProvidersOpenAI, Azure, Vertex, Bedrock, vLLM-✨ Cost Tracking✅LiteLLM Enterprise onlyLogging✅Works across all logging integrations

## Quick Start[​](#quick-start "Direct link to Quick Start")

- Create File for Batch Completion
- Create Batch Request
- List Batches
- Retrieve the Specific Batch and File Content

<!--THE END-->

- LiteLLM PROXY Server
- SDK

```
$ export OPENAI_API_KEY="sk-..."

$ litellm

# RUNNING on http://0.0.0.0:4000
```

**Create File for Batch Completion**

```
curl http://localhost:4000/v1/files \
    -H "Authorization: Bearer sk-1234" \
    -F purpose="batch" \
    -F file="@mydata.jsonl"
```

**Create Batch Request**

```
curl http://localhost:4000/v1/batches \
        -H "Authorization: Bearer sk-1234" \
        -H "Content-Type: application/json" \
        -d '{
            "input_file_id": "file-abc123",
            "endpoint": "/v1/chat/completions",
            "completion_window": "24h"
    }'
```

**Retrieve the Specific Batch**

```
curl http://localhost:4000/v1/batches/batch_abc123 \
    -H "Authorization: Bearer sk-1234" \
    -H "Content-Type: application/json" \
```

**List Batches**

```
curl http://localhost:4000/v1/batches \
    -H "Authorization: Bearer sk-1234" \
    -H "Content-Type: application/json" \
```

## Multi-Account / Model-Based Routing[​](#multi-account--model-based-routing "Direct link to Multi-Account / Model-Based Routing")

Route batch operations to different provider accounts using model-specific credentials from your `config.yaml`. This eliminates the need for environment variables and enables multi-tenant batch processing.

### How It Works[​](#how-it-works "Direct link to How It Works")

**Priority Order:**

1. **Encoded Batch/File ID** (highest) - Model info embedded in the ID
2. **Model Parameter** - Via header (`x-litellm-model`), query param, or request body
3. **Custom Provider** (fallback) - Uses environment variables

### Configuration[​](#configuration "Direct link to Configuration")

```
model_list:
-model_name: gpt-4o-account-1
litellm_params:
model: openai/gpt-4o
api_key: sk-account-1-key
api_base: https://api.openai.com/v1

-model_name: gpt-4o-account-2
litellm_params:
model: openai/gpt-4o
api_key: sk-account-2-key
api_base: https://api.openai.com/v1

-model_name: azure-batches
litellm_params:
model: azure/gpt-4
api_key: azure-key-123
api_base: https://my-resource.openai.azure.com
api_version:"2024-02-01"
```

### Usage Examples[​](#usage-examples "Direct link to Usage Examples")

#### Scenario 1: Encoded File ID with Model[​](#scenario-1-encoded-file-id-with-model "Direct link to Scenario 1: Encoded File ID with Model")

When you upload a file with a model parameter, LiteLLM encodes the model information in the file ID. All subsequent operations automatically use those credentials.

```
# Step 1: Upload file with model
curl http://localhost:4000/v1/files \
  -H "Authorization: Bearer sk-1234" \
  -H "x-litellm-model: gpt-4o-account-1" \
  -F purpose="batch" \
  -F file="@batch.jsonl"

# Response includes encoded file ID:
# {
#   "id": "file-bGl0ZWxsbTpmaWxlLUxkaUwzaVYxNGZRVlpYcU5KVEdkSjk7bW9kZWwsZ3B0LTRvLWFjY291bnQtMQ",
#   ...
# }

# Step 2: Create batch - automatically routes to gpt-4o-account-1
curl http://localhost:4000/v1/batches \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "input_file_id": "file-bGl0ZWxsbTpmaWxlLUxkaUwzaVYxNGZRVlpYcU5KVEdkSjk7bW9kZWwsZ3B0LTRvLWFjY291bnQtMQ",
    "endpoint": "/v1/chat/completions",
    "completion_window": "24h"
  }'

# Batch ID is also encoded with model:
# {
#   "id": "batch_bGl0ZWxsbTpiYXRjaF82OTIwM2IzNjg0MDQ4MTkwYTA3ODQ5NDY3YTFjMDJkYTttb2RlbCxncHQtNG8tYWNjb3VudC0x",
#   "input_file_id": "file-bGl0ZWxsbTpmaWxlLUxkaUwzaVYxNGZRVlpYcU5KVEdkSjk7bW9kZWwsZ3B0LTRvLWFjY291bnQtMQ",
#   ...
# }

# Step 3: Retrieve batch - automatically routes to gpt-4o-account-1
curl http://localhost:4000/v1/batches/batch_bGl0ZWxsbTpiYXRjaF82OTIwM2IzNjg0MDQ4MTkwYTA3ODQ5NDY3YTFjMDJkYTttb2RlbCxncHQtNG8tYWNjb3VudC0x \
  -H "Authorization: Bearer sk-1234"
```

**✅ Benefits:**

- No need to specify model on every request
- File and batch IDs "remember" which account created them
- Automatic routing for retrieve, cancel, and file content operations

Specify the model for each request without encoding it in the ID.

```
# Create batch with model header
curl http://localhost:4000/v1/batches \
  -H "Authorization: Bearer sk-1234" \
  -H "x-litellm-model: gpt-4o-account-2" \
  -H "Content-Type: application/json" \
  -d '{
    "input_file_id": "file-abc123",
    "endpoint": "/v1/chat/completions",
    "completion_window": "24h"
  }'

# Or use query parameter
curl "http://localhost:4000/v1/batches?model=gpt-4o-account-2" \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "input_file_id": "file-abc123",
    "endpoint": "/v1/chat/completions",
    "completion_window": "24h"
  }'

# List batches for specific model
curl "http://localhost:4000/v1/batches?model=gpt-4o-account-2" \
  -H "Authorization: Bearer sk-1234"
```

**✅ Use Case:**

- One-off batch operations
- Different models for different operations
- Explicit control over routing

#### Scenario 3: Environment Variables (Fallback)[​](#scenario-3-environment-variables-fallback "Direct link to Scenario 3: Environment Variables (Fallback)")

Traditional approach using environment variables when no model is specified.

```
export OPENAI_API_KEY="sk-env-key"

curl http://localhost:4000/v1/batches \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "input_file_id": "file-abc123",
    "endpoint": "/v1/chat/completions",
    "completion_window": "24h"
  }'
```

**✅ Use Case:**

- Backward compatibility
- Simple single-account setups
- Quick prototyping

### Complete Multi-Account Example[​](#complete-multi-account-example "Direct link to Complete Multi-Account Example")

```
# Upload file to Account 1
FILE_1=$(curl -s http://localhost:4000/v1/files \
  -H "x-litellm-model: gpt-4o-account-1" \
  -F purpose="batch" \
  -F file="@batch1.jsonl" | jq -r '.id')

# Upload file to Account 2
FILE_2=$(curl -s http://localhost:4000/v1/files \
  -H "x-litellm-model: gpt-4o-account-2" \
  -F purpose="batch" \
  -F file="@batch2.jsonl" | jq -r '.id')

# Create batch on Account 1 (auto-routed via encoded file ID)
BATCH_1=$(curl -s http://localhost:4000/v1/batches \
  -d "{\"input_file_id\": \"$FILE_1\", \"endpoint\": \"/v1/chat/completions\", \"completion_window\": \"24h\"}" | jq -r '.id')

# Create batch on Account 2 (auto-routed via encoded file ID)
BATCH_2=$(curl -s http://localhost:4000/v1/batches \
  -d "{\"input_file_id\": \"$FILE_2\", \"endpoint\": \"/v1/chat/completions\", \"completion_window\": \"24h\"}" | jq -r '.id')

# Retrieve both batches (auto-routed to correct accounts)
curl http://localhost:4000/v1/batches/$BATCH_1
curl http://localhost:4000/v1/batches/$BATCH_2

# List batches per account
curl "http://localhost:4000/v1/batches?model=gpt-4o-account-1"
curl "http://localhost:4000/v1/batches?model=gpt-4o-account-2"
```

### SDK Usage with Model Routing[​](#sdk-usage-with-model-routing "Direct link to SDK Usage with Model Routing")

```
import litellm
import asyncio

# Upload file with model routing
file_obj =await litellm.acreate_file(
file=open("batch.jsonl","rb"),
    purpose="batch",
    model="gpt-4o-account-1",# Route to specific account
)

print(f"File ID: {file_obj.id}")
# File ID is encoded with model info

# Create batch - automatically uses gpt-4o-account-1 credentials
batch =await litellm.acreate_batch(
    completion_window="24h",
    endpoint="/v1/chat/completions",
    input_file_id=file_obj.id,# Model info embedded in ID
)

print(f"Batch ID: {batch.id}")
# Batch ID is also encoded

# Retrieve batch - automatically routes to correct account
retrieved =await litellm.aretrieve_batch(
    batch_id=batch.id,# Model info embedded in ID
)

print(f"Batch status: {retrieved.status}")

# Or explicitly specify model
batch2 =await litellm.acreate_batch(
    completion_window="24h",
    endpoint="/v1/chat/completions",
    input_file_id="file-regular-id",
    model="gpt-4o-account-2",# Explicit routing
)
```

### How ID Encoding Works[​](#how-id-encoding-works "Direct link to How ID Encoding Works")

LiteLLM encodes model information into file and batch IDs using base64:

```
Original:  file-abc123
Encoded:   file-bGl0ZWxsbTpmaWxlLWFiYzEyMzttb2RlbCxncHQtNG8tdGVzdA
           └─┬─┘ └──────────────────┬──────────────────────┘
          prefix      base64(litellm:file-abc123;model,gpt-4o-test)

Original:  batch_xyz789
Encoded:   batch_bGl0ZWxsbTpiYXRjaF94eXo3ODk7bW9kZWwsZ3B0LTRvLXRlc3Q
           └──┬──┘ └──────────────────┬──────────────────────┘
           prefix       base64(litellm:batch_xyz789;model,gpt-4o-test)
```

The encoding:

- ✅ Preserves OpenAI-compatible prefixes (`file-`, `batch_`)
- ✅ Is transparent to clients
- ✅ Enables automatic routing without additional parameters
- ✅ Works across all batch and file endpoints

### Supported Endpoints[​](#supported-endpoints "Direct link to Supported Endpoints")

All batch and file endpoints support model-based routing:

EndpointMethodModel Routing`/v1/files`POST✅ Via header/query/body`/v1/files/{file_id}`GET✅ Auto from encoded ID + header/query`/v1/files/{file_id}/content`GET✅ Auto from encoded ID + header/query`/v1/files/{file_id}`DELETE✅ Auto from encoded ID`/v1/batches`POST✅ Auto from file ID + header/query/body`/v1/batches`GET✅ Via header/query`/v1/batches/{batch_id}`GET✅ Auto from encoded ID`/v1/batches/{batch_id}/cancel`POST✅ Auto from encoded ID

## **Supported Providers**:[​](#supported-providers "Direct link to supported-providers")

### [Azure OpenAI](https://docs.litellm.ai/docs/providers/azure#azure-batches-api)[​](#azure-openai "Direct link to azure-openai")

### [OpenAI](#quick-start)[​](#openai "Direct link to openai")

### [Vertex AI](https://docs.litellm.ai/docs/providers/vertex#batch-apis)[​](#vertex-ai "Direct link to vertex-ai")

### [Bedrock](https://docs.litellm.ai/docs/providers/bedrock_batches)[​](#bedrock "Direct link to bedrock")

### [vLLM](https://docs.litellm.ai/docs/providers/vllm_batches)[​](#vllm "Direct link to vllm")

## How Cost Tracking for Batches API Works[​](#how-cost-tracking-for-batches-api-works "Direct link to How Cost Tracking for Batches API Works")

LiteLLM tracks batch processing costs by logging two key events:

Event TypeDescriptionWhen it's Logged`acreate_batch`Initial batch creationWhen batch request is submitted`batch_success`Final usage and costWhen batch processing completes

Cost calculation:

- LiteLLM polls the batch status until completion
- Upon completion, it aggregates usage and costs from all responses in the output file
- Total `token` and `response_cost` reflect the combined metrics across all batch responses

## [Swagger API Reference](https://litellm-api.up.railway.app/#/batch)[​](#swagger-api-reference "Direct link to swagger-api-reference")