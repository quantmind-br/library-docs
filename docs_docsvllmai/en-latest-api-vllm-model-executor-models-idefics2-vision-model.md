---
title: idefics2_vision_model - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/idefics2_vision_model/
source: sitemap
fetched_at: 2026-05-07T21:30:51.67165913-03:00
rendered_js: false
word_count: 12
summary: This document defines the Idefics2VisionAttention class, which implements a multi-headed attention mechanism for vision models using PyTorch, including support for tensor model parallelism and scaled dot-product attention.
tags:
    - pytorch
    - attention-mechanism
    - neural-network
    - tensor-parallelism
    - vision-model
    - deep-learning
category: reference
---

```
classIdefics2VisionAttention(nn.Module):
"""Multi-headed attention from 'Attention Is All You Need' paper"""

    def__init__(
        self,
        config: Idefics2VisionConfig,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ) -> None:
        super().__init__()
        use_data_parallel = is_vit_use_data_parallel()
        self.config = config
        self.embed_dim = config.hidden_size
        self.num_heads = config.num_attention_heads
        self.head_dim = self.embed_dim // self.num_heads
        if self.head_dim * self.num_heads != self.embed_dim:
            raise ValueError(
                f"embed_dim must be divisible by num_heads (got `embed_dim`: {self.embed_dim} and `num_heads`:"  # noqa: E501
                f" {self.num_heads})."
            )
        self.scale = self.head_dim**-0.5
        self.dropout = config.attention_dropout

        tp_size = 1 if use_data_parallel else get_tensor_model_parallel_world_size()
        assert self.num_heads % tp_size == 0
        self.num_heads_per_partition = self.num_heads // tp_size

        self.qkv_proj = QKVParallelLinear(
            self.embed_dim,
            self.head_dim,
            self.num_heads,
            quant_config=quant_config,
            prefix=f"{prefix}.qkv_proj",
            disable_tp=use_data_parallel,
        )
        self.out_proj = RowParallelLinear(
            self.embed_dim,
            self.embed_dim,
            bias=True,
            quant_config=quant_config,
            prefix=f"{prefix}.out_proj",
            disable_tp=use_data_parallel,
        )
        # Use unified MMEncoderAttention with Flash Attention support
        self.attn = MMEncoderAttention(
            self.num_heads_per_partition,
            self.head_dim,
            self.scale,
            prefix=f"{prefix}.attn",
        )

    defforward(
        self,
        hidden_states: torch.Tensor,
        attention_mask: torch.Tensor | None = None,
    ) -> torch.Tensor:
        qkv, _ = self.qkv_proj(
            hidden_states
        )  # batch_size, q_len, 3 * num_heads_per_partition * head_dim
        query_states, key_states, value_states = qkv.chunk(3, dim=-1)

        # If attention_mask is provided, prefer Torch SDPA so the mask is
        # correctly applied (aligns with HuggingFace NaViT SigLIP behavior).
        if attention_mask is None:
            # Use unified MMEncoderAttention implementation
            out = self.attn(query_states, key_states, value_states)
        else:
            bsz, q_len = query_states.size()[:2]
            kv_len = key_states.size(1)

            query = query_states.view(
                bsz, q_len, self.num_heads_per_partition, self.head_dim
            ).transpose(1, 2)
            key = key_states.view(
                bsz, kv_len, self.num_heads_per_partition, self.head_dim
            ).transpose(1, 2)
            value = value_states.view(
                bsz, kv_len, self.num_heads_per_partition, self.head_dim
            ).transpose(1, 2)

            out = F.scaled_dot_product_attention(
                query,
                key,
                value,
                attn_mask=attention_mask,
                dropout_p=0.0,
                scale=self.scale,
            )
            out = out.transpose(1, 2).reshape(bsz, q_len, -1)
        attn_output, _ = self.out_proj(out)
        return attn_output
```