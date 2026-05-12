---
title: qk_norm_rope_fusion - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/fusion/qk_norm_rope_fusion/
source: sitemap
fetched_at: 2026-05-07T21:16:29.034453228-03:00
rendered_js: false
word_count: 0
summary: This document defines a pattern matcher class designed to identify unfused attention block operations and replace them with optimized, fused QK-norm and RoPE operations in a PyTorch FX graph.
tags:
    - pytorch
    - graph-optimization
    - attention-mechanism
    - rope
    - rms-norm
    - pattern-matching
    - compiler-optimization
category: configuration
---

```
classQkNormRopePattern:
"""
    Match the unfused sequence in attention blocks and replace with the fused op.

    Unfused (conceptually):
      q, k, v = split(qkv, [qsz, kvsz, kvsz], -1)
      qh = reshape(q, [-1, num_heads, head_dim])
      kh = reshape(k, [-1, num_kv_heads, head_dim])
      qn = rms_norm(qh, q_weight, eps)
      kn = rms_norm(kh, k_weight, eps)
      qf = reshape(qn, [-1, num_heads * head_dim])
      kf = reshape(kn, [-1, num_kv_heads * head_dim])
      qf, kf = rotary_embedding(positions, qf, kf, head_dim, cos_sin_cache, is_neox)
      return qf, kf, v

    Fused replacement:
      fused_qk_norm_rope(qkv, num_heads, num_kv_heads, num_kv_heads, head_dim,
                         eps, q_weight, k_weight, cos_sin_cache, is_neox,
                         positions.view(-1))
      return split(qkv, [qsz, kvsz, kvsz], -1)
    """

    def__init__(
        self,
        head_dim: int,
        num_heads: int,
        num_kv_heads: int,
        eps: float,
        is_neox: bool,
        rope_flashinfer: bool = False,
    ) -> None:
        self.num_heads = num_heads
        self.num_kv_heads = num_kv_heads
        self.head_dim = head_dim
        self.q_size = self.num_heads * self.head_dim
        self.kv_size = self.num_kv_heads * self.head_dim
        self.eps = eps
        self.is_neox = is_neox
        self.rope_flashinfer = rope_flashinfer
        self.rope_matcher = MatcherRotaryEmbedding(
            is_neox=is_neox,
            head_size=self.head_dim,
            num_heads=self.num_heads,
            num_kv_heads=self.num_kv_heads,
            use_flashinfer=self.rope_flashinfer,
        )

    defget_inputs(self) -> list[torch.Tensor]:
        # Sample inputs to help pattern tracing
        T = 5
        qkv = empty_bf16(T, self.q_size + 2 * self.kv_size)
        positions = empty_i64(T)
        q_weight = empty_bf16(1, self.head_dim)
        k_weight = empty_bf16(1, self.head_dim)
        if self.rope_flashinfer:
            cos_sin_cache = empty_fp32(4096, self.head_dim)
        else:
            cos_sin_cache = empty_bf16(4096, self.head_dim)
        return [
            qkv,
            positions,
            q_weight,
            k_weight,
            cos_sin_cache,
        ]

    @staticmethod
    defwrap_trace_fn(
        trace_fn: Callable[P, fx.GraphModule],
        *process_fx_fns: Callable[[fx.GraphModule], None],
    ) -> Callable[P, fx.GraphModule]:
        defwrapped(*args: P.args, **kwargs: P.kwargs) -> fx.GraphModule:
            gm = trace_fn(*args, **kwargs)
            for process_fx in process_fx_fns:
                process_fx(gm)

            return gm

        return wrapped

    @staticmethod
    deffx_view_to_reshape(gm: torch.fx.GraphModule) -> None:
        fromtorch._inductor.fx_passes.post_gradimport view_to_reshape

        view_to_reshape(gm)

    defregister(self, pm_pass: PatternMatcherPass) -> None:
        defpattern(
            qkv: torch.Tensor,
            positions: torch.Tensor,
            q_weight: torch.Tensor,
            k_weight: torch.Tensor,
            cos_sin_cache: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
            # split qkv -> q,k,v
            q, k, v = qkv.split([self.q_size, self.kv_size, self.kv_size], dim=-1)

            # Q path: view -> RMS -> view back to q.shape
            q_by_head = q.view(
                *q.shape[:-1], q.shape[-1] // self.head_dim, self.head_dim
            )
            q_normed_by_head = vllm.ir.ops.rms_norm(q_by_head, q_weight, self.eps)
            q_flat = q_normed_by_head.view(q.shape)

            # K path: view -> RMS -> view back to k.shape
            k_by_head = k.view(
                *k.shape[:-1], k.shape[-1] // self.head_dim, self.head_dim
            )
            k_normed_by_head = vllm.ir.ops.rms_norm(k_by_head, k_weight, self.eps)
            k_flat = k_normed_by_head.view(k.shape)

            # RoPE: apply to flattened q/k
            q_rope, k_rope = self.rope_matcher(positions, q_flat, k_flat, cos_sin_cache)
            return q_rope, k_rope, v

        defreplacement(
            qkv: torch.Tensor,
            positions: torch.Tensor,
            q_weight: torch.Tensor,
            k_weight: torch.Tensor,
            cos_sin_cache: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
            # Run fused qk_norm_rope op
            result = auto_functionalized(
                FUSED_QK_ROPE_OP,
                qkv=qkv,
                num_heads_q=self.num_heads,
                num_heads_k=self.num_kv_heads,
                num_heads_v=self.num_kv_heads,
                head_dim=self.head_dim,
                eps=self.eps,
                q_weight=q_weight,
                k_weight=k_weight,
                cos_sin_cache=cos_sin_cache,
                is_neox=self.is_neox,
                position_ids=positions.view(-1),
                forced_token_heads_per_warp=-1,
            )
            result_qkv = result[1]

            # Split back to q,k,v and return
            return result_qkv.split([self.q_size, self.kv_size, self.kv_size], dim=-1)  # type: ignore[no-any-return]

        # NOTE: use fx_view_to_reshape to unify view/reshape to simplify
        # pattern and increase matching opportunities
        pm.register_replacement(
            pattern,
            replacement,
            self.get_inputs(),
            QkNormRopePattern.wrap_trace_fn(
                pm.fwd_only,
                QkNormRopePattern.fx_view_to_reshape,
            ),
            pm_pass,
        )
```