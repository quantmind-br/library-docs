---
title: Custom Arguments - vLLM
url: https://docs.vllm.ai/en/latest/features/custom_arguments/
source: sitemap
fetched_at: 2026-05-07T21:14:06.919621916-03:00
rendered_js: false
word_count: 197
summary: This document explains how to pass user-defined custom arguments into vLLM requests without source code modification by using the extra_args and vllm_xargs mechanisms.
tags:
    - vllm
    - custom-arguments
    - sampling-params
    - rest-api
    - logits-processor
    - inference
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/features/custom_arguments.md "Edit this page")

You can use vLLM *custom arguments* to pass in arguments which are not part of the vLLM [`SamplingParams`](https://docs.vllm.ai/en/latest/api/vllm/sampling_params/#vllm.sampling_params.SamplingParams "            SamplingParams") and REST API specifications. Adding or removing a vLLM custom argument does not require recompiling vLLM, since the custom arguments are passed in as a dictionary.

Custom arguments can be useful if, for example, you want to use a [custom logits processor](https://docs.vllm.ai/en/latest/features/custom_logitsprocs/) without modifying the vLLM source code.

Note

Make sure your custom logits processor have implemented `validate_params` for custom arguments. Otherwise, invalid custom arguments can cause unexpected behaviour.

## Offline Custom Arguments[¶](#offline-custom-arguments "Permanent link")

Custom arguments passed to `SamplingParams.extra_args` as a `dict` will be visible to any code which has access to [`SamplingParams`](https://docs.vllm.ai/en/latest/api/vllm/sampling_params/#vllm.sampling_params.SamplingParams "            SamplingParams"):

```
SamplingParams(extra_args={"your_custom_arg_name": 67})
```

This allows arguments which are not already part of [`SamplingParams`](https://docs.vllm.ai/en/latest/api/vllm/sampling_params/#vllm.sampling_params.SamplingParams "            SamplingParams") to be passed into [`LLM`](https://docs.vllm.ai/en/latest/api/vllm/entrypoints/llm/#vllm.entrypoints.llm.LLM "            LLM") as part of a request.

## Online Custom Arguments[¶](#online-custom-arguments "Permanent link")

The vLLM REST API allows custom arguments to be passed to the vLLM server via `vllm_xargs`. The example below integrates custom arguments into a vLLM REST API request:

```
curlhttp://localhost:8000/v1/completions\
-H"Content-Type: application/json"\
-d'{
        "model": "Qwen/Qwen2.5-1.5B-Instruct",
        ...
        "vllm_xargs": {"your_custom_arg": 67}
    }'
```

Furthermore, OpenAI SDK users can access `vllm_xargs` via the `extra_body` argument:

```
batch = await client.completions.create(
    model="Qwen/Qwen2.5-1.5B-Instruct",
    ...,
    extra_body={
        "vllm_xargs": {
            "your_custom_arg": 67
        }
    }
)
```

Note

`vllm_xargs` is assigned to `SamplingParams.extra_args` under the hood, so code which uses `SamplingParams.extra_args` is compatible with both offline and online scenarios.