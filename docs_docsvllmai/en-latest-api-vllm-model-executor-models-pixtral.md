---
title: pixtral - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/pixtral/
source: sitemap
fetched_at: 2026-05-07T21:32:43.096416266-03:00
rendered_js: false
word_count: 0
summary: This document defines the Pixtral model architecture for vLLM, detailing its multimodal processing capabilities, weight mapping for vision encoders, and integration with causal language models.
tags:
    - pixtral
    - vllm
    - multimodal
    - vision-encoder
    - model-architecture
    - machine-learning
category: api
---

```
@MULTIMODAL_REGISTRY.register_processor(
    PixtralMultiModalProcessor,
    info=PixtralProcessingInfo,
    dummy_inputs=PixtralDummyInputsBuilder,
)
classPixtralForConditionalGeneration(
    nn.Module, SupportsLoRA, SupportsEagle3, SupportsMultiModal, SupportsPP
):
    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            "model.language_model.": "language_model.model.",
            "model.vision_tower.": "vision_encoder.",
            "model.multi_modal_projector.": "vision_language_adapter.",
        },
        orig_to_new_substr={
            ".linear_1.": ".w_in.",
            ".linear_2.": ".w_out.",
        },
    )

    packed_modules_mapping = {
        "qkv_proj": ["q_proj", "k_proj", "v_proj"],
        "gate_up_proj": ["gate_proj", "up_proj"],
    }

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return None

        raise ValueError("Only image modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        config = vllm_config.model_config.hf_config
        multimodal_config = vllm_config.model_config.multimodal_config
        self.config = config
        self.multimodal_config = multimodal_config

        dataclass_fields = {field.name for field in fields(VisionEncoderArgs)}
        vision_args = {
            key: value
            for key, value in self.config.vision_config.to_dict().items()
            if key in dataclass_fields
        }

        self.vision_args = VisionEncoderArgs(**vision_args)

        # init MistralForCausalLM
        with self._mark_language_model(vllm_config):
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config,
                hf_config=config.text_config,
                prefix=maybe_prefix(prefix, "language_model"),
            )

        with self._mark_tower_model(vllm_config, "image"):
            self.vision_encoder = VisionTransformer(
                self.vision_args,
                prefix=maybe_prefix(prefix, "vision_encoder"),
            )
            self.pre_mm_projector_norm = (
                RMSNorm(self.vision_args.hidden_size, eps=1e-5)
                if self.vision_args.add_pre_mm_projector_layer_norm
                else None
            )
            self.patch_merger = (
                PatchMerger(
                    vision_encoder_dim=self.vision_args.hidden_size,
                    spatial_merge_size=self.vision_args.spatial_merge_size,
                    use_mlp_bias=False,
                )
                if self.vision_args.mm_projector_id == PATCH_MERGE
                else None
            )
            self.vision_language_adapter = VisionLanguageAdapter(
                self.vision_args, dim=config.text_config.hidden_size
            )

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> PixtralImagePixelInputs | None:
        images = kwargs.pop("images", None)
        if images is None:
            return None

        return PixtralImagePixelInputs(
            type="pixel_values",
            images=images,
        )

    def_process_image_input(
        self,
        image_input: PixtralImagePixelInputs,
    ) -> tuple[torch.Tensor, ...]:
        images = image_input["images"]
        image_features = self.vision_encoder(images)
        feature_sizes = [image_feature.shape[0] for image_feature in image_features]
        image_features = torch.cat(image_features)
        if self.pre_mm_projector_norm is not None:
            image_features = self.pre_mm_projector_norm(image_features)
        if self.patch_merger is not None:
            patch_size = self.vision_args.patch_size
            spatial_merge_size_square = self.vision_args.spatial_merge_size**2
            img_patch_dims = [
                (img.shape[1] // patch_size, img.shape[2] // patch_size)
                for img in images
            ]
            feature_sizes = [
                feature_size // spatial_merge_size_square
                for feature_size in feature_sizes
            ]
            image_features = self.patch_merger(
                image_features, image_sizes=img_patch_dims
            )
        image_embeds = self.vision_language_adapter(image_features)
        image_embeds = torch.split(image_embeds, feature_sizes)
        return image_embeds

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
        image_input = self._parse_and_validate_image_input(**kwargs)
        if image_input is None:
            return []

        return self._process_image_input(image_input)

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
        **kwargs: object,
    ) -> torch.Tensor | IntermediateTensors:
"""Run forward pass for pixtral."""
        if intermediate_tensors is not None:
            inputs_embeds = None

        hidden_states = self.language_model.model(
            input_ids, positions, intermediate_tensors, inputs_embeds=inputs_embeds
        )

        return hidden_states

    defcompute_logits(
        self,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor | None:
        return self.language_model.compute_logits(hidden_states)

    def_require_language_model_eagle3(self) -> None:
        if not supports_eagle3(self.language_model):
            raise RuntimeError(
                f"EAGLE-3 speculative decoding requires the language model to "
                f"support EAGLE-3, but {type(self.language_model).__name__} does not."
            )

    defset_aux_hidden_state_layers(self, layers: tuple[int, ...]) -> None:
        self._require_language_model_eagle3()
        self.language_model.set_aux_hidden_state_layers(layers)

    defget_eagle3_aux_hidden_state_layers(self) -> tuple[int, ...]:
        self._require_language_model_eagle3()
        return self.language_model.get_eagle3_aux_hidden_state_layers()

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]):
        _vision_encoder_stacked_params = [
            # (param_name, shard_name, shard_id)
            # HF format
            (".qkv_proj", ".q_proj", "q"),
            (".qkv_proj", ".k_proj", "k"),
            (".qkv_proj", ".v_proj", "v"),
            (".gate_up_proj", ".gate_proj", 0),
            (".gate_up_proj", ".up_proj", 1),
            # Mistral native (consolidated) format
            (".qkv_proj", ".wq", "q"),
            (".qkv_proj", ".wk", "k"),
            (".qkv_proj", ".wv", "v"),
            (".gate_up_proj", ".w1", 0),
            (".gate_up_proj", ".w3", 1),
        ]

        # Remap Mistral native names to HF-style names
        # used by the vLLM vision encoder modules.
        _vision_encoder_name_remap = {
            ".wo.": ".o_proj.",
            ".w2.": ".down_proj.",
        }

        defis_vision_encoder_weights(weight: tuple[str, torch.Tensor]):
            return weight[0].startswith(("vision_encoder", "vision_tower"))

        defis_vision_lang_adapter_weights(weight: tuple[str, torch.Tensor]):
            return weight[0].startswith(
                ("vision_language_adapter", "multi_modal_projector")
            )

        defis_patch_merger(weight: tuple[str, torch.Tensor]):
            return weight[0].startswith("patch_merger")

        defis_pre_mm_projector_norm(weight: tuple[str, torch.Tensor]):
            return weight[0].startswith("pre_mm_projector_norm")

        vision_encoder_dict = (
            dict(self.vision_encoder.named_parameters())
            if self.vision_encoder is not None
            else {}
        )
        patch_merger_dict = (
            dict(self.patch_merger.named_parameters())
            if self.patch_merger is not None
            else {}
        )
        pre_mm_projector_norm_dict = (
            dict(self.pre_mm_projector_norm.named_parameters())
            if self.pre_mm_projector_norm is not None
            else {}
        )
        vision_lang_adapter_dict = (
            dict(self.vision_language_adapter.named_parameters())
            if self.vision_language_adapter is not None
            else {}
        )

        defllm_weights_generator():
            for name, w in weights:
                if is_vision_encoder_weights((name, w)):
                    if _is_layer_none_or_staged(self.vision_encoder):
                        continue
                    trimmed_name = ".".join(name.split(".")[1:])
                    for (
                        param_name,
                        weight_name,
                        shard_id,
                    ) in _vision_encoder_stacked_params:
                        if weight_name in trimmed_name:
                            trimmed_name = trimmed_name.replace(weight_name, param_name)
                            param = vision_encoder_dict[trimmed_name]
                            weight_loader = param.weight_loader
                            weight_loader(param, w, shard_id)
                            break
                    else:
                        for old, new in _vision_encoder_name_remap.items():
                            if old in trimmed_name:
                                trimmed_name = trimmed_name.replace(old, new)
                                break

                        param = vision_encoder_dict.get(trimmed_name)
                        if param is not None:
                            weight_loader = getattr(
                                param, "weight_loader", default_weight_loader
                            )
                            weight_loader(param, w)
                elif is_patch_merger((name, w)):
                    if _is_layer_none_or_staged(self.patch_merger):
                        continue
                    trimmed_name = ".".join(name.split(".")[1:])
                    param = patch_merger_dict[trimmed_name]
                    weight_loader = getattr(
                        param, "weight_loader", default_weight_loader
                    )
                    weight_loader(param, w)
                elif is_pre_mm_projector_norm((name, w)):
                    if _is_layer_none_or_staged(self.pre_mm_projector_norm):
                        continue
                    trimmed_name = ".".join(name.split(".")[1:])
                    param = pre_mm_projector_norm_dict[trimmed_name]
                    with torch.no_grad():
                        default_weight_loader(param, w)
                elif is_vision_lang_adapter_weights((name, w)):
                    if _is_layer_none_or_staged(self.vision_language_adapter):
                        continue
                    trimmed_name = ".".join(name.split(".")[1:])
                    param = vision_lang_adapter_dict.get(trimmed_name)
                    if param is not None:
                        weight_loader = getattr(
                            param, "weight_loader", default_weight_loader
                        )
                        weight_loader(param, w)
                else:
                    name = name.removeprefix("language_model.")
                    yield (name, w)

        self.language_model.load_weights(llm_weights_generator())

    defget_mm_mapping(self) -> MultiModelKeys:
        return MultiModelKeys.from_string_field(
            language_model="language_model.",
            connector="vision_language_adapter.",
            tower_model="vision_encoder",
        )

    defget_num_mm_encoder_tokens(self, num_image_tokens: int) -> int:
        if getattr(self, "patch_merger", None) is None:
            return num_image_tokens
        merge_size = self.vision_args.spatial_merge_size
        return num_image_tokens * (merge_size**2)

    defget_num_mm_connector_tokens(self, num_vision_tokens: int) -> int:
        if getattr(self, "patch_merger", None) is None:
            return num_vision_tokens
        merge_size = self.vision_args.spatial_merge_size
        return num_vision_tokens // (merge_size**2)
```