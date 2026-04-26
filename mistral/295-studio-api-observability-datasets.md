---
title: Datasets | Mistral Docs
url: https://docs.mistral.ai/studio-api/observability/datasets
source: sitemap
fetched_at: 2026-04-26T04:13:16.806398273-03:00
rendered_js: false
word_count: 523
summary: Curate and manage datasets for model evaluation including structuring records, importing data, and maintaining quality testing baselines.
tags:
    - datasets
    - data-curation
    - model-evaluation
    - regression-testing
    - machine-learning
    - data-management
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Datasets

Curated collections of conversation records for evaluating model quality, building regression tests, or preparing fine-tuning data.

> [!note] Unlike raw Explorer traffic, Dataset records are **editable**.

## Record Structure

Each record has three parts. **Properties** add structured context:

| Property | Description |
|----------|-------------|
| `expected_output` | Ideal response for Judge comparison |
| `category` | Request type (e.g., `billing`, `technical`) |
| `grading_guidance` | Instructions for Judge evaluation |
| `difficulty` | Complexity marker for segmentation |

Judges reference properties via `{{ properties.your_field_name }}`.

## Create Dataset

### Manually

Add records by hand in Studio. Define conversation turns and attach properties.

**Use for:**
- Regression tests targeting known edge cases
- Golden examples with crafted expected outputs
- Specific scenarios not in production traffic

### From Playground

Import conversations from [Playground](https://console.mistral.ai/build/playground).

### From Campaign

Import all or subset of a Campaign's records, including Judge annotations as properties.

### From Explorer

Select events and click **Export to Dataset**. See [Explorer guide](https://docs.mistriainference.ai/studio-api/observability/explorer#export-to-datasets).

### From File

Upload JSONL:

```json
{"messages": [{"role": "user", "content": "Query"}], "properties": {"category": "support"}}
{"messages": [{"role": "user", "content": "Query 2"}], "properties": {"category": "billing"}}
```

## Curate Records

### Edit

- Fix typos, clarify ambiguous inputs
- Reshape conversations to better represent test cases
- Add `expected_output`, `grading_guidance`, or metadata

### Remove Low-Value Records

- **Duplicates** — Over-represent one scenario
- **Out of scope** — Don't match Dataset purpose
- **Ambiguous** — Even humans couldn't reliably score

## Test Before Scale

Run a Judge on a single record before launching a full Campaign:

```python
# Validate judge works on sample
result = client.judges.validate(
    judge_id=judge.id,
    record_id=sample_record.id
)
```

## Best Practices

| Practice | Description |
|----------|-------------|
| **Name explicitly** | Include scope and date: `support_billing_baseline_2025_06` |
| **Track sources** | Note where records came from and curation applied |
| **Version baselines** | Freeze baseline between uses |
| **Keep separate** | Don't mix unrelated tasks |
| **Check balance** | 90% easy cases won't reveal real problems |

## SDK

```python
# Create dataset
dataset = client.datasets.create(name="my_dataset", description="Support quality baseline")

# Import records
client.datasets.import_records(
    dataset_id=dataset.id,
    records=[{"messages": [...], "properties": {...}}]
)

# Export
client.datasets.export(dataset_id=dataset.id)
```

#datasets #data-curation #model-evaluation #regression-testing #machine-learning #data-management
