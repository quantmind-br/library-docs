---
title: xpu_mla_sparse - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/attention/ops/xpu_mla_sparse/
source: sitemap
fetched_at: 2026-05-07T21:40:12.430095438-03:00
rendered_js: false
word_count: 0
summary: This document defines a Python interface for a Triton-based sparse Multi-Head Latent Attention (MLA) kernel, detailing the required tensor shapes, hardware constraints, and kernel invocation logic.
tags:
    - triton-kernel
    - sparse-attention
    - multi-head-latent-attention
    - deepseek-architecture
    - gpu-optimization
    - torch-extension
category: api
---

```
deftriton_bf16_mla_sparse_interface(
    q: torch.Tensor,  # [num_tokens, num_heads_q, dim_qk]
    kv: torch.Tensor,  # [num_tokens, num_heads_kv, dim_qk]
    indices: torch.Tensor,  # [num_tokens, num_heads_kv, topk]
    sm_scale: float,
    d_v: int = 512,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
"""
    out : [num_tokens, num_heads_q, d_v]
    max_logits : [num_tokens, num_heads_q]
    lse : logsumexp, [num_tokens, num_heads_q]
    """
    num_tokens, num_heads_q, dim_qk = q.shape
    _, num_heads_kv, _ = kv.shape
    assert dim_qk == kv.shape[2], "q and kv have different head dimensions"

    # for deepseek v3.2, index topk should be 2048
    _, _, index_topk = indices.shape

    BLOCK_H = 16
    BLOCK_DMODEL = 512
    BLOCK_DPE = 64
    BLOCK_M = 32
    BLOCK_N = 16
    BLOCK_DV = 512
    assert d_v == BLOCK_DV, "only support d_v = 512"

    assert dim_qk == BLOCK_DMODEL + BLOCK_DPE, (
        "dim_qk does not match BLOCK_DMODEL + BLOCK_DPE"
    )
    assert num_heads_kv == 1, "only support kv head = 1 for now"
    assert index_topk % BLOCK_N == 0, "index_topk must be multiple of BLOCK_N"

    sm_scale *= LOG2E

    kv_group_num = num_heads_q // num_heads_kv
    grid = (
        num_tokens,
        triton.cdiv(num_heads_q, min(BLOCK_H, kv_group_num)),
    )

    out = torch.zeros((num_tokens, num_heads_q, d_v), dtype=q.dtype, device=q.device)
    softmax_lse = torch.zeros(
        (num_tokens, num_heads_q), dtype=torch.float32, device=q.device
    )
    max_logits = torch.zeros(
        (num_tokens, num_heads_q), dtype=torch.float32, device=q.device
    )

    k = kv
    v = kv[..., :d_v]

    _bf16_mla_sparse_kernel[grid](
        q_buffer=q,
        k_buffer=k,
        v_buffer=v,
        indices_ptr=indices,
        out_ptr=out,
        softmax_lse_ptr=softmax_lse,
        max_logits_ptr=max_logits,
        seq_q=num_tokens,
        seq_kv=kv.shape[0],
        h_q=num_heads_q,
        dim_qk=dim_qk,
        dim_v=d_v,
        stride_q_token=q.stride(0),
        stride_q_head=q.stride(1),
        stride_k_token=k.stride(0),
        stride_k_head=k.stride(1),
        stride_v_token=v.stride(0),
        stride_v_head=v.stride(1),
        stride_out_token=out.stride(0),
        stride_out_head=out.stride(1),
        stride_lse=softmax_lse.stride(0),
        stride_indices_token=indices.stride(0),
        stride_indices_head=indices.stride(1),
        sm_scale=sm_scale,
        kv_group_num=kv_group_num,
        index_topk=index_topk,
        BLOCK_H=BLOCK_H,
        BLOCK_M=BLOCK_M,
        BLOCK_N=BLOCK_N,
        BLOCK_DV=BLOCK_DV,
        BLOCK_DMODEL=BLOCK_DMODEL,
        BLOCK_DPE=BLOCK_DPE,
        LOGE2=LOGE2,
    )

    return out, max_logits, softmax_lse
```