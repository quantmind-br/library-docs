---
title: trtllm_nvfp4_moe - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe/
source: sitemap
fetched_at: 2026-05-07T21:24:48.898653953-03:00
rendered_js: false
word_count: 130
summary: This document defines the TrtLlmNvFp4Experts base and modular classes, which implement NvFp4-quantized MoE kernels specifically for Blackwell-family GPUs in the vLLM framework.
tags:
    - vllm
    - moe
    - nvfp4
    - quantization
    - blackwell-gpu
    - kernel-optimization
    - fused-moe
category: reference
---

## TrtLlmNvFp4ExpertsBase [¶](#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsBase "Permanent link")

NvFp4 TRTLLM-Gen MoE kernels. Supports modular and monolithic interface.

Source code in `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`

```
classTrtLlmNvFp4ExpertsBase:
"""
    NvFp4 TRTLLM-Gen MoE kernels. Supports modular and monolithic interface.
    """

    def__init__(
        self,
        moe_config: FusedMoEConfig,
        quant_config: FusedMoEQuantConfig,
    ):
        self.moe_config = moe_config
        self.quant_config = quant_config

        self.routing_method_type = self.moe_config.routing_method
        self.topk = moe_config.experts_per_token
        self.intermediate_size_per_partition = (
            moe_config.intermediate_size_per_partition
        )
        self.hidden_dim = moe_config.hidden_dim
        self.hidden_dim_unpadded = (
            moe_config.hidden_dim_unpadded or moe_config.hidden_dim
        )
        self.local_num_experts = moe_config.num_local_experts
        self.ep_rank = moe_config.moe_parallel_config.ep_rank

        assert self.quant_config.g1_alphas is not None
        assert self.quant_config.a2_gscale is not None
        if moe_config.is_act_and_mul:
            # g1_alpha_s = a13_scale * w13_scale_2
            # a2_gscale = (1 / a2_scale)
            # g1_scale_c = a13_scale * w13_scale_2 / a2_scale
            self.g1_scale_c = self.quant_config.g1_alphas * self.quant_config.a2_gscale
        else:
            self.g1_scale_c = self.quant_config.a2_gscale.clone()

    defprocess_weights_after_loading(self, layer: torch.nn.Module) -> None:
        layer.w13_weight_scale_2.data.mul_(layer.w13_input_scale)
        layer.w2_weight_scale_2.data.mul_(layer.w2_input_scale)
        # Recompute g1_scale_c since g1_alphas was just fused in-place.
        # Register as a layer parameter so EPLB rearranges it alongside
        # other expert weights.
        assert self.quant_config.g1_alphas is not None
        assert self.quant_config.a2_gscale is not None
        if self.moe_config.is_act_and_mul:
            g1_scale_c = self.quant_config.g1_alphas * self.quant_config.a2_gscale
        else:
            g1_scale_c = self.quant_config.a2_gscale.clone()
        layer.register_parameter(
            "g1_scale_c",
            torch.nn.Parameter(g1_scale_c, requires_grad=False),
        )
        self.g1_scale_c = layer.g1_scale_c

    @staticmethod
    def_supports_current_device() -> bool:
"""Supports only Blackwell-family GPUs."""
        p = current_platform
        return (
            p.is_cuda()
            and p.is_device_capability_family(100)
            and has_flashinfer_trtllm_fused_moe()
        )

    @staticmethod
    def_supports_no_act_and_mul() -> bool:
"""Supports non-gated MoE (i.e. Nemotron-Nano)."""
        return True

    @staticmethod
    def_supports_quant_scheme(
        weight_key: QuantKey | None,
        activation_key: QuantKey | None,
    ) -> bool:
"""Supports Nvfp4 quantization."""
        SUPPORTED_W_A = [
            (kNvfp4Static, kNvfp4Dynamic),
        ]
        return (weight_key, activation_key) in SUPPORTED_W_A

    @staticmethod
    def_supports_activation(activation: MoEActivation) -> bool:
"""Supports only SiLU, RELU^2 non-gated and GELU activation."""
        return activation in [
            MoEActivation.SILU,
            MoEActivation.RELU2_NO_MUL,
            MoEActivation.GELU,
        ]

    @staticmethod
    def_supports_shape(hidden_dim: int) -> bool:
        # Weights are zero-padded to 256-alignment at load time and the MoE
        # runner pads activations via _maybe_pad_hidden_states, so any
        # hidden_dim is accepted.
        # NOTE: non-256-aligned dims will trigger a warning log and may
        # cause performance degradation due to activation slicing.
        return True

    @staticmethod
    defactivation_format() -> mk.FusedMoEActivationFormat:
        return mk.FusedMoEActivationFormat.Standard

    defsupports_chunking(self) -> bool:
        return False

    defsupports_expert_map(self) -> bool:
        return False
```

### \_supports\_activation `staticmethod` [¶](#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsBase._supports_activation "Permanent link")

Supports only SiLU, RELU^2 non-gated and GELU activation.

Source code in `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`

