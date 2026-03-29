---
title: AWS Sagemaker | liteLLM
url: https://docs.litellm.ai/docs/providers/aws_sagemaker
source: sitemap
fetched_at: 2026-01-21T19:48:02.470296303-03:00
rendered_js: false
word_count: 327
summary: This document provides instructions and examples for integrating LiteLLM with AWS Sagemaker Huggingface Jumpstart models, covering SDK usage, proxy configuration, and parameter customization. It explains how to handle authentication, streaming, and provider-specific configurations for Sagemaker endpoints.
tags:
    - aws-sagemaker
    - litellm
    - huggingface-jumpstart
    - api-integration
    - model-deployment
    - python-sdk
    - streaming
    - configuration
category: guide
---

LiteLLM supports All Sagemaker Huggingface Jumpstart Models

tip

**We support ALL Sagemaker models, just set `model=sagemaker/<any-model-on-sagemaker>` as a prefix when sending litellm requests**

### API KEYS[​](#api-keys "Direct link to API KEYS")

```
os.environ["AWS_ACCESS_KEY_ID"]=""
os.environ["AWS_SECRET_ACCESS_KEY"]=""
os.environ["AWS_REGION_NAME"]=""
```

### Usage[​](#usage "Direct link to Usage")

```
import os 
from litellm import completion

os.environ["AWS_ACCESS_KEY_ID"]=""
os.environ["AWS_SECRET_ACCESS_KEY"]=""
os.environ["AWS_REGION_NAME"]=""

response = completion(
            model="sagemaker/<your-endpoint-name>",
            messages=[{"content":"Hello, how are you?","role":"user"}],
            temperature=0.2,
            max_tokens=80
)
```

### Usage - Streaming[​](#usage---streaming "Direct link to Usage - Streaming")

Sagemaker currently does not support streaming - LiteLLM fakes streaming by returning chunks of the response string

```
import os 
from litellm import completion

os.environ["AWS_ACCESS_KEY_ID"]=""
os.environ["AWS_SECRET_ACCESS_KEY"]=""
os.environ["AWS_REGION_NAME"]=""

response = completion(
            model="sagemaker/jumpstart-dft-meta-textgeneration-llama-2-7b",
            messages=[{"content":"Hello, how are you?","role":"user"}],
            temperature=0.2,
            max_tokens=80,
            stream=True,
)
for chunk in response:
print(chunk)
```

## **LiteLLM Proxy Usage**[​](#litellm-proxy-usage "Direct link to litellm-proxy-usage")

Here's how to call Sagemaker with the LiteLLM Proxy Server

### 1. Setup config.yaml[​](#1-setup-configyaml "Direct link to 1. Setup config.yaml")

```
model_list:
-model_name: jumpstart-model
litellm_params:
model: sagemaker/jumpstart-dft-hf-textgeneration1-mp-20240815-185614
aws_access_key_id: os.environ/CUSTOM_AWS_ACCESS_KEY_ID
aws_secret_access_key: os.environ/CUSTOM_AWS_SECRET_ACCESS_KEY
aws_region_name: os.environ/CUSTOM_AWS_REGION_NAME
```

All possible auth params:

```
aws_access_key_id: Optional[str],
aws_secret_access_key: Optional[str],
aws_session_token: Optional[str],
aws_region_name: Optional[str],
aws_session_name: Optional[str],
aws_profile_name: Optional[str],
aws_role_name: Optional[str],
aws_web_identity_token: Optional[str],
```

### 2. Start the proxy[​](#2-start-the-proxy "Direct link to 2. Start the proxy")

```
litellm --config /path/to/config.yaml
```

### 3. Test it[​](#3-test-it "Direct link to 3. Test it")

- Curl Request
- OpenAI v1.0.0+
- Langchain

```
curl --location 'http://0.0.0.0:4000/chat/completions' \
--header 'Content-Type: application/json' \
--data ' {
      "model": "jumpstart-model",
      "messages": [
        {
          "role": "user",
          "content": "what llm are you"
        }
      ]
    }
'
```

## Set temperature, top p, etc.[​](#set-temperature-top-p-etc "Direct link to Set temperature, top p, etc.")

- SDK
- PROXY

```
import os
from litellm import completion

os.environ["AWS_ACCESS_KEY_ID"]=""
os.environ["AWS_SECRET_ACCESS_KEY"]=""
os.environ["AWS_REGION_NAME"]=""

response = completion(
  model="sagemaker/jumpstart-dft-hf-textgeneration1-mp-20240815-185614",
  messages=[{"content":"Hello, how are you?","role":"user"}],
  temperature=0.7,
  top_p=1
)
```

## **Allow setting temperature=0** for Sagemaker[​](#allow-setting-temperature0-for-sagemaker "Direct link to allow-setting-temperature0-for-sagemaker")

By default when `temperature=0` is sent in requests to LiteLLM, LiteLLM rounds up to `temperature=0.1` since Sagemaker fails most requests when `temperature=0`

If you want to send `temperature=0` for your model here's how to set it up (Since Sagemaker can host any kind of model, some models allow zero temperature)

- SDK
- PROXY

```
import os
from litellm import completion

os.environ["AWS_ACCESS_KEY_ID"]=""
os.environ["AWS_SECRET_ACCESS_KEY"]=""
os.environ["AWS_REGION_NAME"]=""

response = completion(
  model="sagemaker/jumpstart-dft-hf-textgeneration1-mp-20240815-185614",
  messages=[{"content":"Hello, how are you?","role":"user"}],
  temperature=0,
  aws_sagemaker_allow_zero_temp=True,
)
```

