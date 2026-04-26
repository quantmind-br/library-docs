---
title: Batch Processing | Mistral Docs
url: https://docs.mistral.ai/studio-api/batch-processing
source: sitemap
fetched_at: 2026-04-26T04:12:17.288243173-03:00
rendered_js: false
word_count: 749
summary: Asynchronous batch inference using the API, including file preparation, job creation, status monitoring, and result retrieval for compute cost optimization.
tags:
    - batch-processing
    - asynchronous-inference
    - api-integration
    - jsonl-files
    - compute-optimization
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Batch Processing

Run asynchronous inference on large inputs in parallel at a **50% discount** compared to real-time API calls.

## Batch File Format

Each line in a `.jsonl` file must be a valid JSON object:

```json
{"custom_id": "request-1", "body": {"model": "codestral-latest", "messages": [{"role": "user", "content": "Hello"}]}}
{"custom_id": "request-2", "body": {"model": "codestral-latest", "messages": [{"role": "user", "content": "World"}]}}
```

| Field | Type | Description |
|-------|------|-------------|
| `custom_id` | string | Unique identifier for tracking results |
| `body` | object | Request body matching the endpoint's schema (model optional if specified at job creation) |

> [!warning] Do not add line breaks within a JSON object.

## Supported Endpoints

| Endpoint | Description |
|----------|-------------|
| `/v1/embeddings` | Embeddings generation |
| `/v1/chat/completions` | Chat completion |
| `/v1/fim/completions` | FIM completion |
| `/v1/moderations` | Content moderation |
| `/v1/chat/moderations` | Chat moderation |
| `/v1/ocr` | OCR processing |
| `/v1/classifications` | Classification |
| `/v1/conversations` | Conversations |
| `/v1/audio/transcriptions` | Audio transcription |

## Upload and Create Job

### Via Studio

1. Upload files to [Studio›Files](https://console.mistral.ai/build/files) with `purpose` set to "Batch Processing"
2. Manage batches in [Studio›Batches](https://console.mistral.ai/build/batches)

### Via API

```python
from mistralai.client import MistralClient

client = MistralClient(api_key="your-api-key")

# Upload batch file
with open("batch_requests.jsonl", "rb") as f:
    uploaded_file = client.files.upload(
        file=("batch.jsonl", f, "application/json"),
        purpose="batch"
    )

# Create batch job
batch = client.batch_jobs.create(
    input_files=[uploaded_file.id],
    model="codestral-latest",
    endpoint="/v1/chat/completions"
)
```

## Batch Job Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input_files` | array | List of batch input file IDs |
| `requests` | array | Inline requests (for <10k requests) |
| `model` | string | Single model per batch (e.g., `codestral-latest`) |
| `endpoint` | string | API endpoint to use |
| `metadata` | object | Optional custom metadata |

## Batch Limits

| Limit | Value |
|-------|-------|
| Max file size | 512 MB |
| Max requests per batch | 100,000 |
| Results retention | 24 hours after completion |
| Inline batching threshold | <10,000 requests |

## Monitor and Retrieve Results

```python
# Get job status
job = client.batch_jobs.get(job_id=batch.id)
print(f"Status: {job.status}")

# Download results when complete
if job.status == "SUCCESS":
    result_file = client.batch_jobs.download_results(job_id=batch.id)
```

## Job Statuses

| Status | Description |
|--------|-------------|
| `QUEUED` | Waiting to start |
| `RUNNING` | Currently processing |
| `SUCCESS` | Completed successfully |
| `FAILED` | Failed during processing |
| `TIMEOUT_EXCEEDED` | Exceeded time limit |
| `CANCELLATION_REQUESTED` | Cancellation pending |
| `CANCELLED` | Job was cancelled |

## End-to-End Example

```python
import json
from mistralai.client import MistralClient

client = MistralClient(api_key="your-api-key")

# Generate sample data
requests = [
    {"custom_id": f"req-{i}", "body": {"messages": [{"role": "user", "content": f"Query {i}"}]}}
    for i in range(100)
]

# Write to JSONL
with open("batch.jsonl", "w") as f:
    for req in requests:
        f.write(json.dumps(req) + "\n")

# Upload
with open("batch.jsonl", "rb") as f:
    uploaded = client.files.upload(file=("batch.jsonl", f, "application/json"), purpose="batch")

# Create and wait for job
job = client.batch_jobs.create(input_files=[uploaded.id], model="mistral-large-latest", endpoint="/v1/chat/completions")

# Poll for completion
import time
while job.status not in ["SUCCESS", "FAILED"]:
    time.sleep(10)
    job = client.batch_jobs.get(job_id=job.id)

# Download results
if job.status == "SUCCESS":
    results = client.batch_jobs.download_results(job_id=job.id)
```

#batch-processing #asynchronous-inference #api-integration #jsonl-files #compute-optimization
