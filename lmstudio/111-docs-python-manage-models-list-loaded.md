---
title: List Loaded Models
url: https://lmstudio.ai/docs/python/manage-models/list-loaded
source: sitemap
fetched_at: 2026-04-07T21:29:11.761031953-03:00
rendered_js: false
word_count: 55
summary: This document demonstrates how to programmatically list models that are currently loaded into the system's memory using the SDK.
tags:
    - sdk
    - list-models
    - memory
    - llm
category: reference
---

You can iterate through models loaded into memory using the functions and methods shown below.

The results are full SDK model handles, allowing access to all model functionality.

## List Models Currently Loaded in Memory[](#list-models-currently-loaded-in-memory "Link to 'List Models Currently Loaded in Memory'")

This will give you results equivalent to using [`lms ps`](https://lmstudio.ai/docs/cli/ps) in the CLI.

```
import lmstudio as lms

all_loaded_models = lms.list_loaded_models()
llm_only = lms.list_loaded_models("llm")
embedding_only = lms.list_loaded_models("embedding")

print(all_loaded_models)
```