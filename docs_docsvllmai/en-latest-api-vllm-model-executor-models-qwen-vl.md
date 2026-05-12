---
title: qwen_vl - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/qwen_vl/
source: sitemap
fetched_at: 2026-05-07T21:33:08.163124958-03:00
rendered_js: false
word_count: 0
summary: This document defines a PyTorch module for a visual self-attention layer, providing the initialization and forward pass implementation for computing scaled dot-product attention.
tags:
    - pytorch
    - self-attention
    - neural-network
    - deep-learning
    - attention-mechanism
    - tensor-manipulation
category: api
---

```
classVisualAttention(nn.Module):
"""self-attention layer class.
    Self-attention layer takes input with size [s, b, h]
    and returns output of the same size.
    """

    def__init__(
        self,
        embed_dim: int,
        num_heads: int,
        bias: bool = True,
        kdim: int | None = None,
        vdim: int | None = None,
        prefix: str = "",
    ):
        super().__init__()
        self.embed_dim = embed_dim
        self.kdim = kdim if kdim is not None else embed_dim
        self.vdim = vdim if vdim is not None else embed_dim
        self._qkv_same_embed_dim = self.kdim == embed_dim and self.vdim == embed_dim

        self.num_heads = num_heads

        # Per attention head and per partition values.
        assert embed_dim % num_heads == 0
        self.hidden_size_per_attention_head = embed_dim // num_heads
        self.num_attention_heads_per_partition = num_heads
        self.hidden_size_per_partition = embed_dim

        # Strided linear layer.
        assert self._qkv_same_embed_dim, (
            "Visual Attention implementation only supports self-attention"
        )
        self.in_proj = ReplicatedLinear(
            embed_dim, 3 * embed_dim, prefix=f"{prefix}.in_proj"
        )
        self.out_proj = ReplicatedLinear(
            embed_dim, embed_dim, prefix=f"{prefix}.out_proj"
        )
        self.norm_factor = math.sqrt(self.hidden_size_per_attention_head)

    defforward(
        self,
        x: torch.Tensor,
        attn_mask: torch.Tensor | None = None,
    ) -> torch.Tensor:
        # query/key/value: [sq, b, h]
        sq, b, _ = x.size()
        mixed_x_layer, _ = self.in_proj(x)

        # [sq, b, (np * 3 * hn)] --> [sq, b, np, 3 * hn]
        new_tensor_shape = mixed_x_layer.size()[:-1] + (
            self.num_attention_heads_per_partition,
            3 * self.hidden_size_per_attention_head,
        )
        mixed_x_layer = mixed_x_layer.view(*new_tensor_shape)

        # [sq, b, np, 3 * hn] --> 3 [sq, b, np, hn]
        query_layer, key_layer, value_layer = mixed_x_layer.split(
            self.hidden_size_per_attention_head, dim=-1
        )

        # [sq, b, np, hn] -> [sq, b * np, hn]
        query_layer = query_layer.view(
            sq,
            b * self.num_attention_heads_per_partition,
            self.hidden_size_per_attention_head,
        ).transpose(0, 1)
        # [sk, b, np, hn] -> [sk, b * np, hn]
        key_layer = key_layer.view(
            sq,
            b * self.num_attention_heads_per_partition,
            self.hidden_size_per_attention_head,
        ).transpose(0, 1)

        q_scaled = query_layer / self.norm_factor
        if attn_mask is not None:
            attention_probs = torch.baddbmm(
                attn_mask, q_scaled, key_layer.transpose(-2, -1)
            )
        else:
            attention_probs = torch.bmm(q_scaled, key_layer.transpose(-2, -1))
        attention_probs = attention_probs.softmax(dim=-1)

        value_layer = value_layer.view(
            sq,
            b * self.num_attention_heads_per_partition,
            self.hidden_size_per_attention_head,
        ).transpose(0, 1)

        # matmul: [b * np, sq, hn]
        context_layer = torch.bmm(attention_probs, value_layer)

        # change view [b, np, sq, hn]
        context_layer = context_layer.view(
            b,
            self.num_attention_heads_per_partition,
            sq,
            self.hidden_size_per_attention_head,
        )

        # [b, np, sq, hn] --> [sq, b, np, hn]
        context_layer = context_layer.permute(2, 0, 1, 3).contiguous()

        # [sq, b, np, hn] --> [sq, b, hp]
        new_context_layer_shape = context_layer.size()[:-2] + (
            self.hidden_size_per_partition,
        )
        context_layer = context_layer.view(*new_context_layer_shape)

        output, _ = self.out_proj(context_layer)

        return output
```