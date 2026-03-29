---
title: VLLM | liteLLM
url: https://docs.litellm.ai/docs/providers/vllm
source: sitemap
fetched_at: 2026-01-21T19:50:51.947357054-03:00
rendered_js: false
word_count: 340
summary: This document explains how to integrate LiteLLM with vLLM models using OpenAI-compatible endpoints, covering setup for completions, embeddings, reranking, and video processing.
tags:
    - vllm
    - litellm
    - openai-compatible
    - llm-inference
    - embeddings
    - rerank
    - video-processing
category: guide
---

LiteLLM supports all models on VLLM.

PropertyDetailsDescriptionvLLM is a fast and easy-to-use library for LLM inference and serving. [Docs](https://docs.vllm.ai/en/latest/index.html)Provider Route on LiteLLM`hosted_vllm/` (for OpenAI compatible server), `vllm/` (\[DEPRECATED] for vLLM sdk usage)Provider Doc[vLLM ↗](https://docs.vllm.ai/en/latest/index.html)Supported Endpoints`/chat/completions`, `/embeddings`, `/completions`, `/rerank`, `/audio/transcriptions`

## Quick Start

## Usage - litellm.completion (calling OpenAI compatible endpoint)[​](#usage---litellmcompletion-calling-openai-compatible-endpoint "Direct link to Usage - litellm.completion (calling OpenAI compatible endpoint)")

vLLM Provides an OpenAI compatible endpoints - here's how to call it with LiteLLM

In order to use litellm to call a hosted vllm server add the following to your completion call

- `model="hosted_vllm/<your-vllm-model-name>"`
- `api_base = "your-hosted-vllm-server"`

```
import litellm 

response = litellm.completion(
            model="hosted_vllm/facebook/opt-125m",# pass the vllm model name
            messages=messages,
            api_base="https://hosted-vllm-api.co",
            temperature=0.2,
            max_tokens=80)

print(response)
```

## Usage - LiteLLM Proxy Server (calling OpenAI compatible endpoint)[​](#usage----litellm-proxy-server-calling-openai-compatible-endpoint "Direct link to Usage - LiteLLM Proxy Server (calling OpenAI compatible endpoint)")

Here's how to call an OpenAI-Compatible Endpoint with the LiteLLM Proxy Server

1. Modify the config.yaml

```
model_list:
-model_name: my-model
litellm_params:
model: hosted_vllm/facebook/opt-125m  # add hosted_vllm/ prefix to route as OpenAI provider
api_base: https://hosted-vllm-api.co      # add api base for OpenAI compatible provider
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

## Reasoning Effort[​](#reasoning-effort "Direct link to Reasoning Effort")

- SDK
- PROXY

```
from litellm import completion

response = completion(
    model="hosted_vllm/gpt-oss-120b",
    messages=[{"role":"user","content":"whats 2 + 2"}],
    reasoning_effort="high",
    api_base="https://hosted-vllm-api.co",
)
print(response)
```

## Embeddings[​](#embeddings "Direct link to Embeddings")

- SDK
- PROXY

```
from litellm import embedding   
import os

os.environ["HOSTED_VLLM_API_BASE"]="http://localhost:8000"


embedding = embedding(model="hosted_vllm/facebook/opt-125m",input=["Hello world"])

print(embedding)
```

## Rerank[​](#rerank "Direct link to Rerank")

- SDK
- PROXY

```
from litellm import rerank
import os

os.environ["HOSTED_VLLM_API_BASE"]="http://localhost:8000"
os.environ["HOSTED_VLLM_API_KEY"]=""# [optional], if your VLLM server requires an API key

query ="What is the capital of the United States?"
documents =[
"Carson City is the capital city of the American state of Nevada.",
"The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
"Washington, D.C. is the capital of the United States.",
"Capital punishment has existed in the United States since before it was a country.",
]

response = rerank(
    model="hosted_vllm/your-rerank-model",
    query=query,
    documents=documents,
    top_n=3,
)
print(response)
```

### Async Usage[​](#async-usage "Direct link to Async Usage")

```
from litellm import arerank
import os, asyncio

os.environ["HOSTED_VLLM_API_BASE"]="http://localhost:8000"
os.environ["HOSTED_VLLM_API_KEY"]=""# [optional], if your VLLM server requires an API key

asyncdeftest_async_rerank():
    query ="What is the capital of the United States?"
    documents =[
"Carson City is the capital city of the American state of Nevada.",
"The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
"Washington, D.C. is the capital of the United States.",
"Capital punishment has existed in the United States since before it was a country.",
]

    response =await arerank(
        model="hosted_vllm/your-rerank-model",
        query=query,
        documents=documents,
        top_n=3,
)
print(response)

asyncio.run(test_async_rerank())
```

## Send Video URL to VLLM[​](#send-video-url-to-vllm "Direct link to Send Video URL to VLLM")

Example Implementation from VLLM [here](https://github.com/vllm-project/vllm/pull/10020)

- (Unified) Files Message
- (VLLM-specific) Video Message

Use this to send a video url to VLLM + Gemini in the same format, using OpenAI's `files` message type.

There are two ways to send a video url to VLLM:

1. Pass the video url directly

```
{"type": "file", "file": {"file_id": video_url}},
```

2. Pass the video data as base64

```
{"type": "file", "file": {"file_data": f"data:video/mp4;base64,{video_data_base64}"}}
```

- SDK
- PROXY

```
from litellm import completion

messages=[
{
"role":"user",
"content":[
{
"type":"text",
"text":"Summarize the following video"
},
{
"type":"file",
"file":{
"file_id":"https://www.youtube.com/watch?v=dQw4w9WgXcQ"
}
}
]
}
]

# call vllm 
os.environ["HOSTED_VLLM_API_BASE"]="https://hosted-vllm-api.co"
os.environ["HOSTED_VLLM_API_KEY"]=""# [optional], if your VLLM server requires an API key
response = completion(
    model="hosted_vllm/qwen",# pass the vllm model name
    messages=messages,
)

# call gemini 
os.environ["GEMINI_API_KEY"]="your-gemini-api-key"
response = completion(
    model="gemini/gemini-1.5-flash",# pass the gemini model name
    messages=messages,
)

print(response)
```

## (Deprecated) for `vllm pip package`[​](#deprecated-for-vllm-pip-package "Direct link to deprecated-for-vllm-pip-package")

### Using - `litellm.completion`[​](#using---litellmcompletion "Direct link to using---litellmcompletion")

```
import litellm 

response = litellm.completion(
            model="vllm/facebook/opt-125m",# add a vllm prefix so litellm knows the custom_llm_provider==vllm
            messages=messages,
            temperature=0.2,
            max_tokens=80)

print(response)
```

### Batch Completion[​](#batch-completion "Direct link to Batch Completion")

```
from litellm import batch_completion

model_name ="facebook/opt-125m"
provider ="vllm"
messages =[[{"role":"user","content":"Hey, how's it going"}]for _ inrange(5)]

response_list = batch_completion(
            model=model_name,
            custom_llm_provider=provider,# can easily switch to huggingface, replicate, together ai, sagemaker, etc.
            messages=messages,
            temperature=0.2,
            max_tokens=80,
)
print(response_list)
```

### Prompt Templates[​](#prompt-templates "Direct link to Prompt Templates")

For models with special prompt templates (e.g. Llama2), we format the prompt to fit their template.

**What if we don't support a model you need?** You can also specify you're own custom prompt formatting, in case we don't have your model covered yet.

**Does this mean you have to specify a prompt for all models?** No. By default we'll concatenate your message content to make a prompt (expected format for Bloom, T-5, Llama-2 base models, etc.)

**Default Prompt Template**

```
defdefault_pt(messages):
return" ".join(message["content"]for message in messages)
```

[Code for how prompt templates work in LiteLLM](https://github.com/BerriAI/litellm/blob/main/litellm/llms/prompt_templates/factory.py)

#### Models we already have Prompt Templates for[​](#models-we-already-have-prompt-templates-for "Direct link to Models we already have Prompt Templates for")

Model NameWorks for ModelsFunction Callmeta-llama/Llama-2-7b-chatAll meta-llama llama2 chat models`completion(model='vllm/meta-llama/Llama-2-7b', messages=messages, api_base="your_api_endpoint")`tiiuae/falcon-7b-instructAll falcon instruct models`completion(model='vllm/tiiuae/falcon-7b-instruct', messages=messages, api_base="your_api_endpoint")`mosaicml/mpt-7b-chatAll mpt chat models`completion(model='vllm/mosaicml/mpt-7b-chat', messages=messages, api_base="your_api_endpoint")`codellama/CodeLlama-34b-Instruct-hfAll codellama instruct models`completion(model='vllm/codellama/CodeLlama-34b-Instruct-hf', messages=messages, api_base="your_api_endpoint")`WizardLM/WizardCoder-Python-34B-V1.0All wizardcoder models`completion(model='vllm/WizardLM/WizardCoder-Python-34B-V1.0', messages=messages, api_base="your_api_endpoint")`Phind/Phind-CodeLlama-34B-v2All phind-codellama models`completion(model='vllm/Phind/Phind-CodeLlama-34B-v2', messages=messages, api_base="your_api_endpoint")`

#### Custom prompt templates[​](#custom-prompt-templates "Direct link to Custom prompt templates")

```
# Create your own custom prompt template works 
litellm.register_prompt_template(
	model="togethercomputer/LLaMA-2-7B-32K",
	roles={
"system":{
"pre_message":"[INST] <<SYS>>\n",
"post_message":"\n<</SYS>>\n [/INST]\n"
},
"user":{
"pre_message":"[INST] ",
"post_message":" [/INST]\n"
},
"assistant":{
"pre_message":"\n",
"post_message":"\n",
}
}# tell LiteLLM how you want to map the openai messages to this model
)

deftest_vllm_custom_model():
    model ="vllm/togethercomputer/LLaMA-2-7B-32K"
    response = completion(model=model, messages=messages)
print(response['choices'][0]['message']['content'])
return response

test_vllm_custom_model()
```

[Implementation Code](https://github.com/BerriAI/litellm/blob/6b3cb1898382f2e4e80fd372308ea232868c78d1/litellm/utils.py#L1414)