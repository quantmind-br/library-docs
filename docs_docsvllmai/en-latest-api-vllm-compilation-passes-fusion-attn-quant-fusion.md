---
title: attn_quant_fusion - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/fusion/attn_quant_fusion/
source: sitemap
fetched_at: 2026-05-07T21:16:24.039283833-03:00
rendered_js: false
word_count: 5
summary: This document defines a graph pattern replacement for optimizing attention operations by fusing Nvfp4 quantization directly into the attention kernel.
tags:
    - vllm
    - graph-optimization
    - attention-fusion
    - quantization
    - pytorch
    - nvfp4
category: concept
---

```
classAttnNvfp4QuantPattern(
    VllmPatternReplacement[..., tuple[torch.Tensor, torch.Tensor]]
):
"""
    Fusion for Attention+Nvfp4Quant.

    Only triggers when the attention implementation returns True in
    `fused_output_quant_supported()`. If the pattern is found, the
    Nvfp4Quant op will be removed from the graph, and its scale
    will be passed into Attention op as the `output_scale` argument.
    """

    def__init__(self, layer: Attention, dtype: torch.dtype):
        self._layer_name = layer.layer_name
        self._num_heads = layer.num_heads
        self._head_size = layer.head_size
        self._dtype = dtype
        self._QUANT_OP = QUANT_OPS[kNvfp4Dynamic]

    @property
    defpattern(self) -> Callable[..., tuple[torch.Tensor, torch.Tensor]]:
        _ln = _encode_layer_name(self._layer_name)

        if _USE_LAYERNAME:

            def_pattern_with_ln(  # type: ignore[misc]
                q,
                k,
                v,
                output_attn,
                output_quant,
                output_scale,
                input_scale,
                kv_cache_dummy_dep,
                layer_name,
            ):
                at1 = auto_functionalized(
                    ATTN_OP,
                    query=q,
                    key=k,
                    value=v,
                    output=output_attn,
                    layer_name=layer_name,
                    output_scale=None,
                    output_block_scale=None,
                    kv_cache_dummy_dep=kv_cache_dummy_dep,
                )
                attn_out_view = RESHAPE_OP(
                    at1[1], [q.shape[0], self._num_heads * self._head_size]
                )
                at2 = auto_functionalized(
                    self._QUANT_OP,
                    input=attn_out_view,
                    input_scale=input_scale,
                    is_sf_swizzled_layout=True,
                    output=output_quant,
                    output_scale=output_scale,
                )
                return at2[1], torch.ops.aten.view.dtype(at2[2], FP8_DTYPE)

            return _pattern_with_ln

        def_pattern(
            q,
            k,
            v,
            output_attn,
            output_quant,
            output_scale,
            input_scale,
            kv_cache_dummy_dep,
        ):
            at1 = auto_functionalized(
                ATTN_OP,
                query=q,
                key=k,
                value=v,
                output=output_attn,
                layer_name=_ln,
                output_scale=None,
                output_block_scale=None,
                kv_cache_dummy_dep=kv_cache_dummy_dep,
            )
            attn_out_view = RESHAPE_OP(
                at1[1], [q.shape[0], self._num_heads * self._head_size]
            )
            at2 = auto_functionalized(
                self._QUANT_OP,
                input=attn_out_view,
                input_scale=input_scale,
                is_sf_swizzled_layout=True,
                output=output_quant,
                output_scale=output_scale,
            )
            return at2[1], torch.ops.aten.view.dtype(at2[2], FP8_DTYPE)

        return _pattern

    @property
    defreplacement(self) -> Callable[..., tuple[torch.Tensor, torch.Tensor]]:
        _ln = _encode_layer_name(self._layer_name)

        if _USE_LAYERNAME:

            def_replacement_with_ln(  # type: ignore[misc]
                q,
                k,
                v,
                output_attn,
                _output_quant,
                output_scale,
                input_scale,
                kv_cache_dummy_dep,
                layer_name,
            ):
                output_attn = torch.empty(
                    [q.shape[0], self._num_heads, self._head_size // 2],
                    dtype=FP4_DTYPE,
                    device=q.device,
                )
                osv = torch.ops.aten.view.dtype(output_scale, FP8_DTYPE)
                at2 = auto_functionalized(
                    ATTN_OP,
                    query=q,
                    key=k,
                    value=v,
                    output=output_attn,
                    layer_name=layer_name,
                    output_scale=input_scale,
                    output_block_scale=osv,
                    kv_cache_dummy_dep=kv_cache_dummy_dep,
                )
                return RESHAPE_OP(
                    at2[1], [-1, self._num_heads * self._head_size // 2]
                ), at2[2]

            return _replacement_with_ln

        def_replacement(
            q,
            k,
            v,
            output_attn,
            _output_quant,
            output_scale,
            input_scale,
            kv_cache_dummy_dep,
        ):
            output_attn = torch.empty(
                [q.shape[0], self._num_heads, self._head_size // 2],
                dtype=FP4_DTYPE,
                device=q.device,
            )
            osv = torch.ops.aten.view.dtype(output_scale, FP8_DTYPE)
            at2 = auto_functionalized(
                ATTN_OP,
                query=q,
                key=k,
                value=v,
                output=output_attn,
                layer_name=_ln,
                output_scale=input_scale,
                output_block_scale=osv,
                kv_cache_dummy_dep=kv_cache_dummy_dep,
            )
            return RESHAPE_OP(
                at2[1], [-1, self._num_heads * self._head_size // 2]
            ), at2[2]

        return _replacement

    defget_inputs(self):
        dtype = self._dtype
        num_heads = self._num_heads
        head_size = self._head_size
        inputs: list = [
            self.empty_bf16(5, num_heads, head_size),  # q
            self.empty_bf16(5, num_heads, head_size),  # k
            self.empty_bf16(5, num_heads, head_size),  # v
            self.empty_bf16(5, num_heads, head_size),  # output_attn
            self.empty(5, num_heads * head_size // 2, dtype=FP4_DTYPE),
            self.empty_i32(128, round_up(num_heads * head_size // 16, 4)),
            self.empty_fp32(1, 1),  # input_scale
            self.empty(0, dtype=dtype),  # kv_cache_dummy_dep
        ]
        if _USE_LAYERNAME:
            inputs.append(_encode_layer_name(self._layer_name))
        return inputs
```