---
title: Download a model
url: https://lmstudio.ai/docs/developer/rest/download
source: sitemap
fetched_at: 2026-04-07T21:30:25.576539552-03:00
rendered_js: false
word_count: 138
summary: This document describes the API endpoint for initiating and checking the status of a model download, detailing required request body parameters and possible response fields.
tags:
    - api-endpoint
    - model-download
    - job-status
    - request-body
    - response-fields
category: reference
---

`POST /api/v1/models/download`

**Request body**

model : string

The model to download. Accepts [model catalog](https://lmstudio.ai/models) identifiers (e.g., `openai/gpt-oss-20b`) and exact Hugging Face links (e.g., `https://huggingface.co/lmstudio-community/gpt-oss-20b-GGUF`)

quantization (optional) : string

Quantization level of the model to download (e.g., `Q4_K_M`). Only supported for Hugging Face links.

**Response fields**

Returns a download job status object. The response varies based on the download status.

job\_id (optional) : string

Unique identifier for the download job. Absent when `status` is `already_downloaded`.

status : "downloading" | "paused" | "completed" | "failed" | "already\_downloaded"

Current status of the download.

completed\_at (optional) : string

Download completion time in ISO 8601 format. Present when `status` is `completed`.

total\_size\_bytes (optional) : number

Total size of the download in bytes. Absent when `status` is `already_downloaded`.

started\_at (optional) : string

Download start time in ISO 8601 format. Absent when `status` is `already_downloaded`.