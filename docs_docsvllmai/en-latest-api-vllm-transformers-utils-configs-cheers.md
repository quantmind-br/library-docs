---
title: cheers - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/configs/cheers/
source: sitemap
fetched_at: 2026-05-07T21:36:47.853885988-03:00
rendered_js: false
word_count: 39
summary: This document defines the configuration classes CheersConfig and CheersTextConfig, which manage hyperparameters and architectural settings for the Cheers multimodal machine learning model.
tags:
    - cheers-model
    - configuration-class
    - transformers-utils
    - multimodal-config
    - model-architecture
    - vllm-framework
category: reference
---

## CheersConfig [¶](#vllm.transformers_utils.configs.cheers.CheersConfig "Permanent link")

Bases: `PretrainedConfig`

Configuration class for Cheers (UMM) model.

Source code in `vllm/transformers_utils/configs/cheers.py`

```
classCheersConfig(PretrainedConfig):
"""Configuration class for Cheers (UMM) model."""

    model_type = "umm"

    def__init__(
        self,
        text_config: dict | CheersTextConfig | None = None,
        vision_representation_config: dict | SiglipVisionConfig | None = None,
        vae_encoder_config: dict | None = None,
        vae_decoder_config: dict | None = None,
        **kwargs,
    ):
        super().__init__(**kwargs)

        if isinstance(text_config, dict):
            self.text_config = CheersTextConfig(**text_config)
        else:
            self.text_config = text_config or CheersTextConfig()

        if isinstance(vision_representation_config, dict):
            self.vision_representation_config = SiglipVisionConfig(
                **vision_representation_config
            )
        else:
            self.vision_representation_config = (
                vision_representation_config or SiglipVisionConfig()
            )

        self.vae_encoder_config = vae_encoder_config or {"resolution": 512}
        self.vae_decoder_config = vae_decoder_config or {"resolution": 512}

    @property
    defhidden_size(self) -> int:
"""Return the hidden size of the language model."""
        return self.text_config.hidden_size
```

### hidden\_size `property` [¶](#vllm.transformers_utils.configs.cheers.CheersConfig.hidden_size "Permanent link")

Return the hidden size of the language model.

## CheersTextConfig [¶](#vllm.transformers_utils.configs.cheers.CheersTextConfig "Permanent link")

Bases: `PretrainedConfig`

Qwen2-based text config with Cheers-specific defaults.

Source code in `vllm/transformers_utils/configs/cheers.py`

```
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71

classCheersTextConfig(PretrainedConfig):
"""Qwen2-based text config with Cheers-specific defaults."""

    model_type = "umm"
    base_config_key = "text_config"

    def__init__(
        self,
        vocab_size=152064,
        hidden_size=3584,
        intermediate_size=18944,
        num_hidden_layers=28,
        num_attention_heads=28,
        num_key_value_heads=4,
        hidden_act="silu",
        max_position_embeddings=131072,
        initializer_range=0.02,
        rms_norm_eps=1e-6,
        use_cache=True,
        tie_word_embeddings=False,
        rope_theta=1000000.0,
        rope_scaling=None,
        use_sliding_window=False,
        sliding_window=131072,
        max_window_layers=28,
        layer_types=None,
        attention_dropout=0.0,
        **kwargs,
    ):
        self.vocab_size = vocab_size
        self.max_position_embeddings = max_position_embeddings
        self.hidden_size = hidden_size
        self.intermediate_size = intermediate_size
        self.num_hidden_layers = num_hidden_layers
        self.num_attention_heads = num_attention_heads
        self.use_sliding_window = use_sliding_window
        self.sliding_window = sliding_window if self.use_sliding_window else None
        self.max_window_layers = max_window_layers
        if num_key_value_heads is None:
            num_key_value_heads = num_attention_heads
        self.num_key_value_heads = num_key_value_heads
        self.hidden_act = hidden_act
        self.initializer_range = initializer_range
        self.rms_norm_eps = rms_norm_eps
        self.use_cache = use_cache
        self.rope_theta = rope_theta
        self.rope_scaling = rope_scaling
        self.attention_dropout = attention_dropout
        if self.rope_scaling is not None and "type" in self.rope_scaling:
            self.rope_scaling["rope_type"] = self.rope_scaling["type"]
        rope_config_validation(self)

        self.layer_types = layer_types
        if self.layer_types is None:
            self.layer_types = [
                "sliding_attention"
                if self.sliding_window is not None and i >= self.max_window_layers
                else "full_attention"
                for i in range(self.num_hidden_layers)
            ]

        super().__init__(
            tie_word_embeddings=tie_word_embeddings,
            **kwargs,
        )
```