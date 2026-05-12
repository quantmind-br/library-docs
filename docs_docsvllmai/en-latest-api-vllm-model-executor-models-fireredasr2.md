---
title: fireredasr2 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/fireredasr2/
source: sitemap
fetched_at: 2026-05-07T21:30:03.008013318-03:00
rendered_js: false
word_count: 0
summary: This document defines the schema for FireRedASR2 audio inputs, specifying the tensor dimensions and data types required for batch processing of mel bins, speech lengths, and token lengths.
tags:
    - audio-processing
    - tensor-schema
    - asr-model
    - data-structure
    - pytorch-tensors
    - input-validation
category: reference
---

```
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84

classFireRedASR2AudioInputs(TensorSchema):
"""
    Dimensions:
        - b: Batch size
        - nmb: Number of mel bins
        - t: Time frames (M)
    """

    input_features: Annotated[
        list[torch.Tensor] | None,
        TensorShape("b", "nmb", "t"),
    ]
    speech_lengths: Annotated[
        list[torch.Tensor] | None,
        TensorShape("b"),
    ]
    fake_token_lengths: Annotated[
        list[torch.Tensor] | None,
        TensorShape("b"),
    ]
```