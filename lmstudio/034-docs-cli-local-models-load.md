---
title: '`lms load`'
url: https://lmstudio.ai/docs/cli/local-models/load
source: sitemap
fetched_at: 2026-04-07T21:28:33.842865105-03:00
rendered_js: false
word_count: 463
summary: This document serves as a comprehensive guide detailing how to use the `lms load` command to manage model loading in memory, covering various optional parameters like context length and GPU offloading. It also explains how to unload models using `lms unload`.
tags:
    - model-management
    - cli-guide
    - loading-models
    - gpu-configuration
    - api-commands
category: guide
---

The `lms load` command loads a model into memory. You can optionally set parameters such as context length, GPU offload, and TTL. This guide also covers unloading models with `lms unload`.

### Flags[](#flags)

\[path] (optional) : string

The path of the model to load. If not provided, you will be prompted to select one

--ttl (optional) : number

If provided, when the model is not used for this number of seconds, it will be unloaded

--gpu (optional) : string

How much to offload to the GPU. Values: 0-1, off, max

--context-length (optional) : number

The number of tokens to consider as context when generating text

--identifier (optional) : string

The identifier to assign to the loaded model for API reference

--estimate-only (optional) : boolean

Print a resource (memory) estimate and exit without loading the model

## Load a model[](#load-a-model "Link to 'Load a model'")

Load a model into memory by running the following command:


You can find the `model_key` by first running [`lms ls`](https://lmstudio.ai/docs/cli/local-models/ls) to list your locally downloaded models.

### Set a custom identifier[](#set-a-custom-identifier)

Optionally, you can assign a custom identifier to the loaded model for API reference:

```

lms load <model_key> --identifier "my-custom-identifier"
```

You will then be able to refer to this model by the identifier `my_model` in subsequent commands and API calls (`model` parameter).

### Set context length[](#set-context-length)

You can set the context length when loading a model using the `--context-length` flag:

```

lms load <model_key> --context-length 4096
```

This determines how many tokens the model will consider as context when generating text.

### Set GPU offload[](#set-gpu-offload)

Control GPU memory usage with the `--gpu` flag:

```

lms load <model_key> --gpu 0.5    # Offload 50% of layers to GPU
lms load <model_key> --gpu max    # Offload all layers to GPU
lms load <model_key> --gpu off    # Disable GPU offloading
```

If not specified, LM Studio will automatically determine optimal GPU usage.

### Set TTL[](#set-ttl)

Set an auto-unload timer with the `--ttl` flag (in seconds):

```

lms load <model_key> --ttl 3600   # Unload after 1 hour of inactivity
```

### Estimate resources without loading[](#estimate-resources-without-loading)

Preview memory requirements before loading a model using `--estimate-only`:

```

lms load --estimate-only <model_key>
```

Optional flags such as `--context-length` and `--gpu` are honored and reflected in the estimate. The estimator accounts for factors like context length, flash attention, and whether the model is vision‑enabled.

Example:

```

$ lms load --estimate-only gpt-oss-120b
Model: openai/gpt-oss-120b
Estimated GPU Memory:   65.68 GB
Estimated Total Memory: 65.68 GB

Estimate: This model may be loaded based on your resource guardrails settings.
```

## Unload models[](#unload-models "Link to 'Unload models'")

Use `lms unload` to remove models from memory.

### Flags[](#flags)

\[model\_key] (optional) : string

The key of the model to unload. If not provided, you will be prompted to select one

--all (optional) : flag

Unload all currently loaded models

--host (optional) : string

The host address of a remote LM Studio instance to connect to

### Unload a specific model[](#unload-a-specific-model)


If no model key is provided, you will be prompted to select from currently loaded models.

### Unload all models[](#unload-all-models)


### Unload from a remote LM Studio instance[](#unload-from-a-remote-lm-studio-instance)

```

lms unload <model_key> --host <host>
```

## Operate on a remote LM Studio instance[](#operate-on-a-remote-lm-studio-instance "Link to 'Operate on a remote LM Studio instance'")

`lms load` supports the `--host` flag to connect to a remote LM Studio instance.

```

lms load <model_key> --host <host>
```

For this to work, the remote LM Studio instance must be running and accessible from your local machine, e.g. be accessible on the same subnet.