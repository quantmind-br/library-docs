---
title: Azure Model Router | liteLLM
url: https://docs.litellm.ai/docs/providers/azure_ai/azure_model_router
source: sitemap
fetched_at: 2026-01-21T19:48:11.085902874-03:00
rendered_js: false
word_count: 451
summary: This document explains how to integrate Azure Model Router with LiteLLM, covering configuration via the Python SDK, Proxy server, and Admin UI. It details how to set up automatic model selection, cost tracking, and streaming support for Azure AI Foundry deployments.
tags:
    - azure-model-router
    - litellm
    - azure-ai-foundry
    - model-routing
    - python-sdk
    - api-gateway
    - cost-tracking
category: guide
---

Azure Model Router is a feature in Azure AI Foundry that automatically routes your requests to the best available model based on your requirements. This allows you to use a single endpoint that intelligently selects the optimal model for each request.

## Key Features[​](#key-features "Direct link to Key Features")

- **Automatic Model Selection**: Azure Model Router dynamically selects the best model for your request
- **Cost Tracking**: LiteLLM automatically tracks costs based on the actual model used (e.g., `gpt-4.1-nano`), not the router endpoint
- **Streaming Support**: Full support for streaming responses with accurate cost calculation

## LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

### Basic Usage[​](#basic-usage "Direct link to Basic Usage")

```
import litellm
import os

response = litellm.completion(
    model="azure_ai/azure-model-router",
    messages=[{"role":"user","content":"Hello!"}],
    api_base="https://your-endpoint.cognitiveservices.azure.com/openai/v1/",
    api_key=os.getenv("AZURE_MODEL_ROUTER_API_KEY"),
)

print(response)
```

### Streaming with Usage Tracking[​](#streaming-with-usage-tracking "Direct link to Streaming with Usage Tracking")

```
import litellm
import os

response =await litellm.acompletion(
    model="azure_ai/azure-model-router",
    messages=[{"role":"user","content":"hi"}],
    api_base="https://your-endpoint.cognitiveservices.azure.com/openai/v1/",
    api_key=os.getenv("AZURE_MODEL_ROUTER_API_KEY"),
    stream=True,
    stream_options={"include_usage":True},
)

asyncfor chunk in response:
print(chunk)
```

## LiteLLM Proxy (AI Gateway)[​](#litellm-proxy-ai-gateway "Direct link to LiteLLM Proxy (AI Gateway)")

### config.yaml[​](#configyaml "Direct link to config.yaml")

```
model_list:
-model_name: azure-model-router
litellm_params:
model: azure_ai/azure-model-router
api_base: https://your-endpoint.cognitiveservices.azure.com/openai/v1/
api_key: os.environ/AZURE_MODEL_ROUTER_API_KEY
```

### Start Proxy[​](#start-proxy "Direct link to Start Proxy")

```
litellm --config config.yaml
```

### Test Request[​](#test-request "Direct link to Test Request")

