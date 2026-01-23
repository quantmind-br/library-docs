---
title: Helicone Tutorial | liteLLM
url: https://docs.litellm.ai/observability/helicone_integration
source: sitemap
fetched_at: 2026-01-21T19:41:10.795486736-03:00
rendered_js: false
word_count: 186
summary: This document explains how to integrate LiteLLM with Helicone to monitor and log LLM requests across various providers using success callbacks or proxy configurations.
tags:
    - helicone
    - litellm
    - observability
    - llm-logging
    - callbacks
    - proxy-configuration
category: guide
---

[Helicone](https://helicone.ai/) is an open source observability platform that proxies your OpenAI traffic and provides you key insights into your spend, latency and usage.

## Use Helicone to log requests across all LLM Providers (OpenAI, Azure, Anthropic, Cohere, Replicate, PaLM)[​](#use-helicone-to-log-requests-across-all-llm-providers-openai-azure-anthropic-cohere-replicate-palm "Direct link to Use Helicone to log requests across all LLM Providers (OpenAI, Azure, Anthropic, Cohere, Replicate, PaLM)")

liteLLM provides `success_callbacks` and `failure_callbacks`, making it easy for you to send data to a particular provider depending on the status of your responses.

In this case, we want to log requests to Helicone when a request succeeds.

### Approach 1: Use Callbacks[​](#approach-1-use-callbacks "Direct link to Approach 1: Use Callbacks")

Use just 1 line of code, to instantly log your responses **across all providers** with helicone:

```
litellm.success_callback=["helicone"]
```

Complete code

```
from litellm import completion

## set env variables
os.environ["HELICONE_API_KEY"]="your-helicone-key"
os.environ["OPENAI_API_KEY"], os.environ["COHERE_API_KEY"]="",""

# set callbacks
litellm.success_callback=["helicone"]

#openai call
response = completion(model="gpt-3.5-turbo", messages=[{"role":"user","content":"Hi 👋 - i'm openai"}])

#cohere call
response = completion(model="command-nightly", messages=[{"role":"user","content":"Hi 👋 - i'm cohere"}])
```

### Approach 2: \[OpenAI + Azure only] Use Helicone as a proxy[​](#approach-2-openai--azure-only-use-helicone-as-a-proxy "Direct link to Approach 2: [OpenAI + Azure only] Use Helicone as a proxy")

Helicone provides advanced functionality like caching, etc. Helicone currently supports this for Azure and OpenAI.

If you want to use Helicone to proxy your OpenAI/Azure requests, then you can -

- Set helicone as your base url via: `litellm.api_url`
- Pass in helicone request headers via: `litellm.headers`

Complete Code

```
import litellm
from litellm import completion

litellm.api_base = "https://oai.hconeai.com/v1"
litellm.headers = {"Helicone-Auth": f"Bearer {os.getenv('HELICONE_API_KEY')}"}

response = litellm.completion(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "how does a court case get to the Supreme Court?"}]
)

print(response)
```

- [Use Helicone to log requests across all LLM Providers (OpenAI, Azure, Anthropic, Cohere, Replicate, PaLM)](#use-helicone-to-log-requests-across-all-llm-providers-openai-azure-anthropic-cohere-replicate-palm)
  
  - [Approach 1: Use Callbacks](#approach-1-use-callbacks)
  - [Approach 2: \[OpenAI + Azure only\] Use Helicone as a proxy](#approach-2-openai--azure-only-use-helicone-as-a-proxy)