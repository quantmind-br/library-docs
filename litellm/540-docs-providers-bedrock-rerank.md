---
title: AWS Bedrock - Rerank API | liteLLM
url: https://docs.litellm.ai/docs/providers/bedrock_rerank
source: sitemap
fetched_at: 2026-01-21T19:48:31.257380315-03:00
rendered_js: false
word_count: 70
summary: This document explains how to integrate and use the Bedrock Rerank API through LiteLLM using a Cohere-style interface. It details supported parameters, authentication procedures, and cost tracking while providing a practical Python code sample.
tags:
    - bedrock
    - rerank-api
    - litellm
    - aws-bedrock
    - python-sdk
    - search-ranking
category: api
---

Use Bedrock's Rerank API in the Cohere `/rerank` format.

Cost Tracking

✅ **Cost tracking is supported** for Bedrock Rerank API calls.

## Supported Parameters[​](#supported-parameters "Direct link to Supported Parameters")

- `model` - the foundation model ARN
- `query` - the query to rerank against
- `documents` - the list of documents to rerank
- `top_n` - the number of results to return

## Usage[​](#usage "Direct link to Usage")

- SDK
- PROXY

```
from litellm import rerank
import os 

os.environ["AWS_ACCESS_KEY_ID"]=""
os.environ["AWS_SECRET_ACCESS_KEY"]=""
os.environ["AWS_REGION_NAME"]=""

response = rerank(
    model="bedrock/arn:aws:bedrock:us-west-2::foundation-model/amazon.rerank-v1:0",# provide the model ARN - get this here https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/list_foundation_models.html
    query="hello",
    documents=["hello","world"],
    top_n=2,
)

print(response)
```

## Authentication[​](#authentication "Direct link to Authentication")

All standard Bedrock authentication methods are supported for rerank. See [Bedrock Authentication](https://docs.litellm.ai/docs/providers/bedrock#boto3---authentication) for details.