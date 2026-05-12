---
title: ovis - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/configs/ovis/
source: sitemap
fetched_at: 2026-05-07T21:37:21.917519829-03:00
rendered_js: false
word_count: 148
summary: This document defines the configuration class for the AIMv2 model, detailing the parameters required to initialize the model architecture.
tags:
    - aimv2
    - model-configuration
    - transformer
    - hyperparameters
    - deep-learning
category: reference
---

Bases: `PretrainedConfig`

This is the configuration class to store the configuration of an \[`AIMv2Model`]. Instantiating a configuration with the defaults will yield a similar configuration to that of the [apple/aimv2-large-patch14-224](https://huggingface.co/apple/aimv2-large-patch14-224). Args: hidden\_size: Dimension of the hidden representations. intermediate\_size: Dimension of the SwiGLU representations. num\_hidden\_layers: Number of hidden layers in the Transformer. num\_attention\_heads: Number of attention heads for each attention layer in the Transformer. num\_channels: Number of input channels. image\_size: Image size. patch\_size: Patch size. rms\_norm\_eps: Epsilon value used for the RMS normalization layer. attention\_dropout: Dropout ratio for attention probabilities. projection\_dropout: Dropout ratio for the projection layer after the attention. qkv\_bias: Whether to add a bias to the queries, keys and values. use\_bias: Whether to add a bias in the feed-forward and projection layers. kwargs: Keyword arguments for the \[`PretrainedConfig`].

Source code in `vllm/transformers_utils/configs/ovis.py`

```
classAIMv2Config(PretrainedConfig):
"""This is the configuration class to store the configuration of an [`AIMv2Model`].
    Instantiating a configuration with the defaults will yield a similar configuration
    to that of the [apple/aimv2-large-patch14-224](https://huggingface.co/apple/aimv2-large-patch14-224).
    Args:
        hidden_size: Dimension of the hidden representations.
        intermediate_size: Dimension of the SwiGLU representations.
        num_hidden_layers: Number of hidden layers in the Transformer.
        num_attention_heads: Number of attention heads for each attention layer
            in the Transformer.
        num_channels: Number of input channels.
        image_size: Image size.
        patch_size: Patch size.
        rms_norm_eps: Epsilon value used for the RMS normalization layer.
        attention_dropout: Dropout ratio for attention probabilities.
        projection_dropout: Dropout ratio for the projection layer after the attention.
        qkv_bias: Whether to add a bias to the queries, keys and values.
        use_bias: Whether to add a bias in the feed-forward and projection layers.
        kwargs: Keyword arguments for the [`PretrainedConfig`].
    """

    model_type: str = "aimv2"

    def__init__(
        self,
        hidden_size: int = 1024,
        intermediate_size: int = 2816,
        num_hidden_layers: int = 24,
        num_attention_heads: int = 8,
        num_channels: int = 3,
        image_size: int = 224,
        patch_size: int = 14,
        rms_norm_eps: float = 1e-5,
        attention_dropout: float = 0.0,
        projection_dropout: float = 0.0,
        qkv_bias: bool = False,
        use_bias: bool = False,
        **kwargs: Any,
    ):
        super().__init__(**kwargs)
        self.hidden_size = hidden_size
        self.intermediate_size = intermediate_size
        self.num_hidden_layers = num_hidden_layers
        self.num_attention_heads = num_attention_heads
        self.num_channels = num_channels
        self.patch_size = patch_size
        self.image_size = image_size
        self.attention_dropout = attention_dropout
        self.rms_norm_eps = rms_norm_eps

        self.projection_dropout = projection_dropout
        self.qkv_bias = qkv_bias
        self.use_bias = use_bias
```