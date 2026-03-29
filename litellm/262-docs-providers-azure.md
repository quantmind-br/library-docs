---
title: Azure OpenAI | liteLLM
url: https://docs.litellm.ai/docs/providers/azure/
source: sitemap
fetched_at: 2026-01-21T19:48:16.074242375-03:00
rendered_js: false
word_count: 1013
summary: This document provides instructions for integrating Azure OpenAI Service and Azure Foundry models with LiteLLM using the Python SDK and Proxy Server.
tags:
    - azure-openai
    - litellm
    - python-sdk
    - api-integration
    - azure-foundry
    - chat-completions
category: guide
---

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionAzure OpenAI Service provides REST API access to OpenAI's powerful language models including o1, o1-mini, GPT-5, GPT-4o, GPT-4o mini, GPT-4 Turbo with Vision, GPT-4, GPT-3.5-Turbo, and Embeddings model series. Also supports Claude models via Azure Foundry.Provider Route on LiteLLM`azure/`, [`azure/o_series/`](#o-series-models), [`azure/gpt5_series/`](#gpt-5-models), [`azure/claude-*`](https://docs.litellm.ai/docs/providers/azure/azure_anthropic) (Claude models via Azure Foundry)Supported Operations[`/chat/completions`](#azure-openai-chat-completion-models), [`/responses`](https://docs.litellm.ai/docs/providers/azure/azure_responses), [`/completions`](#azure-instruct-models), [`/embeddings`](https://docs.litellm.ai/docs/providers/azure/azure_embedding), [`/audio/speech`](https://docs.litellm.ai/docs/providers/azure/azure_speech), [`/audio/transcriptions`](https://docs.litellm.ai/docs/providers/audio_transcription), `/fine_tuning`, [`/batches`](#azure-batches-api), `/files`, [`/images`](https://docs.litellm.ai/docs/providers/image_generation#azure-openai-image-generation-models), [`/anthropic/v1/messages`](https://docs.litellm.ai/docs/providers/azure/azure_anthropic)Link to Provider Doc[Azure OpenAI ↗](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview), [Azure Foundry Claude ↗](https://learn.microsoft.com/en-us/azure/ai-services/foundry-models/claude)

## API Keys, Params[​](#api-keys-params "Direct link to API Keys, Params")

api\_key, api\_base, api\_version etc can be passed directly to `litellm.completion` - see here or set as `litellm.api_key` params see here

```
import os
os.environ["AZURE_API_KEY"]=""# "my-azure-api-key"
os.environ["AZURE_API_BASE"]=""# "https://example-endpoint.openai.azure.com"
os.environ["AZURE_API_VERSION"]=""# "2023-05-15"

# optional
os.environ["AZURE_AD_TOKEN"]=""
os.environ["AZURE_API_TYPE"]=""
```

Azure Foundry Claude Models

Azure also supports Claude models via Azure Foundry. Use `azure/claude-*` model names (e.g., `azure/claude-sonnet-4-5`) with Azure authentication. See the [Azure Anthropic documentation](https://docs.litellm.ai/docs/providers/azure/azure_anthropic) for details.

## **Usage - LiteLLM Python SDK**[​](#usage---litellm-python-sdk "Direct link to usage---litellm-python-sdk")

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BerriAI/litellm/blob/main/cookbook/LiteLLM_Azure_OpenAI.ipynb)

### Completion - using .env variables[​](#completion---using-env-variables "Direct link to Completion - using .env variables")

```
from litellm import completion

## set ENV variables
os.environ["AZURE_API_KEY"]=""
os.environ["AZURE_API_BASE"]=""
os.environ["AZURE_API_VERSION"]=""

# azure call
response = completion(
    model ="azure/<your_deployment_name>",
    messages =[{"content":"Hello, how are you?","role":"user"}]
)
```

### Completion - using api\_key, api\_base, api\_version[​](#completion---using-api_key-api_base-api_version "Direct link to Completion - using api_key, api_base, api_version")

```
import litellm

# azure call
response = litellm.completion(
    model ="azure/<your deployment name>",# model = azure/<your deployment name> 
    api_base ="",# azure api base
    api_version ="",# azure api version
    api_key ="",# azure api key
    messages =[{"role":"user","content":"good morning"}],
)
```

### Completion - using azure\_ad\_token, api\_base, api\_version[​](#completion---using-azure_ad_token-api_base-api_version "Direct link to Completion - using azure_ad_token, api_base, api_version")

