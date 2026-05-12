---
title: iquest_loopcoder - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/iquest_loopcoder/
source: sitemap
fetched_at: 2026-05-07T21:31:03.089081377-03:00
rendered_js: false
word_count: 0
summary: This component implements a gated projection mechanism for mixed attention in recurrent neural network architectures, calculating head-specific gating values to weight global versus local key-value caches.
tags:
    - neural-networks
    - attention-mechanism
    - tensor-parallelism
    - deep-learning
    - pytorch
    - vllm-architecture
category: api
---

```
classLoopGateProjection(nn.Module):
"""Gate projection for mixed attention in Loop 2+.

    Computes: g = sigmoid(linear(Q)) for each head independently.
    This gate determines how much to use Loop1's KV (global) vs current
    loop's KV (local).

    Supports tensor parallelism: each GPU handles a subset of heads.
    The weight matrix has shape [num_heads, head_dim] and is split along
    the head dimension.
    """

    def__init__(
        self,
        total_num_heads: int,
        head_dim: int,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ):
        super().__init__()
        self.total_num_heads = total_num_heads
        self.head_dim = head_dim
        tp_size = get_tensor_model_parallel_world_size()
        assert self.total_num_heads % tp_size == 0
        self.num_heads = self.total_num_heads // tp_size

        self.gate_proj = ColumnParallelLinear(
            head_dim,
            self.total_num_heads,
            bias=True,
            gather_output=False,
            quant_config=quant_config,
            prefix=f"{prefix}.gate_proj",
        )

    defforward(self, query: torch.Tensor) -> torch.Tensor:
"""Compute gate values from query tensor.

        Args:
            query: [num_heads, num_tokens, head_dim] (vLLM flattened format)
                where num_heads is the number of heads on this TP rank
                and num_tokens = batch * seq_len

        Returns:
            gate: [num_tokens, num_heads * head_dim] (flattened format matching q shape)
        """
        num_heads, num_tokens, head_dim = query.shape

        assert num_heads == self.num_heads, (
            f"Expected {self.num_heads} heads, got {num_heads}"
        )

        query_flat = query.reshape(-1, head_dim)

        gate_logits_flat, _ = self.gate_proj(query_flat)

        gate_logits = gate_logits_flat.reshape(
            num_heads, num_tokens, self.num_heads
        )  # [num_heads, num_tokens, num_heads]

        # Extract diagonal: each head h's query should use output column h
        # gate_logits[h, :, h] gives the output for head h at each token
        gate_logits = torch.diagonal(
            gate_logits, dim1=0, dim2=2
        )  # [num_tokens, num_heads]
        gate_logits = gate_logits.transpose(0, 1)  # [num_heads, num_tokens]
        gate_logits = gate_logits.unsqueeze(-1)  # [num_heads, num_tokens, 1]

        # Apply sigmoid
        gate = torch.sigmoid(gate_logits)  # [num_heads, num_tokens, 1]

        # Expand and reshape to match q shape: [num_tokens, num_heads * head_dim]
        gate = gate.transpose(0, 1)  # [num_tokens, num_heads, 1]
        gate = gate.expand(-1, -1, head_dim)  # [num_tokens, num_heads, head_dim]
        gate = gate.reshape(
            num_tokens, num_heads * head_dim
        )  # [num_tokens, num_heads * head_dim]

        return gate
```