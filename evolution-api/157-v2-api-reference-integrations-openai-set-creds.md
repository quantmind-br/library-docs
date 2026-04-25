---
title: Creds config OpenAI - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/openai/set-creds
source: sitemap
fetched_at: 2026-04-12T18:48:16.187825428-03:00
rendered_js: false
word_count: 20
summary: This document provides an example using cURL to illustrate how to send a POST request to configure the OpenAI credentials for a specific bot instance.
tags:
    - curl
    - post-request
    - openai-credentials
    - api-call
    - configuration
category: reference
---

```
curl --request POST \
  --url https://evolution-example/openai/creds/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "apiKey": "<string>",
  "name": "<string>"
}
'

This response has no body data.

curl --request POST \
  --url https://evolution-example/openai/creds/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "apiKey": "<string>",
  "name": "<string>"
}
'

This response has no body data.
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

Configuration for the OpenAI bot instance

#### Response

[Find OpenIA Creds](https://doc.evolution-api.com/v2/api-reference/integrations/openai/find-creds-openai)[Delete OpenIA Bot](https://doc.evolution-api.com/v2/api-reference/integrations/openai/delete-creds)