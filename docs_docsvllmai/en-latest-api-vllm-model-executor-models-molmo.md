---
title: molmo - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/molmo/
source: sitemap
fetched_at: 2026-05-07T21:32:05.029564795-03:00
rendered_js: false
word_count: 0
summary: This document defines the MolmoVisionBackbone class, which serves as a neural network module for processing and projecting image embeddings in a vision-language model architecture.
tags:
    - pytorch
    - vision-transformer
    - image-processing
    - multimodal-model
    - neural-network-backbone
    - deep-learning
category: reference
---

```
classMolmoVisionBackbone(nn.Module, SupportsQuant):
    packed_modules_mapping = {"merged_linear": ["gate_proj", "up_proj"]}

    def__init__(
        self,
        config: PretrainedConfig,
        vision_config: VisionBackboneConfig,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ) -> None:
        super().__init__()
        self.vit_layers = VIT_LAYERS
        self.image_num_patch = vision_config.image_num_patch
        self.llm_patches_per_crop = (
            (self.image_num_patch[0] + 1) // POOLING_SIZE,
            (self.image_num_patch[1] + 1) // POOLING_SIZE,
        )
        self.image_vit = VisionTransformer(
            vision_config, quant_config=quant_config, prefix=f"{prefix}.image_vit"
        )
        self.num_prefix_tokens = self.image_vit.num_prefix_tokens
        assert self.num_prefix_tokens in {0, 1}, (
            "Only 0 or 1 prefix tokens are supported"
        )
        self.image_pooling_2d = MultiHeadDotProductAttention(
            vision_config,
            nlayers=len(self.vit_layers),
            quant_config=quant_config,
            prefix=f"{prefix}.image_pooling_2d",
        )
        self.image_projector = ImageProjectorMLP(
            config,
            input_dim=vision_config.image_emb_dim,
            quant_config=quant_config,
            prefix=f"{prefix}.image_projector",
        )

        image_dim = vision_config.image_emb_dim * len(self.vit_layers)
        self.pad_embed = nn.Parameter(torch.zeros((2, image_dim)))

    @property
    defdtype(self) -> torch.dtype:
        return self.image_vit.patch_embedding.weight.dtype

    @property
    defdevice(self) -> torch.device:
        return self.image_vit.patch_embedding.weight.device

    defencode_image(self, images: torch.Tensor) -> torch.Tensor:
"""
        : param images: (batch_size, num_crops, num_patch, n_pixels)
        """
        B, T, N, D = images.shape

        mask = ~torch.all(images.view(B * T, N, D) == -1, dim=(1, 2), keepdim=True)

        images = images.view(B * T, N, D)
        image_features = self.image_vit(images)

        if self.vit_layers is not None:
            features = []
            for layer in self.vit_layers:
                features.append(image_features[layer])
            image_features = torch.cat(features, dim=-1)
        else:
            image_features = image_features[-1]

        if self.num_prefix_tokens > 0:
            image_features = image_features[:, 1:]

        image_features = image_features * mask
        image_features = image_features.view(B, T, N, -1)

        return image_features

    defforward(
        self,
        images: torch.Tensor,
        image_masks: torch.Tensor,
    ) -> torch.Tensor:
        # image_features: (batch_size, num_crops(=num_image), num_patch, nximage_emb_dim) # noqa: E501
        batch_size, num_image = images.shape[:2]
        images = images.to(device=self.device, dtype=self.dtype)
        image_features = self.encode_image(images)

        og_dtype = image_features.dtype
        assert image_masks is not None
        pad_embed = self.pad_embed[:, None, None, None, :]
        all_pad = image_masks == 0
        partial_pad = torch.logical_and(image_masks < 1, torch.logical_not(all_pad)).to(
            dtype=torch.float32
        )
        all_pad = all_pad.to(dtype=torch.float32)
        image_features = image_features + pad_embed[0] * torch.unsqueeze(all_pad, -1)
        image_features = image_features + pad_embed[1] * torch.unsqueeze(
            partial_pad, -1
        )

        image_features = image_features.to(og_dtype)

        image_features = image_features.reshape(
            (batch_size, num_image) + self.image_num_patch + (-1,),
        )

        if missing_w := self.image_num_patch[0] % POOLING_SIZE:
            # Padding for image pooling (see below)
            image_features = F.pad(
                image_features,
                (0, 0, 0, missing_w, 0, missing_w, 0, 0, 0, 0),
            )

        # image pooling
        image_features = rearrange(
            image_features,
            "b n (h dh) (w dw) c -> (b n h w) (dh dw) c",
            dh=POOLING_SIZE,
            dw=POOLING_SIZE,
        )

        query = image_features.mean(-2, keepdim=True)
        image_features = self.image_pooling_2d(query, image_features)

        h, w = self.llm_patches_per_crop
        image_features = image_features.view(batch_size, num_image, h * w, -1)

        image_features = self.image_projector(image_features)

        # image_features: (batch_size, num_image, num_patch, d_model)
        return image_features

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        stacked_params_mapping = [
            # (param_name, shard_name, shard_id)
            ("merged_linear", "gate_proj", 0),
            ("merged_linear", "up_proj", 1),
        ]
        params_dict = dict(self.named_parameters())
        loaded_params: set[str] = set()

        for name, loaded_weight in weights:
            for param_name, weight_name, shard_id in stacked_params_mapping:
                if weight_name not in name:
                    continue
                name = name.replace(weight_name, param_name)
                # Skip loading extra bias for GPTQ models.
                if name.endswith(".bias") and name not in params_dict:
                    continue
                if is_pp_missing_parameter(name, self):
                    continue
                param = params_dict[name]
                weight_loader = param.weight_loader
                weight_loader(param, loaded_weight, shard_id)
                break
            else:
                if name.endswith(".bias") and name not in params_dict:
                    continue
                if is_pp_missing_parameter(name, self):
                    continue
                param = params_dict[name]
                weight_loader = getattr(param, "weight_loader", default_weight_loader)
                weight_loader(param, loaded_weight)
            loaded_params.add(name)
        return loaded_params
```