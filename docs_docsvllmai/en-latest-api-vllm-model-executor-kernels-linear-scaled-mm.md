---
title: scaled_mm - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/scaled_mm/
source: sitemap
fetched_at: 2026-05-07T21:23:44.340708432-03:00
rendered_js: false
word_count: 126
summary: This document defines kernel implementations for scaled matrix multiplication (GEMM) operations in vLLM, specifically detailing ROCm-based Int8 scaled linear kernels and CPU-based FP8 block-scaled kernels.
tags:
    - vllm
    - gemm
    - scaled-linear
    - int8-quantization
    - fp8-quantization
    - rocm
    - kernel-implementation
category: reference
---

Modules:

Name Description `BlockScaledMMLinearKernel` `aiter` `cpu` `flashinfer` `marlin` `pytorch`

## AiterInt8ScaledMMLinearKernel [¶](#vllm.model_executor.kernels.linear.scaled_mm.AiterInt8ScaledMMLinearKernel "Permanent link")

Bases: `CutlassInt8ScaledMMLinearKernel`

Source code in `vllm/model_executor/kernels/linear/scaled_mm/aiter.py`

```
classAiterInt8ScaledMMLinearKernel(CutlassInt8ScaledMMLinearKernel):
    @classmethod
    defis_supported(
        cls, compute_capability: int | None = None
    ) -> tuple[bool, str | None]:
        if not current_platform.is_rocm():
            return False, "Requires ROCm."

        if compute_capability is not None and compute_capability < 90:
            return False, "requires compute capability 90 and above."

        try:
            importaiter  # noqa: F401 # deliberately attempt to import aiter
        except Exception:
            return False, "requires `aiter` to be installed."

        if not rocm_aiter_ops.is_linear_enabled():
            return (
                False,
                "requires setting `VLLM_ROCM_USE_AITER=1` "
                "and `VLLM_ROCM_USE_AITER_LINEAR=1`. "
                "`VLLM_ROCM_USE_AITER_LINEAR` default is True.",
            )
        return True, None

    @classmethod
    defcan_implement(cls, c: Int8ScaledMMLinearLayerConfig) -> tuple[bool, str | None]:
        if not c.input_symmetric:
            return False, "supports symmetric quantization only."
        return True, None

    defapply_weights(
        self,
        layer: torch.nn.Module,
        x: torch.Tensor,
        bias: torch.Tensor | None = None,
    ) -> torch.Tensor:
"""
        `AiterInt8ScaledMMLinearKernel` implements a fused version of
            `output = torch.mm((scale_a * a), (scale_b * b)).to(out_dtype)`
        where scale_a * a and scale_b * b are implemented using numpy-style
        broadcasting.
        Currently only support per-tensor-per-tensor GEMM
        and per-token-per-channel GEMM through AITER
        w8a8 scaled gemm. `AiterInt8ScaledMMLinearKernel` also does not support
        ATIER block scaled GEMM and mix-precision GEMM.
        """
        w_q, w_s, i_s, i_zp, azp_adj = self._get_layer_params(layer)

        # ops.scaled_int8_quant supports both dynamic and static quant:
        # * dynamic, i_s is None and x_s computed from x.
        # * static, i_s is scalar and x_s is i_s.
        symmetric = azp_adj is None
        assert symmetric, (
            "AiterInt8ScaledMMLinearKernel only supports symmetric quantization."
        )
        x_q, x_s, x_zp = ops.scaled_int8_quant(x, i_s, i_zp, symmetric=symmetric)

        assert x_zp is None, (
            "AiterInt8ScaledMMLinearKernel only supports symmetric quantization."
        )
        out_dtype = x.dtype

        assert w_q.shape[0] % 16 == 0 and w_q.shape[1] % 16 == 0
        assert out_dtype is torch.bfloat16 or out_dtype is torch.float16
        assert bias is None or bias.shape[0] == w_q.shape[1] and bias.dtype == out_dtype

        m = x_q.shape[0]  # a
        n = w_q.shape[1]  # b

        per_tensor_scale_a = x_s.numel() == 1
        per_tensor_scale_b = w_s.numel() == 1
        per_token_scale_a = x_s.numel() == m
        per_channel_scale_b = w_s.numel() == n

        # @TODO:
        # Maybe broadcast the per-tensor-scale into per-channel-scale
        # if one of the scale is a per-channel-scale.
        # For now, it only supports:
        # - per-tensor-per-tensor a8w8 scaled GEMM, and
        # - per-token-per-channel a8w8 scaled GEMM
        assert (per_tensor_scale_a and per_tensor_scale_b) or (
            per_token_scale_a and per_channel_scale_b
        ), (
            "Currently only support per-tensor-per-tensor GEMM "
            " and per-token-per-channel GEMM through AITER"
            " w8a8 scaled gemm. `AiterInt8ScaledMMLinearKernel` "
            "does not support AITER block scaled GEMM."
        )

        # gemm_a8w8_CK(a, b, scale_a, scale_b, bias) expects
        # a to be [M, K]
        # b to be [N, K]
        # CutlassInt8ScaledMMLinearKernel prepare weight `w_q` in [K, N] format
        return rocm_aiter_ops.w8a8_gemm(x_q, w_q.t(), x_s, w_s, bias, out_dtype)
```

