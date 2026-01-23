---
title: Response Headers | liteLLM
url: https://docs.litellm.ai/docs/proxy/response_headers
source: sitemap
fetched_at: 2026-01-21T19:53:32.569350377-03:00
rendered_js: false
word_count: 315
summary: This document outlines the standard and custom HTTP response headers returned by the LiteLLM proxy, detailing information on rate limits, latency, cost tracking, and retries.
tags:
    - litellm
    - response-headers
    - rate-limiting
    - api-latency
    - cost-tracking
    - error-handling
    - proxy-metadata
category: reference
---

When you make a request to the proxy, the proxy will return the following headers:

## Rate Limit Headers[​](#rate-limit-headers "Direct link to Rate Limit Headers")

[OpenAI-compatible headers](https://platform.openai.com/docs/guides/rate-limits/rate-limits-in-headers):

HeaderTypeDescription`x-ratelimit-remaining-requests`Optional\[int]The remaining number of requests that are permitted before exhausting the rate limit`x-ratelimit-remaining-tokens`Optional\[int]The remaining number of tokens that are permitted before exhausting the rate limit`x-ratelimit-limit-requests`Optional\[int]The maximum number of requests that are permitted before exhausting the rate limit`x-ratelimit-limit-tokens`Optional\[int]The maximum number of tokens that are permitted before exhausting the rate limit`x-ratelimit-reset-requests`Optional\[int]The time at which the rate limit will reset`x-ratelimit-reset-tokens`Optional\[int]The time at which the rate limit will reset

### How Rate Limit Headers work[​](#how-rate-limit-headers-work "Direct link to How Rate Limit Headers work")

**If key has rate limits set**

The proxy will return the [remaining rate limits for that key](https://github.com/BerriAI/litellm/blob/bfa95538190575f7f317db2d9598fc9a82275492/litellm/proxy/hooks/parallel_request_limiter.py#L778).

**If key does not have rate limits set**

The proxy returns the remaining requests/tokens returned by the backend provider. (LiteLLM will standardize the backend provider's response headers to match the OpenAI format)

If the backend provider does not return these headers, the value will be `None`.

These headers are useful for clients to understand the current rate limit status and adjust their request rate accordingly.

## Latency Headers[​](#latency-headers "Direct link to Latency Headers")

HeaderTypeDescription`x-litellm-response-duration-ms`floatTotal duration from the moment that a request gets to LiteLLM Proxy to the moment it gets returned to the client.`x-litellm-overhead-duration-ms`floatLiteLLM processing overhead in milliseconds

## Retry, Fallback Headers[​](#retry-fallback-headers "Direct link to Retry, Fallback Headers")

HeaderTypeDescription`x-litellm-attempted-retries`intNumber of retry attempts made`x-litellm-attempted-fallbacks`intNumber of fallback attempts made`x-litellm-max-fallbacks`intMaximum number of fallback attempts allowed

## Cost Tracking Headers[​](#cost-tracking-headers "Direct link to Cost Tracking Headers")

HeaderTypeDescriptionAvailable on Pass-Through Endpoints`x-litellm-response-cost`floatCost of the API call`x-litellm-key-spend`floatTotal spend for the API key✅

## LiteLLM Specific Headers[​](#litellm-specific-headers "Direct link to LiteLLM Specific Headers")

HeaderTypeDescriptionAvailable on Pass-Through Endpoints`x-litellm-call-id`stringUnique identifier for the API call✅`x-litellm-model-id`stringUnique identifier for the model used`x-litellm-model-api-base`stringBase URL of the API endpoint✅`x-litellm-version`stringVersion of LiteLLM being used`x-litellm-model-group`stringModel group identifier

## Response headers from LLM providers[​](#response-headers-from-llm-providers "Direct link to Response headers from LLM providers")

LiteLLM also returns the original response headers from the LLM provider. These headers are prefixed with `llm_provider-` to distinguish them from LiteLLM's headers.

Example response headers:

```
llm_provider-openai-processing-ms: 256
llm_provider-openai-version: 2020-10-01
llm_provider-x-ratelimit-limit-requests: 30000
llm_provider-x-ratelimit-limit-tokens: 150000000
```

- [Rate Limit Headers](#rate-limit-headers)
  
  - [How Rate Limit Headers work](#how-rate-limit-headers-work)
- [Latency Headers](#latency-headers)
- [Retry, Fallback Headers](#retry-fallback-headers)
- [Cost Tracking Headers](#cost-tracking-headers)
- [LiteLLM Specific Headers](#litellm-specific-headers)
- [Response headers from LLM providers](#response-headers-from-llm-providers)