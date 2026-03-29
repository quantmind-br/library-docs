---
title: /moderations | liteLLM
url: https://docs.litellm.ai/docs/moderation
source: sitemap
fetched_at: 2026-01-21T19:45:47.654579569-03:00
rendered_js: false
word_count: 0
summary: This document provides a sample JSON response format from a text moderation API, illustrating how content safety flags and confidence scores are structured.
tags:
    - moderation-api
    - content-safety
    - json-schema
    - api-response
    - text-classification
    - safety-filters
category: reference
---

```
{
"id":"modr-AB8CjOTu2jiq12hp1AQPfeqFWaORR",
"model":"text-moderation-007",
"results":[
{
"flagged": true,
"categories":{
"sexual": false,
"hate": false,
"harassment": true,
"self-harm": false,
"sexual/minors": false,
"hate/threatening": false,
"violence/graphic": false,
"self-harm/intent": false,
"self-harm/instructions": false,
"harassment/threatening": true,
"violence": true
},
"category_scores":{
"sexual":0.000011726012417057063,
"hate":0.22706663608551025,
"harassment":0.5215635299682617,
"self-harm":2.227119921371923e-6,
"sexual/minors":7.107352217872176e-8,
"hate/threatening":0.023547329008579254,
"violence/graphic":0.00003391829886822961,
"self-harm/intent":1.646940972932498e-6,
"self-harm/instructions":1.1198755256458526e-9,
"harassment/threatening":0.5694745779037476,
"violence":0.9971134662628174
}
}
]
}

```