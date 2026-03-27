---
title: Building an AI Research Assistant with Firecrawl and AI SDK - Firecrawl Docs
url: https://docs.firecrawl.dev/developer-guides/cookbooks/ai-research-assistant-cookbook
source: sitemap
fetched_at: 2026-03-23T07:39:50.41623-03:00
rendered_js: false
word_count: 579
summary: This document provides a technical walkthrough for building an AI-powered research assistant that utilizes tool calling to perform real-time web scraping and search tasks.
tags:
    - ai-sdk
    - web-scraping
    - tool-calling
    - nextjs
    - openai
    - firecrawl
    - agent-development
category: tutorial
---

Build a complete AI-powered research assistant that can scrape websites and search the web to answer questions. The assistant automatically decides when to use web scraping or search tools to gather information, then provides comprehensive answers based on collected data. ![AI research assistant chatbot interface showing real-time web scraping with Firecrawl and conversational responses powered by OpenAI](https://mintcdn.com/firecrawl/GKat0bF5SiRAHSEa/images/guides/cookbooks/ai-sdk-cookbook/firecrawl-ai-sdk-chatbot.gif?s=cfcbad69aa3f087a474414c0763a260b)

## What You’ll Build

An AI chat interface where users can ask questions about any topic. The AI assistant automatically decides when to use web scraping or search tools to gather information, then provides comprehensive answers based on the data it collects.

## Prerequisites

- Node.js 18 or later installed
- An OpenAI API key from [platform.openai.com](https://platform.openai.com)
- A Firecrawl API key from [firecrawl.dev](https://firecrawl.dev)
- Basic knowledge of React and Next.js

## How It Works

### Message Flow

1. **User sends a message**: The user types a question and clicks submit
2. **Frontend sends request**: `useChat` sends the message to `/api/chat` with the selected model and web search setting
3. **Backend processes message**: The API route receives the message and calls `streamText`
4. **AI decides on tools**: The model analyzes the question and decides whether to use `scrapeWebsite` or `searchWeb` (only if web search is enabled)
5. **Tools execute**: If tools are called, Firecrawl scrapes or searches the web
6. **AI generates response**: The model analyzes tool results and generates a natural language response
7. **Frontend displays results**: The UI shows tool calls and the final response in real-time

### Tool Calling Process

The AI SDK’s tool calling system ([ai-sdk.dev/docs/foundations/tools](https://ai-sdk.dev/docs/foundations/tools)) works as follows:

1. The model receives the user’s message and available tool descriptions
2. If the model determines a tool is needed, it generates a tool call with parameters
3. The SDK executes the tool function with those parameters
4. The tool result is sent back to the model
5. The model uses the result to generate its final response

This all happens automatically within a single `streamText` call, with results streaming to the frontend in real-time.

## Key Features

### Model Selection

The application supports multiple OpenAI models:

- **GPT-5 Mini (Thinking)**: Recent OpenAI model with advanced reasoning capabilities
- **GPT-4o Mini**: Fast and cost-effective model

Users can switch between models using the dropdown selector.

### Web Search Toggle

The Search button controls whether the AI can use Firecrawl tools:

- **Enabled**: AI can call `scrapeWebsite` and `searchWeb` tools as needed
- **Disabled**: AI responds only with its training knowledge

This gives users control over when to use web data versus the model’s built-in knowledge.

## Customization Ideas

### Add More Tools

Extend the assistant with additional tools:

- Database lookups for internal company data
- CRM integration to fetch customer information
- Email sending capabilities
- Document generation

Each tool follows the same pattern: define a schema with Zod, implement the execute function, and register it in the `tools` object.

### Change the AI Model

Swap OpenAI for another provider:

```
import { anthropic } from "@ai-sdk/anthropic";

const result = streamText({
  model: anthropic("claude-4.5-sonnet"),
  // ... rest of config
});
```

The AI SDK supports 20+ providers with the same API. Learn more: [ai-sdk.dev/docs/foundations/providers-and-models](https://ai-sdk.dev/docs/foundations/providers-and-models).

### Customize the UI

AI Elements components are built on shadcn/ui, so you can:

- Modify component styles in the component files
- Add new variants to existing components
- Create custom components that match the design system

## Best Practices

1. **Use appropriate tools**: Choose `searchWeb` to find relevant pages first, `scrapeWebsite` for single pages, or let the AI decide
2. **Monitor API usage**: Track your Firecrawl and OpenAI API usage to avoid unexpected costs
3. **Handle errors gracefully**: The tools include error handling, but consider adding user-facing error messages
4. **Optimize performance**: Use streaming to provide immediate feedback and consider caching frequently accessed content
5. **Set reasonable limits**: The `stopWhen: stepCountIs(5)` prevents excessive tool calls and runaway costs

* * *