---
title: gemma3n - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/gemma3n/
source: sitemap
fetched_at: 2026-05-07T21:30:12.882269193-03:00
rendered_js: false
word_count: 93
summary: This document defines the PyTorch modules for the Gemma3n model architecture, including implementations for Alternating Updates (AltUp), Cross-Decoder layers, and Learned Augmented Residual (Laurel) blocks.
tags:
    - gemma3n
    - vllm
    - neural-network-layers
    - altup
    - cross-decoder
    - laurel-block
    - pytorch-module
category: api
---

## Gemma3nAltUp [¶](#vllm.model_executor.models.gemma3n.Gemma3nAltUp "Permanent link")

Bases: `Module`

Alternating updates (Altup) The AltUp module wraps transformer layers. The `predict` step modifies the input to the transformer layer, and the `correct` step propagates the output of the transformer layer to the sparsely updated dimensions. See more in the research paper: https://proceedings.neurips.cc/paper\_files/paper/2023/file/f2059277ac6ce66e7e5543001afa8bb5-Paper-Conference.pdf

Source code in `vllm/model_executor/models/gemma3n.py`

```
classGemma3nAltUp(nn.Module):
"""Alternating updates (Altup)
    The AltUp module wraps transformer layers. The `predict` step modifies the
    input to the transformer layer, and the `correct` step propagates the output
    of the transformer layer to the sparsely updated dimensions.
    See more in the research paper:
    https://proceedings.neurips.cc/paper_files/paper/2023/file/f2059277ac6ce66e7e5543001afa8bb5-Paper-Conference.pdf
    """

    def__init__(
        self,
        hidden_size: int,
        rms_norm_eps: float,
        altup_num_inputs: int,
        altup_coef_clip: float,
        altup_active_idx: int,
        quant_config: QuantizationConfig,
        prefix: str,
    ):
        super().__init__()

        self.altup_num_inputs = altup_num_inputs
        self.altup_active_idx = altup_active_idx
        self.altup_coef_clip = altup_coef_clip

        self.correction_coefs = ReplicatedLinear(
            altup_num_inputs,
            altup_num_inputs,
            bias=False,
            quant_config=quant_config,
            prefix=f"{prefix}.correction_coefs",
            return_bias=False,
        )
        self.prediction_coefs = ReplicatedLinear(
            altup_num_inputs,
            altup_num_inputs**2,
            bias=False,
            quant_config=quant_config,
            prefix=f"{prefix}.prediction_coefs",
            return_bias=False,
        )
        self.modality_router = ReplicatedLinear(
            hidden_size,
            altup_num_inputs,
            bias=False,
            quant_config=quant_config,
            prefix=f"{prefix}.modality_router",
            return_bias=False,
        )
        self.router_norm = RMSNorm(
            hidden_size=hidden_size,
            eps=rms_norm_eps,
        )
        self.router_input_scale = torch.tensor(
            hidden_size**-1.0, dtype=self.modality_router.weight.dtype
        )
        self.correct_output_scale = nn.Parameter(
            torch.zeros(hidden_size, dtype=torch.float32)
        )

    def_compute_router_modalities(self, x: torch.Tensor) -> torch.Tensor:
        router_inputs = self.router_norm(x) * self.router_input_scale
        routed = self.modality_router(router_inputs)
        return torch.tanh(routed.float()).type_as(x)

    defscale_corrected_output(self, corrected: torch.Tensor) -> torch.Tensor:
        return (
            corrected.type_as(self.correct_output_scale) * self.correct_output_scale
        ).type_as(corrected)

    defpredict(self, hidden_states: torch.Tensor) -> torch.Tensor:
        # hidden:       [altup_num_inputs, num_tokens, hidden_size]
        # modalities:   [num_tokens, num_altup_inputs]
        # all_coefs:    [num_tokens, num_altup_inputs ** 2]
        modalities = self._compute_router_modalities(
            hidden_states[self.altup_active_idx]
        )
        all_coefs = self.prediction_coefs(modalities)

        # Reshape and transpose the 2D matrix for the matmul.
        # all_coefs_T:  [num_tokens, num_altup_inputs, num_altup_inputs]
        all_coefs_T = all_coefs.reshape(
            -1,
            self.altup_num_inputs,
            self.altup_num_inputs,
        ).permute(0, 2, 1)

        # hidden_states to [num_tokens, hidden_size, altup_num_inputs]
        predictions = torch.matmul(hidden_states.permute(1, 2, 0), all_coefs_T)
        # [altup_num_inputs, num_tokens, hidden_size]
        predictions = predictions.permute(2, 0, 1)
        predictions += hidden_states
        return predictions.contiguous()

    defcorrect(
        self, predictions: torch.Tensor, activated: torch.Tensor
    ) -> torch.Tensor:
        # predictions:  [altup_num_inputs, num_tokens, hidden_size]
        # activated:    [num_tokens, hidden_size]
        # modalities:   [num_tokens, altup_num_inputs]
        modalities = self._compute_router_modalities(activated)
        # innovation:   [num_tokens, altup_num_inputs]
        innovation = activated - predictions[self.altup_active_idx]
        # innovation:   [altup_num_inputs, num_tokens, hidden_size]
        innovation = innovation.repeat(self.altup_num_inputs, 1, 1)

        # Permute to [altup_num_inputs, num_tokens] as the last dim
        # is a scalar applied to each altup input and expand on
        # num_tokens dim for broadcastability over hidden_size.
        # all_coefs:    [num_tokens, altup_num_inputs]
        all_coefs = self.correction_coefs(modalities) + 1.0
        # all_coefs:    [altup_num_inputs, num_tokens, 1]
        all_coefs = all_coefs.T.unsqueeze(-1)

        # Elementwise (broadcast over hidden_size).
        corrected = torch.mul(innovation, all_coefs)
        corrected += predictions

        return corrected.contiguous()
```