```
import litellm

# azure call
response = litellm.completion(
    model ="azure/<your deployment name>",# model = azure/<your deployment name> 
    api_base ="",# azure api base
    api_version ="",# azure api version
    azure_ad_token="",# azure_ad_token 
    messages =[{"role":"user","content":"good morning"}],
)
```

## **Usage - LiteLLM Proxy Server**[​](#usage---litellm-proxy-server "Direct link to usage---litellm-proxy-server")

Here's how to call Azure OpenAI models with the LiteLLM Proxy Server

### 1. Save key in your environment[​](#1-save-key-in-your-environment "Direct link to 1. Save key in your environment")

### 2. Start the proxy[​](#2-start-the-proxy "Direct link to 2. Start the proxy")

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: azure/chatgpt-v-2
api_base: https://openai-gpt-4-test-v-1.openai.azure.com/
api_version:"2023-05-15"
api_key: os.environ/AZURE_API_KEY # The `os.environ/` prefix tells litellm to read this from the env.
```

### 3. Test it[​](#3-test-it "Direct link to 3. Test it")

- Curl Request
- OpenAI v1.0.0+
- Langchain

```
curl --location 'http://0.0.0.0:4000/chat/completions' \
--header 'Content-Type: application/json' \
--data ' {
      "model": "gpt-3.5-turbo",
      "messages": [
        {
          "role": "user",
          "content": "what llm are you"
        }
      ]
    }
'
```

### Setting API Version[​](#setting-api-version "Direct link to Setting API Version")

You can set the `api_version` for Azure OpenAI in your proxy config.yaml in the following ways

#### Option 1: Per Model Configuration[​](#option-1-per-model-configuration "Direct link to Option 1: Per Model Configuration")

config.yaml

```
model_list:
-model_name: gpt-4
litellm_params:
model: azure/my-gpt4-deployment
api_base: https://your-resource.openai.azure.com/
api_version:"2024-08-01-preview"# Set version per model
api_key: os.environ/AZURE_API_KEY
```

## Azure OpenAI Chat Completion Models[​](#azure-openai-chat-completion-models "Direct link to Azure OpenAI Chat Completion Models")

tip

**We support ALL Azure models, just set `model=azure/<your deployment name>` as a prefix when sending litellm requests**

Model NameFunction Callo1-mini`response = completion(model="azure/<your deployment name>", messages=messages)`o1-preview`response = completion(model="azure/<your deployment name>", messages=messages)`gpt-5`response = completion(model="azure/<your deployment name>", messages=messages)`gpt-4o-mini`completion('azure/<your deployment name>', messages)`gpt-4o`completion('azure/<your deployment name>', messages)`gpt-4`completion('azure/<your deployment name>', messages)`gpt-4-0314`completion('azure/<your deployment name>', messages)`gpt-4-0613`completion('azure/<your deployment name>', messages)`gpt-4-32k`completion('azure/<your deployment name>', messages)`gpt-4-32k-0314`completion('azure/<your deployment name>', messages)`gpt-4-32k-0613`completion('azure/<your deployment name>', messages)`gpt-4-1106-preview`completion('azure/<your deployment name>', messages)`gpt-4-0125-preview`completion('azure/<your deployment name>', messages)`gpt-3.5-turbo`completion('azure/<your deployment name>', messages)`gpt-3.5-turbo-0301`completion('azure/<your deployment name>', messages)`gpt-3.5-turbo-0613`completion('azure/<your deployment name>', messages)`gpt-3.5-turbo-16k`completion('azure/<your deployment name>', messages)`gpt-3.5-turbo-16k-0613`completion('azure/<your deployment name>', messages)`

## Azure OpenAI Vision Models[​](#azure-openai-vision-models "Direct link to Azure OpenAI Vision Models")

Model NameFunction Callgpt-4-vision`completion(model="azure/<your deployment name>", messages=messages)`gpt-4o`completion('azure/<your deployment name>', messages)`

#### Usage[​](#usage "Direct link to Usage")

```
import os 
from litellm import completion

os.environ["AZURE_API_KEY"]="your-api-key"

# azure call
response = completion(
    model ="azure/<your deployment name>",
    messages=[
{
"role":"user",
"content":[
{
"type":"text",
"text":"What’s in this image?"
},
{
"type":"image_url",
"image_url":{
"url":"https://awsmp-logos.s3.amazonaws.com/seller-xw5kijmvmzasy/c233c9ade2ccb5491072ae232c814942.png"
}
}
]
}
],
)

