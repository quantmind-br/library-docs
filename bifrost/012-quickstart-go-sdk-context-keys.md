---
title: Context Keys
url: https://docs.getbifrost.ai/quickstart/go-sdk/context-keys.md
source: llms
fetched_at: 2026-01-21T19:44:55.967050203-03:00
rendered_js: false
word_count: 693
summary: This document explains how to use Go context keys in Bifrost to configure request behavior and access response metadata during the request lifecycle. It provides a detailed reference of available keys for custom headers, API selection, tracking, and debugging.
tags:
    - go-sdk
    - context-keys
    - request-configuration
    - response-metadata
    - bifrost
    - api-integration
category: reference
---

# Context Keys

> Use context keys to configure request behavior, pass metadata, and access response information throughout the request lifecycle.

Bifrost uses Go's `context.Context` to pass configuration and metadata through the request lifecycle. Context keys allow you to customize request behavior, pass request-specific settings, and read metadata set by Bifrost.

## Request Configuration Keys

These keys can be set before making a request to customize behavior.

### Extra Headers

Pass custom headers with individual requests. Headers are automatically propagated to the provider.

```go  theme={null}
ctx := context.Background()

extraHeaders := map[string][]string{
    "user-id":    {"user-123"},
    "session-id": {"session-abc"},
}
ctx = context.WithValue(ctx, schemas.BifrostContextKeyExtraHeaders, extraHeaders)

response, err := client.ChatCompletionRequest(ctx, &schemas.BifrostChatRequest{
    Provider: schemas.OpenAI,
    Model:    "gpt-4o-mini",
    Input:    messages,
})
```

<Note>
  See [Custom Headers Per Request](./provider-configuration#custom-headers-per-request) for detailed information on header handling and security restrictions.
</Note>

### API Key Name Selection

Explicitly select a named API key from your configured keys.

```go  theme={null}
ctx := context.WithValue(ctx, schemas.BifrostContextKeyAPIKeyName, "premium-key")
```

### Direct Key

Bypass key selection and provide credentials directly. Useful for dynamic key scenarios.

```go  theme={null}
directKey := schemas.Key{
    Value:  "sk-direct-api-key",
    Models: []string{"gpt-4o"},
    Weight: 1.0,
}
ctx := context.WithValue(ctx, schemas.BifrostContextKeyDirectKey, directKey)
```

### Skip Key Selection

Skip the key selection process entirely and pass an empty key to the provider. Useful for providers that don't require authentication or when using ambient credentials.

```go  theme={null}
ctx := context.WithValue(ctx, schemas.BifrostContextKeySkipKeySelection, true)
```

### Request ID

Set a custom request ID for tracking and correlation.

```go  theme={null}
ctx := context.WithValue(ctx, schemas.BifrostContextKeyRequestID, "req-12345-abc")
```

### Custom URL Path

Append a custom path to the provider's base URL. Useful for accessing provider-specific endpoints.

```go  theme={null}
ctx := context.WithValue(ctx, schemas.BifrostContextKeyURLPath, "/custom/endpoint")
```

### Raw Request Body

Send a raw request body instead of Bifrost's standardized format. The provider receives your payload as-is. You must both enable the context key AND set the `RawRequestBody` field on your request.

```go  theme={null}
// Prepare your raw JSON payload
rawPayload := []byte(`{
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "Hello!"}],
    "custom_field": "provider-specific-value"
}`)

// Enable raw request body mode
ctx := context.WithValue(ctx, schemas.BifrostContextKeyUseRawRequestBody, true)

// Set the raw body on the request
response, err := client.ChatCompletionRequest(ctx, &schemas.BifrostChatRequest{
    Provider:       schemas.OpenAI,
    Model:          "gpt-4o",
    RawRequestBody: rawPayload,  // This will be sent directly to the provider
})
```

<Note>
  When using raw request body, Bifrost bypasses its request conversion and sends your payload directly to the provider. You're responsible for ensuring the payload matches the provider's expected format.
</Note>

### Send Back Raw Request/Response

Include the original request or response in the `ExtraFields` for debugging.

```go  theme={null}
// Include raw request in response
ctx := context.WithValue(ctx, schemas.BifrostContextKeySendBackRawRequest, true)

// Include raw provider response
ctx := context.WithValue(ctx, schemas.BifrostContextKeySendBackRawResponse, true)
```

Access in response:

```go  theme={null}
response, _ := client.ChatCompletionRequest(ctx, request)
if response.ChatResponse != nil {
    rawReq := response.ChatResponse.ExtraFields.RawRequest
    rawResp := response.ChatResponse.ExtraFields.RawResponse
}
```

## Response Metadata Keys

These keys are set by Bifrost and can be read from the context after a request completes. They're particularly useful in plugins and hooks.

### Selected Key Information

After Bifrost selects an API key, it stores the selection details in the context.

```go  theme={null}
// Get the selected key's ID
keyID := ctx.Value(schemas.BifrostContextKeySelectedKeyID).(string)

// Get the selected key's name
keyName := ctx.Value(schemas.BifrostContextKeySelectedKeyName).(string)
```

### Retry and Fallback Information

Track retry attempts and fallback progression.

