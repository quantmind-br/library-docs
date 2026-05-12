---
title: isaac - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/configs/isaac/
source: sitemap
fetched_at: 2026-05-07T21:37:04.383298635-03:00
rendered_js: false
word_count: 38
summary: This document defines the configuration classes for the Isaac multimodal model and its vision components, including support for pixel shuffle and specific patch processing parameters.
tags:
    - isaac-model
    - configuration-class
    - multimodal-ai
    - vision-config
    - pixel-shuffle
    - qwen3-config
category: reference
---

## IsaacConfig [¶](#vllm.transformers_utils.configs.isaac.IsaacConfig "Permanent link")

Bases: `Qwen3Config`

Configuration class for Isaac multimodal model.

Source code in `vllm/transformers_utils/configs/isaac.py`

```
classIsaacConfig(Qwen3Config):
"""Configuration class for Isaac multimodal model."""

    model_type = "isaac"
    sub_configs = {
        "vision_config": PixelShuffleSiglip2VisionConfig,
        "text_config": Qwen3Config,
    }

    def__init__(
        self,
        text_config=None,
        vision_config=None,
        vision_patch_size: int = 16,
        vision_max_num_patches: int = 256,
        vision_min_num_patches: int | None = None,
        pixel_shuffle_scale: int = 1,
        max_sequence_length: int = 16384,
        vision_token: str = "<image>",
        vision_attn_implementation: str | None = None,
        **kwargs,
    ):
        if isinstance(text_config, dict):
            # from HF config
            self.text_config = self.sub_configs["text_config"](**text_config)
        elif text_config is None:
            # For BC use all kwargs to init text config.
            self.text_config = self.sub_configs["text_config"](**kwargs)
        else:
            # from Qwen3Config
            self.text_config = text_config

        # EventStreamProcessor parameters (for backward compatibility)
        self.video_patch_size = vision_patch_size
        self.vision_max_num_patches = vision_max_num_patches
        self.vision_min_num_patches = vision_min_num_patches
        self.pixel_shuffle_scale = pixel_shuffle_scale

        # Processing parameters
        self.max_sequence_length = max_sequence_length
        self.vision_token = vision_token

        # Handle vision config - PixelShuffleSiglip2VisionConfig instance
        if isinstance(vision_config, dict):
            self.vision_config = PixelShuffleSiglip2VisionConfig(**vision_config)
        elif vision_config is None:
            self.vision_config = PixelShuffleSiglip2VisionConfig()
        else:
            self.vision_config = vision_config

        # Ensure compatibility with pretrained checkpoints
        self.vision_config.pixel_shuffle_scale_factor = getattr(
            self.vision_config,
            "pixel_shuffle_scale_factor",
            pixel_shuffle_scale,
        )
        self.vision_config.num_patches = getattr(
            self.vision_config,
            "num_patches",
            vision_max_num_patches,
        )
        self.vision_attn_implementation = vision_attn_implementation
        super().__init__(**kwargs)
```

## PixelShuffleSiglip2VisionConfig [¶](#vllm.transformers_utils.configs.isaac.PixelShuffleSiglip2VisionConfig "Permanent link")

Bases: `Siglip2VisionConfig`

Vision configuration for Isaac with Pixel Shuffle support.

Extends Siglip2VisionConfig with additional fields for pixel shuffle.

Source code in `vllm/transformers_utils/configs/isaac.py`

```
classPixelShuffleSiglip2VisionConfig(Siglip2VisionConfig):
"""Vision configuration for Isaac with Pixel Shuffle support.

    Extends Siglip2VisionConfig with additional fields for pixel shuffle.
    """

    model_type = "pixel_shuffle_siglip2"
    base_config_key = "vision_config"

    def__init__(
        self,
        pixel_shuffle_scale_factor: int = 1,
        num_patches: int = 256,
        **kwargs,
    ):
        super().__init__(**kwargs)

        # Add our custom fields
        self.pixel_shuffle_scale_factor = pixel_shuffle_scale_factor
        self.num_patches = num_patches
```