## Gemma3nCrossDecoder [¶](#vllm.model_executor.models.gemma3n.Gemma3nCrossDecoder "Permanent link")

Bases: `Module`

Cross-decoder layers

Source code in `vllm/model_executor/models/gemma3n.py`

```
@support_torch_compile(
    enable_if=lambda vllm_config: vllm_config.cache_config.kv_sharing_fast_prefill
)
classGemma3nCrossDecoder(nn.Module):
"""
    Cross-decoder layers
    """

    def__init__(
        self,
        *,
        vllm_config: VllmConfig,
        prefix: str = "",
        decoder_layers: list[Gemma3nDecoderLayer],
        layer_idx_start: int,
    ):
        super().__init__()
        self.decoder_layers = decoder_layers
        self.layer_idx_start = layer_idx_start

    defforward(
        self,
        positions: torch.Tensor,
        hidden_states: torch.Tensor,
        per_layer_inputs: torch.Tensor,
        **kwargs,
    ) -> torch.Tensor:
        # [altnum_inputs, num_tokens, hidden_size]
        hidden_states = hidden_states.permute(2, 0, 1)
        for idx, layer in enumerate(self.decoder_layers):
            layer_idx = idx + self.layer_idx_start
            # [altup_num_inputs, num_tokens, hidden_size]
            hidden_states = layer(
                positions=positions,
                hidden_states=hidden_states,
                per_layer_input=per_layer_inputs[:, layer_idx, :],
                **kwargs,
            )
        # [num_tokens, hidden_size, altnum_inputs]
        hidden_states = hidden_states.permute(1, 2, 0)
        return hidden_states
```

## Gemma3nLaurelBlock [¶](#vllm.model_executor.models.gemma3n.Gemma3nLaurelBlock "Permanent link")

Bases: `Module`

Learned Augmented Residual Layer

Source code in `vllm/model_executor/models/gemma3n.py`

```
classGemma3nLaurelBlock(nn.Module):
"""Learned Augmented Residual Layer"""

    def__init__(
        self,
        hidden_size: int,
        laurel_rank: int,
        rms_norm_eps: float,
        *,
        quant_config: QuantizationConfig | None = None,
        prefix: str,
    ) -> None:
        super().__init__()

        self.linear_left = ColumnParallelLinear(
            hidden_size,
            laurel_rank,
            bias=False,
            quant_config=quant_config,
            prefix=f"{prefix}.linear_left",
            return_bias=False,
        )
        self.linear_right = RowParallelLinear(
            laurel_rank,
            hidden_size,
            bias=False,
            quant_config=quant_config,
            prefix=f"{prefix}.linear_right",
            return_bias=False,
        )
        self.post_laurel_norm = RMSNorm(
            hidden_size=hidden_size,
            eps=rms_norm_eps,
        )

    defforward(self, x: torch.Tensor) -> torch.Tensor:
        laurel_x = self.linear_left(x)
        laurel_x = self.linear_right(laurel_x)
        normed_laurel_x = self.post_laurel_norm(laurel_x)
        return x + normed_laurel_x
```

## Gemma3nSelfDecoder [¶](#vllm.model_executor.models.gemma3n.Gemma3nSelfDecoder "Permanent link")

Bases: `Module`

Includes altup embedding and self decoder layers

Source code in `vllm/model_executor/models/gemma3n.py`

