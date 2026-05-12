---
title: audio - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/multimodal/media/audio/
source: sitemap
fetched_at: 2026-05-07T21:34:10.849775001-03:00
rendered_js: false
word_count: 185
summary: This document defines classes and utility functions for handling audio data ingestion, including loading and base64 encoding, using libraries like PyAV and soundfile within the vllm framework.
tags:
    - audio-processing
    - multimodal
    - data-loading
    - vllm
    - tensor-handling
    - pyav
    - soundfile
category: reference
---

Bases: `MediaIO[Tensor]`

Configuration values can be user-provided either by --media-io-kwargs or by the runtime API field "media\_io\_kwargs". Ensure proper validation and error handling.

Source code in `vllm/multimodal/media/audio.py`

```
classAudioEmbeddingMediaIO(MediaIO[torch.Tensor]):
"""Configuration values can be user-provided either by --media-io-kwargs or
    by the runtime API field "media_io_kwargs". Ensure proper validation and
    error handling.
    """

    def__init__(self) -> None:
        super().__init__()

    defload_bytes(self, data: bytes) -> torch.Tensor:
        buffer = BytesIO(data)
        # Enable sparse tensor integrity checks to prevent out-of-bounds
        # writes from maliciously crafted tensors
        with torch.sparse.check_sparse_tensor_invariants():
            tensor = torch.load(buffer, weights_only=True)
            return tensor.to_dense()

    defload_base64(self, media_type: str, data: str) -> torch.Tensor:
        return self.load_bytes(pybase64.b64decode(data, validate=True))

    defload_file(self, filepath: Path) -> torch.Tensor:
        # Enable sparse tensor integrity checks to prevent out-of-bounds
        # writes from maliciously crafted tensors
        with torch.sparse.check_sparse_tensor_invariants():
            tensor = torch.load(filepath, weights_only=True)
            return tensor.to_dense()

    defencode_base64(self, media: torch.Tensor) -> str:
        return tensor2base64(media)
```

Bases: `MediaIO[tuple[NDArray, float]]`

Configuration values can be user-provided either by --media-io-kwargs or by the runtime API field "media\_io\_kwargs". Ensure proper validation and error handling.

Source code in `vllm/multimodal/media/audio.py`

```
classAudioMediaIO(MediaIO[tuple[npt.NDArray, float]]):
"""Configuration values can be user-provided either by --media-io-kwargs or
    by the runtime API field "media_io_kwargs". Ensure proper validation and
    error handling.
    """

    def__init__(self, **kwargs) -> None:
        super().__init__()

        # `kwargs` contains custom arguments from
        # --media-io-kwargs for this modality, merged with
        # per-request runtime media_io_kwargs via merge_kwargs().
        # They can be passed to the underlying
        # media loaders (e.g. custom implementations)
        # for flexible control.
        self.kwargs = kwargs

    defload_bytes(self, data: bytes) -> tuple[npt.NDArray, float]:
        return load_audio(BytesIO(data), sr=None)

    defload_base64(
        self,
        media_type: str,
        data: str,
    ) -> tuple[npt.NDArray, float]:
        return self.load_bytes(pybase64.b64decode(data))

    defload_file(self, filepath: Path) -> tuple[npt.NDArray, float]:
        return load_audio(filepath, sr=None)

    defencode_base64(
        self,
        media: tuple[npt.NDArray, int],
        *,
        audio_format: str = "WAV",
    ) -> str:
        audio, sr = media

        with BytesIO() as buffer:
            soundfile.write(buffer, audio, sr, format=audio_format)
            data = buffer.getvalue()

        return pybase64.b64encode(data).decode("utf-8")
```

Load an audio file using PyAV (FFmpeg), returning float32 mono waveform.

Decodes the audio stream at its native sample rate. Channel reduction to mono is performed by averaging across channels. Resampling to a model-specific rate is left to the downstream :class:`AudioResampler`.

Parameters:

Name Type Description Default `path` `BytesIO | Path | str`

A :class:`~io.BytesIO` buffer, a filesystem :class:`~pathlib.Path`, or a string path.

*required*

Returns:

Type Description `NDArray`

`(waveform, sample_rate)` where *waveform* is a 1-D float32

`float`

NumPy array and *sample\_rate* is the native sample rate in Hz.

Source code in `vllm/multimodal/media/audio.py`

```
defload_audio_pyav(
    path: BytesIO | Path | str,
    *,
    sr: float | None = 22050,
    mono: bool = True,
) -> tuple[npt.NDArray, float]:
"""Load an audio file using PyAV (FFmpeg), returning float32 mono waveform.

    Decodes the audio stream at its native sample rate. Channel reduction to
    mono is performed by averaging across channels.  Resampling to a
    model-specific rate is left to the downstream :class:`AudioResampler`.

    Args:
        path: A :class:`~io.BytesIO` buffer, a filesystem
            :class:`~pathlib.Path`, or a string path.

    Returns:
        ``(waveform, sample_rate)`` where *waveform* is a 1-D float32
        NumPy array and *sample_rate* is the native sample rate in Hz.
    """
    native_sr = None
    try:
        with av.open(path) as container:
            if not container.streams.audio:
                raise ValueError("No audio stream found.")
            stream = container.streams.audio[0]
            stream.thread_type = "AUTO"
            native_sr = stream.rate
            sr = sr or native_sr

            chunks: list[npt.NDArray] = []
            needs_resampling = not math.isclose(
                float(sr),
                float(native_sr),
                rel_tol=0.0,
                abs_tol=1e-6,
            )
            resampler = (
                av.AudioResampler(format="fltp", layout="mono", rate=sr)
                if needs_resampling
                else None
            )
            for frame in container.decode(stream):
                if needs_resampling:
                    assert resampler is not None
                    for out_frame in resampler.resample(frame):
                        chunks.append(out_frame.to_ndarray())
                else:
                    chunks.append(frame.to_ndarray())
    except ValueError:
        raise
    except Exception as e:
        raise ValueError(
            "Invalid or corrupted video data when extracting audio. "
            "Ensure the input is valid video bytes (e.g. a complete MP4)."
        ) frome

    if not chunks:
        raise ValueError("No audio found in the video.")

    audio = np.concatenate(chunks, axis=-1).astype(np.float32)
    if mono and audio.ndim > 1:
        audio = np.mean(audio, axis=0)

    return audio, sr
```

Load audio via soundfile

Source code in `vllm/multimodal/media/audio.py`

```
defload_audio_soundfile(
    path: BytesIO | Path | str,
    *,
    sr: float | None = 22050,
    mono: bool = True,
) -> tuple[np.ndarray, int]:
"""Load audio via soundfile"""
    with soundfile.SoundFile(path) as f:
        native_sr = f.samplerate
        y = f.read(dtype="float32", always_2d=False).T

    if mono and y.ndim > 1:
        y = np.mean(y, axis=tuple(range(y.ndim - 1)))

    if sr is not None and sr != native_sr:
        y = resample_audio_pyav(y, orig_sr=native_sr, target_sr=sr)
        return y, int(sr)
    return y, native_sr
```