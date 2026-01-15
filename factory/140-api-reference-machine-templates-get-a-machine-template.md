---
title: Get a machine template - Factory Documentation
url: https://docs.factory.ai/api-reference/machine-templates/get-a-machine-template
source: sitemap
fetched_at: 2026-01-13T19:03:19.331828892-03:00
rendered_js: false
word_count: 0
summary: Defines the JSON schema for a template object, detailing properties for identification, repository configuration, build status, environment variables, and setup scripts.
tags:
    - json-schema
    - template-configuration
    - environment-variables
    - build-status
    - data-structure
category: reference
---

```
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
```