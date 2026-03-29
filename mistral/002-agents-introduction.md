---
title: Agents Introduction | Mistral Docs
url: https://docs.mistral.ai/agents/introduction
source: crawler
fetched_at: 2026-01-29T07:33:11.728012603-03:00
rendered_js: false
word_count: 237
summary: This document introduces AI agents as autonomous systems powered by large language models and provides an overview of the features and tools available in the Agents and Conversations API.
tags:
    - ai-agents
    - mistral-api
    - autonomous-agents
    - multi-agent-systems
    - tool-calling
    - llm-orchestration
category: concept
---

## What are AI agents?

AI agents are autonomous systems powered by large language models (LLMs) that, given high-level instructions, can plan, use tools, carry out processing steps, and take actions to achieve specific goals. These agents leverage advanced natural language processing capabilities to understand and execute complex tasks efficiently and can even collaborate with each other to achieve more sophisticated outcomes.

![agents_graph](https://docs.mistral.ai/img/agent_overview.png)![agents_graph](https://docs.mistral.ai/img/agent_overview_dark.png)

Our Agents and Conversations API allows developers to build such agents, leveraging multiple features such as:

- Multiple mutlimodal models available, **text and vision models**.
- **Persistent state** across conversations.
- Ability to have conversations with **base models**, **a single agent**, and **multiple agents**.
- Built-in connector tools for **code execution**, **web search**, **image generation** and **document library** out of the box.
- **Handoff capability** to use different agents as part of a workflow, allowing agents to call other agents.
- Features supported via our chat completions endpoint are also supported, such as:
  
  - **Structured Outputs**
  - **Document Understanding**
  - **Tool Usage**
  - **Citations**

<!--THE END-->

- [Agents & Conversations](https://docs.mistral.ai/agents/agents): Basic explanations and code snippets around our Agents and Conversations API.
- [Tools](https://docs.mistral.ai/agents/tools): Make tools accessible to any Agent.
  
  - [Built-In](https://docs.mistral.ai/agents/tools/built-in): built-in tools that are available to all agents.
    
    - [Websearch](https://docs.mistral.ai/agents/tools/built-in/websearch): In-depth explanation of our web search built-in connector tool.
    - [Code Interpreter](https://docs.mistral.ai/agents/tools/built-in/code_interpreter): In-depth explanation of our code interpreter for code execution built-in connector tool.
    - [Image Generation](https://docs.mistral.ai/agents/tools/built-in/image_generation): In-depth explanation of our image generation built-in connector tool.
    - [Document Library (Beta)](https://docs.mistral.ai/agents/tools/built-in/document_library): A RAG built-in connector enabling Agents to access a library of documents.
  - [Function Calling](https://docs.mistral.ai/agents/tools/function_calling): Leverage function calling to create custom tools.
  - [MCP](https://docs.mistral.ai/agents/tools/mcp): Leverage MCP Servers to create custom tools or use third-party ones.
- [Handoffs](https://docs.mistral.ai/agents/handoffs): Relay tasks and use other agents as tools in agentic workflows.

For more information and guides on how to use our Agents, we have the following cookbooks: