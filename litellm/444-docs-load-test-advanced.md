---
title: LiteLLM Proxy - 1K RPS Load test on locust | liteLLM
url: https://docs.litellm.ai/docs/load_test_advanced
source: sitemap
fetched_at: 2026-01-21T19:45:34.02511847-03:00
rendered_js: false
word_count: 38
summary: This document provides instructions and a code example for performing load tests on LLM deployments using the Locust framework to measure throughput and API performance.
tags:
    - load-testing
    - llm-performance
    - locust
    - api-benchmarking
    - chat-completions
category: tutorial
---

**Note:** we're currently migrating to aiohttp which has 10x higher throughput. We recommend using the `openai/` provider for load testing.

Run a load test on 2 LLM deployments each with 10K RPM Quota. Expect to see ~20K RPM

```
import os
import uuid
from locust import HttpUser, task, between

classMyUser(HttpUser):
    wait_time = between(0.5,1)# Random wait time between requests

@task(100)
deflitellm_completion(self):
# no cache hits with this
        payload ={
"model":"fake-openai-endpoint",
"messages":[{"role":"user","content":f"{uuid.uuid4()} This is a test there will be no cache hits and we'll fill up the context"*150}],
"user":"my-new-end-user-1"
}
        response = self.client.post("chat/completions", json=payload)
if response.status_code !=200:
# log the errors in error.txt
withopen("error.txt","a")as error_log:
                error_log.write(response.text +"\n")


defon_start(self):
        self.api_key = os.getenv('API_KEY','sk-1234')
        self.client.headers.update({'Authorization':f'Bearer {self.api_key}'})
```