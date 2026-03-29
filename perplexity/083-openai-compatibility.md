---
title: OpenAI Compatibility
url: https://docs.perplexity.ai/docs/grounded-llm/openai-compatibility.md
source: llms
fetched_at: 2026-02-04T07:23:59.15588439-03:00
rendered_js: false
word_count: 799
summary: This document explains how to use OpenAI SDKs to interact with Perplexity's Chat Completions and Agentic Research APIs by updating the base URL and API key.
tags:
    - openai-compatibility
    - perplexity-api
    - sdk-integration
    - chat-completions
    - agentic-research
    - python
    - typescript
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI Compatibility

> Use your existing OpenAI SDKs with Perplexity's Chat Completions and Agentic Research APIs. Full compatibility with minimal code changes.

## Overview

Perplexity's APIs are fully compatible with OpenAI's SDKs. You can use your existing OpenAI client libraries with both the **Chat Completions API** and **Agentic Research API** by simply changing the base URL and providing your Perplexity API key.

<Tip>
  **We recommend using the [Perplexity SDK](/docs/sdk/overview)** for the best experience with full type safety, enhanced features, and preset support. Use OpenAI SDKs if you're already integrated and need drop-in compatibility.
</Tip>

## Quick Start

### Chat Completions API

Use the OpenAI SDK with Perplexity's Chat Completions API:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v2"
    )

    completion = client.chat.completions.create(
        model="sonar-pro",
        messages=[
            {"role": "user", "content": "What are the latest developments in AI?"}
        ]
    )

    print(completion.choices[0].message.content)
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v2"
    });

    const completion = await client.chat.completions.create({
      model: "sonar-pro",
      messages: [
        { role: "user", content: "What are the latest developments in AI?" }
      ]
    });

    console.log(completion.choices[0].message.content);
    ```
  </Tab>
</Tabs>

### Agentic Research API

Use the OpenAI SDK with Perplexity's Agentic Research API:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v2"
    )

    response = client.responses.create(
        model="openai/gpt-5-mini",
        input="What are the latest developments in AI?"
    )


    print(response.output_text)
            break
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v2"
    });

    const response = await client.responses.create({
      model: "openai/gpt-5-mini",
      input: "What are the latest developments in AI?"
    });

    console.log(response.output_text);
    ```
  </Tab>
</Tabs>

## Configuration

### Setting Up the OpenAI SDK

Configure OpenAI SDKs to work with Perplexity by setting the `base_url` to `https://api.perplexity.ai/v2`:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_PERPLEXITY_API_KEY",
        base_url="https://api.perplexity.ai/v2"
    )
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_PERPLEXITY_API_KEY",
      baseURL: "https://api.perplexity.ai/v2"
    });
    ```
  </Tab>
</Tabs>

<Info>
  **Important**: Use `base_url="https://api.perplexity.ai/v2"` (with `/v2`) for both Chat Completions and Agentic Research APIs.
</Info>

## Chat Completions API

Perplexity's Chat Completions API is fully compatible with OpenAI's Chat Completions interface.

### Basic Usage

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v2"
    )

    completion = client.chat.completions.create(
        model="sonar-pro",
        messages=[
            {"role": "user", "content": "What are the latest developments in AI?"}
        ]
    )

    print(completion.choices[0].message.content)
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v2"
    });

    const completion = await client.chat.completions.create({
      model: "sonar-pro",
      messages: [
        { role: "user", content: "What are the latest developments in AI?" }
      ]
    });

    console.log(completion.choices[0].message.content);
    ```
  </Tab>
</Tabs>

### Streaming

