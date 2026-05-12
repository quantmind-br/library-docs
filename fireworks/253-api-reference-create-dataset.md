---
title: Create Dataset
optimized: true
optimized_at: 2026-04-27T00:00:00Z
word_count: 155
---
> [!info] Auth: Bearer token required. Format: `Bearer <API_KEY>`

## Response

| Field | Type | Default | Description |
|---|---|---|---|
| `createTime` | string (date-time) | — | read-only. Dataset creation time. |
| `state` | enum | `STATE_UNSPECIFIED` | read-only. |
| `status` | object | — | read-only. Mirrors [google/rpc/status.proto](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto). |
| `format` | enum | `FORMAT_UNSPECIFIED` | Dataset format. |
| `email` | string | — | User who initiated the fine-tuning job. |
| `updateTime` | string (date-time) | — | read-only. Last update time. |
| `createdByJob` | string | — | Resource name of the job that created this dataset (e.g., batch inference job). Used for lineage tracking. |
| `tokenCount` | integer | — | Estimated token count in the dataset. |
| `avgTurnsPerSample` | number | — | Average turns per sample. |

### State Options

`STATE_UNSPECIFIED`, `UPLOADING`, `READY`

### Format Options

`FORMAT_UNSPECIFIED`, `CHAT`, `COMPLETION`, `RL`
