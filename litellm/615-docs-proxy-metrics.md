---
title: "\U0001F4B8 GET Daily Spend, Usage Metrics | liteLLM"
url: https://docs.litellm.ai/docs/proxy/metrics
source: sitemap
fetched_at: 2026-01-21T19:52:56.412869342-03:00
rendered_js: false
word_count: 0
summary: This document illustrates the data structure used for reporting daily and total expenditures across various AI models and individual API keys.
tags:
    - billing-data
    - usage-tracking
    - cost-analysis
    - api-metrics
    - model-usage
category: reference
---

```
[
    daily_spend = [
{
"daily_spend":7.9261938052047e+16,
"day":"2024-02-01T00:00:00",
"spend_per_model":{"azure/gpt-4":7.9261938052047e+16},
"spend_per_api_key":{
"76":914495704992000.0,
"12":905726697912000.0,
"71":866312628003000.0,
"28":865461799332000.0,
"13":859151538396000.0
}
},
{
"daily_spend":7.938489251309491e+16,
"day":"2024-02-02T00:00:00",
"spend_per_model":{"gpt-3.5":7.938489251309491e+16},
"spend_per_api_key":{
"91":896805036036000.0,
"78":889692646082000.0,
"49":885386687861000.0,
"28":873869890984000.0,
"56":867398637692000.0
}
}

],
    total_spend = 200,
    top_models = {"gpt4":0.2,"vertexai/gemini-pro":10},
    top_api_keys = {"899922":0.9,"838hcjd999seerr88":20}

]

```