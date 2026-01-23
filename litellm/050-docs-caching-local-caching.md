---
title: LiteLLM - Local Caching | liteLLM
url: https://docs.litellm.ai/docs/caching/local_caching
source: sitemap
fetched_at: 2026-01-21T19:44:16.878898057-03:00
rendered_js: false
word_count: 93
summary: This document explains how to implement and configure caching for completion and embedding calls in LiteLLM using in-memory or Redis backends.
tags:
    - litellm
    - caching
    - redis
    - completion-api
    - embeddings
    - streaming
category: guide
---

## Caching `completion()` and `embedding()` calls when switched on[​](#caching-completion-and-embedding-calls-when-switched-on "Direct link to caching-completion-and-embedding-calls-when-switched-on")

liteLLM implements exact match caching and supports the following Caching:

- In-Memory Caching \[Default]
- Redis Caching Local
- Redis Caching Hosted

## Quick Start Usage - Completion[​](#quick-start-usage---completion "Direct link to Quick Start Usage - Completion")

Caching - cache Keys in the cache are `model`, the following example will lead to a cache hit

```
import litellm
from litellm import completion
from litellm.caching.caching import Cache
litellm.cache = Cache()

# Make completion calls
response1 = completion(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":"Tell me a joke."}]
    caching=True
)
response2 = completion(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":"Tell me a joke."}],
    caching=True
)

# response1 == response2, response 1 is cached
```

## Custom Key-Value Pairs[​](#custom-key-value-pairs "Direct link to Custom Key-Value Pairs")

Add custom key-value pairs to your cache.

```
from litellm.caching.caching import Cache
cache = Cache()

cache.add_cache(cache_key="test-key", result="1234")

cache.get_cache(cache_key="test-key")
```

## Caching with Streaming[​](#caching-with-streaming "Direct link to Caching with Streaming")

LiteLLM can cache your streamed responses for you

### Usage[​](#usage "Direct link to Usage")

```
import litellm
from litellm import completion
from litellm.caching.caching import Cache
litellm.cache = Cache()

# Make completion calls
response1 = completion(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":"Tell me a joke."}],
    stream=True,
    caching=True)
for chunk in response1:
print(chunk)
response2 = completion(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":"Tell me a joke."}],
    stream=True,
    caching=True)
for chunk in response2:
print(chunk)
```

## Usage - Embedding()[​](#usage---embedding "Direct link to Usage - Embedding()")

1. Caching - cache Keys in the cache are `model`, the following example will lead to a cache hit

```
import time
import litellm
from litellm import embedding
from litellm.caching.caching import Cache
litellm.cache = Cache()

start_time = time.time()
embedding1 = embedding(model="text-embedding-ada-002",input=["hello from litellm"*5], caching=True)
end_time = time.time()
print(f"Embedding 1 response time: {end_time - start_time} seconds")

start_time = time.time()
embedding2 = embedding(model="text-embedding-ada-002",input=["hello from litellm"*5], caching=True)
end_time = time.time()
print(f"Embedding 2 response time: {end_time - start_time} seconds")
```