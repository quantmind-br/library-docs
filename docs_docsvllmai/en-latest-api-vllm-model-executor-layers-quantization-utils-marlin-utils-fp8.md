---
title: marlin_utils_fp8 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/utils/marlin_utils_fp8/
source: sitemap
fetched_at: 2026-05-07T21:28:01.973529568-03:00
rendered_js: false
word_count: 10
summary: This function converts FP8 Mixture-of-Experts layer weights and scales into the Marlin kernel format to enable efficient weight-only compression and inference.
tags:
    - fp8-quantization
    - marlin-kernel
    - mixture-of-experts
    - model-optimization
    - weight-repacking
    - tensor-processing
category: api
---

```
defprepare_fp8_moe_layer_for_marlin(
    layer: torch.nn.Module,
    w13_weight: torch.Tensor,
    w2_weight: torch.Tensor,
    w13_weight_scale: torch.Tensor,
    w2_weight_scale: torch.Tensor,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
"""
    Shuffle weights and scales into marlin format.

    Note that this function has the side effect of adding a `workspace`
    attribute to the layer. This `workspace` does not need to be
    registered as a Parameter as it is not used during weight reloading.
    """

    logger.warning_once(
        "Your GPU does not have native support for FP8 computation but "
        "FP8 quantization is being used. Weight-only FP8 compression will "
        "be used leveraging the Marlin kernel. This may degrade "
        "performance for compute-heavy workloads."
    )
    input_dtype = get_marlin_input_dtype()
    if input_dtype is not None and input_dtype.itemsize == 1:
        raise NotImplementedError("Marlin W8A8 is not supported.")

    e = layer.num_experts
    k = layer.hidden_size
    n = layer.intermediate_size_per_partition
    w13_n = w13_weight.size(1)
    weight_block_size = getattr(layer, "weight_block_size", None)

    # WORKSPACE
    device = layer.w13_weight.device
    # NOTE(rob): we do not need to register the workspace as a param
    # because it is not used as part of the weight reloading process.
    layer.workspace = marlin_make_workspace_new(device, 4)
    perm = torch.empty(0, dtype=torch.int, device=device)

    # WEIGHT
    # Repack weights to marlin format
    defrepack_weight(name: str, weight: torch.Tensor) -> torch.Tensor:
        tensor_list = []
        if "w13" in name:
            size_n, size_k = w13_n, k
        else:
            size_n, size_k = k, n

        assert weight.shape == (e, size_n, size_k)

        for i in range(e):
            qweight = pack_fp8_to_int32(weight[i], size_k_first=False)
            qweight = qweight.T.contiguous()

            marlin_qweight = ops.gptq_marlin_repack(
                b_q_weight=qweight, perm=perm, size_k=size_k, size_n=size_n, num_bits=8
            )
            tensor_list.append(marlin_qweight)

        return torch.cat([x.unsqueeze(0) for x in tensor_list], 0)

    w13_weight = repack_weight("w13", w13_weight)
    w2_weight = repack_weight("w2", w2_weight)

    # WEIGHT SCALES
    # Permute scales
    group_size = -1 if weight_block_size is None else weight_block_size[1]

    defpermute_scales(scales: torch.Tensor, name: str) -> torch.Tensor:
        scales = scales.to(layer.orig_dtype)
        tensor_list = []
        if "w13" in name:
            size_n, size_k = w13_n, k
        else:
            size_n, size_k = k, n

        # marlin kernel only support channel-wise and group-wise quantization
        # we need to convert the scales
        if weight_block_size is None:
            if scales.nelement() == e:
                # tensor-wise quantization -> channel-wise quantization
                # (e, 1, 1) =>(repeat)=> (e, 1, size_n)
                scales = scales.view(e, 1, 1).repeat_interleave(size_n, 2)
            elif scales.nelement() > e and scales.nelement() != e * size_n:
                assert (e * size_n) % scales.nelement() == 0
                s_size = scales.nelement() // e
                # tensor-wise quantization (for gate-up proj)
                #     -> channel-wise quantization
                # (e, 1, s_size) =>(repeat)=> (e, 1, size_n)
                scales = scales.view(e, 1, s_size)
                scales = scales.repeat_interleave(size_n // s_size, 2)
            else:
                # channel-wise quantization
                # (e, 1, size_n)
                scales = scales.view(e, 1, size_n)
        else:
            # block-wise quantization -> group-wise quantization
            # (e, size_k // block_size[1], ceil(size_n / block_size[0]))
            #  =>(repeat)=> (e, size_k // block_size[1], size_n)
            scales = scales.permute(0, 2, 1)
            block_n = weight_block_size[0]
            scales = scales.repeat_interleave(block_n, 2)
            # size_n may not divisible by block_size[0]
            scales = scales[..., :size_n].contiguous()

        for i in range(e):
            marlin_scales = marlin_permute_scales(
                s=scales[i], size_k=size_k, size_n=size_n, group_size=group_size
            )
            tensor_list.append(marlin_scales)

        scales = torch.cat([x.unsqueeze(0) for x in tensor_list], 0)
        if input_dtype != torch.float8_e4m3fn:
            scales = fp8_fused_exponent_bias_into_scales(scales)
        return scales

    w13_weight_scale = permute_scales(w13_weight_scale, "w13")
    w2_weight_scale = permute_scales(w2_weight_scale, "w2")

    return w13_weight, w2_weight, w13_weight_scale, w2_weight_scale
```