---
title: Get Load Config
url: https://lmstudio.ai/docs/python/model-info/get-load-config
source: sitemap
fetched_at: 2026-04-07T21:31:30.977524762-03:00
rendered_js: false
word_count: 73
summary: This document explains how to retrieve the configuration parameters used when loading a specific model using the LM Studio Python SDK.
tags:
    - python-sdk
    - load-model
    - configuration
    - llm
    - api
category: reference
---

*Required Python SDK version*: **1.2.0**

LM Studio allows you to configure certain parameters when loading a model [through the server UI](https://lmstudio.ai/docs/advanced/per-model) or [through the API](https://lmstudio.ai/docs/api/sdk/load-model).

You can retrieve the config with which a given model was loaded using the SDK.

In the below examples, the LLM reference can be replaced with an embedding model reference without requiring any other changes.

Pro Tip

Context length is a special case that [has its own method](https://lmstudio.ai/docs/api/sdk/get-context-length).

```
import lmstudio as lms

model = lms.llm()

print(model.get_load_config())
```