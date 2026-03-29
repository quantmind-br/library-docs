---
title: Bedrock - Writer Palmyra | liteLLM
url: https://docs.litellm.ai/docs/providers/bedrock_writer
source: sitemap
fetched_at: 2026-01-21T19:48:33.330321565-03:00
rendered_js: false
word_count: 139
summary: This document provides instructions for integrating Writer Palmyra foundation models from Amazon Bedrock using LiteLLM, covering chat completions, tool calling, and PDF document processing.
tags:
    - amazon-bedrock
    - litellm
    - writer-palmyra
    - tool-calling
    - document-processing
    - llm-integration
category: guide
---

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionWriter Palmyra X5 and X4 foundation models on Amazon Bedrock, offering advanced reasoning, tool calling, and document processing capabilitiesProvider Route on LiteLLM`bedrock/`Supported Operations`/chat/completions`Link to Provider Doc[Writer on AWS Bedrock ↗](https://aws.amazon.com/bedrock/writer/)

## Quick Start[​](#quick-start "Direct link to Quick Start")

### LiteLLM SDK[​](#litellm-sdk "Direct link to LiteLLM SDK")

SDK Usage

```
import litellm
import os

os.environ["AWS_ACCESS_KEY_ID"]=""
os.environ["AWS_SECRET_ACCESS_KEY"]=""
os.environ["AWS_REGION_NAME"]="us-west-2"

response = litellm.completion(
    model="bedrock/us.writer.palmyra-x5-v1:0",
    messages=[{"role":"user","content":"Hello, how are you?"}]
)

print(response.choices[0].message.content)
```

### LiteLLM Proxy[​](#litellm-proxy "Direct link to LiteLLM Proxy")

**1. Setup config.yaml**

proxy\_config.yaml

```
model_list:
-model_name: writer-palmyra-x5
litellm_params:
model: bedrock/us.writer.palmyra-x5-v1:0
aws_access_key_id: os.environ/AWS_ACCESS_KEY_ID
aws_secret_access_key: os.environ/AWS_SECRET_ACCESS_KEY
aws_region_name: us-west-2
```

**2. Start the proxy**

Start Proxy

```
litellm --config config.yaml
```

**3. Call the proxy**

- curl
- OpenAI SDK

curl Request

```
curl -X POST http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "writer-palmyra-x5",
    "messages": [{"role": "user", "content": "Hello, how are you?"}]
  }'
```

Writer Palmyra models support multi-step tool calling for complex workflows.

### LiteLLM SDK[​](#litellm-sdk-1 "Direct link to LiteLLM SDK")

Tool Calling - SDK

```
import litellm

tools =[
{
"type":"function",
"function":{
"name":"get_weather",
"description":"Get the current weather in a location",
"parameters":{
"type":"object",
"properties":{
"location":{
"type":"string",
"description":"The city and state"
}
},
"required":["location"]
}
}
}
]

response = litellm.completion(
    model="bedrock/us.writer.palmyra-x5-v1:0",
    messages=[{"role":"user","content":"What's the weather in Boston?"}],
    tools=tools
)
```

### LiteLLM Proxy[​](#litellm-proxy-1 "Direct link to LiteLLM Proxy")

- curl
- OpenAI SDK

Tool Calling - curl

```
curl -X POST http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "writer-palmyra-x5",
    "messages": [{"role": "user", "content": "What'\''s the weather in Boston?"}],
    "tools": [{
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "Get the current weather in a location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {"type": "string", "description": "The city and state"}
          },
          "required": ["location"]
        }
      }
    }]
  }'
```

## Document Input[​](#document-input "Direct link to Document Input")

Writer Palmyra models support document inputs including PDFs.

### LiteLLM SDK[​](#litellm-sdk-2 "Direct link to LiteLLM SDK")

PDF Document Input - SDK

```
import litellm
import base64

# Read and encode PDF
withopen("document.pdf","rb")as f:
    pdf_base64 = base64.b64encode(f.read()).decode("utf-8")

response = litellm.completion(
    model="bedrock/us.writer.palmyra-x5-v1:0",
    messages=[
{
"role":"user",
"content":[
{
"type":"image_url",
"image_url":{
"url":f"data:application/pdf;base64,{pdf_base64}"
}
},
{
"type":"text",
"text":"Summarize this document"
}
]
}
]
)
```

### LiteLLM Proxy[​](#litellm-proxy-2 "Direct link to LiteLLM Proxy")

- curl
- OpenAI SDK

PDF Document Input - curl

```
# First, base64 encode your PDF
PDF_BASE64=$(base64 -i document.pdf)

curl -X POST http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "writer-palmyra-x5",
    "messages": [{
      "role": "user",
      "content": [
        {
          "type": "image_url",
          "image_url": {"url": "data:application/pdf;base64,'$PDF_BASE64'"}
        },
        {
          "type": "text",
          "text": "Summarize this document"
        }
      ]
    }]
  }'
```

## Supported Models[​](#supported-models "Direct link to Supported Models")

Model IDContext WindowInput Cost (per 1K tokens)Output Cost (per 1K tokens)`bedrock/us.writer.palmyra-x5-v1:0`1M tokens$0.0006$0.006`bedrock/us.writer.palmyra-x4-v1:0`128K tokens$0.0025$0.010`bedrock/writer.palmyra-x5-v1:0`1M tokens$0.0006$0.006`bedrock/writer.palmyra-x4-v1:0`128K tokens$0.0025$0.010

Cross-Region Inference

The `us.writer.*` model IDs use cross-region inference profiles. Use these for production workloads.