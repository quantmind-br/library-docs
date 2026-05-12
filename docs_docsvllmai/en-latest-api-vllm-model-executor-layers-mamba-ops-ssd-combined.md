---
title: ssd_combined - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/mamba/ops/ssd_combined/
source: sitemap
fetched_at: 2026-05-07T21:26:09.985503862-03:00
rendered_js: false
word_count: 0
summary: This document defines a Python function that performs a combined chunk-based scan operation for variable-length Mamba state space model sequences.
tags:
    - mamba
    - state-space-models
    - deep-learning
    - tensor-processing
    - variable-length-sequences
    - chunk-scan
category: api
---

```
defmamba_chunk_scan_combined_varlen(
    x,
    dt,
    A,
    B,
    C,
    chunk_size,
    cu_seqlens,
    cu_chunk_seqlens,
    last_chunk_indices,
    seq_idx,
    out,
    D=None,
    z=None,
    dt_bias=None,
    initial_states=None,
    dt_softplus=False,
    dt_limit=(0.0, float("inf")),
    return_intermediate_states=False,
    state_dtype=None,
):
"""
    Argument:
        x: (seqlen, nheads, headdim)
        dt: (seqlen, nheads)
        A: (nheads)
        B: (seqlen, ngroups, dstate)
        C: (seqlen, ngroups, dstate)
        chunk_size: int
        cu_seqlens: (batch + 1,)
        cu_chunk_seqlens: (nchunks + 1,)
        last_chunk_indices: (batch,)
        seq_idx: (nchunks,)
        out: (seqlen, nheads, headdim) preallocated output tensor
        D: (nheads, headdim) or (nheads,)
        z: (seqlen, nheads, headdim)
        dt_bias: (nheads,)
        initial_states: (batch, nheads, headdim, dstate)
        dt_softplus: Whether to apply softplus to dt
        out: (seqlen, nheads, headdim) preallocated output tensor
        state_dtype: The data type of the ssm state
    Return:
        varlen_states: (batch, nheads, headdim, dstate)
    """

    assert cu_seqlens is not None, "cu_seqlens must be provided assuming varlen input"
    assert seq_idx is not None

    varlen_states = _mamba_chunk_scan_combined_fwd(
        x,
        dt,
        A,
        B,
        C,
        chunk_size,
        out,
        D=D,
        z=z,
        dt_bias=dt_bias,
        initial_states=initial_states,
        return_intermediate_states=return_intermediate_states,
        seq_idx=seq_idx,
        cu_seqlens=cu_seqlens,
        cu_chunk_seqlens=cu_chunk_seqlens,
        last_chunk_indices=last_chunk_indices,
        dt_softplus=dt_softplus,
        dt_limit=dt_limit,
        state_dtype=state_dtype,
    )

    return varlen_states
```