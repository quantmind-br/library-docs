---
title: mimo_audio - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/mimo_audio/
source: sitemap
fetched_at: 2026-05-07T21:31:40.028684797-03:00
rendered_js: false
word_count: 0
summary: Implements an audio encoder module for the MiMo-V2-Omni model that transforms mel spectrograms into embeddings suitable for large language models using a combination of vector quantization, transformer processing, and linear projection.
tags:
    - audio-processing
    - deep-learning
    - pytorch
    - multimodal-ai
    - embeddings
    - transformer-models
category: reference
---

```
classMimoAudioEncoder(nn.Module):
"""Audio encoder for MiMo-V2-Omni.

    Encodes mel spectrograms into LLM-compatible embeddings via:
      1. Audio tokenizer (VQ codes)
      2. Speech embeddings lookup
      3. Local Qwen2 transformer
      4. Linear projection
    """

    def__init__(self, config, model_path: str = "") -> None:
        super().__init__()
        if isinstance(config, dict):
            config = MimoAudioEncoderConfig.from_dict(config)
        self.config = config
        self.audio_channels = config.audio_channels
        self.audio_group_size = config.group_size
        self.audio_segment_size = config.audio_segment_size

        speech_vocab_sizes = self._parse_maybe_list(
            config.speech_vocab_size, config.audio_channels
        )
        speech_empty_ids = self._parse_maybe_list(
            config.speech_zeroemb_idx, config.audio_channels
        )

        input_local_config = Qwen2Config(
            hidden_size=config.input_local_dim,
            num_hidden_layers=config.input_local_layers,
            num_attention_heads=config.input_local_attn_heads,
            num_key_value_heads=config.input_local_attn_heads,
            intermediate_size=config.input_local_intermediate_size,
            attention_dropout=config.input_local_hidden_dropout,
            rope_theta=config.rope_theta,
            partial_rotary_factor=config.partial_rotary_factor,
        )

        self.input_local_transformer = Qwen2Model(input_local_config)

        if not config.add_post_norm:
            self.input_local_transformer.norm = nn.Identity()

        self.speech_embeddings = nn.ModuleList(
            [
                nn.Embedding(
                    speech_vocab_sizes[i],
                    config.input_local_dim,
                    padding_idx=speech_empty_ids[i],
                )
                for i in range(config.audio_channels)
            ]
        )

        if config.projection_layers == 1:
            self.projection = nn.Linear(
                config.input_local_dim * config.group_size,
                config.out_hidden_size,
                bias=False,
            )
        elif config.projection_layers == 2:
            self.projection = AudioProjection(
                config.input_local_dim * config.group_size,
                config.input_local_dim * config.group_size * 4,
                config.out_hidden_size,
            )
        else:
            raise ValueError(f"Invalid projection_layers: {config.projection_layers}")

        self.audio_tokenizer: MiMoAudioTokenizer | None = None
        if model_path:
            audio_tokenizer_path = os.path.join(model_path, "audio_tokenizer")
            if os.path.exists(audio_tokenizer_path):
                dev = torch.get_default_device()
                self.audio_tokenizer = self._load_audio_tokenizer(
                    audio_tokenizer_path, dev
                )
            else:
                logger.warning(
                    "Audio tokenizer not found at %s, audio encoding disabled",
                    audio_tokenizer_path,
                )

    @staticmethod
    def_load_audio_tokenizer(path: str, device: torch.device) -> MiMoAudioTokenizer:
"""Load MiMoAudioTokenizer from directory."""
        fromsafetensors.torchimport load_file

        config_path = os.path.join(path, "config.json")
        with open(config_path) as f:
            config_dict = json.load(f)
        config = MiMoAudioTokenizer.config_class(**config_dict)
        model = MiMoAudioTokenizer(config)
        safetensors_path = os.path.join(path, "model.safetensors")
        bin_path = os.path.join(path, "pytorch_model.bin")
        if os.path.exists(safetensors_path):
            state_dict = load_file(safetensors_path, device="cpu")
        elif os.path.exists(bin_path):
            state_dict = torch.load(bin_path, map_location="cpu", weights_only=True)
        else:
            raise FileNotFoundError(
                f"No model weights found in {path} "
                "(expected model.safetensors or pytorch_model.bin)"
            )
        model.load_state_dict(state_dict, strict=False)
        model = model.to(device=device, dtype=torch.bfloat16)
        model.eval()
        model.requires_grad_(False)
        return model

    def_parse_maybe_list(self, value, length: int) -> list[int]:
        if isinstance(value, str) and "-" in value:
            return [int(s) for s in value.split("-")]
        return [int(value)] * length

    defapply_input_local_transformer(self, speech_embeddings: torch.Tensor):
        output = self.input_local_transformer(
            inputs_embeds=speech_embeddings,
            return_dict=True,
            is_causal=not self.config.input_full_attention,
        )
        return output.last_hidden_state

    defapply_speech_embeddings(self, audio_codes: torch.Tensor) -> torch.Tensor:
        num_segments = audio_codes.shape[0]
        _audio_embeddings = torch.zeros(
            (num_segments, self.config.group_size, self.config.input_local_dim),
            dtype=next(self.speech_embeddings[0].parameters()).dtype,
            device=audio_codes.device,
        )
        for i in range(self.config.audio_channels):
            _audio_embeddings.add_(self.speech_embeddings[i](audio_codes[:, :, i]))
        return _audio_embeddings

    defprocess_audio(self, audio: torch.Tensor) -> torch.Tensor:
"""Pad audio codes to group_size boundary.

        Args:
            audio: [T, audio_channels] code tensor

        Returns:
            [T//group_size, group_size, audio_channels]
        """
        T = audio.shape[0]
        audio = audio[:, : self.audio_channels]
        padded_T = (
            (T + self.audio_group_size - 1)
            // self.audio_group_size
            * self.audio_group_size
        )
        padded_audio = torch.cat(
            [
                audio,
                torch.zeros(
                    padded_T - T,
                    self.audio_channels,
                    dtype=torch.int32,
                    device=audio.device,
                )
                + audio[-1, :],
            ],
            dim=0,
        )
        padded_audio = padded_audio.reshape(
            padded_T // self.audio_group_size,
            self.audio_group_size,
            self.audio_channels,
        )
        return padded_audio

    defget_audio_feature(
        self, mel_specs: list[torch.Tensor]
    ) -> tuple[torch.Tensor, list[int]]:
"""Encode mel spectrograms into LLM embedding space.

        Args:
            mel_specs: list of mel spectrogram tensors, each [T, n_mels]

        Returns:
            Tuple of:
            - audio_embeds: [total_tokens, out_hidden_size] concatenated embeddings
            - item_token_lens: list of int, number of tokens per input item
        """
        if self.audio_tokenizer is None:
            raise RuntimeError(
                "audio_tokenizer is not loaded. "
                "Ensure model_path points to a directory containing audio_tokenizer/."
            )

        if not mel_specs:
            device = next(self.projection.parameters()).device
            dtype = next(self.projection.parameters()).dtype
            return (
                torch.empty(0, self.config.out_hidden_size, device=device, dtype=dtype),
                [],
            )

        device = next(self.audio_tokenizer.encoder.parameters()).device
        code_list = tokenize_audio_batch(
            mel_specs,
            self.audio_tokenizer.encoder,
            segment_size=self.audio_segment_size,
            device=device,
        )

        item_token_lens: list[int] = []
        codecs_to_concat = []
        for codecs in code_list:
            padded_codes = self.process_audio(codecs)
            codecs_to_concat.append(padded_codes)
            item_token_lens.append(padded_codes.shape[0])

        audio_codes = torch.cat(
            codecs_to_concat, dim=0
        )  # [total_T//group_size, group_size, audio_channels]

        _audio_embeddings = self.apply_speech_embeddings(audio_codes)
        audio_embeds = self.apply_input_local_transformer(_audio_embeddings)
        B = audio_embeds.shape[0]
        audio_embeds = self.projection(audio_embeds.reshape(B, -1))
        return audio_embeds, item_token_lens
```