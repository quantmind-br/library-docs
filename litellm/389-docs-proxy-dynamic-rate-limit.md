---
title: Dynamic TPM/RPM Allocation | liteLLM
url: https://docs.litellm.ai/docs/proxy/dynamic_rate_limit
source: sitemap
fetched_at: 2026-01-21T19:51:49.159552974-03:00
rendered_js: false
word_count: 0
summary: This document provides a code example for demonstrating and testing rate limiting across multiple API keys sharing a single model via a proxy server. It illustrates how token quotas are enforced per key and how to handle RateLimitError exceptions in a concurrent environment.
tags:
    - rate-limiting
    - openai-proxy
    - token-management
    - api-key-generation
    - python
    - error-handling
category: tutorial
---

```
"""
- Run 2 concurrent teams calling same model
- model has 60 TPM
- Mock response returns 30 total tokens / request
- Each team will only be able to make 1 request per minute
"""

import requests
from openai import OpenAI, RateLimitError

defcreate_key(api_key:str, base_url:str):
    response = requests.post(
        url="{}/key/generate".format(base_url),
        json={},
        headers={
"Authorization":"Bearer {}".format(api_key)
}
)

    _response = response.json()

return _response["key"]

key_1 = create_key(api_key="sk-1234", base_url="http://0.0.0.0:4000")
key_2 = create_key(api_key="sk-1234", base_url="http://0.0.0.0:4000")

# call proxy with key 1 - works
openai_client_1 = OpenAI(api_key=key_1, base_url="http://0.0.0.0:4000")

response = openai_client_1.chat.completions.with_raw_response.create(
    model="my-fake-model", messages=[{"role":"user","content":"Hello world!"}],
)

print("Headers for call 1 - {}".format(response.headers))
_response = response.parse()
print("Total tokens for call - {}".format(_response.usage.total_tokens))


# call proxy with key 2 -  works 
openai_client_2 = OpenAI(api_key=key_2, base_url="http://0.0.0.0:4000")

response = openai_client_2.chat.completions.with_raw_response.create(
    model="my-fake-model", messages=[{"role":"user","content":"Hello world!"}],
)

print("Headers for call 2 - {}".format(response.headers))
_response = response.parse()
print("Total tokens for call - {}".format(_response.usage.total_tokens))
# call proxy with key 2 -  fails
try:
    openai_client_2.chat.completions.with_raw_response.create(model="my-fake-model", messages=[{"role":"user","content":"Hey, how's it going?"}])
raise Exception("This should have failed!")
except RateLimitError as e:
print("This was rate limited b/c - {}".format(str(e)))

```