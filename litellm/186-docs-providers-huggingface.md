---
title: Hugging Face | liteLLM
url: https://docs.litellm.ai/docs/providers/huggingface
source: sitemap
fetched_at: 2026-01-21T19:49:22.709240734-03:00
rendered_js: false
word_count: 235
summary: This document explains how to access Hugging Face models through various inference providers using LiteLLM and a single Hugging Face token. It details the model naming convention and demonstrates features like streaming, vision capabilities, and tool calling.
tags:
    - litellm
    - huggingface
    - inference-api
    - multi-provider
    - chat-completion
    - vision-models
    - function-calling
    - streaming
category: guide
---

With a single Hugging Face token, you can access inference through multiple providers. Your calls are routed through Hugging Face and the usage is billed directly to your Hugging Face account at the standard provider API rates.

To use a Hugging Face model, specify both the provider and model you want to use in the following format:

```
huggingface/<provider>/<hf_org_or_user>/<hf_model>
```

Where `<hf_org_or_user>/<hf_model>` is the Hugging Face model ID and `<provider>` is the inference provider.  
By default, if you don't specify a provider, LiteLLM will use the [HF Inference API](https://huggingface.co/docs/api-inference/en/index).

```
# Run DeepSeek-R1 inference through Together AI
completion(model="huggingface/together/deepseek-ai/DeepSeek-R1",...)

# Run Qwen2.5-72B-Instruct inference through Sambanova
completion(model="huggingface/sambanova/Qwen/Qwen2.5-72B-Instruct",...)

# Run Llama-3.3-70B-Instruct inference through HF Inference API
completion(model="huggingface/meta-llama/Llama-3.3-70B-Instruct",...)
```

Here's an example of chat completion using the DeepSeek-R1 model through Together AI:

```
import os
from litellm import completion

os.environ["HF_TOKEN"]="hf_xxxxxx"

response = completion(
    model="huggingface/together/deepseek-ai/DeepSeek-R1",
    messages=[
{
"role":"user",
"content":"How many r's are in the word 'strawberry'?",
}
],
)
print(response)
```

Now, let's see what a streaming request looks like.

```
import os
from litellm import completion

os.environ["HF_TOKEN"]="hf_xxxxxx"

response = completion(
    model="huggingface/together/deepseek-ai/DeepSeek-R1",
    messages=[
{
"role":"user",
"content":"How many r's are in the word `strawberry`?",

}
],
    stream=True,
)

for chunk in response:
print(chunk)
```

You can also pass images when the model supports it. Here is an example using [Llama-3.2-11B-Vision-Instruct](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct) model through Sambanova.

```
from litellm import completion

# Set your Hugging Face Token
os.environ["HF_TOKEN"]="hf_xxxxxx"

messages=[
{
"role":"user",
"content":[
{"type":"text","text":"What's in this image?"},
{
"type":"image_url",
"image_url":{
"url":"https://awsmp-logos.s3.amazonaws.com/seller-xw5kijmvmzasy/c233c9ade2ccb5491072ae232c814942.png",
}
},
],
}
]

response = completion(
    model="huggingface/sambanova/meta-llama/Llama-3.2-11B-Vision-Instruct",
    messages=messages,
)
print(response.choices[0])
```

You can extend the model's capabilities by giving them access to tools. Here is an example with function calling using [Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) model through Sambanova.

```
import os
from litellm import completion

# Set your Hugging Face Token
os.environ["HF_TOKEN"]="hf_xxxxxx"

tools =[
{
"type":"function",
"function":{
"name":"get_current_weather",
"description":"Get the current weather in a given location",
"parameters":{
"type":"object",
"properties":{
"location":{
"type":"string",
"description":"The city and state, e.g. San Francisco, CA",
},
"unit":{"type":"string","enum":["celsius","fahrenheit"]},
},
"required":["location"],
},
}
}
]
messages =[
{
"role":"user",
"content":"What's the weather like in Boston today?",
}
]

response = completion(
    model="huggingface/sambanova/meta-llama/Llama-3.3-70B-Instruct",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)
print(response)
```