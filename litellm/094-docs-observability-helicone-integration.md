---
title: Helicone - OSS LLM Observability Platform | liteLLM
url: https://docs.litellm.ai/docs/observability/helicone_integration
source: sitemap
fetched_at: 2026-01-21T19:46:07.809804678-03:00
rendered_js: false
word_count: 17
summary: This document demonstrates how to integrate LiteLLM with Helicone to route requests and configure advanced features such as caching, rate limiting, and custom metadata through headers.
tags:
    - litellm
    - helicone
    - api-integration
    - caching
    - rate-limiting
    - error-handling
    - request-metadata
category: guide
---

```
import os
import litellm
from litellm import completion

os.environ["HELICONE_API_KEY"]=""# your Helicone API key

messages =[{"content":"What is the capital of France?","role":"user"}]

# Helicone call - routes through Helicone gateway to any model
response = completion(
    model="helicone/gpt-4o-mini",# or any 100+ models
    messages=messages
)

print(response)
```

You can add custom metadata and properties to your requests using Helicone headers. Here are some examples:

```
litellm.metadata ={
"Helicone-User-Id":"user-abc",# Specify the user making the request
"Helicone-Property-App":"web",# Custom property to add additional information
"Helicone-Property-Custom":"any-value",# Add any custom property
"Helicone-Prompt-Id":"prompt-supreme-court",# Assign an ID to associate this prompt with future versions
"Helicone-Cache-Enabled":"true",# Enable caching of responses
"Cache-Control":"max-age=3600",# Set cache limit to 1 hour
"Helicone-RateLimit-Policy":"10;w=60;s=user",# Set rate limit policy
"Helicone-Retry-Enabled":"true",# Enable retry mechanism
"helicone-retry-num":"3",# Set number of retries
"helicone-retry-factor":"2",# Set exponential backoff factor
"Helicone-Model-Override":"gpt-3.5-turbo-0613",# Override the model used for cost calculation
"Helicone-Session-Id":"session-abc-123",# Set session ID for tracking
"Helicone-Session-Path":"parent-trace/child-trace",# Set session path for hierarchical tracking
"Helicone-Omit-Response":"false",# Include response in logging (default behavior)
"Helicone-Omit-Request":"false",# Include request in logging (default behavior)
"Helicone-LLM-Security-Enabled":"true",# Enable LLM security features
"Helicone-Moderations-Enabled":"true",# Enable content moderation
}
```

```
litellm.metadata ={
"Helicone-Cache-Enabled":"true",# Enable caching of responses
"Cache-Control":"max-age=3600",# Set cache limit to 1 hour
"Helicone-RateLimit-Policy":"100;w=3600;s=user",# Set rate limit policy
}
```