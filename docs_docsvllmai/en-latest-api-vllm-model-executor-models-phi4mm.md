---
title: phi4mm - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/phi4mm/
source: sitemap
fetched_at: 2026-05-07T21:32:38.197989882-03:00
rendered_js: false
word_count: 0
summary: This document defines the Phi4MMImageEncoder module, which processes input image data into visual embeddings for a multimodal model using a vision processor, spatial compression, and HD transformation techniques.
tags:
    - phi-4
    - multimodal
    - vision-encoder
    - image-processing
    - feature-extraction
    - pytorch
category: concept
---

```
classPhi4MMImageEncoder(nn.Module):
"""Image embedding."""

    def__init__(
        self,
        config: PretrainedConfig,
        quant_config: QuantizationConfig | None,
        prefix: str = "",
        model_dir: str = "",
    ) -> None:
        super().__init__()

        # n_embed or hidden_size
        hidden_size = config.n_embd if hasattr(config, "n_embd") else config.hidden_size

        # layer_idx to output the img features
        if isinstance(config.img_processor, dict):
            self.layer_idx = config.img_processor.get("layer_idx", -2)
            self.type_feature = config.img_processor.get("type_feature", "patch")
        else:
            self.layer_idx = -2
            self.type_feature = "patch"

        self.img_processor = get_navit_vision_model(layer_idx=self.layer_idx)

        pe_weight = self.img_processor.embeddings.position_embedding.weight
        L, D = pe_weight.size()
        H = int(math.sqrt(L))
        assert H**2 == L, f"position embedding size {L} is not square"
        if H % 2 != 0:
            self.img_processor_padding = nn.ReflectionPad2d((0, 1, 0, 1))
            H += 1
        image_dim_out = D
        # ((448/14)//2)**2
        self.num_img_tokens = (H // 2) ** 2
        self.base_feat_height_target = H

        self.image_dim_out = image_dim_out
        self.img_sizes = None
        self.image_attention_mask = None

        # global_gn and sub_gn for hd transform, serves as line separator
        self.use_hd_transform = True
        self.with_learnable_separator = True
        self.hd_transform_order = "sub_glb"
        self.freeze_img_processor = False
        self.crop_size = 448

        # image token compression
        self.image_token_compression_cls = "avg_pool_2d"
        self.image_token_compression = nn.AvgPool2d(kernel_size=2, stride=2)
        self.base_feat_height_reduction = 1
        self.base_feat_height_target = self.base_feat_height_target // 2

        # with_hd_transform and with_learnable_separator should have same value
        assert self.use_hd_transform == self.with_learnable_separator, (
            "use_hd_transform and with_learnable_separator should have same value"
        )
        assert self.use_hd_transform, "learnable separator is only for hd transform"
        # 1024 * 4, merge spatial to channel dimension
        self.glb_GN = nn.Parameter(
            torch.zeros([1, 1, self.image_dim_out * self.base_feat_height_reduction**2])
        )
        self.sub_GN = nn.Parameter(
            torch.zeros(
                [1, 1, 1, self.image_dim_out * self.base_feat_height_reduction**2]
            )
        )

        dim_projection = hidden_size
        depth = 2
        layers = [
            nn.Linear(
                image_dim_out * self.base_feat_height_reduction**2, dim_projection
            )
        ]
        for _ in range(1, depth):
            layers.extend([nn.GELU(), nn.Linear(dim_projection, dim_projection)])
        self.img_projection = nn.Sequential(*layers)

        self.vocab_size = config.vocab_size
        self.img_features = None

        self.use_out_place_operations = False

    defget_img_features(
        self, img_embeds: torch.FloatTensor, attention_mask=None
    ) -> torch.FloatTensor:
        img_feature = self.img_processor(
            img_embeds, patch_attention_mask=attention_mask
        )

        if self.type_feature == "patch":
            patch_feature = img_feature

            use_token_compression = self.image_token_compression is not None
            use_padding = getattr(self, "img_processor_padding", None) is not None
            if use_token_compression or use_padding:
                # reshape to 2D tensor
                width = int(math.sqrt(patch_feature.size(1)))
                patch_feature = patch_feature.view(
                    -1, width, width, patch_feature.size(-1)
                )
                # convert to NCHW
                patch_feature = patch_feature.permute(0, 3, 1, 2)

                if use_padding:
                    patch_feature = self.img_processor_padding(patch_feature)
                if use_token_compression:
                    patch_feature = self.image_token_compression(patch_feature)

                # convert to NHWC
                patch_feature = patch_feature.permute(0, 2, 3, 1)
                patch_feature = patch_feature.view(
                    -1,
                    patch_feature.size(1) * patch_feature.size(2),
                    patch_feature.size(-1),
                )

            return patch_feature

        raise NotImplementedError

    defforward(
        self,
        pixel_values: torch.FloatTensor,
        image_sizes: torch.Tensor,
        image_attention_mask: torch.Tensor,
    ) -> list[torch.FloatTensor]:
"""
        process image and return vision embeddings.

        pixel_values: (num_images, num_crops, c, h, w)
        image_sizes: [[h1, w1], [h2, w2]]
        image_attention_mask: num_images x num_crops x 32 x 32
        output: (num_images, num_img_tokens, hidden_size)
        """

        # eg
        # pixel_values: torch.Size([1, 7, 3, 448, 448])
        # image_sizes: tensor([[ 896, 1344]], device='cuda:0')
        # output: torch.Size([1, 1841, 3072])

        if isinstance(self.img_projection, nn.Sequential):
            target_device = self.img_projection[0].bias.device
            target_dtype = self.img_projection[0].bias.dtype
        else:  # It's a single nn.Linear layer
            target_device = self.img_projection.bias.device
            target_dtype = self.img_projection.bias.dtype

        img_sizes = image_sizes
        num_images, num_crops, c, h, w = pixel_values.shape
        bs = num_images
        pixel_values = pixel_values.flatten(0, 1)

        img_features = self.get_img_features(
            pixel_values,
            image_attention_mask.type(torch.BoolTensor).flatten(0, 1).to(target_device),
        )

        base_feat_height_target = self.base_feat_height_target
        base_resolution = self.crop_size
        base_feat_height_reduction = self.base_feat_height_reduction

        base_feat_height = base_feat_width = int(np.sqrt(img_features.shape[1]))
        assert (
            base_feat_height == base_feat_height_target
            and base_feat_width == base_feat_height_target
        ), (
            f"base_feat_height: {base_feat_height}, "
            f"base_feat_width: {base_feat_width}, "
            f"expect {base_feat_height_target} features for hd transform"
        )

        # bs x max_num_crops x (24x24) x C
        img_features = img_features.view(
            bs, -1, base_feat_height * base_feat_width, self.image_dim_out
        )
        C = self.image_dim_out
        H = base_feat_height

        output_imgs = []
        output_len = []
        # training is tensor, inference is list
        if isinstance(img_sizes, torch.Tensor):
            img_sizes = img_sizes.view(-1, 2)
        for _bs in range(bs):
            h, w = img_sizes[_bs]
            h = h // base_resolution
            w = w // base_resolution
            B_ = h * w

            # 1 x (24x24) x 1024
            global_img_feature = img_features[_bs, :1]

            # 1 x 12 x 12 x 4096
            glb_img = (
                global_img_feature.reshape(1, H, H, C)
                .reshape(
                    1,
                    H // base_feat_height_reduction,
                    base_feat_height_reduction,
                    H // base_feat_height_reduction,
                    base_feat_height_reduction,
                    C,
                )
                .contiguous()
                .permute(0, 1, 3, 2, 4, 5)
                .reshape(
                    1,
                    H // base_feat_height_reduction,
                    H // base_feat_height_reduction,
                    base_feat_height_reduction * base_feat_height_reduction * C,
                )
                .contiguous()
            )
            temp_glb_GN = self.sub_GN.repeat(1, H // base_feat_height_reduction, 1, 1)

            # 1 x 156 x 4096
            glb_img = torch.cat([glb_img, temp_glb_GN], dim=2).reshape(
                1, -1, base_feat_height_reduction * base_feat_height_reduction * C
            )

            # (max_num_crops-1) x (12x12) x C
            sub_img = img_features[_bs, 1:]
            # 16x574x1024
            # get rid of padding sub_img
            sub_img = sub_img[:B_]

            # (num_crops, 12, 2, 12, 2, 1024) ->
            # (num_crops, 12, 12, 2, 2, 1024) -> (num_crops, 12*12, 4*1024)
            sub_img = (
                sub_img.reshape(B_, H, H, C)
                .reshape(
                    B_,
                    H // base_feat_height_reduction,
                    base_feat_height_reduction,
                    H // base_feat_height_reduction,
                    base_feat_height_reduction,
                    C,
                )
                .contiguous()
                .permute(0, 1, 3, 2, 4, 5)
                .reshape(
                    B_, -1, base_feat_height_reduction * base_feat_height_reduction * C
                )
                .contiguous()
            )
            sub_img = (
                sub_img.reshape(
                    1,
                    h,
                    w,
                    base_feat_height // base_feat_height_reduction,
                    base_feat_width // base_feat_height_reduction,
                    -1,
                )
                .permute(0, 1, 3, 2, 4, 5)
                .reshape(
                    1,
                    h * base_feat_height // base_feat_height_reduction,
                    w * base_feat_width // base_feat_height_reduction,
                    base_feat_height_reduction * base_feat_height_reduction * C,
                )
            )

            if image_attention_mask is not None and len(image_attention_mask) > 0:
                reshaped_image_attention_mask = (
                    image_attention_mask[_bs, 1 : B_ + 1, 0::2, 0::2]
                    .reshape(
                        1,
                        h,
                        w,
                        base_feat_height // base_feat_height_reduction,
                        base_feat_width // base_feat_height_reduction,
                    )
                    .permute(0, 1, 3, 2, 4)
                    .reshape(
                        1,
                        h * base_feat_height // base_feat_height_reduction,
                        w * base_feat_width // base_feat_height_reduction,
                    )
                )
                useful_height = int(reshaped_image_attention_mask[0, :, 0].sum().item())
                useful_width = int(reshaped_image_attention_mask[0, 0, :].sum().item())
                sub_img = sub_img[:, :useful_height, :useful_width]
                temp_sub_GN = self.sub_GN.repeat(1, useful_height, 1, 1)
                temp_len = (
                    int(image_attention_mask[_bs, : B_ + 1, 0::2, 0::2].sum().item())
                    + (useful_height + 1)
                    + base_feat_height // base_feat_height_reduction
                )
            else:
                temp_sub_GN = self.sub_GN.repeat(
                    1, h * base_feat_height // base_feat_height_reduction, 1, 1
                )
                temp_len = int(
                    (h * w + 1) * self.num_img_tokens
                    + 1
                    + (h + 1) * base_feat_height // base_feat_height_reduction
                )

            sub_img = torch.cat([sub_img, temp_sub_GN], dim=2).reshape(
                1, -1, base_feat_height_reduction * base_feat_height_reduction * C
            )
            # (1, num_img_tokens, 1024*4)

            # glb + sub
            if self.hd_transform_order == "glb_sub":
                output_imgs.append(torch.cat([glb_img, self.glb_GN, sub_img], dim=1))
            elif self.hd_transform_order == "sub_glb":
                output_imgs.append(torch.cat([sub_img, self.glb_GN, glb_img], dim=1))
            else:
                raise NotImplementedError(
                    f"hd_transform_order = {self.hd_transform_order}, not implemented"
                )

            # temp_len = int((h*w+1)*144 + 1 + (h+1)*12)
            assert temp_len == output_imgs[-1].shape[1], (
                f"temp_len: {temp_len}, output_imgs[-1].shape[1]: "
                f"{output_imgs[-1].shape[1]}"
            )

            output_len.append(temp_len)

        img_set_tensor = []
        for _output_img in output_imgs:
            img_feature_proj = self.img_projection(
                _output_img.to(target_device).to(target_dtype)
            )
            img_set_tensor.append(img_feature_proj.squeeze(0))

        return img_set_tensor
```