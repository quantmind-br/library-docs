---
title: funasr - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/processors/funasr/
source: sitemap
fetched_at: 2026-05-07T21:37:54.472394579-03:00
rendered_js: false
word_count: 4
summary: This document defines the FunASRFeatureExtractor class, which processes raw audio data into mel-filter bank features suitable for automated speech recognition tasks.
tags:
    - audio-processing
    - speech-recognition
    - feature-extraction
    - funasr
    - mel-spectrogram
    - python-classes
category: api
---

```
classFunASRFeatureExtractor(SequenceFeatureExtractor):
r"""
    Constructs a FunASR feature extractor.

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
        hop_length (`int`, *optional*, defaults to 160):
            Length of the overlapping windows for the STFT used to obtain the
            Mel Frequency coefficients.
        chunk_length (`int`, *optional*, defaults to 30):
            The maximum number of chunks of `sampling_rate` samples used to
            trim and pad longer or shorter audio sequences.
        n_fft (`int`, *optional*, defaults to 400):
            Size of the Fourier transform.
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
        hop_length=160,
        chunk_length=30,
        n_fft=400,
        padding_value=0.0,
        dither=0.0,
        max_length=1000,
        return_attention_mask=False,
        **kwargs,
    ):
        super().__init__(
            feature_size=feature_size,
            sampling_rate=sampling_rate,
            padding_value=padding_value,
            return_attention_mask=return_attention_mask,
            **kwargs,
        )
        self.frontend_conf = kwargs.get("frontend_conf", {})
        self.max_length = max_length
        self.n_fft = n_fft
        self.hop_length = hop_length
        self.chunk_length = chunk_length
        self.n_samples = chunk_length * sampling_rate
        self.nb_max_frames = self.n_samples // hop_length
        self.sampling_rate = sampling_rate
        self.dither = dither

    defextract_fbank(
        self, data, data_len=None, data_type: str = "sound", frontend=None, **kwargs
    ):
        if isinstance(data, np.ndarray):
            data = torch.from_numpy(data)
            if len(data.shape) < 2:
                data = data[None, :]  # data: [batch, N]
            data_len = [data.shape[1]] if data_len is None else data_len
        elif isinstance(data, torch.Tensor):
            if len(data.shape) < 2:
                data = data[None, :]  # data: [batch, N]
            data_len = [data.shape[1]] if data_len is None else data_len
        elif isinstance(data, (list, tuple)):
            data_list, data_len = [], []
            for data_i in data:
                if isinstance(data_i, np.ndarray):
                    data_i = torch.from_numpy(data_i)
                data_list.append(data_i)
                data_len.append(data_i.shape[0])
            data = pad_sequence(data_list, batch_first=True)

        data, data_len = frontend(data, data_len, **kwargs)

        if isinstance(data_len, (list, tuple)):
            data_len = torch.tensor([data_len])
        return data.to(torch.float32), data_len.to(torch.int32)

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
        device: str | None = "cpu",
        return_token_timestamps: bool | None = None,
        **kwargs,
    ) -> BatchFeature:
        frontend = WavFrontend(**self.frontend_conf, dither=self.dither)

        feats = []
        speech_lengths = []
        fake_token_lengths = []
        for speech in raw_speech:
            feature, length = self.extract_fbank(
                speech,
                data_type=kwargs.get("data_type", "sound"),
                frontend=frontend,
                is_final=True,
            )
            feats.append(feature)
            speech_lengths.append(length)
            olens = 1 + (length - 3 + 2 * 1) // 2
            olens = 1 + (olens - 3 + 2 * 1) // 2
            fake_token_len = (olens - 1) // 2 + 1
            fake_token_len = torch.clamp(fake_token_len, min=1)
            fake_token_lengths.append(fake_token_len)

        feats = torch.concat(feats, dim=0)
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