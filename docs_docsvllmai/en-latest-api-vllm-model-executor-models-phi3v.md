---
title: phi3v - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/phi3v/
source: sitemap
fetched_at: 2026-05-07T21:32:37.213160851-03:00
rendered_js: false
word_count: 13
summary: This code implements the Phi-3 HD image embedding module, which processes high-definition image features by applying spatial transformations, 2x2 patch merging, and learnable separators for vision-language models.
tags:
    - phi-3
    - image-embedding
    - hd-transform
    - computer-vision
    - pytorch
    - multimodal-model
category: concept
---

```
classPhi3HDImageEmbedding(nn.Module):
"""Phi3 Image embedding with HD transform."""

    def__init__(
        self,
        config: PretrainedConfig,
        quant_config: QuantizationConfig | None,
        prefix: str = "",
    ) -> None:
        super().__init__()

        # n_embed or hidden_size
        hidden_size = config.n_embd if hasattr(config, "n_embd") else config.hidden_size

        self.img_processor = _init_img_processor(
            config,
            quant_config=quant_config,
            prefix=f"{prefix}.img_processor",
        )

        image_dim_out = config.img_processor["image_dim_out"]
        self.num_img_tokens = config.img_processor["num_img_tokens"]

        self.image_dim_out = image_dim_out

        # global_gn and sub_gn for hd transform, serves as line separator
        self.use_hd_transform = config.embd_layer.get("use_hd_transform", False)
        self.with_learnable_separator = config.embd_layer.get(
            "with_learnable_separator", False
        )
        self.hd_transform_order = config.embd_layer.get("hd_transform_order", "glb_sub")
        # with_hd_transform and with_learnable_separator should have same value
        assert self.use_hd_transform and self.with_learnable_separator

        # 1024 * 4, merge spatial to channel dimension
        self.glb_GN = nn.Parameter(torch.empty([1, 1, self.image_dim_out * 4]))
        self.sub_GN = nn.Parameter(torch.empty([1, 1, 1, self.image_dim_out * 4]))

        dim_projection = hidden_size
        depth = 2
        layers: list[nn.Module] = [nn.Linear(image_dim_out * 4, dim_projection)]
        for _ in range(1, depth):
            layers.extend([nn.GELU(), nn.Linear(dim_projection, dim_projection)])
        self.img_projection = nn.Sequential(*layers)

        self.type_feature = config.img_processor.get("type_feature", "patch")

    defget_img_features(self, img_embeds: torch.FloatTensor) -> torch.FloatTensor:
        type_feature = self.type_feature

        # NOTE: we skip the step to select the vision feature layer since
        # this is already done inside the img_processor
        img_feature = self.img_processor(img_embeds)

        if type_feature == "patch":
            patch_feature = img_feature[:, 1:]
            return patch_feature

        if type_feature == "cls_patch":
            return img_feature

        raise NotImplementedError(type_feature)

    defforward(
        self, pixel_values: torch.FloatTensor, image_sizes: torch.Tensor
    ) -> torch.FloatTensor:
"""
        process image and return vision embeddings.

        pixel_values: (num_images, num_crops, c, h, w)
        output: (num_images, num_img_tokens, hidden_size)
        """
        num_images, num_crops, c, h, w = pixel_values.shape
        pixel_values = pixel_values.flatten(0, 1)
        img_features = self.get_img_features(pixel_values)
        img_features = img_features.reshape(
            num_images, num_crops, -1, self.image_dim_out
        )
        image_features_proj = self.hd_feature_transform(img_features, image_sizes)
        return image_features_proj

    defhd_feature_transform(self, image_features, image_sizes):
"""
        image_features: (num_images, num_crops+1, 24*24, 1024)
        """
        assert self.hd_transform_order == "sub_glb", (
            f"hd_transform_order `{self.hd_transform_order}` not implemented"
        )
        if isinstance(self.img_projection, nn.Sequential):
            target_device = self.img_projection[0].bias.device
            target_dtype = self.img_projection[0].bias.dtype
        else:  # It's a single nn.Linear layer
            target_device = self.img_projection.bias.device
            target_dtype = self.img_projection.bias.dtype

        global_image_features = image_features[:, 0]  # (num_images, 24*24, 1024)
        # global feature can be viewed as a special HD case with num_crops 1x1
        global_image_features_hd = self.reshape_hd_patches_2x2merge(
            global_image_features, 1, 1
        )
        global_image_features_hd_newline = self.add_image_newline(
            global_image_features_hd
        )

        batch_image_features_proj = []
        # need a for loop to process each image because of different image sizes
        # (patch arrangement is different for each image)
        for i, img_size in enumerate(image_sizes):
            h, w = img_size
            h_crop = h // 336
            w_crop = w // 336
            num_crops = h_crop * w_crop

            # NOTE: real num_crops is padded
            # (num_crops, 24*24, 1024)
            sub_image_features = image_features[i, 1 : 1 + num_crops]
            sub_image_features_hd = self.reshape_hd_patches_2x2merge(
                sub_image_features, h_crop, w_crop
            )
            sub_image_features_hd_newline = self.add_image_newline(
                sub_image_features_hd
            )

            # [sub features, separator, global features]
            image_embeddings = torch.cat(
                [
                    sub_image_features_hd_newline.squeeze(
                        0
                    ),  # (h_crop*12*(w_crop*12+1), 4096)
                    self.glb_GN.squeeze(0),
                    global_image_features_hd_newline[i],
                ]
            )
            img_proj = self.img_projection(
                image_embeddings.to(target_device, target_dtype)
            )
            batch_image_features_proj.append(img_proj)

        return batch_image_features_proj

    defreshape_hd_patches_2x2merge(self, image_features, h_crop, w_crop):
"""
        image_features: (num_images*num_crops, 24*24, 1024)
        output: (num_images, h_crop*12, w_crop*12, 4096)
        where h_crop*w_crop == num_crops
        """
        N, L, C = image_features.shape
        assert L == 576 and C == 1024 and N % (h_crop * w_crop) == 0
        num_images = N // (h_crop * w_crop)
        H = int(L**0.5)
        image_features_hd = (
            image_features.reshape(N, H, H, C)  # N, 24, 24, 1024
            .reshape(N, H // 2, 2, H // 2, 2, C)  # N, 12, 2, 12, 2, 1024
            .permute(0, 1, 3, 2, 4, 5)  # N, 12, 12, 2, 2, 1024
            .reshape(N, -1, 4 * C)  # N, 144, 4096
            .reshape(
                num_images, h_crop, w_crop, H // 2, H // 2, -1
            )  # n_img, h_crop, w_crop, 12, 12, 4096
            .permute(0, 1, 3, 2, 4, 5)  # n_img, h_crop, 12, w_crop, 12, 4096
            .reshape(
                num_images, h_crop * H // 2, w_crop * H // 2, 4 * C
            )  # n_img, h_crop*12, w_crop*12, 4096
        )
        return image_features_hd

    defadd_image_newline(self, image_features_hd):
"""
        image_features_hd: (num_images, h_crop*12, w_crop*12, 4096)
        output: (num_images, (h_crop*12) * (w_crop*12+1), 4096)
        """
        num_images, h, w, hid_dim = image_features_hd.shape
        # add the newline token to the HD image feature patches
        newline_embeddings = self.sub_GN.expand(
            num_images, h, -1, -1
        )  # (n_img, h, 1, hid_dim)
        image_features_hd_newline = torch.cat(
            [image_features_hd, newline_embeddings], dim=2
        ).reshape(num_images, -1, hid_dim)
        return image_features_hd_newline
```