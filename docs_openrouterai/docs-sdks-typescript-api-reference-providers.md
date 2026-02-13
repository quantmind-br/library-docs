---
title: Providers - TypeScript SDK
url: https://openrouter.ai/docs/sdks/typescript/api-reference/providers.mdx
source: llms
fetched_at: 2026-02-13T15:17:14.726281-03:00
rendered_js: false
word_count: 304
summary: This document provides technical reference for the providers endpoint in the OpenRouter TypeScript SDK, explaining how to retrieve a list of available AI providers.
tags:
    - typescript-sdk
    - openrouter-api
    - provider-list
    - api-reference
    - sdk-methods
category: reference
---

***

title: Providers - TypeScript SDK
subtitle: Providers method reference
headline: Providers | OpenRouter TypeScript SDK
canonical-url: '[https://openrouter.ai/docs/sdks/typescript/api-reference/providers](https://openrouter.ai/docs/sdks/typescript/api-reference/providers)'
'og:site\_name': OpenRouter Documentation
'og:title': Providers | OpenRouter TypeScript SDK
'og:description': >-
Providers method documentation for the OpenRouter TypeScript SDK. Learn how to
use this API endpoint with code examples.
'og:image':
type: url
value: >-
[https://openrouter.ai/dynamic-og?title=Providers%20-%20TypeScript%20SDK\&description=Providers%20method%20reference](https://openrouter.ai/dynamic-og?title=Providers%20-%20TypeScript%20SDK\&description=Providers%20method%20reference)
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

Provider information endpoints

### Available Operations

* [list](#list) - List all providers

## list

List all providers

### Example Usage

{/* UsageSnippet language="typescript" operationID="listProviders" method="get" path="/providers" */}

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.providers.list();

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { providersList } from "@openrouter/sdk/funcs/providersList.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await providersList(openRouter);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("providersList failed:", res.error);
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

**Promise\<[operations.ListProvidersResponse](/docs/sdks/typescript/api-reference/operations/listprovidersresponse)>**

### Errors

| Error Type                         | Status Code | Content Type     |
| ---------------------------------- | ----------- | ---------------- |
| errors.InternalServerResponseError | 500         | application/json |
| errors.OpenRouterDefaultError      | 4XX, 5XX    | \*/\*            |