```go  theme={null}
// Number of retries attempted (0 = first attempt)
retries := ctx.Value(schemas.BifrostContextKeyNumberOfRetries).(int)

// Fallback index (0 = primary, 1 = first fallback, etc.)
fallbackIdx := ctx.Value(schemas.BifrostContextKeyFallbackIndex).(int)

// Fallback request ID (set when using a fallback provider)
fallbackReqID := ctx.Value(schemas.BifrostContextKeyFallbackRequestID).(string)
```

### Stream End Indicator

For streaming responses, indicates when the stream has completed.

```go  theme={null}
isStreamEnd := ctx.Value(schemas.BifrostContextKeyStreamEndIndicator).(bool)
```

<Note>
  Plugin developers: When implementing custom streaming in PreHook or PostHook, make sure to mark `BifrostContextKeyStreamEndIndicator` as `true` at the end of the stream for proper cleanup.
</Note>

### Integration Type

Identifies which integration format is being used (useful in gateway scenarios).

```go  theme={null}
integrationType := ctx.Value(schemas.BifrostContextKeyIntegrationType).(string)
// e.g., "openai", "anthropic", "bedrock"
```

## Complete Example

Here's a comprehensive example showing multiple context keys in use:

```go  theme={null}
package main

import (
    "context"
    "fmt"
    "log"

    "github.com/maximhq/bifrost"
    "github.com/maximhq/bifrost/core/schemas"
)

func makeRequest(client *bifrost.Bifrost) {
    // Start with background context
    ctx := context.Background()

    // Add request tracking
    ctx = context.WithValue(ctx, schemas.BifrostContextKeyRequestID, "req-001")

    // Add custom headers for the provider
    extraHeaders := map[string][]string{
        "x-correlation-id": {"corr-12345"},
        "x-tenant-id":      {"tenant-abc"},
    }
    ctx = context.WithValue(ctx, schemas.BifrostContextKeyExtraHeaders, extraHeaders)

    // Request raw response for debugging
    ctx = context.WithValue(ctx, schemas.BifrostContextKeySendBackRawResponse, true)

    // Make the request
    messages := []schemas.BifrostMessage{
        {Role: "user", Content: &schemas.BifrostMessageContent{Text: bifrost.Ptr("Hello!")}},
    }

    response, err := client.ChatCompletionRequest(ctx, &schemas.BifrostChatRequest{
        Provider: schemas.OpenAI,
        Model:    "gpt-4o-mini",
        Input:    messages,
    })

    if err != nil {
        log.Printf("Request failed: %v", err)
        return
    }

    // Access response metadata
    if response.ChatResponse != nil {
        extra := response.ChatResponse.ExtraFields
        fmt.Printf("Provider: %s\n", extra.Provider)
        fmt.Printf("Latency: %dms\n", extra.Latency)

        if extra.RawResponse != nil {
            fmt.Printf("Raw response available for debugging\n")
        }
    }
}
```

## Context Keys Reference

| Key                                    | Type                  | Direction | Description                     |
| -------------------------------------- | --------------------- | --------- | ------------------------------- |
| `BifrostContextKeyVirtualKey`          | `string`              | Set       | Virtual key identifier          |
| `BifrostContextKeyAPIKeyName`          | `string`              | Set       | Explicit API key name selection |
| `BifrostContextKeyRequestID`           | `string`              | Set       | Custom request ID for tracking  |
| `BifrostContextKeyFallbackRequestID`   | `string`              | Read      | Request ID when using fallback  |
| `BifrostContextKeyDirectKey`           | `schemas.Key`         | Set       | Direct key credentials          |
| `BifrostContextKeySelectedKeyID`       | `string`              | Read      | Selected key's ID               |
| `BifrostContextKeySelectedKeyName`     | `string`              | Read      | Selected key's name             |
| `BifrostContextKeyNumberOfRetries`     | `int`                 | Read      | Number of retry attempts        |
| `BifrostContextKeyFallbackIndex`       | `int`                 | Read      | Current fallback index          |
| `BifrostContextKeyStreamEndIndicator`  | `bool`                | Read      | Stream completion flag          |
| `BifrostContextKeySkipKeySelection`    | `bool`                | Set       | Skip key selection              |
| `BifrostContextKeyExtraHeaders`        | `map[string][]string` | Set       | Custom request headers          |
| `BifrostContextKeyURLPath`             | `string`              | Set       | Custom URL path suffix          |
| `BifrostContextKeyUseRawRequestBody`   | `bool`                | Set       | Use raw request body            |
| `BifrostContextKeySendBackRawRequest`  | `bool`                | Set       | Include raw request in response |
| `BifrostContextKeySendBackRawResponse` | `bool`                | Set       | Include raw response            |
| `BifrostContextKeyIntegrationType`     | `string`              | Read      | Integration format type         |
| `BifrostContextKeyUserAgent`           | `string`              | Read      | Request user agent              |

## Next Steps

* **[Provider Configuration](./provider-configuration)** - Configure providers and keys
* **[Streaming Responses](./streaming)** - Real-time response handling
* **[Tool Calling](./tool-calling)** - Enable AI function calling
* **[Core Features](../../features/)** - Advanced Bifrost capabilities


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt