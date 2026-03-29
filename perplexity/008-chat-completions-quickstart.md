---
title: Chat Completions API
url: https://docs.perplexity.ai/docs/grounded-llm/chat-completions/quickstart.md
source: llms
fetched_at: 2026-02-04T07:23:47.404518284-03:00
rendered_js: false
word_count: 347
summary: This document provides a comprehensive guide for integrating Perplexity's Chat Completions API, covering installation, authentication, and basic implementation of web-grounded AI responses.
tags:
    - perplexity-api
    - chat-completions
    - sdk-installation
    - openai-compatibility
    - streaming-responses
    - web-grounded-ai
    - api-authentication
    - developer-tools
category: api
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Chat Completions API

> Get started with Perplexity's Chat Completions API for web-grounded AI responses. Make your first API call in minutes.

## Overview

Perplexity's Chat Completions API provides web-grounded AI responses with support for streaming, tools, search options, and more. You can use it with OpenAI-compatible client libraries or our native SDKs for type safety and enhanced features.

Use the Chat Completions API when you need web search capabilities built-in, streaming responses, or Perplexity's Sonar models. For structured outputs and third-party models, use our [Agentic Research API](/docs/grounded-llm/responses/quickstart).

<Tip>
  Keep using your existing OpenAI SDKs to get started fast; switch to our [native SDKs](/docs/sdk/overview) later as needed.
</Tip>

## Installation

Install the SDK for your preferred language:

<CodeGroup>
  ```bash Python theme={null}
  pip install perplexityai
  ```

  ```bash TypeScript/JavaScript theme={null}
  npm install @perplexity-ai/perplexity_ai
  ```

  ```bash OpenAI Python (Compatible) theme={null}
  pip install openai
  ```

  ```bash OpenAI TypeScript (Compatible) theme={null}
  npm install openai
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

<Note>
  **OpenAI SDK Compatible:** Perplexity's API supports the OpenAI Chat Completions format. You can use OpenAI client libraries by pointing to our endpoint.
</Note>

## Basic Usage

### Non-Streaming Request

<CodeGroup>
  ```python Python SDK theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  completion = client.chat.completions.create(
      model="sonar-pro",
      messages=[
          {"role": "user", "content": "What were the results of the 2025 French Open Finals?"}
      ]
  )

  print(completion.choices[0].message.content)
  ```

  ```typescript TypeScript SDK theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const completion = await client.chat.completions.create({
      model: "sonar-pro",
      messages: [
          { role: "user", content: "What were the results of the 2025 French Open Finals?" }
      ],
  });

  console.log(completion.choices[0].message.content);
  ```

  ```python OpenAI Python SDK theme={null}
  from openai import OpenAI

  client = OpenAI(
      api_key="YOUR_API_KEY",
      base_url="https://api.perplexity.ai"
  )

  resp = client.chat.completions.create(
      model="sonar-pro",
      messages=[
          {"role": "user", "content": "What were the results of the 2025 French Open Finals?"}
      ]
  )
  print(resp.choices[0].message.content)
  ```

  ```typescript OpenAI TypeScript SDK theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai"
  });

  const resp = await client.chat.completions.create({
      model: "sonar-pro",
      messages: [
          { role: "user", content: "What were the results of the 2025 French Open Finals?" }
      ],
  });
  console.log(resp.choices[0].message.content);
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/chat/completions \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "sonar-pro",
      "messages": [
        {
          "role": "user",
          "content": "What were the results of the 2025 French Open Finals?"
        }
      ]
    }' | jq
  ```
</CodeGroup>

### Streaming Response

<CodeGroup>
  ```python Python SDK theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  stream = client.chat.completions.create(
      model="sonar-pro",
      messages=[
          {"role": "user", "content": "What are the most popular open-source alternatives to OpenAI's GPT models?"}
      ],
      stream=True
  )

  for chunk in stream:
      if chunk.choices[0].delta.content:
          print(chunk.choices[0].delta.content, end="")
  ```

  ```typescript TypeScript SDK theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const stream = await client.chat.completions.create({
      model: "sonar-pro",
      messages: [
          { role: "user", content: "What are the most popular open-source alternatives to OpenAI's GPT models?" }
      ],
      stream: true,
  });

  for await (const chunk of stream) {
      if (chunk.choices[0].delta.content) {
          process.stdout.write(chunk.choices[0].delta.content);
      }
  }
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/chat/completions \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "sonar-pro",
      "messages": [
        {
          "role": "user",
          "content": "What are the most popular open-source alternatives to OpenAI'\''s GPT models?"
        }
      ],
      "stream": true
    }'
  ```
</CodeGroup>

<Info title="Complete Streaming Guide" href="/docs/grounded-llm/output-control/streaming-responses">
  For a full guide on streaming, including parsing, error handling, citation management, and best practices, see our [streaming guide](/docs/grounded-llm/output-control/streaming-responses).
</Info>

## Response Structure

Chat Completions responses follow the OpenAI-compatible format:

```json  theme={null}
{
    "id": "pplx-1234567890",
    "model": "sonar-pro",
    "created": 1234567890,
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "The 2025 French Open Finals results..."
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 12,
        "completion_tokens": 315,
        "total_tokens": 327
    }
}
```

## Next Steps

<CardGroup cols={2}>
  <Card title="Chat Completions Guide" icon="book" href="/docs/grounded-llm/openai-compatibility">
    Complete guide to the Chat Completions API with advanced features and examples.
  </Card>

  <Card title="Models" icon="brain" href="/docs/grounded-llm/chat-completions/models">
    Explore available Sonar models and their capabilities.
  </Card>

  <Card title="API Reference" icon="code" href="/api-reference/chat-completions-post">
    View complete endpoint documentation and parameters.
  </Card>

  <Card title="Search Controls" icon="magnifying-glass" href="/docs/grounded-llm/chat-completions/filters/search-control">
    Learn how to control search behavior with filters and parameters.
  </Card>

  <Card title="Agentic Research API" icon="code" href="/docs/grounded-llm/responses/quickstart">
    Need structured outputs or third-party models? Check out the Agentic Research API.
  </Card>

  <Card title="Search API" icon="magnifying-glass" href="/docs/search/quickstart">
    Get raw search results with the Search API.
  </Card>
</CardGroup>

<Info>
  Need help? Check out our [community](https://community.perplexity.ai) for support and discussions with other developers.
</Info>