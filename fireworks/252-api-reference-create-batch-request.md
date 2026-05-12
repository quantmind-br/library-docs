---
title: Create Batch Request
optimized: true
optimized_at: 2026-04-27T00:00:00Z
word_count: 171
---
> [!info] Auth: Provide Fireworks API key via `Authorization: FIREWORKS_API_KEY` header or `api_key` query param.

## Path Parameters

| Param | Type | Description |
|---|---|---|
| `path` | string | Relative route of target API operation (e.g. `"v1/audio/transcriptions"`, `"v1/audio/translations"`). Must be a valid backend route. |

## Body

Request body must conform to the schema defined by the selected `endpoint_id` and `path`. For example, transcription requests accept `model`, `diarize`, `response_format` fields.

> [!tip] See [[287-api-reference-audio-transcriptions]] or [[288-api-reference-audio-translations]] for required fields.

## Response

| Field | Type | Description |
|---|---|---|
| `status` | string | Batch submission status. `"submitted"` = accepted and queued. |
| `batchId` | string | Unique batch job ID for status checks and result retrieval. |
| `accountId` | string | Account ID associated with the batch job. |
| `backend` | string | Backend service selected to process the request. |
| `message` | string | Human-readable result message. Typically `"Request submitted successfully"`. |

> [!tip] Check batch status with [[226-api-reference-get-batch-status]] using the returned `batch_id`.
