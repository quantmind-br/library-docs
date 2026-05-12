---
title: minimax_qk_norm_fusion - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/fusion/minimax_qk_norm_fusion/
source: sitemap
fetched_at: 2026-05-07T21:16:26.921511275-03:00
rendered_js: false
word_count: 0
summary: This document defines a pattern matcher class that identifies specific QK normalization operations in a model and replaces them with a fused kernel for optimized execution.
tags:
    - pattern-matching
    - tensor-parallelism
    - kernel-fusion
    - optimization
    - pytorch-optimization
category: api
---

```
classMiniMaxQKNormPattern:
"""
    Match the forward_qk allreduce+rms pattern and replace with Lamport kernel.
    """

    def__init__(
        self,
        q_size: int,
        kv_size: int,
        eps: float,
        tp_world: int,
        tp_rank: int,
        max_tokens: int,
        dtype: torch.dtype,
        device: str | None,
    ) -> None:
        self.q_size = q_size
        self.kv_size = kv_size
        self.eps = eps
        self.tp_world = tp_world
        self.tp_rank = tp_rank
        self.max_tokens = max_tokens
        self.dtype = dtype
        self.device = device

    defget_inputs(self) -> list[torch.Tensor]:
        T = 4
        qkv = torch.empty(
            [T, self.q_size + 2 * self.kv_size],
            device=self.device,
            dtype=self.dtype,
        )
        q_weight = torch.empty([self.q_size], device=self.device, dtype=self.dtype)
        k_weight = torch.empty([self.kv_size], device=self.device, dtype=self.dtype)
        return [qkv, q_weight, k_weight]

    defregister(self, pm_pass: PatternMatcherPass) -> None:
        q_size = self.q_size
        kv_size = self.kv_size
        eps = self.eps
        tp_world = self.tp_world
        max_tokens = self.max_tokens
        tp_rank = self.tp_rank
        dtype = self.dtype

        defpattern(
            qkv: torch.Tensor,
            q_weight: torch.Tensor,
            k_weight: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
            q, k, v = qkv.split([q_size, kv_size, kv_size], dim=-1)
            q_fp32 = q.to(torch.float32)
            k_fp32 = k.to(torch.float32)
            q_var = q_fp32.pow(2).mean(dim=-1, keepdim=True)
            k_var = k_fp32.pow(2).mean(dim=-1, keepdim=True)
            qk_var = torch.cat([q_var, k_var], dim=-1)
            qk_var = tensor_model_parallel_all_reduce(qk_var) / tp_world
            q_var, k_var = qk_var.chunk(2, dim=-1)
            q_out = (q_fp32 * torch.rsqrt(q_var + eps) * q_weight).to(dtype)
            k_out = (k_fp32 * torch.rsqrt(k_var + eps) * k_weight).to(dtype)
            return q_out, k_out, v

        defreplacement(
            qkv: torch.Tensor,
            q_weight: torch.Tensor,
            k_weight: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
            assert _MINIMAX_QK_NORM_FUSED_OP is not None
            q_out, k_out = torch.ops.vllm.minimax_qk_norm_fused(
                qkv,
                q_weight,
                k_weight,
                q_size,
                kv_size,
                tp_rank,
                tp_world,
                eps,
                max_tokens,
            )
            _, _, v = qkv.split([q_size, kv_size, kv_size], dim=-1)
            return q_out, k_out, v

        pm.register_replacement(
            pattern, replacement, self.get_inputs(), pm.fwd_only, pm_pass
        )

        # Second pattern: three separate split_with_sizes nodes (one per output),
        # each with _users=1. This occurs when the QKV projection uses a
        # functional GEMM kernel (e.g. cutlass_scaled_mm via auto_functionalized),
        # which causes inductor to generate one split per consumer.
        defpattern_split3(
            qkv: torch.Tensor,
            q_weight: torch.Tensor,
            k_weight: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
            q = qkv.split([q_size, kv_size, kv_size], dim=-1)[0]
            k = qkv.split([q_size, kv_size, kv_size], dim=-1)[1]
            v = qkv.split([q_size, kv_size, kv_size], dim=-1)[2]
            q_fp32 = q.to(torch.float32)
            k_fp32 = k.to(torch.float32)
            q_var = q_fp32.pow(2).mean(dim=-1, keepdim=True)
            k_var = k_fp32.pow(2).mean(dim=-1, keepdim=True)
            qk_var = torch.cat([q_var, k_var], dim=-1)
            qk_var = tensor_model_parallel_all_reduce(qk_var) / tp_world
            q_var, k_var = qk_var.chunk(2, dim=-1)
            q_out = (q_fp32 * torch.rsqrt(q_var + eps) * q_weight).to(dtype)
            k_out = (k_fp32 * torch.rsqrt(k_var + eps) * k_weight).to(dtype)
            return q_out, k_out, v

        pm.register_replacement(
            pattern_split3, replacement, self.get_inputs(), pm.fwd_only, pm_pass
        )
```