---
title: audioflamingo3 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/audioflamingo3/
source: sitemap
fetched_at: 2026-05-07T21:29:03.958856055-03:00
rendered_js: false
word_count: 0
summary: This document defines the AudioFlamingo3ForConditionalGeneration class, which integrates an audio encoder and a multimodal projector with a language model for conditional generation tasks.
tags:
    - multimodal
    - audio-processing
    - pytorch
    - vllm
    - model-architecture
    - encoder-decoder
category: api
---

```
@MULTIMODAL_REGISTRY.register_processor(
    AudioFlamingo3MultiModalProcessor,
    info=AudioFlamingo3ProcessingInfo,
    dummy_inputs=AudioFlamingo3DummyInputsBuilder,
)
classAudioFlamingo3ForConditionalGeneration(
    nn.Module, SupportsMultiModal, SupportsPP, SupportsLoRA
):
    packed_modules_mapping = {
        "qkv_proj": ["q_proj", "k_proj", "v_proj"],
        "gate_up_proj": ["gate_proj", "up_proj"],
    }

    defget_mm_mapping(self) -> MultiModelKeys:
"""
        Get the module prefix in multimodal models
        """
        return MultiModelKeys.from_string_field(
            language_model="language_model.",
            connector="multi_modal_projector.",
            tower_model="audio_tower.",
        )

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        config = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config
        multimodal_config = vllm_config.model_config.multimodal_config
        self.config = config
        self.multimodal_config = multimodal_config
        self.quant_config = quant_config

        with self._mark_tower_model(vllm_config, "audio"):
            self.audio_tower = AudioFlamingo3Encoder(
                config.audio_config,
            )
            self.multi_modal_projector = AudioFlamingo3MultiModalProjector(config)

        with self._mark_language_model(vllm_config):
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config,
                hf_config=config.text_config,
                prefix=maybe_prefix(prefix, "language_model"),
                architectures=["Qwen2ForCausalLM"],
            )

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

    def_parse_and_validate_audio_input(
        self, **kwargs: object
    ) -> AudioFlamingo3Inputs | None:
        input_features = kwargs.pop("input_features", None)
        audio_embeds = kwargs.pop("audio_embeds", None)
        feature_attention_mask = kwargs.pop("feature_attention_mask", None)
        chunk_counts = kwargs.pop("chunk_counts", None)

        if input_features is None and audio_embeds is None:
            return None

        if audio_embeds is not None:
            return AudioFlamingo3EmbeddingInputs(
                type="audio_embeds", audio_embeds=audio_embeds
            )

        if input_features is not None:
            return AudioFlamingo3FeatureInputs(
                type="audio_features",
                input_features=input_features,
                feature_attention_mask=feature_attention_mask,
                chunk_counts=chunk_counts,
            )

        raise AssertionError("This line should be unreachable.")

    def_process_audio_input(
        self, audio_input: AudioFlamingo3Inputs
    ) -> torch.Tensor | tuple[torch.Tensor, ...]:
        if audio_input["type"] == "audio_embeds":
            audio_embeds = audio_input["audio_embeds"]
            return tuple(audio_embeds)

        (
            input_features,
            feature_attention_mask,
            chunk_counts,
        ) = self._normalize_audio_feature_inputs(audio_input)
        audio_hidden_states = self._encode_audio_features(
            input_features,
            feature_attention_mask,
        )
        audio_features = self.multi_modal_projector(audio_hidden_states)
        return self._group_audio_embeddings(
            audio_features,
            feature_attention_mask,
            chunk_counts,
        )

    def_normalize_audio_feature_inputs(
        self, audio_input: AudioFlamingo3FeatureInputs
    ) -> tuple[torch.Tensor, torch.Tensor, list[int]]:
        input_features = audio_input["input_features"]
        feature_attention_mask = audio_input["feature_attention_mask"]
        chunk_counts = audio_input.get("chunk_counts")

        if isinstance(input_features, list):
            input_features = torch.cat(input_features, dim=0)
            feature_attention_mask = torch.cat(feature_attention_mask, dim=0)

        if chunk_counts is None:
            chunk_counts = [1] * input_features.shape[0]
        elif isinstance(chunk_counts, torch.Tensor):
            chunk_counts = chunk_counts.tolist()
        elif (
            isinstance(chunk_counts, list)
            and chunk_counts
            and isinstance(chunk_counts[0], torch.Tensor)
        ):
            chunk_counts = [count.item() for count in chunk_counts]

        return input_features, feature_attention_mask, chunk_counts

    def_encode_audio_features(
        self,
        input_features: torch.Tensor,
        feature_attention_mask: torch.Tensor,
    ) -> torch.Tensor:
        audio_attention_mask = _build_audio_encoder_attention_mask(
            feature_attention_mask,
            dtype=self.audio_tower.conv1.weight.dtype,
            device=self.audio_tower.conv1.weight.device,
        )

        return self.audio_tower(input_features, attention_mask=audio_attention_mask)

    def_group_audio_embeddings(
        self,
        audio_features: torch.Tensor,
        feature_attention_mask: torch.Tensor,
        chunk_counts: list[int],
    ) -> tuple[torch.Tensor, ...]:
        masked_audio_features, audio_output_lengths = _flatten_valid_audio_embeddings(
            audio_features,
            feature_attention_mask,
        )
        chunk_embeddings = torch.split(
            masked_audio_features,
            audio_output_lengths.tolist(),
        )

        grouped_embeddings = []
        current_idx = 0
        for count in chunk_counts:
            audio_chunks = chunk_embeddings[current_idx : current_idx + count]
            grouped_embeddings.append(torch.cat(audio_chunks, dim=0))
            current_idx += count
        return tuple(grouped_embeddings)

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
        audio_input = self._parse_and_validate_audio_input(**kwargs)
        if audio_input is None:
            return []
        masked_audio_features = self._process_audio_input(audio_input)
        return masked_audio_features

    defforward(
        self,
        input_ids: torch.Tensor,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
        **kwargs: object,
    ) -> torch.Tensor | IntermediateTensors:
        if intermediate_tensors is not None:
            inputs_embeds = None

        hidden_states = self.language_model.model(
            input_ids,
            positions,
            intermediate_tensors,
            inputs_embeds=inputs_embeds,
        )
        return hidden_states

    defcompute_logits(
        self,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor | None:
        return self.language_model.compute_logits(hidden_states)

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        loader = AutoWeightsLoader(self)
        return loader.load_weights(weights)
```