---
title: Build an agent with tools | Mistral Docs
url: https://docs.mistral.ai/getting-started/quickstarts/developer/build-an-agent
source: sitemap
fetched_at: 2026-04-26T04:07:08.856419843-03:00
rendered_js: false
word_count: 204
summary: This document explains how to integrate external functions with Mistral models by defining tool schemas, triggering tool calls, and feeding execution results back to the model.
tags:
    - mistral-ai
    - tool-calling
    - function-calling
    - llm-integration
    - api-development
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Give a Mistral model access to external functions it can call mid-conversation.

- Define a tool schema that describes your function
- Send a message that triggers a tool call
- Execute the function locally and feed the result back to the model

The pattern works for any data source: APIs, databases, or internal services.

**Time to complete:** ~10 minutes

**Prerequisites:**
- A Mistral API key
- Python 3.9+ or Node.js 18+
- The Mistral SDK installed

## Define a Tool

Define the function the model can call. This example creates a `get_weather` tool that accepts a city name.

## Trigger a Tool Call

Ask the model a question that requires the tool. The model returns a `tool_calls` response instead of a text answer.

## Process the Result

Run your function with the model's arguments, then send the result back so the model can generate a natural-language answer.

A successful run prints a natural-language response that includes the tool's return value. The model:

- Detected the request needed external data
- Generated a structured `tool_calls` request
- Incorporated your function's result into a conversational answer

## Tool Choice Options

Set `tool_choice: "any"` to force the model to always call a tool, or use `tool_choice: "auto"` (default) to let the model decide.

#tool-calling #function-calling #llm-integration