```

#### Usage - with Azure Vision enhancements[​](#usage---with-azure-vision-enhancements "Direct link to Usage - with Azure Vision enhancements")

Note: **Azure requires the `base_url` to be set with `/extensions`**

Example

```
base_url=https://gpt-4-vision-resource.openai.azure.com/openai/deployments/gpt-4-vision/extensions
# base_url="{azure_endpoint}/openai/deployments/{azure_deployment}/extensions"
```

**Usage**

```
import os 
from litellm import completion

os.environ["AZURE_API_KEY"]="your-api-key"

# azure call
response = completion(
            model="azure/gpt-4-vision",
            timeout=5,
            messages=[
{
"role":"user",
"content":[
{"type":"text","text":"Whats in this image?"},
{
"type":"image_url",
"image_url":{
"url":"https://avatars.githubusercontent.com/u/29436595?v=4"
},
},
],
}
],
            base_url="https://gpt-4-vision-resource.openai.azure.com/openai/deployments/gpt-4-vision/extensions",
            api_key=os.getenv("AZURE_VISION_API_KEY"),
            enhancements={"ocr":{"enabled":True},"grounding":{"enabled":True}},
            dataSources=[
{
"type":"AzureComputerVision",
"parameters":{
"endpoint":"https://gpt-4-vision-enhancement.cognitiveservices.azure.com/",
"key": os.environ["AZURE_VISION_ENHANCE_KEY"],
},
}
],
)
```

## O-Series Models[​](#o-series-models "Direct link to O-Series Models")

Azure OpenAI O-Series models are supported on LiteLLM.

LiteLLM routes any deployment name with `o1` or `o3` in the model name, to the O-Series [transformation](https://github.com/BerriAI/litellm/blob/91ed05df2962b8eee8492374b048d27cc144d08c/litellm/llms/azure/chat/o1_transformation.py#L4) logic.

To set this explicitly, set `model` to `azure/o_series/<your-deployment-name>`.

**Automatic Routing**

- SDK
- PROXY

```
import litellm

litellm.completion(model="azure/my-o3-deployment", messages=[{"role":"user","content":"Hello, world!"}])# 👈 Note: 'o3' in the deployment name
```

**Explicit Routing**

- SDK
- PROXY

```
import litellm

litellm.completion(model="azure/o_series/my-random-deployment-name", messages=[{"role":"user","content":"Hello, world!"}])# 👈 Note: 'o_series/' in the deployment name
```

## GPT-5 Models[​](#gpt-5-models "Direct link to GPT-5 Models")

PropertyDetailsDescriptionAzure OpenAI GPT-5 modelsProvider Route on LiteLLM`azure/gpt5_series/<custom-name>` or `azure/gpt-5-deployment-name`

LiteLLM supports using Azure GPT-5 models in one of the two ways:

1. Explicit Routing: `model = azure/gpt5_series/<deployment-name>`. In this scenario the model onboarded to litellm follows the format `model=azure/gpt5_series/<deployment-name>`.
2. Inferred Routing (If the azure deployment name contains `gpt-5` in the name): `model = azure/gpt-5-mini`. In this scenario the model onboarded to litellm follows the format `model=azure/gpt-5-mini`.

#### Explicit Routing[​](#explicit-routing "Direct link to Explicit Routing")

Use `azure/gpt5_series/<deployment-name>` for explicit GPT-5 model routing.

- SDK
- PROXY

```
import litellm

response = litellm.completion(
    model="azure/gpt5_series/my-gpt-5-deployment",
    messages=[{"role":"user","content":"Hello, world!"}]
)
```

#### Inferred Routing (gpt-5 in the deployment name)[​](#inferred-routing-gpt-5-in-the-deployment-name "Direct link to Inferred Routing (gpt-5 in the deployment name)")

If your Azure deployment name contains `gpt-5`, LiteLLM automatically recognizes it as a GPT-5 model.

- SDK
- PROXY

```
import litellm

# Deployment name contains 'gpt-5' - automatically inferred
response = litellm.completion(
    model="azure/my-gpt-5-deployment",
    messages=[{"role":"user","content":"Hello, world!"}]
)
```

## Azure Audio Model[​](#azure-audio-model "Direct link to Azure Audio Model")

- SDK
- PROXY

```
from litellm import completion
import os

