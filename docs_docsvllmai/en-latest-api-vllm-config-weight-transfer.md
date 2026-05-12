---
title: weight_transfer - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/config/weight_transfer/
source: sitemap
fetched_at: 2026-05-07T21:17:19.047316084-03:00
rendered_js: false
word_count: 22
summary: This document defines the configuration settings for weight transfer operations used during reinforcement learning training, specifically detailing the available backend options.
tags:
    - weight-transfer
    - reinforcement-learning
    - configuration-settings
    - nccl
    - ipc
    - vllm-config
category: configuration
---

Configuration for weight transfer during RL training.

Source code in `vllm/config/weight_transfer.py`

```
@config
classWeightTransferConfig:
"""Configuration for weight transfer during RL training."""

    backend: Literal["nccl", "ipc"] = "nccl"
"""The backend to use for weight transfer."""
```

### backend `class-attribute` `instance-attribute` [¶](#vllm.config.weight_transfer.WeightTransferConfig.backend "Permanent link")

```
backend: Literal['nccl', 'ipc'] = 'nccl'
```

The backend to use for weight transfer.