---
title: Azure Passthrough | liteLLM
url: https://docs.litellm.ai/docs/pass_through/azure_passthrough
source: sitemap
fetched_at: 2026-01-21T19:46:49.651876351-03:00
rendered_js: false
word_count: 111
summary: This document explains how to use LiteLLM pass-through endpoints to access Azure OpenAI features not yet natively supported, such as the Assistants and Threads APIs.
tags:
    - litellm
    - azure-openai
    - pass-through
    - assistants-api
    - proxy-server
    - api-gateway
category: guide
---

Pass-through endpoints for `/azure`

## Overview[​](#overview "Direct link to Overview")

FeatureSupportedNotesCost Tracking❌Not supportedLogging✅Works across all integrationsStreaming✅Fully supported

### When to use this?[​](#when-to-use-this "Direct link to When to use this?")

- For most use cases, you should use the [native LiteLLM Azure OpenAI Integration](https://docs.litellm.ai/docs/providers/azure/azure) (`/chat/completions`, `/embeddings`, `/completions`, `/images`, etc.)
- Use this passthrough to call newer or less common Azure OpenAI endpoints that LiteLLM doesn't fully support yet, such as `/assistants`, `/threads`, `/vector_stores`

Simply replace your Azure endpoint (e.g. `https://<your-resource-name>.openai.azure.com`) with `LITELLM_PROXY_BASE_URL/azure`

## Usage Examples[​](#usage-examples "Direct link to Usage Examples")

### Assistants API[​](#assistants-api "Direct link to Assistants API")

#### Create Azure OpenAI Client[​](#create-azure-openai-client "Direct link to Create Azure OpenAI Client")

Make sure you do the following:

- Point `azure_endpoint` to your `LITELLM_PROXY_BASE_URL/azure`
- Use your `LITELLM_API_KEY` as the `api_key`

```
import openai

client = openai.AzureOpenAI(
    azure_endpoint="http://0.0.0.0:4000/azure",# <your-proxy-url>/azure
    api_key="sk-anything",# <your-proxy-api-key>
    api_version="2024-05-01-preview"# required Azure API version
)
```

#### Create an Assistant[​](#create-an-assistant "Direct link to Create an Assistant")

```
assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a math tutor. Help solve equations.",
    model="gpt-4o",
)
```

#### Create a Thread[​](#create-a-thread "Direct link to Create a Thread")

```
thread = client.beta.threads.create()
```

#### Add a Message to the Thread[​](#add-a-message-to-the-thread "Direct link to Add a Message to the Thread")

```
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Solve 3x + 11 = 14",
)
```

#### Run the Assistant[​](#run-the-assistant "Direct link to Run the Assistant")

```
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
)

# Check run status
run_status = client.beta.threads.runs.retrieve(
    thread_id=thread.id,
    run_id=run.id
)
```

#### Retrieve Messages[​](#retrieve-messages "Direct link to Retrieve Messages")

```
messages = client.beta.threads.messages.list(
    thread_id=thread.id
)
```

#### Delete the Assistant[​](#delete-the-assistant "Direct link to Delete the Assistant")

```
client.beta.assistants.delete(assistant.id)
```