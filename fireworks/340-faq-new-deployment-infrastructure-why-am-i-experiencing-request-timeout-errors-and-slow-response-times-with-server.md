---
title: Why am I experiencing request timeout errors and slow response times with serverless LLM models? - Fireworks AI Docs
url: https://docs.fireworks.ai/faq-new/deployment-infrastructure/why-am-i-experiencing-request-timeout-errors-and-slow-response-times-with-server
source: sitemap
fetched_at: 2026-04-27T20:12:52.586377116-03:00
rendered_js: false
word_count: 183
summary: This document explains the performance challenges associated with serverless deployment, particularly during high traffic, and outlines recommended solutions like using on-demand deployments while also providing tips for further optimization.
tags:
    - serverless-performance
    - timeout-errors
    - on-demand
    - generative-ai
    - latency-variability
    - response-times
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Why am I experiencing request timeout errors and slow response times with serverless models?

Timeout errors and slow response times occur due to **server load during high-traffic periods**. Serverless users share a pool of GPUs with pre-provisioned models, which allows seamless access to the latest models in minimal code. However, this shared model introduces **minor latency and performance variability** during high-volume periods. With on-demand deployments, users reserve dedicated GPUs billed by rented time instead of usage volume.

## Solution: Use on-demand deployments

- **Guaranteed response times**
- **Dedicated resources** ensure availability
- **No concern about traffic spikes**

## Upcoming improvements

- Enhanced SLAs for uptime
- More consistent generation speeds during peak load times

## Support request details

If you experience persistent issues, include:

1. Exact **model name**
2. **Timestamp** of errors (in UTC)
3. **Frequency** of timeouts
4. **Average wait times**

## Performance optimization tips

- Consider **batch processing** for bulk requests
- Implement **retry logic with exponential backoff**
- Monitor **usage patterns** to identify peak traffic times
- Set **appropriate timeout settings** based on model complexity

#serverless-performance #timeout-errors #on-demand #latency-variability
