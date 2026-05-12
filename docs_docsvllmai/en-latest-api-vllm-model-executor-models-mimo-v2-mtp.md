---
title: mimo_v2_mtp - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/mimo_v2_mtp/
source: sitemap
fetched_at: 2026-05-07T21:31:43.606302255-03:00
rendered_js: false
word_count: 0
summary: This document defines the MiMoV2MTPLayer class, which implements a single multi-token prediction predictor layer for the MiMo-V2 model architecture. It handles hidden state projection, attention mechanisms with sliding window functionality, and MLP processing within a transformer block.
tags:
    - deep-learning
    - transformer-architecture
    - multi-token-prediction
    - pytorch
    - neural-networks
    - attention-mechanism
category: reference
---

```
classMiMoV2MTPLayer(nn.Module):
"""Single MTP predictor layer for MiMo-V2 (Pro and Flash).

    Mirrors the single-layer MiMo-V2 nextn reference implementation.
    """

    def__init__(
        self,
        config: PretrainedConfig,
        prefix: str,
        quant_config: QuantizationConfig | None = None,
    ) -> None:
        super().__init__()

        # Predictor head components
        self.enorm = RMSNorm(config.hidden_size, eps=config.layernorm_epsilon)
        self.hnorm = RMSNorm(config.hidden_size, eps=config.layernorm_epsilon)
        self.eh_proj = ReplicatedLinear(
            config.hidden_size * 2, config.hidden_size, bias=False
        )

        # MTP uses the SWA attention configuration
        # implementation.
        swa_rope_theta = getattr(
            config,
            "swa_rope_theta",
            getattr(config, "rope_theta", 1000000),
        )
        sliding_window_size = getattr(config, "sliding_window_size", -1)

        self.input_layernorm = RMSNorm(config.hidden_size, eps=config.layernorm_epsilon)
        self.self_attn = MiMoV2Attention(
            hidden_size=config.hidden_size,
            num_heads=config.swa_num_attention_heads,
            num_kv_heads=config.swa_num_key_value_heads,
            head_dim=config.swa_head_dim,
            v_head_dim=getattr(config, "swa_v_head_dim", None),
            v_scale=getattr(config, "attention_value_scale", None),
            sliding_window_size=sliding_window_size,
            attention_bias=config.attention_bias,
            add_swa_attention_sink_bias=getattr(
                config, "add_swa_attention_sink_bias", False
            ),
            layer_id=0,
            rope_theta=swa_rope_theta,
            max_position_embeddings=getattr(config, "max_position_embeddings", 32768),
            quant_config=quant_config,
            partial_rotary_factor=getattr(config, "partial_rotary_factor", 1.0),
            prefix=f"{prefix}.self_attn",
        )
        self.pre_mlp_layernorm = RMSNorm(
            config.hidden_size, eps=config.layernorm_epsilon
        )
        self.mlp = MiMoV2MLP(
            hidden_size=config.hidden_size,
            intermediate_size=config.intermediate_size,
            hidden_act=config.hidden_act,
            quant_config=quant_config,
            prefix=f"{prefix}.mlp",
        )
        self.final_layernorm = RMSNorm(config.hidden_size, eps=config.layernorm_epsilon)

    defforward(
        self,
        inputs_embeds: torch.Tensor,
        positions: torch.Tensor,
        previous_hidden_states: torch.Tensor,
    ) -> torch.Tensor:
        # Combine token embedding and previous hidden state
        h, _ = self.eh_proj(
            torch.cat(
                [self.enorm(inputs_embeds), self.hnorm(previous_hidden_states)], dim=-1
            )
        )

        # Transformer block with fused residual norms
        residual = h
        h = self.input_layernorm(h)
        h = self.self_attn(positions=positions, hidden_states=h)
        h, residual = self.pre_mlp_layernorm(h, residual)
        h = self.mlp(h)
        h = h + residual

        return self.final_layernorm(h)
```