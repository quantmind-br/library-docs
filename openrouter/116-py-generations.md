---
title: Generations - Python SDK
url: https://openrouter.ai/docs/sdks/python/api-reference/generations.mdx
source: llms
fetched_at: 2026-02-13T15:17:32.507645-03:00
rendered_js: false
word_count: 251
summary: This document provides a technical reference for the generations method in the OpenRouter Python SDK, detailing how to retrieve request and usage metadata for specific generation IDs.
tags:
    - openrouter
    - python-sdk
    - api-reference
    - generations
    - metadata-retrieval
    - error-handling
category: api
---

***

title: Generations - Python SDK
subtitle: Generations method reference
headline: Generations | OpenRouter Python SDK
canonical-url: '[https://openrouter.ai/docs/sdks/python/api-reference/generations](https://openrouter.ai/docs/sdks/python/api-reference/generations)'
'og:site\_name': OpenRouter Documentation
'og:title': Generations | OpenRouter Python SDK
'og:description': >-
Generations method documentation for the OpenRouter Python SDK. Learn how to
use this API endpoint with code examples.
'og:image':
type: url
value: >-
[https://openrouter.ai/dynamic-og?title=Generations%20-%20Python%20SDK\&description=Generations%20method%20reference](https://openrouter.ai/dynamic-og?title=Generations%20-%20Python%20SDK\&description=Generations%20method%20reference)
'og:image:width': 1200
'og:image:height': 630
'twitter:card': summary\_large\_image
'twitter:site': '@OpenRouterAI'
noindex: false
nofollow: false
---------------

{/* banner:start */}

<Warning>
  The Python SDK and docs are currently in beta.
  Report issues on [GitHub](https://github.com/OpenRouterTeam/python-sdk/issues).
</Warning>

{/* banner:end */}

(*generations*)

## Overview

Generation history endpoints

### Available Operations

* [get\_generation](#get_generation) - Get request & usage metadata for a generation

## get\_generation

Get request & usage metadata for a generation

### Example Usage

{/* UsageSnippet language="python" operationID="getGeneration" method="get" path="/generation" */}

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.generations.get_generation(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter | Type                                                               | Required             | Description                                                         |
| --------- | ------------------------------------------------------------------ | -------------------- | ------------------------------------------------------------------- |
| `id`      | *str*                                                              | :heavy\_check\_mark: | N/A                                                                 |
| `retries` | [Optional\[utils.RetryConfig\]](../../models/utils/retryconfig.md) | :heavy\_minus\_sign: | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetGenerationResponse](/docs/sdks/python/api-reference/operations/getgenerationresponse)**

### Errors

| Error Type                             | Status Code | Content Type     |
| -------------------------------------- | ----------- | ---------------- |
| errors.UnauthorizedResponseError       | 401         | application/json |
| errors.PaymentRequiredResponseError    | 402         | application/json |
| errors.NotFoundResponseError           | 404         | application/json |
| errors.TooManyRequestsResponseError    | 429         | application/json |
| errors.InternalServerResponseError     | 500         | application/json |
| errors.BadGatewayResponseError         | 502         | application/json |
| errors.EdgeNetworkTimeoutResponseError | 524         | application/json |
| errors.ProviderOverloadedResponseError | 529         | application/json |
| errors.OpenRouterDefaultError          | 4XX, 5XX    | \*/\*            |