---
title: Providers - Python SDK
url: https://openrouter.ai/docs/sdks/python/api-reference/providers.mdx
source: llms
fetched_at: 2026-02-13T15:17:38.884843-03:00
rendered_js: false
word_count: 183
summary: This document provides technical documentation and usage examples for the providers endpoint within the OpenRouter Python SDK, specifically detailing the method to list all available providers.
tags:
    - openrouter-sdk
    - python
    - api-reference
    - list-providers
    - provider-information
category: api
---

***

title: Providers - Python SDK
subtitle: Providers method reference
headline: Providers | OpenRouter Python SDK
canonical-url: '[https://openrouter.ai/docs/sdks/python/api-reference/providers](https://openrouter.ai/docs/sdks/python/api-reference/providers)'
'og:site\_name': OpenRouter Documentation
'og:title': Providers | OpenRouter Python SDK
'og:description': >-
Providers method documentation for the OpenRouter Python SDK. Learn how to use
this API endpoint with code examples.
'og:image':
type: url
value: >-
[https://openrouter.ai/dynamic-og?title=Providers%20-%20Python%20SDK\&description=Providers%20method%20reference](https://openrouter.ai/dynamic-og?title=Providers%20-%20Python%20SDK\&description=Providers%20method%20reference)
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

(*providers*)

## Overview

Provider information endpoints

### Available Operations

* [list](#list) - List all providers

## list

List all providers

### Example Usage

{/* UsageSnippet language="python" operationID="listProviders" method="get" path="/providers" */}

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.providers.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter | Type                                                               | Required             | Description                                                         |
| --------- | ------------------------------------------------------------------ | -------------------- | ------------------------------------------------------------------- |
| `retries` | [Optional\[utils.RetryConfig\]](../../models/utils/retryconfig.md) | :heavy\_minus\_sign: | Configuration to override the default retry behavior of the client. |

### Response

**[operations.ListProvidersResponse](/docs/sdks/python/api-reference/operations/listprovidersresponse)**

### Errors

| Error Type                         | Status Code | Content Type     |
| ---------------------------------- | ----------- | ---------------- |
| errors.InternalServerResponseError | 500         | application/json |
| errors.OpenRouterDefaultError      | 4XX, 5XX    | \*/\*            |