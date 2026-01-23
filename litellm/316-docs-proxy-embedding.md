---
title: Embeddings - /embeddings | liteLLM
url: https://docs.litellm.ai/docs/proxy/embedding
source: sitemap
fetched_at: 2026-01-21T19:51:53.055119947-03:00
rendered_js: false
word_count: 42
summary: Provides a quick-start guide for setting up the LiteLLM proxy to handle embedding requests for multiple models and cloud providers using a YAML configuration.
tags:
    - litellm
    - embedding-models
    - proxy-server
    - configuration
    - aws-bedrock
    - azure-openai
    - sagemaker
category: guide
---

See supported Embedding Providers & Models [here](https://docs.litellm.ai/docs/embedding/supported_embedding)

## Quick start[​](#quick-start "Direct link to Quick start")

Here's how to route between GPT-J embedding (sagemaker endpoint), Amazon Titan embedding (Bedrock) and Azure OpenAI embedding on the proxy server:

1. Set models in your config.yaml

```
model_list:
-model_name: sagemaker-embeddings
litellm_params:
model:"sagemaker/berri-benchmarking-gpt-j-6b-fp16"
-model_name: amazon-embeddings
litellm_params:
model:"bedrock/amazon.titan-embed-text-v1"
-model_name: azure-embeddings
litellm_params:
model:"azure/azure-embedding-model"
api_base:"os.environ/AZURE_API_BASE"# os.getenv("AZURE_API_BASE")
api_key:"os.environ/AZURE_API_KEY"# os.getenv("AZURE_API_KEY")
api_version:"2023-07-01-preview"

general_settings:
master_key: sk-1234# [OPTIONAL] if set all calls to proxy will require either this key or a valid generated token
```

2. Start the proxy

```
$ litellm --config /path/to/config.yaml
```

3. Test the embedding call

```
curl --location 'http://0.0.0.0:4000/v1/embeddings' \
--header 'Authorization: Bearer sk-1234' \
--header 'Content-Type: application/json' \
--data '{
    "input": "The food was delicious and the waiter..",
    "model": "sagemaker-embeddings",
}'
```