os.environ["AZURE_API_KEY"]=""
os.environ["AZURE_API_BASE"]=""
os.environ["AZURE_API_VERSION"]=""

response = completion(
    model="azure/azure-openai-4o-audio",
    messages=[
{
"role":"user",
"content":"I want to try out speech to speech"
}
],
    modalities=["text","audio"],
    audio={"voice":"alloy","format":"wav"}
)

print(response)
```

## Azure Instruct Models[​](#azure-instruct-models "Direct link to Azure Instruct Models")

Use `model="azure_text/<your-deployment>"`

Model NameFunction Callgpt-3.5-turbo-instruct`response = completion(model="azure_text/<your deployment name>", messages=messages)`gpt-3.5-turbo-instruct-0914`response = completion(model="azure_text/<your deployment name>", messages=messages)`

```
import litellm

## set ENV variables
os.environ["AZURE_API_KEY"]=""
os.environ["AZURE_API_BASE"]=""
os.environ["AZURE_API_VERSION"]=""

response = litellm.completion(
    model="azure_text/<your-deployment-name",
    messages=[{"role":"user","content":"What is the weather like in Boston?"}]
)

print(response)
```

## **Authentication**[​](#authentication "Direct link to authentication")

### Entra ID - use `azure_ad_token`[​](#entra-id---use-azure_ad_token "Direct link to entra-id---use-azure_ad_token")

This is a walkthrough on how to use Azure Active Directory Tokens - Microsoft Entra ID to make `litellm.completion()` calls.

> **Note:** You can follow the same process below to use Azure Active Directory Tokens for all other Azure endpoints (e.g., chat, embeddings, image, audio, etc.) with LiteLLM.

Step 1 - Download Azure CLI Installation instructions: [https://learn.microsoft.com/en-us/cli/azure/install-azure-cli](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)

```
brew update && brew install azure-cli
```

Step 2 - Sign in using `az`

Step 3 - Generate azure ad token

```
az account get-access-token --resource https://cognitiveservices.azure.com
```

In this step you should see an `accessToken` generated

```
{
  "accessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSIsImtpZCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSJ9",
  "expiresOn": "2023-11-14 15:50:46.000000",
  "expires_on": 1700005846,
  "subscription": "db38de1f-4bb3..",
  "tenant": "bdfd79b3-8401-47..",
  "tokenType": "Bearer"
}
```

Step 4 - Make litellm.completion call with Azure AD token

Set `azure_ad_token` = `accessToken` from step 3 or set `os.environ['AZURE_AD_TOKEN']`

- SDK
- PROXY config.yaml

```
response = litellm.completion(
    model ="azure/<your deployment name>",# model = azure/<your deployment name> 
    api_base ="",# azure api base
    api_version ="",# azure api version
    azure_ad_token="",# your accessToken from step 3 
    messages =[{"role":"user","content":"good morning"}],
)

```

### Entra ID - use tenant\_id, client\_id, client\_secret[​](#entra-id---use-tenant_id-client_id-client_secret "Direct link to Entra ID - use tenant_id, client_id, client_secret")

Here is an example of setting up `tenant_id`, `client_id`, `client_secret` in your litellm proxy `config.yaml`

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: azure/chatgpt-v-2
api_base: https://openai-gpt-4-test-v-1.openai.azure.com/
api_version:"2023-05-15"
tenant_id: os.environ/AZURE_TENANT_ID
client_id: os.environ/AZURE_CLIENT_ID
client_secret: os.environ/AZURE_CLIENT_SECRET
azure_scope: os.environ/AZURE_SCOPE  # defaults to "https://cognitiveservices.azure.com/.default"
```

Test it

```
curl --location 'http://0.0.0.0:4000/chat/completions' \
--header 'Content-Type: application/json' \
--data ' {
      "model": "gpt-3.5-turbo",
      "messages": [
        {
          "role": "user",
          "content": "what llm are you"
        }
      ]
    }
'
```

Example video of using `tenant_id`, `client_id`, `client_secret` with LiteLLM Proxy Server

### Entra ID - use client\_id, username, password[​](#entra-id---use-client_id-username-password "Direct link to Entra ID - use client_id, username, password")

