---
title: ovis - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/ovis/
source: sitemap
fetched_at: 2026-05-07T21:32:28.067946403-03:00
rendered_js: false
word_count: 9
summary: This document defines a VisualTokenizer PyTorch module that processes image pixel values into discrete tokens using a vision backbone and a projection head.
tags:
    - pytorch
    - visual-tokenizer
    - computer-vision
    - feature-extraction
    - tokenization
    - deep-learning
category: reference
---

```
classVisualTokenizer(torch.nn.Module):
    def__init__(
        self,
        config: PretrainedConfig,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ):
        super().__init__()
        self.config = config
        self.backbone = self._init_backbone(
            config=config,
            quant_config=quant_config,
            prefix=f"{prefix}.backbone",
        )
        # reserved tokens for IMAGE_INDICATORS
        head_dim = config.vocab_size - len(IMAGE_INDICATOR_IDS)
        self.head = torch.nn.Sequential(
            ReplicatedLinear(
                config.backbone_config.hidden_size
                * config.hidden_stride
                * config.hidden_stride,
                head_dim,
                bias=False,
                return_bias=False,
            ),
            torch.nn.LayerNorm(head_dim),
        )

    def_init_backbone(
        self,
        config: PretrainedConfig,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ) -> nn.Module:
        model_type = config.backbone_config.model_type
        if model_type == "aimv2":
            # No post rms_norm in Ovis2's AIMv2 ViT.
            return AIMv2Model(
                config=config.backbone_config,
                quant_config=quant_config,
                require_post_norm=False,
                prefix=prefix,
            )
        elif model_type == "siglip_vision_model":
            return SiglipVisionModel(
                config=config.backbone_config,
                quant_config=quant_config,
                prefix=prefix,
            )
        raise ValueError(f"Unsupported visual tokenizer model_type: {model_type}")

    @property
    defdtype(self) -> torch.dtype:
        return next(self.head.parameters()).dtype

    @property
    defdevice(self) -> torch.device:
        return next(self.head.parameters()).device

    deftokenize(self, logits: torch.Tensor) -> torch.Tensor:
        if self.config.tokenize_function == "softmax":
            tokens = softmax(logits, dim=-1)
        elif self.config.tokenize_function == "gumbel_argmax":
            tokens = gumbel_softmax(logits, tau=self.config.tau, hard=True)
        elif self.config.tokenize_function == "st_argmax":
            tokens = st_argmax(logits, dim=-1)
        else:
            raise ValueError(
                "Invalid `max_type`, expected softmax or gumbel_argmax "
                f"or st_argmax, but got {self.config.tokenize_function}"
            )
        return tokens

    defencode(self, pixel_values: torch.Tensor) -> torch.Tensor:
        features = self.backbone(pixel_values)
        if self.config.drop_cls_token:
            features = features[:, 1:, :]

        # merge number of `hidden_stride * hidden_stride` hidden states together
        # to reduce token sequence length
        # e.g., for hidden_stride=2, this leads to a token length reduction:
        # 1024 -> 256 for aimv2
        if self.config.hidden_stride > 1:
            # this `d` maybe different from the above `d`
            n, L, d = features.shape
            sqrt_l = int(L**0.5)
            assert sqrt_l**2 == L, (
                "The token sequence length should be a perfect square."
            )
            features = features.reshape(n, sqrt_l, sqrt_l, d)
            pl = (
                self.config.hidden_stride - (sqrt_l % self.config.hidden_stride)
            ) % self.config.hidden_stride
            features = pad(features, (0, 0, 0, pl, 0, pl), "constant", 0)
            sqrt_l += pl
            features = features.reshape(
                n,
                sqrt_l // self.config.hidden_stride,
                self.config.hidden_stride,
                sqrt_l // self.config.hidden_stride,
                self.config.hidden_stride,
                d,
            )
            # [n, sqrt_l/hs, sqrt_l/hs, hs, hs, d]
            features = features.permute(0, 1, 3, 2, 4, 5)
            # [n, sqrt_l/hs, sqrt_l/hs, hs*hs*d]
            features = features.flatten(3)
            # [n, sqrt_l/hs*sqrt_l/hs, hs*hs*d]
            features = features.reshape(
                n, -1, self.config.hidden_stride * self.config.hidden_stride * d
            )

        return features

    defforward(self, pixel_values: torch.Tensor) -> torch.Tensor:
"""[BatchSize, ImageShape] -> [BatchSize, Token, VocabSize]"""
        features = self.encode(pixel_values)
        logits = self.head(features)
        tokens = self.tokenize(logits)
        # tokens' shape is [BatchSize, #Token, VocabSize-5], so padding with
        # [BatchSize, #Token, 5], after which, tokens' shape should become
        # [BatchSize, #Token, VocabSize]
        tokens = torch.nn.functional.pad(
            tokens,
            (0, len(IMAGE_INDICATOR_IDS)),
            mode="constant",
            value=0,
        )
        return tokens
```