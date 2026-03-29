---
title: Semantic Caching
url: https://docs.getbifrost.ai/features/semantic-caching.md
source: llms
fetched_at: 2026-01-21T19:43:49.862371381-03:00
rendered_js: false
word_count: 824
summary: This document explains how to implement semantic caching using vector similarity search to reduce AI latency and API costs. It provides detailed setup instructions for vector stores and configuration options for the semantic cache plugin.
tags:
    - semantic-caching
    - vector-search
    - ai-infrastructure
    - performance-optimization
    - weaviate
    - embeddings
category: guide
---

# Semantic Caching

> Intelligent response caching based on semantic similarity. Reduce costs and latency by serving cached responses for semantically similar requests.

## Overview

Semantic caching uses vector similarity search to intelligently cache AI responses, serving cached results for semantically similar requests even when the exact wording differs. This dramatically reduces API costs and latency for repeated or similar queries.

**Key Benefits:**

* **Cost Reduction**: Avoid expensive LLM API calls for similar requests
* **Improved Performance**: Sub-millisecond cache retrieval vs multi-second API calls
* **Intelligent Matching**: Semantic similarity beyond exact text matching
* **Streaming Support**: Full streaming response caching with proper chunk ordering

***

## Core Features

* **Dual-Layer Caching**: Exact hash matching + semantic similarity search (customizable threshold)
* **Vector-Powered Intelligence**: Uses embeddings to find semantically similar requests
* **Dynamic Configuration**: Per-request TTL and threshold overrides via headers/context
* **Model/Provider Isolation**: Separate caching per model and provider combination

***

## Vector Store Setup

<Tabs group="vector-store-setup">
  <Tab title="Go SDK">
    ```go  theme={null}
    import (
        "context"
        "github.com/maximhq/bifrost/framework/vectorstore"
        "github.com/maximhq/bifrost/core/schemas"
    )

    // Configure vector store
    vectorConfig := &vectorstore.Config{
        Enabled: true,
        Type:    vectorstore.VectorStoreTypeWeaviate,
        Config: vectorstore.WeaviateConfig{
            Scheme:    "http",
            Host:      "localhost:8080",
        },
    }

    // Create vector store
    store, err := vectorstore.NewVectorStore(context.Background(), vectorConfig, logger)
    if err != nil {
        log.Fatal("Failed to create vector store:", err)
    }
    ```
  </Tab>

  <Tab title="config.json">
    ```json  theme={null}
    {
      "vector_store": {
        "enabled": true,
        "type": "weaviate",
        "config": {
          "host": "localhost:8080",
          "scheme": "http",
        }
      }
    }
    ```

    **For Weaviate Cloud:**

    ```json  theme={null}
    {
      "vector_store": {
        "enabled": true,
        "type": "weaviate",
        "config": {
          "host": "your-cluster.weaviate.network",
          "scheme": "https",
          "api_key": "your-weaviate-api-key"
        }
      }
    }
    ```
  </Tab>
</Tabs>

***

## Semantic Cache Configuration

<Tabs group="cache-config">
  <Tab title="Go SDK">
    ```go  theme={null}
    import (
        "github.com/maximhq/bifrost/plugins/semanticcache"
        "github.com/maximhq/bifrost/core/schemas"
    )

    // Configure semantic cache plugin
    cacheConfig := semanticcache.Config{
        // Embedding model configuration (Required)
        Provider:       schemas.OpenAI,
        Keys:          []schemas.Key{{Value: "sk-..."}},
        EmbeddingModel: "text-embedding-3-small",
        Dimension:     1536,
        
        // Cache behavior
        TTL:       5 * time.Minute,  // Time to live for cached responses (default: 5 minutes)
        Threshold: 0.8,              // Similarity threshold for cache lookup (default: 0.8)
        CleanUpOnShutdown: true,     // Clean up cache on shutdown (default: false)
        
        // Conversation behavior
        ConversationHistoryThreshold: 5,    // Skip caching if conversation has > N messages (default: 3)
        ExcludeSystemPrompt: bifrost.Ptr(false), // Exclude system messages from cache key (default: false)
        
        // Advanced options
        CacheByModel:    bifrost.Ptr(true),  // Include model in cache key (default: true)
        CacheByProvider: bifrost.Ptr(true),  // Include provider in cache key (default: true)
    }

    // Create plugin
    plugin, err := semanticcache.Init(context.Background(), cacheConfig, logger, store)
    if err != nil {
        log.Fatal("Failed to create semantic cache plugin:", err)
    }

    // Add to Bifrost config
    bifrostConfig := schemas.BifrostConfig{
        Plugins: []schemas.Plugin{plugin},
        // ... other config
    }
    ```
  </Tab>

  <Tab title="Web UI">
        <img src="https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-semantic-cache-config.png?fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=174f448c78600e2a3cbb4fc820fb0fed" alt="Semantic Cache Plugin Configuration" data-og-width="3492" width="3492" data-og-height="2358" height="2358" data-path="media/ui-semantic-cache-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-semantic-cache-config.png?w=280&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=2a666d52f293fdfaeca624edb6dcf6f8 280w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-semantic-cache-config.png?w=560&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=c37b79047f43511074d414fceae2f442 560w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-semantic-cache-config.png?w=840&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=9355338fb9c9789fd8fb4ff326b5d2f0 840w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-semantic-cache-config.png?w=1100&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=3c6b5b5bde45cb34a5f49072d7155f39 1100w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-semantic-cache-config.png?w=1650&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=fa95aaa0f5602b5b44078decb7b339cb 1650w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-semantic-cache-config.png?w=2500&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=e04aff29eb6af677b866b828b2f1b843 2500w" />

    **Note**: Make sure you have a vector store setup (using `config.json`) before configuring the semantic cache plugin.

    1. **Navigate to Settings**
       * Open Bifrost UI at `http://localhost:8080`
       * Go to Settings.

    2. **Configure Semantic Cache Plugin**

    * Toggle the plugin switch to enable it, and fill in the required fields.

    **Required Fields:**

    * **Provider**: The provider to use for caching.
    * **Embedding Model**: The embedding model to use for caching.

    **Note**: Changes will need a restart of the Bifrost server to take effect, because the plugin is loaded on startup only.
  </Tab>

  <Tab title="config.json">
    ```json  theme={null}
    {
      "plugins": [
        {
          "enabled": true,
          "name": "semantic_cache",
          "config": {        
            "provider": "openai",
            "embedding_model": "text-embedding-3-small",
            
            "cleanup_on_shutdown": true,
            "ttl": "5m",
            "threshold": 0.8,
            
            "conversation_history_threshold": 3,
            "exclude_system_prompt": false,
            
            "cache_by_model": true,
            "cache_by_provider": true
          }
        }
      ]
    }
    ```

    > **Note**: All the available keys will be taken from the provider config on initialization, so make sure to add the keys to the provider you have specified in the config. Any updates to the keys will not be reflected until next restart.

    **TTL Format Options:**

    * Duration strings: `"30s"`, `"5m"`, `"1h"`, `"24h"`
    * Numeric seconds: `300` (5 minutes), `3600` (1 hour)
  </Tab>
</Tabs>

***

## Cache Triggering

<Warning>
  **Cache Key is mandatory**: Semantic caching only activates when a cache key is provided. Without a cache key, requests bypass caching entirely.
</Warning>

<Tabs group="cache-triggering">
  <Tab title="Go SDK">
    Must set cache key in request context:

    ```go  theme={null}
    // This request WILL be cached
    ctx = context.WithValue(ctx, semanticcache.CacheKey, "session-123")
    response, err := client.ChatCompletionRequest(ctx, request)

    // This request will NOT be cached (no context value)
    response, err := client.ChatCompletionRequest(context.Background(), request)
    ```
  </Tab>

  <Tab title="HTTP API">
    Must set cache key in request header `x-bf-cache-key`:

    ```bash  theme={null}
    # This request WILL be cached
    curl -H "x-bf-cache-key: session-123" ...

    # This request will NOT be cached (no header)
    curl ...
    ```
  </Tab>
</Tabs>

## Per-Request Overrides

Override default TTL and similarity threshold per request:

<Tabs group="per-request-overrides">
  <Tab title="Go SDK">
    You can set TTL and threshold in the request context, in the keys you configured in the plugin config:

    ```go  theme={null}
    // Go SDK: Custom TTL and threshold
    ctx = context.WithValue(ctx, semanticcache.CacheKey, "session-123")
    ctx = context.WithValue(ctx, semanticcache.CacheTTLKey, 30*time.Second)
    ctx = context.WithValue(ctx, semanticcache.CacheThresholdKey, 0.9)
    ```
  </Tab>

  <Tab title="HTTP API">
    You can set TTL and threshold in the request headers `x-bf-cache-ttl` and `x-bf-cache-threshold`:

    ```bash  theme={null}
    # HTTP: Custom TTL and threshold
    curl -H "x-bf-cache-key: session-123" \
         -H "x-bf-cache-ttl: 30s" \
         -H "x-bf-cache-threshold: 0.9" ...
    ```
  </Tab>
</Tabs>

***

## Advanced Cache Control

### Cache Type Control

Control which caching mechanism to use per request:

<Tabs group="cache-type-control">
  <Tab title="Go SDK">
    ```go  theme={null}
    // Use only direct hash matching (fastest)
    ctx = context.WithValue(ctx, semanticcache.CacheKey, "session-123")
    ctx = context.WithValue(ctx, semanticcache.CacheTypeKey, semanticcache.CacheTypeDirect)

    // Use only semantic similarity search
    ctx = context.WithValue(ctx, semanticcache.CacheKey, "session-123")  
    ctx = context.WithValue(ctx, semanticcache.CacheTypeKey, semanticcache.CacheTypeSemantic)

    // Default behavior: Direct + semantic fallback (if not specified)
    ctx = context.WithValue(ctx, semanticcache.CacheKey, "session-123")
    ```
  </Tab>

  <Tab title="HTTP API">
    ```bash  theme={null}
    # Direct hash matching only
    curl -H "x-bf-cache-key: session-123" \
         -H "x-bf-cache-type: direct" ...

    # Semantic similarity search only  
    curl -H "x-bf-cache-key: session-123" \
         -H "x-bf-cache-type: semantic" ...

    # Default: Both (if header not specified)
    curl -H "x-bf-cache-key: session-123" ...
    ```
  </Tab>
</Tabs>

### No-Store Control

Disable response caching while still allowing cache reads:

<Tabs group="no-store-control">
  <Tab title="Go SDK">
    ```go  theme={null}
    // Read from cache but don't store the response
    ctx = context.WithValue(ctx, semanticcache.CacheKey, "session-123")
    ctx = context.WithValue(ctx, semanticcache.CacheNoStoreKey, true)
    ```
  </Tab>

  <Tab title="HTTP API">
    ```bash  theme={null}
    # Read from cache but don't store response
    curl -H "x-bf-cache-key: session-123" \
         -H "x-bf-cache-no-store: true" ...
    ```
  </Tab>
</Tabs>

***

## Conversation Configuration

### History Threshold Logic

The `ConversationHistoryThreshold` setting skips caching for conversations with many messages to prevent false positives:

**Why this matters:**

* **Semantic False Positives**: Long conversation histories have high probability of semantic matches with unrelated conversations due to topic overlap
* **Direct Cache Inefficiency**: Long conversations rarely have exact hash matches, making direct caching less effective
* **Performance**: Reduces vector store load by filtering out low-value caching scenarios

```json  theme={null}
{
  "conversation_history_threshold": 3  // Skip caching if > 3 messages in conversation
}
```

**Recommended Values:**

* **1-2**: Very conservative (may miss valuable caching opportunities)
* **3-5**: Balanced approach (default: 3)
* **10+**: Cache longer conversations (higher false positive risk)

### System Prompt Handling

Control whether system messages are included in cache key generation:

```json  theme={null}
{
  "exclude_system_prompt": false  // Include system messages in cache key (default)
}
```

**When to exclude (`true`):**

* System prompts change frequently but content is similar
* Multiple system prompt variations for same use case
* Focus caching on user content similarity

**When to include (`false`):**

* System prompts significantly change response behavior
* Each system prompt requires distinct cached responses
* Strict response consistency requirements