## Pass provider-specific params[​](#pass-provider-specific-params "Direct link to Pass provider-specific params")

If you pass a non-openai param to litellm, we'll assume it's provider-specific and send it as a kwarg in the request body. [See more](https://docs.litellm.ai/docs/completion/input#provider-specific-params)

- SDK
- PROXY

```
import os
from litellm import completion

os.environ["AWS_ACCESS_KEY_ID"]=""
os.environ["AWS_SECRET_ACCESS_KEY"]=""
os.environ["AWS_REGION_NAME"]=""

response = completion(
  model="sagemaker/jumpstart-dft-hf-textgeneration1-mp-20240815-185614",
  messages=[{"content":"Hello, how are you?","role":"user"}],
  top_k=1# 👈 PROVIDER-SPECIFIC PARAM
)
```

### Passing Inference Component Name[​](#passing-inference-component-name "Direct link to Passing Inference Component Name")

If you have multiple models on an endpoint, you'll need to specify the individual model names, do this via `model_id`.

```
import os 
from litellm import completion

os.environ["AWS_ACCESS_KEY_ID"]=""
os.environ["AWS_SECRET_ACCESS_KEY"]=""
os.environ["AWS_REGION_NAME"]=""

response = completion(
            model="sagemaker/<your-endpoint-name>",
            model_id="<your-model-name",
            messages=[{"content":"Hello, how are you?","role":"user"}],
            temperature=0.2,
            max_tokens=80
)
```

### Passing credentials as parameters - Completion()[​](#passing-credentials-as-parameters---completion "Direct link to Passing credentials as parameters - Completion()")

Pass AWS credentials as parameters to litellm.completion

```
import os 
from litellm import completion

response = completion(
            model="sagemaker/jumpstart-dft-meta-textgeneration-llama-2-7b",
            messages=[{"content":"Hello, how are you?","role":"user"}],
            aws_access_key_id="",
            aws_secret_access_key="",
            aws_region_name="",
)
```

### Applying Prompt Templates[​](#applying-prompt-templates "Direct link to Applying Prompt Templates")

To apply the correct prompt template for your sagemaker deployment, pass in it's hf model name as well.

```
import os 
from litellm import completion

os.environ["AWS_ACCESS_KEY_ID"]=""
os.environ["AWS_SECRET_ACCESS_KEY"]=""
os.environ["AWS_REGION_NAME"]=""

response = completion(
            model="sagemaker/jumpstart-dft-meta-textgeneration-llama-2-7b",
            messages=messages,
            temperature=0.2,
            max_tokens=80,
            hf_model_name="meta-llama/Llama-2-7b",
)
```

You can also pass in your own [custom prompt template](https://docs.litellm.ai/docs/completion/prompt_formatting#format-prompt-yourself)

## Sagemaker Messages API[​](#sagemaker-messages-api "Direct link to Sagemaker Messages API")

Use route `sagemaker_chat/*` to route to Sagemaker Messages API

```
model: sagemaker_chat/<your-endpoint-name>
```

- SDK
- PROXY

```
import os
import litellm
from litellm import completion

litellm.set_verbose =True# 👈 SEE RAW REQUEST

os.environ["AWS_ACCESS_KEY_ID"]=""
os.environ["AWS_SECRET_ACCESS_KEY"]=""
os.environ["AWS_REGION_NAME"]=""

response = completion(
            model="sagemaker_chat/<your-endpoint-name>",
            messages=[{"content":"Hello, how are you?","role":"user"}],
            temperature=0.2,
            max_tokens=80
)
```

## Completion Models[​](#completion-models "Direct link to Completion Models")

tip

**We support ALL Sagemaker models, just set `model=sagemaker/<any-model-on-sagemaker>` as a prefix when sending litellm requests**

Here's an example of using a sagemaker model with LiteLLM

Model NameFunction CallYour Custom Huggingface Model`completion(model='sagemaker/<your-deployment-name>', messages=messages)`Meta Llama 2 7B`completion(model='sagemaker/jumpstart-dft-meta-textgeneration-llama-2-7b', messages=messages)`Meta Llama 2 7B (Chat/Fine-tuned)`completion(model='sagemaker/jumpstart-dft-meta-textgeneration-llama-2-7b-f', messages=messages)`Meta Llama 2 13B`completion(model='sagemaker/jumpstart-dft-meta-textgeneration-llama-2-13b', messages=messages)`Meta Llama 2 13B (Chat/Fine-tuned)`completion(model='sagemaker/jumpstart-dft-meta-textgeneration-llama-2-13b-f', messages=messages)`Meta Llama 2 70B`completion(model='sagemaker/jumpstart-dft-meta-textgeneration-llama-2-70b', messages=messages)`Meta Llama 2 70B (Chat/Fine-tuned)`completion(model='sagemaker/jumpstart-dft-meta-textgeneration-llama-2-70b-b-f', messages=messages)`

## Embedding Models[​](#embedding-models "Direct link to Embedding Models")

LiteLLM supports all Sagemaker Jumpstart Huggingface Embedding models. Here's how to call it:

```
from litellm import completion

os.environ["AWS_ACCESS_KEY_ID"]=""
os.environ["AWS_SECRET_ACCESS_KEY"]=""
os.environ["AWS_REGION_NAME"]=""

response = litellm.embedding(model="sagemaker/<your-deployment-name>",input=["good morning from litellm","this is another item"])
print(f"response: {response}")
```