```
@staticmethod
def_supports_activation(activation: MoEActivation) -> bool:
"""Supports only SiLU, RELU^2 non-gated and GELU activation."""
    return activation in [
        MoEActivation.SILU,
        MoEActivation.RELU2_NO_MUL,
        MoEActivation.GELU,
    ]
```

### \_supports\_current\_device `staticmethod` [¶](#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsBase._supports_current_device "Permanent link")

```
_supports_current_device() -> bool
```

Supports only Blackwell-family GPUs.

Source code in `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`

```
@staticmethod
def_supports_current_device() -> bool:
"""Supports only Blackwell-family GPUs."""
    p = current_platform
    return (
        p.is_cuda()
        and p.is_device_capability_family(100)
        and has_flashinfer_trtllm_fused_moe()
    )
```

### \_supports\_no\_act\_and\_mul `staticmethod` [¶](#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsBase._supports_no_act_and_mul "Permanent link")

```
_supports_no_act_and_mul() -> bool
```

Supports non-gated MoE (i.e. Nemotron-Nano).

Source code in `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`

```
@staticmethod
def_supports_no_act_and_mul() -> bool:
"""Supports non-gated MoE (i.e. Nemotron-Nano)."""
    return True
```

### \_supports\_quant\_scheme `staticmethod` [¶](#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsBase._supports_quant_scheme "Permanent link")

Supports Nvfp4 quantization.

Source code in `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`

```
@staticmethod
def_supports_quant_scheme(
    weight_key: QuantKey | None,
    activation_key: QuantKey | None,
) -> bool:
"""Supports Nvfp4 quantization."""
    SUPPORTED_W_A = [
        (kNvfp4Static, kNvfp4Dynamic),
    ]
    return (weight_key, activation_key) in SUPPORTED_W_A
```

## TrtLlmNvFp4ExpertsModular [¶](#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsModular "Permanent link")

Bases: `TrtLlmNvFp4ExpertsBase`, `FusedMoEExpertsModular`

Modular version of the implementation (just the experts).

Source code in `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`

```
classTrtLlmNvFp4ExpertsModular(TrtLlmNvFp4ExpertsBase, mk.FusedMoEExpertsModular):
"""
    Modular version of the implementation (just the experts).
    """

    @staticmethod
    def_supports_parallel_config(moe_parallel_config: FusedMoEParallelConfig) -> bool:
"""The modular implementation supports all parallel configs."""
        return True

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
        # The workspaces for this implementation are managed by flashinfer.
        workspace1 = (0,)
        workspace2 = (0,)

        # Hidden states are Nvfp4, packed into int8 dtype, so we
        # need to multiply K by 2 to get the output shape right.
        assert self.hidden_dim == K * 2
        output = (M, self.hidden_dim)

        return (workspace1, workspace2, output)

    deffinalize_weight_and_reduce_impl(self) -> mk.TopKWeightAndReduce:
        return TopKWeightAndReduceNoOP()

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
        importflashinfer

        assert self._supports_activation(activation)
        assert a1q_scale is not None
        assert self.quant_config.w1_scale is not None
        assert self.quant_config.w2_scale is not None

        # Pack topk ids and weights into format expected by the kernel.
        packed_tensor = trtllm_moe_pack_topk_ids_weights(topk_ids, topk_weights)

        # Invoke kernel.
        flashinfer.fused_moe.trtllm_fp4_block_scale_routed_moe(
            topk_ids=packed_tensor,
            routing_bias=None,
            hidden_states=hidden_states,
            hidden_states_scale=a1q_scale.view(torch.float8_e4m3fn).reshape(
                *hidden_states.shape[:-1], -1
            ),
            gemm1_weights=w1,
            gemm1_weights_scale=self.quant_config.w1_scale.view(torch.float8_e4m3fn),
            gemm1_bias=None,
            gemm1_alpha=None,
            gemm1_beta=None,
            gemm1_clamp_limit=None,
            gemm2_weights=w2,
            gemm2_weights_scale=self.quant_config.w2_scale.view(torch.float8_e4m3fn),
            gemm2_bias=None,
            output1_scale_scalar=self.g1_scale_c,
            output1_scale_gate_scalar=self.quant_config.g1_alphas,
            output2_scale_scalar=self.quant_config.g2_alphas,
            num_experts=global_num_experts,
            top_k=self.topk,
            n_group=0,
            topk_group=0,
            intermediate_size=self.intermediate_size_per_partition,
            local_expert_offset=self.ep_rank * self.local_num_experts,
            local_num_experts=self.local_num_experts,
            routed_scaling_factor=None,
            routing_method_type=1,  # not used
            do_finalize=True,
            activation_type=activation_to_flashinfer_int(activation),
            output=output,
        )
```

### \_supports\_parallel\_config `staticmethod` [¶](#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsModular._supports_parallel_config "Permanent link")

The modular implementation supports all parallel configs.

Source code in `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`

```
@staticmethod
def_supports_parallel_config(moe_parallel_config: FusedMoEParallelConfig) -> bool:
"""The modular implementation supports all parallel configs."""
    return True
```