***

## Cache Management

### Cache Metadata Location

When responses are served from semantic cache, 3 key variables are automatically added to the response:

**Location**: `response.ExtraFields.CacheDebug` (as a JSON object)

**Fields**:

* `CacheHit` (boolean): `true` if the response was served from the cache, `false` when lookup fails.
* `HitType` (string): `"semantic"` for similarity match, `"direct"` for hash match
* `CacheID` (string): Unique cache entry ID for management operations (present only for cache hits)

**Semantic Cache Only**:

* `ProviderUsed` (string): Provider used for the calculating semantic match embedding. (present for both cache hits and misses)
* `ModelUsed` (string): Model used for the calculating semantic match embedding. (present for both cache hits and misses)
* `InputTokens` (number): Number of tokens extracted from the request for the semantic match embedding calculation. (present for both cache hits and misses)
* `Threshold` (number): Similarity threshold used for the match. (present only for cache hits)
* `Similarity` (number): Similarity score for the match. (present only for cache hits)

Example HTTP Response:

```json  theme={null}
{
  "extra_fields": {
    "cache_debug": {
      "cache_hit": true,
      "hit_type": "direct",
      "cache_id": "550e8500-e29b-41d4-a725-446655440001",
    }
  }
}

{
  "extra_fields": {
    "cache_debug": {
      "cache_hit": true,
      "hit_type": "semantic",
      "cache_id": "550e8500-e29b-41d4-a725-446655440001",
      "threshold": 0.8,
      "similarity": 0.95,
      "provider_used": "openai",
      "model_used": "gpt-4o-mini",
      "input_tokens": 100
    }
  }
}

{
  "extra_fields": {
    "cache_debug": {
      "cache_hit": false,
      "provider_used": "openai",
      "model_used": "gpt-4o-mini",
      "input_tokens": 20
    }
  }
}
```

These variables allow you to detect cached responses and get the cache entry ID needed for clearing specific entries.

### Clear Specific Cache Entry

Use the request ID from cached responses to clear specific entries:

<Tabs group="cache-clear">
  <Tab title="Go SDK">
    ```go  theme={null}
    // Clear specific entry by request ID
    err := plugin.ClearCacheForRequestID("550e8400-e29b-41d4-a716-446655440000")

    // Clear all entries for a cache key  
    err := plugin.ClearCacheForKey("support-session-456")
    ```
  </Tab>

  <Tab title="HTTP API">
    ```bash  theme={null}
    # Clear specific cached entry by request ID
    curl -X DELETE http://localhost:8080/api/cache/clear/550e8400-e29b-41d4-a716-446655440000

    # Clear all entries for a cache key
    curl -X DELETE http://localhost:8080/api/cache/clear-by-key/support-session-456
    ```
  </Tab>
</Tabs>

### Cache Lifecycle & Cleanup

The semantic cache automatically handles cleanup to prevent storage bloat:

**Automatic Cleanup:**

* **TTL Expiration**: Entries are automatically removed when TTL expires
* **Shutdown Cleanup**: All cache entries are cleared from the vector store namespace and the namespace itself when Bifrost client shuts down
* **Namespace Isolation**: Each Bifrost instance uses isolated vector store namespaces to prevent conflicts

**Manual Cleanup Options:**

* Clear specific entries by request ID (see examples above)
* Clear all entries for a cache key
* Restart Bifrost to clear all cache data

<Warning>
  The semantic cache namespace and all its cache entries are deleted when Bifrost client shuts down **only if `cleanup_on_shutdown` is set to `true`**. By default (`cleanup_on_shutdown: false`), cache data persists between restarts. DO NOT use the plugin's namespace for external purposes.
</Warning>

<Warning>
  **Dimension Changes**: If you update the `dimension` config, the existing namespace will contain data with mixed dimensions, causing retrieval issues. To avoid this, either use a different `vector_store_namespace` or set `cleanup_on_shutdown: true` before restarting.
</Warning>

***

<Info>
  **Vector Store Requirement**: Semantic caching requires a configured vector store (currently Weaviate only). Without vector store setup, the plugin will not function.
</Info>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt