---
title: Mock Completion Responses - Save Testing Costs | liteLLM
url: https://docs.litellm.ai/docs/tutorials/mock_completion
source: sitemap
fetched_at: 2026-01-21T19:55:37.089487275-03:00
rendered_js: false
word_count: 34
summary: This document explains how to use the mock_response parameter in LiteLLM to simulate API responses for testing purposes without making actual network calls or incurring costs.
tags:
    - litellm
    - mock-response
    - unit-testing
    - api-mocking
    - python
    - completion-api
category: guide
---

Trying to test making LLM Completion calls without calling the LLM APIs ? Pass `mock_response` to `litellm.completion` and litellm will directly return the response without neededing the call the LLM API and spend $$

```
from litellm import completion
import pytest

deftest_completion_openai():
try:
        response = completion(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content":"Why is LiteLLM amazing?"}],
            mock_response="LiteLLM is awesome"
)
# Add any assertions here to check the response
print(response)
print(response['choices'][0]['finish_reason'])
except Exception as e:
        pytest.fail(f"Error occurred: {e}")
```