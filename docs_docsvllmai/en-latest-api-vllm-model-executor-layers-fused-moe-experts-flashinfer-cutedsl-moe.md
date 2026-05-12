---
title: flashinfer_cutedsl_moe - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/flashinfer_cutedsl_moe/
source: sitemap
fetched_at: 2026-05-07T21:24:41.969105512-03:00
rendered_js: false
word_count: 0
summary: This document defines a Python class for implementing NvFP4-quantized Mixture-of-Experts (MoE) layers using the FlashInfer functional API and modular configuration framework.
tags:
    - flashinfer
    - mixture-of-experts
    - nvfp4
    - quantization
    - neural-networks
    - cuda-kernels
category: reference
---

```
classFlashInferCuteDSLExperts(mk.FusedMoEExpertsModular):
"""
    CuteDSL NvFP4 MoE experts using the FlashInfer functional API.

    Uses Standard activation format (non-batched). The kernel handles
    routing, expert computation, and reduction internally.
    Supports expert parallelism natively.
    """

    def__init__(
        self,
        moe_config: FusedMoEConfig,
        quant_config: FusedMoEQuantConfig,
    ):
        super().__init__(
            moe_config=moe_config,
            quant_config=quant_config,
        )
        assert quant_config.quant_dtype == "nvfp4", (
            "Only nvfp4 quantization is currently supported."
        )
        self.out_dtype = moe_config.in_dtype
        self.hidden_dim = moe_config.hidden_dim
        self.intermediate_size_per_partition = (
            moe_config.intermediate_size_per_partition
        )
        self.topk = moe_config.experts_per_token
        self.local_num_experts = moe_config.num_local_experts
        self.global_num_experts = moe_config.num_experts
        self.ep_rank = moe_config.moe_parallel_config.ep_rank
        self.local_expert_offset = self.ep_rank * self.local_num_experts

    defprocess_weights_after_loading(self, layer: torch.nn.Module) -> None:
        layer.w13_weight_scale_2.data.mul_(layer.w13_input_scale)
        layer.w2_weight_scale_2.data.mul_(layer.w2_input_scale)

    @staticmethod
    defactivation_format() -> mk.FusedMoEActivationFormat:
        return mk.FusedMoEActivationFormat.Standard

    @staticmethod
    def_supports_current_device() -> bool:
        p = current_platform
        return (
            p.is_cuda()
            and p.is_device_capability_family(100)
            and has_flashinfer_cutedsl_moe_nvfp4()
        )

    @staticmethod
    def_supports_no_act_and_mul() -> bool:
        return False

    @staticmethod
    def_supports_quant_scheme(
        weight_key: QuantKey | None,
        activation_key: QuantKey | None,
    ) -> bool:
        SUPPORTED_W_A = [
            (kNvfp4Static, kNvfp4Dynamic),
        ]
        return (weight_key, activation_key) in SUPPORTED_W_A

    @staticmethod
    def_supports_activation(activation: MoEActivation) -> bool:
        return activation == MoEActivation.SILU

    @staticmethod
    def_supports_parallel_config(
        moe_parallel_config: FusedMoEParallelConfig,
    ) -> bool:
        return True

    defsupports_expert_map(self) -> bool:
        return False

    deffinalize_weight_and_reduce_impl(self) -> mk.TopKWeightAndReduce:
        return TopKWeightAndReduceNoOP()

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
        workspace1 = (0,)
        workspace2 = (0,)
        # K is packed (K//2 for uint8), so output uses hidden_dim.
        assert self.hidden_dim == K * 2
        output = (M, self.hidden_dim)
        return (workspace1, workspace2, output)

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
        workspace13: torch.Tensor | None,
        workspace2: torch.Tensor | None,
        expert_tokens_meta: mk.ExpertTokensMetadata | None,
        apply_router_weight_on_input: bool | None,
    ):
        assert self.quant_dtype == "nvfp4"
        assert a1q_scale is not None
        assert self.w1_scale is not None
        assert self.w2_scale is not None

        # a1q_scale is (M, K//16) float8_e4m3fn from fp4_quantize.
        # The functional API expects x_sf with trailing dim: (M, K//16, 1).
        x_sf = a1q_scale.unsqueeze(-1)

        fromvllm.utils.flashinferimport _is_fi_autotuning, autotune

        with autotune(_is_fi_autotuning):
            flashinfer_cute_dsl_fused_moe_nvfp4(
                x=hidden_states,
                x_sf=x_sf,
                token_selected_experts=topk_ids.to(torch.int32),
                token_final_scales=topk_weights.float(),
                w1_weight=w1,
                w1_weight_sf=self.w1_scale,
                w1_alpha=self.g1_alphas,
                fc2_input_scale=self.a2_gscale,
                w2_weight=w2,
                w2_weight_sf=self.w2_scale,
                w2_alpha=self.g2_alphas,
                num_experts=self.global_num_experts,
                top_k=self.topk,
                num_local_experts=self.local_num_experts,
                local_expert_offset=self.local_expert_offset,
                moe_output=output,
            )
```