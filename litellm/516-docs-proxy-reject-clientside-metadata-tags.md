---
title: Reject Client-Side Metadata Tags | liteLLM
url: https://docs.litellm.ai/docs/proxy/reject_clientside_metadata_tags
source: sitemap
fetched_at: 2026-01-21T19:53:28.414175748-03:00
rendered_js: false
word_count: 234
summary: This document explains the reject_clientside_metadata_tags setting, which prevents users from overriding request tags to ensure consistent budget tracking and routing. It covers configuration steps, usage scenarios, and the error behavior of the API when this security feature is enabled.
tags:
    - api-security
    - configuration
    - metadata-tags
    - litellm
    - access-control
    - budget-tracking
category: configuration
---

## Overview[​](#overview "Direct link to Overview")

The `reject_clientside_metadata_tags` setting allows you to prevent users from passing client-side `metadata.tags` in their API requests. This ensures that tags are only inherited from the API key metadata and cannot be overridden by users to potentially influence budget tracking or routing decisions.

## Use Case[​](#use-case "Direct link to Use Case")

This feature is particularly useful in multi-tenant scenarios where:

- You want to enforce strict budget tracking based on API key tags
- You want to prevent users from manipulating routing decisions by sending custom client-side tags
- You need to ensure consistent tag-based filtering and reporting

## Configuration[​](#configuration "Direct link to Configuration")

Add the following to your `config.yaml`:

```
general_settings:
reject_clientside_metadata_tags:true# Default is false/null
```

## Behavior[​](#behavior "Direct link to Behavior")

### When `reject_clientside_metadata_tags: true`[​](#when-reject_clientside_metadata_tags-true "Direct link to when-reject_clientside_metadata_tags-true")

**Rejected Request Example:**

```
curl -X POST http://localhost:4000/chat/completions \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Hello"}],
    "metadata": {
      "tags": ["custom-tag"]  # This will be rejected
    }
  }'
```

**Error Response:**

```
{
"error":{
"message":"Client-side 'metadata.tags' not allowed in request. 'reject_clientside_metadata_tags'=True. Tags can only be set via API key metadata.",
"type":"bad_request_error",
"param":"metadata.tags",
"code":400
}
}
```

**Allowed Request Example:**

```
curl -X POST http://localhost:4000/chat/completions \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Hello"}],
    "metadata": {
      "custom_field": "value"  # Other metadata fields are allowed
    }
  }'
```

### When `reject_clientside_metadata_tags: false` or not set[​](#when-reject_clientside_metadata_tags-false-or-not-set "Direct link to when-reject_clientside_metadata_tags-false-or-not-set")

All requests are allowed, including those with client-side `metadata.tags`.

When `reject_clientside_metadata_tags` is enabled, tags should be set on the API key metadata:

```
curl -X POST http://localhost:4000/key/generate \
  -H "Authorization: Bearer sk-master-key" \
  -H "Content-Type: application/json" \
  -d '{
    "metadata": {
      "tags": ["team-a", "production"]
    }
  }'
```

These tags will be automatically inherited by all requests made with that API key.

## Complete Example Configuration[​](#complete-example-configuration "Direct link to Complete Example Configuration")

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: gpt-3.5-turbo
api_key: os.environ/OPENAI_API_KEY

general_settings:
master_key: sk-1234
database_url:"postgresql://user:password@localhost:5432/litellm"

# Reject client-side tags
reject_clientside_metadata_tags:true

# Optional: Also enforce user parameter
enforce_user_param:true
```

## Similar Features[​](#similar-features "Direct link to Similar Features")

- `enforce_user_param` - Requires all requests to include a 'user' parameter
- Tag-based routing - Use tags for intelligent request routing
- Budget tracking - Track spending per tag

## Notes[​](#notes "Direct link to Notes")

- This check only applies to LLM API routes (e.g., `/chat/completions`, `/embeddings`)
- Management endpoints (e.g., `/key/generate`) are not affected
- The check validates that client-side `metadata.tags` is not present in the request body
- Other metadata fields can still be passed in requests
- Tags set on API keys will still be applied to all requests