Here is an example of setting up `client_id`, `azure_username`, `azure_password` in your litellm proxy `config.yaml`

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: azure/chatgpt-v-2
api_base: https://openai-gpt-4-test-v-1.openai.azure.com/
api_version:"2023-05-15"
client_id: os.environ/AZURE_CLIENT_ID
azure_username: os.environ/AZURE_USERNAME
azure_password: os.environ/AZURE_PASSWORD
azure_scope: os.environ/AZURE_SCOPE  # defaults to "https://cognitiveservices.azure.com/.default"
```

Test it

```
curl --location 'http://0.0.0.0:4000/chat/completions' \
--header 'Content-Type: application/json' \
--data ' {
      "model": "gpt-3.5-turbo",
      "messages": [
        {
          "role": "user",
          "content": "what llm are you"
        }
      ]
    }
'
```

Use this if you want to use Azure `DefaultAzureCredential` for Authentication on your requests. `DefaultAzureCredential` automatically discovers and uses available Azure credentials from multiple sources.

- SDK
- PROXY config.yaml

**Option 1: Explicit DefaultAzureCredential (Recommended)**

```
from litellm import completion
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# DefaultAzureCredential automatically discovers credentials from:
# - Environment variables (AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, AZURE_TENANT_ID)
# - Managed Identity (AKS, Azure VMs, etc.)
# - Azure CLI credentials
# - And other Azure identity sources
token_provider = get_bearer_token_provider(DefaultAzureCredential(),"https://cognitiveservices.azure.com/.default")

response = completion(
    model ="azure/<your deployment name>",# model = azure/<your deployment name> 
    api_base ="",# azure api base
    api_version ="",# azure api version
    azure_ad_token_provider=token_provider,
    messages =[{"role":"user","content":"good morning"}],
)
```

**Option 2: LiteLLM Auto-Fallback to DefaultAzureCredential**

```
import litellm

# Enable automatic fallback to DefaultAzureCredential
litellm.enable_azure_ad_token_refresh =True

response = litellm.completion(
    model ="azure/<your deployment name>",
    api_base ="",
    api_version ="",
    messages =[{"role":"user","content":"good morning"}],
)
```

## **Azure Batches API**[​](#azure-batches-api "Direct link to azure-batches-api")

PropertyDetailsDescriptionAzure OpenAI Batches API`custom_llm_provider` on LiteLLM`azure/`Supported Operations`/v1/batches`, `/v1/files`Azure OpenAI Batches API[Azure OpenAI Batches API ↗](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/batch)Cost Tracking, Logging Support✅ LiteLLM will log, track cost for Batch API Requests

### Quick Start[​](#quick-start "Direct link to Quick Start")

Just add the azure env vars to your environment.

```
export AZURE_API_KEY=""
export AZURE_API_BASE=""
```

- LiteLLM PROXY Server
- LiteLLM SDK

**1. Upload a File**

- OpenAI Python SDK
- Curl

```
from openai import OpenAI

# Initialize the client
client = OpenAI(
    base_url="http://localhost:4000",
    api_key="your-api-key"
)

batch_input_file = client.files.create(
file=open("mydata.jsonl","rb"),
    purpose="batch",
    extra_headers={"custom-llm-provider":"azure"}
)
file_id = batch_input_file.id
```

**Example File Format**

```
{"custom_id":"task-0","method":"POST","url":"/chat/completions","body":{"model":"REPLACE-WITH-MODEL-DEPLOYMENT-NAME","messages":[{"role":"system","content":"You are an AI assistant that helps people find information."},{"role":"user","content":"When was Microsoft founded?"}]}}
{"custom_id":"task-1","method":"POST","url":"/chat/completions","body":{"model":"REPLACE-WITH-MODEL-DEPLOYMENT-NAME","messages":[{"role":"system","content":"You are an AI assistant that helps people find information."},{"role":"user","content":"When was the first XBOX released?"}]}}
{"custom_id":"task-2","method":"POST","url":"/chat/completions","body":{"model":"REPLACE-WITH-MODEL-DEPLOYMENT-NAME","messages":[{"role":"system","content":"You are an AI assistant that helps people find information."},{"role":"user","content":"What is Altair Basic?"}]}}
```

**2. Create a Batch Request**

- OpenAI Python SDK
- Curl

```
batch = client.batches.create(# re use client from above
    input_file_id=file_id,
    endpoint="/v1/chat/completions",
    completion_window="24h",
    metadata={"description":"My batch job"},
    extra_headers={"custom-llm-provider":"azure"}
)
```

**3. Retrieve a Batch**

- OpenAI Python SDK
- Curl

```
retrieved_batch = client.batches.retrieve(
    batch.id,
    extra_headers={"custom-llm-provider":"azure"}
)
```

**4. Cancel a Batch**

- OpenAI Python SDK
- Curl

```
cancelled_batch = client.batches.cancel(
    batch.id,
    extra_headers={"custom-llm-provider":"azure"}
)
```

**5. List Batches**

- OpenAI Python SDK
- Curl

```
client.batches.list(extra_headers={"custom-llm-provider":"azure"})
```

### [Health Check Azure Batch models](https://docs.litellm.ai/docs/providers/azure/proxy/health.md#batch-models-azure-only)[​](#health-check-azure-batch-models "Direct link to health-check-azure-batch-models")

### \[BETA] Loadbalance Multiple Azure Deployments[​](#beta-loadbalance-multiple-azure-deployments "Direct link to [BETA] Loadbalance Multiple Azure Deployments")

In your config.yaml, set `enable_loadbalancing_on_batch_endpoints: true`

```
model_list:
-model_name:"batch-gpt-4o-mini"
litellm_params:
model:"azure/gpt-4o-mini"
api_key: os.environ/AZURE_API_KEY
api_base: os.environ/AZURE_API_BASE
model_info:
mode: batch

litellm_settings:
enable_loadbalancing_on_batch_endpoints:true# 👈 KEY CHANGE
```

Note: This works on `{PROXY_BASE_URL}/v1/files` and `{PROXY_BASE_URL}/v1/batches`. Note: Response is in the OpenAI-format.

1. Upload a file

Just set `model: batch-gpt-4o-mini` in your .jsonl.

```
curl http://localhost:4000/v1/files \
    -H "Authorization: Bearer sk-1234" \
    -F purpose="batch" \
    -F file="@mydata.jsonl"
```

**Example File**

Note: `model` should be your azure deployment name.

```
{"custom_id":"task-0","method":"POST","url":"/chat/completions","body":{"model":"batch-gpt-4o-mini","messages":[{"role":"system","content":"You are an AI assistant that helps people find information."},{"role":"user","content":"When was Microsoft founded?"}]}}
{"custom_id":"task-1","method":"POST","url":"/chat/completions","body":{"model":"batch-gpt-4o-mini","messages":[{"role":"system","content":"You are an AI assistant that helps people find information."},{"role":"user","content":"When was the first XBOX released?"}]}}
{"custom_id":"task-2","method":"POST","url":"/chat/completions","body":{"model":"batch-gpt-4o-mini","messages":[{"role":"system","content":"You are an AI assistant that helps people find information."},{"role":"user","content":"What is Altair Basic?"}]}}
```

Expected Response (OpenAI-compatible)

```
{"id":"file-f0be81f654454113a922da60acb0eea6",...}
```

2. Create a batch

```
curl http://0.0.0.0:4000/v1/batches \
  -H "Authorization: Bearer $LITELLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input_file_id": "file-f0be81f654454113a922da60acb0eea6",
    "endpoint": "/v1/chat/completions",
    "completion_window": "24h",
    "model: "batch-gpt-4o-mini"
  }'
```

Expected Response:

```
{"id":"batch_94e43f0a-d805-477d-adf9-bbb9c50910ed",...}
```

3. Retrieve a batch

```
curl http://0.0.0.0:4000/v1/batches/batch_94e43f0a-d805-477d-adf9-bbb9c50910ed \
  -H "Authorization: Bearer $LITELLM_API_KEY" \
  -H "Content-Type: application/json" \
```

Expected Response:

```
{"id":"batch_94e43f0a-d805-477d-adf9-bbb9c50910ed",...}
```

4. List batch

```
curl http://0.0.0.0:4000/v1/batches?limit=2 \
  -H "Authorization: Bearer $LITELLM_API_KEY" \
  -H "Content-Type: application/json"
