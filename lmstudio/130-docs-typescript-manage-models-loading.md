---
title: Manage Models in Memory
url: https://lmstudio.ai/docs/typescript/manage-models/loading
source: sitemap
fetched_at: 2026-04-07T21:28:51.283137822-03:00
rendered_js: false
word_count: 393
summary: This document details how to programmatically manage AI models using LM Studio's SDK, covering methods for retrieving currently loaded models, loading new instances, unloading models from memory, and setting load-time configuration parameters.
tags:
    - sdk
    - model-management
    - loading
    - unloading
    - llm-studio
    - api
category: reference
---

AI models are huge. It can take a while to load them into memory. LM Studio's SDK allows you to precisely control this process.

**Most commonly:**

- Use `.model()` to get any currently loaded model
- Use `.model("model-key")` to use a specific model

**Advanced (manual model management):**

- Use `.load("model-key")` to load a new instance of a model
- Use `model.unload()` to unload a model from memory

## Get the Current Model with `.model()`[](#get-the-current-model-with-model "Link to 'Get the Current Model with ,[object Object]'")

If you already have a model loaded in LM Studio (either via the GUI or `lms load`), you can use it by calling `.model()` without any arguments.

## Get a Specific Model with `.model("model-key")`[](#get-a-specific-model-with-modelmodel-key "Link to 'Get a Specific Model with ,[object Object]'")

If you want to use a specific model, you can provide the model key as an argument to `.model()`.

#### Get if Loaded, or Load if not

Calling `.model("model-key")` will load the model if it's not already loaded, or return the existing instance if it is.

## Load a New Instance of a Model with `.load()`[](#load-a-new-instance-of-a-model-with-load "Link to 'Load a New Instance of a Model with ,[object Object]'")

Use `load()` to load a new instance of a model, even if one already exists. This allows you to have multiple instances of the same or different models loaded at the same time.

### Note about Instance Identifiers[](#note-about-instance-identifiers)

If you provide an instance identifier that already exists, the server will throw an error. So if you don't really care, it's safer to not provide an identifier, in which case the server will generate one for you. You can always check in the server tab in LM Studio, too!

## Unload a Model from Memory with `.unload()`[](#unload-a-model-from-memory-with-unload "Link to 'Unload a Model from Memory with ,[object Object]'")

Once you no longer need a model, you can unload it by simply calling `unload()` on its handle.

## Set Custom Load Config Parameters[](#set-custom-load-config-parameters "Link to 'Set Custom Load Config Parameters'")

You can also specify the same load-time configuration options when loading a model, such as Context Length and GPU offload.

See [load-time configuration](https://lmstudio.ai/docs/typescript/llm-prediction/parameters) for more.

## Set an Auto Unload Timer (TTL)[](#set-an-auto-unload-timer-ttl "Link to 'Set an Auto Unload Timer (TTL)'")

You can specify a *time to live* for a model you load, which is the idle time (in seconds) after the last request until the model unloads. See [Idle TTL](https://lmstudio.ai/docs/api/ttl-and-auto-evict) for more on this.