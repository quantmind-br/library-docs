---
title: /converse | liteLLM
url: https://docs.litellm.ai/docs/bedrock_converse
source: sitemap
fetched_at: 2026-01-21T19:44:09.450223429-03:00
rendered_js: false
word_count: 73
summary: This document explains how to configure and use the LiteLLM Proxy to access Amazon Bedrock's converse and converse-stream endpoints, including instructions for load balancing and SDK integration.
tags:
    - litellm
    - amazon-bedrock
    - api-proxy
    - load-balancing
    - streaming-api
    - boto3
    - aws-credentials
category: guide
---

Call Bedrock's `/converse` endpoint through LiteLLM Proxy.

FeatureSupportedCost Tracking✅Logging✅Streaming✅ via `/converse-stream`Load Balancing✅

## Quick Start[​](#quick-start "Direct link to Quick Start")

### 1. Setup config.yaml[​](#1-setup-configyaml "Direct link to 1. Setup config.yaml")

```
model_list:
-model_name: my-bedrock-model
litellm_params:
model: bedrock/us.anthropic.claude-3-5-sonnet-20240620-v1:0
aws_region_name: us-west-2
aws_access_key_id: os.environ/AWS_ACCESS_KEY_ID  # reads from environment
aws_secret_access_key: os.environ/AWS_SECRET_ACCESS_KEY
custom_llm_provider: bedrock
```

Set AWS credentials in your environment:

```
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
```

### 2. Start Proxy[​](#2-start-proxy "Direct link to 2. Start Proxy")

```
litellm --config config.yaml

# RUNNING on http://0.0.0.0:4000
```

### 3. Call /converse endpoint[​](#3-call-converse-endpoint "Direct link to 3. Call /converse endpoint")

```
curl -X POST 'http://0.0.0.0:4000/bedrock/model/my-bedrock-model/converse' \
-H 'Authorization: Bearer sk-1234' \
-H 'Content-Type: application/json' \
-d '{
    "messages": [
        {
            "role": "user",
            "content": [{"text": "Hello, how are you?"}]
        }
    ],
    "inferenceConfig": {
        "temperature": 0.5,
        "maxTokens": 100
    }
}'
```

## Streaming[​](#streaming "Direct link to Streaming")

For streaming responses, use `/converse-stream`:

```
curl -X POST 'http://0.0.0.0:4000/bedrock/model/my-bedrock-model/converse-stream' \
-H 'Authorization: Bearer sk-1234' \
-H 'Content-Type: application/json' \
-d '{
    "messages": [
        {
            "role": "user",
            "content": [{"text": "Tell me a short story"}]
        }
    ],
    "inferenceConfig": {
        "temperature": 0.7,
        "maxTokens": 200
    }
}'
```

## Load Balancing[​](#load-balancing "Direct link to Load Balancing")

Define multiple deployments with the same `model_name` for automatic load balancing:

```
model_list:
# Deployment 1 - us-west-2
-model_name: my-bedrock-model
litellm_params:
model: bedrock/us.anthropic.claude-3-5-sonnet-20240620-v1:0
aws_region_name: us-west-2
aws_access_key_id: os.environ/AWS_ACCESS_KEY_ID
aws_secret_access_key: os.environ/AWS_SECRET_ACCESS_KEY
custom_llm_provider: bedrock

# Deployment 2 - us-east-1
-model_name: my-bedrock-model
litellm_params:
model: bedrock/us.anthropic.claude-3-5-sonnet-20240620-v1:0
aws_region_name: us-east-1
aws_access_key_id: os.environ/AWS_ACCESS_KEY_ID
aws_secret_access_key: os.environ/AWS_SECRET_ACCESS_KEY
custom_llm_provider: bedrock
```

The proxy automatically distributes requests across both regions.

## Using boto3 SDK[​](#using-boto3-sdk "Direct link to Using boto3 SDK")

```
import boto3
import json
import os

# Set dummy AWS credentials (required by boto3, but not used by LiteLLM proxy)
os.environ['AWS_ACCESS_KEY_ID']='dummy'
os.environ['AWS_SECRET_ACCESS_KEY']='dummy'
os.environ['AWS_BEARER_TOKEN_BEDROCK']="sk-1234"# your litellm proxy api key

# Point boto3 to the LiteLLM proxy
bedrock_runtime = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-west-2',
    endpoint_url='http://0.0.0.0:4000/bedrock'
)

response = bedrock_runtime.converse(
    modelId='my-bedrock-model',# Your model_name from config.yaml
    messages=[
{
"role":"user",
"content":[{"text":"Hello, how are you?"}]
}
],
    inferenceConfig={
"temperature":0.5,
"maxTokens":100
}
)

print(response['output']['message']['content'][0]['text'])
```

## More Info[​](#more-info "Direct link to More Info")

For complete documentation including Guardrails, Knowledge Bases, and Agents, see:

- [Full Bedrock Passthrough Docs](https://docs.litellm.ai/docs/pass_through/bedrock)