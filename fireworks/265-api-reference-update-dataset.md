---
title: Update Dataset
url: https://docs.fireworks.ai/api-reference/update-dataset
source: sitemap
fetched_at: 2026-04-27T20:13:41.765321826-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - metadata-schema
    - data-structure
    - api-fields
    - document-properties
    - object-definition
category: reference
word_count: 4
---
Dataset metadata response schema.

```json
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
```
