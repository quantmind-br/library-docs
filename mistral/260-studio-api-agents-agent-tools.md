---
title: Agents Tools Overview | Mistral Docs
url: https://docs.mistral.ai/studio-api/agents/agent-tools
source: sitemap
fetched_at: 2026-04-26T04:11:48.760798104-03:00
rendered_js: false
word_count: 129
summary: Enhance agent capabilities by integrating external tools and using built-in functionalities via the API.
tags:
    - ai-agents
    - tool-integration
    - api-functionality
    - built-in-tools
    - external-services
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Agent Tools

Agents use tools to interact with the external world — APIs, databases, or services — extending their functionality beyond their own knowledge base.

![Tools architecture](https://docs.mistral.ai/img/tools_graph.png)![Tools architecture dark](https://docs.mistral.ai/img/tools_graph_dark.png)

## Tool Types

![Built-in tools](https://docs.mistral.ai/img/built_in_graph.png)![Built-in tools dark](https://docs.mistral.ai/img/built_in_graph_dark.png)

### Built-in Tools

Ready out of the box. Execution happens in Mistral's internal environment. Available for direct use via Conversations without creating an Agent first.

> [!info] Built-in tools are only available when using the Agents and/or Conversations APIs.

Specify tools in the `tools` parameter when creating an Agent or calling the Conversations API. Multiple tools can be used simultaneously.

## Available Built-in Tools

| Tool | Description |
|------|-------------|
| `web_search` / `web_search_premium` | Browse the web for real-time information |
| `code_interpreter` | Safely execute Python code in an isolated container |
| `image_generation` | Generate images of various kinds and forms |
| `document_library` | RAG tool for knowledge grounding and search on custom data |

#ai-agents #tool-integration #api-functionality #built-in-tools #external-services
