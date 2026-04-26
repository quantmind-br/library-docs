---
title: Campaigns | Mistral Docs
url: https://docs.mistral.ai/studio-api/observability/campaigns
source: sitemap
fetched_at: 2026-04-26T04:13:15.662190959-03:00
rendered_js: false
word_count: 279
summary: Batch-annotate production traffic using Judges for quality assessment, classification, and dataset creation.
tags:
    - batch-annotation
    - production-traffic
    - model-evaluation
    - data-labeling
    - observability
    - campaign-management
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Campaigns

Batch-annotate production traffic using a Judge. Define a filter, pick a Judge, and the Campaign runs on every matching event.

## Prerequisites

Create a [Judge](https://docs.mistral.ai/studio-api/observability/judges) defining your quality criteria first.

> [!note] A Campaign uses a **single Judge**. Create separate Campaigns for multiple checks.

## Step 1: Filter Events

1. Select a **time range**
2. Add filter conditions (see [Explorer filter syntax](https://docs.mistral.ai/studio-api/observability/explorer#filter-language))
3. Set maximum events (100 to 10,000)

## Step 2: Launch Campaign

```python
campaign = client.campaigns.create(
    judge_id=judge.id,
    time_range={"start": "2024-01-01", "end": "2024-01-31"},
    filters=[{"field": "model", "operator": "eq", "value": "mistral-large-latest"}],
    max_events=1000
)
```

Campaign runs in the background — check progress later.

## Step 3: Analyze Results

Once complete, events appear **with annotations** in the **Judge output** column.

| Action | Description |
|--------|-------------|
| Filter by annotation | Surface flagged events (e.g., `rude` or scored below 3) |
| Inspect individual events | Verify Judge assessments |
| Export to Dataset | Further review or analysis |

## Use Cases

| Scenario | Judge Type |
|----------|------------|
| Detect problematic behavior | Rudeness, quality |
| Tag traffic for analysis | Classification (`code`/`search`/`general`) |
| Build quality-labeled Datasets | Regression scores |

## SDK Example

```python
from mistralai.client import MistralClient

client = MistralClient(api_key="your-api-key")

# Create and monitor campaign
campaign = client.campaigns.create(
    judge_id="judge-id",
    time_range={"start": "2024-01-01", "end": "2024-01-31"},
    max_events=500
)

# Poll for completion
import time
while campaign.status not in ["completed", "failed"]:
    time.sleep(60)
    campaign = client.campaigns.get(campaign.id)
```

#batch-annotation #production-traffic #model-evaluation #data-labeling #observability #campaign-management