## TrtLlmNvFp4ExpertsMonolithic [¶](#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsMonolithic "Permanent link")

Bases: `TrtLlmNvFp4ExpertsBase`, `FusedMoEExpertsMonolithic`

Monolithic version of the kernel (router + experts).

Source code in `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`

```
classTrtLlmNvFp4ExpertsMonolithic(
    TrtLlmNvFp4ExpertsBase, mk.FusedMoEExpertsMonolithic
):
"""
    Monolithic version of the kernel (router + experts).
    """

    @staticmethod
    def_supports_parallel_config(moe_parallel_config: FusedMoEParallelConfig) -> bool:
"""The modular implementation should be used for the Dp/Ep or EPLB case."""
        return (
            not moe_parallel_config.use_all2all_kernels
            and not moe_parallel_config.enable_eplb
        )

    @staticmethod
    def_supports_routing_method(
        routing_method_type: RoutingMethodType,
        weight_key: QuantKey | None,
        activation_key: QuantKey | None,
    ) -> bool:
        # NOTE(rob): this is a conservative list.
        return routing_method_type in [
            RoutingMethodType.DeepSeekV3,
            RoutingMethodType.Renormalize,
            RoutingMethodType.RenormalizeNaive,
            RoutingMethodType.Llama4,
            RoutingMethodType.SigmoidRenorm,
            RoutingMethodType.MiniMax2,
            RoutingMethodType.Simulated,
            RoutingMethodType.SigmoidRenorm,
        ]

    @staticmethod
    def_supports_router_logits_dtype(
        router_logits_dtype: torch.dtype | None,
        routing_method: RoutingMethodType,
    ) -> bool:
        return True

    defapply(
        self,
        hidden_states: torch.Tensor,
        w1: torch.Tensor,
        w2: torch.Tensor,
        router_logits: torch.Tensor,
        activation: MoEActivation,
        global_num_experts: int,
        expert_map: torch.Tensor | None,
        a1q_scale: torch.Tensor | None,
        apply_router_weight_on_input: bool,
        # grouped topk + fused topk bias parameters
        num_expert_group: int | None = None,
        e_score_correction_bias: torch.Tensor | None = None,
        routed_scaling_factor: float | None = None,
        topk_group: int | None = None,
    ) -> torch.Tensor:
        importflashinfer

        assert self._supports_activation(activation)
        assert a1q_scale is not None
        assert self.quant_config.w1_scale is not None
        assert self.quant_config.w2_scale is not None
        assert (
            apply_router_weight_on_input
            and self.routing_method_type == RoutingMethodType.Llama4
        ) or (
            not apply_router_weight_on_input
            and self.routing_method_type != RoutingMethodType.Llama4
        )

        # Currently FI requires bfloat16 routing bias.
        # https://github.com/flashinfer-ai/flashinfer/issues/2909
        if e_score_correction_bias is not None:
            e_score_correction_bias = e_score_correction_bias.to(torch.bfloat16)

        # Invoke kernel.
        # NOTE: Activation padding and output
        # truncation are handled by the MoE runner's
        return flashinfer.fused_moe.trtllm_fp4_block_scale_moe(
            routing_logits=router_logits,
            routing_bias=e_score_correction_bias,
            hidden_states=hidden_states,
            hidden_states_scale=a1q_scale.view(torch.float8_e4m3fn).reshape(
                *hidden_states.shape[:-1], -1
            ),
            gemm1_weights=w1,
            gemm1_weights_scale=self.quant_config.w1_scale.view(torch.float8_e4m3fn),
            gemm1_bias=None,
            gemm1_alpha=None,
            gemm1_beta=None,
            gemm1_clamp_limit=None,
            gemm2_weights=w2,
            gemm2_weights_scale=self.quant_config.w2_scale.view(torch.float8_e4m3fn),
            gemm2_bias=None,
            output1_scale_scalar=self.g1_scale_c,
            output1_scale_gate_scalar=self.quant_config.g1_alphas,
            output2_scale_scalar=self.quant_config.g2_alphas,
            num_experts=global_num_experts,
            top_k=self.topk,
            n_group=(num_expert_group or 0),
            topk_group=(topk_group or 0),
            intermediate_size=self.intermediate_size_per_partition,
            local_expert_offset=self.ep_rank * self.local_num_experts,
            local_num_experts=self.local_num_experts,
            routed_scaling_factor=routed_scaling_factor,
            routing_method_type=self.routing_method_type,
            do_finalize=True,
            activation_type=activation_to_flashinfer_int(activation),
        )[0]
```

### \_supports\_parallel\_config `staticmethod` [¶](#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsMonolithic._supports_parallel_config "Permanent link")

The modular implementation should be used for the Dp/Ep or EPLB case.

Source code in `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`

```
@staticmethod
def_supports_parallel_config(moe_parallel_config: FusedMoEParallelConfig) -> bool:
"""The modular implementation should be used for the Dp/Ep or EPLB case."""
    return (
        not moe_parallel_config.use_all2all_kernels
        and not moe_parallel_config.enable_eplb
    )
```