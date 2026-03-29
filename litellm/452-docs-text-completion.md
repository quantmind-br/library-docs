---
title: /completions | liteLLM
url: https://docs.litellm.ai/docs/text_completion
source: sitemap
fetched_at: 2026-01-21T19:54:52.91637695-03:00
rendered_js: false
word_count: 0
summary: This document illustrates the structure and schema of a response object from a text completion API, including metadata, generation results, and token usage statistics.
tags:
    - api-response
    - text-completion
    - json-structure
    - openai-api
    - token-usage
category: reference
---

```
{
"id":"cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",
"object":"text_completion",
"created":1589478378,
"model":"gpt-3.5-turbo-instruct",
"system_fingerprint":"fp_44709d6fcb",
"choices":[
{
"text":"\n\nThis is indeed a test",
"index":0,
"logprobs": null,
"finish_reason":"length"
}
],
"usage":{
"prompt_tokens":5,
"completion_tokens":7,
"total_tokens":12
}
}

```