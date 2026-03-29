---
title: Integrations
url: https://docs.getbifrost.ai/quickstart/gateway/integrations.md
source: llms
fetched_at: 2026-01-21T19:44:48.869997814-03:00
rendered_js: false
word_count: 236
summary: This document explains how Bifrost integrations act as protocol adapters to provide drop-in compatibility with existing AI provider SDKs. It describes how users can access advanced features like governance and monitoring by simply changing their API base URL without modifying existing code.
tags:
    - ai-integrations
    - sdk-compatibility
    - drop-in-replacement
    - bifrost-api
    - protocol-adapters
    - sdk-integration
category: guide
---

# Integrations

> Use Bifrost as a drop-in replacement for existing AI provider SDKs with zero code changes. Just change the base URL and unlock advanced features.

## What are Integrations?

Integrations are protocol adapters that make Bifrost **100% compatible** with existing AI provider SDKs. They translate between provider-specific API formats (OpenAI, Anthropic, Google GenAI) and Bifrost's unified API, enabling you to:

* **Drop-in replacement** - Change only the base URL in your existing code
* **Zero migration effort** - Keep your current SDK and request/response handling
* **Instant feature access** - Get governance, caching, fallbacks, and monitoring without code changes

## Quick Example

### Before (Direct Provider)

```python  theme={null}
import openai

client = openai.OpenAI(
    api_key="your-openai-key"
)
```

### After (Bifrost Integration)

```python  theme={null}
import openai

client = openai.OpenAI(
    base_url="http://localhost:8080/openai",  # Point to Bifrost
    api_key="dummy-key"  # Keys handled by Bifrost
)
```

**That's it!** Your application now has automatic fallbacks, governance, monitoring, and all Bifrost features.

## Available Integrations

Bifrost provides complete compatibility with these popular AI SDKs:

* **[OpenAI SDK](../../integrations/openai-sdk)**
* **[Anthropic SDK](../../integrations/anthropic-sdk)**
* **[Google GenAI SDK](../../integrations/genai-sdk)**
* **[LiteLLM](../../integrations/litellm-sdk)**
* **[LangChain](../../integrations/langchain-sdk)**

## Learn More

For detailed setup guides, compatibility information, and advanced usage:

**➜ [Complete Integration Documentation](../../integrations/what-is-an-integration)**

## Next Steps

Now that you understand integrations, explore these related topics:

### Essential Topics

* **[Provider Configuration](./provider-configuration)** - Set up multiple AI providers for redundancy
* **[Tool Calling](./tool-calling)** - Enable AI models to use external functions
* **[Streaming Responses](./streaming)** - Real-time response generation
* **[Multimodal AI](./multimodal)** - Process images, audio, and multimedia content

### Advanced Topics

* **[Core Features](../../features/)** - Governance, caching, and observability
* **[Architecture](../../architecture/)** - How Bifrost works internally
* **[Deployment](../../deployment-guides)** - Production setup and scaling


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt