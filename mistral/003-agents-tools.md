---
title: Agents Tools Overview | Mistral Docs
url: https://docs.mistral.ai/agents/tools
source: crawler
fetched_at: 2026-01-29T07:33:13.014196033-03:00
rendered_js: false
word_count: 254
summary: This document explains how AI agents can leverage built-in, local, and MCP server tools to interact with external services and extend their functional capabilities.
tags:
    - ai-agents
    - tool-integration
    - function-calling
    - mcp-protocol
    - built-in-tools
    - llm-capabilities
category: concept
---

Agents can use tools to interact with the external world, these can be APIs, databases, or other services, increasing the capabilities of your agent and extending its functionality beyond its own knowledge base and fixed environment.

![tools_graph](https://docs.mistral.ai/img/tools_graph.png)![tools_graph](https://docs.mistral.ai/img/tools_graph_dark.png)

## Tool Types

We provide a variety of different **types** of tools agents can laverage.

TypeDescription[Built-In](https://docs.mistral.ai/agents/tools/built-in)These are available tools out of the box we provide, these can be called at any given point and all execution happens in our internal environment and cloud.[Functions](https://docs.mistral.ai/agents/tools/function_calling)Custom local tools, these are usually functions that are defined in your local environment or code and can be called by the agent, execution happens in your local environment.[MCP Servers](https://docs.mistral.ai/agents/tools/mcp)Following the Model Context Protocol, we provide an SDK compatible which allows you to create or leverage tools from created servers that can be called by the agent, execution happens in your local environment and/or cloud provider hosting the MCP server.

## Built-In

Below is a list of the built-in tools currently available.

TypeDescription[Web Search](https://docs.mistral.ai/agents/tools/built-in/websearch)Allows searching the web for information, this is useful for finding up to date information or information that is not in the agents knowledge.[Code Interpreter](https://docs.mistral.ai/agents/tools/built-in/code_interpreter)Can run code and generate plots, this is useful for data analysis, visualization or running code in a sandboxed environment.[Image Generation](https://docs.mistral.ai/agents/tools/built-in/image_generation)Generates images, this is useful for creating images based on a prompt or description.[Document Library](https://docs.mistral.ai/agents/tools/built-in/document_library)Provides access to read and search through a vast amount of documents, this is useful for finding information in documents or PDFs and perform RAG (Retrieval Augmented Generation) to answer questions based on very specific information.