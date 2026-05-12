---
title: rope_kvcache_fusion - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/fusion/rope_kvcache_fusion/
source: sitemap
fetched_at: 2026-05-07T21:16:32.117686619-03:00
rendered_js: false
word_count: 0
summary: This document defines a pattern matching class used to replace unfused rotary embedding and KV cache update operations with a single, fused operation for improved performance.
tags:
    - graph-optimization
    - pytorch-fx
    - fused-kernels
    - kv-cache
    - rotary-embedding
    - compiler-pass
category: concept
---

```
classRopeReshapeKVCachePattern:
"""
    This pattern matches the following unfused inplace ops:
      q, k = rotary_embedding(positions, q, k, head_size, cos_sin_cache, is_neox)
      kv_cache_dummy = unified_kv_cache_update(k, v, layer_name)

    and replaces it with the fused inplace op:
      kv_cache_dummy = fused_rope_and_unified_kv_cache_update(
        q, k, v, positions, cos_sin_cache, is_neox, layer_name
      )
    """

    FUSED_OP = torch.ops.vllm.fused_rope_and_unified_kv_cache_update.default

    def__init__(
        self,
        layer: Attention,
        is_neox: bool,
    ) -> None:
        self.layer_name = layer.layer_name
        self.num_heads = layer.num_heads
        self.num_kv_heads = layer.num_kv_heads
        self.head_size = layer.head_size
        self.head_size_v = layer.head_size_v
        self.is_neox = is_neox

        self.q_size = self.num_heads * self.head_size
        self.k_size = self.num_kv_heads * self.head_size
        self.v_size = self.num_kv_heads * self.head_size_v

        self.rope_matcher = MatcherRotaryEmbedding(
            is_neox=self.is_neox,
            head_size=self.head_size,
            num_heads=self.num_heads,
            num_kv_heads=self.num_kv_heads,
        )

    defget_inputs(self) -> list:
        # Sample inputs to help pattern tracing
        T = 5
        L = 4096
        qkv = empty_bf16(T, self.q_size + self.k_size + self.v_size)
        positions = empty_i64(T)
        cos_sin_cache = empty_bf16(L, self.head_size)
        inputs: list = [qkv, positions, cos_sin_cache]
        if _USE_LAYERNAME:
            inputs.append(_encode_layer_name(self.layer_name))
        return inputs

    def_mk_pattern_with_layer_name_input(self, _ln):
"""Pattern/replacement with layer_name as an explicit input."""

        defpattern(qkv, positions, cos_sin_cache, layer_name):
            q, k, v = qkv.split([self.q_size, self.k_size, self.v_size], dim=-1)
            q, k = self.rope_matcher(positions, q, k, cos_sin_cache)
            q = q.view(-1, self.num_heads, self.head_size)
            k = k.view(-1, self.num_kv_heads, self.head_size)
            v = v.view(-1, self.num_kv_heads, self.head_size_v)
            return torch.ops.vllm.unified_kv_cache_update(k, v, layer_name), q, k, v

        defreplacement(qkv, positions, cos_sin_cache, layer_name):
            q, k, v = qkv.split([self.q_size, self.k_size, self.v_size], dim=-1)
            q = q.view(-1, self.num_heads, self.head_size)
            k = k.view(-1, self.num_kv_heads, self.head_size)
            v = v.view(-1, self.num_kv_heads, self.head_size_v)
            results = auto_functionalized(
                self.FUSED_OP,
                query=q,
                key=k,
                value=v,
                positions=positions,
                cos_sin_cache=cos_sin_cache,
                is_neox=self.is_neox,
                layer_name=layer_name,
            )
            return results[0], results[1], results[2], v

        return pattern, replacement

    def_mk_pattern_with_layer_name_closure(self, _ln):
"""Pattern/replacement with layer_name as a closure constant."""

        defpattern(qkv, positions, cos_sin_cache):
            q, k, v = qkv.split([self.q_size, self.k_size, self.v_size], dim=-1)
            q, k = self.rope_matcher(positions, q, k, cos_sin_cache)
            q = q.view(-1, self.num_heads, self.head_size)
            k = k.view(-1, self.num_kv_heads, self.head_size)
            v = v.view(-1, self.num_kv_heads, self.head_size_v)
            return torch.ops.vllm.unified_kv_cache_update(k, v, _ln), q, k, v

        defreplacement(qkv, positions, cos_sin_cache):
            q, k, v = qkv.split([self.q_size, self.k_size, self.v_size], dim=-1)
            q = q.view(-1, self.num_heads, self.head_size)
            k = k.view(-1, self.num_kv_heads, self.head_size)
            v = v.view(-1, self.num_kv_heads, self.head_size_v)
            results = auto_functionalized(
                self.FUSED_OP,
                query=q,
                key=k,
                value=v,
                positions=positions,
                cos_sin_cache=cos_sin_cache,
                is_neox=self.is_neox,
                layer_name=_ln,
            )
            return results[0], results[1], results[2], v

        return pattern, replacement

    defregister(self, pm_pass: PatternMatcherPass) -> None:
        _ln = _encode_layer_name(self.layer_name)

        if _USE_LAYERNAME:
            pattern, replacement = self._mk_pattern_with_layer_name_input(_ln)
        else:
            pattern, replacement = self._mk_pattern_with_layer_name_closure(_ln)

        # NOTE: use view_to_reshape to unify view/reshape to simplify
        # pattern and increase matching opportunities
        deffwd_and_view_to_reshape(*args, **kwargs) -> fx.GraphModule:
            gm = pm.fwd_only(*args, **kwargs)
            view_to_reshape(gm)
            return gm

        pm.register_replacement(
            pattern,
            replacement,
            self.get_inputs(),
            fwd_and_view_to_reshape,
            pm_pass,
        )
```