### apply\_weights [¶](#vllm.model_executor.kernels.linear.scaled_mm.AiterInt8ScaledMMLinearKernel.apply_weights "Permanent link")

`AiterInt8ScaledMMLinearKernel` implements a fused version of `output = torch.mm((scale_a * a), (scale_b * b)).to(out_dtype)` where scale\_a * a and scale\_b * b are implemented using numpy-style broadcasting. Currently only support per-tensor-per-tensor GEMM and per-token-per-channel GEMM through AITER w8a8 scaled gemm. `AiterInt8ScaledMMLinearKernel` also does not support ATIER block scaled GEMM and mix-precision GEMM.

Source code in `vllm/model_executor/kernels/linear/scaled_mm/aiter.py`

```
defapply_weights(
    self,
    layer: torch.nn.Module,
    x: torch.Tensor,
    bias: torch.Tensor | None = None,
) -> torch.Tensor:
"""
    `AiterInt8ScaledMMLinearKernel` implements a fused version of
        `output = torch.mm((scale_a * a), (scale_b * b)).to(out_dtype)`
    where scale_a * a and scale_b * b are implemented using numpy-style
    broadcasting.
    Currently only support per-tensor-per-tensor GEMM
    and per-token-per-channel GEMM through AITER
    w8a8 scaled gemm. `AiterInt8ScaledMMLinearKernel` also does not support
    ATIER block scaled GEMM and mix-precision GEMM.
    """
    w_q, w_s, i_s, i_zp, azp_adj = self._get_layer_params(layer)

    # ops.scaled_int8_quant supports both dynamic and static quant:
    # * dynamic, i_s is None and x_s computed from x.
    # * static, i_s is scalar and x_s is i_s.
    symmetric = azp_adj is None
    assert symmetric, (
        "AiterInt8ScaledMMLinearKernel only supports symmetric quantization."
    )
    x_q, x_s, x_zp = ops.scaled_int8_quant(x, i_s, i_zp, symmetric=symmetric)

    assert x_zp is None, (
        "AiterInt8ScaledMMLinearKernel only supports symmetric quantization."
    )
    out_dtype = x.dtype

    assert w_q.shape[0] % 16 == 0 and w_q.shape[1] % 16 == 0
    assert out_dtype is torch.bfloat16 or out_dtype is torch.float16
    assert bias is None or bias.shape[0] == w_q.shape[1] and bias.dtype == out_dtype

    m = x_q.shape[0]  # a
    n = w_q.shape[1]  # b

    per_tensor_scale_a = x_s.numel() == 1
    per_tensor_scale_b = w_s.numel() == 1
    per_token_scale_a = x_s.numel() == m
    per_channel_scale_b = w_s.numel() == n

    # @TODO:
    # Maybe broadcast the per-tensor-scale into per-channel-scale
    # if one of the scale is a per-channel-scale.
    # For now, it only supports:
    # - per-tensor-per-tensor a8w8 scaled GEMM, and
    # - per-token-per-channel a8w8 scaled GEMM
    assert (per_tensor_scale_a and per_tensor_scale_b) or (
        per_token_scale_a and per_channel_scale_b
    ), (
        "Currently only support per-tensor-per-tensor GEMM "
        " and per-token-per-channel GEMM through AITER"
        " w8a8 scaled gemm. `AiterInt8ScaledMMLinearKernel` "
        "does not support AITER block scaled GEMM."
    )

    # gemm_a8w8_CK(a, b, scale_a, scale_b, bias) expects
    # a to be [M, K]
    # b to be [N, K]
    # CutlassInt8ScaledMMLinearKernel prepare weight `w_q` in [K, N] format
    return rocm_aiter_ops.w8a8_gemm(x_q, w_q.t(), x_s, w_s, bias, out_dtype)
```

