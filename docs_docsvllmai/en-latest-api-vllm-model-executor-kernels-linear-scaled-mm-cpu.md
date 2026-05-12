---
title: cpu - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/scaled_mm/cpu/
source: sitemap
fetched_at: 2026-05-07T21:23:46.540386505-03:00
rendered_js: false
word_count: 0
summary: This document defines a PyTorch kernel implementation for FP8 block-quantized matrix multiplication specifically optimized for CPU architectures using AMX instructions.
tags:
    - cpu-optimization
    - fp8-quantization
    - amx-acceleration
    - matrix-multiplication
    - pytorch-kernel
    - gemm
category: api
---

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