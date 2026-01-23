---
title: v1.65.0-stable - Model Context Protocol
url: https://docs.litellm.ai/release_notes/v1.65.0-stable
source: sitemap
fetched_at: 2026-01-21T19:43:30.00368969-03:00
rendered_js: false
word_count: 0
summary: This document illustrates the structure of an API usage report, detailing metrics such as token consumption and financial spend broken down by date and model.
tags:
    - usage-metrics
    - api-response
    - billing-data
    - token-tracking
    - spend-analysis
category: reference
---

```
{
"results":[
{
"date":"2025-03-27",
"metrics":{
"spend":0.0177072,
"prompt_tokens":111,
"completion_tokens":1711,
"total_tokens":1822,
"api_requests":11
},
"breakdown":{
"models":{
"gpt-4o-mini":{
"spend":1.095e-05,
"prompt_tokens":37,
"completion_tokens":9,
"total_tokens":46,
"api_requests":1
},
"providers":{"openai":{ ... },"azure_ai":{ ... }},
"api_keys":{"3126b6eaf1...":{ ... }}
}
}
],
"metadata":{
"total_spend":0.7274667,
"total_prompt_tokens":280990,
"total_completion_tokens":376674,
"total_api_requests":14
}
}
```