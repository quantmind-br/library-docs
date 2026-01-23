---
title: Greenscale - Track LLM Spend and Responsible Usage | liteLLM
url: https://docs.litellm.ai/docs/observability/greenscale_integration
source: sitemap
fetched_at: 2026-01-21T19:46:07.181337601-03:00
rendered_js: false
word_count: 130
summary: This document explains how to integrate Greenscale with liteLLM to monitor GenAI spending and usage through automated metadata logging and callbacks.
tags:
    - litellm
    - greenscale
    - llm-monitoring
    - observability
    - metadata-logging
    - callbacks
category: tutorial
---

[Greenscale](https://greenscale.ai/) is a production monitoring platform for your LLM-powered app that provides you granular key insights into your GenAI spending and responsible usage. Greenscale only captures metadata to minimize the exposure risk of personally identifiable information (PII).

liteLLM provides `callbacks`, making it easy for you to log data depending on the status of your responses.

First, email `hello@greenscale.ai` to get an API\_KEY.

Use just 1 line of code, to instantly log your responses **across all providers** with Greenscale:

```
from litellm import completion

## set env variables
os.environ['GREENSCALE_API_KEY']='your-greenscale-api-key'
os.environ['GREENSCALE_ENDPOINT']='greenscale-endpoint'
os.environ["OPENAI_API_KEY"]=""

# set callback
litellm.success_callback =["greenscale"]

#openai call
response = completion(
  model="gpt-3.5-turbo",
  messages=[{"role":"user","content":"Hi 👋 - i'm openai"}]
  metadata={
"greenscale_project":"acme-project",
"greenscale_application":"acme-application"
}
)
```

You can send any additional information to Greenscale by using the `metadata` field in completion and `greenscale_` prefix. This can be useful for sending metadata about the request, such as the project and application name, customer\_id, environment, or any other information you want to track usage. `greenscale_project` and `greenscale_application` are required fields.

```
#openai call with additional metadata
response = completion(
  model="gpt-3.5-turbo",
  messages=[
{"role":"user","content":"Hi 👋 - i'm openai"}
],
  metadata={
"greenscale_project":"acme-project",
"greenscale_application":"acme-application",
"greenscale_customer_id":"customer-123"
}
)
```