---
title: Agentic Research API
url: https://docs.perplexity.ai/docs/grounded-llm/responses/quickstart.md
source: llms
fetched_at: 2026-02-04T07:24:21.313419716-03:00
rendered_js: false
word_count: 694
summary: This document introduces the Agentic Research API, detailing how to install SDKs, authenticate, and implement multi-provider LLM applications with integrated web search and tool capabilities.
tags:
    - agentic-research-api
    - perplexity-ai
    - sdk-installation
    - web-search-tool
    - multi-provider-llm
    - api-authentication
category: api
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Agentic Research API

> The Agentic Research API is a multi-provider, interoperable API specification for building LLM applications. Access models from multiple providers with integrated real-time web search, tool configuration, reasoning control, and token budgets—all through one unified interface.

## Why Use the Agentic Research API?

<CardGroup cols={3}>
  <Card title="Multi-Provider Access" icon="layer-group">
    Access OpenAI, Anthropic, Google, xAI, and more through one unified API, no need to manage multiple API keys.
  </Card>

  <Card title="Transparent Pricing" icon="receipt">
    See exact token counts and costs per request, no markup, just direct provider pricing.
  </Card>

  <Card title="Granular Control" icon="sliders">
    Change models, reasoning, tokens, and tools with consistent syntax.
  </Card>
</CardGroup>

<Info>
  We recommend using our [official SDKs](/docs/sdk/overview) for a more convenient and type-safe way to interact with the Agentic Research API.
</Info>

## Installation

Install the SDK for your preferred language:

<CodeGroup>
  ```bash Python theme={null}
  pip install perplexityai
  ```

  ```bash TypeScript/JavaScript theme={null}
  npm install @perplexity-ai/perplexity_ai
  ```
</CodeGroup>

## Authentication

Set your API key as an environment variable. The SDK will automatically read it:

<Tabs>
  <Tab title="macOS/Linux">
    ```bash  theme={null}
    export PERPLEXITY_API_KEY="your_api_key_here"
    ```
  </Tab>

  <Tab title="Windows">
    ```powershell  theme={null}
    setx PERPLEXITY_API_KEY "your_api_key_here"
    ```
  </Tab>
</Tabs>

Or use a `.env` file in your project:

```bash .env theme={null}
PERPLEXITY_API_KEY=your_api_key_here
```

<Info>
  All SDK examples below automatically use the `PERPLEXITY_API_KEY` environment variable. You can also pass the key explicitly if needed.
</Info>

## Generating an API Key

<Card title="Get your Perplexity API Key" icon="key" arrow="True" horizontal="True" iconType="solid" cta="Click here" href="https://perplexity.ai/account/api">
  Navigate to the **API Keys** tab in the API Portal and generate a new key.
</Card>

## Basic Usage

<Tip>
  **Convenience Property:** Both Python and TypeScript SDKs provide an `output_text` property that aggregates all text content from response outputs. Instead of iterating through `response.output`, simply use `response.output_text` for cleaner code.
</Tip>

### Using a Third-Party Model

Use third-party models from OpenAI, Anthropic, Google, X.AI, and other providers for specific capabilities:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Using a third-party model
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are the latest developments in AI?",
      tools=[{"type": "web_search"}],
      instructions="You have access to a web_search tool. Use it for questions about current events, news, or recent developments. Use 1 query for simple questions. Keep queries brief: 2-5 words. NEVER ask permission to search - just search when appropriate",
  )

  print(f"Response ID: {response.id}")
  print(response.output_text)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are the latest developments in AI?",
      tools: [{ type: "web_search" }],
      instructions: "You have access to a web_search tool. Use it for questions about current events.",
  });

  console.log(`Response ID: ${response.id}`);
  console.log(response.output_text);
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "What are the latest developments in AI?",
      "tools": [{"type": "web_search"}],
      "instructions": "You have access to a web_search tool. Use it for questions about current events.",
      "max_output_tokens": 1000
    }' | jq
  ```
</CodeGroup>

### Using a Preset

Presets provide optimized defaults for specific use cases. Start with a preset for quick setup:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Using a preset (e.g., pro-search)
  response = client.responses.create(
      preset="pro-search",
      input="What are the latest developments in AI?",
  )

  print(f"Response ID: {response.id}")
  print(response.output_text)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Using a preset
  const response = await client.responses.create({
      preset: "pro-search",
      input: "What are the latest developments in AI?",
  });

  console.log(`Response ID: ${response.id}`);
  console.log(response.output_text);
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "preset": "pro-search",
      "input": "What are the latest developments in AI?"
    }' | jq
  ```
</CodeGroup>

### With Web Search Tool

Enable web search capabilities using the `web_search` tool:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What's the weather in San Francisco?",
      tools=[
          {
              "type": "web_search"
          }
      ],
      instructions="You have access to a web_search tool. Use it when you need current information.",
  )

  if response.status == "completed":
      print(response.output_text)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What's the weather in San Francisco?",
      tools: [
          {
              type: "web_search"
          }
      ],
      instructions: "You have access to a web_search tool. Use it when you need current information.",
  });

  if (response.status === "completed") {
      console.log(response.output_text);
  }
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "What'\''s the weather in San Francisco?",
      "tools": [{"type": "web_search"}],
      "instructions": "You have access to a web_search tool. Use it when you need current information."
    }' | jq
  ```
</CodeGroup>

## Input Formats

The `input` parameter accepts either a string or an array of message objects.

### String Input

Simple string input for straightforward queries:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are the latest AI developments?",
  )
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are the latest AI developments?",
  });
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "What are the latest AI developments?"
    }' | jq
  ```
</CodeGroup>

### Message Array Input

Use message arrays for multi-turn conversations:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.responses.create(
      model="openai/gpt-5.2",
      input=[
          {"type": "message", "role": "system", "content": "You are a helpful assistant."},
          {"type": "message", "role": "user", "content": "What are the latest AI developments?"},
      ],
      instructions="Provide detailed, well-researched answers.",
  )
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: [
          { type: "message", role: "system", content: "You are a helpful assistant." },
          { type: "message", role: "user", content: "What are the latest AI developments?" },
      ],
      instructions: "Provide detailed, well-researched answers.",
  });
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": [
        {"type": "message", "role": "system", "content": "You are a helpful assistant."},
        {"type": "message", "role": "user", "content": "What are the latest AI developments?"}
      ],
      "instructions": "Provide detailed, well-researched answers."
    }' | jq
  ```
</CodeGroup>

## Instructions Parameter

The `instructions` parameter provides system instructions or guidelines for the model. This is particularly useful for:

* **Tool usage instructions**: Guide the model on when and how to use available tools
* **Response style guidelines**: Control the tone and format of responses
* **Behavior constraints**: Set boundaries and constraints for model behavior

**Example with tool instructions:**

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are the latest developments in AI?",
      instructions="You have access to a web_search tool. Use it for questions about current events, news, or recent developments. Use 1 query for simple questions. Keep queries brief: 2-5 words. NEVER ask permission to search - just search when appropriate",
      tools=[{"type": "web_search"}],
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are the latest developments in AI?",
      instructions: "You have access to a web_search tool. Use it for questions about current events, news, or recent developments. Use 1 query for simple questions. Keep queries brief: 2-5 words. NEVER ask permission to search - just search when appropriate",
      tools: [{ type: "web_search" }],
  });
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "What are the latest developments in AI?",
      "instructions": "You have access to a web_search tool. Use it for questions about current events, news, or recent developments. Use 1 query for simple questions. Keep queries brief: 2-5 words. NEVER ask permission to search - just search when appropriate",
      "tools": [{"type": "web_search"}]
    }' | jq
  ```
</CodeGroup>

## Tools

The Agentic Research API provides two powerful tools for accessing real-time web information:

* **`web_search`** - Performs web searches to retrieve current information and news
* **`fetch_url`** - Fetches and extracts content from specific URLs

The `web_search` tool can optionally include user location for localized results:

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="What are the latest news in San Francisco?",
      tools=[
          {
              "type": "web_search",
              "user_location": {
                  "latitude": 37.7749,
                  "longitude": -122.4194,
                  "country": "US",
                  "city": "San Francisco",
                  "region": "CA"
              }
          }
      ],
      instructions="Use web_search to find current information.",
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "What are the latest news in San Francisco?",
      tools: [
          {
              type: "web_search",
              user_location: {
                  latitude: 37.7749,
                  longitude: -122.4194,
                  country: "US",
                  city: "San Francisco",
                  region: "CA"
              }
          }
      ],
      instructions: "Use web_search to find current information.",
  });
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "What are the latest news in San Francisco?",
      "tools": [
        {
          "type": "web_search",
          "user_location": {
            "latitude": 37.7749,
            "longitude": -122.4194,
            "country": "US",
            "city": "San Francisco",
            "region": "CA"
          }
        }
      ],
      "instructions": "Use web_search to find current information."
    }' | jq
  ```
</CodeGroup>

## Generation Parameters

Control response generation with standard parameters:

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="Explain quantum computing",
      max_output_tokens=1000,  # Maximum tokens to generate
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "Explain quantum computing",
      max_output_tokens: 1000,  // Maximum tokens to generate
  });
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "Explain quantum computing",
      "max_output_tokens": 1000,
    }' | jq
  ```
</CodeGroup>

## Reasoning Effort

Control the reasoning effort level for reasoning models:

* **`low`**: Minimal reasoning effort
* **`medium`**: Moderate reasoning effort
* **`high`**: Maximum reasoning effort

<Info>
  The `reasoning` parameter is only supported by models with reasoning capabilities. Models without reasoning support will ignore this parameter.
