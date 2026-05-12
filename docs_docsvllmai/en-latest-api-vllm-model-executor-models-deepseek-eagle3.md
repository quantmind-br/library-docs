---
title: deepseek_eagle3 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/deepseek_eagle3/
source: sitemap
fetched_at: 2026-05-07T21:29:35.935621996-03:00
rendered_js: false
word_count: 0
summary: This document defines the Eagle3 decoder layer implementation for the Deepseek model architecture, specifically handling input processing, Multi-Head Latent Attention (MLA), and MLP operations within a neural network framework.
tags:
    - deepseek
    - decoder-layer
    - model-architecture
    - neural-networks
    - multi-head-latent-attention
    - vllm
category: reference
---

```
classDeepseekV2Eagle3DecoderLayer(nn.Module):
"""
    Eagle3 decoder layer for Deepseek that:
    1. Always uses MLP (not MoE)
    2. First layer accepts concatenated embeds + hidden_states
    """

    def__init__(
        self,
        vllm_config: VllmConfig,
        prefix: str,
        config: DeepseekV2Config | DeepseekV3Config | None = None,
        layer_idx: int = 0,
    ) -> None:
        super().__init__()

        if config is None:
            config = vllm_config.model_config.hf_config
        cache_config = vllm_config.cache_config
        quant_config = get_draft_quant_config(vllm_config)

        self.hidden_size = config.hidden_size
        rope_scaling = getattr(config, "rope_scaling", None)
        max_position_embeddings = getattr(config, "max_position_embeddings", 8192)

        self.layer_idx = layer_idx

        # MLA attention parameters
        qk_nope_head_dim = getattr(config, "qk_nope_head_dim", 0)
        qk_rope_head_dim = getattr(config, "qk_rope_head_dim", 0)
        v_head_dim = getattr(config, "v_head_dim", 0)
        kv_lora_rank = getattr(config, "kv_lora_rank", 0)
        config = copy.copy(config)
        if rope_scaling:
            rope_params = rope_scaling.copy()
            rope_params["rope_type"] = "deepseek_yarn"
        else:
            rope_params = {"rope_type": "default"}
        config.rope_parameters = rope_params
        self.self_attn = DeepseekV2MLAAttention(
            vllm_config=vllm_config,
            config=config,
            hidden_size=self.hidden_size,
            num_heads=config.num_attention_heads,
            qk_nope_head_dim=qk_nope_head_dim,
            qk_rope_head_dim=qk_rope_head_dim,
            v_head_dim=v_head_dim,
            q_lora_rank=config.q_lora_rank if hasattr(config, "q_lora_rank") else None,
            kv_lora_rank=kv_lora_rank,
            max_position_embeddings=max_position_embeddings,
            cache_config=cache_config,
            quant_config=quant_config,
            prefix=f"{prefix}.self_attn",
            input_size=2 * self.hidden_size if layer_idx == 0 else self.hidden_size,
        )

        # Always use MLP (not MoE) for Eagle3
        self.mlp = DeepseekV2MLP(
            hidden_size=config.hidden_size,
            intermediate_size=config.intermediate_size,
            hidden_act=config.hidden_act,
            quant_config=quant_config,
            prefix=f"{prefix}.mlp",
        )

        self.input_layernorm = RMSNorm(config.hidden_size, eps=config.rms_norm_eps)
        self.post_attention_layernorm = RMSNorm(
            config.hidden_size, eps=config.rms_norm_eps
        )

        self.hidden_norm = RMSNorm(config.hidden_size, eps=config.rms_norm_eps)

        if getattr(config, "norm_before_residual", False):
            self._residual_norm = self._norm_before_residual
        else:
            self._residual_norm = self._norm_after_residual

    def_norm_before_residual(
        self, hidden_states: torch.Tensor
    ) -> tuple[torch.Tensor, torch.Tensor]:
        hidden_states = self.hidden_norm(hidden_states)
        residual = hidden_states
        return hidden_states, residual

    def_norm_after_residual(
        self, hidden_states: torch.Tensor
    ) -> tuple[torch.Tensor, torch.Tensor]:
        residual = hidden_states
        hidden_states = self.hidden_norm(hidden_states)
        return hidden_states, residual

    defforward(
        self,
        positions: torch.Tensor,
        embeds: torch.Tensor,
        hidden_states: torch.Tensor,
        residual: torch.Tensor | None,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        if self.layer_idx == 0:
            # First layer: concatenate embeds with hidden_states
            embeds = self.input_layernorm(embeds)
            hidden_states, residual = self._residual_norm(hidden_states=hidden_states)
            hidden_states = torch.cat([embeds, hidden_states], dim=-1)
        else:
            # Subsequent layers: process hidden_states and residuals only
            hidden_states, residual = self.input_layernorm(hidden_states, residual)

        # Self Attention
        hidden_states = self.self_attn(
            positions=positions,
            hidden_states=hidden_states,
            llama_4_scaling=None,
        )

        hidden_states, residual = self.post_attention_layernorm(hidden_states, residual)

        # Fully Connected (MLP, not MoE)
        hidden_states = self.mlp(hidden_states)

        return hidden_states, residual
```