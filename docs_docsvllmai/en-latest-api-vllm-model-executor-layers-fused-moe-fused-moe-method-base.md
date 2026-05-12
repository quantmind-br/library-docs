---
title: fused_moe_method_base - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/fused_moe_method_base/
source: sitemap
fetched_at: 2026-05-07T21:24:57.088148882-03:00
rendered_js: false
word_count: 0
summary: Defines an abstract base class for implementing fused mixture-of-experts (MoE) quantization methods, providing interfaces for weight creation, layer configuration, and execution kernels.
tags:
    - mixture-of-experts
    - quantization
    - deep-learning
    - neural-networks
    - fused-kernels
    - model-optimization
category: reference
---

```
classFusedMoEMethodBase(QuantizeMethodBase):
    def__init__(self, moe: FusedMoEConfig):
        super().__init__()
        self.moe: FusedMoEConfig = moe
        self.moe_quant_config: FusedMoEQuantConfig | None = None
        self.moe_kernel: mk.FusedMoEKernel | None = None

    @property
    defsupports_internal_mk(self) -> bool:
        # NOTE(rob): temporary attribute to indicate support for
        # completed migration to the new internal MK interface.
        return self.moe_kernel is not None

    @property
    defmk_owns_shared_expert(self) -> bool:
        # NOTE(rob): temporary attribute to indicate support for
        # completed migration to the new internal MK interface.
        return self.moe_kernel is not None and self.moe_kernel.owns_shared_experts

    @abstractmethod
    defcreate_weights(
        self,
        layer: torch.nn.Module,
        num_experts: int,
        hidden_size: int,
        intermediate_size_per_partition: int,
        params_dtype: torch.dtype,
        **extra_weight_attrs,
    ):
        raise NotImplementedError

    defuses_weight_scale_2_pattern(self) -> bool:
"""
        Returns True if this quantization method uses 'weight_scale_2' pattern
        for per-tensor weight scales (e.g., FP4 variants), False otherwise.

        This method should be overridden by subclasses that use the
        'weight_scale_2' pattern instead of the standard 'weight_scale' pattern.
        """
        return False

    defmaybe_roundup_sizes(
        self,
        hidden_size: int,
        intermediate_size_per_partition: int,
        act_dtype: torch.dtype,
        moe_parallel_config: FusedMoEParallelConfig,
    ) -> tuple[int, int]:
"""
        Given layer hidden size and intermediate size per partition and MoE
        configurations, round up hidden_size and intermediate_size_per_partition
        if necessary.

        Args:
            hidden_size: Layer hidden-size
            intermediate_size_per_partition: Intermediate size per partition for
                the layer.
            act_dtype: Data type of the layer activations.
            moe_parallel_config: Fused MoE parallelization strategy configuration.

        Return:
            A tuple of (rounded_hidden_size, rounded_intermediate_size_per_partition),
            where:
                - rounded_hidden_size is the possibly rounded up hidden size.
                - rounded_intermediate_size_per_partition is the possibly rounded
                  up intermediate size per partition.
        """
        from.all2all_utilsimport maybe_roundup_layer_hidden_size

        return maybe_roundup_layer_hidden_size(
            hidden_size, act_dtype, moe_parallel_config
        ), intermediate_size_per_partition

    defmaybe_make_prepare_finalize(
        self,
        routing_tables: tuple[torch.Tensor, torch.Tensor, torch.Tensor] | None = None,
    ) -> FusedMoEPrepareAndFinalizeModular | None:
        from.all2all_utilsimport maybe_make_prepare_finalize

        pf = maybe_make_prepare_finalize(
            self.moe, self.moe_quant_config, routing_tables
        )
        assert pf is None or isinstance(pf, FusedMoEPrepareAndFinalizeModular)
        return pf

    defselect_gemm_impl(
        self,
        prepare_finalize: FusedMoEPrepareAndFinalizeModular,
        layer: torch.nn.Module,
    ) -> FusedMoEExpertsModular:
        # based on the all2all implementation, select the appropriate
        # gemm implementation
        raise ValueError(
            f"{self.__class__.__name__} uses the new modular kernel initialization "
            "logic. This function should not be called."
        )

    @abstractmethod
    defget_fused_moe_quant_config(
        self, layer: torch.nn.Module
    ) -> FusedMoEQuantConfig | None:
        raise NotImplementedError

    @property
    deftopk_indices_dtype(self) -> torch.dtype | None:
        if self.moe_kernel is not None:
            return self.moe_kernel.prepare_finalize.topk_indices_dtype()
        return None

    @property
    defskip_forward_padding(self) -> bool:
"""Whether to skip the padding in the forward before applying the moe method."""
        return False

    @property
    defsupports_eplb(self) -> bool:
        return False

    @property
    defmethod_name(self) -> str:
        return self.__class__.__name__

    @property
    defis_monolithic(self) -> bool:
        if self.moe_kernel is None:
            if hasattr(self, "experts_cls"):
                return self.experts_cls.is_monolithic()
            else:
                return False
        return self.moe_kernel.is_monolithic

    defapply(
        self,
        layer: "FusedMoE",  # type: ignore[name-defined] # noqa: F821
        x: torch.Tensor,
        topk_weights: torch.Tensor,
        topk_ids: torch.Tensor,
        shared_experts_input: torch.Tensor | None,
    ) -> torch.Tensor:
        raise NotImplementedError

    defapply_monolithic(
        self,
        layer: "FusedMoE",  # type: ignore[name-defined] # noqa: F821
        x: torch.Tensor,
        router_logits: torch.Tensor,
        input_ids: torch.Tensor | None = None,
    ) -> torch.Tensor:
        raise NotImplementedError
```