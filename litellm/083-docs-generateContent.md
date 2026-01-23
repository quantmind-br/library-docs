---
title: /generateContent | liteLLM
url: https://docs.litellm.ai/docs/generateContent
source: sitemap
fetched_at: 2026-01-21T19:45:18.97605738-03:00
rendered_js: false
word_count: 70
summary: This document provides instructions and code examples for using LiteLLM to interact with Google Gemini models through the Python SDK and Proxy Server. It covers setup for text generation, streaming responses, and configuration for various integration methods.
tags:
    - litellm
    - google-gemini
    - python-sdk
    - llm-proxy
    - streaming
    - text-generation
    - google-ai
category: guide
---

Use LiteLLM to call Google AI's generateContent endpoints for text generation, multimodal interactions, and streaming responses.

## Overview[​](#overview "Direct link to Overview")

FeatureSupportedNotesCost Tracking✅Logging✅works across all integrationsEnd-user Tracking✅Streaming✅Fallbacks✅between supported modelsLoadbalancing✅between supported models

## Usage[​](#usage "Direct link to Usage")

* * *

### LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

- Basic Usage
- Sync Usage

#### Non-streaming example[​](#non-streaming-example "Direct link to Non-streaming example")

Basic Text Generation

```
from litellm.google_genai import agenerate_content
from google.genai.types import ContentDict, PartDict
import os

# Set API key
os.environ["GEMINI_API_KEY"]="your-gemini-api-key"

contents = ContentDict(
    parts=[
        PartDict(text="Hello, can you tell me a short joke?")
],
    role="user",
)

response =await agenerate_content(
    contents=contents,
    model="gemini/gemini-2.0-flash",
    max_tokens=100,
)
print(response)
```

#### Streaming example[​](#streaming-example "Direct link to Streaming example")

Streaming Text Generation

```
from litellm.google_genai import agenerate_content_stream
from google.genai.types import ContentDict, PartDict
import os

# Set API key
os.environ["GEMINI_API_KEY"]="your-gemini-api-key"

contents = ContentDict(
    parts=[
        PartDict(text="Write a long story about space exploration")
],
    role="user",
)

response =await agenerate_content_stream(
    contents=contents,
    model="gemini/gemini-2.0-flash",
    max_tokens=500,
)

asyncfor chunk in response:
print(chunk)
```

### LiteLLM Proxy Server[​](#litellm-proxy-server "Direct link to LiteLLM Proxy Server")

1. Setup config.yaml

```
model_list:
-model_name: gemini-flash
litellm_params:
model: gemini/gemini-2.0-flash
api_key: os.environ/GEMINI_API_KEY
```

2. Start proxy

```
litellm --config /path/to/config.yaml
```

3. Test it!

<!--THE END-->

- Google GenAI SDK
- curl

Google GenAI SDK with LiteLLM Proxy

```
from google.genai import Client
import os

# Configure Google GenAI SDK to use LiteLLM proxy
os.environ["GOOGLE_GEMINI_BASE_URL"]="http://localhost:4000"
os.environ["GEMINI_API_KEY"]="sk-1234"

client = Client()

response = client.models.generate_content(
    model="gemini-flash",
    contents=[
{
"parts":[{"text":"Write a short story about AI"}],
"role":"user"
}
],
    config={"max_output_tokens":100}
)
```

- [Use LiteLLM with gemini-cli](https://docs.litellm.ai/docs/tutorials/litellm_gemini_cli)