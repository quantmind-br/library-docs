---
title: bagel - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/configs/bagel/
source: sitemap
fetched_at: 2026-05-07T21:36:45.57259913-03:00
rendered_js: false
word_count: 26
summary: This document defines the BagelConfig class, which manages configuration settings and parameters for the BAGEL model architecture within the vLLM framework.
tags:
    - vllm
    - model-configuration
    - bagel-model
    - pretrained-config
    - transformer-utils
category: reference
---

## vllm.transformers\_utils.configs.bagel [¶](#vllm.transformers_utils.configs.bagel "Permanent link")

## BagelConfig [¶](#vllm.transformers_utils.configs.bagel.BagelConfig "Permanent link")

Bases: `PretrainedConfig`

Configuration class for BAGEL model.

Source code in `vllm/transformers_utils/configs/bagel.py`

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

classBagelConfig(PretrainedConfig):
"""Configuration class for BAGEL model."""

    model_type = "bagel"

    def__init__(
        self,
        visual_gen: bool = True,
        visual_und: bool = True,
        llm_config: dict | Qwen2Config | None = None,
        vit_config: dict | SiglipVisionConfig | None = None,
        vae_config: dict | None = None,
        latent_patch_size: int = 2,
        max_latent_size: int = 32,
        vit_max_num_patch_per_side: int = 70,
        connector_act: str = "gelu_pytorch_tanh",
        interpolate_pos: bool = False,
        timestep_shift: float = 1.0,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.visual_gen = visual_gen
        self.visual_und = visual_und

        # Convert dict configs to proper config objects
        if isinstance(llm_config, dict):
            self.llm_config = Qwen2Config(**llm_config)
        else:
            self.llm_config = llm_config or Qwen2Config()

        if isinstance(vit_config, dict):
            self.vit_config = SiglipVisionConfig(**vit_config)
        else:
            self.vit_config = vit_config or SiglipVisionConfig()

        self.vae_config = vae_config or {"z_channels": 16, "downsample": 8}
        self.latent_patch_size = latent_patch_size
        self.max_latent_size = max_latent_size
        self.vit_max_num_patch_per_side = vit_max_num_patch_per_side
        self.connector_act = connector_act
        self.interpolate_pos = interpolate_pos
        self.timestep_shift = timestep_shift

    @property
    defhidden_size(self) -> int:
"""Return the hidden size of the language model."""
        return self.llm_config.hidden_size
```

### hidden\_size `property` [¶](#vllm.transformers_utils.configs.bagel.BagelConfig.hidden_size "Permanent link")

Return the hidden size of the language model.