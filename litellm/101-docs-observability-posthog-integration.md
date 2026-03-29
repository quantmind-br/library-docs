---
title: PostHog - Tracking LLM Usage Analytics | liteLLM
url: https://docs.litellm.ai/docs/observability/posthog_integration
source: sitemap
fetched_at: 2026-01-21T19:46:26.858865343-03:00
rendered_js: false
word_count: 377
summary: This document explains how to integrate PostHog with LiteLLM to track and analyze LLM application metrics, usage, and performance through both the Python SDK and Proxy gateway.
tags:
    - posthog
    - litellm
    - product-analytics
    - observability
    - llm-monitoring
    - logging-callbacks
category: guide
---

## What is PostHog?[​](#what-is-posthog "Direct link to What is PostHog?")

PostHog is an open-source product analytics platform that helps you track and analyze how users interact with your product. For LLM applications, PostHog provides specialized AI features to track model usage, performance, and user interactions with your AI features.

## Usage with LiteLLM Proxy (LLM Gateway)[​](#usage-with-litellm-proxy-llm-gateway "Direct link to Usage with LiteLLM Proxy (LLM Gateway)")

**Step 1**: Create a `config.yaml` file and set `litellm_settings`: `success_callback`

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: gpt-3.5-turbo

litellm_settings:
success_callback:["posthog"]
failure_callback:["posthog"]
```

**Step 2**: Set required environment variables

```
export POSTHOG_API_KEY="your-posthog-api-key"
# Optional, defaults to https://app.posthog.com
export POSTHOG_API_URL="https://app.posthog.com" # optional
```

**Step 3**: Start the proxy, make a test request

Start proxy

```
litellm --config config.yaml --debug
```

Test Request

```
curl --location 'http://0.0.0.0:4000/chat/completions' \
    --header 'Content-Type: application/json' \
    --data '{
    "model": "gpt-3.5-turbo",
    "messages": [
        {
        "role": "user",
        "content": "what llm are you"
        }
    ],
    "metadata": {
        "user_id": "user-123",
        "custom_field": "custom_value"
    }
}'
```

### Team-Based Logging[​](#team-based-logging "Direct link to Team-Based Logging")

Configure different PostHog credentials per team using the team callback settings:

```
curl -X POST 'http://localhost:4000/team/{team_id}/callback' \
  -H 'Authorization: Bearer sk-1234' \
  -H 'Content-Type: application/json' \
  -d '{
    "callback_name": "posthog",
    "callback_type": "success",
    "callback_vars": {
      "posthog_api_key": "ph_team_specific_key",
      "posthog_api_url": "https://custom.posthog.com"
    }
  }'
```

Now all requests from that team will be logged to their specific PostHog project.

## Usage with LiteLLM Python SDK[​](#usage-with-litellm-python-sdk "Direct link to Usage with LiteLLM Python SDK")

### Quick Start[​](#quick-start "Direct link to Quick Start")

Use just 2 lines of code, to instantly log your responses **across all providers** with PostHog:

```
litellm.success_callback =["posthog"]
litellm.failure_callback =["posthog"]# logs errors to posthog
```

```
import litellm
import os

# from PostHog
os.environ["POSTHOG_API_KEY"]=""
# Optional, defaults to https://app.posthog.com
os.environ["POSTHOG_API_URL"]=""# optional

# LLM API Keys
os.environ['OPENAI_API_KEY']=""

# set posthog as a callback, litellm will send the data to posthog
litellm.success_callback =["posthog"]

# openai call
response = litellm.completion(
    model="gpt-3.5-turbo",
    messages=[
{"role":"user","content":"Hi - i'm openai"}
],
    metadata ={
"user_id":"user-123",# set posthog user ID
}
)
```

### Advanced[​](#advanced "Direct link to Advanced")

#### Set User ID and Custom Metadata[​](#set-user-id-and-custom-metadata "Direct link to Set User ID and Custom Metadata")

Pass `user_id` in `metadata` to associate events with specific users in PostHog:

**With LiteLLM Python SDK:**

```
import litellm

