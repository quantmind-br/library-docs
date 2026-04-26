---
title: Websearch | Mistral Docs
url: https://docs.mistral.ai/studio-api/agents/agent-tools/websearch
source: sitemap
fetched_at: 2026-04-26T04:11:57.257100001-03:00
rendered_js: false
word_count: 529
summary: Integrate web search capabilities into AI agents to retrieve real-time information and interpret tool execution and message output metadata.
tags:
    - web-search
    - ai-agents
    - tool-integration
    - metadata
    - rag
    - retrieval-augmented-generation
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Websearch

Browse the web to retrieve real-time information. Fixes limitations of models that are not up to date due to training data, and enables accessing recent information or specific websites.

![Websearch architecture](https://docs.mistral.ai/img/websearch_connector.png)![Websearch architecture dark](https://docs.mistral.ai/img/websearch_connector_dark.png)

## Tool Versions

| Tool | Description |
|------|-------------|
| `web_search` | Simple web search via search engine |
| `web_search_premium` | Search engine plus integrated news provider verification |

## Usage

Create an agent with websearch as one of the tools:

```python
from mistralai.client import MistralClient

client = MistralClient(api_key="your-api-key")

agent = client.agents.create(
    model="mistral-large-latest",
    tools=[{"type": "web_search"}]
)

chat_response = client.agents.chat(
    agent_id=agent.id,
    inputs="What are the latest developments in AI?"
)
```

> [!note] You can add more tools to the agent. The model decides whether to search the web or not.

## Response Structure

### `tool.execution`

Web search tool execution metadata:

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Tool name: `web_search` |
| `object` | string | Object type: `entry` |
| `type` | string | Entry type: `tool.execution` |
| `created_at` | datetime | Execution start timestamp |
| `completed_at` | datetime | Execution completion timestamp |
| `id` | string | Unique execution identifier |

### `message.output`

Generated answer with citations:

| Field | Type | Description |
|-------|------|-------------|
| `content` | list | List of chunks (text + tool_reference) |
| `content[].type` | string | Chunk type: `text` or `tool_reference` |
| `content[].text` | string | Actual text content |
| `content[].tool` | string | Reference tool name: `web_search` |
| `content[].title` | string | Reference source title |
| `content[].url` | string | Reference source URL |
| `content[].source` | string | Reference source name |

> [!info] Reference chunks provide transparent feedback on where the model got its response. This is useful for RAG-related tool usages and citations.

## Related

- [Document Library tool](https://docs.mistral.ai/studio-api/knowledge-rag/libraries#connecting-libraries-to-agents) — also uses references
- [Citations guide](https://docs.mistral.ai/studio-api/conversations/citations)

#web-search #ai-agents #tool-integration #metadata #rag #retrieval-augmented-generation
