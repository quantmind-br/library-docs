---
title: minicpmo - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/minicpmo/
source: sitemap
fetched_at: 2026-05-07T21:31:47.968693713-03:00
rendered_js: false
word_count: 0
summary: This document defines the MiniCPMOBaseModel class, which extends multimodal capabilities to handle audio inputs, including audio feature extraction, encoder integration, and attention masking strategies.
tags:
    - minicpm
    - multimodal-models
    - audio-processing
    - feature-extraction
    - attention-masking
    - pytorch
category: concept
---

```
classMiniCPMOBaseModel:
"""Base mixin class for MiniCPM-O models with audio support."""

    packed_modules_mapping = {
        "qkv_proj": [
            "q_proj",
            "k_proj",
            "v_proj",
        ],
        "gate_up_proj": [
            "gate_proj",
            "up_proj",
        ],
    }

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return "(<image>./</image>)"
        if modality.startswith("video"):
            return "(<video>./</video>)"
        if modality.startswith("audio"):
            return "(<audio>./</audio>)"

        raise ValueError("Only image, video or audio modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__(vllm_config=vllm_config, prefix=prefix)

        with self._mark_tower_model(vllm_config, "audio"):
            self.apm = self.init_audio_module(
                vllm_config=vllm_config, prefix=maybe_prefix(prefix, "apm")
            )

    definit_audio_module(self, *, vllm_config: VllmConfig, prefix: str = ""):
        # Do not use parameters temporarily
        audio_config = self.config.audio_config
        model = MiniCPMWhisperEncoder(audio_config)
        audio_output_dim = int(audio_config.encoder_ffn_dim // 4)
        self.audio_avg_pooler = nn.AvgPool1d(
            self.config.audio_pool_step, stride=self.config.audio_pool_step
        )
        self.audio_projection_layer = MultiModalProjector(
            in_dim=audio_output_dim, out_dim=self.embed_dim
        )
        self.audio_encoder_layer = -1
        return model

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        loader = AutoWeightsLoader(self, skip_prefixes=["tts"])
        return loader.load_weights(weights)

    defsubsequent_chunk_mask(
        self,
        size: int,
        chunk_size: int,
        num_left_chunks: int = -1,
        device: torch.device = CPU_DEVICE,
        num_lookhead: int = 0,
    ) -> torch.Tensor:
        ret = torch.zeros(size, size, device=device, dtype=torch.bool)
        # Vectorized computation of row indices and chunk boundaries
        row_indices = torch.arange(size, device=device)
        chunk_indices = row_indices // chunk_size
        if num_left_chunks < 0:
            # If num_left_chunks < 0, start is always 0 for all rows
            start_indices = torch.zeros_like(row_indices)
        else:
            # Compute start indices vectorially
            start_chunk_indices = torch.clamp(chunk_indices - num_left_chunks, min=0)
            start_indices = start_chunk_indices * chunk_size
        # Compute ending indices vectorially
        end_chunk_indices = chunk_indices + 1
        end_indices = torch.clamp(
            end_chunk_indices * chunk_size + num_lookhead, max=size
        )
        # Create column indices for broadcasting
        col_indices = torch.arange(size, device=device).unsqueeze(0)
        start_indices = start_indices.unsqueeze(1)
        end_indices = end_indices.unsqueeze(1)
        # Vectorized mask creation
        ret = (col_indices >= start_indices) & (col_indices < end_indices)
        return ret

    def_get_feat_extract_output_lengths(self, input_lengths: torch.LongTensor):
        input_lengths_after_cnn = (input_lengths - 1) // 2 + 1
        input_lengths_after_pooling = (
            input_lengths_after_cnn - self.config.audio_pool_step
        ) // self.config.audio_pool_step + 1
        input_lengths_after_pooling = input_lengths_after_pooling.to(dtype=torch.int32)

        return input_lengths_after_cnn, input_lengths_after_pooling

    defget_audio_hidden_states(
        self, data: MiniCPMOAudioFeatureInputs
    ) -> list[torch.Tensor]:
        chunk_length = self.config.audio_chunk_length

        # (bs, 80, frames) or [], multi audios need filled in advance
        wavforms_raw = data["audio_features"]
        if isinstance(wavforms_raw, list):
            B = len(wavforms_raw)
            C = wavforms_raw[0].shape[-2]
            L = max(item.shape[-1] for item in wavforms_raw)
            device = wavforms_raw[0].device
            dtype = wavforms_raw[0].dtype

            wavforms = torch.zeros((B, C, L), dtype=dtype, device=device)
            for i, wavforms_item in enumerate(wavforms_raw):
                L_item = wavforms_item.shape[-1]
                wavforms[i, ..., :L_item] = wavforms_item
        else:
            wavforms = wavforms_raw

        # list, [[x1, x2], [y1], [z1]]
        audio_feature_lens_raw = data["audio_feature_lens"]
        if isinstance(audio_feature_lens_raw, torch.Tensor):
            audio_feature_lens_raw = audio_feature_lens_raw.unbind(0)

        audio_feature_lens = torch.hstack(audio_feature_lens_raw)
        batch_size, _, max_mel_seq_len = wavforms.shape
        max_seq_len = (max_mel_seq_len - 1) // 2 + 1

        # Create a sequence tensor of shape (batch_size, max_seq_len)
        seq_range = (
            torch.arange(
                0,
                max_seq_len,
                dtype=audio_feature_lens.dtype,
                device=audio_feature_lens.device,
            )
            .unsqueeze(0)
            .expand(batch_size, max_seq_len)
        )
        lengths_expand = audio_feature_lens.unsqueeze(1).expand(batch_size, max_seq_len)
        # Create mask
        padding_mask = seq_range >= lengths_expand  # 1 for padded values

        audio_attention_mask_ = padding_mask.view(batch_size, 1, 1, max_seq_len).expand(
            batch_size, 1, max_seq_len, max_seq_len
        )
        audio_attention_mask = audio_attention_mask_.to(
            dtype=self.apm.conv1.weight.dtype, device=self.apm.conv1.weight.device
        )

        if chunk_length > 0:
            chunk_num_frame = int(chunk_length * 50)
            chunk_mask = self.subsequent_chunk_mask(
                size=max_seq_len,
                chunk_size=chunk_num_frame,
                num_left_chunks=-1,
                device=audio_attention_mask_.device,
            )
            audio_attention_mask_ = torch.logical_or(
                audio_attention_mask_, torch.logical_not(chunk_mask)
            )

        audio_attention_mask[audio_attention_mask_] = float("-inf")
        audio_states = self.apm(
            wavforms, attention_mask=audio_attention_mask
        ).hidden_states[self.audio_encoder_layer]
        audio_embeds = self.audio_projection_layer(audio_states)

        audio_embeds = audio_embeds.transpose(1, 2)
        audio_embeds = self.audio_avg_pooler(audio_embeds)
        audio_embeds = audio_embeds.transpose(1, 2)

        _, feature_lens_after_pooling = self._get_feat_extract_output_lengths(
            audio_feature_lens
        )

        num_audio_tokens = feature_lens_after_pooling

        final_audio_embeds = list[torch.Tensor]()
        idx = 0
        for i in range(len(audio_feature_lens_raw)):
            target_audio_embeds_lst = list[torch.Tensor]()
            for _ in range(len(audio_feature_lens_raw[i])):
                target_audio_embeds_lst.append(
                    audio_embeds[idx, : num_audio_tokens[idx], :]
                )
                idx += 1

            final_audio_embeds.append(torch.cat(target_audio_embeds_lst))

        return final_audio_embeds

    def_parse_and_validate_audio_input(
        self, **kwargs: object
    ) -> MiniCPMOAudioInputs | None:
        audio_features = kwargs.pop("audio_features", None)
        audio_embeds = kwargs.pop("audio_embeds", None)

        if audio_features is None and audio_embeds is None:
            return None

        if audio_embeds is not None:
            return MiniCPMOAudioEmbeddingInputs(
                type="audio_embeds",
                audio_embeds=audio_embeds,
            )

        audio_feature_lens = kwargs.pop("audio_feature_lens")

        return MiniCPMOAudioFeatureInputs(
            type="audio_features",
            audio_features=audio_features,
            audio_feature_lens=audio_feature_lens,
        )

    def_parse_and_validate_multimodal_inputs(self, **kwargs: object) -> dict:
        modalities = super()._parse_and_validate_multimodal_inputs(**kwargs)

        # Preserve the order of modalities if there are multiple of them
        # from the order of kwargs.
        for input_key in kwargs:
            if (
                input_key in ("audio_features", "audio_embeds")
                and "audios" not in modalities
            ):
                modalities["audios"] = self._parse_and_validate_audio_input(**kwargs)

        return modalities

    def_process_audio_input(
        self,
        audio_input: MiniCPMOAudioInputs,
    ) -> torch.Tensor | list[torch.Tensor]:
        if audio_input["type"] == "audio_embeds":
            return audio_input["audio_embeds"]

        return self.get_audio_hidden_states(audio_input)

    def_process_multimodal_inputs(self, modalities: dict):
        multimodal_embeddings = super()._process_multimodal_inputs(modalities)

        for modality in modalities:
            if modality == "audios":
                audio_input = modalities["audios"]
                audio_embeddings = self._process_audio_input(audio_input)
                multimodal_embeddings += tuple(audio_embeddings)

        return multimodal_embeddings
```