litellm.success_callback =["posthog"]

response = litellm.completion(
    model="gpt-3.5-turbo",
    messages=[
{"role":"user","content":"Hello world"}
],
    metadata={
"user_id":"user-123",# Add user ID for PostHog tracking
"custom_field":"custom_value"# Add custom metadata
}
)
```

**With LiteLLM Proxy using OpenAI Python SDK:**

```
import openai

client = openai.OpenAI(
    api_key="sk-1234",# Your LiteLLM Proxy API key
    base_url="http://0.0.0.0:4000"# Your LiteLLM Proxy URL
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
{"role":"user","content":"Hello world"}
],
    extra_body={
"metadata":{
"user_id":"user-123",# Add user ID for PostHog tracking
"project_name":"my-project",# Add custom metadata
"environment":"production"
}
}
)
```

#### Per-Request Credentials[​](#per-request-credentials "Direct link to Per-Request Credentials")

You can override PostHog credentials on a per-request basis:

```
import litellm

litellm.success_callback =["posthog"]

# Use custom PostHog credentials for this specific request
response = litellm.completion(
    model="gpt-3.5-turbo",
    messages=[
{"role":"user","content":"Hello world"}
],
    posthog_api_key="ph_custom_project_key",
    posthog_api_url="https://custom.posthog.com"
)
```

This is useful when you need to:

- Log different teams/projects to separate PostHog instances
- Use different PostHog projects for staging vs production
- Route logs based on customer or tenant

#### Disable Logging for Specific Calls[​](#disable-logging-for-specific-calls "Direct link to Disable Logging for Specific Calls")

Use the `no-log` flag to prevent logging for specific calls:

```
import litellm

litellm.success_callback =["posthog"]

response = litellm.completion(
    model="gpt-3.5-turbo",
    messages=[
{"role":"user","content":"This won't be logged"}
],
    metadata={"no-log":True}
)
```

## What's Logged to PostHog?[​](#whats-logged-to-posthog "Direct link to What's Logged to PostHog?")

When LiteLLM logs to PostHog, it captures detailed information about your LLM usage:

### For Completion Calls[​](#for-completion-calls "Direct link to For Completion Calls")

- **Model Information**: Provider, model name, model parameters
- **Usage Metrics**: Input tokens, output tokens, total cost
- **Performance**: Latency, completion time
- **Content**: Input messages, model responses (respects privacy settings)
- **Metadata**: Custom fields, user ID, trace information

### For Embedding Calls[​](#for-embedding-calls "Direct link to For Embedding Calls")

- **Model Information**: Provider, model name
- **Usage Metrics**: Input tokens, total cost
- **Performance**: Latency
- **Content**: Input text (respects privacy settings)
- **Metadata**: Custom fields, user ID, trace information

### For Errors[​](#for-errors "Direct link to For Errors")

- **Error Details**: Error type, error message, stack trace
- **Context**: Model, provider, input that caused the error
- **Timing**: When the error occurred, request duration

## Environment Variables[​](#environment-variables "Direct link to Environment Variables")

VariableRequiredDescription`POSTHOG_API_KEY`YesYour PostHog project API key`POSTHOG_API_URL`NoPostHog API URL (defaults to [https://app.posthog.com](https://app.posthog.com))

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### 1. Missing API Key[​](#1-missing-api-key "Direct link to 1. Missing API Key")

```
Error: POSTHOG_API_KEY is not set
```

Set your PostHog API key:

```
import os
os.environ["POSTHOG_API_KEY"]="your-api-key"
```

### 2. Custom PostHog Instance[​](#2-custom-posthog-instance "Direct link to 2. Custom PostHog Instance")

If you're using a self-hosted PostHog instance:

```
import os
os.environ["POSTHOG_API_URL"]="https://your-posthog-instance.com"
```

### 3. Events Not Appearing[​](#3-events-not-appearing "Direct link to 3. Events Not Appearing")

- Check that your API key is correct
- Verify network connectivity to PostHog
- Events may take a few minutes to appear in PostHog dashboard