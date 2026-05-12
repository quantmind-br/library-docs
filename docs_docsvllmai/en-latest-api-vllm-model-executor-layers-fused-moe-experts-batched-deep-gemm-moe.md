---
title: batched_deep_gemm_moe - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/batched_deep_gemm_moe/
source: sitemap
fetched_at: 2026-05-07T21:24:37.088094755-03:00
rendered_js: false
word_count: 362
summary: This document defines the BatchedDeepGemmExperts class, which implements fused Mixture-of-Experts (MoE) operations using optimized DeepGemm kernels for FP8 quantization.
tags:
    - vllm
    - moe
    - deep-gemm
    - fp8-quantization
    - fused-kernel
    - gpu-acceleration
category: reference
---

## BatchedDeepGemmExperts [¶](#vllm.model_executor.layers.fused_moe.experts.batched_deep_gemm_moe.BatchedDeepGemmExperts "Permanent link")

Bases: `FusedMoEExpertsModular`

Source code in `vllm/model_executor/layers/fused_moe/experts/batched_deep_gemm_moe.py`

```
classBatchedDeepGemmExperts(mk.FusedMoEExpertsModular):
    def__init__(
        self,
        moe_config: FusedMoEConfig,
        quant_config: FusedMoEQuantConfig,
        max_num_tokens: int,
        num_dispatchers: int,
    ):
"""
        max_num_tokens: Maximum number of tokens from a DP Rank
        num_dispatchers: The number of DP dispatchers.
        quant_config: Quantization configuration
        """
        super().__init__(
            moe_config=moe_config,
            quant_config=quant_config,
            max_num_tokens=max_num_tokens,
            num_dispatchers=num_dispatchers,
        )
        assert self.block_shape == get_mk_alignment_for_contiguous_layout()
        assert self.quant_config.use_fp8_w8a8

    @staticmethod
    defactivation_format() -> mk.FusedMoEActivationFormat:
        return mk.FusedMoEActivationFormat.BatchedExperts

    @staticmethod
    def_supports_current_device() -> bool:
        return is_deep_gemm_supported()

    @staticmethod
    def_supports_no_act_and_mul() -> bool:
        return False

    @staticmethod
    def_supports_quant_scheme(
        weight_key: QuantKey | None,
        activation_key: QuantKey | None,
    ) -> bool:
        SUPPORTED_W_A = [(kFp8Static128BlockSym, kFp8Dynamic128Sym)]
        return (weight_key, activation_key) in SUPPORTED_W_A

    @staticmethod
    def_supports_activation(activation: MoEActivation) -> bool:
        return activation == MoEActivation.SILU

    @staticmethod
    def_supports_parallel_config(moe_parallel_config: FusedMoEParallelConfig) -> bool:
        return True

    defsupports_expert_map(self) -> bool:
        return False

    defsupports_packed_ue8m0_act_scales(self) -> bool:
"""
        DeepGemm supports packed ue8m0 activation scales format in devices == sm100
        """
        return (
            is_deep_gemm_e8m0_used()
            and current_platform.is_device_capability_family(100)
        )

    deffinalize_weight_and_reduce_impl(self) -> mk.TopKWeightAndReduce:
        # Let PrepareAndFinalize::finalize() decide the impl.
        return TopKWeightAndReduceDelegate()

    defworkspace_shapes(
        self,
        M: int,
        N: int,
        K: int,
        topk: int,
        global_num_experts: int,
        local_num_experts: int,
        expert_tokens_meta: mk.ExpertTokensMetadata | None,
        activation: MoEActivation,
    ) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
        # FIXME (varun): We should be able to dispatch only from the leader
        # DP ranks in the case of TP > 1. At the moment, all the Ranks
        # end up sending their tokens. This needs to be fixed.
        assert self.num_dispatchers is not None
        assert self.max_num_tokens is not None
        num_dispatchers = self.num_dispatchers
        num_experts = local_num_experts
        max_num_tokens = M if self.max_num_tokens is None else self.max_num_tokens
        activation_out_dim = self.adjust_N_for_activation(N, activation)
        workspace13 = (num_experts, max_num_tokens * num_dispatchers, max(K, N))
        workspace2 = (num_experts, max_num_tokens * num_dispatchers, activation_out_dim)
        output = (num_experts, max_num_tokens * num_dispatchers, K)
        return (workspace13, workspace2, output)

    defestimate_expected_m(
        self, global_num_experts: int, max_tokens_per_expert: int, topk: int
    ) -> int:
        dp_meta = (
            get_forward_context().dp_metadata
            if is_forward_context_available()
            else None
        )
        if dp_meta is None:
            logger.warning_once(
                "DPMetadata unavailable. Defaulting expected_m to "
                f"{max_tokens_per_expert}.",
            )
            return max_tokens_per_expert

        total_num_tokens = dp_meta.num_tokens_across_dp_cpu.sum().item()
        total_num_tokens_replicated = total_num_tokens * topk

        # Assume even load balancing
        assert global_num_experts != 0
        estimate = round_up(int(total_num_tokens_replicated // global_num_experts), 16)
        # clamp estimate
        estimate = max(estimate, 16)
        estimate = min(max_tokens_per_expert, estimate)
        return estimate

    defapply(
        self,
        output: torch.Tensor,
        hidden_states: torch.Tensor,
        w1: torch.Tensor,
        w2: torch.Tensor,
        topk_weights: torch.Tensor,
        topk_ids: torch.Tensor,
        activation: MoEActivation,
        global_num_experts: int,
        expert_map: torch.Tensor | None,
        a1q_scale: torch.Tensor | None,
        a2_scale: torch.Tensor | None,
        workspace13: torch.Tensor,
        workspace2: torch.Tensor,
        expert_tokens_meta: mk.ExpertTokensMetadata | None,
        apply_router_weight_on_input: bool,
    ):
        assert expert_tokens_meta is not None
        expert_num_tokens = expert_tokens_meta.expert_num_tokens

        assert hidden_states.ndim == 3
        assert self.block_shape is not None

        a1q = hidden_states
        _, N, K = w1.size()

        assert w2.size(1) == K

        E, max_num_tokens, N, K, _ = self.moe_problem_size(
            hidden_states, w1, w2, topk_ids
        )

        workspace1 = _resize_cache(workspace13, (E, max_num_tokens, N))

        expected_m = self.estimate_expected_m(
            global_num_experts=global_num_experts,
            max_tokens_per_expert=max_num_tokens,
            topk=topk_ids.size(-1),
        )

        fp8_m_grouped_gemm_nt_masked(
            (a1q, a1q_scale),
            (w1, self.w1_scale),
            workspace1,
            expert_num_tokens,
            expected_m,
        )

        quant_scale_fmt = DeepGemmQuantScaleFMT.from_oracle()
        a2q, a2q_scale = persistent_masked_m_silu_mul_quant(
            workspace1,
            expert_num_tokens,
            quant_scale_fmt=quant_scale_fmt,
        )

        fp8_m_grouped_gemm_nt_masked(
            (a2q, a2q_scale),
            (w2, self.w2_scale),
            output,
            expert_num_tokens,
            expected_m,
        )
```

