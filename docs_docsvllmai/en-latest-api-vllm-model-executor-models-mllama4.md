---
title: mllama4 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/mllama4/
source: sitemap
fetched_at: 2026-05-07T21:31:59.975986568-03:00
rendered_js: false
word_count: 0
summary: This document defines the Llama4 multimodal model implementation, integrating vision encoders, multi-modal projectors, and causal language modeling within the vLLM framework.
tags:
    - llama4
    - multimodal-model
    - vllm
    - deep-learning
    - pytorch
    - model-architecture
category: concept
---

```
@MULTIMODAL_REGISTRY.register_processor(
    Mllama4MultiModalProcessor,
    info=Mllama4ProcessingInfo,
    dummy_inputs=Mllama4DummyInputsBuilder,
)
classLlama4ForConditionalGeneration(
    nn.Module,
    SupportsMultiModal,
    SupportsPP,
    MixtureOfExperts,
    SupportsEagle3,
    SupportsLoRA,
):
    packed_modules_mapping = {
        "qkv_proj": ["q_proj", "k_proj", "v_proj"],
        "gate_up_proj": ["gate_proj", "up_proj"],
    }

    supports_encoder_tp_data = True

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return "<|image|>"

        raise ValueError("Only image modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        config = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config
        multimodal_config = vllm_config.model_config.multimodal_config
        self.use_data_parallel = multimodal_config.mm_encoder_tp_mode == "data"

        self.vllm_config = vllm_config
        self.config = config
        self.quant_config = quant_config
        self.multimodal_config = multimodal_config

        with self._mark_tower_model(vllm_config, "image"):
            with set_current_vllm_config(vllm_config):
                self.vision_model = Llama4VisionModel(
                    config=config.vision_config,
                    quant_config=None,
                    prefix=maybe_prefix(prefix, "vision_model"),
                )

            self.multi_modal_projector = Llama4MultiModalProjector(
                config=self.config,
                quant_config=None,
                prefix=maybe_prefix(prefix, "multi_modal_projector"),
            )

        with self._mark_language_model(vllm_config):
            self.language_model = initialize_model(
                vllm_config=vllm_config.with_hf_config(
                    config.text_config, ["LlamaForCausalLM"]
                ),
                prefix=maybe_prefix(prefix, "language_model"),
                model_class=Llama4ForCausalLM,
            )

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

        # Set MoE hyperparameters
        self.num_expert_groups = 1
        self.num_logical_experts = self.language_model.num_logical_experts
        self.num_physical_experts = self.language_model.num_physical_experts
        self.num_local_physical_experts = self.language_model.num_local_physical_experts
        self.num_routed_experts = self.language_model.num_routed_experts
        self.num_shared_experts = self.language_model.num_shared_experts
        self.num_redundant_experts = self.language_model.num_redundant_experts
        self.moe_layers = self.language_model.moe_layers
        self.num_moe_layers = len(self.moe_layers)

    defset_aux_hidden_state_layers(self, layers: tuple[int, ...]) -> None:
        # Delegate to underlying language model (Llama4ForCausalLM)
        assert hasattr(self.language_model, "set_aux_hidden_state_layers")
        self.language_model.set_aux_hidden_state_layers(layers)

    defget_eagle3_default_aux_hidden_state_layers(self) -> tuple[int, ...]:
        # Delegate to underlying language model (Llama4ForCausalLM)
        assert hasattr(
            self.language_model, "get_eagle3_default_aux_hidden_state_layers"
        )
        return self.language_model.get_eagle3_default_aux_hidden_state_layers()

    defset_eplb_state(
        self,
        expert_load_view: torch.Tensor,
        logical_to_physical_map: torch.Tensor,
        logical_replica_count: torch.Tensor,
    ):
        self.language_model.set_eplb_state(
            expert_load_view, logical_to_physical_map, logical_replica_count
        )
        self.expert_weights = self.language_model.expert_weights

    defupdate_physical_experts_metadata(
        self, num_physical_experts: int, num_local_physical_experts: int
    ):
        self.language_model.update_physical_experts_metadata(
            num_physical_experts, num_local_physical_experts
        )

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> Llama4ImagePatchInputs | None:
        # num_images, 1, num_chunks, channel, image_size, image_size
        pixel_values = kwargs.pop("pixel_values", None)
        if pixel_values is None:
            return None

        patches_per_image = kwargs.pop("patches_per_image")
        aspect_ratios = kwargs.pop("aspect_ratios")

        return Llama4ImagePatchInputs(
            type="pixel_values",
            pixel_values=pixel_values,
            patches_per_image=patches_per_image,
            aspect_ratios=aspect_ratios,
        )

    def_process_image_input(
        self, image_input: Llama4ImagePatchInputs
    ) -> MultiModalEmbeddings:
        assert self.vision_model and self.multi_modal_projector
        pixel_values = image_input["pixel_values"]
        patches_per_image = image_input["patches_per_image"].tolist()

        # shard image input
        if self.use_data_parallel:
            vision_embeddings_flat = run_dp_sharded_vision_model(
                pixel_values, self.vision_model
            )
        else:
            vision_embeddings_flat = self.vision_model(pixel_values)

        vision_embeddings_flat = self.multi_modal_projector(vision_embeddings_flat)

        return [
            img.flatten(0, 1)
            for img in vision_embeddings_flat.split(patches_per_image, dim=0)
        ]

    defembed_multimodal(self, **kwargs) -> MultiModalEmbeddings:
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
        if intermediate_tensors is not None:
            inputs_embeds = None

        return self.language_model(
            input_ids, positions, intermediate_tensors, inputs_embeds
        )

    defcompute_logits(
        self,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor | None:
        return self.language_model.compute_logits(hidden_states)

    defseparate_weights(
        self,
        weights: Iterable[tuple[str, torch.Tensor]],
        prefix: str,
    ) -> tuple[Iterable[tuple[str, torch.Tensor]], Iterable[tuple[str, torch.Tensor]]]:
        weights1, weights2 = tee(weights, 2)

        defget_prefix_weights() -> Iterable[tuple[str, torch.Tensor]]:
            for name, data in weights1:
                if name.startswith(prefix):
                    yield (name, data)

        defget_other_weights() -> Iterable[tuple[str, torch.Tensor]]:
            for name, data in weights2:
                if not name.startswith(prefix):
                    yield (name, data)

        return get_prefix_weights(), get_other_weights()

    def_consolidate_qkv_weights(
        self, weights: Iterable[tuple[str, torch.Tensor]]
    ) -> Iterable[tuple[str, torch.Tensor]]:
        qkv_idx_mappings = {
            ".self_attn.q_proj": 0,
            ".self_attn.k_proj": 1,
            ".self_attn.v_proj": 2,
        }
        qkv_weights = {}
        for name, loaded_weight in weights:
            for weight_name, idx in qkv_idx_mappings.items():
                if weight_name not in name:
                    continue
                new_name = name.replace(weight_name, ".self_attn.qkv_proj")
                if new_name not in qkv_weights:
                    qkv_weights[new_name] = [None] * 3
                qkv_weights[new_name][idx] = loaded_weight
                break
            else:
                yield name, loaded_weight
        for key, weight in qkv_weights.items():
            qkv_weight = torch.cat(weight, dim=0)
            yield key, qkv_weight

    def_rename_weight_for_modelopt_checkpoint(self, name: str) -> str:
"""Rename weights from ModelOpt llama4 fp8 checkpoints to vLLM
        format."""
        if name.startswith("model.") or name.startswith("language_model.model."):
            renamed = (
                name.replace("model.", "language_model.model.", 1)
                if name.startswith("model.")
                else name
            )
            # Handle expert scale parameters with flat naming
            if "feed_forward.experts." in name and (
                "_input_scale" in name or "_weight_scale" in name
            ):
                # Map checkpoint naming to vLLM's expected naming
                if "down_proj_input_scale" in renamed:
                    return renamed.replace("down_proj_input_scale", "w2_input_scale")
                elif "down_proj_weight_scale" in renamed:
                    return renamed.replace("down_proj_weight_scale", "w2_weight_scale")
                elif "gate_up_proj_input_scale" in renamed:
                    return renamed.replace(
                        "gate_up_proj_input_scale", "w13_input_scale"
                    )
                elif "gate_up_proj_weight_scale" in renamed:
                    return renamed.replace(
                        "gate_up_proj_weight_scale", "w13_weight_scale"
                    )
                return renamed

            # Handle attention scale parameters
            elif "self_attn." in name and (".k_scale" in name or ".v_scale" in name):
                if ".k_proj.k_scale" in renamed:
                    return renamed.replace(".k_proj.k_scale", ".attn.k_scale")
                elif ".v_proj.v_scale" in renamed:
                    return renamed.replace(".v_proj.v_scale", ".attn.v_scale")
                return renamed

            # Standard model.* to language_model.model.* renaming
            return renamed

        elif name.startswith("lm_head.weight"):
            return name.replace("lm_head.weight", "language_model.lm_head.weight")

        return name

    def_separate_and_rename_weights(
        self, weights: Iterable[tuple[str, torch.Tensor]]
    ) -> tuple[list[tuple[str, torch.Tensor]], list[tuple[str, torch.Tensor]]]:
"""Rename weights and separate them into language_model and other
        weights."""
        language_model_weights = []
        other_weights = []

        for name, weight in weights:
            renamed = self._rename_weight_for_modelopt_checkpoint(name)

            attr = renamed.split(".", 1)[0]
            if isinstance(getattr(self, attr), StageMissingLayer):
                continue

            if renamed.startswith("language_model."):
                language_model_weights.append((renamed, weight))
            else:
                other_weights.append((renamed, weight))

        return language_model_weights, other_weights

    def_handle_expert_scale_broadcasting(
        self, weights: list[tuple[str, torch.Tensor]], params_dict: dict
    ) -> tuple[list[tuple[str, torch.Tensor]], set[str]]:
"""Handle expert scale parameters that need broadcasting.

        ModelOpt checkpoints use a single value tensor scalar for BMM style
        experts, vLLM expects the scale to be broadcasted across all experts.
        """
        regular_weights = []
        expert_scale_weights = []
        updated_params = set()

        for name, weight in weights:
            # Check if this is an expert scale parameter that needs broadcasting
            if (
                "feed_forward.experts." in name
                and "scale" in name
                and ".shared_expert" not in name
            ):
                if name in params_dict:
                    param = params_dict[name]
                    if (
                        hasattr(param, "data")
                        and param.data.numel() > 1
                        and weight.numel() == 1
                    ):
                        # Broadcast single value to all experts
                        param.data.fill_(weight.item())
                        updated_params.add(name)
                        continue

                expert_scale_weights.append((name, weight))
            else:
                regular_weights.append((name, weight))

        return regular_weights, expert_scale_weights, updated_params

    def_load_other_weights(
        self,
        other_weights: Iterable[tuple[str, torch.Tensor]],
        params_dict: dict,
        stacked_params_mapping: list,
    ) -> set[str]:
"""Load non-language-model weights with stacking support."""
        updated_params = set()

        if self.use_data_parallel:
            other_weights = self._consolidate_qkv_weights(other_weights)

        for name, loaded_weight in other_weights:
            # Try stacked parameter mapping first
            for param_name, weight_name, shard_id in stacked_params_mapping:
                if weight_name not in name or self.use_data_parallel:
                    continue
                name = name.replace(weight_name, param_name)
                param = params_dict[name]
                updated_params.add(name)
                weight_loader = param.weight_loader
                weight_loader(param, loaded_weight, shard_id)
                break
            else:
                # Use regular weight loading
                param = params_dict[name]
                weight_loader = getattr(param, "weight_loader", default_weight_loader)
                weight_loader(param, loaded_weight)
                updated_params.add(name)

        return updated_params

    defget_expert_mapping(self) -> list[tuple[str, str, int, str]]:
        # Params for weights, fp8 weight scales, fp8 activation scales
        # (param_name, weight_name, expert_id, shard_id)
        return fused_moe_make_expert_params_mapping(
            self,
            ckpt_gate_proj_name="gate_proj",
            ckpt_down_proj_name="down_proj",
            ckpt_up_proj_name="up_proj",
            num_experts=self.config.text_config.num_local_experts,
            num_redundant_experts=self.num_redundant_experts,
        )

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        stacked_params_mapping = [
            # (param_name, shard_name, shard_id)
            (".self_attn.qkv_proj", ".self_attn.q_proj", "q"),
            (".self_attn.qkv_proj", ".self_attn.k_proj", "k"),
            (".self_attn.qkv_proj", ".self_attn.v_proj", "v"),
            # Shared expert gate_up_proj stacking
            (".shared_expert.gate_up_proj", ".shared_expert.gate_proj", 0),
            (".shared_expert.gate_up_proj", ".shared_expert.up_proj", 1),
            # Feed forward gate_up_proj stacking (for non-MoE layers if any)
            (".feed_forward.gate_up_proj", ".feed_forward.gate_proj", 0),
            (".feed_forward.gate_up_proj", ".feed_forward.up_proj", 1),
        ]
        params_dict = dict(self.named_parameters())
        updated_params: set[str] = set()

        # Separate and rename weights
        language_model_weights, other_weights = self._separate_and_rename_weights(
            weights
        )

        # Handle expert scale parameters
        regular_weights, expert_scale_weights, updated_params_from_experts = (
            self._handle_expert_scale_broadcasting(language_model_weights, params_dict)
        )
        updated_params.update(updated_params_from_experts)

        loader = AutoWeightsLoader(self)
        loaded_language_model_params = loader.load_weights(regular_weights)
        assert loaded_language_model_params is not None
        updated_params.update(loaded_language_model_params)

        if expert_scale_weights:
            loaded_expert_scale_params = loader.load_weights(expert_scale_weights)
            if loaded_expert_scale_params:
                updated_params.update(loaded_expert_scale_params)

        updated_params.update(
            self._load_other_weights(other_weights, params_dict, stacked_params_mapping)
        )

        return updated_params

    defget_mm_mapping(self) -> MultiModelKeys:
"""
        Get the module prefix in multimodal models
        """
        return MultiModelKeys.from_string_field(
            language_model="language_model",
            connector=[
                "multi_modal_projector.",
                "vision_model.vision_adapter.",
            ],
            tower_model="vision_model.",
        )

    defget_num_mm_encoder_tokens(self, num_image_tokens: int) -> int:
        vision_config = self.config.vision_config
        patches_per_chunk = Mllama4ProcessingInfo.get_patch_per_chunk(vision_config)
        if num_image_tokens <= 0 or patches_per_chunk <= 0:
            return 0
        raw_patches = (vision_config.image_size // vision_config.patch_size) ** 2
        num_chunks = num_image_tokens // patches_per_chunk
        # Encoder processes raw_patches + 1 (CLS) per chunk
        return num_chunks * (raw_patches + 1)

    defget_num_mm_connector_tokens(self, num_vision_tokens: int) -> int:
        vision_config = self.config.vision_config
        raw_patches = (vision_config.image_size // vision_config.patch_size) ** 2
        if num_vision_tokens <= 0:
            return 0
        num_chunks = num_vision_tokens // (raw_patches + 1)
        patches_per_chunk = Mllama4ProcessingInfo.get_patch_per_chunk(vision_config)
        return num_chunks * patches_per_chunk
```