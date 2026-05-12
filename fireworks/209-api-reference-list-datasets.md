---
title: List Datasets - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/list-datasets
source: sitemap
fetched_at: 2026-04-27T20:14:03.408477091-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - dataset-metadata
    - api-response
    - data-structure
    - dataset-properties
    - json-schema
category: reference
word_count: 60
---
# List Datasets

`GET /datasets` — Returns a paginated list of datasets in the account.

## Response Schema

```json
{
  "datasets": [
    {
      "name": "<string>",
      "displayName": "<string>",
      "createTime": "2023-11-07T05:31:56Z",
      "state": "STATE_UNSPECIFIED",
      "status": {
        "code": "OK",
        "message": "<string>"
      },
      "exampleCount": "<string>",
      "userUploaded": {},
      "evaluationResult": {
        "evaluationJobId": "<string>"
      },
      "transformed": {
        "sourceDatasetId": "<string>",
        "filter": "<string>",
        "originalFormat": "FORMAT_UNSPECIFIED"
      },
      "splitted": {
        "sourceDatasetId": "<string>"
      },
      "evalProtocol": {},
      "externalUrl": "<string>",
      "format": "FORMAT_UNSPECIFIED",
      "createdBy": "<string>",
      "updateTime": "2023-11-07T05:31:56Z",
      "sourceJobName": "<string>",
      "estimatedTokenCount": "<string>",
      "averageTurnCount": 123
    }
  ],
  "nextPageToken": "<string>",
  "totalSize": 123
}
```

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `datasets` | array | List of dataset objects. |
| `nextPageToken` | string | Token for fetching the next page. |
| `totalSize` | integer | Total number of datasets. |