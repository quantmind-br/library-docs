---
title: Vertex AI Embedding | liteLLM
url: https://docs.litellm.ai/docs/providers/vertex_embedding
source: sitemap
fetched_at: 2026-01-21T19:50:43.918774564-03:00
rendered_js: false
word_count: 187
summary: This document provides a technical reference for using LiteLLM to interface with Vertex AI embedding models, including text, BGE, and multi-modal types. It details supported model IDs, parameter mappings for OpenAI compatibility, and configuration steps for both the SDK and LiteLLM Proxy.
tags:
    - litellm
    - vertex-ai
    - embeddings
    - multi-modal
    - google-cloud
    - python-sdk
    - bge-embeddings
category: reference
---

## Usage - Embedding[​](#usage---embedding "Direct link to Usage - Embedding")

- SDK
- LiteLLM PROXY

```
import litellm
from litellm import embedding
litellm.vertex_project ="hardy-device-38811"# Your Project ID
litellm.vertex_location ="us-central1"# proj location

response = embedding(
    model="vertex_ai/textembedding-gecko",
input=["good morning from litellm"],
)
print(response)
```

#### Supported Embedding Models[​](#supported-embedding-models "Direct link to Supported Embedding Models")

All models listed [here](https://github.com/BerriAI/litellm/blob/57f37f743886a0249f630a6792d49dffc2c5d9b7/model_prices_and_context_window.json#L835) are supported

Model NameFunction Calltext-embedding-004`embedding(model="vertex_ai/text-embedding-004", input)`text-multilingual-embedding-002`embedding(model="vertex_ai/text-multilingual-embedding-002", input)`textembedding-gecko`embedding(model="vertex_ai/textembedding-gecko", input)`textembedding-gecko-multilingual`embedding(model="vertex_ai/textembedding-gecko-multilingual", input)`textembedding-gecko-multilingual@001`embedding(model="vertex_ai/textembedding-gecko-multilingual@001", input)`textembedding-gecko@001`embedding(model="vertex_ai/textembedding-gecko@001", input)`textembedding-gecko@003`embedding(model="vertex_ai/textembedding-gecko@003", input)`text-embedding-preview-0409`embedding(model="vertex_ai/text-embedding-preview-0409", input)`text-multilingual-embedding-preview-0409`embedding(model="vertex_ai/text-multilingual-embedding-preview-0409", input)`Fine-tuned OR Custom Embedding models`embedding(model="vertex_ai/<your-model-id>", input)`

### Supported OpenAI (Unified) Params[​](#supported-openai-unified-params "Direct link to Supported OpenAI (Unified) Params")

[param](https://docs.litellm.ai/docs/embedding/supported_embedding#input-params-for-litellmembedding)type[vertex equivalent](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text-embeddings-api)`input`**string or List\[string]**`instances``dimensions`**int**`output_dimensionality``input_type`**Literal\["RETRIEVAL\_QUERY","RETRIEVAL\_DOCUMENT", "SEMANTIC\_SIMILARITY", "CLASSIFICATION", "CLUSTERING", "QUESTION\_ANSWERING", "FACT\_VERIFICATION"]**`task_type`

#### Usage with OpenAI (Unified) Params[​](#usage-with-openai-unified-params "Direct link to Usage with OpenAI (Unified) Params")

- SDK
- LiteLLM PROXY

```
response = litellm.embedding(
    model="vertex_ai/text-embedding-004",
input=["good morning from litellm","gm"]
    input_type ="RETRIEVAL_DOCUMENT",
    dimensions=1,
)
```

### Supported Vertex Specific Params[​](#supported-vertex-specific-params "Direct link to Supported Vertex Specific Params")

paramtype`auto_truncate`**bool**`task_type`**Literal\["RETRIEVAL\_QUERY","RETRIEVAL\_DOCUMENT", "SEMANTIC\_SIMILARITY", "CLASSIFICATION", "CLUSTERING", "QUESTION\_ANSWERING", "FACT\_VERIFICATION"]**`title`**str**

#### Usage with Vertex Specific Params (Use `task_type` and `title`)[​](#usage-with-vertex-specific-params--use-task_type-and-title "Direct link to usage-with-vertex-specific-params--use-task_type-and-title")

You can pass any vertex specific params to the embedding model. Just pass them to the embedding function like this:

[Relevant Vertex AI doc with all embedding params](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text-embeddings-api#request_body)

- SDK
- LiteLLM PROXY

```
response = litellm.embedding(
    model="vertex_ai/text-embedding-004",
input=["good morning from litellm","gm"]
    task_type ="RETRIEVAL_DOCUMENT",
    title ="test",
    dimensions=1,
    auto_truncate=True,
)
```

## **BGE Embeddings**[​](#bge-embeddings "Direct link to bge-embeddings")

Use BGE (Baidu General Embedding) models deployed on Vertex AI.

### Usage[​](#usage "Direct link to Usage")

- SDK
- LiteLLM PROXY

Using BGE on Vertex AI

```
import litellm

response = litellm.embedding(
    model="vertex_ai/bge/<your-endpoint-id>",
input=["Hello","World"],
    vertex_project="your-project-id",
    vertex_location="your-location"
)

print(response)
```

## **Multi-Modal Embeddings**[​](#multi-modal-embeddings "Direct link to multi-modal-embeddings")

Known Limitations:

- Only supports 1 image / video / image per request
- Only supports GCS or base64 encoded images / videos

### Usage[​](#usage-1 "Direct link to Usage")

- SDK
- LiteLLM PROXY (Unified Endpoint)
- LiteLLM PROXY (Vertex SDK)

Using GCS Images

```
response =await litellm.aembedding(
    model="vertex_ai/multimodalembedding@001",
input="gs://cloud-samples-data/vertex-ai/llm/prompts/landmark1.png"# will be sent as a gcs image
)
```

Using base 64 encoded images

```
response =await litellm.aembedding(
    model="vertex_ai/multimodalembedding@001",
input="data:image/jpeg;base64,..."# will be sent as a base64 encoded image
)
```

### Text + Image + Video Embeddings[​](#text--image--video-embeddings "Direct link to Text + Image + Video Embeddings")

- SDK
- LiteLLM PROXY (Unified Endpoint)

Text + Image

```
response =await litellm.aembedding(
    model="vertex_ai/multimodalembedding@001",
input=["hey","gs://cloud-samples-data/vertex-ai/llm/prompts/landmark1.png"]# will be sent as a gcs image
)
```

Text + Video

```
response =await litellm.aembedding(
    model="vertex_ai/multimodalembedding@001",
input=["hey","gs://my-bucket/embeddings/supermarket-video.mp4"]# will be sent as a gcs image
)
```

Image + Video

```
response =await litellm.aembedding(
    model="vertex_ai/multimodalembedding@001",
input=["gs://cloud-samples-data/vertex-ai/llm/prompts/landmark1.png","gs://my-bucket/embeddings/supermarket-video.mp4"]# will be sent as a gcs image
)
```