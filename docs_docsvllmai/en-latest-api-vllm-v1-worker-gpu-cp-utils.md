---
title: cp_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/worker/gpu/cp_utils/
source: sitemap
fetched_at: 2026-05-07T21:42:21.212262393-03:00
rendered_js: false
word_count: 18
summary: This document describes the utility function used to populate the persistent sequence length buffer for distributed context parallelism in vLLM's GPU worker module.
tags:
    - vllm
    - cuda-graph
    - distributed-context-parallelism
    - gpu-worker
    - sequence-length
category: reference
---

## vllm.v1.worker.gpu.cp\_utils [¶](#vllm.v1.worker.gpu.cp_utils "Permanent link")

## prepare\_dcp\_local\_seq\_lens [¶](#vllm.v1.worker.gpu.cp_utils.prepare_dcp_local_seq_lens "Permanent link")

```
prepare_dcp_local_seq_lens(
    dcp_local_seq_lens: Tensor,
    seq_lens: Tensor,
    num_reqs: int,
    dcp_size: int,
    dcp_rank: int,
    cp_interleave: int,
) -> None
```

Populate the persistent DCP local seq\_lens buffer (CUDA graph safe).

Source code in `vllm/v1/worker/gpu/cp_utils.py`

```
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32

defprepare_dcp_local_seq_lens(
    dcp_local_seq_lens: torch.Tensor,
    seq_lens: torch.Tensor,
    num_reqs: int,
    dcp_size: int,
    dcp_rank: int,
    cp_interleave: int,
) -> None:
"""Populate the persistent DCP local seq_lens buffer (CUDA graph safe)."""
    if dcp_size == 1:
        return

    max_num_reqs = dcp_local_seq_lens.shape[0]
    BLOCK_SIZE = 128
    num_blocks = triton.cdiv(max_num_reqs, BLOCK_SIZE)
    _dcp_local_seq_lens_kernel[(num_blocks,)](
        dcp_local_seq_lens,
        seq_lens,
        dcp_size,
        dcp_rank,
        cp_interleave,
        num_reqs,
        max_num_reqs,
        BLOCK_SIZE,
    )
```