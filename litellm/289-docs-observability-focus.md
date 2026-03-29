---
title: Focus Export (Experimental) | liteLLM
url: https://docs.litellm.ai/docs/observability/focus
source: sitemap
fetched_at: 2026-01-21T19:46:02.77683232-03:00
rendered_js: false
word_count: 116
summary: This document describes the experimental feature in LiteLLM for exporting usage data in the FinOps FOCUS v1.2 format to cloud storage like Amazon S3 for cost analysis.
tags:
    - litellm
    - finops
    - focus-format
    - amazon-s3
    - cost-analysis
    - usage-tracking
category: guide
---

Experimental feature

Focus Format export is under active development and currently considered experimental. Interfaces, schema mappings, and configuration options may change as we iterate based on user feedback. Please treat this integration as a preview and report any issues or suggestions to help us stabilize and improve the workflow.

LiteLLM can emit usage data in the [FinOps FOCUS format](https://focus.finops.org/focus-specification/v1-2/) and push artifacts (for example Parquet files) to destinations such as Amazon S3. This enables downstream cost-analysis tooling to ingest a standardised dataset directly from LiteLLM.

LiteLLM currently conforms to the FinOps FOCUS v1.2 specification when emitting this dataset.

```
export FOCUS_PROVIDER="s3"
export FOCUS_PREFIX="focus_exports"

# S3 example
export FOCUS_S3_BUCKET_NAME="my-litellm-focus-bucket"
export FOCUS_S3_REGION_NAME="us-east-1"
export FOCUS_S3_ACCESS_KEY="AKIA..."
export FOCUS_S3_SECRET_KEY="..."
```

During boot LiteLLM registers the Focus logger and a background job that runs according to the configured frequency.