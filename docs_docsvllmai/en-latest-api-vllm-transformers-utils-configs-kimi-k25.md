---
title: kimi_k25 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/configs/kimi_k25/
source: sitemap
fetched_at: 2026-05-07T21:37:05.868736019-03:00
rendered_js: false
word_count: 138
summary: This document provides the technical configuration specification for the Kimi-K2.5 multimodal model, detailing its integration of vision towers with video-chunk processing and text-based deepseek architectures.
tags:
    - kimi-k25
    - model-configuration
    - multimodal
    - computer-vision
    - vllm
    - deepseek-v3
category: reference
---

## vllm.transformers\_utils.configs.kimi\_k25 [¶](#vllm.transformers_utils.configs.kimi_k25 "Permanent link")

Kimi-K2.5 Model Configuration.

This configuration supports video-chunk as an internal modality type. A video-chunk is the smallest independently processable unit of video.

## KimiK25Config [¶](#vllm.transformers_utils.configs.kimi_k25.KimiK25Config "Permanent link")

Bases: `PretrainedConfig`

Kimi-K2.5 model configuration.

Kimi-K2.5 extends Kimi-K2 with vision support using video-chunks. A video-chunk consists of multiple consecutive frames that are processed together with temporal pooling.

Parameters:

Name Type Description Default `vision_config` `dict | KimiK25VisionConfig | None`

Configuration for the vision tower and projector.

`None` `text_config` `dict | DeepseekV3Config | None`

Configuration for the text model (DeepseekV3).

`None` `ignore_index` `int`

The ignore index for the loss function.

`-100` `media_placeholder_token_id` `int`

The token ID for media placeholders.

`163605` `pad_token_id` `int`

The token ID for padding.

`0`

Source code in `vllm/transformers_utils/configs/kimi_k25.py`

```
classKimiK25Config(PretrainedConfig):
"""Kimi-K2.5 model configuration.

    Kimi-K2.5 extends Kimi-K2 with vision support using video-chunks.
    A video-chunk consists of multiple consecutive frames
    that are processed together with temporal pooling.

    Args:
        vision_config: Configuration for the vision tower and projector.
        text_config: Configuration for the text model (DeepseekV3).
        ignore_index: The ignore index for the loss function.
        media_placeholder_token_id: The token ID for media placeholders.
        pad_token_id: The token ID for padding.
    """

    model_type = "kimi_k25"

    def__init__(
        self,
        vision_config: dict | KimiK25VisionConfig | None = None,
        text_config: dict | DeepseekV3Config | None = None,
        ignore_index: int = -100,
        media_placeholder_token_id: int = 163605,
        pad_token_id: int = 0,
        use_unified_vision_chunk: bool = False,
        video_placeholder: str = "<|kimi_k25_video_placeholder|>",
        **kwargs,
    ):
        # Vision config
        if vision_config is None:
            self.vision_config = KimiK25VisionConfig()
        elif isinstance(vision_config, dict):
            self.vision_config = KimiK25VisionConfig(**vision_config)
        else:
            self.vision_config = vision_config

        # Text config
        if text_config is None:
            self.text_config = DeepseekV3Config()
        elif isinstance(text_config, dict):
            self.text_config = DeepseekV3Config(**text_config)
        else:
            self.text_config = text_config

        # Set mm_hidden_size to text hidden size if not explicitly set
        if self.vision_config.mm_hidden_size == self.vision_config.hidden_size:
            self.vision_config.mm_hidden_size = self.text_config.hidden_size

        # Other config
        self.ignore_index = ignore_index
        self.media_placeholder_token_id = media_placeholder_token_id
        self.use_unified_vision_chunk = use_unified_vision_chunk
        self.video_placeholder = video_placeholder

        # Propagate quantization config from text model
        if getattr(self.text_config, "quantization_config", None) is not None:
            self.quantization_config = self.text_config.quantization_config

        super().__init__(pad_token_id=pad_token_id, **kwargs)

    @property
    defhidden_size(self) -> int:
"""Get hidden size from text config for compatibility."""
        return self.text_config.hidden_size

    @property
    defvocab_size(self) -> int:
"""Get vocab size from text config for compatibility."""
        return self.text_config.vocab_size
```

### hidden\_size `property` [¶](#vllm.transformers_utils.configs.kimi_k25.KimiK25Config.hidden_size "Permanent link")

Get hidden size from text config for compatibility.

### vocab\_size `property` [¶](#vllm.transformers_utils.configs.kimi_k25.KimiK25Config.vocab_size "Permanent link")

Get vocab size from text config for compatibility.