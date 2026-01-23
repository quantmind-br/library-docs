---
title: Vertex Batch APIs | liteLLM
url: https://docs.litellm.ai/docs/providers/vertex_batch
source: sitemap
fetched_at: 2026-01-21T19:50:42.470379538-03:00
rendered_js: false
word_count: 187
summary: This document provides a step-by-step guide for performing batch predictions on Vertex AI using an OpenAI-compatible workflow, covering environment setup, file management, and job tracking.
tags:
    - vertex-ai
    - batch-prediction
    - litellm
    - google-cloud-storage
    - openai-api
    - python-sdk
category: tutorial
---

Just add the following Vertex env vars to your environment.

```
# GCS Bucket settings, used to store batch prediction files in
export GCS_BUCKET_NAME="my-batch-bucket" # the bucket you want to store batch prediction files in
export GCS_PATH_SERVICE_ACCOUNT="/path/to/service_account.json" # path to your service account json file

# Vertex /batch endpoint settings, used for LLM API requests
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service_account.json" # path to your service account json file
export VERTEXAI_LOCATION="us-central1" # can be any vertex location
export VERTEXAI_PROJECT="my-project" 
```

### Usage[​](#usage "Direct link to Usage")

Follow this complete workflow: create JSONL file → upload file → create batch → retrieve batch status → get file content

#### 1. Create a JSONL file of batch requests[​](#1-create-a-jsonl-file-of-batch-requests "Direct link to 1. Create a JSONL file of batch requests")

