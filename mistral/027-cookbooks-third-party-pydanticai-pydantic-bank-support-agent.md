---
title: Build a bank support agent with Pydantic AI and Mistral AI - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-pydanticai-pydantic_bank_support_agent
source: crawler
fetched_at: 2026-01-29T07:33:51.934538965-03:00
rendered_js: false
word_count: 447
summary: This document provides a step-by-step tutorial on building a bank support agent using Mistral AI and PydanticAI. It explains how to implement structured responses, dependency injection, and tool integration for real-time information retrieval.
tags:
    - mistral-ai
    - pydantic-ai
    - structured-outputs
    - ai-agents
    - tool-calling
    - python
    - dependency-injection
category: tutorial
---

In this cookbook, we'll demonstrate how to build a bank support agent using Mistral AI and PydanticAI, which offers the following features:

- Structured Responses: Pydantic ensures that outputs conform to a predefined schema, providing consistent and validated responses.
- External Dependencies: Enhance AI interactions by integrating external dependencies, such as databases, through a type-safe dependency injection system.
- Dynamic Context: System prompt functions allow the injection of runtime information, like a customer's name, into the agent's context, enabling personalized interactions.
- Tool Integration: The agent can invoke tools for real-time information retrieval, enhancing its capabilities beyond static responses.

Example in this cookbook is adapted from [https://ai.pydantic.dev/](https://ai.pydantic.dev/).

If you're running pydantic-ai in a jupyter notebook or Colab, you will need nest-asyncio to manage conflicts between event loops that occur between jupyter's event loops and pydantic-ai's:

## Example 1: Basic Q&A with Mistral

Let's start with a straightforward example using Pydantic AI for a basic Q&A with Mistral.

We'll define an agent powered by Mistral with a system prompt designed to ensure concise responses. When we ask about the origin of “hello world,” the model will provide a brief, one-sentence answer.

## Example 2: Bank support agent

In this more complex example, we build a bank support agent.

## Step 1: Define a database

In more advanced AI workflows, your model may require external data, such as information from a database. Here, we define a fictional database class that retrieves a customer's name and balance. In a real-world scenario, this class could connect to a live database. The agent can use these methods to respond to customer inquiries effectively.

## Step 2: Define the bank support agent

In this step, we define how the support agent works by setting up its input dependencies and expected output format.

Code Breakdown:

Why This Design Matters:

- By defining input dependencies and output formats, we guarantee that the agent always receives the correct data and produces predictable results. This makes integration into larger systems easier and supports clear, actionable responses.

## Step 3: Add a dynamic system prompt

This code attaches a dynamic system prompt function. Before the model sees the user's query, it gets a special system prompt enriched with the customer's name.

## Step 4: Defining tools that the agent can use

By decorating customer\_balance with @support\_agent.tool, we're telling the model it can call this function to retrieve the customer's balance. This transforms the model from a passive text generator into an active problem solver that can interact with external resources.

## Step 5: Run agent

When asked about the customer’s balance, the agent uses the injected dependencies and tools to return a structured response.

You can check the results and message history including the system prompt and the tool usage: