---
title: Agent Models | Firecrawl
url: https://docs.firecrawl.dev/features/models
source: sitemap
fetched_at: 2026-03-23T07:24:45.661833-03:00
rendered_js: false
word_count: 259
summary: This document provides a comparative guide to Firecrawl's Spark 1 Mini and Spark 1 Pro models, helping users select the appropriate model based on task complexity, accuracy needs, and cost requirements.
tags:
    - firecrawl
    - data-extraction
    - model-selection
    - api-configuration
    - cost-optimization
    - web-scraping
category: guide
---

Firecrawl Agent offers two models optimized for different use cases. Choose the right model based on your extraction complexity and cost requirements.

## Available Models

ModelCostAccuracyBest For`spark-1-mini`**60% cheaper**StandardMost tasks (default)`spark-1-pro`StandardHigherComplex research, critical extraction

## Spark 1 Mini (Default)

`spark-1-mini` is our efficient model, ideal for straightforward data extraction tasks. **Use Mini when:**

- Extracting simple data points (contact info, pricing, etc.)
- Working with well-structured websites
- Cost efficiency is a priority
- Running high-volume extraction jobs

**Example use cases:**

- Extracting product prices from e-commerce sites
- Gathering contact information from company pages
- Pulling basic metadata from articles
- Simple data point lookups

## Spark 1 Pro

`spark-1-pro` is our flagship model, designed for maximum accuracy on complex extraction tasks. **Use Pro when:**

- Performing complex competitive analysis
- Extracting data that requires deep reasoning
- Accuracy is critical for your use case
- Dealing with ambiguous or hard-to-find data

**Example use cases:**

- Multi-domain competitive analysis
- Complex research tasks requiring reasoning
- Extracting nuanced information from multiple sources
- Critical business intelligence gathering

## Specifying a Model

Pass the `model` parameter to select which model to use:

## Model Comparison

FeatureSpark 1 MiniSpark 1 Pro**Cost**60% cheaperStandard**Accuracy**StandardHigher**Speed**FastFast**Best for**Most tasksComplex tasks**Reasoning**StandardAdvanced**Multi-domain**GoodExcellent

## Pricing by Model

Both models use dynamic, credit-based pricing that scales with task complexity:

- **Spark 1 Mini**: Uses approximately 60% fewer credits than Pro for equivalent tasks
- **Spark 1 Pro**: Standard credit consumption for maximum accuracy

## Choosing the Right Model

```
                    ┌─────────────────────────────────┐
                    │   What type of task?            │
                    └─────────────────────────────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    ▼                             ▼
          ┌─────────────────┐           ┌─────────────────┐
          │  Simple/Direct  │           │ Complex/Research│
          │  extraction     │           │ multi-domain    │
          └─────────────────┘           └─────────────────┘
                    │                             │
                    ▼                             ▼
          ┌─────────────────┐           ┌─────────────────┐
          │  spark-1-mini   │           │  spark-1-pro    │
          │  (60% cheaper)  │           │  (higher acc.)  │
          └─────────────────┘           └─────────────────┘
```

## API Reference

See the [Agent API Reference](https://docs.firecrawl.dev/api-reference/endpoint/agent) for complete parameter documentation. Have questions about which model to use? Email [help@firecrawl.com](mailto:help@firecrawl.com).

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.