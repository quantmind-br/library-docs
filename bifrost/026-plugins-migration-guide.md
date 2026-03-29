---
title: Plugin Migration Guide
url: https://docs.getbifrost.ai/plugins/migration-guide.md
source: llms
fetched_at: 2026-01-21T19:44:17.779961578-03:00
rendered_js: false
word_count: 590
summary: This document provides instructions and code examples for migrating Bifrost plugins from v1.3.x to v1.4.x, focusing on the transition from legacy transport interceptors to the new dual-hook HTTP pattern.
tags:
    - bifrost
    - plugin-migration
    - golang
    - http-transport
    - wasm-support
    - api-update
category: guide
---

# Plugin Migration Guide

> How to migrate your Bifrost plugins from v1.3.x to v1.4.x

## Overview

Bifrost v1.4.x introduces a new plugin interface for HTTP transport layer interception. This guide helps you migrate existing plugins from the v1.3.x `TransportInterceptor` pattern to the v1.4.x `HTTPTransportPreHook` and `HTTPTransportPostHook` pattern.

<Note>
  If your plugin doesn't use `TransportInterceptor`, no migration is needed. The `PreHook`, `PostHook`, `Init`, `GetName`, and `Cleanup` functions remain unchanged.
</Note>

## What Changed?

The HTTP transport interception mechanism changed from a simple function that receives and returns headers/body to a dual-hook pattern that works with both native `.so` plugins and WASM plugins.

### Key Differences

| Aspect          | v1.3.x (TransportInterceptor)                   | v1.4.x+ (Pre/Post Hooks)                                                   |
| --------------- | ----------------------------------------------- | -------------------------------------------------------------------------- |
| Signature       | `TransportInterceptor(ctx, url, headers, body)` | `HTTPTransportPreHook(ctx, req)` + `HTTPTransportPostHook(ctx, req, resp)` |
| Return type     | `(headers, body, error)`                        | Pre: `(*HTTPResponse, error)`, Post: `error`                               |
| Request type    | Separate `headers map`, `body map`              | Unified `*HTTPRequest` struct                                              |
| Response access | Not available                                   | Post-hook receives `*HTTPResponse`                                         |
| Modification    | Return modified maps                            | Modify `req`/`resp` in-place                                               |
| Short-circuit   | Return error                                    | Return `*HTTPResponse`                                                     |
| WASM support    | No                                              | Yes                                                                        |
| Context         | Limited `BifrostContext`                        | Full `*BifrostContext` with `SetValue`/`Value`                             |

### Why the Change?

The new dual-hook pattern provides:

1. **WASM plugin support** - Serializable types work across WASM boundary
2. **Response interception** - Post-hook can modify responses before returning to client
3. **Simpler API** - No middleware wrapper, direct function call
4. **Better testability** - No fasthttp dependency in plugin tests
5. **Full context access** - BifrostContext available for sharing data between hooks
6. **Custom response short-circuits** - Return a full response to short-circuit

## Migration Steps

### Step 1: Update Imports

Remove the `fasthttp` import if present:

```go  theme={null}
import (
	"fmt"

	"github.com/maximhq/bifrost/core/schemas"
	// Remove: "github.com/valyala/fasthttp"
)
```

### Step 2: Replace the Function

**Before (v1.3.x):**

```go  theme={null}
// TransportInterceptor modifies raw HTTP headers and body
func TransportInterceptor(ctx *schemas.BifrostContext, url string, headers map[string]string, body map[string]any) (map[string]string, map[string]any, error) {
	// Add custom header
	headers["X-Custom-Header"] = "value"
	
	// Modify body
	body["custom_field"] = "custom_value"
	
	return headers, body, nil
}
```

**After (v1.4.x+):**

```go  theme={null}
// HTTPTransportPreHook intercepts requests BEFORE they enter Bifrost core
// Modify req in-place. Return (*HTTPResponse, nil) to short-circuit.
func HTTPTransportPreHook(ctx *schemas.BifrostContext, req *schemas.HTTPRequest) (*schemas.HTTPResponse, error) {
	// Add custom header (in-place modification)
	req.Headers["x-custom-header"] = "value"
	
	// Modify body (in-place modification)
	var body map[string]any
	sonic.Unmarshal(req.Body, &body)
	body["custom_field"] = "custom_value"
	req.Body, _ = sonic.Marshal(body)
	
	// Store values in context for use in post-hook
	ctx.SetValue(schemas.BifrostContextKey("my-plugin-key"), "my-value")
	
	// Return nil to continue, or return &HTTPResponse{} to short-circuit
	return nil, nil
}

// HTTPTransportPostHook intercepts responses AFTER they exit Bifrost core
// Modify resp in-place. Called in reverse order of pre-hooks.
func HTTPTransportPostHook(ctx *schemas.BifrostContext, req *schemas.HTTPRequest, resp *schemas.HTTPResponse) error {
	// Add response header
	resp.Headers["x-processed-by"] = "my-plugin"
	
	// Read values set in pre-hook
	if val := ctx.Value(schemas.BifrostContextKey("my-plugin-key")); val != nil {
		fmt.Println("Context value:", val)
	}
	
	// Return nil to continue, or return error to short-circuit
	return nil
}
```

