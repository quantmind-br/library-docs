---
title: Citations & References | Mistral Docs
url: https://docs.mistral.ai/studio-api/conversations/citations
source: sitemap
fetched_at: 2026-04-26T04:12:26.291641948-03:00
rendered_js: false
word_count: 362
summary: Implement citations and references in model responses using tool calls to support Retrieval-Augmented Generation (RAG) workflows.
tags:
    - rag
    - citations
    - references
    - tool-calls
    - grounding
    - api-integration
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Citations & References

Models can ground responses and provide references using tool calls, enabling source attribution for RAG and agentic applications.

## Overview

Models are trained to ground on documents and extract references and citations from tool call responses.

> [!note] For chat completions basics, see [Chat Completions](https://docs.mistral.ai/studio-api/conversations/chat-completion).

## Setup

### 1. Define Reference Tool

```python
def get_information(query: str):
    """Retrieve information from external source."""
    # Return references from Wikipedia or other source
    return {
        "references": [
            {"title": "Article Title", "url": "https://example.com", "content": "..."}
        ]
    }

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_information",
            "description": "Get information about a query",
            "parameters": {"type": "object", "properties": {"query": {"type": "string"}}}
        }
    }
]
```

### 2. Initialize Client and Chat History

```python
from mistralai.client import MistralClient

client = MistralClient(api_key="your-api-key")

messages = [
    {"role": "user", "content": "What is the capital of France?"}
]
```

### 3. Initial Chat Request

```python
response = client.chat(
    model="mistral-large-latest",
    messages=messages,
    tools=tools
)

# Model wants to call get_information tool
tool_calls = response.choices[0].message.tool_calls
```

### 4. Execute Tool and Append Result

```python
if tool_calls:
    tool_result = get_information(query="capital of France")
    messages.append({"role": "tool", "tool_call_id": tool_calls[0].id, "content": json.dumps(tool_result)})
```

### 5. Final Response with Citations

```python
final_response = client.chat(
    model="mistral-large-latest",
    messages=messages
)

# Extract references
for chunk in final_response.choices[0].message.content:
    if chunk.type == "tool_reference":
        print(f"Source: {chunk.title} - {chunk.url}")
```

## Response Structure

| Chunk Type | Description |
|------------|-------------|
| `text` | Actual response text |
| `tool_reference` | Citation pointing to source |

> [!tip] Full cookbook with Wikipedia RAG example available [here](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/rag/mistral-reference-rag.ipynb).

#rag #citations #references #tool-calls #grounding #api-integration
