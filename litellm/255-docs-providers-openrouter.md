---
title: OpenRouter | liteLLM
url: https://docs.litellm.ai/docs/providers/openrouter
source: sitemap
fetched_at: 2026-01-21T19:50:03.414699558-03:00
rendered_js: false
word_count: 232
summary: This document provides instructions and code examples for integrating LiteLLM with OpenRouter to perform text completion, embeddings, and image generation across various models.
tags:
    - litellm
    - openrouter
    - text-completion
    - image-generation
    - embeddings
    - api-configuration
category: guide
---

LiteLLM supports all the text / chat / vision / embedding models from [OpenRouter](https://openrouter.ai/docs)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BerriAI/litellm/blob/main/cookbook/LiteLLM_OpenRouter.ipynb)

## Usage[​](#usage "Direct link to Usage")

```
import os
from litellm import completion

os.environ["OPENROUTER_API_KEY"]=""
os.environ["OPENROUTER_API_BASE"]=""# [OPTIONAL] defaults to https://openrouter.ai/api/v1
os.environ["OR_SITE_URL"]=""# [OPTIONAL]
os.environ["OR_APP_NAME"]=""# [OPTIONAL]

response = completion(
            model="openrouter/google/palm-2-chat-bison",
            messages=messages,
)
```

## Configuration with Environment Variables[​](#configuration-with-environment-variables "Direct link to Configuration with Environment Variables")

For production environments, you can dynamically configure the base\_url using environment variables:

```
import os
from litellm import completion

# Configure with environment variables
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_API_BASE","https://openrouter.ai/api/v1")

# Set environment for LiteLLM
os.environ["OPENROUTER_API_KEY"]= OPENROUTER_API_KEY
os.environ["OPENROUTER_API_BASE"]= OPENROUTER_BASE_URL

response = completion(
    model="openrouter/google/palm-2-chat-bison",
    messages=messages,
    base_url=OPENROUTER_BASE_URL  # Explicitly pass base_url for clarity
)
```

This approach provides better flexibility for managing configurations across different environments (dev, staging, production) and makes it easier to switch between self-hosted and cloud endpoints.

## OpenRouter Completion Models[​](#openrouter-completion-models "Direct link to OpenRouter Completion Models")

🚨 LiteLLM supports ALL OpenRouter models, send `model=openrouter/<your-openrouter-model>` to send it to open router. See all openrouter models [here](https://openrouter.ai/models)

Model NameFunction Callopenrouter/openai/gpt-3.5-turbo`completion('openrouter/openai/gpt-3.5-turbo', messages)`openrouter/openai/gpt-3.5-turbo-16k`completion('openrouter/openai/gpt-3.5-turbo-16k', messages)`openrouter/openai/gpt-4`completion('openrouter/openai/gpt-4', messages)`openrouter/openai/gpt-4-32k`completion('openrouter/openai/gpt-4-32k', messages)`openrouter/anthropic/claude-2`completion('openrouter/anthropic/claude-2', messages)`openrouter/anthropic/claude-instant-v1`completion('openrouter/anthropic/claude-instant-v1', messages)`openrouter/google/palm-2-chat-bison`completion('openrouter/google/palm-2-chat-bison', messages)`openrouter/google/palm-2-codechat-bison`completion('openrouter/google/palm-2-codechat-bison', messages)`openrouter/meta-llama/llama-2-13b-chat`completion('openrouter/meta-llama/llama-2-13b-chat', messages)`openrouter/meta-llama/llama-2-70b-chat`completion('openrouter/meta-llama/llama-2-70b-chat', messages)`

## Passing OpenRouter Params - transforms, models, route[​](#passing-openrouter-params---transforms-models-route "Direct link to Passing OpenRouter Params - transforms, models, route")

Pass `transforms`, `models`, `route`as arguments to `litellm.completion()`

```
import os
from litellm import completion

os.environ["OPENROUTER_API_KEY"]=""

response = completion(
            model="openrouter/google/palm-2-chat-bison",
            messages=messages,
            transforms =[""],
            route=""
)
```

## Embedding[​](#embedding "Direct link to Embedding")

```
from litellm import embedding
import os

os.environ["OPENROUTER_API_KEY"]="your-api-key"

response = embedding(
    model="openrouter/openai/text-embedding-3-small",
input=["good morning from litellm","this is another item"],
)
print(response)
```

## Image Generation[​](#image-generation "Direct link to Image Generation")

OpenRouter supports image generation through select models like Google Gemini image generation models. LiteLLM transforms standard image generation requests to OpenRouter's chat completion format.

### Supported Parameters[​](#supported-parameters "Direct link to Supported Parameters")

- `size`: Maps to OpenRouter's `aspect_ratio` format
  
  - `1024x1024` → `1:1` (square)
  - `1536x1024` → `3:2` (landscape)
  - `1024x1536` → `2:3` (portrait)
  - `1792x1024` → `16:9` (wide landscape)
  - `1024x1792` → `9:16` (tall portrait)
- `quality`: Maps to OpenRouter's `image_size` format (Gemini models)
  
  - `low` or `standard` → `1K`
  - `medium` → `2K`
  - `high` or `hd` → `4K`
- `n`: Number of images to generate

### Usage[​](#usage-1 "Direct link to Usage")

```
from litellm import image_generation
import os

os.environ["OPENROUTER_API_KEY"]="your-api-key"

# Basic image generation
response = image_generation(
    model="openrouter/google/gemini-2.5-flash-image",
    prompt="A beautiful sunset over a calm ocean",
)
print(response)
```

### Advanced Usage with Parameters[​](#advanced-usage-with-parameters "Direct link to Advanced Usage with Parameters")

```
from litellm import image_generation
import os

os.environ["OPENROUTER_API_KEY"]="your-api-key"

# Generate high-quality landscape image
response = image_generation(
    model="openrouter/google/gemini-2.5-flash-image",
    prompt="A serene mountain landscape with a lake",
    size="1536x1024",# Landscape format
    quality="high",# High quality (4K)
)

# Access the generated image
image_data = response.data[0]
if image_data.b64_json:
# Base64 encoded image
print(f"Generated base64 image: {image_data.b64_json[:50]}...")
elif image_data.url:
# Image URL
print(f"Generated image URL: {image_data.url}")
```

### Using OpenRouter-Specific Parameters[​](#using-openrouter-specific-parameters "Direct link to Using OpenRouter-Specific Parameters")

You can also pass OpenRouter-specific parameters directly using `image_config`:

```
from litellm import image_generation
import os

os.environ["OPENROUTER_API_KEY"]="your-api-key"

response = image_generation(
    model="openrouter/google/gemini-2.5-flash-image",
    prompt="A futuristic cityscape at night",
    image_config={
"aspect_ratio":"16:9",# OpenRouter native format
"image_size":"4K"# OpenRouter native format
}
)
print(response)
```

### Response Format[​](#response-format "Direct link to Response Format")

The response follows the standard LiteLLM ImageResponse format:

```
{
"created":1703658209,
"data":[{
"b64_json":"iVBORw0KGgoAAAANSUhEUgAA...",# Base64 encoded image
"url":None,
"revised_prompt":None
}],
"usage":{
"input_tokens":10,
"output_tokens":1290,
"total_tokens":1300
}
}
```

### Cost Tracking[​](#cost-tracking "Direct link to Cost Tracking")

OpenRouter provides cost information in the response, which LiteLLM automatically tracks:

```
response = image_generation(
    model="openrouter/google/gemini-2.5-flash-image",
    prompt="A cute baby sea otter",
)

# Cost is available in the response metadata
print(f"Request cost: ${response._hidden_params['additional_headers']['llm_provider-x-litellm-response-cost']}")
```