---
title: kv_transfer_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/attention/kv_transfer_utils/
source: sitemap
fetched_at: 2026-05-07T21:24:02.203904209-03:00
rendered_js: false
word_count: 45
summary: A Python decorator designed to manage KV cache layer transfers by synchronizing data loads and saves before and after the execution of attention layers.
tags:
    - kv-cache
    - decorator
    - attention-layer
    - distributed-inference
    - vllm-framework
    - memory-management
category: api
---

Decorator that handles KV layer transfer prior and after execution of an attention layer, if enabled. Otherwise, the wrapper is a no-op.

On entry: waits for the KV layer from the connector. On exit: saves the KV layer to the connector.

Source code in `vllm/model_executor/layers/attention/kv_transfer_utils.py`

```
defmaybe_transfer_kv_layer(func: Callable) -> Callable:
"""Decorator that handles KV layer transfer prior and after execution of
    an attention layer, if enabled. Otherwise, the wrapper is a no-op.

    On entry: waits for the KV layer from the connector.
    On exit: saves the KV layer to the connector.
    """
    # Import at runtime to avoid circular dependency
    fromvllm.model_executor.layers.attention.attentionimport get_attention_context

    # Inspect the signature ONCE when the decorator is applied.
    sig = inspect.signature(func)
    param_names = list(sig.parameters.keys())

    # Find the index of 'layer_name' parameter.
    try:
        layer_name_index = param_names.index("layer_name")
    except ValueError as e:
        raise TypeError(
            f"Function {func.__name__} must have a 'layer_name' parameter"
        ) frome

    @wraps(func)
    defwrapper(*args, **kwargs):
        if not has_kv_transfer_group() or not is_v1_kv_transfer_group():
            return func(*args, **kwargs)

        layer_name = _resolve_layer_name(args[layer_name_index])

        # Extract attention context (metadata, layer, kv_cache, layer_slot_mapping)
        attn_metadata, _, kv_cache, _ = get_attention_context(layer_name)
        connector = get_kv_transfer_group()
        if attn_metadata is None or not connector.has_connector_metadata():
            return func(*args, **kwargs)

        # Wait for KV layer on entry
        connector.wait_for_layer_load(layer_name)

        # Execute the function
        result = func(*args, **kwargs)

        # Save KV cache layer on exit
        connector.save_kv_layer(layer_name, kv_cache, attn_metadata)

        return result

    return wrapper
```