## CPUFp8BlockScaledMMKernel [¶](#vllm.model_executor.kernels.linear.scaled_mm.CPUFp8BlockScaledMMKernel "Permanent link")

Bases: `Fp8BlockScaledMMLinearKernel`

FP8 W8A16 block-quantized GEMM via AMX BRGEMM on CPU.

Source code in `vllm/model_executor/kernels/linear/scaled_mm/cpu.py`

```
classCPUFp8BlockScaledMMKernel(Fp8BlockScaledMMLinearKernel):
"""FP8 W8A16 block-quantized GEMM via AMX BRGEMM on CPU."""

    # Input stays BF16 — no FP8 activation quantization.
    apply_input_quant = False

    @classmethod
    defis_supported(
        cls, compute_capability: int | None = None
    ) -> tuple[bool, str | None]:
        if not current_platform.is_cpu():
            return False, "requires CPU platform."
        if not torch.cpu._is_amx_tile_supported():
            return False, "requires AMX tile support (Sapphire Rapids or newer)."
        if not ops._supports_cpu_fp8_w8a16:
            return False, "fp8_scaled_mm_cpu op not available."
        return True, None

    @classmethod
    defcan_implement(
        cls, config: FP8ScaledMMLinearLayerConfig
    ) -> tuple[bool, str | None]:
        # Validate weight block shape
        weight_gs = config.weight_quant_key.scale.group_shape
        if weight_gs.col <= 0 or weight_gs.col != 128:
            return False, (
                "CPU FP8 kernel requires K-dimension block size of 128, "
                f"got {weight_gs.col}."
            )
        if weight_gs.row <= 0 or weight_gs.row % 32 != 0:
            return False, (
                "CPU FP8 kernel requires N-dimension block size to be "
                f"a positive multiple of 32, got {weight_gs.row}."
            )
        if config.out_dtype not in (torch.bfloat16, torch.float32):
            return False, "Only bfloat16/float32 output dtype supported."
        return True, None

    defprocess_weights_after_loading(self, layer: torch.nn.Module) -> None:
        # Skip the base class process (FP8 padding / fnuz normalization)
        # which is GPU-oriented.  Instead, VNNI-prepack weights for AMX.
        params = self._get_layer_params(layer)
        packed_weight = torch.ops._C.convert_weight_packed(params.weight)
        replace_parameter(
            layer,
            params.WEIGHT,
            torch.nn.Parameter(packed_weight, requires_grad=False),
        )

        # Re-wrap scale as a plain Parameter so the kernel can read it
        # without weight-loader metadata interfering.
        scale_attr = (
            params.WEIGHT_SCALE_INV
            if params.weight_scale_inv is not None
            else params.WEIGHT_SCALE
        )
        weight_scale = (
            params.weight_scale_inv
            if params.weight_scale_inv is not None
            else params.weight_scale
        )
        assert weight_scale is not None
        replace_parameter(
            layer,
            scale_attr,
            torch.nn.Parameter(weight_scale.data, requires_grad=False),
        )

    defapply_weights(
        self,
        layer: torch.nn.Module,
        x: torch.Tensor,
        bias: torch.Tensor | None = None,
        **kwargs,
    ) -> torch.Tensor:
        params = self._get_layer_params(layer)
        weight_scale = (
            params.weight_scale_inv
            if params.weight_scale_inv is not None
            else params.weight_scale
        )

        x_2d = x.reshape(-1, x.shape[-1]) if x.dim() > 2 else x
        out = torch.ops._C.fp8_scaled_mm_cpu(
            x_2d,
            params.weight,
            weight_scale,
            list(self.weight_group_shape),
            bias,
            x.dtype,
            True,  # is_vnni (weight already prepacked)
        )
        return out.reshape(x.shape[:-1] + (out.size(-1),)) if x.dim() > 2 else out

    defapply_block_scaled_mm(
        self,
        A: torch.Tensor,
        B: torch.Tensor,
        As: torch.Tensor,
        Bs: torch.Tensor,
    ) -> torch.Tensor:
        raise NotImplementedError(
            "CPUFp8BlockScaledMMKernel overrides apply_weights directly."
        )
```

