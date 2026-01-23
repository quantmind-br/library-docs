---
title: LiteLLM v1.71.1 Benchmarks | liteLLM
url: https://docs.litellm.ai/docs/aiohttp_benchmarks
source: sitemap
fetched_at: 2026-01-21T19:44:00.25769849-03:00
rendered_js: false
word_count: 172
summary: This document provides performance benchmark results for LiteLLM v1.71.1, comparing the efficiency of the new aiohttp transport layer against the legacy httpx implementation.
tags:
    - litellm
    - performance-benchmarks
    - aiohttp
    - load-testing
    - latency-reduction
    - httpx
category: reference
---

## Overview[​](#overview "Direct link to Overview")

This document presents performance benchmarks comparing LiteLLM's v1.71.1 to prior litellm versions.

**Related PR:** [#11097](https://github.com/BerriAI/litellm/pull/11097)

## Testing Methodology[​](#testing-methodology "Direct link to Testing Methodology")

The load testing was conducted using the following parameters:

- **Request Rate:** 200 RPS (Requests Per Second)
- **User Ramp Up:** 200 concurrent users
- **Transport Comparison:** httpx (existing) vs aiohttp (new implementation)
- **Number of pods/instance of litellm:** 1
- **Machine Specs:** 2 vCPUs, 4GB RAM
- **LiteLLM Settings:**
  
  - Tested against a [fake openai endpoint](https://exampleopenaiendpoint-production.up.railway.app/)
  - Set `USE_AIOHTTP_TRANSPORT="True"` in the environment variables. This feature flag enables the aiohttp transport.

## Benchmark Results[​](#benchmark-results "Direct link to Benchmark Results")

Metrichttpx (Existing)aiohttp (LiteLLM v1.71.1)ImprovementCalculation**RPS**50.2224**+346%** ✅(224 - 50.2) / 50.2 × 100 = 346%**Median Latency**2,500ms74ms**-97%** ✅(74 - 2500) / 2500 × 100 = -97%**95th Percentile**5,600ms250ms**-96%** ✅(250 - 5600) / 5600 × 100 = -96%**99th Percentile**6,200ms330ms**-95%** ✅(330 - 6200) / 6200 × 100 = -95%

## Key Improvements[​](#key-improvements "Direct link to Key Improvements")

- **4.5x increase** in requests per second (from 50.2 to 224 RPS)
- **97% reduction** in median response time (from 2.5 seconds to 74ms)
- **96% reduction** in 95th percentile latency (from 5.6 seconds to 250ms)
- **95% reduction** in 99th percentile latency (from 6.2 seconds to 330ms)