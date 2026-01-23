---
title: OpenAI Passthrough | liteLLM
url: https://docs.litellm.ai/docs/pass_through/openai_passthrough
source: sitemap
fetched_at: 2026-01-21T19:46:56.498784047-03:00
rendered_js: false
word_count: 114
summary: This document explains how to use LiteLLM's pass-through endpoints to access newer OpenAI features like the Assistants API by routing requests through the LiteLLM proxy.
tags:
    - litellm
    - openai-api
    - assistants-api
    - proxy-configuration
    - pass-through
category: guide
---

Pass-through endpoints for `/openai`

## Overview[​](#overview "Direct link to Overview")

FeatureSupportedNotesCost Tracking❌Not supportedLogging✅Works across all integrationsStreaming✅Fully supported

### When to use this?[​](#when-to-use-this "Direct link to When to use this?")

- For 90% of your use cases, you should use the [native LiteLLM OpenAI Integration](https://docs.litellm.ai/docs/providers/openai) (`/chat/completions`, `/embeddings`, `/completions`, `/images`, `/batches`, etc.)
- Use this passthrough to call less popular or newer OpenAI endpoints that LiteLLM doesn't fully support yet, such as `/assistants`, `/threads`, `/vector_stores`

Simply replace `https://api.openai.com` with `LITELLM_PROXY_BASE_URL/openai`

## Usage Examples[​](#usage-examples "Direct link to Usage Examples")

Requirements: Set `OPENAI_API_KEY` in your environment variables.

### Assistants API[​](#assistants-api "Direct link to Assistants API")

#### Create OpenAI Client[​](#create-openai-client "Direct link to Create OpenAI Client")

Make sure you do the following:

- Point `base_url` to your `LITELLM_PROXY_BASE_URL/openai`
- Use your `LITELLM_API_KEY` as the `api_key`

```
import openai

client = openai.OpenAI(
    base_url="http://0.0.0.0:4000/openai",# <your-proxy-url>/openai
    api_key="sk-anything"# <your-proxy-api-key>
)
```

#### Create an Assistant[​](#create-an-assistant "Direct link to Create an Assistant")

```
# Create an assistant
assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a math tutor. Help solve equations.",
    model="gpt-4o",
)
```

#### Create a Thread[​](#create-a-thread "Direct link to Create a Thread")

```
# Create a thread
thread = client.beta.threads.create()
```

#### Add a Message to the Thread[​](#add-a-message-to-the-thread "Direct link to Add a Message to the Thread")

```
# Add a message
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Solve 3x + 11 = 14",
)
```

#### Run the Assistant[​](#run-the-assistant "Direct link to Run the Assistant")

```
# Create a run to get the assistant's response
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
# List messages after the run completes
messages = client.beta.threads.messages.list(
    thread_id=thread.id
)
```

#### Delete the Assistant[​](#delete-the-assistant "Direct link to Delete the Assistant")

```
# Delete the assistant when done
client.beta.assistants.delete(assistant.id)
```