```
@support_torch_compile(
    enable_if=lambda vllm_config: vllm_config.cache_config.kv_sharing_fast_prefill
)
classGemma3nSelfDecoder(nn.Module):
"""
    Includes altup embedding and self decoder layers
    """

    def__init__(
        self,
        *,
        vllm_config: VllmConfig,
        prefix: str = "",
        decoder_layers: list[Gemma3nDecoderLayer],
        layer_idx_start: int,
    ):
        super().__init__()
        self.decoder_layers = decoder_layers
        self.layer_idx_start = layer_idx_start

        config = vllm_config.model_config.hf_config
        self.config = config
        quant_config = vllm_config.quant_config

        self.embed_tokens = VocabParallelEmbedding(
            config.vocab_size,
            config.hidden_size,
            quant_config=quant_config,
            prefix=f"{prefix}.embed_tokens",
        )
        self.embed_scale = torch.tensor(
            config.hidden_size**0.5,
            dtype=self.embed_tokens.weight.dtype,
        )
        # Additional per-layer embeddings (PLE)
        self.embed_tokens_per_layer = VocabParallelEmbedding(
            config.vocab_size_per_layer_input,
            config.num_hidden_layers * config.hidden_size_per_layer_input,
            quant_config=quant_config,
            prefix=f"{prefix}.per_layer_embed_tokens",
        )
        self.embed_scale_per_layer = torch.tensor(
            config.hidden_size_per_layer_input**0.5,
            dtype=self.embed_tokens.weight.dtype,
        )
        self.per_layer_model_projection = ColumnParallelLinear(
            config.hidden_size,
            config.num_hidden_layers * config.hidden_size_per_layer_input,
            bias=False,
            gather_output=True,
            return_bias=False,
            quant_config=quant_config,
            prefix=f"{prefix}.per_layer_model_projection",
        )
        self.per_layer_projection_norm = RMSNorm(
            hidden_size=config.hidden_size_per_layer_input,
            eps=config.rms_norm_eps,
        )
        self.per_layer_input_scale = torch.rsqrt(torch.tensor(2.0)).to(
            self.embed_tokens.weight.dtype
        )
        self.per_layer_projection_scale = torch.tensor(
            config.hidden_size**0.5,
            dtype=self.embed_tokens.weight.dtype,
        )
        self.altup_projections = nn.ModuleList(
            [
                ColumnParallelLinear(
                    config.hidden_size,
                    config.hidden_size,
                    bias=False,
                    gather_output=True,
                    return_bias=False,
                    quant_config=quant_config,
                    prefix=f"{prefix}.altup_projections.{idx-1}",
                )
                for idx in range(1, self.config.altup_num_inputs)
            ]
        )

    defget_per_layer_input_embeddings(self, input_ids: torch.Tensor) -> torch.Tensor:
        # Deal with the fact that vocab_size_per_layer_input < vocab_size
        # which causes us to have some out of vocab tokens by setting
        # those token ids to 0. This matches the HF implementation.
        per_layer_inputs_mask = torch.logical_and(
            input_ids >= 0, input_ids < self.config.vocab_size_per_layer_input
        )
        per_layer_inputs_tokens = torch.where(
            per_layer_inputs_mask, input_ids, torch.zeros_like(input_ids)
        )
        return (
            self.embed_tokens_per_layer(per_layer_inputs_tokens)
            * self.embed_scale_per_layer
        )

    defget_per_layer_inputs(
        self,
        hidden_states_0: torch.Tensor,
        per_layer_inputs: torch.Tensor | None,
    ) -> torch.Tensor:
        per_layer_projection = self.per_layer_model_projection(hidden_states_0)
        per_layer_projection = per_layer_projection.reshape(
            *hidden_states_0.shape[:-1],
            self.config.num_hidden_layers,
            self.config.hidden_size_per_layer_input,
        )
        per_layer_projection = self.per_layer_projection_norm(per_layer_projection)
        if per_layer_inputs is not None:
            # Profiling run does not compute per_layer_inputs
            per_layer_inputs = per_layer_projection + per_layer_inputs
            per_layer_inputs *= self.per_layer_input_scale
        else:
            per_layer_inputs = per_layer_projection
        return per_layer_inputs

    defembed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
        return self.embed_tokens(input_ids) * self.embed_scale

    defaltup_embed(self, hidden_states_0: torch.Tensor) -> torch.Tensor:
        # Altup embed.
        hidden_states = [hidden_states_0] * self.config.altup_num_inputs
        target_magnitude = torch.mean(hidden_states_0**2, dim=-1, keepdim=True) ** 0.5
        for i in range(1, self.config.altup_num_inputs):
            hidden_states[i] = self.altup_projections[i - 1](hidden_states[i])
            new_magnitude = (
                torch.mean(hidden_states[i] ** 2, dim=-1, keepdim=True) ** 0.5
            )
            hidden_states[i] *= target_magnitude / torch.maximum(new_magnitude, EPS)
        hidden_states = torch.stack(hidden_states, dim=-1)
        return hidden_states

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        inputs_embeds: torch.Tensor | None = None,
        per_layer_inputs: torch.Tensor | None = None,
        **kwargs,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        if inputs_embeds is not None:
            hidden_states_0 = inputs_embeds
        else:
            hidden_states_0 = self.embed_input_ids(input_ids)

        adjusted_per_layer_inputs = self.get_per_layer_inputs(
            hidden_states_0, per_layer_inputs
        )
        hidden_states = self.altup_embed(hidden_states_0)

        # [altnum_inputs, num_tokens, hidden_size]
        hidden_states = hidden_states.permute(2, 0, 1)

        for idx, layer in enumerate(self.decoder_layers):
            layer_idx = idx + self.layer_idx_start
            # [altup_num_inputs, num_tokens, hidden_size]
            hidden_states = layer(
                positions=positions,
                hidden_states=hidden_states,
                per_layer_input=adjusted_per_layer_inputs[:, layer_idx, :],
                **kwargs,
            )

        # [num_tokens, hidden_size, altnum_inputs]
        hidden_states = hidden_states.permute(1, 2, 0)

        return hidden_states, adjusted_per_layer_inputs
```