### \_\_init\__ [¶](#vllm.model_executor.layers.fused_moe.experts.batched_deep_gemm_moe.BatchedDeepGemmExperts.__init__ "Permanent link")

max\_num\_tokens: Maximum number of tokens from a DP Rank num\_dispatchers: The number of DP dispatchers. quant\_config: Quantization configuration

Source code in `vllm/model_executor/layers/fused_moe/experts/batched_deep_gemm_moe.py`

```
def__init__(
    self,
    moe_config: FusedMoEConfig,
    quant_config: FusedMoEQuantConfig,
    max_num_tokens: int,
    num_dispatchers: int,
):
"""
    max_num_tokens: Maximum number of tokens from a DP Rank
    num_dispatchers: The number of DP dispatchers.
    quant_config: Quantization configuration
    """
    super().__init__(
        moe_config=moe_config,
        quant_config=quant_config,
        max_num_tokens=max_num_tokens,
        num_dispatchers=num_dispatchers,
    )
    assert self.block_shape == get_mk_alignment_for_contiguous_layout()
    assert self.quant_config.use_fp8_w8a8
```

### supports\_packed\_ue8m0\_act\_scales [¶](#vllm.model_executor.layers.fused_moe.experts.batched_deep_gemm_moe.BatchedDeepGemmExperts.supports_packed_ue8m0_act_scales "Permanent link")

```
supports_packed_ue8m0_act_scales() -> bool
```

DeepGemm supports packed ue8m0 activation scales format in devices == sm100

Source code in `vllm/model_executor/layers/fused_moe/experts/batched_deep_gemm_moe.py`

```
defsupports_packed_ue8m0_act_scales(self) -> bool:
"""
    DeepGemm supports packed ue8m0 activation scales format in devices == sm100
    """
    return (
        is_deep_gemm_e8m0_used()
        and current_platform.is_device_capability_family(100)
    )
```

