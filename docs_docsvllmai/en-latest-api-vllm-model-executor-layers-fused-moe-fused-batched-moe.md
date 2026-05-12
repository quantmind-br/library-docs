---
title: fused_batched_moe - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/fused_batched_moe/
source: sitemap
fetched_at: 2026-05-07T21:24:53.614422911-03:00
rendered_js: false
word_count: 0
summary: Implements a Triton-based Mixture-of-Experts (MoE) class designed for batched token dispatching and kernel execution.
tags:
    - triton
    - mixture-of-experts
    - moe
    - deep-learning
    - tensor-parallelism
    - cuda-kernels
category: reference
---

```
classBatchedTritonExperts(mk.FusedMoEExpertsModular):
"""
    A Triton based MoE expert class that operates on expert batched format,
    i.e. E x max_num_tokens x K.  This is the format that the batched
    dispatch/combine kernels use.
    """

    def__init__(
        self,
        moe_config: FusedMoEConfig,
        quant_config: FusedMoEQuantConfig,
        max_num_tokens: int,
        num_dispatchers: int,
    ):
        super().__init__(
            moe_config=moe_config,
            quant_config=quant_config,
            max_num_tokens=max_num_tokens,
            num_dispatchers=num_dispatchers,
        )
        assert not self.quant_config.use_int8_w8a8, "NYI"
        assert not self.quant_config.use_int8_w8a16, "NYI"
        assert not self.quant_config.use_int4_w4a16, "NYI"
        assert self.quant_config.ocp_mx_scheme is None, "NYI"

    @staticmethod
    defactivation_format() -> mk.FusedMoEActivationFormat:
        return mk.FusedMoEActivationFormat.BatchedExperts

    @staticmethod
    def_supports_current_device() -> bool:
        return current_platform.is_cuda_alike()

    @staticmethod
    def_supports_no_act_and_mul() -> bool:
        return True

    @staticmethod
    def_supports_quant_scheme(
        weight_key: QuantKey | None,
        activation_key: QuantKey | None,
    ) -> bool:
        p = current_platform
        if p.is_rocm():
            fromvllm.platforms.rocmimport on_gfx9

            is_rocm_on_gfx9 = on_gfx9()
        else:
            is_rocm_on_gfx9 = False

        device_supports_fp8 = is_rocm_on_gfx9 or (
            p.is_cuda() and p.has_device_capability((8, 9))
        )

        supported: list[tuple[QuantKey | None, QuantKey | None]] = [(None, None)]
        if device_supports_fp8:
            supported += [
                (kFp8Static128BlockSym, kFp8Dynamic128Sym),
                (kFp8StaticChannelSym, kFp8DynamicTokenSym),
                (kFp8StaticTensorSym, kFp8DynamicTokenSym),
                (kFp8StaticTensorSym, kFp8StaticTensorSym),
                (kFp8StaticTensorSym, kFp8DynamicTensorSym),
            ]
        return (weight_key, activation_key) in supported

    @staticmethod
    def_supports_activation(activation: MoEActivation) -> bool:
        return activation in [
            MoEActivation.SILU,
            MoEActivation.GELU,
            MoEActivation.GELU_TANH,
            MoEActivation.SWIGLUOAI,
            MoEActivation.SILU_NO_MUL,
            MoEActivation.GELU_NO_MUL,
            MoEActivation.GELU_TANH_NO_MUL,
            MoEActivation.RELU2_NO_MUL,
        ]

    @staticmethod
    def_supports_parallel_config(moe_parallel_config: FusedMoEParallelConfig) -> bool:
        return True

    defsupports_expert_map(self) -> bool:
        return False

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
        assert self.num_dispatchers is not None
        assert self.max_num_tokens is not None
        num_dp = self.num_dispatchers
        num_experts = local_num_experts
        max_num_tokens = self.max_num_tokens
        activation_out_dim = self.adjust_N_for_activation(N, activation)
        workspace13 = (num_experts, max_num_tokens * num_dp, max(K, N))
        workspace2 = (num_experts, max_num_tokens * num_dp, activation_out_dim)
        output = (num_experts, max_num_tokens * num_dp, K)
        return (workspace13, workspace2, output)

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
        # Check constraints.
        if self.quant_config.use_int4_w4a16:
            assert hidden_states.size(-1) // 2 == w1.size(2), "Hidden size mismatch"
        else:
            assert hidden_states.size(-1) == w1.size(2), (
                f"Hidden size mismatch {hidden_states.size(-1)} != {w1.size(2)}"
            )

        assert hidden_states.is_contiguous(), "Hidden_states must be contiguous"
        assert w1.stride(-1) == 1, "Stride of last dimension must be 1"
        assert w2.stride(-1) == 1, "Stride of last dimension must be 1"
        assert hidden_states.dtype in [
            torch.float32,
            torch.float16,
            torch.bfloat16,
            torch.float8_e4m3fn,
            torch.float8_e4m3fnuz,
        ]
        assert expert_tokens_meta is not None

        expert_num_tokens = expert_tokens_meta.expert_num_tokens

        E, max_num_tokens, N, K, top_k_num = self.moe_problem_size(
            hidden_states, w1, w2, topk_ids
        )

        assert w1.size(0) == E
        assert w2.size(0) == E

        config_dtype = self.quant_config.config_name(hidden_states.dtype)

        config = try_get_optimal_moe_config(
            w1.size(),
            w2.size(),
            top_k_num,
            config_dtype,
            max_num_tokens,
            block_shape=self.block_shape,
        )

        if hidden_states.dtype == torch.bfloat16:
            compute_type = tl.bfloat16
        elif hidden_states.dtype == torch.float16:
            compute_type = tl.float16
        elif hidden_states.dtype == torch.float32:
            compute_type = tl.float32
        elif hidden_states.dtype == current_platform.fp8_dtype():
            compute_type = tl.bfloat16
        else:
            raise ValueError(f"Unsupported compute_type: {hidden_states.dtype}")

        # We can reuse the memory between these because by the time we need
        # cache3, we're done with cache1
        intermediate_cache1 = _resize_cache(workspace13, (E, max_num_tokens, N))
        activation_out_dim = self.adjust_N_for_activation(N, activation)
        intermediate_cache2 = _resize_cache(
            workspace2, (E, max_num_tokens, activation_out_dim)
        )

        # TODO(bnell): should this be done for any quantized type?
        if self.quant_config.use_fp8_w8a8:
            intermediate_cache1.fill_(0)

        a1q_scale = normalize_batched_scales_shape(a1q_scale, E)

        # MM1
        invoke_moe_batched_triton_kernel(
            A=hidden_states,
            B=w1,
            C=intermediate_cache1,
            expert_num_tokens=expert_num_tokens,
            compute_type=compute_type,
            A_scale=a1q_scale,
            B_scale=self.w1_scale,
            B_zp=self.w1_zp,
            use_fp8_w8a8=self.quant_config.use_fp8_w8a8,
            use_int8_w8a16=self.quant_config.use_int8_w8a16,
            use_int4_w4a16=self.quant_config.use_int4_w4a16,
            config=config,
            per_act_token_quant=self.per_act_token_quant,
            block_shape=self.block_shape,
        )

        intermediate_cache2.fill_(0)

        # TODO (bnell): use triton utility from batched deep gemm.
        self.activation(
            activation,
            intermediate_cache2.view(-1, activation_out_dim),
            intermediate_cache1.view(-1, N),
        )

        qintermediate_cache2, a2q_scale = batched_moe_kernel_quantize_input(
            intermediate_cache2,
            a2_scale,
            max_num_tokens,
            E,
            N,
            expert_num_tokens,
            self.quant_dtype,
            self.per_act_token_quant,
            self.block_shape,
        )

        invoke_moe_batched_triton_kernel(
            A=qintermediate_cache2,
            B=w2,
            C=output,
            expert_num_tokens=expert_num_tokens,
            compute_type=compute_type,
            A_scale=a2q_scale,
            B_scale=self.w2_scale,
            B_zp=self.w2_zp,
            use_fp8_w8a8=self.quant_config.use_fp8_w8a8,
            use_int8_w8a16=self.quant_config.use_int8_w8a16,
            use_int4_w4a16=self.quant_config.use_int4_w4a16,
            config=config,
            per_act_token_quant=self.per_act_token_quant,
            block_shape=self.block_shape,
        )
```