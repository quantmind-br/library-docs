---
title: lfm2_vl - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/lfm2_vl/
source: sitemap
fetched_at: 2026-05-07T21:31:24.060819088-03:00
rendered_js: false
word_count: 0
summary: This class provides processing logic for vision-language models, specifically handling image tiling, grid layout calculation, and feature token generation.
tags:
    - computer-vision
    - image-processing
    - multimodal
    - vision-language-model
    - tensor-manipulation
category: concept
---

```
classLfm2VLProcessingInfo(BaseProcessingInfo):
    defget_hf_config(self):
        return self.ctx.get_hf_config(Lfm2VlConfig)

    defget_hf_processor(self, **kwargs):
        return self.ctx.get_hf_processor(Lfm2VlProcessor, **kwargs)

    defget_image_processor(self, **kwargs: object) -> Lfm2VlImageProcessorFast:
        return self.get_hf_processor(**kwargs).image_processor

    defget_default_tok_params(self) -> TokenizeParams:
        return super().get_default_tok_params().with_kwargs(add_special_tokens=False)

    defget_supported_mm_limits(self) -> Mapping[str, int | None]:
        return {"image": None}

    defget_image_size_with_most_features(self) -> ImageSize:
        processor = self.get_image_processor()
        max_image_tokens = processor.max_image_tokens
        encoder_patch_size = processor.encoder_patch_size
        downsample_factor = processor.downsample_factor
        max_pixels = max_image_tokens * (encoder_patch_size**2) * (downsample_factor**2)
        side = int(math.sqrt(max_pixels))
        return ImageSize(width=side, height=side)

    def_is_image_too_large(
        self,
        height: int,
        width: int,
        max_image_tokens: int,
        encoder_patch_size: int,
        downsample_factor: int,
        max_pixels_tolerance: float,
    ) -> bool:
"""Check if the image is too large to be processed as one tile."""
        total_factor = encoder_patch_size * downsample_factor

        h_bar = max(encoder_patch_size, round_by_factor(height, total_factor))
        w_bar = max(encoder_patch_size, round_by_factor(width, total_factor))
        return (
            h_bar * w_bar
            > max_image_tokens
            * encoder_patch_size**2
            * downsample_factor**2
            * max_pixels_tolerance
        )

    defsmart_resize(
        self,
        height: int,
        width: int,
        downsample_factor: int,
        min_image_tokens: int,
        max_image_tokens: int,
        encoder_patch_size: int,
    ) -> tuple[int, int]:
        total_factor = encoder_patch_size * downsample_factor
        smart_resize_min_pixels = (
            min_image_tokens * encoder_patch_size**2 * downsample_factor**2
        )
        smart_resize_max_pixels = (
            max_image_tokens * encoder_patch_size**2 * downsample_factor**2
        )

        h_bar = max(total_factor, round_by_factor(height, total_factor))
        w_bar = max(total_factor, round_by_factor(width, total_factor))

        if h_bar * w_bar > smart_resize_max_pixels:
            beta = math.sqrt((height * width) / smart_resize_max_pixels)
            h_bar = max(
                total_factor, math.floor(height / beta / total_factor) * total_factor
            )
            w_bar = max(
                total_factor, math.floor(width / beta / total_factor) * total_factor
            )
        elif h_bar * w_bar < smart_resize_min_pixels:
            beta = math.sqrt(smart_resize_min_pixels / (height * width))
            h_bar = math.ceil(height * beta / total_factor) * total_factor
            w_bar = math.ceil(width * beta / total_factor) * total_factor

        return w_bar, h_bar

    def_target_ratios(self, min_tiles: int, max_tiles: int) -> list[tuple[int, int]]:
        ratios = [
            (w, h)
            for n in range(min_tiles, max_tiles + 1)
            for w in range(1, n + 1)
            for h in range(1, n + 1)
            if min_tiles <= w * h <= max_tiles
        ]
        return sorted(set(ratios), key=lambda x: x[0] * x[1])

    def_get_grid_layout(
        self,
        height: int,
        width: int,
        min_tiles: int,
        max_tiles: int,
        tile_size: int,
    ) -> tuple[int, int, int]:
        aspect_ratio = width / height
        target_ratios = self._target_ratios(min_tiles, max_tiles)
        # find best matching grid configuration
        grid_width, grid_height = find_closest_aspect_ratio(
            aspect_ratio, target_ratios, width, height, tile_size
        )
        total_patches = grid_width * grid_height
        return grid_width, grid_height, total_patches

    def_get_image_feature_grid_size(
        self,
        image_width: int,
        image_height: int,
        processor: Lfm2VlProcessor,
        mm_kwargs: Mapping[str, object],
    ) -> tuple[int, int, int]:
        image_processor: Lfm2VlImageProcessorFast = processor.image_processor

        mm_kwargs = self.ctx.get_merged_mm_kwargs(mm_kwargs)
        downsample_factor = mm_kwargs.get(
            "downsample_factor", image_processor.downsample_factor
        )
        encoder_patch_size = mm_kwargs.get(
            "encoder_patch_size", image_processor.encoder_patch_size
        )
        max_pixels_tolerance = mm_kwargs.get(
            "max_pixels_tolerance", image_processor.max_pixels_tolerance
        )
        min_tiles = mm_kwargs.get("min_tiles", image_processor.min_tiles)
        max_tiles = mm_kwargs.get("max_tiles", image_processor.max_tiles)
        max_image_tokens = mm_kwargs.get(
            "max_image_tokens", image_processor.max_image_tokens
        )
        tile_size = mm_kwargs.get("tile_size", image_processor.tile_size)

        do_image_splitting = not min_tiles == max_tiles == 1
        is_image_large = self._is_image_too_large(
            height=image_height,
            width=image_width,
            max_image_tokens=max_image_tokens,
            encoder_patch_size=encoder_patch_size,
            downsample_factor=downsample_factor,
            max_pixels_tolerance=max_pixels_tolerance,
        )

        # Big image will be cropped into patches and small images are just resized
        if is_image_large and do_image_splitting:
            grid_width, grid_height, total_patches = self._get_grid_layout(
                image_height,
                image_width,
                min_tiles=min_tiles,
                max_tiles=max_tiles,
                tile_size=tile_size,
            )
        else:
            grid_width = grid_height = total_patches = 1

        if grid_width * grid_height != 1:  # Thumbnail
            total_patches += 1

        return grid_width, grid_height, total_patches

    defget_num_patches(
        self,
        *,
        image_width: int,
        image_height: int,
        processor: Lfm2VlProcessor,
        mm_kwargs: Mapping[str, object],
    ) -> int:
        _, _, total_patches = self._get_image_feature_grid_size(
            image_width=image_width,
            image_height=image_height,
            processor=processor,
            mm_kwargs=mm_kwargs,
        )
        return total_patches

    defget_image_repl(
        self,
        image_width: int,
        image_height: int,
        spatial_shapes: torch.Tensor,
        processor: Lfm2VlProcessor,
        mm_kwargs: Mapping[str, object],
    ) -> str:
        grid_placeholder = "<|img_row_{n_h}_col_{n_w}|>"
        image_token = processor.image_token
        image_start_token = processor.image_start_token
        image_end_token = processor.image_end_token
        image_thumbnail_token = processor.image_thumbnail_token

        num_thumbnail_tokens, num_tokens_per_tile = self.get_num_image_tokens(
            spatial_shapes=spatial_shapes,
            processor=processor,
            mm_kwargs=mm_kwargs,
        )
        tile_img_placeholder = grid_placeholder + (image_token * num_tokens_per_tile)

        grid_w, grid_h, _ = self._get_image_feature_grid_size(
            image_width=image_width,
            image_height=image_height,
            processor=processor,
            mm_kwargs=mm_kwargs,
        )

        if grid_w > 1 or grid_h > 1:
            tiles_placeholder: list[str] = [
                tile_img_placeholder.format(n_h=i + 1, n_w=j + 1)
                for i in range(grid_h)
                for j in range(grid_w)
            ]

            if num_thumbnail_tokens > 0:
                tiles_placeholder.append(
                    image_thumbnail_token + (image_token * num_thumbnail_tokens)
                )
        else:
            tiles_placeholder = [image_token * num_thumbnail_tokens]

        placeholder = "".join(
            itertools.chain([image_start_token], tiles_placeholder, [image_end_token])
        )
        return placeholder

    defget_num_image_tokens(
        self,
        *,
        spatial_shapes: torch.Tensor,
        processor: Lfm2VlProcessor,
        mm_kwargs: Mapping[str, object],
    ) -> tuple[int, int]:
        image_processor: Lfm2VlImageProcessorFast = processor.image_processor

        mm_kwargs = self.ctx.get_merged_mm_kwargs(mm_kwargs)
        downsample_factor = mm_kwargs.get(
            "downsample_factor", image_processor.downsample_factor
        )
        encoder_patch_size = mm_kwargs.get(
            "encoder_patch_size", image_processor.encoder_patch_size
        )
        tile_size = mm_kwargs.get("tile_size", image_processor.tile_size)

        thumbnail_height_patches = int(spatial_shapes[-1][0].item())
        thumbnail_width_patches = int(spatial_shapes[-1][1].item())
        # HF computes thumbnail tokens as
        # ceil(h_patches / downsample_factor) * ceil(w_patches / downsample_factor).
        # We assert divisibility here so any processor/model drift is surfaced
        # immediately instead of being hidden by floor division.
        assert thumbnail_height_patches % downsample_factor == 0, (
            "LFM2-VL thumbnail height patch grid must be divisible by "
            f"downsample_factor, got height_patches={thumbnail_height_patches}, "
            f"downsample_factor={downsample_factor}"
        )
        assert thumbnail_width_patches % downsample_factor == 0, (
            "LFM2-VL thumbnail width patch grid must be divisible by "
            f"downsample_factor, got width_patches={thumbnail_width_patches}, "
            f"downsample_factor={downsample_factor}"
        )
        num_thumbnail_tokens = math.ceil(
            thumbnail_height_patches / downsample_factor
        ) * math.ceil(thumbnail_width_patches / downsample_factor)
        num_patches_tile = tile_size // encoder_patch_size
        dwn_num_patches_tile = math.ceil(num_patches_tile / downsample_factor)
        num_tiles_tokens = dwn_num_patches_tile * dwn_num_patches_tile

        return num_thumbnail_tokens, num_tiles_tokens
```