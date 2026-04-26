---
title: Libraries | Mistral Docs
url: https://docs.mistral.ai/studio-api/knowledge-rag/libraries
source: sitemap
fetched_at: 2026-04-26T04:13:09.137470369-03:00
rendered_js: false
word_count: 543
summary: Manage persistent knowledge bases and integrate them with AI agents for retrieval-augmented generation (RAG) using the API.
tags:
    - knowledge-base
    - rag
    - ai-agents
    - document-processing
    - access-control
    - api-integration
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Libraries

Persistent knowledge bases for RAG. Upload PDFs, papers, or documents and connect to agents for on-demand search.

## Create Library

```python
library = client.libraries.create(
    name="My Knowledge Base",
    description="Company documentation"
)
```

> [!note] `generated_name` and `generated_description` are auto-updated as you add files.

## Upload Document

```python
with open("document.pdf", "rb") as f:
    doc = client.libraries.documents.upload(
        library_id=library.id,
        file=("doc.pdf", f, "application/pdf")
    )
```

## Check Processing Status

```python
status = client.libraries.documents.get(
    library_id=library.id,
    document_id=doc.id
)
# Status: "Running" (processing) or "Completed" (ready)
```

## List Documents

```python
docs = client.libraries.documents.list(library_id=library.id)
```

## Get Document Content

```python
content = client.libraries.documents.get_content(
    library_id=library.id,
    document_id=doc.id
)
```

## Delete

```python
# Delete single document
client.libraries.documents.delete(library_id=library.id, document_id=doc.id)

# Delete entire library
client.libraries.delete(library_id=library.id)
```

## Access Control

| Parameter | Description |
|-----------|-------------|
| `org_id` | Your organization ID |
| `level` | Access level: `"Viewer"` or `"Editor"` |
| `share_with_uuid` | ID of entity to share with |
| `share_with_type` | Entity type: `"User"`, `"Workspace"`, or `"Org"` |

### Rules

- Library owner can share
- Owner cannot delete their own access
- Viewers cannot edit; Editors can

### Share Library

```python
client.libraries.permissions.create(
    library_id=library.id,
    share_with_uuid="user-id",
    share_with_type="User",
    level="Viewer"
)
```

## Connect to Agent

Create an agent with `document_library` tool:

```python
agent = client.agents.create(
    model="mistral-large-latest",
    tools=[{
        "type": "document_library",
        "document_library": {"library_ids": [library.id]}
    }]
)

# Start conversation
response = client.agents.chat(
    agent_id=agent.id,
    inputs="What does the document say about pricing?"
)
```

### Response Structure

| Entry | Description |
|-------|-------------|
| `tool.execution` | Document Library search ran |
| `message.output` | Agent's grounded answer |

> [!info] Citations (`tool_reference` chunks) are included for verifiable outputs. `usage` object shows `connector_tokens` consumed.

## Related

- [RAG quickstart](https://docs.mistral.ai/studio-api/knowledge-rag/rag_quickstart)
- [Embeddings](https://docs.mistral.ai/studio-api/knowledge-rag/embeddings)
- [Agent tools](https://docs.mistral.ai/studio-api/agents/agent-tools)

#knowledge-base #rag #ai-agents #document-processing #access-control #api-integration