LiteLLM expects the file to follow the [**OpenAI batches files format**](https://platform.openai.com/docs/guides/batch).

Each `body` in the file should be an **OpenAI API request**.

Create a file called `batch_requests.jsonl` with your requests:

```
{"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gemini-2.5-flash-lite", "messages": [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": "Hello world!"}],"max_tokens": 10}}
{"custom_id": "request-2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gemini-2.5-flash-lite", "messages": [{"role": "system", "content": "You are an unhelpful assistant."},{"role": "user", "content": "Hello world!"}],"max_tokens": 10}}
```

#### 2. Upload the file[​](#2-upload-the-file "Direct link to 2. Upload the file")

Upload your JSONL file. For `vertex_ai`, the file will be stored in your configured GCS bucket provided by `GCS_BUCKET_NAME`.

- Python
- Curl

upload\_file.py

```
from openai import OpenAI

oai_client = OpenAI(
    api_key="sk-1234",# litellm proxy API key
    base_url="http://localhost:4000"# litellm proxy base url
)

file_obj = oai_client.files.create(
file=open("batch_requests.jsonl","rb"),
    purpose="batch",
    extra_headers={"custom-llm-provider":"vertex_ai"}
)

print(f"File uploaded with ID: {file_obj.id}")
```

**Expected Response:**

```
{
"id":"gs://my-batch-bucket/litellm-vertex-files/publishers/google/models/gemini-2.5-flash-lite/abc123-def4-5678-9012-34567890abcd",
"bytes":416,
"created_at":1758303684,
"filename":"litellm-vertex-files/publishers/google/models/gemini-2.5-flash-lite/abc123-def4-5678-9012-34567890abcd",
"object":"file",
"purpose":"batch",
"status":"uploaded",
"expires_at":null,
"status_details":null
}
```

#### 3. Create a batch[​](#3-create-a-batch "Direct link to 3. Create a batch")

Create a batch job using the uploaded file ID.

- Python
- Curl

create\_batch.py

```
batch_input_file_id = file_obj.id# from step 2
create_batch_response = oai_client.batches.create(
    completion_window="24h",
    endpoint="/v1/chat/completions",
    input_file_id=batch_input_file_id,# e.g. "gs://my-batch-bucket/litellm-vertex-files/publishers/google/models/gemini-2.5-flash-lite/abc123-def4-5678-9012-34567890abcd"
    extra_headers={"custom-llm-provider":"vertex_ai"}
)

print(f"Batch created with ID: {create_batch_response.id}")
```

**Expected Response:**

```
{
"id":"7814463557919047680",
"completion_window":"24hrs",
"created_at":1758328011,
"endpoint":"",
"input_file_id":"gs://my-batch-bucket/litellm-vertex-files/publishers/google/models/gemini-2.5-flash-lite/abc123-def4-5678-9012-34567890abcd",
"object":"batch",
"status":"validating",
"cancelled_at":null,
"cancelling_at":null,
"completed_at":null,
"error_file_id":null,
"errors":null,
"expired_at":null,
"expires_at":null,
"failed_at":null,
"finalizing_at":null,
"in_progress_at":null,
"metadata":null,
"output_file_id":"gs://my-batch-bucket/litellm-vertex-files/publishers/google/models/gemini-2.5-flash-lite",
"request_counts":null,
"usage":null
}
```

#### 4. Retrieve batch status[​](#4-retrieve-batch-status "Direct link to 4. Retrieve batch status")

Check the status of your batch job. The batch will progress through states: `validating` → `in_progress` → `completed`.

- Python
- Curl

retrieve\_batch.py

```
retrieved_batch = oai_client.batches.retrieve(
    batch_id=create_batch_response.id,# Created batch id, e.g. 7814463557919047680
    extra_headers={"custom-llm-provider":"vertex_ai"}
)

print(f"Batch status: {retrieved_batch.status}")
if retrieved_batch.status =="completed":
print(f"Output file: {retrieved_batch.output_file_id}")
```

**Expected Response (when completed):**

```
{
"id":"7814463557919047680",
"completion_window":"24hrs",
"created_at":1758328011,
"endpoint":"",
"input_file_id":"gs://my-batch-bucket/litellm-vertex-files/publishers/google/models/gemini-2.5-flash-lite/abc123-def4-5678-9012-34567890abcd",
"object":"batch",
"status":"completed",
"cancelled_at":null,
"cancelling_at":null,
"completed_at":null,
"error_file_id":null,
"errors":null,
"expired_at":null,
"expires_at":null,
"failed_at":null,
"finalizing_at":null,
"in_progress_at":null,
"metadata":null,
"output_file_id":"gs://my-batch-bucket/litellm-vertex-files/publishers/google/models/gemini-2.5-flash-lite/prediction-model-2025-09-19T21:26:51.569037Z/predictions.jsonl",
"request_counts":null,
"usage":null
}
```

#### 5. Get file content[​](#5-get-file-content "Direct link to 5. Get file content")

Once the batch is completed, retrieve the results using the `output_file_id` from the batch response.

**Important:** The `output_file_id` must be URL encoded when used in the request path.

- Python
- Curl

get\_file\_content.py

```
import urllib.parse
import json

output_file_id = retrieved_batch.output_file_id
# URL encode the file ID
encoded_file_id = urllib.parse.quote_plus(output_file_id)

# Get file content
file_content = oai_client.files.content(
    file_id=encoded_file_id,
    extra_headers={"custom-llm-provider":"vertex_ai"}
)

# Process the results
for line in file_content.text.strip().split('\n'):
    result = json.loads(line)
print(f"Request: {result['request']}")
print(f"Response: {result['response']}")
print("---")
```

**Expected Response:**

The response contains JSONL format with one result per line:

```
{"status":"","processed_time":"2025-09-19T21:29:47.352+00:00","request":{"contents":[{"parts":[{"text":"Hello world!"}],"role":"user"}],"generationConfig":{"max_output_tokens":10},"system_instruction":{"parts":[{"text":"You are a helpful assistant."}]}},"response":{"candidates":[{"avgLogprobs":-0.48079710006713866,"content":{"parts":[{"text":"Hello there! It's nice to meet you"}],"role":"model"},"finishReason":"MAX_TOKENS"}],"createTime":"2025-09-19T21:29:47.484619Z","modelVersion":"gemini-2.5-flash-lite","responseId":"S8vNaIvKHdvshMIP_aOtuAg","usageMetadata":{"candidatesTokenCount":10,"candidatesTokensDetails":[{"modality":"TEXT","tokenCount":10}],"promptTokenCount":9,"promptTokensDetails":[{"modality":"TEXT","tokenCount":9}],"totalTokenCount":19,"trafficType":"ON_DEMAND"}}}
{"status":"","processed_time":"2025-09-19T21:29:47.358+00:00","request":{"contents":[{"parts":[{"text":"Hello world!"}],"role":"user"}],"generationConfig":{"max_output_tokens":10},"system_instruction":{"parts":[{"text":"You are an unhelpful assistant."}]}},"response":{"candidates":[{"avgLogprobs":-0.6168075137668185,"content":{"parts":[{"text":"I am unable to assist with this request."}],"role":"model"},"finishReason":"STOP"}],"createTime":"2025-09-19T21:29:47.470889Z","modelVersion":"gemini-2.5-flash-lite","responseId":"S8vNaOneHISShMIP28nA8QQ","usageMetadata":{"candidatesTokenCount":9,"candidatesTokensDetails":[{"modality":"TEXT","tokenCount":9}],"promptTokenCount":9,"promptTokensDetails":[{"modality":"TEXT","tokenCount":9}],"totalTokenCount":18,"trafficType":"ON_DEMAND"}}}
```