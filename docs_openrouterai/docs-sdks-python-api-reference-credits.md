---
title: Credits - Python SDK
url: https://openrouter.ai/docs/sdks/python/api-reference/credits.mdx
source: llms
fetched_at: 2026-02-13T15:17:27.336099-03:00
rendered_js: false
word_count: 362
summary: This document provides a technical reference for managing user credits and processing cryptocurrency payments via the OpenRouter Python SDK. It details specific API methods for retrieving credit balances and generating Coinbase charges, including parameter requirements and error codes.
tags:
    - openrouter
    - python-sdk
    - api-reference
    - credit-management
    - coinbase
    - cryptocurrency-payments
category: reference
---

***

title: Credits - Python SDK
subtitle: Credits method reference
headline: Credits | OpenRouter Python SDK
canonical-url: '[https://openrouter.ai/docs/sdks/python/api-reference/credits](https://openrouter.ai/docs/sdks/python/api-reference/credits)'
'og:site\_name': OpenRouter Documentation
'og:title': Credits | OpenRouter Python SDK
'og:description': >-
Credits method documentation for the OpenRouter Python SDK. Learn how to use
this API endpoint with code examples.
'og:image':
type: url
value: >-
[https://openrouter.ai/dynamic-og?title=Credits%20-%20Python%20SDK\&description=Credits%20method%20reference](https://openrouter.ai/dynamic-og?title=Credits%20-%20Python%20SDK\&description=Credits%20method%20reference)
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

(*credits*)

## Overview

Credit management endpoints

### Available Operations

* [get\_credits](#get_credits) - Get remaining credits
* [create\_coinbase\_charge](#create_coinbase_charge) - Create a Coinbase charge for crypto payment

## get\_credits

Get total credits purchased and used for the authenticated user. [Provisioning key](/docs/guides/overview/auth/provisioning-api-keys) required.

### Example Usage

{/* UsageSnippet language="python" operationID="getCredits" method="get" path="/credits" */}

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.credits.get_credits()

    # Handle response
    print(res)

```

### Parameters

| Parameter | Type                                                               | Required             | Description                                                         |
| --------- | ------------------------------------------------------------------ | -------------------- | ------------------------------------------------------------------- |
| `retries` | [Optional\[utils.RetryConfig\]](../../models/utils/retryconfig.md) | :heavy\_minus\_sign: | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetCreditsResponse](/docs/sdks/python/api-reference/operations/getcreditsresponse)**

### Errors

| Error Type                         | Status Code | Content Type     |
| ---------------------------------- | ----------- | ---------------- |
| errors.UnauthorizedResponseError   | 401         | application/json |
| errors.ForbiddenResponseError      | 403         | application/json |
| errors.InternalServerResponseError | 500         | application/json |
| errors.OpenRouterDefaultError      | 4XX, 5XX    | \*/\*            |

## create\_coinbase\_charge

Create a Coinbase charge for crypto payment

### Example Usage

{/* UsageSnippet language="python" operationID="createCoinbaseCharge" method="post" path="/credits/coinbase" */}

```python
from openrouter import OpenRouter, operations
import os

with OpenRouter() as open_router:

    res = open_router.credits.create_coinbase_charge(security=operations.CreateCoinbaseChargeSecurity(
        bearer=os.getenv("OPENROUTER_BEARER", ""),
    ), amount=100, sender="0x1234567890123456789012345678901234567890", chain_id=1)

    # Handle response
    print(res)

```

### Parameters

| Parameter  | Type                                                                                                               | Required             | Description                                                         |
| ---------- | ------------------------------------------------------------------------------------------------------------------ | -------------------- | ------------------------------------------------------------------- |
| `security` | [operations.CreateCoinbaseChargeSecurity](/docs/sdks/python/api-reference/operations/createcoinbasechargesecurity) | :heavy\_check\_mark: | N/A                                                                 |
| `amount`   | *float*                                                                                                            | :heavy\_check\_mark: | N/A                                                                 |
| `sender`   | *str*                                                                                                              | :heavy\_check\_mark: | N/A                                                                 |
| `chain_id` | [components.ChainID](/docs/sdks/python/api-reference/components/chainid)                                           | :heavy\_check\_mark: | N/A                                                                 |
| `retries`  | [Optional\[utils.RetryConfig\]](../../models/utils/retryconfig.md)                                                 | :heavy\_minus\_sign: | Configuration to override the default retry behavior of the client. |

### Response

**[operations.CreateCoinbaseChargeResponse](/docs/sdks/python/api-reference/operations/createcoinbasechargeresponse)**

### Errors

| Error Type                          | Status Code | Content Type     |
| ----------------------------------- | ----------- | ---------------- |
| errors.BadRequestResponseError      | 400         | application/json |
| errors.UnauthorizedResponseError    | 401         | application/json |
| errors.TooManyRequestsResponseError | 429         | application/json |
| errors.InternalServerResponseError  | 500         | application/json |
| errors.OpenRouterDefaultError       | 4XX, 5XX    | \*/\*            |