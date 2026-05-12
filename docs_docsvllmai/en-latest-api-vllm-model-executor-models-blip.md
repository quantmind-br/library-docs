---
title: blip - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/blip/
source: sitemap
fetched_at: 2026-05-07T21:29:13.925262578-03:00
rendered_js: false
word_count: 19
summary: This document defines the BlipAttention PyTorch module, which implements multi-headed attention with support for tensor model parallelism and quantization configurations.
tags:
    - blip-model
    - multi-head-attention
    - pytorch-module
    - tensor-parallelism
    - model-architecture
category: api
---

```
classBlipAttention(nn.Module):
"""Multi-headed attention from 'Attention Is All You Need' paper"""

    def__init__(
        self,
        config: BlipVisionConfig | Blip2VisionConfig,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ) -> None:
        super().__init__()
        self.config = config
        self.embed_dim = config.hidden_size
        self.num_heads = config.num_attention_heads
        self.head_dim = self.embed_dim // self.num_heads
        if self.head_dim * self.num_heads != self.embed_dim:
            raise ValueError(
                "embed_dim must be divisible by num_heads "
                f"(got `embed_dim`: {self.embed_dim} and `num_heads`:"
                f" {self.num_heads})."
            )
        self.scale = self.head_dim**-0.5
        self.dropout = config.attention_dropout

        self.qkv = QKVParallelLinear(
            self.embed_dim,
            self.head_dim,
            self.num_heads,
            bias=config.qkv_bias,
            quant_config=quant_config,
            prefix=f"{prefix}.qkv",
        )
        self.projection = RowParallelLinear(
            self.embed_dim,
            self.embed_dim,
            quant_config=quant_config,
            prefix=f"{prefix}.projection",
        )

        self.tp_size = get_tensor_model_parallel_world_size()
        self.num_heads_per_partition = divide(self.num_heads, self.tp_size)

        self.attn = MMEncoderAttention(
            self.num_heads_per_partition,
            self.head_dim,
            self.scale,
            prefix=f"{prefix}.attn",
        )

    def_shape(self, tensor: torch.Tensor, seq_len: int, bsz: int):
        return (
            tensor.view(bsz, seq_len, self.num_heads, self.head_dim)
            .transpose(1, 2)
            .contiguous()
        )

    defforward(
        self,
        hidden_states: torch.Tensor,
    ):
"""Input shape: Batch x Time x Channel"""

        qkv_states, _ = self.qkv(hidden_states)
        query_states, key_states, value_states = qkv_states.chunk(3, dim=-1)
        out = self.attn(query_states, key_states, value_states)
        attn_output, _ = self.projection(out)

        return attn_output, None
```