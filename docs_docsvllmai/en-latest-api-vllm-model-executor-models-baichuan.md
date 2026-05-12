---
title: baichuan - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/baichuan/
source: sitemap
fetched_at: 2026-05-07T21:29:07.003363552-03:00
rendered_js: false
word_count: 0
summary: This document defines the BaiChuanAttention module, which implements multi-headed attention with support for either ALiBi or rotary positional embeddings in a tensor-parallel configuration.
tags:
    - deep-learning
    - attention-mechanism
    - neural-networks
    - tensor-parallelism
    - baichuan-model
    - pytorch
category: concept
---

```
classBaiChuanAttention(nn.Module):
"""Multi-headed attention from 'Attention Is All You Need' paper"""

    def__init__(
        self,
        hidden_size: int,
        num_heads: int,
        position_embedding: str,
        rope_parameters: dict,
        max_position_embeddings: int = 8192,
        cache_config: CacheConfig | None = None,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ):
        super().__init__()
        self.hidden_size = hidden_size
        tensor_model_parallel_world_size = get_tensor_model_parallel_world_size()
        self.total_num_heads = num_heads
        assert self.total_num_heads % tensor_model_parallel_world_size == 0
        self.num_heads = self.total_num_heads // tensor_model_parallel_world_size
        self.head_dim = hidden_size // self.total_num_heads
        self.position_embedding = position_embedding
        self.max_position_embeddings = max_position_embeddings

        # pylint: disable=invalid-name
        self.W_pack = QKVParallelLinear(
            hidden_size,
            self.head_dim,
            self.total_num_heads,
            self.total_num_heads,
            bias=False,
            quant_config=quant_config,
            prefix=f"{prefix}.W_pack",
        )
        self.o_proj = RowParallelLinear(
            self.total_num_heads * self.head_dim,
            hidden_size,
            bias=False,
            quant_config=quant_config,
            prefix=f"{prefix}.o_proj",
        )
        # Create the alibi slopes and slice them.
        if self.position_embedding == "ALIBI":
            tp_rank = get_tensor_model_parallel_rank()
            head_start = tp_rank * self.num_heads
            head_end = (tp_rank + 1) * self.num_heads
            alibi_slopes = _get_alibi_slopes(self.total_num_heads)
            alibi_slopes = alibi_slopes[head_start:head_end].tolist()

            scaling = self.head_dim**-0.5
            self.attn = Attention(
                self.num_heads,
                self.head_dim,
                scaling,
                alibi_slopes=alibi_slopes,
                quant_config=quant_config,
                prefix=f"{prefix}.attn",
            )
        else:
            self.rotary_emb = get_rope(
                self.head_dim,
                max_position=self.max_position_embeddings,
                rope_parameters=rope_parameters,
            )
            self.scaling = self.head_dim**-0.5
            self.attn = Attention(
                self.num_heads,
                self.head_dim,
                self.scaling,
                cache_config=cache_config,
                quant_config=quant_config,
                prefix=f"{prefix}.attn",
            )

    defforward(
        self,
        positions: torch.Tensor,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor:
        qkv, _ = self.W_pack(hidden_states)
        q, k, v = qkv.chunk(chunks=3, dim=-1)
        if self.position_embedding != "ALIBI":
            q, k = self.rotary_emb(positions, q, k)
        attn_output = self.attn(q, k, v)
        output, _ = self.o_proj(attn_output)
        return output
```