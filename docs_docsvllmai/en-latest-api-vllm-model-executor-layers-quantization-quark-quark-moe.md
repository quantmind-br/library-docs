---
title: quark_moe - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/quark/quark_moe/
source: sitemap
fetched_at: 2026-05-07T21:27:33.1548559-03:00
rendered_js: false
word_count: 13
summary: This document defines a quantization method class for Mixture-of-Experts (MoE) layers, specifically managing OCP MX format configurations and backend selection for hardware-accelerated quantization.
tags:
    - quantization
    - mixture-of-experts
    - mxfp4
    - ocp
    - model-optimization
    - tensors
    - backend-selection
category: concept
---

```
classQuarkOCP_MX_MoEMethod(QuarkMoEMethod):
    def__init__(
        self,
        weight_config: dict[str, Any],
        input_config: dict[str, Any] | None,
        moe: FusedMoEConfig,
    ):
        super().__init__(moe)
        self.weight_quant = weight_config
        self.input_quant = input_config

        weight_qscheme = self.weight_quant.get("qscheme")
        if not weight_qscheme == "per_group":
            raise ValueError(
                "For MX(FP4) Fused MoE layers, only per-group scales "
                f"for weights are supported. Found {weight_qscheme}."
            )  # noqa E501

        self.weight_dtype = self.weight_quant["dtype"].replace("fp", "mxfp")
        if self.input_quant is not None:
            input_quant = self.input_quant["dtype"]
            if input_quant in ["fp4", "fp6_e3m2", "fp6_e2m3"]:
                self.input_dtype = input_quant.replace("fp", "mxfp")
            elif input_quant == "fp8_e4m3":
                self.input_dtype = input_quant.replace("fp8_e4m3", "fp8")
            else:
                raise NotImplementedError(
                    f"Current input dtype {input_quant} is not compatible \
                        with OCP MX (weight) MoE quantization. Please open an issue"
                )
        else:
            self.input_dtype = None

        self.fp4_dtype = getattr(torch, "float4_e2m1fn_x2", None)

        self.ocp_mx_scheme = OCP_MX_Scheme.from_quant_dtype(
            self.input_dtype, self.weight_dtype
        )

        if self.ocp_mx_scheme is None:
            raise ValueError(
                f"Unsupported OCP MX dtype combination for MoE: "
                f"input_dtype={self.input_dtype}, weight_dtype={self.weight_dtype}. "
                f"Please check that the combination is supported in OCP_MX_Scheme."
            )

        # TODO(bowenbao): refactor and introduce backends for other OCP MX schemes,
        # use kernel abstraction for all OCP MX MOE implementations.
        self.mxfp4_backend: Mxfp4MoeBackend = Mxfp4MoeBackend.NONE
        self.experts_cls: type[mk.FusedMoEExperts] | None = None
        self.moe_kernel: mk.FusedMoEKernel | None = None

        # Used for triton kernel precision configs (W4A8, TRITON backends)
        self.w13_precision_config = None
        self.w2_precision_config = None

        if self.input_quant is not None:
            self.static_input_scales = not self.input_quant.get("is_dynamic")
        else:
            self.static_input_scales = False

        # Select backend based on OCP MX scheme
        if self.ocp_mx_scheme == "w_mxfp4":
            # W4A16: weight-only MXFP4
            self.mxfp4_backend, self.experts_cls = select_mxfp4_moe_backend(moe)
        elif self.ocp_mx_scheme == "w_mxfp4_a_fp8" and self.static_input_scales:
            # W4A8: MXFP4 weights + static FP8 activations
            self.mxfp4_backend, self.experts_cls = select_mxfp4_moe_backend(
                moe, activation_key=kFp8StaticTensorSym
            )

        # Validation for unsupported schemes
        if any(
            self.ocp_mx_scheme.endswith(a_scheme)
            for a_scheme in ["a_mxfp4", "a_mxfp6_e3m2", "a_mxfp6_e2m3"]
        ):
            if self.static_input_scales:
                raise NotImplementedError(
                    "QuarkOCP_MX_MoEMethod with static input scales is currently "
                    f"not implemented for OCP MX scheme {self.ocp_mx_scheme}. "
                    "Please open an issue."
                )
        elif self.ocp_mx_scheme.endswith("a_fp8") and not self.static_input_scales:
            raise NotImplementedError(
                "QuarkOCP_MX_MoEMethod with dynamic input scales is currently "
                f"not implemented for OCP MX scheme {self.ocp_mx_scheme}. "
                "Please open an issue."
            )

        self.use_rocm_aiter_moe = rocm_aiter_ops.is_fused_moe_enabled()

        self.model_type = getattr(
            get_current_vllm_config().model_config.hf_config, "model_type", None
        )

        # TODO: Remove once all OCP MX schemes use the kernel abstraction
        _AITER_NATIVE_OCP_MX_SCHEMES = ("w_mxfp4", "w_mxfp4_a_mxfp4", "w_mxfp4_a_fp8")
        self.emulate = (
            not current_platform.supports_mx()
            or self.ocp_mx_scheme not in _AITER_NATIVE_OCP_MX_SCHEMES
        ) and (
            self.mxfp4_backend is Mxfp4MoeBackend.NONE or not self.use_rocm_aiter_moe
        )

        if self.emulate:
            # We use the same code path between MXFP4/MXFP6 emulation.
            self.mxfp4_backend = Mxfp4MoeBackend.EMULATION

        # TODO: Remove `self.mxfp4_backend != Mxfp4MoeBackend.NONE` and make it so that
        # all MXFP4 backends use the kernel abstraction.
        if self.mxfp4_backend != Mxfp4MoeBackend.NONE:
            self.experts_cls = backend_to_kernel_cls(self.mxfp4_backend)[0]

        # Log backend selection
        if self.mxfp4_backend != Mxfp4MoeBackend.NONE:
            logger.info_once(
                f"Using {self.mxfp4_backend.value} backend for {self.ocp_mx_scheme}"
            )
        elif self.emulate:
            logger.warning_once(
                f"The current mode (supports_mx={current_platform.supports_mx()}, "
                f"use_rocm_aiter_moe={self.use_rocm_aiter_moe}, "
                f"ocp_mx_scheme={self.ocp_mx_scheme}) "
                "does not support native MXFP4/MXFP6 "
                "computation. Simulated weight dequantization and activation "
                "QDQ (quantize and dequantize) will be used, with the linear "
                "layers computed in high precision."
            )

    defmaybe_roundup_sizes(
        self,
        hidden_size: int,
        intermediate_size_per_partition: int,
        act_dtype: torch.dtype,
        moe_parallel_config: FusedMoEParallelConfig,
    ) -> tuple[int, int]:
        hidden_size, intermediate_size_per_partition = super().maybe_roundup_sizes(
            hidden_size=hidden_size,
            intermediate_size_per_partition=intermediate_size_per_partition,
            act_dtype=act_dtype,
            moe_parallel_config=moe_parallel_config,
        )
        # In case quantization emulation backend is used, there is no need to apply
        # MXFP4-specific padding logic as the compute happens in higher precision.
        if (
            self.mxfp4_backend is not None
            and self.mxfp4_backend != Mxfp4MoeBackend.EMULATION
        ):
            hidden_size, intermediate_size_per_partition = (
                mxfp4_round_up_hidden_size_and_intermediate_size(
                    self.mxfp4_backend, hidden_size, intermediate_size_per_partition
                )
            )
        return hidden_size, intermediate_size_per_partition

    defget_packed_dim(self, dim: int, quant_dtype: str):
        if quant_dtype == "mxfp4":
            assert dim % 2 == 0
            return dim // 2
        else:
            # FP6 packs 4 * 6 = 24 bits on 3 bytes.
            assert (dim * 3) % 4 == 0
            return (dim * 3) // 4

    defcreate_weights(
        self,
        layer: torch.nn.Module,
        num_experts: int,
        hidden_size: int,
        intermediate_size_per_partition: int,
        params_dtype: torch.dtype,
        **extra_weight_attrs,
    ):
        # Add the quantization method used (per tensor/grouped/channel)
        # to ensure the weight scales are loaded in properly
        extra_weight_attrs.update(
            {"quant_method": FusedMoeWeightScaleSupported.BLOCK.value}
        )

        params_dtype = torch.uint8

        # WEIGHTS
        w13_weight = torch.nn.Parameter(
            torch.zeros(
                num_experts,
                2 * intermediate_size_per_partition,
                self.get_packed_dim(hidden_size, self.weight_dtype),
                dtype=params_dtype,
            ),
            requires_grad=False,
        )
        layer.register_parameter("w13_weight", w13_weight)

        set_weight_attrs(w13_weight, extra_weight_attrs)

        w2_weight = torch.nn.Parameter(
            torch.zeros(
                num_experts,
                hidden_size,
                self.get_packed_dim(intermediate_size_per_partition, self.weight_dtype),
                dtype=params_dtype,
            ),
            requires_grad=False,
        )
        layer.register_parameter("w2_weight", w2_weight)

        set_weight_attrs(w2_weight, extra_weight_attrs)

        # WEIGHT_SCALES
        w13_weight_scale = torch.nn.Parameter(
            torch.ones(
                num_experts,
                2 * intermediate_size_per_partition,
                hidden_size // OCP_MX_BLOCK_SIZE,
                dtype=params_dtype,
            ),
            requires_grad=False,
        )
        w2_weight_scale = torch.nn.Parameter(
            torch.ones(
                num_experts,
                hidden_size,
                intermediate_size_per_partition // OCP_MX_BLOCK_SIZE,
                dtype=params_dtype,
            ),
            requires_grad=False,
        )
        set_weight_attrs(w2_weight_scale, extra_weight_attrs)
        set_weight_attrs(w13_weight_scale, extra_weight_attrs)

        layer.register_parameter("w13_weight_scale", w13_weight_scale)
        layer.register_parameter("w2_weight_scale", w2_weight_scale)

        if self.has_bias:
            w13_bias = torch.nn.Parameter(
                torch.zeros(
                    num_experts,
                    2 * intermediate_size_per_partition,
                    dtype=torch.float32,
                ),
                requires_grad=False,
            )
            layer.register_parameter("w13_bias", w13_bias)
            set_weight_attrs(w13_bias, extra_weight_attrs)

            w2_bias = torch.nn.Parameter(
                torch.zeros(num_experts, hidden_size, dtype=torch.float32),
                requires_grad=False,
            )
            layer.register_parameter("w2_bias", w2_bias)
            set_weight_attrs(w2_bias, extra_weight_attrs)
        else:
            layer.w13_bias, layer.w2_bias = None, None

        # INPUT_SCALES
        if self.static_input_scales:
            w13_input_scale = torch.nn.Parameter(
                torch.ones(num_experts, dtype=torch.float32), requires_grad=False
            )
            layer.register_parameter("w13_input_scale", w13_input_scale)
            set_weight_attrs(w13_input_scale, extra_weight_attrs)

            w2_input_scale = torch.nn.Parameter(
                torch.ones(num_experts, dtype=torch.float32), requires_grad=False
            )
            layer.register_parameter("w2_input_scale", w2_input_scale)
            set_weight_attrs(w2_input_scale, extra_weight_attrs)
        else:
            layer.w13_input_scale = None
            layer.w2_input_scale = None

    defprocess_weights_after_loading(self, layer):
        # For MXFP4 schemes with native backend, use oracle
        if self.mxfp4_backend != Mxfp4MoeBackend.NONE:
            self._setup_kernel(layer)
            return

        if self.static_input_scales and self.input_dtype == "fp8":
            # firstly, process activations if fp8 static input
            if layer.w13_input_scale is None or layer.w2_input_scale is None:
                raise ValueError(
                    "QuantConfig has static quantization, but found "
                    "activation scales are None."
                )
            if not all_close_1d(layer.w13_input_scale) or not all_close_1d(
                layer.w2_input_scale
            ):
                logger.warning_once(
                    "Found input_scales that are not equal for "
                    "fp8 MoE layer. Using the maximum across experts "
                    "for each layer. "
                )
            layer.w13_input_scale = torch.nn.Parameter(
                layer.w13_input_scale.max(), requires_grad=False
            )
            layer.w2_input_scale = torch.nn.Parameter(
                layer.w2_input_scale.max(), requires_grad=False
            )

            if current_platform.is_fp8_fnuz():
                # Normalize the weights and scales
                _, _, w13_input_scale = normalize_e4m3fn_to_e4m3fnuz(
                    torch.empty_like(layer.w13_weight, dtype=torch.float8_e4m3fn),
                    torch.empty_like(
                        layer.w13_weight_scale, dtype=layer.w13_weight_scale.dtype
                    ),
                    layer.w13_input_scale,
                )
                _, _, w2_input_scale = normalize_e4m3fn_to_e4m3fnuz(
                    torch.empty_like(layer.w2_weight, dtype=torch.float8_e4m3fn),
                    torch.empty_like(
                        layer.w2_weight_scale, dtype=layer.w13_weight_scale.dtype
                    ),
                    layer.w2_input_scale,
                )
                # Reset the parameter
                if w13_input_scale is not None:
                    layer.w13_input_scale = torch.nn.Parameter(
                        w13_input_scale, requires_grad=False
                    )
                if w2_input_scale is not None:
                    layer.w2_input_scale = torch.nn.Parameter(
                        w2_input_scale, requires_grad=False
                    )

        # TODO(bowenbao): gradually migrate to oracles.
        # Existing AITER path for w_mxfp4_a_mxfp4 and other schemes
        fromaiter.utility.fp4_utilsimport e8m0_shuffle

        # Pre-shuffle weight scales
        s0, s1, _ = layer.w13_weight_scale.shape
        w13_weight_scale = layer.w13_weight_scale.view(s0 * s1, -1)
        w13_weight_scale = e8m0_shuffle(w13_weight_scale)
        layer.w13_weight_scale.data = w13_weight_scale.view(s0, s1, -1)

        s0, s1, _ = layer.w2_weight_scale.shape
        w2_weight_scale = layer.w2_weight_scale.view(s0 * s1, -1)
        w2_weight_scale = e8m0_shuffle(w2_weight_scale)
        layer.w2_weight_scale.data = w2_weight_scale.view(s0, s1, -1)

        if self.fp4_dtype is not None:
            layer.w13_weight = torch.nn.Parameter(
                layer.w13_weight.view(self.fp4_dtype),
                requires_grad=layer.w13_weight.requires_grad,
            )
            layer.w2_weight = torch.nn.Parameter(
                layer.w2_weight.view(self.fp4_dtype),
                requires_grad=layer.w2_weight.requires_grad,
            )
        # Pre-shuffle weight
        shuffled_w13, shuffled_w2 = rocm_aiter_ops.shuffle_weights(
            layer.w13_weight.data, layer.w2_weight.data
        )

        layer.w13_weight = torch.nn.Parameter(shuffled_w13, requires_grad=False)
        layer.w2_weight = torch.nn.Parameter(shuffled_w2, requires_grad=False)
        layer.w13_weight.is_shuffled = True
        layer.w2_weight.is_shuffled = True

        # Build quant config for AITER path
        self.moe_quant_config = self.get_fused_moe_quant_config(layer)
        torch.accelerator.empty_cache()

    def_setup_kernel(self, layer: FusedMoE):
"""Setup kernel using oracle functions for MXFP4 schemes (W4A16, W4A8)."""
        w13_bias = getattr(layer, "w13_bias", None)
        w2_bias = getattr(layer, "w2_bias", None)

        # Convert weights to kernel format (handles all backend-specific logic)
        w13, w2, w13_scale, w2_scale, w13_bias, w2_bias = (
            convert_gpt_oss_weight_to_mxfp4_moe_kernel_format(
                mxfp4_backend=self.mxfp4_backend,
                layer=layer,
                w13_weight=layer.w13_weight,
                w2_weight=layer.w2_weight,
                w13_weight_scale=layer.w13_weight_scale,
                w2_weight_scale=layer.w2_weight_scale,
                w13_bias=w13_bias,
                w2_bias=w2_bias,
            )
        )

        # Handle weight/scale assignment based on backend type
        if self.mxfp4_backend in TRITON_BACKENDS or self.mxfp4_backend in (
            Mxfp4MoeBackend.AITER_MXFP4_FP8,
        ):
            # Triton-based backends: w13/w2 are triton_kernels.tensor.Tensor
            # Store on layer for apply(), scales are PrecisionConfig
            layer.w13_weight = w13
            layer.w2_weight = w2
            self.w13_precision_config = w13_scale
            self.w2_precision_config = w2_scale
        else:
            # Standard backends: replace parameters
            replace_parameter(layer, "w13_weight", w13)
            replace_parameter(layer, "w2_weight", w2)
            replace_parameter(layer, "w13_weight_scale", w13_scale)
            replace_parameter(layer, "w2_weight_scale", w2_scale)

        if w13_bias is not None and w2_bias is not None:
            replace_parameter(layer, "w13_bias", w13_bias)
            replace_parameter(layer, "w2_bias", w2_bias)

        torch.accelerator.empty_cache()

        # Build quant config and kernel
        self.moe_quant_config = self.get_fused_moe_quant_config(layer)
        if self.moe_quant_config is not None and self.experts_cls is not None:
            self.moe_kernel = make_mxfp4_moe_kernel(
                moe_quant_config=self.moe_quant_config,
                moe_config=self.moe,
                mxfp4_backend=self.mxfp4_backend,
                experts_cls=self.experts_cls,
                routing_tables=layer._maybe_init_expert_routing_tables(),
                shared_experts=layer.shared_experts,
            )

    defget_fused_moe_quant_config(
        self, layer: torch.nn.Module
    ) -> FusedMoEQuantConfig | None:
        # For oracle-based backends (W4A16, W4A8), use make_mxfp4_moe_quant_config
        if self.mxfp4_backend not in (Mxfp4MoeBackend.NONE, Mxfp4MoeBackend.EMULATION):
            # Determine scale source based on backend type
            if self.mxfp4_backend in TRITON_BACKENDS or self.mxfp4_backend in (
                Mxfp4MoeBackend.AITER_MXFP4_FP8,
            ):
                w1_scale = self.w13_precision_config
                w2_scale = self.w2_precision_config
            else:
                w1_scale = layer.w13_weight_scale
                w2_scale = layer.w2_weight_scale

            return make_mxfp4_moe_quant_config(
                mxfp4_backend=self.mxfp4_backend,
                w1_scale=w1_scale,
                w2_scale=w2_scale,
                w1_bias=getattr(layer, "w13_bias", None),
                w2_bias=getattr(layer, "w2_bias", None),
                a1_scale=getattr(layer, "w13_input_scale", None),
                a2_scale=getattr(layer, "w2_input_scale", None),
            )

        # Emulation and other schemes
        if self.ocp_mx_scheme == "w_mxfp4":
            return mxfp4_w4a16_moe_quant_config(
                w1_scale=layer.w13_weight_scale,
                w2_scale=layer.w2_weight_scale,
                w1_bias=layer.w13_bias,
                w2_bias=layer.w2_bias,
            )
        elif self.ocp_mx_scheme == "w_mxfp4_a_fp8":
            return mxfp4_w4a8_moe_quant_config(
                w1_scale=layer.w13_weight_scale,
                w2_scale=layer.w2_weight_scale,
                a1_scale=layer.w13_input_scale,
                a2_scale=layer.w2_input_scale,
                w1_bias=layer.w13_bias,
                w2_bias=layer.w2_bias,
                block_shape=None,
            )
        elif self.ocp_mx_scheme in ["w_mxfp6_e3m2_a_fp8", "w_mxfp6_e2m3_a_fp8"]:
            raise NotImplementedError(
                "Currently there is no corresponding fused moe quant config configured "
                f"in vLLM for OCP MX scheme {self.ocp_mx_scheme}. Please open an issue."
            )
        else:
            return ocp_mx_moe_quant_config(
                quant_dtype=self.input_dtype,
                weight_dtype=self.weight_dtype,
                w1_scale=layer.w13_weight_scale,
                w2_scale=layer.w2_weight_scale,
                w1_bias=layer.w13_bias,
                w2_bias=layer.w2_bias,
                a1_scale=None,
                a2_scale=None,
                block_shape=None,
            )

    @property
    defis_monolithic(self) -> bool:
        if self.moe_kernel is not None:
            return self.moe_kernel.is_monolithic
        return False

    defapply(
        self,
        layer: FusedMoE,
        x: torch.Tensor,
        topk_weights: torch.Tensor,
        topk_ids: torch.Tensor,
        shared_experts_input: torch.Tensor | None,
    ) -> torch.Tensor:
        # For oracle-based kernels (W4A16, W4A8) or emulation kernel
        if self.moe_kernel is not None:
            return self.moe_kernel.apply(
                hidden_states=x,
                w1=layer.w13_weight,
                w2=layer.w2_weight,
                topk_weights=topk_weights,
                topk_ids=topk_ids,
                activation=layer.activation,
                global_num_experts=layer.global_num_experts,
                apply_router_weight_on_input=layer.apply_router_weight_on_input,
                expert_map=layer.expert_map,
                shared_experts_input=shared_experts_input,
            )

        # AITER path
        # TODO: Refactor this to use modular MOE kernel as well.
        fromvllm.model_executor.layers.fused_moe.rocm_aiter_fused_moeimport (
            rocm_aiter_fused_experts,
        )

        return rocm_aiter_fused_experts(
            x,
            layer.w13_weight,
            layer.w2_weight,
            topk_weights=topk_weights,
            topk_ids=topk_ids,
            activation=layer.activation,
            quant_config=self.moe_quant_config,
            moe_config=layer.moe_config,
            expert_map=layer.expert_map,
        )

    defapply_monolithic(
        self,
        layer: FusedMoE,
        x: torch.Tensor,
        router_logits: torch.Tensor,
        input_ids: torch.Tensor | None = None,
    ) -> torch.Tensor:
        assert self.is_monolithic
        assert self.moe_kernel is not None
        return self.moe_kernel.apply_monolithic(
            hidden_states=x,
            w1=layer.w13_weight,
            w2=layer.w2_weight,
            router_logits=router_logits,
            activation=layer.activation,
            global_num_experts=layer.global_num_experts,
            expert_map=layer.expert_map,
            apply_router_weight_on_input=layer.apply_router_weight_on_input,
        )
```