```
curl -X POST http://localhost:4000/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "azure-model-router",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

## Add Azure Model Router via LiteLLM UI[​](#add-azure-model-router-via-litellm-ui "Direct link to Add Azure Model Router via LiteLLM UI")

This walkthrough shows how to add an Azure Model Router endpoint to LiteLLM using the Admin Dashboard.

### Select Provider[​](#select-provider "Direct link to Select Provider")

Navigate to the Models page and select "Azure AI Foundry (Studio)" as the provider.

#### Navigate to Models Page[​](#navigate-to-models-page "Direct link to Navigate to Models Page")

![Navigate to Models](https://docs.litellm.ai/assets/images/azure_model_router_01-46aa80fc7e22d674f29edf087d257477.jpeg)

#### Click Provider Dropdown[​](#click-provider-dropdown "Direct link to Click Provider Dropdown")

![Click Provider](https://docs.litellm.ai/assets/images/azure_model_router_02-1e7dba4a5142e040290c5fdfe4fed86f.jpeg)

#### Choose Azure AI Foundry[​](#choose-azure-ai-foundry "Direct link to Choose Azure AI Foundry")

![Select Azure AI Foundry](https://docs.litellm.ai/assets/images/azure_model_router_03-13867e6e1ac1bdf923d1417dc69c810f.jpeg)

### Configure Model Name[​](#configure-model-name "Direct link to Configure Model Name")

Set up the model name by entering `azure_ai/` followed by your model router deployment name from Azure.

#### Click Model Name Field[​](#click-model-name-field "Direct link to Click Model Name Field")

![Click Model Field](https://docs.litellm.ai/assets/images/azure_model_router_04-413a9f5aee073d351a78402ef93710e1.jpeg)

#### Select Custom Model Name[​](#select-custom-model-name "Direct link to Select Custom Model Name")

![Select Custom Model](https://docs.litellm.ai/assets/images/azure_model_router_05-8128fb119a5120222e443f77c858bb26.jpeg)

#### Enter LiteLLM Model Name[​](#enter-litellm-model-name "Direct link to Enter LiteLLM Model Name")

![LiteLLM Model Name](https://docs.litellm.ai/assets/images/azure_model_router_06-d1ca95899eca543acf1f183edf2fe628.jpeg)

#### Click Custom Model Name Field[​](#click-custom-model-name-field "Direct link to Click Custom Model Name Field")

![Enter Custom Name Field](https://docs.litellm.ai/assets/images/azure_model_router_07-c2480c83f06f656a50cdd60a92f17277.jpeg)

#### Type Model Prefix[​](#type-model-prefix "Direct link to Type Model Prefix")

Type `azure_ai/` as the prefix.

![Type azure_ai prefix](https://docs.litellm.ai/assets/images/azure_model_router_08-40cfc7b2f7757a7d28c46ece4f5e5fa1.jpeg)

#### Copy Model Name from Azure Portal[​](#copy-model-name-from-azure-portal "Direct link to Copy Model Name from Azure Portal")

Switch to Azure AI Foundry and copy your model router deployment name.

![Azure Portal Model Name](https://docs.litellm.ai/assets/images/azure_model_router_09-bd23fe2b51b6aff89d7f146c26cfc1e1.jpeg)

![Copy Model Name](https://docs.litellm.ai/assets/images/azure_model_router_10-3e473ddd0bbd087547dec48be2a09763.jpeg)

#### Paste Model Name[​](#paste-model-name "Direct link to Paste Model Name")

Paste to get `azure_ai/azure-model-router`.

![Paste Model Name](https://docs.litellm.ai/assets/images/azure_model_router_11-48cc37b23e0eecff01118d1135f7cb2e.jpeg)

### Configure API Base and Key[​](#configure-api-base-and-key "Direct link to Configure API Base and Key")

Copy the endpoint URL and API key from Azure portal.

#### Copy API Base URL from Azure[​](#copy-api-base-url-from-azure "Direct link to Copy API Base URL from Azure")

![Copy API Base](https://docs.litellm.ai/assets/images/azure_model_router_12-5776789a3f63960bd329cab180a6a5c7.jpeg)

#### Enter API Base in LiteLLM[​](#enter-api-base-in-litellm "Direct link to Enter API Base in LiteLLM")

![Click API Base Field](https://docs.litellm.ai/assets/images/azure_model_router_13-00f46768c441086ccc0058e30513cf19.jpeg)

![Paste API Base](https://docs.litellm.ai/assets/images/azure_model_router_14-6580a687a8b762da01da087498624860.jpeg)

#### Copy API Key from Azure[​](#copy-api-key-from-azure "Direct link to Copy API Key from Azure")

![Copy API Key](https://docs.litellm.ai/assets/images/azure_model_router_15-91ea00001995c7575728a2640982f990.jpeg)

#### Enter API Key in LiteLLM[​](#enter-api-key-in-litellm "Direct link to Enter API Key in LiteLLM")

![Enter API Key](https://docs.litellm.ai/assets/images/azure_model_router_16-f0c2e59bac0dfe40ad6a54e35278f70d.jpeg)

### Test and Add Model[​](#test-and-add-model "Direct link to Test and Add Model")

Verify your configuration works and save the model.

#### Test Connection[​](#test-connection "Direct link to Test Connection")

![Test Connection](https://docs.litellm.ai/assets/images/azure_model_router_17-dc1ef19ff118fe926139ee0e758c3041.jpeg)

#### Close Test Dialog[​](#close-test-dialog "Direct link to Close Test Dialog")

![Close Dialog](https://docs.litellm.ai/assets/images/azure_model_router_18-7779347db79d6ce4944b6484c7d73e5e.jpeg)

#### Add Model[​](#add-model "Direct link to Add Model")

![Add Model](https://docs.litellm.ai/assets/images/azure_model_router_19-e927be77ba4955d05aa160741d57bb47.jpeg)

### Verify in Playground[​](#verify-in-playground "Direct link to Verify in Playground")

Test your model and verify cost tracking is working.

#### Open Playground[​](#open-playground "Direct link to Open Playground")

![Go to Playground](https://docs.litellm.ai/assets/images/azure_model_router_20-35aa370cab03cddb3ccf298a90b2c184.jpeg)

#### Select Model[​](#select-model "Direct link to Select Model")

![Select Model](https://docs.litellm.ai/assets/images/azure_model_router_21-62d8310814628b966dc0bf5347160834.jpeg)

#### Send Test Message[​](#send-test-message "Direct link to Send Test Message")

![Send Message](https://docs.litellm.ai/assets/images/azure_model_router_22-56a9eb25c8587ec220c4592280ca04e7.jpeg)

#### View Logs[​](#view-logs "Direct link to View Logs")

![View Logs](https://docs.litellm.ai/assets/images/azure_model_router_23-f28793256896febcbfa7619b9ca5f829.jpeg)

#### Verify Cost Tracking[​](#verify-cost-tracking "Direct link to Verify Cost Tracking")

Cost is tracked based on the actual model used (e.g., `gpt-4.1-nano`).

![Verify Cost](https://docs.litellm.ai/assets/images/azure_model_router_24-1e6e728788d447123e5c1486d6125178.jpeg)

## Cost Tracking[​](#cost-tracking "Direct link to Cost Tracking")

LiteLLM automatically handles cost tracking for Azure Model Router by:

1. **Detecting the actual model**: When Azure Model Router routes your request to a specific model (e.g., `gpt-4.1-nano-2025-04-14`), LiteLLM extracts this from the response
2. **Calculating accurate costs**: Costs are calculated based on the actual model used, not the router endpoint name
3. **Streaming support**: Cost tracking works correctly for both streaming and non-streaming requests

### Example Response with Cost[​](#example-response-with-cost "Direct link to Example Response with Cost")

```
import litellm

response = litellm.completion(
    model="azure_ai/azure-model-router",
    messages=[{"role":"user","content":"Hello!"}],
    api_base="https://your-endpoint.cognitiveservices.azure.com/openai/v1/",
    api_key="your-api-key",
)

# The response will show the actual model used
print(f"Model used: {response.model}")# e.g., "gpt-4.1-nano-2025-04-14"

# Get cost
from litellm import completion_cost
cost = completion_cost(completion_response=response)
print(f"Cost: ${cost}")
```