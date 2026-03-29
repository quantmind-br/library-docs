---
title: Braintrust - Evals + Logging | liteLLM
url: https://docs.litellm.ai/docs/observability/braintrust
source: sitemap
fetched_at: 2026-01-21T19:45:56.270110809-03:00
rendered_js: false
word_count: 305
summary: This guide explains how to integrate LiteLLM with Braintrust to automate logging, evaluation, and trace management for AI applications. It details setup procedures for both the Python SDK and the OpenAI-compatible proxy, including advanced metadata and span customization.
tags:
    - litellm
    - braintrust
    - observability
    - ai-logging
    - llm-proxy
    - tracing
    - python-sdk
category: guide
---

[Braintrust](https://www.braintrust.dev/) manages evaluations, logging, prompt playground, to data management for AI products.

## Quick Start[​](#quick-start "Direct link to Quick Start")

```
# pip install braintrust
import litellm
import os

# set env
os.environ["BRAINTRUST_API_KEY"]=""
os.environ["BRAINTRUST_API_BASE"]="https://api.braintrustdata.com/v1"
os.environ['OPENAI_API_KEY']=""

# set braintrust as a callback, litellm will send the data to braintrust
litellm.callbacks =["braintrust"]

# openai call
response = litellm.completion(
  model="gpt-3.5-turbo",
  messages=[
{"role":"user","content":"Hi 👋 - i'm openai"}
]
)
```

## OpenAI Proxy Usage[​](#openai-proxy-usage "Direct link to OpenAI Proxy Usage")

1. Add keys to env

```
BRAINTRUST_API_KEY=""
BRAINTRUST_API_BASE="https://api.braintrustdata.com/v1"
```

2. Add braintrust to callbacks

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: gpt-3.5-turbo
api_key: os.environ/OPENAI_API_KEY

litellm_settings:
callbacks:["braintrust"]
```

3. Test it!

```
curl -X POST 'http://0.0.0.0:4000/chat/completions' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer sk-1234' \
-D '{
    "model": "groq-llama3",
    "messages": [
        { "role": "system", "content": "Use your tools smartly"},
        { "role": "user", "content": "What time is it now? Use your tool"}
    ]
}'
```

## Advanced - pass Project ID or name[​](#advanced---pass-project-id-or-name "Direct link to Advanced - pass Project ID or name")

It is recommended that you include the `project_id` or `project_name` to ensure your traces are being written out to the correct Braintrust project.

### Custom Span Names[​](#custom-span-names "Direct link to Custom Span Names")

You can customize the span name in Braintrust logging by passing `span_name` in the metadata. By default, the span name is set to "Chat Completion".

### Custom Span Attributes[​](#custom-span-attributes "Direct link to Custom Span Attributes")

You can customize the span id, root span name and span parents in Braintrust logging by passing `span_id`, `root_span_id` and `span_parents` in the metadata. `span_parents` should be a string containing a list of span ids, joined by ,

- SDK
- PROXY

```
response = litellm.completion(
  model="gpt-3.5-turbo",
  messages=[
{"role":"user","content":"Hi 👋 - i'm openai"}
],
  metadata={
"project_id":"1234",
# passing project_name will try to find a project with that name, or create one if it doesn't exist
# if both project_id and project_name are passed, project_id will be used
# "project_name": "my-special-project",
# custom span name for this operation (default: "Chat Completion")
"span_name":"User Greeting Handler"
}
)
```

Note: Other `metadata` can be included here as well when using the SDK.

```
response = litellm.completion(
  model="gpt-3.5-turbo",
  messages=[
{"role":"user","content":"Hi 👋 - i'm openai"}
],
  metadata={
"project_id":"1234",
"span_name":"Custom Operation",
"item1":"an item",
"item2":"another item"
}
)
```

You can use `BRAINTRUST_API_BASE` to point to your self-hosted Braintrust data plane. Read more about this [here](https://www.braintrust.dev/docs/guides/self-hosting).

## Full API Spec[​](#full-api-spec "Direct link to Full API Spec")

Here's everything you can pass in metadata for a braintrust request

`braintrust_*` - If you are adding metadata from *proxy request headers*, any metadata field starting with `braintrust_` will be passed as metadata to the logging request. If you are using the SDK, just pass your metadata like normal (e.g., `metadata={"project_name": "my-test-project", "item1": "an item", "item2": "another item"}`)

`project_id` - Set the project id for a braintrust call. Default is `litellm`.

`project_name` - Set the project name for a braintrust call. Will try to find a project with that name, or create one if it doesn't exist. If both `project_id` and `project_name` are passed, `project_id` will be used.

`span_name` - Set a custom span name for the operation. Default is `"Chat Completion"`. Use this to provide more descriptive names for different types of operations in your application (e.g., "User Query", "Document Summary", "Code Generation").