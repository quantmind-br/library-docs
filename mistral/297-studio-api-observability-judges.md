---
title: Judges | Mistral Docs
url: https://docs.mistral.ai/studio-api/observability/judges
source: sitemap
fetched_at: 2026-04-26T04:13:21.564315132-03:00
rendered_js: false
word_count: 489
summary: LLM-based evaluators that score or classify model responses at scale, used to power Campaigns for batch annotation of production traffic.
tags:
    - llm-evaluation
    - model-scoring
    - classification
    - regression
    - prompt-engineering
    - observability
    - automated-testing
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Judges

LLM-based evaluators that **score or classify model responses** at scale.

Define quality criteria once, apply consistently across thousands of events.

> [!note] Judges are used by [Campaigns](https://docs.mistral.ai/studio-api/observability/campaigns) to batch-annotate production traffic.

## Judge Components

| Component | Description |
|-----------|-------------|
| **Type** | Classification (discrete label) or Regression (score) |
| **Model** | Model used for evaluation |
| **Instructions** | Quality criteria and evaluation guidelines |

## Types

### Classification Judges

Assign a **discrete label**.

| Use Case | Examples |
|----------|----------|
| Binary | `helpful` / `not helpful`, `safe` / `unsafe` |
| Multi-class | `excellent` / `acceptable` / `poor` |
| Routing | `code` / `search` / `guide` |

### Regression Judges

Assign a **numeric score**.

## Instructions Guidelines

| Guideline | Description |
|-----------|-------------|
| **Be specific** | Avoid vague prompts; spell out what "good" means |
| **Never assume** | The Judge doesn't know your context |
| **Ensure testability** | If you can't apply criteria consistently, neither can the Judge |
| **Use boundary examples** | "Score 3 = partially helpful, omits key detail" |

## Properties in Instructions

Reference Dataset record properties using Jinja2:

```
Compare against expected output: {{ properties.expected_output }}
Use grading guidance: {{ properties.grading_guidance }}
```

## Validation Before Scale

Test on 10–20 records before running Campaign:

1. Select Source (**Traffic** or **Dataset**)
2. Optionally filter events
3. Use **Try it** button to run Judge

### What to Check

| Check | Description |
|-------|-------------|
| **Agreement** | Do Judge scores match your expectations? |
| **Stability** | Does Judge score similar inputs consistently? |
| **Failure patterns** | Undefined answers or contradictions? |

Revise instructions before scaling.

## Model Selection

| Consideration | Description |
|---------------|-------------|
| Stronger models | More nuanced judgments, higher cost |
| Faster models | Well-suited for straightforward, well-defined criteria |

## SDK Example

```python
from mistralai.client import MistralClient

client = MistralClient(api_key="your-api-key")

# Create Judge
judge = client.judges.create(
    name="Quality Classifier",
    type="classification",
    model="mistral-large-latest",
    instructions="""
    Evaluate the assistant's final response.
    Is it accurate, relevant, and complete?
    Classify as:
    - excellent: Fully addresses question with accurate, clear info
    - acceptable: Addresses question but with minor issues
    - poor: Fails to address question or contains significant errors
    """
)

# Validate
result = client.judges.validate(
    judge_id=judge.id,
    record_id=sample_record.id
)
```

#llm-evaluation #model-scoring #classification #regression #prompt-engineering #observability #automated-testing
