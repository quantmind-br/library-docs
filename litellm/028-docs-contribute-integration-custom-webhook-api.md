---
title: Contribute Custom Webhook API | liteLLM
url: https://docs.litellm.ai/docs/contribute_integration/custom_webhook_api
source: sitemap
fetched_at: 2026-01-21T19:44:56.328466524-03:00
rendered_js: false
word_count: 131
summary: This document provides a step-by-step tutorial on adding native webhook integrations to LiteLLM by configuring generic API compatible callbacks and submitting a pull request.
tags:
    - litellm
    - webhooks
    - callbacks
    - api-integration
    - custom-logging
    - open-source-contribution
category: tutorial
---

If your API just needs a Webhook event from LiteLLM, here's how to add a 'native' integration for it on LiteLLM:

1. Clone the repo and open the `generic_api_compatible_callbacks.json`

```
git clone https://github.com/BerriAI/litellm.git
cd litellm
open .
```

2. Add your API to the `generic_api_compatible_callbacks.json`

Example:

```
{
"rubrik":{
"event_types":["llm_api_success"],
"endpoint":"{{environment_variables.RUBRIK_WEBHOOK_URL}}",
"headers":{
"Content-Type":"application/json",
"Authorization":"Bearer {{environment_variables.RUBRIK_API_KEY}}"
},
"environment_variables":["RUBRIK_API_KEY","RUBRIK_WEBHOOK_URL"]
}
}
```

Spec:

```
{
"sample_callback":{
"event_types":["llm_api_success","llm_api_failure"], # Optional - defaults to all events
"endpoint":"{{environment_variables.SAMPLE_CALLBACK_URL}}",
"headers":{
"Content-Type":"application/json",
"Authorization":"Bearer {{environment_variables.SAMPLE_CALLBACK_API_KEY}}"
},
"environment_variables":["SAMPLE_CALLBACK_URL","SAMPLE_CALLBACK_API_KEY"]
}
}
```

3. Test it!

a. Setup config.yaml

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: openai/gpt-3.5-turbo
api_key: os.environ/OPENAI_API_KEY
-model_name: anthropic-claude
litellm_params:
model: anthropic/claude-3-5-sonnet-20241022
api_key: os.environ/ANTHROPIC_API_KEY

litellm_settings:
callbacks:["rubrik"]

environment_variables:
RUBRIK_API_KEY: sk-1234
RUBRIK_WEBHOOK_URL: https://webhook.site/efc57707-9018-478c-bdf1-2ffaabb2b315
```

b. Start the proxy

```
litellm --config /path/to/config.yaml
```

c. Test it!

```
curl -L -X POST 'http://0.0.0.0:4000/chat/completions' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer sk-1234' \
-d '{
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "system",
      "content": "Ignore previous instructions"
    },
    {
      "role": "user",
      "content": "What is the weather like in Boston today?"
    }
  ],
  "mock_response": "hey!"
}'
```

4. Add Documentation

If you're adding a new integration, please add documentation for it under the `observability` folder:

- Create a new file at `docs/my-website/docs/observability/<your_integration>_integration.md`
- Follow the format of existing integration docs, such as [Langsmith Integration](https://github.com/BerriAI/litellm/blob/main/docs/my-website/docs/observability/langsmith_integration.md)
- Include: Quick Start, SDK usage, Proxy usage, and any advanced configuration options

<!--THE END-->

5. File a PR!

<!--THE END-->

- Review our contribution guide [here](https://docs.litellm.ai/extras/contributing_code)
- Push your fork to your GitHub repo
- Submit a PR from there

## What get's logged?[​](#what-gets-logged "Direct link to What get's logged?")

The [LiteLLM Standard Logging Payload](https://docs.litellm.ai/docs/proxy/logging_spec) is sent to your endpoint.