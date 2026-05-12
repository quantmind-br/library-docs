---
title: intern_vit - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/intern_vit/
source: sitemap
fetched_at: 2026-05-07T21:30:56.001107138-03:00
rendered_js: false
word_count: 12
summary: This document defines a PyTorch module for parallel multi-headed attention, supporting tensor model parallelism and optional query-key normalization for deep learning models.
tags:
    - deep-learning
    - pytorch
    - multi-head-attention
    - tensor-parallelism
    - neural-network-layers
category: api
---

```
classInternParallelAttention(nn.Module):
"""Multi-headed attention from 'Attention Is All You Need' paper"""

    def__init__(
        self,
        config: PretrainedConfig,
        quant_config: QuantizationConfig | None = None,
        *,
        num_dummy_heads: int = 0,
        prefix: str = "",
    ) -> None:
        super().__init__()

        self.config = config
        self.embed_dim = config.hidden_size
        self.num_heads = config.num_attention_heads
        self.head_dim = self.embed_dim // self.num_heads
        if self.head_dim * self.num_heads != self.embed_dim:
            raise ValueError(
                f"embed_dim must be divisible by num_heads "
                f"(got `embed_dim`: {self.embed_dim} and `num_heads`:"
                f" {self.num_heads})."
            )

        use_data_parallel = is_vit_use_data_parallel()
        # if the number of heads is not divisible by tp_size,
        # we also disable Attention's TP
        tp_size = 1 if use_data_parallel else get_tensor_model_parallel_world_size()
        use_data_parallel = (
            use_data_parallel or (self.num_heads + num_dummy_heads) % tp_size != 0
        )
        self.tp_size = 1 if use_data_parallel else tp_size
        self.tp_rank = 0 if use_data_parallel else get_tensor_model_parallel_rank()

        # Additional dummy heads are used to enable TP for common GPU counts.
        self.dummy_dim = (num_dummy_heads + self.num_heads) * self.head_dim
        self.num_heads_per_partition = divide(
            num_dummy_heads + self.num_heads, self.tp_size
        )

        self.scale = self.head_dim**-0.5
        self.qkv = QKVParallelLinear(
            self.embed_dim,
            self.head_dim,
            num_dummy_heads + self.num_heads,
            bias=config.qkv_bias,
            quant_config=quant_config,
            prefix=f"{prefix}.qkv",
            disable_tp=use_data_parallel,
        )

        self.qk_normalization = config.qk_normalization

        if self.qk_normalization:
            self.q_norm = RMSNorm(
                self.dummy_dim,
                eps=config.layer_norm_eps,
                var_hidden_size=self.embed_dim,
            )
            self.k_norm = RMSNorm(
                self.dummy_dim,
                eps=config.layer_norm_eps,
                var_hidden_size=self.embed_dim,
            )

        self.proj = RowParallelLinear(
            self.dummy_dim,
            self.embed_dim,
            quant_config=quant_config,
            prefix=f"{prefix}.proj",
            disable_tp=use_data_parallel,
        )

        self.attn = MMEncoderAttention(
            self.num_heads_per_partition,
            self.head_dim,
            self.scale,
            prefix=f"{prefix}.attn",
        )

    def_apply_qk_norm(self, q: torch.Tensor, k: torch.Tensor):
        if self.tp_size > 1:
            q = tensor_model_parallel_all_gather(q.contiguous())
            k = tensor_model_parallel_all_gather(k.contiguous())
        q = self.q_norm(q)
        k = self.k_norm(k)
        if self.tp_size > 1:
            splitter = partial(split_tensor_along_last_dim, num_partitions=self.tp_size)
            q = splitter(q)[self.tp_rank]
            k = splitter(k)[self.tp_rank]
        return q, k

    defforward(self, x: torch.Tensor) -> torch.Tensor:
        B, N, _ = x.shape
        qkv, _ = self.qkv(x)
        q, k, v = qkv.chunk(3, dim=-1)

        if self.qk_normalization:
            q, k = self._apply_qk_norm(q, k)

        out = self.attn(q, k, v)
        out, _ = self.proj(out)
        return out
```