---
title: ultravox - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/ultravox/
source: sitemap
fetched_at: 2026-05-07T21:33:41.126268538-03:00
rendered_js: false
word_count: 14
summary: This document defines the UltravoxModel class in PyTorch, which implements a multimodal model supporting audio processing, projection, and language model integration within the vLLM framework.
tags:
    - multimodal-model
    - vllm
    - audio-processing
    - pytorch
    - model-architecture
    - embedding-layer
category: reference
---

```
@MULTIMODAL_REGISTRY.register_processor(
    UltravoxMultiModalProcessor,
    info=UltravoxProcessingInfo,
    dummy_inputs=UltravoxDummyInputsBuilder,
)
classUltravoxModel(nn.Module, SupportsMultiModal, SupportsPP, SupportsLoRA):
    packed_modules_mapping = {
        "qkv_proj": ["q_proj", "k_proj", "v_proj"],
        "gate_up_proj": ["gate_proj", "up_proj"],
    }

    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={"audio_tower.model.encoder.": "audio_tower."}
    )

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("audio"):
            return "<|audio|>"

        raise ValueError("Only audio modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        config: UltravoxConfig = vllm_config.model_config.hf_config
        multimodal_config = vllm_config.model_config.multimodal_config
        self.config = config
        self.multi_modal_config = multimodal_config
        assert self.multi_modal_config

        self.configure_mm_token_handling(
            self.config.vocab_size,
            [self.config.audio_token_index],
        )

        self.secondary_weights = []
        if config.audio_model_id is not None:
            # this prefix is not for initialization, but for loading weights
            # note the trailing dot
            self.secondary_weights.append(
                DefaultModelLoader.Source(
                    model_or_path=config.audio_model_id,
                    revision=None,
                    prefix="audio_tower.",
                )
            )
        if config.text_model_id is not None:
            # this prefix is not for initialization, but for loading weights
            # note the trailing dot
            self.secondary_weights.append(
                DefaultModelLoader.Source(
                    model_or_path=config.text_model_id,
                    revision=None,
                    prefix="language_model.",
                )
            )

        with self._mark_tower_model(vllm_config, "audio"):
            self.audio_tower = ModifiedWhisperEncoder(config.audio_config)
            if config.num_projector_layers > 0:
                self.multi_modal_projector = UltravoxTransformerProjector(config)
            else:
                self.multi_modal_projector = UltravoxFeedForwardProjector(config)

        with self._mark_language_model(vllm_config):
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config,
                hf_config=config.wrapped_model_config,
                prefix=maybe_prefix(prefix, "language_model"),
            )

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

    defget_mm_mapping(self) -> MultiModelKeys:
"""
        Get the module prefix in multimodal models
        """
        return MultiModelKeys.from_string_field(
            language_model="language_model.",
            connector="multi_modal_projector.",
            tower_model="audio_tower.",
        )

    def_audio_features_to_embeddings(
        self,
        input_features: torch.Tensor,
        audio_lens: torch.Tensor,
        audio_token_len: torch.Tensor,
    ) -> torch.Tensor:
        audio_features = input_features.to(self.audio_tower.dtype)
        batch_size = audio_features.size(0)
        audio_embeddings = []

        # Process audio features in batches to keep memory usage predictable
        for start in range(0, batch_size, _MAX_ENCODER_BATCH_SIZE):
            end = min(start + _MAX_ENCODER_BATCH_SIZE, batch_size)
            # Process through audio tower
            batch_features = self.audio_tower(
                audio_features[start:end], audio_lens[start:end]
            )
            batch_features = batch_features.to(self.audio_tower.dtype)

            # Process through projector
            batch_embeddings = self.multi_modal_projector(
                batch_features, audio_token_len[start:end]
            )
            audio_embeddings.append(batch_embeddings)

        # Concatenate results
        audio_embeddings = torch.cat(audio_embeddings, dim=0)
        return audio_embeddings

    def_parse_and_validate_audio_input(
        self, **kwargs: object
    ) -> UltravoxAudioInputs | None:
        audio_features = kwargs.pop("audio_features", None)
        audio_embeds = kwargs.pop("audio_embeds", None)
        audio_lens = kwargs.pop("audio_lens", None)
        audio_token_len = kwargs.pop("audio_token_len", None)
        audio_num_chunks = kwargs.pop("audio_num_chunks", None)

        if audio_features is None and audio_embeds is None:
            return None

        if audio_features is not None:
            return UltravoxAudioFeatureInputs(
                type="audio_features",
                data=audio_features,
                lens=audio_lens,
                token_len=audio_token_len,
                num_chunks=audio_num_chunks,
            )

        if audio_embeds is not None:
            return UltravoxAudioEmbeddingInputs(type="audio_embeds", data=audio_embeds)

        raise AssertionError("This line should be unreachable.")

    def_process_audio_input(
        self,
        audio_input: UltravoxAudioInputs,
    ) -> NestedTensors | tuple[torch.Tensor, ...]:
        if audio_input["type"] == "audio_embeds":
            return audio_input["data"]

        # Pad and concatenate audio features
        # [[B1, 80, M1], [B2, 80, M2]] -> [B1+B2, 80, max(M1, M2)]
        audio_features = pad_and_concat_to_dim3(audio_input["data"])

        audio_lens = audio_input["lens"]
        audio_token_len = audio_input["token_len"]

        embeddings = self._audio_features_to_embeddings(
            audio_features, audio_lens, audio_token_len
        )

        # We should flatten and concatenate embeddings based on token lengths
        # For example, with token_len = [4, 2, 3], flattened_embeddings will be
        # concat(embeddings[0][:4], embeddings[1][:2], embeddings[2][:3])

        # Create a mask of valid indices based on token lengths
        max_len = embeddings.shape[1]
        indices = torch.arange(max_len, device=embeddings.device).expand(
            embeddings.shape[0], -1
        )
        mask = indices < audio_token_len[:, None]
        # Apply mask and flatten
        flattened_embeddings = embeddings[mask]

        # Return one tensor per input audio
        embed_lens = [
            chunk_lens.sum().item()
            for chunk_lens in audio_token_len.split(audio_input["num_chunks"].tolist())
        ]
        return flattened_embeddings.split(embed_lens)

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
        audio_input = self._parse_and_validate_audio_input(**kwargs)
        if audio_input is None:
            return []
        audio_embeddings = self._process_audio_input(audio_input)
        return audio_embeddings

    defembed_input_ids(
        self,
        input_ids: torch.Tensor,
        multimodal_embeddings: MultiModalEmbeddings | None = None,
        *,
        is_multimodal: torch.Tensor | None = None,
    ) -> torch.Tensor:
        # This is to satisfy the type checker for each overload
        if multimodal_embeddings is None or is_multimodal is None:
            return super().embed_input_ids(input_ids)

        return super().embed_input_ids(
            input_ids,
            multimodal_embeddings=multimodal_embeddings,
            is_multimodal=is_multimodal,
        )

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors: torch.Tensor | None = None,
        inputs_embeds: torch.Tensor | None = None,
        **kwargs,
    ) -> torch.Tensor | IntermediateTensors:
"""Run forward pass for Ultravox

        One key thing to understand is the `input_ids` already accounts for the
        positions of the to-be-inserted audio embeddings. The to-be-inserted
        audio has a size that is essentially 6.25 tokens per second of audio.

        This way, the `positions` and `attn_metadata` are consistent
        with the `input_ids`.

        Args:
            input_ids: Flattened (concatenated) input_ids corresponding to a
                batch.
            positions: Position indices for the input tokens.
            intermediate_tensors: Intermediate tensors from prior forward pass.
            inputs_embeds: Optional tensor of input embeddings.

        """

        if intermediate_tensors is not None:
            inputs_embeds = None

        language_model = self.language_model
        if hasattr(language_model, "language_model"):
            language_model = language_model.language_model

        hidden_states = language_model.model(
            input_ids, positions, intermediate_tensors, inputs_embeds=inputs_embeds
        )
        return hidden_states

    defcompute_logits(self, hidden_states: torch.Tensor) -> torch.Tensor:
        return self.language_model.compute_logits(hidden_states)

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        loader = AutoWeightsLoader(self, ignore_unexpected_prefixes=["audio_tower."])
        return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
```