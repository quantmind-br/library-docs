---
title: '[New] Fallback Management Endpoints | liteLLM'
url: https://docs.litellm.ai/docs/proxy/fallback_management
source: sitemap
fetched_at: 2026-01-21T19:51:57.082198447-03:00
rendered_js: false
word_count: 472
summary: This document describes the dedicated API endpoints for configuring and managing model fallbacks, enabling specialized error handling for context window limits and content policy violations. It provides technical details on request parameters, validation logic, and the advantages of these endpoints over general configuration updates.
tags:
    - model-fallbacks
    - api-endpoints
    - proxy-configuration
    - error-handling
    - database-storage
    - content-policy
    - request-validation
category: api
---

Dedicated endpoints for managing model fallbacks separately from the general configuration.

## Overview[​](#overview "Direct link to Overview")

These endpoints allow you to configure, retrieve, and delete fallback models without modifying the entire proxy configuration. This provides a cleaner and safer way to manage fallbacks compared to using the `/config/update` endpoint.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

- Database storage must be enabled: Set `STORE_MODEL_IN_DB=True` in your environment
- Models must exist in the router before configuring fallbacks

## Endpoints[​](#endpoints "Direct link to Endpoints")

### POST /fallback[​](#post-fallback "Direct link to POST /fallback")

Create or update fallbacks for a specific model.

**Request Body:**

```
{
"model":"gpt-3.5-turbo",
"fallback_models":["gpt-4","claude-3-haiku"],
"fallback_type":"general"
}
```

**Parameters:**

- `model` (string, required): The primary model name to configure fallbacks for
- `fallback_models` (array of strings, required): List of fallback model names in priority order
- `fallback_type` (string, optional): Type of fallback. Options:
  
  - `"general"` (default): Standard fallbacks for any error
  - `"context_window"`: Fallbacks for context window exceeded errors
  - `"content_policy"`: Fallbacks for content policy violations

**Response:**

```
{
"model":"gpt-3.5-turbo",
"fallback_models":["gpt-4","claude-3-haiku"],
"fallback_type":"general",
"message":"Fallback configuration created successfully"
}
```

**Example using cURL:**

```
curl -X POST "http://localhost:4000/fallback" \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-3.5-turbo",
    "fallback_models": ["gpt-4", "claude-3-haiku"],
    "fallback_type": "general"
  }'
```

**Example using Python:**

```
import requests

response = requests.post(
"http://localhost:4000/fallback",
    headers={
"Authorization":"Bearer sk-1234",
"Content-Type":"application/json"
},
    json={
"model":"gpt-3.5-turbo",
"fallback_models":["gpt-4","claude-3-haiku"],
"fallback_type":"general"
}
)

print(response.json())
```

### GET /fallback/{model}[​](#get-fallbackmodel "Direct link to GET /fallback/{model}")

Get fallback configuration for a specific model.

**Parameters:**

- `model` (path parameter, required): The model name to get fallbacks for
- `fallback_type` (query parameter, optional): Type of fallback to retrieve (default: "general")

**Response:**

```
{
"model":"gpt-3.5-turbo",
"fallback_models":["gpt-4","claude-3-haiku"],
"fallback_type":"general"
}
```

**Example using cURL:**

```
curl -X GET "http://localhost:4000/fallback/gpt-3.5-turbo?fallback_type=general" \
  -H "Authorization: Bearer sk-1234"
```

**Example using Python:**

```
import requests

response = requests.get(
"http://localhost:4000/fallback/gpt-3.5-turbo",
    headers={"Authorization":"Bearer sk-1234"},
    params={"fallback_type":"general"}
)

print(response.json())
```

### DELETE /fallback/{model}[​](#delete-fallbackmodel "Direct link to DELETE /fallback/{model}")

Delete fallback configuration for a specific model.

**Parameters:**

- `model` (path parameter, required): The model name to delete fallbacks for
- `fallback_type` (query parameter, optional): Type of fallback to delete (default: "general")

**Response:**

