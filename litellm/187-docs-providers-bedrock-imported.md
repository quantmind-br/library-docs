---
title: Bedrock Imported Models | liteLLM
url: https://docs.litellm.ai/docs/providers/bedrock_imported
source: sitemap
fetched_at: 2026-01-21T19:48:29.791375212-03:00
rendered_js: false
word_count: 323
summary: This document outlines how to configure and use various AWS Bedrock imported models, including Deepseek and Qwen architectures, through the LiteLLM SDK and proxy.
tags:
    - aws-bedrock
    - litellm
    - deepseek
    - qwen
    - model-import
    - openai-compatible
category: guide
---

Bedrock Imported Models (Deepseek, Deepseek R1, Qwen, OpenAI-compatible models)

### Deepseek R1[​](#deepseek-r1 "Direct link to Deepseek R1")

This is a separate route, as the chat template is different.

PropertyDetailsProvider Route`bedrock/deepseek_r1/{model_arn}`Provider Documentation[Bedrock Imported Models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html), [Deepseek Bedrock Imported Model](https://aws.amazon.com/blogs/machine-learning/deploy-deepseek-r1-distilled-llama-models-with-amazon-bedrock-custom-model-import/)

- SDK
- Proxy

```
from litellm import completion
import os

response = completion(
    model="bedrock/deepseek_r1/arn:aws:bedrock:us-east-1:086734376398:imported-model/r4c4kewx2s0n",# bedrock/deepseek_r1/{your-model-arn}
    messages=[{"role":"user","content":"Tell me a joke"}],
)
```

### Deepseek (not R1)[​](#deepseek-not-r1 "Direct link to Deepseek (not R1)")

PropertyDetailsProvider Route`bedrock/llama/{model_arn}`Provider Documentation[Bedrock Imported Models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html), [Deepseek Bedrock Imported Model](https://aws.amazon.com/blogs/machine-learning/deploy-deepseek-r1-distilled-llama-models-with-amazon-bedrock-custom-model-import/)

Use this route to call Bedrock Imported Models that follow the `llama` Invoke Request / Response spec

- SDK
- Proxy

```
from litellm import completion
import os

response = completion(
    model="bedrock/llama/arn:aws:bedrock:us-east-1:086734376398:imported-model/r4c4kewx2s0n",# bedrock/llama/{your-model-arn}
    messages=[{"role":"user","content":"Tell me a joke"}],
)
```

### Qwen3 Imported Models[​](#qwen3-imported-models "Direct link to Qwen3 Imported Models")

PropertyDetailsProvider Route`bedrock/qwen3/{model_arn}`Provider Documentation[Bedrock Imported Models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html), [Qwen3 Models](https://aws.amazon.com/about-aws/whats-new/2025/09/qwen3-models-fully-managed-amazon-bedrock/)

- SDK
- Proxy

```
from litellm import completion
import os

response = completion(
    model="bedrock/qwen3/arn:aws:bedrock:us-east-1:086734376398:imported-model/your-qwen3-model",# bedrock/qwen3/{your-model-arn}
    messages=[{"role":"user","content":"Tell me a joke"}],
    max_tokens=100,
    temperature=0.7
)
```

### Qwen2 Imported Models[​](#qwen2-imported-models "Direct link to Qwen2 Imported Models")

PropertyDetailsProvider Route`bedrock/qwen2/{model_arn}`Provider Documentation[Bedrock Imported Models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html)NoteQwen2 and Qwen3 architectures are mostly similar. The main difference is in the response format: Qwen2 uses "text" field while Qwen3 uses "generation" field.

- SDK
- Proxy

```
from litellm import completion
import os

response = completion(
    model="bedrock/qwen2/arn:aws:bedrock:us-east-1:086734376398:imported-model/your-qwen2-model",# bedrock/qwen2/{your-model-arn}
    messages=[{"role":"user","content":"Tell me a joke"}],
    max_tokens=100,
    temperature=0.7
)
```

### OpenAI-Compatible Imported Models (Qwen 2.5 VL, etc.)[​](#openai-compatible-imported-models-qwen-25-vl-etc "Direct link to OpenAI-Compatible Imported Models (Qwen 2.5 VL, etc.)")

Use this route for Bedrock imported models that follow the **OpenAI Chat Completions API spec**. This includes models like Qwen 2.5 VL that accept OpenAI-formatted messages with support for vision (images), tool calling, and other OpenAI features.

PropertyDetailsProvider Route`bedrock/openai/{model_arn}`Provider Documentation[Bedrock Imported Models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html)Supported FeaturesVision (images), tool calling, streaming, system messages

#### LiteLLMSDK Usage[​](#litellmsdk-usage "Direct link to LiteLLMSDK Usage")

**Basic Usage**

```
from litellm import completion

response = completion(
    model="bedrock/openai/arn:aws:bedrock:us-east-1:046319184608:imported-model/0m2lasirsp6z",# bedrock/openai/{your-model-arn}
    messages=[{"role":"user","content":"Tell me a joke"}],
    max_tokens=300,
    temperature=0.5
)
```

**With Vision (Images)**

```
import base64
from litellm import completion

# Load and encode image
withopen("image.jpg","rb")as f:
    image_base64 = base64.b64encode(f.read()).decode("utf-8")

response = completion(
    model="bedrock/openai/arn:aws:bedrock:us-east-1:046319184608:imported-model/0m2lasirsp6z",
    messages=[
{
"role":"system",
"content":"You are a helpful assistant that can analyze images."
},
{
"role":"user",
"content":[
{"type":"text","text":"What's in this image?"},
{
"type":"image_url",
"image_url":{"url":f"data:image/jpeg;base64,{image_base64}"}
}
]
}
],
    max_tokens=300,
    temperature=0.5
)
```

**Comparing Multiple Images**

```
import base64
from litellm import completion

# Load images
withopen("image1.jpg","rb")as f:
    image1_base64 = base64.b64encode(f.read()).decode("utf-8")
withopen("image2.jpg","rb")as f:
    image2_base64 = base64.b64encode(f.read()).decode("utf-8")

response = completion(
    model="bedrock/openai/arn:aws:bedrock:us-east-1:046319184608:imported-model/0m2lasirsp6z",
    messages=[
{
"role":"system",
"content":"You are a helpful assistant that can analyze images."
},
{
"role":"user",
"content":[
{"type":"text","text":"Spot the difference between these two images?"},
{
"type":"image_url",
"image_url":{"url":f"data:image/jpeg;base64,{image1_base64}"}
},
{
"type":"image_url",
"image_url":{"url":f"data:image/jpeg;base64,{image2_base64}"}
}
]
}
],
    max_tokens=300,
    temperature=0.5
)
```

#### LiteLLM Proxy Usage (AI Gateway)[​](#litellm-proxy-usage-ai-gateway "Direct link to LiteLLM Proxy Usage (AI Gateway)")

**1. Add to config**

```
model_list:
-model_name: qwen-25vl-72b
litellm_params:
model: bedrock/openai/arn:aws:bedrock:us-east-1:046319184608:imported-model/0m2lasirsp6z
```

**2. Start proxy**

```
litellm --config /path/to/config.yaml

# RUNNING at http://0.0.0.0:4000
```

**3. Test it!**

Basic text request:

```
curl --location 'http://0.0.0.0:4000/chat/completions' \
      --header 'Authorization: Bearer sk-1234' \
      --header 'Content-Type: application/json' \
      --data '{
            "model": "qwen-25vl-72b",
            "messages": [
                {
                    "role": "user",
                    "content": "what llm are you"
                }
            ],
            "max_tokens": 300
        }'
```

With vision (image):

```
curl --location 'http://0.0.0.0:4000/chat/completions' \
      --header 'Authorization: Bearer sk-1234' \
      --header 'Content-Type: application/json' \
      --data '{
            "model": "qwen-25vl-72b",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant that can analyze images."
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "What is in this image?"},
                        {
                            "type": "image_url",
                            "image_url": {"url": "data:image/jpeg;base64,/9j/4AAQSkZ..."}
                        }
                    ]
                }
            ],
            "max_tokens": 300,
            "temperature": 0.5
        }'
```

### Moonshot Kimi K2 Thinking[​](#moonshot-kimi-k2-thinking "Direct link to Moonshot Kimi K2 Thinking")

Moonshot AI's Kimi K2 Thinking model is now available on Amazon Bedrock. This model features advanced reasoning capabilities with automatic reasoning content extraction.

PropertyDetailsProvider Route`bedrock/moonshot.kimi-k2-thinking`, `bedrock/invoke/moonshot.kimi-k2-thinking`Provider Documentation[AWS Bedrock Moonshot Announcement ↗](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-bedrock-fully-managed-open-weight-models/)Supported Parameters`temperature`, `max_tokens`, `top_p`, `stream`, `tools`, `tool_choice`Special FeaturesReasoning content extraction, Tool calling

#### Supported Features[​](#supported-features "Direct link to Supported Features")

- **Reasoning Content Extraction**: Automatically extracts `<reasoning>` tags and returns them as `reasoning_content` (similar to OpenAI's o1 models)
- **Tool Calling**: Full support for function/tool calling with tool responses
- **Streaming**: Both streaming and non-streaming responses
- **System Messages**: System message support

#### Basic Usage[​](#basic-usage "Direct link to Basic Usage")

- SDK
- Proxy

Moonshot Kimi K2 SDK Usage

```
from litellm import completion
import os

os.environ["AWS_ACCESS_KEY_ID"]="your-aws-access-key"
os.environ["AWS_SECRET_ACCESS_KEY"]="your-aws-secret-key"
os.environ["AWS_REGION_NAME"]="us-west-2"# or your preferred region

# Basic completion
response = completion(
    model="bedrock/moonshot.kimi-k2-thinking",# or bedrock/invoke/moonshot.kimi-k2-thinking
    messages=[
{"role":"user","content":"What is 2+2? Think step by step."}
],
    temperature=0.7,
    max_tokens=200
)

print(response.choices[0].message.content)

# Access reasoning content if present
if response.choices[0].message.reasoning_content:
print("Reasoning:", response.choices[0].message.reasoning_content)
```

#### Tool Calling Example[​](#tool-calling-example "Direct link to Tool Calling Example")

Kimi K2 with Tool Calling

```
from litellm import completion
import os

os.environ["AWS_ACCESS_KEY_ID"]="your-aws-access-key"
os.environ["AWS_SECRET_ACCESS_KEY"]="your-aws-secret-key"
os.environ["AWS_REGION_NAME"]="us-west-2"

# Tool calling example
response = completion(
    model="bedrock/moonshot.kimi-k2-thinking",
    messages=[
{"role":"user","content":"What's the weather in Tokyo?"}
],
    tools=[
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
"description":"The city name"
}
},
"required":["location"]
}
}
}
]
)

if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
print(f"Tool called: {tool_call.function.name}")
print(f"Arguments: {tool_call.function.arguments}")
```

#### Streaming Example[​](#streaming-example "Direct link to Streaming Example")

Kimi K2 Streaming

```
from litellm import completion
import os

os.environ["AWS_ACCESS_KEY_ID"]="your-aws-access-key"
os.environ["AWS_SECRET_ACCESS_KEY"]="your-aws-secret-key"
os.environ["AWS_REGION_NAME"]="us-west-2"

response = completion(
    model="bedrock/moonshot.kimi-k2-thinking",
    messages=[
{"role":"user","content":"Explain quantum computing in simple terms."}
],
    stream=True,
    temperature=0.7
)

for chunk in response:
if chunk.choices[0].delta.content:
print(chunk.choices[0].delta.content, end="")

# Check for reasoning content in streaming
ifhasattr(chunk.choices[0].delta,'reasoning_content')and chunk.choices[0].delta.reasoning_content:
print(f"\n[Reasoning: {chunk.choices[0].delta.reasoning_content}]")
```

#### Supported Parameters[​](#supported-parameters "Direct link to Supported Parameters")

ParameterTypeDescriptionSupported`temperature`float (0-1)Controls randomness in output✅`max_tokens`integerMaximum tokens to generate✅`top_p`floatNucleus sampling parameter✅`stream`booleanEnable streaming responses✅`tools`arrayTool/function definitions✅`tool_choice`string/objectTool choice specification✅`stop`arrayStop sequences❌ (Not supported on Bedrock)