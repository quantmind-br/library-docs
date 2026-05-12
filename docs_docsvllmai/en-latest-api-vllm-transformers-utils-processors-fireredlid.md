---
title: fireredlid - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/processors/fireredlid/
source: sitemap
fetched_at: 2026-05-07T21:37:53.117233214-03:00
rendered_js: false
word_count: 4
summary: This document defines a feature extractor class that processes raw audio waveforms into log-mel filterbank features with CMVN normalization and calculates sequence lengths for downstream machine learning tasks.
tags:
    - audio-processing
    - feature-extraction
    - log-mel-filterbank
    - cmvn
    - machine-learning
    - signal-processing
    - tensor-manipulation
category: api
---

```
classFireRedLIDFeatureExtractor(SequenceFeatureExtractor):
"""
    Extracts 80-dim log-mel filterbank features from raw waveforms,
    applies CMVN, and returns padded feature tensors with lengths.

    Also computes ``fake_token_lengths`` — the actual encoder output
    length for each audio — so that vLLM can allocate the correct
    number of cross-attention KV cache slots.
    """

    model_input_names = ["input_features"]

    def__init__(
        self,
        feature_size=80,
        sampling_rate=16000,
        chunk_length=30,
        padding_value=0.0,
        return_attention_mask=False,
        dim=80,
        means=None,
        inverse_std_variences=None,
        num_mel_bins=80,
        frame_length=25,
        frame_shift=10,
        dither=0.0,
        left_context=3,
        right_context=3,
        **kwargs,
    ):
        super().__init__(
            feature_size=feature_size,
            sampling_rate=sampling_rate,
            padding_value=padding_value,
            return_attention_mask=return_attention_mask,
            **kwargs,
        )
        self.chunk_length = chunk_length
        self.dim = dim
        self.means = means
        self.inverse_std_variences = inverse_std_variences
        self.num_mel_bins = num_mel_bins
        self.frame_length = frame_length
        self.frame_shift = frame_shift
        self.dither = dither
        self.sampling_rate = sampling_rate
        self.context = left_context + 1 + right_context

    def__call__(
        self,
        raw_speech: np.ndarray | list[float] | list[np.ndarray] | list[list[float]],
        truncation: bool = True,
        pad_to_multiple_of: int | None = None,
        return_tensors: str | TensorType | None = None,
        return_attention_mask: bool | None = None,
        padding: str | None = "max_length",
        max_length: int | None = None,
        sampling_rate: int | None = None,
        do_normalize: bool | None = None,
        **kwargs,
    ) -> BatchFeature:
        if sampling_rate is not None and sampling_rate != self.sampling_rate:
            raise ValueError(
                f"FireRedLIDFeatureExtractor expects sampling_rate="
                f"{self.sampling_rate}, got {sampling_rate}."
            )

        # Initialize helpers
        cmvn = CMVN(self.dim, self.means, self.inverse_std_variences)
        fbank = KaldifeatFbank(
            num_mel_bins=self.num_mel_bins,
            frame_length=self.frame_length,
            frame_shift=self.frame_shift,
            dither=self.dither,
        )

        defpadding_position_is_0(padded_input, input_lengths):
            N, T = padded_input.size()[:2]
            mask = torch.ones((N, T)).to(padded_input.device)
            for i in range(N):
                mask[i, input_lengths[i] :] = 0
            mask = mask.unsqueeze(dim=1)
            return mask.to(torch.uint8)

        feats = []
        speech_lengths = []
        fake_token_lengths = []

        for speech in raw_speech:
            # vLLM loads audio via librosa (float32 in [-1,1]),
            # but kaldi_native_fbank expects int16-scale values.
            speech_scaled = speech * 32768
            feat = fbank(self.sampling_rate, speech_scaled)
            feat = cmvn(feat)
            feat = torch.from_numpy(feat).float()
            length = feat.size(0)
            feats.append(feat)
            speech_lengths.append(length)

            # Compute the actual Conv2dSubsampling output length.
            # This mirrors the mask logic in Conv2dSubsampling.forward:
            #   pad context frames, then mask[:, :, :-2:2][:, :, :-2:2].sum()
            padded_input = F.pad(feat, (0, 0, 0, self.context - 1), "constant", 0.0)
            src_mask = padding_position_is_0(
                padded_input[None, :, :],
                torch.tensor([length], dtype=torch.int32),
            )
            mask = src_mask[:, :, :-2:2][:, :, :-2:2]
            enc_len = mask[:, -1, :].sum(dim=-1)
            fake_token_len = torch.clamp(enc_len, min=1)
            fake_token_lengths.append(fake_token_len)

        if len(feats) == 0:
            return BatchFeature()

        # Pad to uniform length
        max_feat_len = max(f.size(0) for f in feats)
        padded = feats[0].new_zeros(len(feats), max_feat_len, feats[0].size(1))
        for i, feat in enumerate(feats):
            padded[i, : feat.size(0)] = feat

        result = BatchFeature({"input_features": padded})

        if return_tensors is not None:
            result = result.convert_to_tensors(return_tensors)

        result["speech_lengths"] = torch.tensor(speech_lengths, dtype=torch.long)
        result["fake_token_lengths"] = torch.concat(fake_token_lengths)
        return result
```