## MarlinFP8ScaledMMLinearKernel [¶](#vllm.model_executor.kernels.linear.scaled_mm.MarlinFP8ScaledMMLinearKernel "Permanent link")

Bases: `FP8ScaledMMLinearKernel`

FP8 Marlin kernel for GPUs that lack FP8 hardware support. Leverages the Marlin kernel for fast weight-only FP8 quantization.

Source code in `vllm/model_executor/kernels/linear/scaled_mm/marlin.py`

```
classMarlinFP8ScaledMMLinearKernel(FP8ScaledMMLinearKernel):
"""
    FP8 Marlin kernel for GPUs that lack FP8 hardware support.
    Leverages the Marlin kernel for fast weight-only FP8 quantization.
    """

    @classmethod
    defis_supported(
        cls, compute_capability: int | None = None
    ) -> tuple[bool, str | None]:
        if not current_platform.is_cuda():
            return False, "requires CUDA."
        # Check if platform supports FP8 Marlin
        if not is_fp8_marlin_supported():
            return False, "FP8 Marlin requires compute capability 7.5 or higher"
        if envs.VLLM_BATCH_INVARIANT:
            return False, "FP8 Marlin not supported for batch invariant execution."
        if (
            compute_capability is not None
            and compute_capability >= 89
            and not envs.VLLM_TEST_FORCE_FP8_MARLIN
        ):
            return (
                False,
                "To apply FP8 Marlin on high-capability GPUs, please set "
                "VLLM_TEST_FORCE_FP8_MARLIN=1",
            )
        return True, None

    @classmethod
    defcan_implement(cls, c: FP8ScaledMMLinearLayerConfig) -> tuple[bool, str | None]:
        return True, None

    def__init__(
        self, c: FP8ScaledMMLinearLayerConfig, layer_param_names: Sequence[str]
    ) -> None:
        super().__init__(c, layer_param_names)
        self.marlin_input_dtype = None
        self.block_quant = self.config.weight_quant_key in {kFp8Static128BlockSym}
        self.size_k_first = not self.block_quant

    defprocess_weights_after_loading(self, layer: torch.nn.Module) -> None:
        if self.block_quant:
            weight, weight_scale_inv = process_fp8_weight_block_strategy(
                layer.weight, layer.weight_scale_inv
            )
            # Update layer with new values
            replace_parameter(layer, "weight", weight.data)
            replace_parameter(layer, "weight_scale_inv", weight_scale_inv.data)
        else:
            w_q, *_ = self._get_layer_params(layer)
            # Compressed tensors transposes the weight to (K, N)
            # for channel and tensor quant strategies.
            # So we can skip the transpose if the layout is
            # already (K, N).
            # TODO: Remove this check once the layouts have been
            # canonicalized to a standard (N, K) dimension. See issue
            # #33314 for more details.
            if w_q.shape != (
                layer.input_size_per_partition,
                layer.output_size_per_partition,
            ):
                # transpose the weights to (K,N)
                replace_parameter(
                    layer,
                    "weight",
                    w_q.t(),
                )

        layer.input_scale = None
        prepare_fp8_layer_for_marlin(
            layer, self.size_k_first, input_dtype=self.marlin_input_dtype
        )
        del layer.input_scale

    defapply_weights(
        self,
        layer: torch.nn.Module,
        x: torch.Tensor,
        bias: torch.Tensor | None = None,
    ) -> torch.Tensor:
        if self.block_quant:
            weight_scale = layer.weight_scale_inv
        else:
            weight_scale = layer.weight_scale
        return apply_fp8_marlin_linear(
            input=x,
            weight=layer.weight,
            weight_scale=weight_scale,
            workspace=layer.workspace,
            size_n=layer.output_size_per_partition,
            size_k=layer.input_size_per_partition,
            input_dtype=self.marlin_input_dtype,
            bias=bias,
        )

    defapply_scaled_mm(
        self,
        *,
        A: torch.Tensor,
        B: torch.Tensor,
        out_dtype: torch.dtype,
        As: torch.Tensor,
        Bs: torch.Tensor,
        bias: torch.Tensor | None,
        output_shape: list,
    ) -> torch.Tensor:
        pass
```