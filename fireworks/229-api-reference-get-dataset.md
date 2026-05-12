---
title: Get Dataset - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/get-dataset
source: sitemap
fetched_at: 2026-04-27T20:14:24.309948261-03:00
rendered_js: false
word_count: 10
summary: This document presents a structured JSON schema that defines the metadata fields available for an entity, detailing attributes such as its name, creation time, status, and various transformation details.
tags:
    - json-schema
    - metadata
    - data-structure
    - api-response
    - document-definition
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Get Dataset

Response schema for dataset details.

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

#api-reference #datasets
