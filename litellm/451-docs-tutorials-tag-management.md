---
title: '[Beta] Routing based on request metadata | liteLLM'
url: https://docs.litellm.ai/docs/tutorials/tag_management
source: sitemap
fetched_at: 2026-01-21T19:55:50.376327816-03:00
rendered_js: false
word_count: 181
summary: This document explains how to configure and use tag-based routing in the LiteLLM proxy to control which models are available based on request metadata. It covers the setup process in the configuration file, tag management via the UI, and testing routing rules using the OpenAI SDK.
tags:
    - litellm-proxy
    - tag-routing
    - access-control
    - model-routing
    - configuration-guide
    - request-metadata
category: guide
---

Create routing rules based on request metadata.

## Setup[​](#setup "Direct link to Setup")

Add the following to your litellm proxy config yaml file.

litellm proxy config.yaml

```
router_settings:
enable_tag_filtering:True# 👈 Key Change
```

## 1. Create a tag[​](#1-create-a-tag "Direct link to 1. Create a tag")

On the LiteLLM UI, navigate to Experimental &gt; Tag Management &gt; Create Tag.

Create a tag called `private-data` and only select the allowed models for requests with this tag. Once created, you will see the tag in the Tag Management page.

## 2. Test Tag Routing[​](#2-test-tag-routing "Direct link to 2. Test Tag Routing")

Now we will test the tag based routing rules.

### 2.1 Invalid model[​](#21-invalid-model "Direct link to 2.1 Invalid model")

This request will fail since we send `tags=private-data` but the model `gpt-4o` is not in the allowed models for the `private-data` tag.

Here is an example sending the same request using the OpenAI Python SDK.

- OpenAI Python SDK
- cURL

```
from openai import OpenAI

client = OpenAI(
    api_key="sk-1234",
    base_url="http://0.0.0.0:4000/v1/"
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
{"role":"user","content":"Hello, how are you?"}
],
    extra_body={
"tags":"private-data"
}
)
```

### 2.2 Valid model[​](#22-valid-model "Direct link to 2.2 Valid model")

This request will succeed since we send `tags=private-data` and the model `us.anthropic.claude-3-7-sonnet-20250219-v1:0` is in the allowed models for the `private-data` tag.

Here is an example sending the same request using the OpenAI Python SDK.

- OpenAI Python SDK
- cURL

```
from openai import OpenAI

client = OpenAI(
    api_key="sk-1234",
    base_url="http://0.0.0.0:4000/v1/"
)

response = client.chat.completions.create(
    model="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    messages=[
{"role":"user","content":"Hello, how are you?"}
],
    extra_body={
"tags":"private-data"
}
)
```

## Additional Tag Features[​](#additional-tag-features "Direct link to Additional Tag Features")

- [Sending tags in request headers](https://docs.litellm.ai/docs/proxy/tag_routing#calling-via-request-header)
- [Tag based routing](https://docs.litellm.ai/docs/proxy/tag_routing)
- [Track spend per tag](https://docs.litellm.ai/docs/tutorials/cost_tracking#-custom-tags)
- [Setup Budgets per Virtual Key, Team](https://docs.litellm.ai/docs/tutorials/users)