---
title: fallback - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/fallback/
source: sitemap
fetched_at: 2026-05-07T21:24:50.876383911-03:00
rendered_js: false
word_count: 0
summary: This document defines an abstract base class for managing runtime dispatching between primary and fallback Mixture-of-Experts (MoE) implementations in a modular framework.
tags:
    - python
    - mixture-of-experts
    - model-architecture
    - runtime-dispatch
    - abstract-base-class
    - tensor-processing
category: reference
---

```
classFallbackExperts(mk.FusedMoEExpertsModular, ABC):
"""Base class for runtime dispatching of expert implementations."""

    def__init__(
        self,
        experts: mk.FusedMoEExpertsModular,
        fallback_experts: mk.FusedMoEExpertsModular,
    ):
        super().__init__(
            moe_config=experts.moe_config, quant_config=experts.quant_config
        )
        self.fallback_experts = fallback_experts
        self.experts = experts

    @staticmethod
    defget_clses() -> tuple[
        type[mk.FusedMoEExpertsModular],
        type[mk.FusedMoEExpertsModular],
    ]:
"""
        Get the cls for the experts and fallback experts.

        Subclasses should implement this method, so that
        we have a consistent way to call the _supports_*
        class methods below.
        """
        raise NotImplementedError(
            "Subclasses must return the cls for the experts and fallback experts."
        )

    @classmethod
    defactivation_format(
        cls: type["FallbackExperts"],
    ) -> mk.FusedMoEActivationFormat:
        experts_cls, fallback_cls = cls.get_clses()
        assert experts_cls.activation_format() == fallback_cls.activation_format()
        return experts_cls.activation_format()

    @classmethod
    def_supports_current_device(cls) -> bool:
        experts_cls, fallback_cls = cls.get_clses()
        return (
            experts_cls._supports_current_device()
            and fallback_cls._supports_current_device()
        )

    @classmethod
    def_supports_no_act_and_mul(cls) -> bool:
        experts_cls, fallback_cls = cls.get_clses()
        return (
            experts_cls._supports_no_act_and_mul()
            and fallback_cls._supports_no_act_and_mul()
        )

    @classmethod
    def_supports_quant_scheme(
        cls,
        weight_key: QuantKey | None,
        activation_key: QuantKey | None,
    ) -> bool:
        experts_cls, fallback_cls = cls.get_clses()
        return experts_cls._supports_quant_scheme(
            weight_key, activation_key
        ) and fallback_cls._supports_quant_scheme(weight_key, activation_key)

    @classmethod
    def_supports_activation(cls, activation: MoEActivation) -> bool:
        experts_cls, fallback_cls = cls.get_clses()
        return experts_cls._supports_activation(
            activation
        ) and fallback_cls._supports_activation(activation)

    @classmethod
    def_supports_parallel_config(
        cls, moe_parallel_config: FusedMoEParallelConfig
    ) -> bool:
        experts_cls, fallback_cls = cls.get_clses()
        return experts_cls._supports_parallel_config(
            moe_parallel_config
        ) and fallback_cls._supports_parallel_config(moe_parallel_config)

    defsupports_expert_map(self) -> bool:
        assert (
            self.experts.supports_expert_map()
            == self.fallback_experts.supports_expert_map()
        )
        return (
            self.experts.supports_expert_map()
            and self.fallback_experts.supports_expert_map()
        )

    deffinalize_weight_and_reduce_impl(self) -> mk.TopKWeightAndReduce:
        e_war = self.experts.finalize_weight_and_reduce_impl()
        fbe_war = self.fallback_experts.finalize_weight_and_reduce_impl()
        is_dge_war = e_war is not None
        is_fbe_war = fbe_war is not None

        if is_dge_war and is_fbe_war:
            assert e_war == fbe_war, (
                "Both implementations should agree on WeightAndReduce impls. "
                f"Got e_war: {e_war}, and fbe_war: {fbe_war}"
            )

        if e_war is not None:
            return e_war
        assert fbe_war is not None
        return fbe_war

    @abstractmethod
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
        raise NotImplementedError

    @abstractmethod
    def_select_experts_impl(
        self,
        hidden_states: torch.Tensor,
        w1: torch.Tensor,
        w2: torch.Tensor,
    ) -> mk.FusedMoEExpertsModular:
        raise NotImplementedError

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
        experts = self._select_experts_impl(hidden_states, w1, w2)
        experts.apply(
            output,
            hidden_states,
            w1,
            w2,
            topk_weights,
            topk_ids,
            activation,
            global_num_experts,
            expert_map,
            a1q_scale,
            a2_scale,
            workspace13,
            workspace2,
            expert_tokens_meta,
            apply_router_weight_on_input,
        )
```