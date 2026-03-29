---
title: /batchPredictionJobs | liteLLM
url: https://docs.litellm.ai/docs/vertex_batch_passthrough
source: sitemap
fetched_at: 2026-01-21T19:55:56.972885514-03:00
rendered_js: false
word_count: 333
summary: This document explains how to configure and use LiteLLM to manage Vertex AI batch prediction jobs, including job creation, status monitoring, and automated cost tracking.
tags:
    - vertex-ai
    - batch-prediction
    - litellm
    - cost-tracking
    - gemini
    - api-passthrough
category: guide
---

LiteLLM supports Vertex AI batch prediction jobs through passthrough endpoints, allowing you to create and manage batch jobs directly through the proxy server.

## Features[​](#features "Direct link to Features")

- **Batch Job Creation**: Create batch prediction jobs using Vertex AI models
- **Cost Tracking**: Automatic cost calculation and usage tracking for batch operations
- **Status Monitoring**: Track job status and retrieve results
- **Model Support**: Works with all supported Vertex AI models (Gemini, Text Embedding)

## Cost Tracking Support[​](#cost-tracking-support "Direct link to Cost Tracking Support")

FeatureSupportedNotesCost Tracking✅Automatic cost calculation for batch operationsUsage Monitoring✅Track token usage and costs across batch jobsLogging✅Supported

## Quick Start[​](#quick-start "Direct link to Quick Start")

1. **Configure your model** in the proxy configuration:

```
model_list:
-model_name: gemini-1.5-flash
litellm_params:
model: vertex_ai/gemini-1.5-flash
vertex_project: your-project-id
vertex_location: us-central1
vertex_credentials: path/to/service-account.json
```

2. **Create a batch job**:

```
curl -X POST "http://localhost:4000/v1/projects/your-project/locations/us-central1/batchPredictionJobs" \
  -H "Authorization: Bearer your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "displayName": "my-batch-job",
    "model": "projects/your-project/locations/us-central1/publishers/google/models/gemini-1.5-flash",
    "inputConfig": {
      "gcsSource": {
        "uris": ["gs://my-bucket/input.jsonl"]
      },
      "instancesFormat": "jsonl"
    },
    "outputConfig": {
      "gcsDestination": {
        "outputUriPrefix": "gs://my-bucket/output/"
      },
      "predictionsFormat": "jsonl"
    }
  }'
```

3. **Monitor job status**:

```
curl -X GET "http://localhost:4000/v1/projects/your-project/locations/us-central1/batchPredictionJobs/job-id" \
  -H "Authorization: Bearer your-api-key"
```

## Model Configuration[​](#model-configuration "Direct link to Model Configuration")

When configuring models for batch operations, use these naming conventions:

- **`model_name`** : Base model name (e.g., `gemini-1.5-flash`)
- **`model`** : Full LiteLLM identifier (e.g., `vertex_ai/gemini-1.5-flash`)

## Supported Models[​](#supported-models "Direct link to Supported Models")

- `gemini-1.5-flash` / `vertex_ai/gemini-1.5-flash`
- `gemini-1.5-pro` / `vertex_ai/gemini-1.5-pro`
- `gemini-2.0-flash` / `vertex_ai/gemini-2.0-flash`
- `gemini-2.0-pro` / `vertex_ai/gemini-2.0-pro`

## Advanced Usage[​](#advanced-usage "Direct link to Advanced Usage")

### Batch Job with Custom Parameters[​](#batch-job-with-custom-parameters "Direct link to Batch Job with Custom Parameters")

```
curl -X POST "http://localhost:4000/v1/projects/your-project/locations/us-central1/batchPredictionJobs" \
  -H "Authorization: Bearer your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "displayName": "advanced-batch-job",
    "model": "projects/your-project/locations/us-central1/publishers/google/models/gemini-1.5-pro",
    "inputConfig": {
      "gcsSource": {
        "uris": ["gs://my-bucket/advanced-input.jsonl"]
      },
      "instancesFormat": "jsonl"
    },
    "outputConfig": {
      "gcsDestination": {
        "outputUriPrefix": "gs://my-bucket/advanced-output/"
      },
      "predictionsFormat": "jsonl"
    },
    "labels": {
      "environment": "production",
      "team": "ml-engineering"
    }
  }'
```

### List All Batch Jobs[​](#list-all-batch-jobs "Direct link to List All Batch Jobs")

```
curl -X GET "http://localhost:4000/v1/projects/your-project/locations/us-central1/batchPredictionJobs" \
  -H "Authorization: Bearer your-api-key"
```

### Cancel a Batch Job[​](#cancel-a-batch-job "Direct link to Cancel a Batch Job")

```
curl -X POST "http://localhost:4000/v1/projects/your-project/locations/us-central1/batchPredictionJobs/job-id:cancel" \
  -H "Authorization: Bearer your-api-key"
```

## Cost Tracking Details[​](#cost-tracking-details "Direct link to Cost Tracking Details")

LiteLLM provides comprehensive cost tracking for Vertex AI batch operations:

- **Token Usage**: Tracks input and output tokens for each batch request
- **Cost Calculation**: Automatically calculates costs based on current Vertex AI pricing
- **Usage Aggregation**: Aggregates costs across all requests in a batch job
- **Real-time Monitoring**: Monitor costs as batch jobs progress

The cost tracking works seamlessly with the `generateContent` API and provides detailed insights into your batch processing expenses.

## Error Handling[​](#error-handling "Direct link to Error Handling")

Common error scenarios and their solutions:

ErrorDescriptionSolution`INVALID_ARGUMENT`Invalid model or configurationVerify model name and project settings`PERMISSION_DENIED`Insufficient permissionsCheck Vertex AI IAM roles`RESOURCE_EXHAUSTED`Quota exceededCheck Vertex AI quotas and limits`NOT_FOUND`Job or resource not foundVerify job ID and project configuration

## Best Practices[​](#best-practices "Direct link to Best Practices")

1. **Use appropriate batch sizes**: Balance between processing efficiency and resource usage
2. **Monitor job status**: Regularly check job status to handle failures promptly
3. **Set up alerts**: Configure monitoring for job completion and failures
4. **Optimize costs**: Use cost tracking to identify optimization opportunities
5. **Test with small batches**: Validate your setup with small test batches first

<!--THE END-->

- [Vertex AI Provider Documentation](https://docs.litellm.ai/docs/vertex.md)
- [General Batches API Documentation](https://docs.litellm.ai/batches.md)
- [Cost Tracking and Monitoring](https://docs.litellm.ai/observability/telemetry.md)