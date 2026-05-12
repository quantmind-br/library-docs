---
title: fireredasr2 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/processors/fireredasr2/
source: sitemap
fetched_at: 2026-05-07T21:37:52.606451726-03:00
rendered_js: false
word_count: 5
summary: This class defines a feature extractor for the FireRedASR2 model, responsible for converting raw speech into mel-filter bank features and applying normalization via CMVN. It manages audio preprocessing steps such as padding, truncation, and feature dimension adjustment for model input.
tags:
    - audio-processing
    - feature-extraction
    - asr
    - mel-filter-bank
    - speech-recognition
    - python-class
category: reference
---

```
classFireRedASR2FeatureExtractor(SequenceFeatureExtractor):
r"""
    Constructs a FireRedASR2 feature extractor.

    This feature extractor inherits from [`~feature_extraction_sequence_
        utils.SequenceFeatureExtractor`] which contains most of the main
        methods. Users should refer to this superclass for more information
        regarding those methods.

    This class extracts mel-filter bank features from raw speech using a custom
    numpy implementation of the `Short Time Fourier Transform` which should
    match pytorch's `torch.stft` equivalent.

    Args:
        feature_size (`int`, *optional*, defaults to 80):
            The feature dimension of the extracted features.
        sampling_rate (`int`, *optional*, defaults to 16000):
            The sampling rate at which the audio files should be digitalized
            expressed in hertz (Hz).
        chunk_length (`int`, *optional*, defaults to 30):
            The maximum number of chunks of `sampling_rate` samples used to
            trim and pad longer or shorter audio sequences.
        padding_value (`float`, *optional*, defaults to 0.0):
            Padding value used to pad the audio. Should correspond to silences.
        dither (`float`, *optional*, defaults to 0.0):
            Adds dithering. In other words, adds a small Gaussian noise to each frame.
            E.g. use 0.0001 to add dithering with a normal distribution centered
            around 0.0 with standard deviation 0.0001 (assuming [-1,+1] range
            of raw_speech). The value 0.0 means no dithering.
            Dithering has similar effect as `spectrogram(mel_floor=...)`. It reduces
            the high log_mel_fbank values for signals with hard-zero sections,
            when VAD cutoff is present in the signal.
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
        max_length=3000,
        downsample_rate=2,
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
        self.max_length = max_length
        self.dim = dim
        self.means = means
        self.inverse_std_variences = inverse_std_variences
        self.num_mel_bins = num_mel_bins
        self.frame_length = frame_length
        self.frame_shift = frame_shift
        self.dither = dither
        self.sampling_rate = sampling_rate
        self.downsample_rate = downsample_rate
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
        if sampling_rate != self.sampling_rate:
            raise ValueError(
                f"The model corresponding to this feature extractor: "
                f"{self.__class__.__name__} was trained using a sampling "
                f"rate of {self.sampling_rate}. Please make sure that the "
                f"provided `raw_speech` input was sampled with "
                f"{self.sampling_rate} and not {sampling_rate}."
            )

        defpadding_position_is_0(padded_input, input_lengths):
            N, T = padded_input.size()[:2]
            mask = torch.ones((N, T)).to(padded_input.device)
            for i in range(N):
                mask[i, input_lengths[i] :] = 0
            mask = mask.unsqueeze(dim=1)
            return mask.to(torch.uint8)

        # initialize the CMVN and Fbank objects
        self.cmvn = CMVN(self.dim, self.means, self.inverse_std_variences)
        self.fbank = KaldifeatFbank(
            num_mel_bins=self.num_mel_bins,
            frame_length=self.frame_length,
            frame_shift=self.frame_shift,
            dither=self.dither,
        )

        feats = []
        speech_lengths = []
        fake_token_lengths = []
        for speech in raw_speech:
"""
            We must multiply by 32768 here because FireRedASR2 loads audio data
            using kaldiio.load_mat, while vLLM loads audio data using pyav.
            """
            speech = speech * 32768
            fbank = self.fbank(sampling_rate, speech)
            fbank = self.cmvn(fbank)
            fbank = torch.from_numpy(fbank).float()
            length = fbank.size(0)
            feats.append(fbank)
            speech_lengths.append(length)
            padded_input2 = fbank
            padded_input2 = F.pad(
                padded_input2, (0, 0, 0, self.context - 1), "constant", 0.0
            )
            src_mask = padding_position_is_0(
                padded_input2[None, :, :], torch.tensor([length], dtype=torch.int32)
            )
            x_mask = src_mask
            mask = x_mask[:, :, :-2:2][:, :, :-2:2]
            input_lengths = mask[:, -1, :].sum(dim=-1)
            input_lengths = input_lengths // self.downsample_rate
            fake_token_len = torch.clamp(input_lengths, min=1)
            fake_token_lengths.append(fake_token_len)

        feats = torch.stack(feats, dim=0)
        batched_speech = self.pad(
            BatchFeature({"input_features": feats}),
            padding=padding,
            max_length=max_length if max_length else self.max_length,
            truncation=truncation,
            pad_to_multiple_of=pad_to_multiple_of,
            return_attention_mask=return_attention_mask or do_normalize,
        )

        if return_tensors is not None:
            batched_speech = batched_speech.convert_to_tensors(return_tensors)

        batched_speech["speech_lengths"] = torch.tensor(speech_lengths)
        batched_speech["fake_token_lengths"] = torch.concat(fake_token_lengths)
        return batched_speech
```