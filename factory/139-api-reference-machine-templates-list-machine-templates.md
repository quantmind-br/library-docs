---
title: List machine templates - Factory Documentation
url: https://docs.factory.ai/api-reference/machine-templates/list-machine-templates
source: sitemap
fetched_at: 2026-01-13T19:03:20.749625058-03:00
rendered_js: false
word_count: 0
summary: This document outlines the JSON schema for listing templates, including configuration details, build status, environment variables, and pagination metadata.
tags:
    - json-schema
    - template-management
    - pagination
    - environment-variables
    - build-status
category: reference
---

```
{
  "templates": [
    {
      "templateId": "<string>",
      "repoUrl": "<string>",
      "templateName": "<string>",
      "defaultBranch": "<string>",
      "createdBy": "<string>",
      "createdAt": 123,
      "buildStatus": {
        "status": "building",
        "failureReason": "setup_script_error",
        "buildStartedAt": 123,
        "builtAt": 123,
        "logs": "<string>"
      },
      "lastUpdatedAt": 123,
      "environmentVariables": [
        {
          "key": "<string>",
          "value": "<string>"
        }
      ],
      "userEnvironmentVariablesByUser": [
        {
          "key": "<string>",
          "value": "<string>"
        }
      ],
      "setupScript": "<string>"
    }
  ],
  "pagination": {
    "hasMore": true,
    "nextCursor": "<string>"
  }
}
```