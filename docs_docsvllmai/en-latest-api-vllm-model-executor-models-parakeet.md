---
title: parakeet - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/parakeet/
source: sitemap
fetched_at: 2026-05-07T21:32:32.0844247-03:00
rendered_js: false
word_count: 10
summary: This code implements a Parakeet audio feature extractor that processes raw waveforms into normalized mel-filterbank features, including support for windowing, STFT, pre-emphasis, and audio clipping.
tags:
    - audio-processing
    - feature-extraction
    - mel-spectrogram
    - pytorch
    - signal-processing
    - speech-recognition
category: reference
---

```
classParakeetExtractor:
    def__init__(self, config: PretrainedConfig) -> None:
        self.config = ExtractorConfig.from_hf_config(config)
"""`config` is named *exactly* for `._get_subsampling_output_length` below"""
        self._clip_target_samples = int(
            round(self.config.clip_duration_s * self.config.sampling_rate)
        )
        self._tail_min_samples = int(
            round(self.config.clip_min_duration_s * self.config.sampling_rate)
        )

    @staticmethod
    @cache
    def_get_window(win_length: int, device: str) -> torch.Tensor:
        return torch.hann_window(win_length, periodic=False, device=device)

    @staticmethod
    @cache
    def_get_mel_filters(
        feature_size: int, sampling_rate: int, n_fft: int, device: str
    ) -> torch.Tensor:
        filter_bank = mel_filter_bank(
            num_frequency_bins=n_fft // 2 + 1,
            num_mel_filters=feature_size,
            min_frequency=0.0,
            max_frequency=sampling_rate / 2,
            sampling_rate=sampling_rate,
            norm="slaney",
            mel_scale="slaney",
        )
        return torch.from_numpy(filter_bank.T).to(device=device, dtype=torch.float32)

    def_torch_extract_fbank_features(self, waveform: torch.Tensor, device: str):
        # spectrogram
        device = str(torch.device(device))
        cfg = self.config
        window = self._get_window(cfg.win_length, device)
        stft = torch.stft(
            waveform,
            self.config.n_fft,
            hop_length=cfg.hop_length,
            win_length=cfg.win_length,
            window=window,
            return_complex=True,
            pad_mode="constant",
        )
        mel_filters = self._get_mel_filters(
            cfg.feature_size, cfg.sampling_rate, cfg.n_fft, device
        )
        return self._apply_mel_filters(stft, mel_filters)

    @torch.compile(dynamic=True)
    def_apply_mel_filters(
        self, stft_output: torch.Tensor, mel_filters: torch.Tensor
    ) -> torch.Tensor:
        magnitudes = stft_output.real.square() + stft_output.imag.square()
        mel_spec = mel_filters @ magnitudes
        mel_spec = torch.log(mel_spec + LOG_ZERO_GUARD_VALUE)
        return mel_spec.permute(0, 2, 1)

    @torch.compile(dynamic=True)
    def_apply_preemphasis(
        self, input_features: torch.Tensor, audio_lengths: torch.Tensor
    ) -> torch.Tensor:
        timemask = torch.arange(
            input_features.shape[1], device=input_features.device
        ).unsqueeze(0) < audio_lengths.unsqueeze(1)
        input_features = torch.cat(
            [
                input_features[:, :1],
                input_features[:, 1:]
                - self.config.preemphasis * input_features[:, :-1],
            ],
            dim=1,
        )
        input_features = input_features.masked_fill(~timemask, 0.0)
        return input_features

    @torch.compile(dynamic=True)
    def_normalize_mel_features(
        self, mel_features: torch.Tensor, audio_lengths: torch.Tensor
    ) -> tuple[torch.Tensor, torch.Tensor]:
        features_lengths = torch.floor_divide(
            audio_lengths + self.config.n_fft // 2 * 2 - self.config.n_fft,
            self.config.hop_length,
        )
        attention_mask = (
            torch.arange(mel_features.shape[1], device=mel_features.device)[None, :]
            < features_lengths[:, None]
        )
        mask = attention_mask.unsqueeze(-1)
        lengths = attention_mask.sum(dim=1)
        mel_features_masked = mel_features * mask
        mean = (mel_features_masked.sum(dim=1) / lengths.unsqueeze(-1)).unsqueeze(1)
        variance = ((mel_features_masked - mean) ** 2 * mask).sum(dim=1) / (
            lengths - 1
        ).unsqueeze(-1)
        std = torch.sqrt(variance).unsqueeze(1)
        return (mel_features - mean) / (std + EPSILON) * mask, attention_mask

    def_pad_raw_speech(
        self, raw_speech: list[torch.Tensor], max_len: int, device: str
    ) -> torch.Tensor:
        output = torch.full(
            (len(raw_speech), max_len),
            self.config.padding_value,
            device=device,
            dtype=torch.float32,
        )
        dsts = [output[i, : raw_speech[i].shape[0]] for i in range(len(raw_speech))]
        srcs = [s.squeeze(-1) for s in raw_speech]
        # single kernel horizontal fusion
        torch._foreach_copy_(dsts, srcs)
        return output

    def_clip_sizes(self, audio_len: int) -> list[int]:
        audio_len = max(audio_len, self._tail_min_samples)
        num_full_clips, remainder = divmod(audio_len, self._clip_target_samples)
        clip_sizes = [self._clip_target_samples] * num_full_clips
        if remainder > 0:
            clip_sizes.append(max(remainder, self._tail_min_samples))
        return clip_sizes

    defaudio_token_count(self, audio_len: int) -> int:
        total_tokens = 0
        for clip_size in self._clip_sizes(audio_len):
            num_frames = clip_size // self.config.hop_length
            n_tokens = HFParakeetEncoder._get_subsampling_output_length(
                self, torch.tensor([num_frames], dtype=torch.float)
            )
            total_tokens += int(n_tokens.item())
        return max(1, total_tokens)

    defsplit_audio_into_clips(self, audio: torch.Tensor) -> list[torch.Tensor]:
        assert audio.ndim == 1
        audio_len = int(audio.shape[0])
        clip_sizes = self._clip_sizes(audio_len)
        target_len = sum(clip_sizes)
        if audio_len < target_len:
            audio = torch.nn.functional.pad(audio, (0, target_len - audio_len))

        clips = list[torch.Tensor]()
        offset = 0
        for clip_size in clip_sizes:
            clips.append(audio[offset : offset + clip_size])
            offset += clip_size
        return clips

    def__call__(
        self,
        raw_speech: list[np.ndarray],
        *,
        device: str = "cpu",
    ) -> dict[str, Any]:
        raw_speech = [
            torch.as_tensor(speech, device=device, dtype=torch.float32)
            for speech in raw_speech
        ]

        for i, speech in enumerate(raw_speech):
            if len(speech.shape) > 1:
                logger.warning(
                    "Only mono-channel audio is supported for input to %s. "
                    "We will take the mean of the channels to convert to mono.",
                    self.__class__.__name__,
                )
                raw_speech[i] = speech.mean(-1)

        audio_clips = list[torch.Tensor]()
        audio_num_clips = list[int]()
        for audio in raw_speech:
            clips = self.split_audio_into_clips(audio)
            audio_clips.extend(clips)
            audio_num_clips.append(len(clips))
        raw_speech = audio_clips

        audio_lengths = torch.tensor(
            [len(speech) for speech in raw_speech], dtype=torch.long, device=device
        )

        max_length = max(len(speech) for speech in raw_speech)
        input_features = self._pad_raw_speech(raw_speech, max_length, device)
        input_features = self._apply_preemphasis(input_features, audio_lengths)
        input_features = self._torch_extract_fbank_features(input_features, device)
        input_features, attention_mask = self._normalize_mel_features(
            input_features, audio_lengths
        )

        return {
            "input_audio_features": input_features,
            "feature_attention_mask": attention_mask,
            "audio_num_clips": audio_num_clips,
        }

    @staticmethod
    defaudio_length(raw_config: PretrainedConfig, audio_tokens: int) -> int:
        config = ExtractorConfig.from_hf_config(raw_config)
        return int(audio_tokens * config.subsampling_factor * config.hop_length)
```