---
title: Image Generations | liteLLM
url: https://docs.litellm.ai/docs/image_generation
source: sitemap
fetched_at: 2026-01-21T19:45:26.239267592-03:00
rendered_js: false
word_count: 676
summary: This document provides documentation and usage instructions for the LiteLLM image_generation function and proxy server across multiple AI providers. It details available features, required parameters, and configuration steps for integrating image generation models into applications.
tags:
    - litellm
    - image-generation
    - api-integration
    - openai
    - azure-openai
    - ai-proxy
    - python-sdk
category: api
---

## Overview[​](#overview "Direct link to Overview")

FeatureSupportedNotesCost Tracking✅Works with all supported modelsLogging✅Works across all integrationsEnd-user Tracking✅Fallbacks✅Works between supported modelsLoadbalancing✅Works between supported modelsGuardrails✅Applies to input prompts (non-streaming only)Supported ProvidersOpenAI, Azure, Google AI Studio, Vertex AI, AWS Bedrock, Recraft, OpenRouter, Xinference, Nscale

## Quick Start[​](#quick-start "Direct link to Quick Start")

### LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

```
from litellm import image_generation
import os 

# set api keys 
os.environ["OPENAI_API_KEY"]=""

response = image_generation(prompt="A cute baby sea otter", model="dall-e-3")

print(f"response: {response}")
```

### LiteLLM Proxy[​](#litellm-proxy "Direct link to LiteLLM Proxy")

### Setup config.yaml[​](#setup-configyaml "Direct link to Setup config.yaml")

```
model_list:
-model_name: gpt-image-1### RECEIVED MODEL NAME ###
litellm_params:# all params accepted by litellm.image_generation()
model: azure/gpt-image-1### MODEL NAME sent to `litellm.image_generation()` ###
api_base: https://my-endpoint-europe-berri-992.openai.azure.com/
api_key:"os.environ/AZURE_API_KEY_EU"# does os.getenv("AZURE_API_KEY_EU")

```

### Start proxy[​](#start-proxy "Direct link to Start proxy")

```
litellm --config /path/to/config.yaml 

# RUNNING on http://0.0.0.0:4000
```

### Test[​](#test "Direct link to Test")

- Curl
- OpenAI

```
curl -X POST 'http://0.0.0.0:4000/v1/images/generations' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer sk-1234' \
-d '{
    "model": "gpt-image-1",
    "prompt": "A cute baby sea otter",
    "n": 1,
    "size": "1024x1024"
}'
```

## Input Params for `litellm.image_generation()`[​](#input-params-for-litellmimage_generation "Direct link to input-params-for-litellmimage_generation")

info

Any non-openai params, will be treated as provider-specific params, and sent in the request body as kwargs to the provider.