Streaming works exactly like OpenAI's API:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v2"
    )

    stream = client.chat.completions.create(
        model="sonar-pro",
        messages=[
            {"role": "user", "content": "What are the latest developments in AI?"}
        ],
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v2"
    });

    const stream = await client.chat.completions.create({
      model: "sonar-pro",
      messages: [
        { role: "user", content: "What are the latest developments in AI?" }
      ],
      stream: true
    });

    for await (const chunk of stream) {
      if (chunk.choices[0]?.delta?.content) {
        process.stdout.write(chunk.choices[0].delta.content);
      }
    }
    ```
  </Tab>
</Tabs>

### Perplexity-Specific Parameters

Add Perplexity-specific search parameters using `extra_body` (Python) or direct parameters (TypeScript):

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v2"
    )

    completion = client.chat.completions.create(
        model="sonar-pro",
        messages=[
            {"role": "user", "content": "Latest climate research findings"}
        ],
        extra_body={
            "search_domain_filter": ["nature.com", "science.org"],
            "search_recency_filter": "month"
        }
    )

    print(completion.choices[0].message.content)
    print(f"Sources: {len(completion.search_results)} articles found")
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v2"
    });

    const completion = await client.chat.completions.create({
      model: "sonar-pro",
      messages: [
        { role: "user", content: "Latest climate research findings" }
      ],
      search_domain_filter: ["nature.com", "science.org"],
      search_recency_filter: "month"
    });

    console.log(completion.choices[0].message.content);
    console.log(`Sources: ${completion.search_results.length} articles found`);
    ```
  </Tab>
</Tabs>

## Agentic Research API

Perplexity's Agentic Research API is fully compatible with OpenAI's Agentic Research API interface.

### Basic Usage

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v2"
    )

    response = client.responses.create(
        model="openai/gpt-5-mini",
        input="What are the latest developments in AI?"
    )


    print(response.output_text)
            break
    print(f"Response ID: {response.id}")
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v2"
    });

    const response = await client.responses.create({
      model: "openai/gpt-5-mini",
      input: "What are the latest developments in AI?"
    });

    console.log(response.output_text);
    console.log(`Response ID: ${response.id}`);
    ```
  </Tab>
</Tabs>

### Using Presets

Presets are pre-configured setups optimized for specific use cases. Use the `extra_body` parameter (Python) or cast the parameter (TypeScript) to pass presets:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v2"
    )

    # Use a preset instead of specifying model and parameters
    response = client.responses.create(
        input="What are the latest developments in AI?",
        extra_body={
            "preset": "pro-search"
        }
    )


    print(response.output_text)
            break
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v2"
    });

    // Use a preset instead of specifying model and parameters
    const response = await client.responses.create({
      input: "What are the latest developments in AI?",
      preset: "pro-search"
    } as any);

    console.log(response.output_text);
    ```
  </Tab>
</Tabs>

<Info>
  See [Agentic Research API Presets](/docs/grounded-llm/agentic-research/presets) for available presets and their configurations.
</Info>

### Using Third-Party Models

You can also specify third-party models directly instead of using presets:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v2"
    )

    response = client.responses.create(
        model="openai/gpt-5-mini",
        input="What are the latest developments in AI?"
    )


    print(response.output_text)
            break
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v2"
    });

    const response = await client.responses.create({
      model: "openai/gpt-5-mini",
      input: "What are the latest developments in AI?"
    });

    console.log(response.output_text);
    ```
  </Tab>
</Tabs>

### Streaming Responses

Streaming works with the Agentic Research API:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v2"
    )

    response = client.responses.create(
        model="openai/gpt-5-mini",
        input="Write a bedtime story about a unicorn.",
        stream=True
    )

    for event in response:
        if event.type == "response.output_text.delta":
            print(event.delta, end="", flush=True)
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v2"
    });

    const response = await client.responses.create({
      model: "openai/gpt-5-mini",
      input: "Write a bedtime story about a unicorn.",
      stream: true
    });

    for await (const event of response) {
      if (event.type === "response.output_text.delta") {
        process.stdout.write(event.delta);
      }
    }
    ```
  </Tab>
</Tabs>

### Using Tools

