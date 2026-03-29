---
title: Drop-in Replacement
url: https://docs.getbifrost.ai/features/drop-in-replacement.md
source: llms
fetched_at: 2026-01-21T19:43:35.908770759-03:00
rendered_js: false
word_count: 251
summary: This document explains how to integrate the Bifrost Gateway as a drop-in replacement for popular AI SDKs by simply updating the base URL. It describes how this switch enables advanced features like load balancing, failovers, and governance without requiring changes to existing application logic.
tags:
    - ai-gateway
    - sdk-integration
    - drop-in-replacement
    - load-balancing
    - failover-management
    - openai-compatible
    - multi-provider
category: guide
---

# Drop-in Replacement

> Replace your existing AI SDK connections with Bifrost by changing just the base URL. Keep your code, gain advanced features like fallbacks, load balancing, and governance.

## Zero Code Changes

The Bifrost Gateway acts as a drop-in replacement for popular AI SDKs. This means you can point your existing OpenAI, Anthropic, or Google GenAI client to Bifrost's HTTP gateway and instantly gain access to advanced features without rewriting your application.

The magic happens with a single line change: update your `base_url` to point to Bifrost's gateway, and everything else stays exactly the same.

## How It Works

Bifrost provides **100% compatible endpoints** for popular AI SDKs by acting as a protocol adapter. Your existing SDK code continues to work unchanged, but now benefits from Bifrost's multi-provider support, automatic failovers, semantic caching, and governance features.

<Tabs group="drop-in-replacement">
  <Tab title="OpenAI SDK">
    ```python  theme={null}
    # Before: Direct to OpenAI
    client = openai.OpenAI(
        api_key="your-openai-key"
    )

    # After: Through Bifrost
    client = openai.OpenAI(
        base_url="http://localhost:8080/openai",  # Only change needed
        api_key="dummy-key"  # Keys handled by Bifrost
    )
    ```
  </Tab>

  <Tab title="Anthropic SDK">
    ```python  theme={null}
    # Before: Direct to Anthropic
    client = anthropic.Anthropic(
        api_key="your-anthropic-key"
    )

    # After: Through Bifrost
    client = anthropic.Anthropic(
        base_url="http://localhost:8080/anthropic",  # Only change needed
        api_key="dummy-key"  # Keys handled by Bifrost
    )
    ```
  </Tab>
</Tabs>

## Instant Advanced Features

Once your SDK points to Bifrost, you automatically get:

* **Multi-provider support** with automatic failovers
* **Load balancing** across multiple API keys
* **Semantic caching** for faster responses
* **Governance controls** for usage monitoring and budgets
* **Request/response logging** and analytics
* **Rate limiting** and circuit breakers

and so much more! All without changing a **single line** of your application logic.

## Complete Integration Support

Bifrost provides drop-in compatibility for multiple popular AI SDKs and frameworks:

* **[OpenAI SDK](../integrations/openai-sdk)**
* **[Anthropic SDK](../integrations/anthropic-sdk)**
* **[Google GenAI SDK](../integrations/genai-sdk)**
* **[LiteLLM](../integrations/litellm-sdk)**
* **[LangChain](../integrations/langchain-sdk)**

**For detailed setup instructions and compatibility information:** [Complete Integration Guide](../integrations/what-is-an-integration)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt