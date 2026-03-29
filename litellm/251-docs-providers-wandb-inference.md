---
title: Weights & Biases Inference | liteLLM
url: https://docs.litellm.ai/docs/providers/wandb_inference
source: sitemap
fetched_at: 2026-01-21T19:50:55.932586953-03:00
rendered_js: false
word_count: 487
summary: This document explains how to integrate LiteLLM with the W&B Inference service to perform text generation and streaming tasks. It provides setup instructions for API authentication, proxy server configuration, and common error resolution.
tags:
    - litellm
    - wandb-inference
    - text-generation
    - streaming
    - api-configuration
    - error-handling
category: guide
---

[https://weave-docs.wandb.ai/quickstart-inference](https://weave-docs.wandb.ai/quickstart-inference)

tip

Litellm provides support to all models from W&B Inference service. To use a model, set `model=wandb/<any-model-on-wandb-inference-dashboard>` as a prefix for litellm requests. The full list of supported models is provided at [https://docs.wandb.ai/guides/inference/models/](https://docs.wandb.ai/guides/inference/models/)

## API Key[​](#api-key "Direct link to API Key")

You can get an API key for W&B Inference at - [https://wandb.ai/authorize](https://wandb.ai/authorize)

```
import os
# env variable
os.environ['WANDB_API_KEY']
```

## Sample Usage: Text Generation[​](#sample-usage-text-generation "Direct link to Sample Usage: Text Generation")

```
from litellm import completion
import os

os.environ['WANDB_API_KEY']="insert-your-wandb-api-key"
response = completion(
    model="wandb/Qwen/Qwen3-235B-A22B-Instruct-2507",
    messages=[
{
"role":"user",
"content":"What character was Wall-e in love with?",
}
],
    max_tokens=10,
    response_format={"type":"json_object"},
    seed=123,
    temperature=0.6,# either set temperature or `top_p`
    top_p=0.01,# to get as deterministic results as possible
)
print(response)
```

## Sample Usage - Streaming[​](#sample-usage---streaming "Direct link to Sample Usage - Streaming")

```
from litellm import completion
import os

os.environ['WANDB_API_KEY']=""
response = completion(
    model="wandb/Qwen/Qwen3-235B-A22B-Instruct-2507",
    messages=[
{
"role":"user",
"content":"What character was Wall-e in love with?",
}
],
    stream=True,
    max_tokens=10,
    response_format={"type":"json_object"},
    seed=123,
    temperature=0.6,# either set temperature or `top_p`
    top_p=0.01,# to get as deterministic results as possible
)

for chunk in response:
print(chunk)
```

## Usage with LiteLLM Proxy Server[​](#usage-with-litellm-proxy-server "Direct link to Usage with LiteLLM Proxy Server")

Here's how to call a W&B Inference model with the LiteLLM Proxy Server

1. Modify the config.yaml

```
model_list:
-model_name: my-model
litellm_params:
model: wandb/<your-model-name># add wandb/ prefix to use W&B Inference as provider
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
    api_key="litellm-proxy-key",# pass litellm proxy key, if you're using virtual keys
    base_url="http://0.0.0.0:4000"# litellm-proxy-base url
)

response = client.chat.completions.create(
    model="my-model",
    messages =[
{
"role":"user",
"content":"What character was Wall-e in love with?"
}
],
)

print(response)
```

## Supported Parameters[​](#supported-parameters "Direct link to Supported Parameters")

The W&B Inference provider supports the following parameters:

### Chat Completion Parameters[​](#chat-completion-parameters "Direct link to Chat Completion Parameters")

ParameterTypeDescriptionfrequency\_penaltynumberPenalizes new tokens based on their frequency in the textfunction\_callstring/objectControls how the model calls functionsfunctionsarrayList of functions for which the model may generate JSON inputslogit\_biasmapModifies the likelihood of specified tokensmax\_tokensintegerMaximum number of tokens to generatenintegerNumber of completions to generatepresence\_penaltynumberPenalizes tokens based on if they appear in the text so farresponse\_formatobjectFormat of the response, e.g., `{"type": "json"}`seedintegerSampling seed for deterministic resultsstopstring/arraySequences where the API will stop generating tokensstreambooleanWhether to stream the responsetemperaturenumberControls randomness (0-2)top\_pnumberControls nucleus sampling

## Error Handling[​](#error-handling "Direct link to Error Handling")

The integration uses the standard LiteLLM error handling. Further, here's a list of commonly encountered errors with the W&B Inference API -

Error CodeMessageCauseSolution401Authentication failedYour authentication credentials are incorrect or your W&B project entity and/or name are incorrect.Ensure you're using the correct API key and that your W&B project name and entity are correct.403Country, region, or territory not supportedAccessing the API from an unsupported location.Please see [Geographic restrictions](https://docs.wandb.ai/guides/inference/usage-limits/#geographic-restrictions)429Concurrency limit reached for requestsToo many concurrent requests.Reduce the number of concurrent requests or increase your limits. For more information, see [Usage information and limits](https://docs.wandb.ai/guides/inference/usage-limits/).429You exceeded your current quota, please check your plan and billing detailsOut of credits or reached monthly spending cap.Get more credits or increase your limits. For more information, see [Usage information and limits](https://docs.wandb.ai/guides/inference/usage-limits/).429W&B Inference isn't available for personal accounts.Switch to a non-personal account.Follow [the instructions below](#error-429-personal-entities-unsupported) for a work around.500The server had an error while processing your requestInternal server error.Retry after a brief wait and contact support if it persists.503The engine is currently overloaded, please try again laterServer is experiencing high traffic.Retry your request after a short delay.

### Error 429: Personal entities unsupported[​](#error-429-personal-entities-unsupported "Direct link to Error 429: Personal entities unsupported")

The user is on a personal account, which doesn't have access to W&B Inference. If one isn't available, create a Team to create a non-personal account.

Once done, add the `openai-project` header to your request as shown below:

```
response = completion(
    model="...",
    extra_headers={"openai-project":"team_name/project_name"},
...
```

For more information, see [Personal entities unsupported](https://docs.wandb.ai/guides/inference/usage-limits/#personal-entities-unsupported).

You can find more ways of using custom headers with LiteLLM here - [https://docs.litellm.ai/docs/proxy/request\_headers](https://docs.litellm.ai/docs/proxy/request_headers).