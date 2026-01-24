---
title: Azure OpenAI · Cloudflare AI Gateway docs
url: https://developers.cloudflare.com/ai-gateway/usage/providers/azureopenai/index.md
source: llms
fetched_at: 2026-01-24T14:03:01.571304053-03:00
rendered_js: false
word_count: 126
summary: This document provides instructions and endpoint details for routing Azure OpenAI requests through Cloudflare AI Gateway.
tags:
    - cloudflare-ai-gateway
    - azure-openai
    - api-integration
    - endpoint-configuration
    - openai-sdk
category: configuration
---

[Azure OpenAI](https://azure.microsoft.com/en-gb/products/ai-services/openai-service/) allows you apply natural language algorithms on your data.

## Endpoint

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/azure-openai/{resource_name}/{deployment_name}
```

## Prerequisites

When making requests to Azure OpenAI, you will need:

* AI Gateway account ID
* AI Gateway gateway name
* Azure OpenAI API key
* Azure OpenAI resource name
* Azure OpenAI deployment name (aka model name)

## URL structure

Your new base URL will use the data above in this structure: `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/azure-openai/{resource_name}/{deployment_name}`. Then, you can append your endpoint and api-version at the end of the base URL, like `.../chat/completions?api-version=2023-05-15`.

## Examples

### cURL

```bash
curl 'https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway}/azure-openai/{resource_name}/{deployment_name}/chat/completions?api-version=2023-05-15' \
  --header 'Content-Type: application/json' \
  --header 'api-key: {azure_api_key}' \
  --data '{
  "messages": [
    {
      "role": "user",
      "content": "What is Cloudflare?"
    }
  ]
}'
```

### Use `openai` JavaScript SDK

```js
import { AzureOpenAI } from "openai";


const azure_openai = new AzureOpenAI({
  apiKey: "{azure_api_key}",
  baseURL: `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway}/azure-openai/{resource_name}/`,
  apiVersion: "2023-05-15",
  defaultHeaders: { "cf-aig-authorization": "{cf-api-token}" }, // if authenticated
});


const result = await azure_openai.chat.completions.create({
  model: '{deployment_name}',
  messages: [{ role: "user", content: "Hello" }],
});
```