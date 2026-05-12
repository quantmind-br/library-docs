---
title: deepencoder2 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/deepencoder2/
source: sitemap
fetched_at: 2026-05-07T21:29:34.142764096-03:00
rendered_js: false
word_count: 0
summary: This document defines a custom Qwen2 decoder implementation that integrates non-causal and causal attention mechanisms via custom token type identification and attention mask generation.
tags:
    - qwen2
    - transformer-models
    - attention-mechanisms
    - custom-decoder
    - mask-generation
    - deep-learning
    - pytorch
category: api
---

```
@PluggableLayer.register("qwen2_decoder")
classCustomQwen2Decoder(PluggableLayer):
"""
    Qwen2 visual encoder
    non-causal attention + causal attention
    token_type_ids ：0=non-causal, 1=causal
    """

    # --8<-- [end:qwen2_decoder]

    def__init__(
        self,
        decoder_layer: int = 24,
        max_position_embeddings: int = 131072,
        hidden_dimension: int = 896,
        num_attention_heads: int = 14,
        num_key_value_heads: int = 2,
        intermediate_size: int = 4864,
        vocab_size: int = 151936,
        attn_implementation: str = "sdpa",
        rms_norm_eps: float = 1e-06,
        rope_theta: float = 1000000.0,
        attention_dropout: float = 0.0,
        hidden_act: str = "silu",
        initializer_range: float = 0.02,
    ):
        super().__init__()

        # load
        Qwen2Model = transformers.models.qwen2.modeling_qwen2.Qwen2Model
        Qwen2Config = transformers.Qwen2Config

        # config
        config = Qwen2Config(
            hidden_size=hidden_dimension,
            num_hidden_layers=decoder_layer,
            num_attention_heads=num_attention_heads,
            num_key_value_heads=num_key_value_heads,
            intermediate_size=intermediate_size,
            max_position_embeddings=max_position_embeddings,
            vocab_size=vocab_size,
            rms_norm_eps=rms_norm_eps,
            rope_theta=rope_theta,
            attention_dropout=attention_dropout,
            hidden_act=hidden_act,
            initializer_range=initializer_range,
            _attn_implementation=attn_implementation,  # ⭐
        )

        #
        self.model = self._create_custom_model(Qwen2Model, config)

        del self.model.embed_tokens

    def_create_custom_model(self, Qwen2Model, config):
"""Qwen2Model"""

        classCustomQwen2ModelInner(Qwen2Model):
            defforward(
                self,
                input_ids=None,
                attention_mask=None,
                position_ids=None,
                past_key_values=None,
                inputs_embeds=None,
                token_type_ids=None,  # ⭐
                use_cache=None,
                output_attentions=None,
                output_hidden_states=None,
                return_dict=None,
                cache_position=None,
            ):
                # token_type_ids
                self._current_token_type_ids = token_type_ids
                causal_mask_mapping = {
                    "full_attention": self._update_causal_mask(
                        attention_mask,
                        inputs_embeds,
                        cache_position,
                        past_key_values,
                        output_attentions,
                    )
                }
                outputs = super().forward(
                    input_ids=input_ids,
                    attention_mask=causal_mask_mapping,
                    position_ids=position_ids,
                    past_key_values=past_key_values,
                    inputs_embeds=inputs_embeds,
                    use_cache=use_cache,
                    output_attentions=output_attentions,
                    output_hidden_states=output_hidden_states,
                    return_dict=return_dict,
                    cache_position=cache_position,
                )

                return outputs

            def_update_causal_mask(
                self,
                attention_mask,
                input_tensor,
                cache_position,
                past_key_values,
                output_attentions,
            ):
                dtype, device = input_tensor.dtype, input_tensor.device
                min_dtype = torch.finfo(dtype).min
                batch_size, sequence_length = (
                    input_tensor.shape[0],
                    input_tensor.shape[1],
                )

                token_type_ids = self._current_token_type_ids

                # attention mask
                causal_mask = self._create_custom_4d_mask(
                    sequence_length=sequence_length,
                    dtype=dtype,
                    device=device,
                    batch_size=batch_size,
                    token_type_ids=token_type_ids,
                )

                #  padding mask
                if attention_mask is not None and attention_mask.dim() == 2:
                    padding_mask = attention_mask[:, None, None, :].to(dtype=dtype)
                    padding_mask = (1.0 - padding_mask) * min_dtype
                    causal_mask = causal_mask + padding_mask

                return causal_mask

            def_create_custom_4d_mask(
                self,
                sequence_length,
                dtype,
                device,
                batch_size,
                token_type_ids,
            ):
                min_dtype = torch.finfo(dtype).min

                masks = []
                for b in range(batch_size):
                    mask = torch.full(
                        (sequence_length, sequence_length),
                        fill_value=min_dtype,
                        dtype=dtype,
                        device=device,
                    )

                    type_ids = token_type_ids[b]

                    image_positions = (type_ids == 0).nonzero(as_tuple=True)[0]
                    text_positions = (type_ids == 1).nonzero(as_tuple=True)[0]

                    # non-casual
                    if len(image_positions) > 0:
                        mask[image_positions[:, None], image_positions] = 0.0

                    # causal
                    for i, text_pos in enumerate(text_positions):
                        if len(image_positions) > 0:
                            mask[text_pos, image_positions] = 0.0
                        mask[text_pos, text_positions[: i + 1]] = 0.0

                    masks.append(mask)

                mask = torch.stack(masks, dim=0).unsqueeze(1)
                return mask

        return CustomQwen2ModelInner(config)

    defforward(
        self,
        inputs_embeds: torch.Tensor,
        token_type_ids: torch.Tensor,
        attention_mask: torch.Tensor = None,
        **kwargs,
    ):
"""
        Args:
            inputs_embeds: [batch_size, seq_len, hidden_dim]
            token_type_ids: [batch_size, seq_len], 0=non-causal, 1=causal
            attention_mask: [batch_size, seq_len], optional
        """
        return self.model(
            inputs_embeds=inputs_embeds,
            token_type_ids=token_type_ids,
            attention_mask=attention_mask,
            **kwargs,
        )
```