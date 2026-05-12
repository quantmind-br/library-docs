---
title: clip - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/clip/
source: sitemap
fetched_at: 2026-05-07T21:29:19.891653215-03:00
rendered_js: false
word_count: 10
summary: Defines the CLIPAttention class, a PyTorch module designed to handle parallelized multi-head attention mechanisms for CLIP-based text and vision configurations.
tags:
    - clip-attention
    - neural-networks
    - tensor-parallelism
    - model-architecture
    - pytorch-module
category: reference
---

```
classCLIPAttention(nn.Module):
    def__init__(
        self,
        config: CLIPTextConfig | CLIPVisionConfig,
        quant_config: QuantizationConfig | None = None,
        *,
        prefix: str = "",
        attn_cls: type[Attention] | type[MMEncoderAttention],
    ) -> None:
        super().__init__()

        self.config = config
        self.embed_dim = config.hidden_size
        self.num_heads = config.num_attention_heads
        self.head_dim = self.embed_dim // self.num_heads
        if self.head_dim * self.num_heads != self.embed_dim:
            raise ValueError(
                f"embed_dim must be divisible by num_heads "
                f"(got `embed_dim`: {self.embed_dim} and "
                f"`num_heads`: {self.num_heads})."
            )
        self.scale = self.head_dim**-0.5

        use_data_parallel = is_vit_use_data_parallel()
        self.qkv_proj = QKVParallelLinear(
            hidden_size=self.embed_dim,
            head_size=self.head_dim,
            total_num_heads=self.num_heads,
            quant_config=quant_config,
            prefix=f"{prefix}.qkv_proj",
            disable_tp=use_data_parallel,
        )

        self.out_proj = RowParallelLinear(
            input_size=self.embed_dim,
            output_size=self.embed_dim,
            quant_config=quant_config,
            prefix=f"{prefix}.out_proj",
            disable_tp=use_data_parallel,
        )

        self.tp_size = (
            1 if use_data_parallel else get_tensor_model_parallel_world_size()
        )
        self.num_heads_per_partition = divide(self.num_heads, self.tp_size)

        if attn_cls == MMEncoderAttention:
            self.attn = attn_cls(
                self.num_heads_per_partition,
                self.head_dim,
                self.scale,
                prefix=f"{prefix}.attn",
            )
        else:
            self.attn = attn_cls(
                self.num_heads_per_partition,
                self.head_dim,
                self.scale,
                prefix=f"{prefix}.attn",
            )

    defforward(
        self,
        hidden_states: torch.Tensor,
    ):
"""Input shape: Batch x Time x Channel"""

        qkv_states, _ = self.qkv_proj(hidden_states)
        query_states, key_states, value_states = qkv_states.chunk(3, dim=-1)
        out = self.attn(query_states, key_states, value_states)
        attn_output, _ = self.out_proj(out)

        return attn_output, None
```