The Agentic Research API supports tools, including web search:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v2"
    )

    response = client.responses.create(
        model="openai/gpt-5-mini",
        input="What are the latest developments in AI?",
        tools=[
            {
                "type": "web_search",
                "filters": {
                    "search_domain_filter": ["techcrunch.com", "wired.com"]
                }
            }
        ],
        instructions="You have access to a web_search tool. Use it for current information."
    )


    print(response.output_text)
            break
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    import OpenAI from 'openai';

    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai/v2"
    });

    const response = await client.responses.create({
      model: "openai/gpt-5-mini",
      input: "What are the latest developments in AI?",
      tools: [
        {
          type: "web_search",
          filters: {
            search_domain_filter: ["techcrunch.com", "wired.com"]
          }
        }
      ],
      instructions: "You have access to a web_search tool. Use it for current information."
    });

    console.log(response.output_text);
    ```
  </Tab>
</Tabs>

## API Compatibility

### Standard OpenAI Parameters

These parameters work exactly the same as OpenAI's API:

**Chat Completions API:**

* `model` - Model name (use Perplexity model names like `sonar-pro`)
* `messages` - Chat messages array
* `max_tokens` - Maximum tokens in response
* `stream` - Enable streaming responses

**Agentic Research API:**

* `model` - Model name (use 3rd party models like `openai/gpt-5.2`)
* `input` - Input text or message array
* `instructions` - System instructions
* `max_output_tokens` - Maximum tokens in response
* `stream` - Enable streaming responses
* `tools` - Array of tools including `web_search`

### Perplexity-Specific Parameters

**Chat Completions API:**

* `search_domain_filter` - Limit or exclude specific domains
* `search_recency_filter` - Filter by content recency
* `return_images` - Include image URLs in response
* `return_related_questions` - Include related questions
* `search_mode` - "web" (default) or "academic" mode selector

**Agentic Research API:**

* `preset` - Preset name (use Perplexity presets like `pro-search`)
* `tools[].filters` - Search filters within web\_search tool
* `tools[].user_location` - User location for localized results

<Info>
  See [Chat Completions API Reference](/api-reference/chat-completions-post) and [Agentic Research API Reference](/api-reference/responses-post) for complete parameter details.
</Info>

## Response Structure

### Chat Completions API

Perplexity responses match OpenAI's format exactly:

* `choices[0].message.content` - The AI-generated response
* `model` - The model name used
* `usage` - Token consumption details
* `id`, `created`, `object` - Standard response metadata
* `search_results` - Array of web sources (Perplexity-specific)
* `citations` - Array of citation URLs (Perplexity-specific)

### Agentic Research API

Perplexity Agentic Research API matches OpenAI's Agentic Research API format:

* `output` - Structured output array containing messages with `content[].text`
* `model` - The model name used
* `usage` - Token consumption details
* `id`, `created_at`, `status` - Response metadata

## Best Practices

<Steps>
  <Step title="Use the correct base URL">
    Always use `https://api.perplexity.ai/v2` (with `/v2`) for both APIs.

    ```python  theme={null}
    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.perplexity.ai/v2"  # Correct
    )
    ```
  </Step>

  <Step title="Choose the right API">
    * **Chat Completions API**: Best for web-grounded conversations with built-in search
    * **Agentic Research API**: Best for structured outputs, third-party models, and tool use

    ```python  theme={null}
    # Chat Completions - web search built-in
    completion = client.chat.completions.create(
        model="sonar-pro",
        messages=[{"role": "user", "content": "Latest AI news"}]
    )

    # Responses - explicit tool control
    response = client.responses.create(
        model="openai/gpt-5-mini",
        input="Latest AI news",
        tools=[{"type": "web_search"}]
    )
    ```
  </Step>

  <Step title="Handle errors gracefully">
    Use the OpenAI SDK's error handling:

    ```python  theme={null}
    from openai import OpenAI, APIError, RateLimitError

    try:
        completion = client.chat.completions.create(...)
    except RateLimitError:
        print("Rate limit exceeded, please retry later")
    except APIError as e:
        print(f"API error: {e.message}")
    ```
  </Step>

  <Step title="Use streaming for better UX">
    Stream responses for real-time user experience:

    ```python  theme={null}
    stream = client.chat.completions.create(
        model="sonar-pro",
        messages=[{"role": "user", "content": "Long query..."}],
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    ```
  </Step>
</Steps>

## Recommended: Perplexity SDK

We recommend using Perplexity's native SDKs for the best developer experience:

* **Cleaner preset syntax** - Use `preset="pro-search"` directly instead of `extra_body={"preset": "pro-search"}`
* **Type safety** - Full TypeScript/Python type definitions for all parameters
* **Enhanced features** - Direct access to all Perplexity-specific features
* **Better error messages** - Perplexity-specific error handling
* **Simpler setup** - No need to configure base URLs

See the [Perplexity SDK Guide](/docs/sdk/overview) for details.

## Next Steps