[**See Reserved Params**](https://github.com/BerriAI/litellm/blob/2f5f85cb52f36448d1f8bbfbd3b8af8167d0c4c8/litellm/main.py#L4082)

### Required Fields[​](#required-fields "Direct link to Required Fields")

- `prompt`: *string* - A text description of the desired image(s).

### Optional LiteLLM Fields[​](#optional-litellm-fields "Direct link to Optional LiteLLM Fields")

model: Optional\[str] = None, n: Optional\[int] = None, quality: Optional\[str] = None, response\_format: Optional\[str] = None, size: Optional\[str] = None, style: Optional\[str] = None, user: Optional\[str] = None, timeout=600, # default to 10 minutes api\_key: Optional\[str] = None, api\_base: Optional\[str] = None, api\_version: Optional\[str] = None, litellm\_logging\_obj=None, custom\_llm\_provider=None,

- `model`: *string (optional)* The model to use for image generation. Defaults to openai/gpt-image-1
- `n`: *int (optional)* The number of images to generate. Must be between 1 and 10. For dall-e-3, only n=1 is supported.
- `quality`: *string (optional)* The quality of the image that will be generated.
  
  - `auto` (default value) will automatically select the best quality for the given model.
  - `high`, `medium` and `low` are supported for `gpt-image-1`.
  - `hd` and `standard` are supported for `dall-e-3`.
  - `standard` is the only option for `dall-e-2`.
- `response_format`: *string (optional)* The format in which the generated images are returned. Must be one of url or b64\_json.
- `size`: *string (optional)* The size of the generated images. Must be one of `1024x1024`, `1536x1024` (landscape), `1024x1536` (portrait), or `auto` (default value) for `gpt-image-1`, one of `256x256`, `512x512`, or `1024x1024` for `dall-e-2`, and one of `1024x1024`, `1792x1024`, or `1024x1792` for `dall-e-3`.
- `timeout`: *integer* - The maximum time, in seconds, to wait for the API to respond. Defaults to 600 seconds (10 minutes).
- `user`: *string (optional)* A unique identifier representing your end-user,
- `api_base`: *string (optional)* - The api endpoint you want to call the model with
- `api_version`: *string (optional)* - (Azure-specific) the api version for the call; required for dall-e-3 on Azure
- `api_key`: *string (optional)* - The API key to authenticate and authorize requests. If not provided, the default API key is used.
- `api_type`: *string (optional)* - The type of API to use.

### Output from `litellm.image_generation()`[​](#output-from-litellmimage_generation "Direct link to output-from-litellmimage_generation")

```

{
"created":1703658209,
"data":[{
        'b64_json': None,
        'revised_prompt': 'Adorable baby sea otter with a coat of thick brown fur, playfully swimming in blue ocean waters. Its curious, bright eyes gleam as it is surfaced above water, tiny paws held close to its chest, as it playfully spins in the gentle waves under the soft rays of a setting sun.',
        'url': 'https://oaidalleapiprodscus.blob.core.windows.net/private/org-ikDc4ex8NB5ZzfTf8m5WYVB7/user-JpwZsbIXubBZvan3Y3GchiiB/img-dpa3g5LmkTrotY6M93dMYrdE.png?st=2023-12-27T05%3A23%3A29Z&se=2023-12-27T07%3A23%3A29Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-12-26T13%3A22%3A56Z&ske=2023-12-27T13%3A22%3A56Z&sks=b&skv=2021-08-06&sig=hUuQjYLS%2BvtsDdffEAp2gwewjC8b3ilggvkd9hgY6Uw%3D'
}],
"usage":{'prompt_tokens':0, 'completion_tokens':0, 'total_tokens':0}
}
```

## OpenAI Image Generation Models[​](#openai-image-generation-models "Direct link to OpenAI Image Generation Models")

### Usage[​](#usage "Direct link to Usage")

```
from litellm import image_generation
import os
os.environ['OPENAI_API_KEY']=""
response = image_generation(model='gpt-image-1', prompt="cute baby otter")
```

Model NameFunction CallRequired OS Variablesgpt-image-1`image_generation(model='gpt-image-1', prompt="cute baby otter")``os.environ['OPENAI_API_KEY']`dall-e-3`image_generation(model='dall-e-3', prompt="cute baby otter")``os.environ['OPENAI_API_KEY']`dall-e-2`image_generation(model='dall-e-2', prompt="cute baby otter")``os.environ['OPENAI_API_KEY']`

## Azure OpenAI Image Generation Models[​](#azure-openai-image-generation-models "Direct link to Azure OpenAI Image Generation Models")

### API keys[​](#api-keys "Direct link to API keys")

This can be set as env variables or passed as **params to litellm.image\_generation()**

```
import os
os.environ['AZURE_API_KEY']=
os.environ['AZURE_API_BASE']=
os.environ['AZURE_API_VERSION']=
```

### Usage[​](#usage-1 "Direct link to Usage")

```
from litellm import embedding
response = embedding(
    model="azure/<your deployment name>",
    prompt="cute baby otter",
    api_key=api_key,
    api_base=api_base,
    api_version=api_version,
)
print(response)
```

Model NameFunction Callgpt-image-1`image_generation(model="azure/<your deployment name>", prompt="cute baby otter")`dall-e-3`image_generation(model="azure/<your deployment name>", prompt="cute baby otter")`dall-e-2`image_generation(model="azure/<your deployment name>", prompt="cute baby otter")`

## Xinference Image Generation Models[​](#xinference-image-generation-models "Direct link to Xinference Image Generation Models")

Use this for Stable Diffusion models hosted on Xinference

#### Usage[​](#usage-2 "Direct link to Usage")

See Xinference usage with LiteLLM [here](https://docs.litellm.ai/docs/providers/xinference#image-generation)

## Recraft Image Generation Models[​](#recraft-image-generation-models "Direct link to Recraft Image Generation Models")

Use this for AI-powered design and image generation with Recraft

#### Usage[​](#usage-3 "Direct link to Usage")

```
from litellm import image_generation
import os

os.environ['RECRAFT_API_KEY']="your-api-key"

response = image_generation(
    model="recraft/recraftv3",
    prompt="A beautiful sunset over a calm ocean",
)
print(response)
```

See Recraft usage with LiteLLM [here](https://docs.litellm.ai/docs/providers/recraft#image-generation)

## OpenRouter Image Generation Models[​](#openrouter-image-generation-models "Direct link to OpenRouter Image Generation Models")

Use this for image generation models available through OpenRouter (e.g., Google Gemini image generation models)

#### Usage[​](#usage-4 "Direct link to Usage")

```
from litellm import image_generation
import os

os.environ['OPENROUTER_API_KEY']="your-api-key"

response = image_generation(
    model="openrouter/google/gemini-2.5-flash-image",
    prompt="A beautiful sunset over a calm ocean",
    size="1024x1024",
    quality="high",
)
print(response)
```

## OpenAI Compatible Image Generation Models[​](#openai-compatible-image-generation-models "Direct link to OpenAI Compatible Image Generation Models")

Use this for calling `/image_generation` endpoints on OpenAI Compatible Servers, example [https://github.com/xorbitsai/inference](https://github.com/xorbitsai/inference)

**Note add `openai/` prefix to model so litellm knows to route to OpenAI**

### Usage[​](#usage-5 "Direct link to Usage")

```
from litellm import image_generation
response = image_generation(
  model ="openai/<your-llm-name>",# add `openai/` prefix to model so litellm knows to route to OpenAI
  api_base="http://0.0.0.0:8000/"# set API Base of your Custom OpenAI Endpoint
  prompt="cute baby otter"
)
```

## Bedrock - Stable Diffusion[​](#bedrock---stable-diffusion "Direct link to Bedrock - Stable Diffusion")

Use this for stable diffusion on bedrock

### Usage[​](#usage-6 "Direct link to Usage")

```
import os
from litellm import image_generation

os.environ["AWS_ACCESS_KEY_ID"]=""
os.environ["AWS_SECRET_ACCESS_KEY"]=""
os.environ["AWS_REGION_NAME"]=""

response = image_generation(
            prompt="A cute baby sea otter",
            model="bedrock/stability.stable-diffusion-xl-v0",
)
print(f"response: {response}")
```

## VertexAI - Image Generation Models[​](#vertexai---image-generation-models "Direct link to VertexAI - Image Generation Models")

### Usage[​](#usage-7 "Direct link to Usage")

Use this for image generation models on VertexAI

```
response = litellm.image_generation(
    prompt="An olympic size swimming pool",
    model="vertex_ai/imagegeneration@006",
    vertex_ai_project="adroit-crow-413218",
    vertex_ai_location="us-central1",
)
print(f"response: {response}")
```

## Supported Providers[​](#supported-providers "Direct link to Supported Providers")

#### ⚡️See all supported models and providers at [models.litellm.ai](https://models.litellm.ai/)[​](#%EF%B8%8Fsee-all-supported-models-and-providers-at-modelslitellmai "Direct link to ️see-all-supported-models-and-providers-at-modelslitellmai")

ProviderDocumentation LinkOpenAI[OpenAI Image Generation →](https://docs.litellm.ai/docs/providers/openai)Azure OpenAI[Azure OpenAI Image Generation →](https://docs.litellm.ai/docs/providers/azure/azure)Google AI Studio[Google AI Studio Image Generation →](https://docs.litellm.ai/docs/providers/google_ai_studio/image_gen)Vertex AI[Vertex AI Image Generation →](https://docs.litellm.ai/docs/providers/vertex_image)AWS Bedrock[Bedrock Image Generation →](https://docs.litellm.ai/docs/providers/bedrock)Recraft[Recraft Image Generation →](https://docs.litellm.ai/docs/providers/recraft#image-generation)OpenRouter[OpenRouter Image Generation →](https://docs.litellm.ai/docs/providers/openrouter#image-generation)Xinference[Xinference Image Generation →](https://docs.litellm.ai/docs/providers/xinference#image-generation)Nscale[Nscale Image Generation →](https://docs.litellm.ai/docs/providers/nscale#image-generation)