### Step 3: Update Body Modification Logic

In v1.3.x, you received the body as a `map[string]any`. In v1.4.x, you work with `req.Body` bytes:

**Before (v1.3.x):**

```go  theme={null}
func TransportInterceptor(ctx *schemas.BifrostContext, url string, headers map[string]string, body map[string]any) (map[string]string, map[string]any, error) {
	// Direct map access
	body["model"] = "gpt-4"
	return headers, body, nil
}
```

**After (v1.4.x+):**

```go  theme={null}
import "github.com/bytedance/sonic"

func HTTPTransportPreHook(ctx *schemas.BifrostContext, req *schemas.HTTPRequest) (*schemas.HTTPResponse, error) {
	// Parse body
	var body map[string]any
	if err := sonic.Unmarshal(req.Body, &body); err == nil {
		// Modify body
		body["model"] = "gpt-4"
		// Update req.Body in-place
		req.Body, _ = sonic.Marshal(body)
	}
	return nil, nil
}

func HTTPTransportPostHook(ctx *schemas.BifrostContext, req *schemas.HTTPRequest, resp *schemas.HTTPResponse) error {
	// Modify response body if needed
	var respBody map[string]any
	if err := sonic.Unmarshal(resp.Body, &respBody); err == nil {
		respBody["plugin_processed"] = true
		resp.Body, _ = sonic.Marshal(respBody)
	}
	return nil
}
```

## Common Migration Patterns

### Adding Headers

**v1.3.x:**

```go  theme={null}
headers["authorization"] = "Bearer " + token
return headers, body, nil
```

**v1.4.x+:**

```go  theme={null}
// In HTTPTransportPreHook - modify request headers
req.Headers["authorization"] = "Bearer " + token
return nil, nil

// In HTTPTransportPostHook - modify response headers
resp.Headers["x-request-id"] = requestID
return nil
```

### Reading Headers

**v1.3.x:**

```go  theme={null}
apiKey := headers["X-API-Key"]
```

**v1.4.x+:**

```go  theme={null}
// Use case-insensitive helper for reading (recommended)
apiKey := req.CaseInsensitiveHeaderLookup("X-API-Key")

// Or direct map access (case-sensitive)
apiKey := req.Headers["x-api-key"]
```

### Conditional Processing

**v1.3.x:**

```go  theme={null}
func TransportInterceptor(ctx *schemas.BifrostContext, url string, headers map[string]string, body map[string]any) (map[string]string, map[string]any, error) {
	if headers["x-skip-processing"] == "true" {
		return headers, body, nil
	}
	// Process...
	return headers, body, nil
}
```

**v1.4.x+:**

```go  theme={null}
func HTTPTransportPreHook(ctx *schemas.BifrostContext, req *schemas.HTTPRequest) (*schemas.HTTPResponse, error) {
	if req.CaseInsensitiveHeaderLookup("x-skip-processing") == "true" {
		return nil, nil // Continue without modification
	}
	// Process...
	return nil, nil
}

func HTTPTransportPostHook(ctx *schemas.BifrostContext, req *schemas.HTTPRequest, resp *schemas.HTTPResponse) error {
	// Post-hook always runs unless pre-hook short-circuited
	return nil
}
```

### Error Handling / Short-Circuit

**v1.3.x:**

```go  theme={null}
func TransportInterceptor(ctx *schemas.BifrostContext, url string, headers map[string]string, body map[string]any) (map[string]string, map[string]any, error) {
	if headers["x-api-key"] == "" {
		return nil, nil, fmt.Errorf("missing API key")
	}
	return headers, body, nil
}
```

**v1.4.x+:**

```go  theme={null}
func HTTPTransportPreHook(ctx *schemas.BifrostContext, req *schemas.HTTPRequest) (*schemas.HTTPResponse, error) {
	if req.CaseInsensitiveHeaderLookup("x-api-key") == "" {
		// Return a custom response to short-circuit
		return &schemas.HTTPResponse{
			StatusCode: 401,
			Headers:    map[string]string{"Content-Type": "application/json"},
			Body:       []byte(`{"error": "missing API key"}`),
		}, nil
	}
	return nil, nil
}

func HTTPTransportPostHook(ctx *schemas.BifrostContext, req *schemas.HTTPRequest, resp *schemas.HTTPResponse) error {
	// Not called if pre-hook short-circuited
	return nil
}
```

### Accessing Request Method and Path

**v1.3.x:**

```go  theme={null}
// url parameter contained the full URL
func TransportInterceptor(ctx *schemas.BifrostContext, url string, headers map[string]string, body map[string]any) (map[string]string, map[string]any, error) {
	// Limited access to URL
	return headers, body, nil
}
```

**v1.4.x+:**

```go  theme={null}
func HTTPTransportPreHook(ctx *schemas.BifrostContext, req *schemas.HTTPRequest) (*schemas.HTTPResponse, error) {
	// Full access to request properties
	method := req.Method        // "GET", "POST", etc.
	path := req.Path            // "/v1/chat/completions"
	query := req.Query          // map[string]string of query params
	pathParams := req.PathParams // map[string]string of path variables (e.g., {model})
	return nil, nil
}

func HTTPTransportPostHook(ctx *schemas.BifrostContext, req *schemas.HTTPRequest, resp *schemas.HTTPResponse) error {
	// Access both request and response
	statusCode := resp.StatusCode
	responseHeaders := resp.Headers
	responseBody := resp.Body
	_ = statusCode      // Use variables...
	_ = responseHeaders
	_ = responseBody
	return nil
}
```

## Testing Your Migration

1. **Build your updated plugin:**
   ```bash  theme={null}
   go build -buildmode=plugin -o my-plugin.so main.go
   ```

2. **Update Bifrost to v1.4.x:**
   ```bash  theme={null}
   go get github.com/maximhq/bifrost/core@v1.4.0
   ```

3. **Test with a simple request:**
   ```bash  theme={null}
   curl -X POST http://localhost:8080/v1/chat/completions \
     -H "Content-Type: application/json" \
     -d '{"model": "openai/gpt-4o-mini", "messages": [{"role": "user", "content": "Hello"}]}'
   ```

4. **Verify logs show both hooks being called:**
   ```
   HTTPTransportPreHook called
   PreHook called
   PostHook called
   HTTPTransportPostHook called
   ```

## Troubleshooting

### Plugin fails to load after migration

**Error:** `plugin: symbol TransportInterceptor not found`

This error occurs if Bifrost v1.4.x is looking for the old function. Make sure:

1. You've updated to `HTTPTransportPreHook` and `HTTPTransportPostHook`
2. The function signatures match exactly:
   * `func HTTPTransportPreHook(ctx *schemas.BifrostContext, req *schemas.HTTPRequest) (*schemas.HTTPResponse, error)`
   * `func HTTPTransportPostHook(ctx *schemas.BifrostContext, req *schemas.HTTPRequest, resp *schemas.HTTPResponse) error`
3. You've rebuilt the plugin with the correct core version

### Body modification not working

Make sure you're assigning back to `req.Body` in the pre-hook:

```go  theme={null}
// Wrong - body changes lost
var body map[string]any
sonic.Unmarshal(req.Body, &body)
body["model"] = "gpt-4"
// Missing: req.Body = ...

// Correct - body changes applied
var body map[string]any
sonic.Unmarshal(req.Body, &body)
body["model"] = "gpt-4"
req.Body, _ = sonic.Marshal(body)  // Assign back!
```

### Response modification not working

Make sure you're modifying `resp` in the post-hook:

```go  theme={null}
func HTTPTransportPostHook(ctx *schemas.BifrostContext, req *schemas.HTTPRequest, resp *schemas.HTTPResponse) error {
	// Modify response headers
	resp.Headers["x-custom-header"] = "value"
	
	// Modify response body
	var body map[string]any
	sonic.Unmarshal(resp.Body, &body)
	body["extra_field"] = "value"
	resp.Body, _ = sonic.Marshal(body)
	
	return nil
}
```

### Headers not being set

Make sure you're modifying `req.Headers` or `resp.Headers` directly:

```go  theme={null}
// Set request header in pre-hook
req.Headers["x-custom-header"] = "value"

// Set response header in post-hook
resp.Headers["x-custom-header"] = "value"

// Read headers using case-insensitive helper
value := req.CaseInsensitiveHeaderLookup("X-Custom-Header")
```

### Context values not available in post-hook

Make sure you're using the correct context key type:

```go  theme={null}
// In pre-hook - set value
ctx.SetValue(schemas.BifrostContextKey("my-key"), "my-value")

// In post-hook - read value
if val := ctx.Value(schemas.BifrostContextKey("my-key")); val != nil {
	// Use val
}
```

## Need Help?

* **Discord Community**: [Join our Discord](https://getmax.im/bifrost-discord)
* **GitHub Issues**: [Report bugs or request features](https://github.com/maximhq/bifrost/issues)
* **Writing Plugins Guide**: [Full plugin documentation](./writing-plugin)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt