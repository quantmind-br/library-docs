---
title: Durable Agents | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/building-workflows/durable_agents
source: sitemap
fetched_at: 2026-04-26T04:13:43.94447136-03:00
rendered_js: false
word_count: 422
summary: This document describes how to implement and manage durable LLM agents within Mistral workflows, covering tool integration, multi-agent handoffs, and production deployment practices.
tags:
    - llm-agents
    - mistral-workflows
    - mcp-support
    - agent-orchestration
    - workflow-automation
    - tool-integration
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Durable Agents allow you to run LLM agents within your Mistral workflows. To use Durable Agents, install the Mistral plugin.

## What is a Durable Agent?

A Durable Agent is an LLM agent that executes within a workflow, benefiting from:

- **Durability**: Agent state is preserved across failures and restarts
- **Tool Integration**: Use activities as agent tools
- **Multi-Agent Handoffs**: Agents can delegate tasks to specialized agents
- **MCP Support**: Connect to external tools via Model Context Protocol (stdio / SSE)

## Core Components

The `Agent` class defines an LLM agent with its model, instructions, tools and handoffs:

```python
```

The `Runner` executes an agent with user inputs and manages the conversation loop. It calls the model, processes tool calls, and repeats until the agent produces a final response or reaches `max_turns`. If `max_turns` is reached, the runner returns whatever outputs have been collected so far.

The returned `outputs` is a list of output items produced by the agent during the run (text responses, tool results, handoff results).

Sessions manage agent state and API communication. Two session types are available:

```python
```

## Simple Agent Workflow

Here's a simple agent workflow that uses an activity as a tool:

```python
```

## Multi-Agent Handoffs

Agents can delegate tasks to specialized agents using handoffs. The system automatically manages the handoff conversation:

```python
```

When the finance agent receives a query about ECB interest rates, it can automatically hand off to the specialized `interest_rate_agent`.

## MCP Integration

Connect to external tool servers using the Model Context Protocol. Two transport types are supported:

For local command-line MCP servers:

```python
For remote MCP servers over Server-Sent Events:
```

```python
```

## Built-in Tools

Use Mistral's built-in tools alongside activities:

```python
```

Available built-in tools:

```python
```

These tools are executed server-side by the Mistral platform — they do not run in your worker process. Pass them in the `tools` list alongside any activity-based tools.

## Session Types

### RemoteSession

Uses the Mistral Agents SDK for production workloads:

Features:
- Full Agents SDK integration
- Automatic agent creation and updates
- Managed conversation state
- Production-ready

### LocalSession

Runs agents locally using the completion endpoint:

Use cases:
- On-premises deployments that doesn't have access to Agents (Bora)
- Development and testing
- Full context control

> [!warning] `LocalSession` is experimental and may be removed in future versions. Use `RemoteSession` for production workloads.

## Full Example

A full example combining activities, handoffs and workflow orchestration:

```python
```

## Best Practices

1. **Use RemoteSession for production** - It provides better reliability and Agents SDK integration
2. **Keep activities granular** - Small, focused activities work better as agent tools
3. **Provide clear instructions** - Agent performance depends on clear instructions
4. **Use handoffs for specialization** - Create specialized agents for specific domains and improve context management by delegating tasks
5. **Handle tool errors gracefully** - Activities used as tools should return meaningful error messages