## persistent\_masked\_m\_silu\_mul\_quant [¶](#vllm.model_executor.layers.fused_moe.experts.batched_deep_gemm_moe.persistent_masked_m_silu_mul_quant "Permanent link")

Quantize silu(y\[..., :H]) * y\[..., H:] to FP8 with group per-token scales y has shape (E, T, 2\*H). The first half of the last dimension is silu-activated, multiplied by the second half, then quantized into FP8. We launch a fixed grid of threads to accommodate CUDA graphs. Let `P2` be a parallelization factor for persistent\_masked\_m\_silu\_mul\_quant over the hidden dimension.

Let `expert_offsets = [0] + [num_tokens.cumsum()]` and `total_tokens = expert_offsets[-1]`. persistent\_masked\_m\_silu\_mul\_quant launches `total_tokens x P2` number of thread blocks. Each thread block contains `NUM_WARPS` warps.

Every thread block needs to find it's corresponding expert by warp-parallel scanning over the `expert_offsets` array.

The i-th warp in the first thread block processes `[i * warp_chunk_size, (i + 1) * warp_chunk_size]` groups sequentially, where `warp_chunk_size = ((H / GROUP_SIZE) / P2) / NUM_WARPS`, pipelining loads and computes.

The shared memory layout for 4 warps with a 2-stage pipeline for SiLU V2 can is visualized like so:

┌─────┬───┬─────┬───┬─────┬───┬─────┬───┬─────┬───┬─────┬───┬─────┬───┬─────┬───┐ │gate0│up0│gate1│up1│gate2│up2│gate3│up3│gate0│up0│gate1│up1│gate2│up2│gate3│up3│ └─────┴───┴─────┴───┴─────┴───┴─────┴───┴─────┴───┴─────┴───┴─────┴───┴─────┴───┘

with the main difference between V1 and V2 being the global load stride between warps, and between half-warps. Regarding the latter stride, we assign the first half warp of every warp for `gate` loads and the second half-warp to `up` loads.

