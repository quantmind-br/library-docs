---
title: Agents & Conversations | Mistral Docs
url: https://docs.mistral.ai/studio-api/agents/agents-api
source: sitemap
fetched_at: 2026-04-26T04:11:59.116564932-03:00
rendered_js: false
word_count: 760
summary: API structure and management for Agents and Conversations, including configuring custom AI assistants and maintaining persistent interaction histories.
tags:
    - agents
    - conversations
    - api-integration
    - system-prompts
    - tool-calling
    - chat-completion
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Agents & Conversations

## Overview

**Agents** are predefined models with custom system prompts and tools. **Conversations** maintain a history of interactions with an assistant, supporting both Agents and direct model queries.

### Core Objects

| Object | Description |
|--------|-------------|
| **Agent** | Pre-selected values (tools, instructions, completion parameters) that define model behavior |
| **Conversation** | History of interactions (messages, tool executions) with an assistant |
| **Entry** | An action created by user or assistant, enabling flexible representation of interactions |

> [!note] You can create Conversations without creating Agents. These APIs are independent.

[API spec: Agents](https://docs.mistral.ai/api/#tag/beta.agents) | [API spec: Conversations](https://docs.mistral.ai/api/#tag/beta.conversations)

## Agent Creation

Create an Agent with predefined values:

```python
agent = client.agents.create(
    model="mistral-large-latest",
    description="Web search assistant",
    name="search-agent",
    instructions="You are a helpful research assistant.",
    tools=[{"type": "web_search"}],
    completion_args={"temperature": 0.7}
)
```

### Agent Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `model` | string | Yes | Model for chat completion |
| `description` | string | No | Agent description |
| `name` | string | No | Agent name |
| `instructions` | string | No | System prompt / main task description |
| `tools` | array | No | Available tools |
| `completion_args` | object | No | Chat completion sampler arguments |

### Tool Types

| Type | Description |
|------|-------------|
| `function` | User-defined tools (standard function calling) |
| `web_search` / `web_search_premium` | Built-in web search |
| `code_interpreter` | Built-in code execution |
| `image_generation` | Built-in image generation |
| `document_library` | Built-in RAG tool |

## Conversations

### Start a Conversation

```python
# With an Agent
conversation = client.conversations.create(
    agent_id=agent.id,
    inputs="What is the capital of France?"
)

# With a Model directly
conversation = client.conversations.create(
    model="mistral-large-latest",
    inputs="What is the capital of France?"
)
```

### Continue a Conversation

```python
client.conversations.append(
    conversation_id=conversation.id,
    inputs="Tell me more about it."
)
```

> [!note] A new Conversation ID is returned on each append.

### Disable Storage

```python
client.conversations.create(
    model="mistral-large-latest",
    inputs="Sensitive query",
    store=False  # History not stored on cloud
)
```

## Guardrails

If the agent has guardrails configured, they are automatically applied to all conversations. Override by passing `guardrails` directly on `POST /v1/conversations` with a model. See [Custom guardrails](https://docs.mistral.ai/studio-api/safety-moderation#custom-guardrails).

## Handoff Execution Modes

`handoff_execution` parameter controls agent handoff behavior:

| Mode | Description |
|------|-------------|
| `server` | Runs handoff internally on Mistral servers (default) |
| `client` | Returns response directly to user for client-side handoff handling |

For details on handoffs, see the [handoffs guide](https://docs.mistral.ai/studio-api/agents/handoffs).

#agents #conversations #api-integration #system-prompts #tool-calling #chat-completion