```
{
"model":"gpt-3.5-turbo",
"fallback_type":"general",
"message":"Fallback configuration deleted successfully"
}
```

**Example using cURL:**

```
curl -X DELETE "http://localhost:4000/fallback/gpt-3.5-turbo?fallback_type=general" \
  -H "Authorization: Bearer sk-1234"
```

**Example using Python:**

```
import requests

response = requests.delete(
"http://localhost:4000/fallback/gpt-3.5-turbo",
    headers={"Authorization":"Bearer sk-1234"},
    params={"fallback_type":"general"}
)

print(response.json())
```

### Test fallback[​](#test-fallback "Direct link to Test fallback")

```
curl -X POST 'http://0.0.0.0:4000/chat/completions' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer sk-1234' \
-d '{
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "user",
      "content": "ping"
    }
  ],
  "mock_testing_fallbacks": true
}
'
```

## Validation[​](#validation "Direct link to Validation")

The endpoints perform the following validations:

1. **Model Existence**: Verifies that the primary model exists in the router
2. **Fallback Model Existence**: Ensures all fallback models exist in the router
3. **No Self-Fallback**: Prevents a model from being its own fallback
4. **No Duplicates**: Ensures no duplicate models in the fallback list
5. **Database Enabled**: Requires `STORE_MODEL_IN_DB=True` to be set

## Error Responses[​](#error-responses "Direct link to Error Responses")

### 400 Bad Request[​](#400-bad-request "Direct link to 400 Bad Request")

```
{
"detail":{
"error":"Invalid fallback models: ['non-existent-model']",
"available_models":["gpt-3.5-turbo","gpt-4","claude-3-haiku"]
}
}
```

### 404 Not Found[​](#404-not-found "Direct link to 404 Not Found")

```
{
"detail":{
"error":"Model 'gpt-3.5-turbo' not found in router",
"available_models":["gpt-4","claude-3-haiku"]
}
}
```

### 500 Internal Server Error[​](#500-internal-server-error "Direct link to 500 Internal Server Error")

```
{
"detail":{
"error":"Router not initialized"
}
}
```

## Fallback Types Explained[​](#fallback-types-explained "Direct link to Fallback Types Explained")

### General Fallbacks[​](#general-fallbacks "Direct link to General Fallbacks")

Used for any type of error that occurs during model invocation. This is the most common type of fallback.

**Use Case:** When a model is unavailable, rate-limited, or returns an error.

```
{
"model":"gpt-3.5-turbo",
"fallback_models":["gpt-4","claude-3-haiku"],
"fallback_type":"general"
}
```

### Context Window Fallbacks[​](#context-window-fallbacks "Direct link to Context Window Fallbacks")

Specifically triggered when a context window exceeded error occurs.

**Use Case:** When the input is too long for the primary model, fallback to a model with a larger context window.

```
{
"model":"gpt-3.5-turbo",
"fallback_models":["gpt-4-32k","claude-3-opus"],
"fallback_type":"context_window"
}
```

### Content Policy Fallbacks[​](#content-policy-fallbacks "Direct link to Content Policy Fallbacks")

Specifically triggered when content policy violations occur.

**Use Case:** When the primary model rejects content due to safety filters, fallback to a model with different content policies.

```
{
"model":"gpt-4",
"fallback_models":["claude-3-haiku"],
"fallback_type":"content_policy"
}
```

## Benefits Over /config/update[​](#benefits-over-configupdate "Direct link to Benefits Over /config/update")

1. **Safety**: Only modifies fallback configuration, won't accidentally change other settings
2. **Simplicity**: Focused API with clear validation messages
3. **Granularity**: Manage fallbacks per model and per type
4. **Validation**: Comprehensive checks ensure configuration is valid before applying
5. **Clarity**: Clear error messages with available models listed

## Notes[​](#notes "Direct link to Notes")

- Fallbacks are triggered after the configured number of retries fails
- Fallbacks are attempted in the order specified in `fallback_models`
- The maximum number of fallbacks attempted is controlled by the router's `max_fallbacks` setting
- Changes take effect immediately and are persisted to the database