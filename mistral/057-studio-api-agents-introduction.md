---
title: Agents Introduction | Mistral Docs
url: https://docs.mistral.ai/studio-api/agents/introduction
source: sitemap
fetched_at: 2026-04-26T04:12:02.694818448-03:00
rendered_js: false
word_count: 277
summary: This document provides an overview of AI agents powered by large language models, detailing the features and tools available within the Agents and Conversations API to build autonomous workflows.
tags:
    - ai-agents
    - llm-framework
    - agentic-workflows
    - api-integration
    - tool-calling
    - multimodal-models
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## What are AI agents?

AI agents are autonomous systems powered by large language models (LLMs) that, given high-level instructions, can plan, use tools, carry out processing steps, and take actions to achieve specific goals. These agents use advanced natural language processing to understand and execute complex tasks and can collaborate with each other.

![agents_graph](https://docs.mistral.ai/img/agent_overview.png)![agents_graph](https://docs.mistral.ai/img/agent_overview_dark.png)

## Agents and Conversations API

The Agents and Conversations API enables developers to build agents with these features:

| Feature | Description |
|---------|-------------|
| **Multimodal models** | Text and vision models available |
| **Persistent state** | State persists across conversations |
| **Conversation types** | Base models, single agent, or multiple agents |
| **Built-in connectors** | Code execution, web search, image generation, document library |
| **Handoffs** | Use different agents as tools in workflows |
| **Structured outputs** | Supported via chat completions |
| **Document understanding** | Supported via chat completions |
| **Tool usage** | Supported via chat completions |
| **Citations** | Supported via chat completions |

## Related Documentation

- [**Agents & Conversations API**](https://docs.mistral.ai/studio-api/agents/agents-api): Basic explanations and code snippets
- [**Tools**](https://docs.mistral.ai/studio-api/agents/agent-tools): Make tools accessible to any Agent
  - [Websearch](https://docs.mistral.ai/studio-api/agents/agent-tools/websearch)
  - [Code Interpreter](https://docs.mistral.ai/studio-api/agents/agent-tools/code_interpreter)
  - [Image Generation](https://docs.mistral.ai/studio-api/agents/agent-tools/image_generation)
  - [Document Library](https://docs.mistral.ai/studio-api/knowledge-rag/libraries)
  - [Function Calling](https://docs.mistral.ai/studio-api/agents/agent-tools/function-calling)
  - [Connectors](https://docs.mistral.ai/studio-api/knowledge-rag/connectors)
- [**Handoffs**](https://docs.mistral.ai/studio-api/agents/handoffs): Relay tasks and use other agents as tools

For cookbooks and guides, visit the [cookbooks section](https://docs.mistral.ai/resources/cookbooks).

#ai-agents #llm-framework #agentic-workflows