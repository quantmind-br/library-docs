---
title: Vertex AI - Self Deployed Models | liteLLM
url: https://docs.litellm.ai/docs/providers/vertex_self_deployed
source: sitemap
fetched_at: 2026-01-21T19:50:48.241730021-03:00
rendered_js: false
word_count: 142
summary: This document explains how to deploy and access models from Vertex AI Model Garden and custom endpoints using LiteLLM. It provides configuration details for both SDK and proxy usage, specifically for OpenAI-compatible models and Gemma-based custom deployments.
tags:
    - vertex-ai
    - google-cloud-platform
    - model-garden
    - litellm
    - gemma
    - custom-endpoints
    - api-integration
category: guide
---

Deploy and use your own models on Vertex AI through Model Garden or custom endpoints.

## Model Garden[​](#model-garden "Direct link to Model Garden")

tip

All OpenAI compatible models from Vertex Model Garden are supported.

### Using Model Garden[​](#using-model-garden "Direct link to Using Model Garden")

**Almost all Vertex Model Garden models are OpenAI compatible.**

- OpenAI Compatible Models
- Non-OpenAI Compatible Models

PropertyDetailsProvider Route`vertex_ai/openai/{MODEL_ID}`Vertex Documentation[Model Garden LiteLLM Inference](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/open-models/use-cases/model_garden_litellm_inference.ipynb), [Vertex Model Garden](https://cloud.google.com/model-garden?hl=en)Supported Operations`/chat/completions`, `/embeddings`

- SDK
- Proxy

```
from litellm import completion
import os

## set ENV variables
os.environ["VERTEXAI_PROJECT"]="hardy-device-38811"
os.environ["VERTEXAI_LOCATION"]="us-central1"

response = completion(
  model="vertex_ai/openai/<your-endpoint-id>",
  messages=[{"content":"Hello, how are you?","role":"user"}]
)
```

## Gemma Models (Custom Endpoints)[​](#gemma-models-custom-endpoints "Direct link to Gemma Models (Custom Endpoints)")

Deploy Gemma models on custom Vertex AI prediction endpoints with OpenAI-compatible format.

PropertyDetailsProvider Route`vertex_ai/gemma/{MODEL_NAME}`Vertex Documentation[Vertex AI Prediction](https://cloud.google.com/vertex-ai/docs/predictions/get-predictions)Required Parameter`api_base` - Full prediction endpoint URL

**Proxy Usage:**

**1. Add to config.yaml**

```
model_list:
-model_name: gemma-model
litellm_params:
model: vertex_ai/gemma/gemma-3-12b-it-1222199011122
api_base: https://ENDPOINT.us-central1-PROJECT.prediction.vertexai.goog/v1/projects/PROJECT_ID/locations/us-central1/endpoints/ENDPOINT_ID:predict
vertex_project:"my-project-id"
vertex_location:"us-central1"
```

**2. Start proxy**

```
litellm --config /path/to/config.yaml
```

**3. Test it**

```
curl http://0.0.0.0:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "gemma-model",
    "messages": [{"role": "user", "content": "What is machine learning?"}],
    "max_tokens": 100
  }'
```

**SDK Usage:**

```
from litellm import completion

response = completion(
    model="vertex_ai/gemma/gemma-3-12b-it-1222199011122",
    messages=[{"role":"user","content":"What is machine learning?"}],
    api_base="https://ENDPOINT.us-central1-PROJECT.prediction.vertexai.goog/v1/projects/PROJECT_ID/locations/us-central1/endpoints/ENDPOINT_ID:predict",
    vertex_project="my-project-id",
    vertex_location="us-central1",
)
```

## MedGemma Models (Custom Endpoints)[​](#medgemma-models-custom-endpoints "Direct link to MedGemma Models (Custom Endpoints)")

Deploy MedGemma models on custom Vertex AI prediction endpoints with OpenAI-compatible format. MedGemma models use the same `vertex_ai/gemma/` route.

PropertyDetailsProvider Route`vertex_ai/gemma/{MODEL_NAME}`Vertex Documentation[Vertex AI Prediction](https://cloud.google.com/vertex-ai/docs/predictions/get-predictions)Required Parameter`api_base` - Full prediction endpoint URL

**Proxy Usage:**

**1. Add to config.yaml**

```
model_list:
-model_name: medgemma-model
litellm_params:
model: vertex_ai/gemma/medgemma-2b-v1
api_base: https://ENDPOINT.us-central1-PROJECT.prediction.vertexai.goog/v1/projects/PROJECT_ID/locations/us-central1/endpoints/ENDPOINT_ID:predict
vertex_project:"my-project-id"
vertex_location:"us-central1"
```

**2. Start proxy**

```
litellm --config /path/to/config.yaml
```

**3. Test it**

```
curl http://0.0.0.0:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "medgemma-model",
    "messages": [{"role": "user", "content": "What are the symptoms of hypertension?"}],
    "max_tokens": 100
  }'
```

**SDK Usage:**

```
from litellm import completion

response = completion(
    model="vertex_ai/gemma/medgemma-2b-v1",
    messages=[{"role":"user","content":"What are the symptoms of hypertension?"}],
    api_base="https://ENDPOINT.us-central1-PROJECT.prediction.vertexai.goog/v1/projects/PROJECT_ID/locations/us-central1/endpoints/ENDPOINT_ID:predict",
    vertex_project="my-project-id",
    vertex_location="us-central1",
)
```