</Info>

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="Solve this complex problem step by step",
      reasoning={
          "effort": "high"  # Use maximum reasoning
      },
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "Solve this complex problem step by step",
      reasoning: {
          effort: "high"  // Use maximum reasoning
      },
  });
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "Solve this complex problem step by step",
      "reasoning": {
        "effort": "high"
      }
    }' | jq
  ```
</CodeGroup>

## Streaming Responses

The Agentic Research API supports streaming responses using Server-Sent Events (SSE). Enable streaming by setting `stream=True`:

<CodeGroup>
  ```python Python theme={null}
  response = client.responses.create(
      model="openai/gpt-5.2",
      input="Explain quantum computing in detail",
      stream=True,
  )

  # Process streaming response
  for chunk in response:
      if chunk.type == "response.output_text.delta":
          print(chunk.delta, end="", flush=True)
      elif chunk.type == "response.completed":
          print(f"\n\nResponse completed: {chunk.response.output_text}")
  ```

  ```typescript TypeScript theme={null}
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      input: "Explain quantum computing in detail",
      stream: true,
  });

  // Process streaming response
  for await (const chunk of response) {
      if (chunk.type === "response.output_text.delta") {
          process.stdout.write(chunk.delta);
      } else if (chunk.type === "response.completed") {
          console.log(`\n\nResponse completed: ${chunk.response.output_text}`);
      }
  }
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "Explain quantum computing in detail",
      "stream": true
    }'
  ```
</CodeGroup>

<Info>
  For comprehensive streaming documentation, see the [Streaming Guide](/docs/grounded-llm/output-control/streaming-responses).
</Info>

## Error Handling

Handle errors gracefully:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity, APIError

  try:
      response = client.responses.create(
          model="openai/gpt-5.2",
          input="What is AI?",
      )

      if response.status == "completed":
          print(response.output_text)
      elif response.status == "failed":
          if response.error:
              print(f"Error: {response.error.message}")

  except APIError as e:
      print(f"API Error: {e.message}")
      print(f"Status Code: {e.status_code}")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  try {
      const response = await client.responses.create({
          model: "openai/gpt-5.2",
          input: "What is AI?",
      });

      if (response.status === "completed") {
          console.log(response.output_text);
      } else if (response.status === "failed") {
          if (response.error) {
              console.error(`Error: ${response.error.message}`);
          }
      }
  } catch (error) {
      if (error instanceof Perplexity.APIError) {
          console.error(`API Error: ${error.message}`);
          console.error(`Status Code: ${error.status}`);
      }
  }
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "What is AI?"
    }' | jq
  ```
</CodeGroup>

## Response Structure

<Accordion title="Response Structure Example">
  Responses from the Agentic Research API have a structured format:

  ```json  theme={null}
  {
      "id": "resp_1234567890",
      "object": "response",
      "created_at": 1234567890,
      "model": "openai/gpt-5.2",
      "status": "completed",
      "output": [
          {
              "type": "message",
              "id": "msg_1234567890",
              "status": "completed",
              "role": "assistant",
              "content": [
                  {
                      "type": "output_text",
                      "text": "The weather in San Francisco is currently sunny...",
                      "annotations": [
                          {
                              "type": "citation",
                              "start_index": 0,
                              "end_index": 50,
                              "url": "https://example.com/weather",
                              "title": "Weather Report"
                          }
                      ]
                  }
              ]
          }
      ],
      "usage": {
          "input_tokens": 100,
          "output_tokens": 200,
          "total_tokens": 300
      }
  }
  ```
</Accordion>

## Next Steps

<CardGroup cols={2}>
  <Card title="Model Fallback" icon="layer-group" href="/docs/grounded-llm/responses/model-fallback">
    Specify multiple models for automatic failover and higher availability.
  </Card>

  <Card title="Presets" icon="gear" href="/docs/grounded-llm/responses/presets">
    Explore available presets and their configurations.
  </Card>

  <Card title="Models" icon="brain" href="/docs/grounded-llm/responses/models">
    Explore available presets and third-party models for the Agentic Research API.
  </Card>

  <Card title="API Reference" icon="code" href="/api-reference/responses-post">
    View complete endpoint documentation and parameters.
  </Card>

  <Card title="Structured Outputs" icon="code" href="/docs/grounded-llm/output-control/structured-outputs">
    Generate formatted responses with JSON schema or regex.
  </Card>

  <Card title="Chat Completions API" icon="message" href="/docs/grounded-llm/chat-completions/quickstart">
    Need web-grounded responses with built-in search? Check out the Chat Completions API.
  </Card>

  <Card title="Search API" icon="magnifying-glass" href="/docs/search/quickstart">
    Get raw search results with the Search API.
  </Card>
</CardGroup>

<Info>
  Need help? Check out our [community](https://community.perplexity.ai) for support and discussions with other developers.
</Info>