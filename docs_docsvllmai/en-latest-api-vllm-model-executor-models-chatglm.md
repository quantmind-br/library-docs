---
title: chatglm - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/chatglm/
source: sitemap
fetched_at: 2026-05-07T21:29:18.000293765-03:00
rendered_js: false
word_count: 82
summary: This document provides the technical implementation details for the ChatGLM transformer architecture, specifically detailing the structure of individual transformer layers, MLP blocks, and the overall transformer stack.
tags:
    - chatglm
    - transformer-architecture
    - neural-network-layers
    - vllm
    - mlp-block
    - deep-learning-models
category: reference
---

Inference-only ChatGLM model compatible with THUDM weights.

## GLMBlock [¶](#vllm.model_executor.models.chatglm.GLMBlock "Permanent link")

Bases: `Module`

A single transformer layer.

Transformer layer takes input with size \[s, b, h] and returns an output of the same size.

Source code in `vllm/model_executor/models/chatglm.py`

```
classGLMBlock(nn.Module):
"""A single transformer layer.

    Transformer layer takes input with size [s, b, h] and returns an
    output of the same size.
    """

    def__init__(
        self,
        config: ChatGLMConfig,
        cache_config: CacheConfig | None = None,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ):
        super().__init__()
        self.apply_residual_connection_post_layernorm = (
            config.apply_residual_connection_post_layernorm
        )

        self.fp32_residual_connection = config.fp32_residual_connection

        layer_norm_func = RMSNorm if config.rmsnorm else LayerNorm
        # Layernorm on the input data.
        self.input_layernorm = layer_norm_func(
            config.hidden_size, eps=config.layernorm_epsilon
        )

        # Self attention.
        self.self_attention = GLMAttention(
            config, cache_config, quant_config, prefix=f"{prefix}.self_attention"
        )
        self.hidden_dropout = config.hidden_dropout

        # Layernorm on the attention output
        self.post_attention_layernorm = layer_norm_func(
            config.hidden_size, eps=config.layernorm_epsilon
        )

        # MLP
        self.mlp = GLMMLP(config, quant_config, prefix=f"{prefix}.mlp")

    defforward(
        self,
        hidden_states: torch.Tensor,
        position_ids: torch.Tensor,
    ) -> torch.Tensor:
        # hidden_states: [num_tokens, h]
        # Layer norm at the beginning of the transformer layer.
        layernorm_output = self.input_layernorm(hidden_states)
        # Self attention.
        attention_output = self.self_attention(
            hidden_states=layernorm_output,
            position_ids=position_ids,
        )

        # Residual connection.
        if self.apply_residual_connection_post_layernorm:
            residual = layernorm_output
        else:
            residual = hidden_states

        layernorm_input = residual + attention_output

        # Layer norm post the self attention.
        layernorm_output = self.post_attention_layernorm(layernorm_input)

        # Second residual connection.
        if self.apply_residual_connection_post_layernorm:
            residual = layernorm_output
        else:
            residual = layernorm_input

        output = self.mlp(layernorm_output) + residual

        return output
```

## GLMMLP [¶](#vllm.model_executor.models.chatglm.GLMMLP "Permanent link")

Bases: `Module`

MLP.

MLP will take the input with h hidden state, project it to 4\*h hidden dimension, perform nonlinear transformation, and project the state back into h hidden dimension.

Source code in `vllm/model_executor/models/chatglm.py`

```
classGLMMLP(nn.Module):
"""MLP.

    MLP will take the input with h hidden state, project it to 4*h
    hidden dimension, perform nonlinear transformation, and project the
    state back into h hidden dimension.
    """

    def__init__(
        self,
        config: ChatGLMConfig,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ):
        super().__init__()

        self.add_bias = config.add_bias_linear

        # Project to 4h.
        self.dense_h_to_4h = MergedColumnParallelLinear(
            config.hidden_size,
            [config.ffn_hidden_size] * 2,
            bias=config.add_bias_linear,
            quant_config=quant_config,
            prefix=f"{prefix}.dense_h_to_4h",
        )

        self.activation_func = SiluAndMul()

        # Project back to h.
        self.dense_4h_to_h = RowParallelLinear(
            config.ffn_hidden_size,
            config.hidden_size,
            bias=config.add_bias_linear,
            quant_config=quant_config,
            prefix=f"{prefix}.dense_4h_to_h",
        )

    defforward(self, hidden_states):
        # [s, b, 4hp]
        intermediate_parallel, _ = self.dense_h_to_4h(hidden_states)
        intermediate_parallel = self.activation_func(intermediate_parallel)
        # [s, b, h]
        output, _ = self.dense_4h_to_h(intermediate_parallel)
        return output
```

## GLMTransformer [¶](#vllm.model_executor.models.chatglm.GLMTransformer "Permanent link")

Bases: `Module`

Transformer class.

Source code in `vllm/model_executor/models/chatglm.py`

```
classGLMTransformer(nn.Module):
"""Transformer class."""

    def__init__(
        self,
        config: ChatGLMConfig,
        cache_config: CacheConfig | None = None,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ):
        super().__init__()
        self.post_layer_norm = config.post_layer_norm

        # Number of layers.
        self.num_layers = config.num_layers

        # Transformer layers.
        self.start_layer, self.end_layer, self.layers = make_layers(
            self.num_layers,
            lambda prefix: GLMBlock(config, cache_config, quant_config, prefix=prefix),
            prefix=f"{prefix}.layers",
        )

        if self.post_layer_norm:
            layer_norm_func = RMSNorm if config.rmsnorm else LayerNorm
            # Final layer norm before output.
            self.final_layernorm = layer_norm_func(
                config.hidden_size, eps=config.layernorm_epsilon
            )

        self.make_empty_intermediate_tensors = make_empty_intermediate_tensors_factory(
            ["hidden_states"], config.hidden_size
        )

    defforward(
        self,
        hidden_states: torch.Tensor,
        position_ids: torch.Tensor,
    ) -> torch.Tensor | IntermediateTensors:
        for layer in islice(self.layers, self.start_layer, self.end_layer):
            hidden_states = layer(
                hidden_states=hidden_states, position_ids=position_ids
            )

        if not get_pp_group().is_last_rank:
            return IntermediateTensors({"hidden_states": hidden_states})

        # Final layer norm.
        if self.post_layer_norm:
            hidden_states = self.final_layernorm(hidden_states)

        return hidden_states
```