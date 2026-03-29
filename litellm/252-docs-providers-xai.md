---
title: xAI | liteLLM
url: https://docs.litellm.ai/docs/providers/xai
source: sitemap
fetched_at: 2026-01-21T19:50:58.648216377-03:00
rendered_js: false
word_count: 258
summary: This document provides technical specifications and implementation guides for using xAI's Grok models through the LiteLLM library, covering model versions, feature support, and proxy configuration.
tags:
    - xai
    - grok
    - litellm
    - api-integration
    - python-sdk
    - llm-models
    - reasoning-models
category: reference
---

[https://docs.x.ai/docs](https://docs.x.ai/docs)

tip

**We support ALL xAI models, just set `model=xai/<any-model-on-xai>` as a prefix when sending litellm requests**

## Supported Models[​](#supported-models "Direct link to Supported Models")

**Latest Release** - Grok 4.1 Fast: Optimized for high-performance agentic tool calling with 2M context and prompt caching.

ModelContextFeatures`xai/grok-4-1-fast-reasoning`2M tokens**Reasoning**, Function calling, Vision, Audio, Web search, Caching`xai/grok-4-1-fast-non-reasoning`2M tokensFunction calling, Vision, Audio, Web search, Caching

**When to use:**

- ✅ **Reasoning model**: Complex analysis, planning, multi-step reasoning problems
- ✅ **Non-reasoning model**: Simple queries, faster responses, lower token usage

**Example:**

```
from litellm import completion

# With reasoning
response = completion(
    model="xai/grok-4-1-fast-reasoning",
    messages=[{"role":"user","content":"Analyze this problem step by step..."}]
)

# Without reasoning
response = completion(
    model="xai/grok-4-1-fast-non-reasoning",
    messages=[{"role":"user","content":"What's 2+2?"}]
)
```

* * *

### All Available Models[​](#all-available-models "Direct link to All Available Models")

Model FamilyModelContextFeatures**Grok 4.1**`xai/grok-4-1-fast-reasoning`2M**Reasoning**, Tools, Vision, Audio, Web search, Caching`xai/grok-4-1-fast-non-reasoning`2MTools, Vision, Audio, Web search, Caching**Grok 4**`xai/grok-4`256KTools, Web search`xai/grok-4-0709`256KTools, Web search`xai/grok-4-fast-reasoning`2M**Reasoning**, Tools, Web search`xai/grok-4-fast-non-reasoning`2MTools, Web search**Grok 3**`xai/grok-3`131KTools, Web search`xai/grok-3-mini`131KTools, Web search`xai/grok-3-fast-beta`131KTools, Web search**Grok Code**`xai/grok-code-fast`256K**Reasoning**, Tools, Code generation, Caching**Grok 2**`xai/grok-2`131KTools, **Vision**`xai/grok-2-vision-latest`32KTools, **Vision**

**Features:**

- **Reasoning** = Chain-of-thought reasoning with reasoning tokens
- **Tools** = Function calling / Tool use
- **Web search** = Live internet search
- **Vision** = Image understanding
- **Audio** = Audio input support
- **Caching** = Prompt caching for cost savings
- **Code generation** = Optimized for code tasks

**Pricing:** See [xAI's pricing page](https://docs.x.ai/docs/models) for current rates.

## API Key[​](#api-key "Direct link to API Key")

```
# env variable
os.environ['XAI_API_KEY']
```

## Sample Usage[​](#sample-usage "Direct link to Sample Usage")

LiteLLM python sdk usage - Non-streaming

```
from litellm import completion
import os

os.environ['XAI_API_KEY']=""
response = completion(
    model="xai/grok-3-mini-beta",
    messages=[
{
"role":"user",
"content":"What's the weather like in Boston today in Fahrenheit?",
}
],
    max_tokens=10,
    response_format={"type":"json_object"},
    seed=123,
    stop=["\n\n"],
    temperature=0.2,
    top_p=0.9,
    tool_choice="auto",
    tools=[],
    user="user",
)
print(response)
```

## Sample Usage - Streaming[​](#sample-usage---streaming "Direct link to Sample Usage - Streaming")

LiteLLM python sdk usage - Streaming

```
from litellm import completion
import os

os.environ['XAI_API_KEY']=""
response = completion(
    model="xai/grok-3-mini-beta",
    messages=[
{
"role":"user",
"content":"What's the weather like in Boston today in Fahrenheit?",
}
],
    stream=True,
    max_tokens=10,
    response_format={"type":"json_object"},
    seed=123,
    stop=["\n\n"],
    temperature=0.2,
    top_p=0.9,
    tool_choice="auto",
    tools=[],
    user="user",
)

for chunk in response:
print(chunk)
```

## Sample Usage - Vision[​](#sample-usage---vision "Direct link to Sample Usage - Vision")

LiteLLM python sdk usage - Vision

```
import os 
from litellm import completion

os.environ["XAI_API_KEY"]="your-api-key"

response = completion(
    model="xai/grok-2-vision-latest",
    messages=[
{
"role":"user",
"content":[
{
"type":"image_url",
"image_url":{
"url":"https://science.nasa.gov/wp-content/uploads/2023/09/web-first-images-release.png",
"detail":"high",
},
},
{
"type":"text",
"text":"What's in this image?",
},
],
},
],
)
```

## Usage with LiteLLM Proxy Server[​](#usage-with-litellm-proxy-server "Direct link to Usage with LiteLLM Proxy Server")

Here's how to call a XAI model with the LiteLLM Proxy Server

1. Modify the config.yaml

```
model_list:
-model_name: my-model
litellm_params:
model: xai/<your-model-name># add xai/ prefix to route as XAI provider
api_key: api-key                 # api key to send your model
```

2. Start the proxy

```
$ litellm --config /path/to/config.yaml
```

3. Send Request to LiteLLM Proxy Server

<!--THE END-->

- OpenAI Python v1.0.0+
- curl

```
import openai
client = openai.OpenAI(
    api_key="sk-1234",# pass litellm proxy key, if you're using virtual keys
    base_url="http://0.0.0.0:4000"# litellm-proxy-base url
)

response = client.chat.completions.create(
    model="my-model",
    messages =[
{
"role":"user",
"content":"what llm are you"
}
],
)

print(response)
```

## Reasoning Usage[​](#reasoning-usage "Direct link to Reasoning Usage")

LiteLLM supports reasoning usage for xAI models.

- LiteLLM Python SDK
- LiteLLM Proxy - OpenAI SDK Usage

reasoning with xai/grok-3-mini-beta

```
import litellm
response = litellm.completion(
    model="xai/grok-3-mini-beta",
    messages=[{"role":"user","content":"What is 101*3?"}],
    reasoning_effort="low",
)

print("Reasoning Content:")
print(response.choices[0].message.reasoning_content)

print("\nFinal Response:")
print(completion.choices[0].message.content)

print("\nNumber of completion tokens (input):")
print(completion.usage.completion_tokens)

print("\nNumber of reasoning tokens (input):")
print(completion.usage.completion_tokens_details.reasoning_tokens)
```

**Example Response:**

```
Reasoning Content:
Let me calculate 101 multiplied by 3:
101 * 3 = 303.
I can double-check that: 100 * 3 is 300, and 1 * 3 is 3, so 300 + 3 = 303. Yes, that's correct.

Final Response:
The result of 101 multiplied by 3 is 303.

Number of completion tokens (input):
14

Number of reasoning tokens (input):
310
```