---
title: List Evaluators - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/list-evaluators
source: sitemap
fetched_at: 2026-04-27T20:19:07.790563622-03:00
rendered_js: false
word_count: 0
summary: This document provides a JSON structure that outlines the metadata for an evaluator, detailing its various attributes such as name, status, creation time, and associated evaluation criteria.
tags:
    - evaluator-metadata
    - json-structure
    - evaluation-object
    - api-payload
    - criteria-list
    - github-source
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
```
{
  "evaluators": [
    {
      "name": "<string>",
      "displayName": "<string>",
      "description": "<string>",
      "createTime": "2023-11-07T05:31:56Z",
      "createdBy": "<string>",
      "updateTime": "2023-11-07T05:31:56Z",
      "state": "STATE_UNSPECIFIED",
      "criteria": [
        {
          "type": "TYPE_UNSPECIFIED",
          "name": "<string>",
          "description": "<string>",
          "codeSnippets": {
            "language": "<string>",
            "fileContents": {},
            "entryFile": "<string>",
            "entryFunc": "<string>"
          }
        }
      ],
      "requirements": "<string>",
      "entryPoint": "<string>",
      "status": {
        "code": "OK",
        "message": "<string>"
      },
      "commitHash": "<string>",
      "source": {
        "type": "TYPE_UNSPECIFIED",
        "githubRepositoryName": "<string>"
      },
      "defaultDataset": "<string>"
    }
  ],
  "nextPageToken": "<string>",
  "totalSize": 123
}
```
