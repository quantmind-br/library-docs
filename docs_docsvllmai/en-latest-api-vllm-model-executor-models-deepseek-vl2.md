---
title: deepseek_vl2 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/deepseek_vl2/
source: sitemap
fetched_at: 2026-05-07T21:29:42.913443821-03:00
rendered_js: false
word_count: 0
summary: This document defines the model architecture and processing logic for the Deepseek-VL2 multimodal model, including vision encoder integration, projector implementation, and tensor-parallel support within the vLLM framework.
tags:
    - deepseek-vl2
    - multimodal-model
    - vision-encoder
    - vllm-framework
    - tensor-parallelism
    - pytorch-module
category: reference
---

```
@MULTIMODAL_REGISTRY.register_processor(
    DeepseekVL2MultiModalProcessor,
    info=DeepseekVL2ProcessingInfo,
    dummy_inputs=DeepseekVL2DummyInputsBuilder,
)
classDeepseekVLV2ForCausalLM(nn.Module, SupportsMultiModal, SupportsPP):
    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            "language.": "language_model.",
        }
    )

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return "<image>"

        raise ValueError("Only image modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        config: DeepseekVLV2Config = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config
        multimodal_config = vllm_config.model_config.multimodal_config

        self.config = config
        self.multimodal_config = multimodal_config

        self.vision_config = config.vision_config
        self.projector_config = config.projector_config
        self.text_config = config.text_config

        model_config = vllm_config.model_config
        tokenizer = cached_tokenizer_from_config(model_config)
        self.image_token_id: int = tokenizer.vocab[_IMAGE_TOKEN]

        with self._mark_tower_model(vllm_config, "image"):
            self.vision = self._init_vision_module(
                self.vision_config, quant_config, maybe_prefix(prefix, "vision")
            )

            self.projector = MlpProjector(self.projector_config)
            self.tile_tag = config.tile_tag
            self.global_view_pos = config.global_view_pos

            # special token for image token sequence format
            embed_std = 1 / torch.sqrt(
                torch.tensor(self.projector_config.n_embed, dtype=torch.float32)
            )
            if self.tile_tag == "2D":
                # <|view_seperator|>, <|\n|>
                self.image_newline = nn.Parameter(
                    torch.randn(self.projector_config.n_embed) * embed_std
                )
                # This is a typo in original implementation
                self.view_seperator = nn.Parameter(
                    torch.randn(self.projector_config.n_embed) * embed_std
                )
            else:
                raise ValueError(
                    f"Only 2D tile_tag is supported currently, got: {self.tile_tag}"
                )

        with self._mark_language_model(vllm_config):
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config,
                hf_config=self.text_config,
                prefix=maybe_prefix(prefix, "language"),
            )

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

    def_get_parent_and_attr(self, root: torch.nn.Module, dotted_name: str):
"""Return (parent_module, final_attr_name) for a dotted module path."""
        names = dotted_name.split(".")
        parent = root
        for n in names[:-1]:
            parent = getattr(parent, n)
        return parent, names[-1]

    # patch for timm ViT instance to support tensor parallel
    defpatch_vit_for_tp(self, vit: torch.nn.Module, quant_config: QuantizationConfig):
        try:
            importtimm
        except ImportError as e:
            raise ImportError("Please install timm") frome

        for name, module in vit.named_modules():
            if isinstance(module, nn.Linear):
                parent, attr_name = self._get_parent_and_attr(vit, name)
                if isinstance(parent, timm.layers.Mlp) and attr_name == "fc1":
                    new_linear = replace_linear_class(
                        module, "colwise", quant_config, prefix=name
                    )
                    setattr(parent, attr_name, new_linear)
                elif isinstance(parent, timm.layers.Mlp) and attr_name == "fc2":
                    new_linear = replace_linear_class(
                        module, "rowwise", quant_config, prefix=name
                    )
                    setattr(parent, attr_name, new_linear)

        return vit

    def_init_vision_module(
        self,
        vision_config: VisionEncoderConfig,
        quant_config: QuantizationConfig | None,
        prefix: str = "",
    ) -> nn.Module:
        # TODO: refactor vision model through timm wrapper from transformers
        try:
            importtimm
        except ImportError as e:
            raise ImportError("Please install timm") frome

        with set_default_torch_dtype(torch.float16):
            model = timm.create_model(
                "vit_so400m_patch14_siglip_384.webli",
                pretrained=False,
                num_classes=0,
                dynamic_img_size=True,
                dynamic_img_pad=True,
            )

        if get_tensor_model_parallel_world_size() > 1:
            model = self.patch_vit_for_tp(model, quant_config)

        model = model.to(dtype=torch.get_default_dtype())
        return model

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> DeepseekVL2ImageInputs | None:
        pixel_values = kwargs.pop("pixel_values", None)
        images_spatial_crop = kwargs.pop("images_spatial_crop", None)
        image_embeds = kwargs.pop("image_embeds", None)

        if pixel_values is None and image_embeds is None:
            return None

        if pixel_values is not None:
            expected_h = expected_w = self.vision_config.image_size
            return DeepseekVL2ImagePixelInputs(
                type="pixel_values",
                data=pixel_values,
                images_spatial_crop=images_spatial_crop,
                resolve_bindings={
                    "h": expected_h,
                    "w": expected_w,
                },
            )

        if image_embeds is not None:
            return DeepseekVL2VImageEmbeddingInputs(
                type="image_embeds",
                data=image_embeds,
            )

        raise AssertionError("This line should be unreachable.")

    def_pixel_values_to_embedding(
        self,
        pixel_values: torch.Tensor,
        images_spatial_crop: torch.Tensor,
    ) -> list[torch.Tensor]:
        # [batch_all_tiles, vit_seq_len, c]
        images_feature = self.vision.forward_features(pixel_values)

        # [batch_all_tiles, hw, D]
        images_embeds = self.projector(images_feature)

        _, hw, n_dim = images_embeds.shape
        h = w = int(hw**0.5)

        # fill image token based on self.tile_tag & self.global_view_pos
        tile_index = 0
        vision_embeddings = []
        for jdx in range(images_spatial_crop.size(0)):
            # extra global & local features
            num_width_tiles, num_height_tiles = images_spatial_crop[jdx]
            if num_width_tiles == 0 or num_height_tiles == 0:
                break
            num_tiles_in_image = num_width_tiles * num_height_tiles

            # [hw, D]
            global_features = images_embeds[tile_index]

            # [num_height_tiles * num_width_tiles, hw, D]
            local_features = images_embeds[
                tile_index + 1 : tile_index + 1 + num_tiles_in_image
            ]
            tile_index += num_tiles_in_image + 1

            # format global and local features
            # ----------------- global view add newline -----------------
            # [hw, D] -> [h, w, D]
            global_features = global_features.view(h, w, n_dim)

            # [D]     -> [h, 1, D]
            new_lines_in_global = repeat(self.image_newline, "d -> h 1 d", h=h)

            # cat([h, w, D], [h, 1, D], dim=1) -> [h, w + 1, D]
            global_features = torch.cat([global_features, new_lines_in_global], dim=1)

            # [h, w + 1, D] -> [h * (w + 1), D]
            global_features = global_features.view(-1, n_dim)

            # ----------------- local view add newline -----------------
            # [num_height_tiles * num_width_tiles, h * w, D] ->
            # [num_height_tiles * h, num_width_tiles * w, D]
            local_features = rearrange(
                local_features,
                "(th tw) (h w) d -> (th h) (tw w) d",
                th=num_height_tiles,
                tw=num_width_tiles,
                h=h,
                w=w,
            )

            # [D] -> [num_height_tiles * h, 1, D]
            new_lines_in_local = repeat(
                self.image_newline, "d -> (th h) 1 d", th=num_height_tiles, h=h
            )

            # [num_height_tiles * h, num_width_tiles * w + 1, D]
            local_features = torch.cat([local_features, new_lines_in_local], dim=1)

            # [num_height_tiles * h, num_width_tiles * w + 1, D]
            #   --> [(num_height_tiles * h) * (num_width_tiles * w + 1), D]
            local_features = local_features.view(-1, n_dim)

            # merge global and local tiles
            if self.global_view_pos == "head":
                global_local_features = torch.cat(
                    [
                        global_features,
                        self.view_seperator[None, :],
                        local_features,
                    ]
                )
            else:
                global_local_features = torch.cat(
                    [
                        local_features,
                        self.view_seperator[None, :],
                        global_features,
                    ]
                )

            vision_embeddings.append(global_local_features)
        return vision_embeddings

    def_process_image_input(
        self, image_input: DeepseekVL2ImageInputs
    ) -> torch.Tensor | list[torch.Tensor]:
        if image_input["type"] == "image_embeds":
            return image_input["data"]

        pixel_values = image_input["data"]
        images_spatial_crop = image_input["images_spatial_crop"]

        return self._pixel_values_to_embedding(
            pixel_values=pixel_values, images_spatial_crop=images_spatial_crop
        )

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
        image_input = self._parse_and_validate_image_input(**kwargs)
        if image_input is None:
            return []
        vision_embeddings = self._process_image_input(image_input)
        return vision_embeddings

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
        **kwargs: object,
    ):
        if intermediate_tensors is not None:
            inputs_embeds = None

        hidden_states = self.language_model(
            input_ids, positions, intermediate_tensors, inputs_embeds=inputs_embeds
        )

        return hidden_states

    defcompute_logits(
        self,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor | None:
        return self.language_model.compute_logits(hidden_states)

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        loader = AutoWeightsLoader(self)
        autoloaded_weights = loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
        return autoloaded_weights
```