---
title: Known Limitations | Mistral Docs
url: https://docs.mistral.ai/resources/known-limitations
source: sitemap
fetched_at: 2026-04-26T04:11:38.70339453-03:00
rendered_js: false
word_count: 401
summary: Technical constraints, rate limits, and operational requirements for the Mistral platform API services.
tags:
    - api-limitations
    - rate-limits
    - token-usage
    - file-upload
    - json-mode
    - batch-processing
    - model-constraints
category: reference
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Known Limitations

Current platform limitations. Check [changelogs](https://docs.mistral.ai/resources/changelogs) for updates.

## Context Window

- Requests exceeding the model's context window return a `400 Bad Request` error.
- Token counts include both input and output tokens. Plan your `max_tokens` accordingly.

## Rate Limits

Rate limits vary by subscription tier and model. When exceeded, the API returns `429 Too Many Requests`.

- **Requests per second** and **tokens per minute** are enforced independently.
- Limits apply per API key, not per workspace.
- [Batch processing](https://docs.mistral.ai/studio-api/batch-processing) does not count against real-time rate limits.
- Check `X-RateLimit-Remaining` response header to monitor usage.

## File Upload

- Maximum file size: **512 MB**
- Supported formats for OCR: PDF, PNG, JPG, JPEG, TIFF, BMP, GIF, WEBP
- Uploaded files are retained for 30 days unless deleted earlier.

## Batch Processing

- Maximum batch file size: **512 MB**
- Maximum requests per batch: **100,000**
- Batch jobs are processed asynchronously; completion time depends on queue depth and request complexity.
- Batch results are available for download for **24 hours** after completion.

## Streaming

- Streaming connections time out after **10 minutes** of inactivity.
- `stream_options.include_usage` must be explicitly set to receive token usage in stream events.
- Some client HTTP libraries may buffer streamed responses; ensure chunked transfer encoding is handled correctly.

## Tools

- Maximum number of tools per request: **128**
- Tool descriptions are included in the token count. Long descriptions reduce available context for messages.
- Parallel function calls are supported but may return calls in any order.
- `tool_choice: "any"` forces a tool call but does not guarantee which tool is selected.

## JSON Mode

- When `response_format: {"type": "json_object"}` is set, the model always returns valid JSON.
- You must include "JSON" in the system or user prompt. Otherwise the model may produce an infinite whitespace stream.
- JSON mode does not guarantee adherence to a specific schema. Use function calling for structured outputs.

## Image Input

- Maximum image size: **20 MB** per image.
- Supported formats: PNG, JPG, JPEG, GIF, WEBP.
- Maximum images per request depends on the model and total token budget.
- Images are resized internally; very small images may lose detail.

## Audio Input

- Supported formats: WAV, MP3, FLAC, OGG, WEBM.
- Maximum audio duration: **60 minutes**.
- Maximum file size: **500 MB**.
- Transcription is optimized for clear speech; heavy background noise reduces accuracy.

## Data Residency

- The Mistral API is served from EU data centers by default.
- Some models may not be available in all regions. Check the [models page](https://docs.mistral.ai/models) for details.

#api-limitations #rate-limits #token-usage #file-upload #json-mode #batch-processing #model-constraints