Returns `(y_q, y_s)` where * `y_q`: FP8 tensor, shape (E, T, H), same layout as y\[..., :H] * `y_s` depends on quant\_scale\_fmt, - quant\_scale\_fmt == FLOAT32, `y_s`: FP32 tensor, shape (E, T, H // group\_size), strides (T*G, 1, T) - quant\_scale\_fmt == E8M0, `y_s`: Int32 tensor, shape (E, T, H // group\_size // 4), strides (T*G, 1, T) - quant\_scale\_fmt == E8M0\_FLOAT32\_SPARSE `y_s`: FP32 tensor, shape (E, T, H // group\_size), strides (T\*G, 1, T) Let NUM\_WARPS be the number of warps in a single thread block and `GROUP_SIZE = 128` be the size of the quantization group.

Source code in `vllm/model_executor/layers/fused_moe/experts/batched_deep_gemm_moe.py`

```
defpersistent_masked_m_silu_mul_quant(
    y: torch.Tensor,  # (E, T, 2*H)
    tokens_per_expert: torch.Tensor,  # (E,) number of valid tokens per expert
    num_parallel_tokens=16,
    group_size: int = 128,
    quant_scale_fmt: DeepGemmQuantScaleFMT = DeepGemmQuantScaleFMT.FLOAT32,
) -> tuple[torch.Tensor, torch.Tensor]:
"""Quantize silu(y[..., :H]) * y[..., H:] to FP8 with group per-token scales
    y has shape (E, T, 2*H). The first half of the last dimension is
    silu-activated, multiplied by the second half, then quantized into FP8.
    We launch a fixed grid of threads to accommodate CUDA graphs. Let `P2`
    be a parallelization factor for persistent_masked_m_silu_mul_quant over the
    hidden dimension.

    Let `expert_offsets = [0] + [num_tokens.cumsum()]` and
    `total_tokens = expert_offsets[-1]`.
    persistent_masked_m_silu_mul_quant launches `total_tokens x P2` number of
    thread blocks. Each thread block contains `NUM_WARPS` warps.

    Every thread block needs to find it's corresponding expert by warp-parallel scanning
    over the `expert_offsets` array.

    The i-th warp in the first thread block processes
    `[i * warp_chunk_size, (i + 1) * warp_chunk_size]` groups
    sequentially, where `warp_chunk_size = ((H / GROUP_SIZE) / P2) / NUM_WARPS`,
    pipelining loads and computes.

    The shared memory layout for 4 warps with a 2-stage pipeline for SiLU V2
    can is visualized like so:

                         stage0                              stage1
    ┌─────┬───┬─────┬───┬─────┬───┬─────┬───┬─────┬───┬─────┬───┬─────┬───┬─────┬───┐
    │gate0│up0│gate1│up1│gate2│up2│gate3│up3│gate0│up0│gate1│up1│gate2│up2│gate3│up3│
    └─────┴───┴─────┴───┴─────┴───┴─────┴───┴─────┴───┴─────┴───┴─────┴───┴─────┴───┘

    with the main difference between V1 and V2 being the global load
    stride between warps, and between half-warps. Regarding the latter stride,
    we assign the first half warp of every warp for `gate` loads and the second
    half-warp to `up` loads.

    Returns `(y_q, y_s)` where
    * `y_q`: FP8 tensor, shape (E, T, H), same layout as y[..., :H]
    * `y_s` depends on quant_scale_fmt,
      - quant_scale_fmt == FLOAT32,
         `y_s`: FP32 tensor, shape (E, T, H // group_size), strides (T*G, 1, T)
      - quant_scale_fmt == E8M0,
         `y_s`: Int32 tensor, shape (E, T, H // group_size // 4), strides (T*G, 1, T)
      - quant_scale_fmt == E8M0_FLOAT32_SPARSE
         `y_s`: FP32 tensor, shape (E, T, H // group_size), strides (T*G, 1, T)
    Let NUM_WARPS be the number of warps in a single thread block and
    `GROUP_SIZE = 128` be the size of the quantization group.
    """
    assert y.ndim == 3, "y must be (E, T, 2*H)"
    E, T, H2 = y.shape
    assert H2 % 2 == 0, "last dim of y must be even (2*H)"
    H = H2 // 2
    G = (H + group_size - 1) // group_size
    assert H % 8 == 0, "H must be divisible by 8"
    assert group_size == 128, "H must be divisible by 8"
    assert tokens_per_expert.ndim == 1 and tokens_per_expert.shape[0] == E

    tokens_per_expert = tokens_per_expert.to(device=y.device, dtype=torch.int32)

    fp8_dtype = current_platform.fp8_dtype()
    y_q = torch.empty((E, T, H), dtype=fp8_dtype, device=y.device)

    ys_shape, ys_strides, ys_dtype = scales_shape_stride_dtype(E, T, G, quant_scale_fmt)
    y_s = torch.empty_strided(
        ys_shape,
        ys_strides,
        dtype=ys_dtype,
        device=y.device,
    )

    ceil_ue8m0 = quant_scale_fmt in [
        DeepGemmQuantScaleFMT.FLOAT32_CEIL_UE8M0,
        DeepGemmQuantScaleFMT.UE8M0,
    ]

    device_capability = current_platform.get_device_capability(device_id=y.device.index)
    assert device_capability is not None
    cuda_arch = device_capability.to_int()

    if current_platform.is_cuda() and cuda_arch >= 80:
        torch.ops._C.persistent_masked_m_silu_mul_quant(
            y, tokens_per_expert, y_q, y_s, ceil_ue8m0
        )
    else:
        # Triton fallback for ROCm -- the C++ kernel is guarded by
        # #ifndef USE_ROCM in activation_kernels.cu.
        # https://github.com/ROCm/aiter/issues/2420
        stride_cnt_e = tokens_per_expert.stride()[0]

        # Static grid over experts and H-groups.
        # A loop inside the kernel handles the token dim
        grid = (E * G,)
        # strides (elements)
        stride_i_e, stride_i_t, stride_i_h = y.stride()
        stride_yq_e, stride_yq_t, stride_yq_h = y_q.stride()

        fp8_min, fp8_max = get_fp8_min_max()
        eps: float = 1e-10
        assert y_s.dtype == torch.float32, (
            "_silu_mul_fp8_quant_deep_gemm Triton fallback does not "
            f"support {y_s.dtype} scales. Only torch.float32 supported."
        )
        _silu_mul_fp8_quant_deep_gemm[grid](
            y,
            y_q,
            y_s,
            tokens_per_expert,
            H,
            group_size,
            stride_i_e,
            stride_i_t,
            stride_i_h,
            stride_yq_e,
            stride_yq_t,
            stride_yq_h,
            ys_strides[0],
            ys_strides[1],
            ys_strides[2],
            stride_cnt_e,
            eps,
            fp8_min,
            fp8_max,
            ceil_ue8m0,
            BLOCK=group_size,
            NUM_STAGES=4,
            num_warps=1,
        )

    return y_q, y_s
```