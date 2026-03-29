---
title: Transformers fallback in SGLang — SGLang
url: https://docs.sglang.io/supported_models/transformers_fallback.html
source: crawler
fetched_at: 2026-02-04T08:47:07.485011945-03:00
rendered_js: false
word_count: 175
summary: This document describes the Transformers fallback mechanism in SGLang, detailing how to enable it for unsupported models and requirements for custom attention implementations.
tags:
    - sglang
    - transformers-fallback
    - model-implementation
    - quantization
    - remote-code
    - backend-configuration
category: guide
---

## Contents

## Transformers fallback in SGLang[#](#transformers-fallback-in-sglang "Link to this heading")

`sglang` can fall back to using models that are available in `transformers`. This works for most decoder-style language models and support for vision-language models is coming soon!

## Example launch Command[#](#example-launch-command "Link to this heading")

By default, we will use sglang implementation if it is available. Otherwise, we will fall back to transformers one. However, you can switch the implementation by setting `--model-impl` to `transformers`.

```
python3-msglang.launch_server\
--model-pathmeta-llama/Llama-3.2-1B-Instruct\
--host0.0.0.0\
--port30000\
--model-impltransformers
```

## Supported features[#](#supported-features "Link to this heading")

### Quantization[#](#quantization "Link to this heading")

Transformers fall back has supported most of available quantization in SGLang (except GGUF). See [Quantization page](https://docs.sglang.io/advanced_features/quantization.html) for more information about supported quantization in SGLang.

### Remote code[#](#remote-code "Link to this heading")

This fallback also means that any model on the hub that can be used in `transformers` with `trust_remote_code=True` that correctly implements attention can be used in production!

A model just needs the following two things:

```
fromtransformersimport PreTrainedModel
fromtorchimport nn

classMyAttention(nn.Module):

  defforward(self, hidden_states, **kwargs): # <- kwargs are required

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

classMyModel(PreTrainedModel):
  _supports_attention_backend = True
```

Here is what happens in the background:

1. The config is loaded
2. `MyModel` python class is loaded from the `auto_map`, and we check that the model `_supports_attention_backend`.
3. The `TransformersModel` backend is used. See `/srt/models/transformers`, which leverages `self.config._attn_implementation = "sglang"`, thus the need to use `ALL_ATTENTION_FUNCTIONS`.

That’s it!