---
title: Explorer | Mistral Docs
url: https://docs.mistral.ai/studio-api/observability/explorer
source: sitemap
fetched_at: 2026-04-26T04:13:19.568675001-03:00
rendered_js: false
word_count: 331
summary: Search, filter, inspect, and export production chat completion events for observability and dataset management.
tags:
    - observability
    - production-monitoring
    - event-filtering
    - data-export
    - chat-completions
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Explorer

Window into production traffic. Search, filter, and inspect every chat completion event.

> [!info] Explorer is restricted to **Workspace administrators**.

## Features

- **Search and filter** by model, tool usage, message content, latency, etc.
- **Inspect** conversation records (messages, tool calls, metadata)
- **Export** filtered events to [Datasets](https://docs.mistral.ai/studio-api/observability/datasets)
- **Automate** by creating [Judges](https://docs.mistral.ai/studio-api/observability/judges) and [Campaigns](https://docs.mistral.ai/studio-api/observability/campaigns)

## Filter Language

Write conditions on event fields using `AND`, `OR`, and parentheses.

### Operators

| Operator | Description |
|----------|-------------|
| `eq` | Equals |
| `ne` | Not equals |
| `gt`, `gte` | Greater than, greater than or equal |
| `lt`, `lte` | Less than, less than or equal |
| `contains` | String contains |
| `in` | Value in list |

### Examples

**Filter by model and tool:**
```
model = "mistral-large-latest" AND tools CONTAINS "web_search"
```

**Filter by model family:**
```
model CONTAINS "mistral-large"
```

**Filter by response time:**
```
latency_ms > 5000
```

**Combine conditions:**
```
(model = "mistral-large-latest" AND latency_ms > 1000) OR tools CONTAINS "code_interpreter"
```

## Query Design Tips

1. Start broad with a time range, then narrow
2. Add one business-relevant condition (specific tool, feature, model)
3. Add one technical condition (latency, content, tools)
4. Scan a few results before exporting

## Inspect Events

Click any event to see:

- **Message feed** — Full conversation (user inputs, assistant responses, system prompts)
- **Properties** — Model name, token counts, computation duration, tools invoked

## Export to Dataset

1. Select events using checkboxes
2. Click **Add to dataset**
3. Choose existing Dataset or create new

> [!tip] Dataset exports are snapshots. Use descriptive names like `support_web_search_2026_02`.

## SDK

```python
# Search events
events = client.explorer.search(
    filters={
        "AND": [
            {"field": "model", "operator": "eq", "value": "mistral-large-latest"},
            {"field": "latency_ms", "operator": "gt", "value": 1000}
        ]
    },
    limit=100
)

# Export to dataset
client.datasets.import_records(
    dataset_id="dataset-id",
    records=[{"messages": e.messages, "properties": e.metadata} for e in events]
)
```

#observability #production-monitoring #event-filtering #data-export #chat-completions
