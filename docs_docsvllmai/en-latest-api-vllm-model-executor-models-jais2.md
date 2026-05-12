---
title: jais2 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/jais2/
source: sitemap
fetched_at: 2026-05-07T21:31:06.315886904-03:00
rendered_js: false
word_count: 0
summary: This document defines the Jais2DecoderLayer class within a neural network architecture, implementing the attention mechanism, multilayer perceptron, and layer normalization components required for the forward pass.
tags:
    - neural-network
    - decoder-layer
    - attention-mechanism
    - pytorch
    - model-architecture
    - vllm
category: reference
---

```
classJais2DecoderLayer(nn.Module):
    def__init__(
        self,
        vllm_config: VllmConfig,
        config: Jais2Config,
        prefix: str = "",
    ) -> None:
        super().__init__()

        config = config or vllm_config.model_config.hf_config
        cache_config = vllm_config.cache_config
        quant_config = self.get_quant_config(vllm_config)

        self.hidden_size = config.hidden_size
        max_position_embeddings = getattr(config, "max_position_embeddings", 8192)
        # Support abacusai/Smaug-72B-v0.1 with attention_bias
        # Support internlm/internlm-7b with bias
        attention_bias = getattr(config, "attention_bias", False) or getattr(
            config, "bias", False
        )
        self.self_attn = Jais2Attention(
            config=config,
            hidden_size=self.hidden_size,
            num_heads=config.num_attention_heads,
            num_kv_heads=getattr(
                config, "num_key_value_heads", config.num_attention_heads
            ),
            max_position_embeddings=max_position_embeddings,
            quant_config=quant_config,
            bias=attention_bias,
            cache_config=cache_config,
            prefix=f"{prefix}.self_attn",
        )
        self.mlp = Jais2MLP(
            hidden_size=self.hidden_size,
            intermediate_size=config.intermediate_size,
            hidden_act=config.hidden_act,
            quant_config=quant_config,
            bias=getattr(config, "mlp_bias", False),
            prefix=f"{prefix}.mlp",
        )
        self.input_layernorm = nn.LayerNorm(
            config.hidden_size, eps=config.layer_norm_eps
        )
        self.post_attention_layernorm = nn.LayerNorm(
            config.hidden_size, eps=config.layer_norm_eps
        )

    defforward(
        self,
        positions: torch.Tensor,
        hidden_states: torch.Tensor,
        residual: torch.Tensor | None,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        # Self Attention
        if residual is None:
            residual = hidden_states
            hidden_states = self.input_layernorm(hidden_states)
        else:
            hidden_states, residual = (
                self.input_layernorm(hidden_states + residual),
                hidden_states + residual,
            )
        hidden_states = self.self_attn(
            positions=positions,
            hidden_states=hidden_states,
        )

        # Fully Connected
        hidden_states, residual = (
            self.post_attention_layernorm(hidden_states + residual),
            hidden_states + residual,
        )
        hidden_states = self.mlp(hidden_states)
        return hidden_states, residual

    defget_quant_config(self, vllm_config: VllmConfig) -> QuantizationConfig | None:
"""Get quantization config for this layer. Override in subclasses."""
        return vllm_config.quant_config
```