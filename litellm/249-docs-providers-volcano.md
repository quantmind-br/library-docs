---
title: Volcano Engine (Volcengine) | liteLLM
url: https://docs.litellm.ai/docs/providers/volcano
source: sitemap
fetched_at: 2026-01-21T19:50:54.012232836-03:00
rendered_js: false
word_count: 106
summary: This document provides instructions and code samples for integrating Volcengine (Doubao) chat and embedding models into LiteLLM, including API key setup and proxy configuration.
tags:
    - volcengine
    - litellm
    - python-sdk
    - llm-api
    - embeddings
    - chat-completion
    - proxy-configuration
category: guide
---

[https://www.volcengine.com/docs/82379/1263482](https://www.volcengine.com/docs/82379/1263482)

tip

**We support ALL Volcengine models including Chat and Embeddings, just set `model=volcengine/<any-model-on-volcengine>` as a prefix when sending litellm requests**

## API Key[​](#api-key "Direct link to API Key")

```
# env variable
os.environ['VOLCENGINE_API_KEY']
# or
os.environ['ARK_API_KEY']
```

## Sample Usage[​](#sample-usage "Direct link to Sample Usage")

```
from litellm import completion
import os

os.environ['VOLCENGINE_API_KEY']=""
response = completion(
    model="volcengine/<OUR_ENDPOINT_ID>",
    messages=[
{
"role":"user",
"content":"What's the weather like in Boston today in Fahrenheit?",
}
],
    temperature=0.2,# optional
    top_p=0.9,# optional
    frequency_penalty=0.1,# optional
    presence_penalty=0.1,# optional
    max_tokens=10,# optional
    stop=["\n\n"],# optional
)
print(response)
```

## Sample Usage - Streaming[​](#sample-usage---streaming "Direct link to Sample Usage - Streaming")

```
from litellm import completion
import os

os.environ['VOLCENGINE_API_KEY']=""
response = completion(
    model="volcengine/<OUR_ENDPOINT_ID>",
    messages=[
{
"role":"user",
"content":"What's the weather like in Boston today in Fahrenheit?",
}
],
    stream=True,
    temperature=0.2,# optional
    top_p=0.9,# optional
    frequency_penalty=0.1,# optional
    presence_penalty=0.1,# optional
    max_tokens=10,# optional
    stop=["\n\n"],# optional
)

for chunk in response:
print(chunk)
```

## Sample Usage - Embedding[​](#sample-usage---embedding "Direct link to Sample Usage - Embedding")

```
from litellm import embedding
import os

os.environ['VOLCENGINE_API_KEY']=""
response = embedding(
    model="volcengine/doubao-embedding-text-240715",
input=["hello world","good morning"]
)
print(response)
```

### Supported Embedding Models[​](#supported-embedding-models "Direct link to Supported Embedding Models")

- `doubao-embedding-large` (2048 dimensions)
- `doubao-embedding-large-text-250515` (2048 dimensions)
- `doubao-embedding-large-text-240915` (4096 dimensions)
- `doubao-embedding` (2560 dimensions)
- `doubao-embedding-text-240715` (2560 dimensions)

### Embedding Parameters[​](#embedding-parameters "Direct link to Embedding Parameters")

```
from litellm import embedding

response = embedding(
    model="volcengine/doubao-embedding-text-240715",
input=["sample text"],
    encoding_format="float",# optional: "float" (default), "base64"
    user="user-123",# optional: user identifier for tracking
)
```

## Supported Models - 💥 ALL Volcengine Models Supported\![​](#supported-models----all-volcengine-models-supported "Direct link to Supported Models - 💥 ALL Volcengine Models Supported!")

We support ALL `volcengine` models for both chat completions and embeddings:

- **Chat Models**: Set `volcengine/<OUR_ENDPOINT_ID>` as a prefix when sending completion requests
- **Embedding Models**: Use the specific model names listed above (e.g., `volcengine/doubao-embedding-text-240715`)

## Sample Usage - LiteLLM Proxy[​](#sample-usage---litellm-proxy "Direct link to Sample Usage - LiteLLM Proxy")

### Config.yaml setting[​](#configyaml-setting "Direct link to Config.yaml setting")

```
model_list:
# Chat model
-model_name: volcengine-model
litellm_params:
model: volcengine/<OUR_ENDPOINT_ID>
api_key: os.environ/VOLCENGINE_API_KEY
# Embedding model
-model_name: volcengine-embedding
litellm_params:
model: volcengine/doubao-embedding-text-240715
api_key: os.environ/VOLCENGINE_API_KEY
```

### Send Request[​](#send-request "Direct link to Send Request")

#### Chat Completion[​](#chat-completion "Direct link to Chat Completion")

```
curl --location 'http://localhost:4000/chat/completions' \
    --header 'Authorization: Bearer sk-1234' \
    --header 'Content-Type: application/json' \
    --data '{
    "model": "volcengine-model",
    "messages": [
        {
        "role": "user",
        "content": "here is my api key. openai_api_key=sk-1234"
        }
    ]
}'
```

#### Embedding[​](#embedding "Direct link to Embedding")

```
curl --location 'http://localhost:4000/embeddings' \
    --header 'Authorization: Bearer sk-1234' \
    --header 'Content-Type: application/json' \
    --data '{
    "model": "volcengine-embedding",
    "input": ["hello world", "good morning"]
}'
```