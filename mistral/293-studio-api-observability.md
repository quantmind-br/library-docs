---
title: Observability | Mistral Docs
url: https://docs.mistral.ai/studio-api/observability
source: sitemap
fetched_at: 2026-04-26T04:13:13.114047611-03:00
rendered_js: false
word_count: 257
summary: Observability suite for LLM applications covering production traffic monitoring, response quality assessment, and dataset management.
tags:
    - llm-observability
    - production-monitoring
    - data-analysis
    - model-evaluation
    - enterprise-tools
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Observability

Understand what your LLM applications are doing in production, measure response quality at scale, and iterate with confidence.

> [!info] The Observability suite (Explorer, Judges, Campaigns, Datasets) is available to **Enterprise-tier organizations** only.

## Core Capabilities

| Capability | Description |
|------------|-------------|
| **Visibility** | See what's happening in production traffic event by event |
| **Quality signals** | Score and classify assistant responses automatically with LLM-powered Judges |
| **Iteration loops** | Annotate traffic at scale and build quality-tagged Datasets |

## Components

### Explorer

Search, filter, and inspect every chat completion event. Export filtered slices to Datasets.

[Go to Explorer →](https://docs.mistral.ai/studio-api/observability/explorer)

### Judges

Design and configure automated scoring criteria.

[Judges →](https://docs.mistral.ai/studio-api/observability/judges)

### Campaigns

Run batch annotations on live production traffic.

[Campaigns →](https://docs.mistral.ai/studio-api/observability/campaigns)

### Datasets

Build and manage curated collections of conversation records.

[Datasets →](https://docs.mistral.ai/studio-api/observability/datasets)

## Workflow

```
Explorer → Judge → Campaign → Explorer (filter by annotations) → Dataset
```

![Observability workflow](https://docs.mistral.ai/img/observability_basic_flow.svg)

## Quickstart

[Observability quickstart](https://docs.mistral.ai/studio-api/observability/quickstart) — Set up a Judge and get a quality signal from real traffic.

#llm-observability #production-monitoring #data-analysis #model-evaluation #enterprise-tools
