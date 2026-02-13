---
title: Credits - TypeScript SDK
url: https://openrouter.ai/docs/sdks/typescript/api-reference/credits.mdx
source: llms
fetched_at: 2026-02-13T15:17:02.629799-03:00
rendered_js: false
word_count: 600
summary: This document provides a technical reference for managing user credits and cryptocurrency payments using the OpenRouter TypeScript SDK. It details specific methods for retrieving credit balances and creating Coinbase charges through both class-based and standalone function implementations.
tags:
    - openrouter-sdk
    - typescript
    - credit-management
    - api-reference
    - coinbase-integration
    - crypto-payments
    - sdk-documentation
category: reference
---

***

title: Credits - TypeScript SDK
subtitle: Credits method reference
headline: Credits | OpenRouter TypeScript SDK
canonical-url: '[https://openrouter.ai/docs/sdks/typescript/api-reference/credits](https://openrouter.ai/docs/sdks/typescript/api-reference/credits)'
'og:site\_name': OpenRouter Documentation
'og:title': Credits | OpenRouter TypeScript SDK
'og:description': >-
Credits method documentation for the OpenRouter TypeScript SDK. Learn how to
use this API endpoint with code examples.
'og:image':
type: url
value: >-
[https://openrouter.ai/dynamic-og?title=Credits%20-%20TypeScript%20SDK\&description=Credits%20method%20reference](https://openrouter.ai/dynamic-og?title=Credits%20-%20TypeScript%20SDK\&description=Credits%20method%20reference)
'og:image:width': 1200
'og:image:height': 630
'twitter:card': summary\_large\_image
'twitter:site': '@OpenRouterAI'
noindex: false
nofollow: false
---------------

{/* banner:start */}

<Warning>
  The TypeScript SDK and docs are currently in beta.
  Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).
</Warning>

{/* banner:end */}

## Overview

Credit management endpoints

### Available Operations

* [getCredits](#getcredits) - Get remaining credits
* [createCoinbaseCharge](#createcoinbasecharge) - Create a Coinbase charge for crypto payment

## getCredits

Get total credits purchased and used for the authenticated user. [Provisioning key](/docs/guides/overview/auth/provisioning-api-keys) required.

### Example Usage

{/* UsageSnippet language="typescript" operationID="getCredits" method="get" path="/credits" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.credits.getCredits();

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { creditsGetCredits } from "@openrouter/sdk/funcs/creditsGetCredits.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await creditsGetCredits(openRouter);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("creditsGetCredits failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter              | Type                                                                                    | Required             | Description                                                                                                                                                                    |
| ---------------------- | --------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `options`              | RequestOptions                                                                          | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options) | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/api-reference/lib/retryconfig)                      | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.GetCreditsResponse](/docs/sdks/typescript/api-reference/operations/getcreditsresponse)>**

### Errors

| Error Type                         | Status Code | Content Type     |
| ---------------------------------- | ----------- | ---------------- |
| errors.UnauthorizedResponseError   | 401         | application/json |
| errors.ForbiddenResponseError      | 403         | application/json |
| errors.InternalServerResponseError | 500         | application/json |
| errors.OpenRouterDefaultError      | 4XX, 5XX    | \*/\*            |

## createCoinbaseCharge

Create a Coinbase charge for crypto payment

### Example Usage

{/* UsageSnippet language="typescript" operationID="createCoinbaseCharge" method="post" path="/credits/coinbase" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter();

async function run() {
  const result = await openRouter.credits.createCoinbaseCharge({
    bearer: process.env["OPENROUTER_BEARER"] ?? "",
  }, {
    amount: 100,
    sender: "0x1234567890123456789012345678901234567890",
    chainId: 1,
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { creditsCreateCoinbaseCharge } from "@openrouter/sdk/funcs/creditsCreateCoinbaseCharge.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore();

async function run() {
  const res = await creditsCreateCoinbaseCharge(openRouter, {
    bearer: process.env["OPENROUTER_BEARER"] ?? "",
  }, {
    amount: 100,
    sender: "0x1234567890123456789012345678901234567890",
    chainId: 1,
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("creditsCreateCoinbaseCharge failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter              | Type                                                                                                                   | Required             | Description                                                                                                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`              | [models.CreateChargeRequest](/docs/sdks/typescript/api-reference/models/createchargerequest)                           | :heavy\_check\_mark: | The request object to use for the request.                                                                                                                                     |
| `security`             | [operations.CreateCoinbaseChargeSecurity](/docs/sdks/typescript/api-reference/operations/createcoinbasechargesecurity) | :heavy\_check\_mark: | The security requirements to use for the request.                                                                                                                              |
| `options`              | RequestOptions                                                                                                         | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/api-reference/lib/retryconfig)                                                     | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.CreateCoinbaseChargeResponse](/docs/sdks/typescript/api-reference/operations/createcoinbasechargeresponse)>**

### Errors

| Error Type                          | Status Code | Content Type     |
| ----------------------------------- | ----------- | ---------------- |
| errors.BadRequestResponseError      | 400         | application/json |
| errors.UnauthorizedResponseError    | 401         | application/json |
| errors.TooManyRequestsResponseError | 429         | application/json |
| errors.InternalServerResponseError  | 500         | application/json |
| errors.OpenRouterDefaultError       | 4XX, 5XX    | \*/\*            |