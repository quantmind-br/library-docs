---
title: Transformers Fallback in SGLang - SGLang Documentation
url: https://docs.sglang.io/docs/supported-models/transformers_fallback
source: sitemap
fetched_at: 2026-05-11T05:48:04.135561328-03:00
rendered_js: false
word_count: 191
summary: This document explains how to utilize the transformers fallback mechanism in SGLang to run various language models and outlines the requirements for custom models to integrate with the SGLang backend.
tags:
    - sglang
    - transformers-fallback
    - model-deployment
    - quantization
    - custom-models
category: guide
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

`sglang` can fall back to using models that are available in `transformers`. This works for most decoder-style language models and support for vision-language models is coming soon!

## Example launch Command

By default, we will use sglang implementation if it is available. Otherwise, we will fall back to transformers one. However, you can switch the implementation by setting `--model-impl` to `transformers`.

```
python3 -m sglang.launch_server \
  --model-path meta-llama/Llama-3.2-1B-Instruct \
  --host 0.0.0.0 \
  --port 30000 \
  --model-impl transformers
```

## Supported features

### Quantization

Transformers fall back has supported most of available quantization in SGLang (except GGUF). See [Quantization page](https://docs.sglang.io/docs/advanced_features/quantization) for more information about supported quantization in SGLang.

### Remote code

This fallback also means that any model on the hub that can be used in `transformers` with `trust_remote_code=True` that correctly implements attention can be used in production! A model just needs the following two things:

```
from transformers import PreTrainedModel
from torch import nn

class MyAttention(nn.Module):

  def forward(self, hidden_states, **kwargs): # <- kwargs are required

    ...
    attention_interface = ALL_ATTENTION_FUNCTIONS[self.config._attn_implementation]
    attn_output, attn_weights = attention_interface(
      self,
      query_states,
      key_states,
      value_states,
      **kwargs,
    )
    ...

class MyModel(PreTrainedModel):
  _supports_attention_backend = True
```

Here is what happens in the background:

1. The config is loaded
2. `MyModel` python class is loaded from the `auto_map`, and we check that the model `_supports_attention_backend`.
3. The `TransformersModel` backend is used. See `/srt/models/transformers`, which leverages `self.config._attn_implementation = "sglang"`, thus the need to use `ALL_ATTENTION_FUNCTIONS`.

That’s it!