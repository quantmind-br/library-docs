---
title: LiteLLM Proxy - Locust Load Test | liteLLM
url: https://docs.litellm.ai/docs/load_test
source: sitemap
fetched_at: 2026-01-21T19:45:33.870889569-03:00
rendered_js: false
word_count: 110
summary: This document provides instructions for performing load testing on a LiteLLM Proxy using the Locust framework and a simulated OpenAI endpoint. It covers configuration steps, installation, and how to evaluate response times and health readiness via the Locust web interface.
tags:
    - litellm
    - locust
    - load-testing
    - performance-benchmarking
    - openai-proxy
    - python
category: tutorial
---

## Locust Load Test LiteLLM Proxy[​](#locust-load-test-litellm-proxy "Direct link to Locust Load Test LiteLLM Proxy")

1. Add `fake-openai-endpoint` to your proxy config.yaml and start your litellm proxy litellm provides a free hosted `fake-openai-endpoint` you can load test against

```
model_list:
-model_name: fake-openai-endpoint
litellm_params:
model: openai/fake
api_key: fake-key
api_base: https://exampleopenaiendpoint-production.up.railway.app/
```

2. `pip install locust`
3. Create a file called `locustfile.py` on your local machine. Copy the contents from the litellm load test located [here](https://github.com/BerriAI/litellm/blob/main/.github/workflows/locustfile.py)
4. Start locust Run `locust` in the same directory as your `locustfile.py` from step 2

Output on terminal

```
[2024-03-15 07:19:58,893] Starting web interface at http://0.0.0.0:8089
[2024-03-15 07:19:58,898] Starting Locust 2.24.0
```

5. Run Load test on locust

Head to the locust UI on [http://0.0.0.0:8089](http://0.0.0.0:8089)

Set Users=100, Ramp Up Users=10, Host=Base URL of your LiteLLM Proxy

6. Expected Results

Expect to see the following response times for `/health/readiness` Median → /health/readiness is `150ms`

Avg → /health/readiness is `219ms`