```

Expected Response:

```
{"data":[{"id":"batch_R3V...}
```

## Advanced[​](#advanced "Direct link to Advanced")

### Azure API Load-Balancing[​](#azure-api-load-balancing "Direct link to Azure API Load-Balancing")

Use this if you're trying to load-balance across multiple Azure/OpenAI deployments.

`Router` prevents failed requests, by picking the deployment which is below rate-limit and has the least amount of tokens used.

In production, [Router connects to a Redis Cache](#redis-queue) to track usage across multiple deployments.

#### Quick Start[​](#quick-start-1 "Direct link to Quick Start")

```
from litellm import Router

model_list =[{# list of model deployments 
"model_name":"gpt-3.5-turbo",# openai model name 
"litellm_params":{# params for litellm completion/embedding call 
"model":"azure/chatgpt-v-2",
"api_key": os.getenv("AZURE_API_KEY"),
"api_version": os.getenv("AZURE_API_VERSION"),
"api_base": os.getenv("AZURE_API_BASE")
},
"tpm":240000,
"rpm":1800
},{
"model_name":"gpt-3.5-turbo",# openai model name 
"litellm_params":{# params for litellm completion/embedding call 
"model":"azure/chatgpt-functioncalling",
"api_key": os.getenv("AZURE_API_KEY"),
"api_version": os.getenv("AZURE_API_VERSION"),
"api_base": os.getenv("AZURE_API_BASE")
},
"tpm":240000,
"rpm":1800
},{
"model_name":"gpt-3.5-turbo",# openai model name 
"litellm_params":{# params for litellm completion/embedding call 
"model":"gpt-3.5-turbo",
"api_key": os.getenv("OPENAI_API_KEY"),
},
"tpm":1000000,
"rpm":9000
}]

router = Router(model_list=model_list)

# openai.chat.completions.create replacement
response = router.completion(model="gpt-3.5-turbo",
				messages=[{"role":"user","content":"Hey, how's it going?"}]

print(response)
```

#### Redis Queue[​](#redis-queue "Direct link to Redis Queue")

```
router = Router(model_list=model_list,
                redis_host=os.getenv("REDIS_HOST"),
                redis_password=os.getenv("REDIS_PASSWORD"),
                redis_port=os.getenv("REDIS_PORT"))

print(response)
```

### Tool Calling / Function Calling[​](#tool-calling--function-calling "Direct link to Tool Calling / Function Calling")

See a detailed walthrough of parallel function calling with litellm [here](https://docs.litellm.ai/docs/completion/function_call)

- SDK
- PROXY

```
# set Azure env variables
import os
import litellm
import json

os.environ['AZURE_API_KEY']=""# litellm reads AZURE_API_KEY from .env and sends the request
os.environ['AZURE_API_BASE']="https://openai-gpt-4-test-v-1.openai.azure.com/"
os.environ['AZURE_API_VERSION']="2023-07-01-preview"

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
},
}
]

response = litellm.completion(
    model="azure/chatgpt-functioncalling",# model = azure/<your-azure-deployment-name>
    messages=[{"role":"user","content":"What's the weather like in San Francisco, Tokyo, and Paris?"}],
    tools=tools,
    tool_choice="auto",# auto is default, but we'll be explicit
)
print("\nLLM Response1:\n", response)
response_message = response.choices[0].message
tool_calls = response.choices[0].message.tool_calls
print("\nTool Choice:\n", tool_calls)
```

### Spend Tracking for Azure OpenAI Models (PROXY)[​](#spend-tracking-for-azure-openai-models-proxy "Direct link to Spend Tracking for Azure OpenAI Models (PROXY)")

Set base model for cost tracking azure image-gen call

#### Image Generation[​](#image-generation "Direct link to Image Generation")

```
model_list:
-model_name: dall-e-3
litellm_params:
model: azure/dall-e-3-test
api_version: 2023-06-01-preview
api_base: https://openai-gpt-4-test-v-1.openai.azure.com/
api_key: os.environ/AZURE_API_KEY
base_model: dall-e-3# 👈 set dall-e-3 as base model
model_info:
mode: image_generation
```

#### Chat Completions / Embeddings[​](#chat-completions--embeddings "Direct link to Chat Completions / Embeddings")

**Problem**: Azure returns `gpt-4` in the response when `azure/gpt-4-1106-preview` is used. This leads to inaccurate cost tracking

**Solution** ✅ : Set `base_model` on your config so litellm uses the correct model for calculating azure cost

Get the base model name from [here](https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json)

Example config with `base_model`

```
model_list:
-model_name: azure-gpt-3.5
litellm_params:
model: azure/chatgpt-v-2
api_base: os.environ/AZURE_API_BASE
api_key: os.environ/AZURE_API_KEY
api_version:"2023-07-01-preview"
model_info:
base_model: azure/gpt-4-1106-preview
```