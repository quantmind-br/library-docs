---
title: Add Rerank Provider | liteLLM
url: https://docs.litellm.ai/docs/adding_provider/new_rerank_provider
source: sitemap
fetched_at: 2026-01-21T19:43:56.473085725-03:00
rendered_js: false
word_count: 47
summary: This document provides instructions on how to integrate new rerank providers into LiteLLM by implementing a custom configuration class and handling HTTP requests based on the Cohere Rerank API format.
tags:
    - litellm
    - rerank-api
    - provider-integration
    - python-development
    - custom-providers
category: guide
---

LiteLLM **follows the Cohere Rerank API format** for all rerank providers. Here's how to add a new rerank provider:

Create a config class named `<Provider><Endpoint>Config` that inherits from [`BaseRerankConfig`](https://github.com/BerriAI/litellm/blob/main/litellm/llms/base_llm/rerank/transformation.py):

```
from litellm.types.rerank import OptionalRerankParams, RerankRequest, RerankResponse
classYourProviderRerankConfig(BaseRerankConfig):
defget_supported_cohere_rerank_params(self, model:str)->list:
return[
"query",
"documents",
"top_n",
# ... other supported params
]

deftransform_rerank_request(self, model:str, optional_rerank_params: Dict, headers:dict)->dict:
# Transform request to RerankRequest spec
return rerank_request.model_dump(exclude_none=True)

deftransform_rerank_response(self, model:str, raw_response: httpx.Response,...)-> RerankResponse:
# Transform provider response to RerankResponse
return RerankResponse(**raw_response_json)
```

Add a code block to handle when your provider is called. Your provider should use the `base_llm_http_handler.rerank` method

```
elif _custom_llm_provider =="your_provider":
...
    response = base_llm_http_handler.rerank(
        model=model,
        custom_llm_provider=_custom_llm_provider,
        optional_rerank_params=optional_rerank_params,
        logging_obj=litellm_logging_obj,
        timeout=optional_params.timeout,
        api_key=dynamic_api_key or optional_params.api_key,
        api_base=api_base,
        _is_async=_is_async,
        headers=headers or litellm.headers or{},
        client=client,
        mod el_response=model_response,
)
...
```

```
deftest_basic_rerank_cohere():
    response = litellm.rerank(
        model="cohere/rerank-english-v3.0",
        query="hello",
        documents=["hello","world"],
        top_n=3,
)

print("re rank response: ", response)

assert response.idisnotNone
assert response.results isnotNone
```