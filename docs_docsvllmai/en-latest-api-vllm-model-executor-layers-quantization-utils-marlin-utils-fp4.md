---
title: marlin_utils_fp4 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/utils/marlin_utils_fp4/
source: sitemap
fetched_at: 2026-05-07T21:28:00.893573204-03:00
rendered_js: false
word_count: 0
summary: This function converts Mixture of Experts (MoE) model weights into the Marlin format for MXFP4 quantization, performing necessary repacking and scaling transformations.
tags:
    - marlin-format
    - mxfp4
    - weight-repacking
    - model-quantization
    - moe-layers
    - pytorch-optimization
category: api
---

```
defprepare_moe_mxfp4_layer_for_marlin(
    layer: torch.nn.Module,
    w13: torch.Tensor,
    w2: torch.Tensor,
    w13_scale: torch.Tensor,
    w2_scale: torch.Tensor,
    w13_bias: torch.Tensor | None,
    w2_bias: torch.Tensor | None,
) -> tuple[
    torch.Tensor,
    torch.Tensor,
    torch.Tensor,
    torch.Tensor,
    torch.Tensor | None,
    torch.Tensor | None,
]:
"""Pure-function version of prepare_moe_fp4_layer_for_marlin for MXFP4.

    Takes weight tensors as inputs and returns transformed tensors.
    Does NOT modify the layer in-place.
    """
    input_dtype = get_marlin_input_dtype()
    if (
        input_dtype is not None
        and input_dtype.itemsize == 1
        and input_dtype != torch.float8_e4m3fn
    ):
        raise RuntimeError("MXFP4 weight + INT8 activation is not supported.")

    group_size = 32  # MXFP4 block size

    # Derive dimensions from actual weight shapes to handle rounded/padded
    # sizes correctly (e.g., Mxfp4MoEMethod rounds up hidden_dim).
    # w13 shape: (E, 2*N, K//2)
    e = w13.shape[0]
    n = w13.shape[1] // 2  # intermediate_size_per_partition
    k = w13.shape[2] * 2  # hidden_size

    device = w13.device
    param_dtype = layer.params_dtype
    is_a_8bit = input_dtype is not None and input_dtype.itemsize == 1
    perm = torch.empty(0, dtype=torch.int, device=device)

    # WEIGHT: Repack weights to marlin format
    defrepack_weight(weight: torch.Tensor, name: str) -> torch.Tensor:
        tensor_list = []
        if "w13" in name:
            size_n, size_k = n * 2, k
        else:
            size_n, size_k = k, n

        assert weight.shape == (e, size_n, size_k // 2)

        for i in range(e):
            qweight = weight[i].view(torch.int32).T.contiguous()
            marlin_qweight = ops.gptq_marlin_repack(
                b_q_weight=qweight,
                perm=perm,
                size_k=size_k,
                size_n=size_n,
                num_bits=4,
                is_a_8bit=is_a_8bit,
            )
            tensor_list.append(marlin_qweight)
        return torch.cat([x.unsqueeze(0) for x in tensor_list], 0)

    w13 = repack_weight(w13, "w13")
    w2 = repack_weight(w2, "w2")

    # WEIGHT SCALES: Permute scales
    defpermute_scales(scales: torch.Tensor, name: str) -> torch.Tensor:
        scales = scales.view(torch.float8_e8m0fnu)
        scales = scales.to(param_dtype)

        tensor_list = []
        if "w13" in name:
            size_n, size_k = n * 2, k
        else:
            size_n, size_k = k, n

        for i in range(e):
            scale = scales[i].T
            marlin_scales = marlin_permute_scales(
                s=scale,
                size_k=size_k,
                size_n=size_n,
                group_size=group_size,
                is_a_8bit=is_a_8bit,
            )
            marlin_scales = mxfp4_marlin_process_scales(
                marlin_scales, input_dtype=input_dtype
            )
            tensor_list.append(marlin_scales)
        return torch.cat([x.unsqueeze(0) for x in tensor_list], 0)

    w13_scale = permute_scales(w13_scale, "w13")
    w2_scale = permute_scales(w2_scale, "w2")

    # BIAS: Permute bias
    defpermute_bias(bias: torch.Tensor | None) -> torch.Tensor | None:
        if bias is None:
            return None
        bias = bias.to(param_dtype)
        tensor_list = []
        for i in range(e):
            tensor_list.append(marlin_permute_bias(bias[i]))
        return torch.cat([x.unsqueeze(0) for x in tensor_list], 0)

    w13_bias = permute_bias(w13_bias)
    w2_bias = permute_bias(w2_bias)

    return w13, w2, w13_scale, w2_scale, w13_bias, w2_bias
```