<CardGroup cols={2}>
  <Card title="Chat Completions Quickstart" icon="message" href="/docs/grounded-llm/chat-completions/quickstart">
    Get started with Chat Completions API using OpenAI SDKs.
  </Card>

  <Card title="Responses Quickstart" icon="reply" href="/docs/grounded-llm/responses/quickstart">
    Get started with Agentic Research API using OpenAI SDKs.
  </Card>

  <Card title="Prompt Guide" icon="book" href="/docs/grounded-llm/prompting/prompt-guide">
    Learn best practices for prompting both APIs.
  </Card>

  <Card title="API Reference" icon="code" href="/docs/api-reference/chat-completions-post">
    View complete API documentation for both endpoints.
  </Card>
</CardGroup>

## Migrating to the Perplexity SDK

Switch to the Perplexity SDK for enhanced features and cleaner syntax. With the Perplexity SDK, you can use presets directly without `extra_body` and get full type safety:

<Steps>
  <Step title="Install the Perplexity SDK">
    <Tabs>
      <Tab title="Python">
        ```bash  theme={null}
        pip install perplexityai
        ```
      </Tab>

      <Tab title="TypeScript">
        ```bash  theme={null}
        npm install @perplexity-ai/perplexity_ai
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Update the import and client">
    <Tabs>
      <Tab title="Python">
        ```python  theme={null}
        # Before (OpenAI SDK)
        from openai import OpenAI
        client = OpenAI(
            api_key="pplx-...",
            base_url="https://api.perplexity.ai/v2"
        )

        # After (Perplexity SDK)
        from perplexity import Perplexity
        client = Perplexity(api_key="pplx-...")
        # Or just: client = Perplexity() if PERPLEXITY_API_KEY env var is set
        ```
      </Tab>

      <Tab title="TypeScript">
        ```typescript  theme={null}
        // Before (OpenAI SDK)
        import OpenAI from 'openai';
        const client = new OpenAI({
          apiKey: "pplx-...",
          baseURL: "https://api.perplexity.ai/v2"
        });

        // After (Perplexity SDK)
        import Perplexity from '@perplexity-ai/perplexity_ai';
        const client = new Perplexity({ apiKey: "pplx-..." });
        // Or just: const client = new Perplexity() if PERPLEXITY_API_KEY env var is set
        ```
      </Tab>
    </Tabs>

    <Info>
      **No base URL needed** - The Perplexity SDK automatically uses the correct endpoint.
    </Info>
  </Step>

  <Step title="Update the API calls">
    The API calls are very similar:

    <Tabs>
      <Tab title="Python">
        ```python  theme={null}
        # Chat Completions API - same interface
        completion = client.chat.completions.create(
            model="sonar-pro",
            messages=[{"role": "user", "content": "Hello!"}]
        )

        # Agentic Research API - same interface
        response = client.responses.create(
            model="openai/gpt-5-mini",
            input="Hello!"
        )
        ```
      </Tab>

      <Tab title="TypeScript">
        ```typescript  theme={null}
        // Chat Completions API - same interface
        const completion = await client.chat.completions.create({
          model: "pro-search",
          messages: [{ role: "user", content: "Hello!" }]
        });

        // Agentic Research API - same interface
        const response = await client.responses.create({
          model: "openai/gpt-5-mini",
          input: "Hello!"
        });
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Use presets with cleaner syntax">
    The Perplexity SDK supports presets with cleaner syntax compared to OpenAI SDK:

    <Tabs>
      <Tab title="Python">
        ```python  theme={null}
        # Before (OpenAI SDK) - extra_body required
        response = client.responses.create(
            input="What are the latest developments in AI?",
            extra_body={"preset": "pro-search"}
        )

        # After (Perplexity SDK) - direct parameter
        response = client.responses.create(
            preset="pro-search",
            input="What are the latest developments in AI?"
        )
        ```
      </Tab>

      <Tab title="TypeScript">
        ```typescript  theme={null}
        // Before (OpenAI SDK) - type casting required
        const response = await client.responses.create({
          input: "What are the latest developments in AI?",
          preset: "pro-search"
        } as any);

        // After (Perplexity SDK) - fully typed
        const response = await client.responses.create({
          preset: "pro-search",
          input: "What are the latest developments in AI?"
        });
        ```
      </Tab>
    </Tabs>
  </Step>
</Steps>