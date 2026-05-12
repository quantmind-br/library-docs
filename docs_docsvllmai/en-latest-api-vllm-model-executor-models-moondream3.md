---
title: moondream3 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/moondream3/
source: sitemap
fetched_at: 2026-05-07T21:32:07.873696205-03:00
rendered_js: false
word_count: 32
summary: This document defines the Moondream3 model architecture integration for vLLM, detailing the implementation of its vision encoder, projection layer, and text decoder.
tags:
    - vllm
    - moondream3
    - multimodal-model
    - causal-lm
    - vision-encoder
    - pytorch
category: reference
---

```
@MULTIMODAL_REGISTRY.register_processor(
    Moondream3MultiModalProcessor,
    info=Moondream3ProcessingInfo,
    dummy_inputs=Moondream3DummyInputsBuilder,
)
classMoondream3ForCausalLM(nn.Module, SupportsMultiModal, SupportsPP):
"""Moondream3 multimodal model for causal language modeling.

    vLLM supports the standard autoregressive Moondream3 query and caption
    prompt formats. The region-module point/detect skills require custom
    coordinate decoding and are intentionally not exposed here.
    """

    supports_multimodal = True
    packed_modules_mapping = {
        "qkv_proj": ["q_proj", "k_proj", "v_proj"],
    }

    def__init__(
        self,
        *,
        vllm_config: VllmConfig,
        prefix: str = "",
    ):
        super().__init__()

        hf_config = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config
        cache_config = vllm_config.cache_config

        # Reuse the transformers_utils config implementation.
        if isinstance(hf_config, Moondream3Config):
            self.config = hf_config
        else:
            config_dict = hf_config.config if hasattr(hf_config, "config") else {}
            self.config = Moondream3Config(config=config_dict)

        with self._mark_tower_model(vllm_config, "image"):
            # Vision encoder
            self.vision = Moondream3VisionEncoder(
                config=self.config.vision_config,
                quant_config=quant_config,
                prefix=maybe_prefix(prefix, "vision"),
            )

            # Vision projection
            self.vision_proj = Moondream3VisionProjection(
                input_dim=self.config.vision_config.enc_dim,
                inner_dim=self.config.vision_config.proj_inner_dim,
                output_dim=self.config.text_config.dim,
                quant_config=quant_config,
                prefix=maybe_prefix(prefix, "vision_proj"),
            )

        with self._mark_language_model(vllm_config):
            # Text decoder
            self.text = Moondream3TextModel(
                config=self.config.text_config,
                cache_config=cache_config,
                quant_config=quant_config,
                prefix=maybe_prefix(prefix, "text"),
            )

            # LM head (with bias - Moondream3 has lm_head bias)
            self.lm_head = ParallelLMHead(
                self.config.text_config.vocab_size,
                self.config.text_config.dim,
                bias=True,
                quant_config=quant_config,
                prefix=maybe_prefix(prefix, "lm_head"),
            )

        self.logits_processor = LogitsProcessor(self.config.text_config.vocab_size)
        self.make_empty_intermediate_tensors = self.text.make_empty_intermediate_tensors
        self._answer_id = getattr(
            self.config,
            "answer_token_id",
            getattr(hf_config, "answer_token_id", 3),
        )

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality == "image":
            return "<image>"
        return None

    defget_language_model(self) -> nn.Module:
        return self.text

    defget_num_mm_encoder_tokens(self, num_image_tokens: int) -> int:
        return num_image_tokens

    defget_num_mm_connector_tokens(self, num_vision_tokens: int) -> int:
        return num_vision_tokens

    def_split_pixel_values(
        self,
        pixel_values: object,
    ) -> list[torch.Tensor]:
        # The processor should standardize image inputs into:
        # - torch.Tensor [num_images, num_crops, C, H, W], or
        # - list[torch.Tensor[num_crops, C, H, W]] for ragged crops.
        if isinstance(pixel_values, torch.Tensor):
            if pixel_values.dim() != 5:
                raise ValueError(
                    "Expected `pixel_values` tensor with shape "
                    "[num_images, num_crops, C, H, W], got "
                    f"{tuple(pixel_values.shape)}."
                )
            return [pv.contiguous() for pv in pixel_values]

        if isinstance(pixel_values, (list, tuple)):
            tensors: list[torch.Tensor] = []
            for value in pixel_values:
                if not isinstance(value, torch.Tensor):
                    raise TypeError(
                        "Expected each `pixel_values` element to be a tensor, "
                        f"got {type(value)!r}."
                    )
                if value.dim() != 4:
                    raise ValueError(
                        f"Unsupported pixel_values element shape {tuple(value.shape)}."
                    )
                tensors.append(value.contiguous())
            return tensors

        raise TypeError(
            "pixel_values must be a tensor or a sequence of tensors, "
            f"got {type(pixel_values)!r}."
        )

    def_split_tilings(
        self,
        tilings: object,
        expected: int,
    ) -> list[tuple[int, int] | None]:
        if tilings is None:
            return [None] * expected

        if isinstance(tilings, torch.Tensor):
            if tilings.dim() != 2 or tilings.shape[1] != 2:
                raise ValueError(
                    "Expected `tilings` tensor with shape [num_images, 2], got "
                    f"{tuple(tilings.shape)}."
                )
            tiling_items = tilings.tolist()
        elif isinstance(tilings, (list, tuple)):
            tiling_items = list(tilings)
        else:
            raise TypeError(
                "tilings must be None, a tensor or a sequence of tuples, "
                f"got {type(tilings)!r}."
            )

        if len(tiling_items) != expected:
            raise ValueError(
                "Mismatch between the number of pixel_values entries "
                f"({expected}) and tilings ({len(tiling_items)})."
            )

        normalized: list[tuple[int, int] | None] = []
        for tiling in tiling_items:
            if tiling is None:
                normalized.append(None)
                continue
            if isinstance(tiling, torch.Tensor):
                tiling = tiling.tolist()
            if isinstance(tiling, (list, tuple)) and len(tiling) == 2:
                normalized.append((int(tiling[0]), int(tiling[1])))
            else:
                raise ValueError(
                    f"Each tiling entry must be a pair of integers, got {tiling!r}."
                )
        return normalized

    def_parse_image_inputs(self, **kwargs: object) -> list[Moondream3ImageInput]:
        pixel_values = kwargs.get("pixel_values")
        if pixel_values is None:
            return []

        pixel_values_list = self._split_pixel_values(pixel_values)
        tilings_list = self._split_tilings(
            kwargs.get("tilings"), len(pixel_values_list)
        )

        image_inputs: list[Moondream3ImageInput] = []
        for value, tiling in zip(pixel_values_list, tilings_list):
            if value.dim() != 4:
                raise ValueError(
                    f"Expected 4D tensor for crops, got {tuple(value.shape)}."
                )
            image_inputs.append(Moondream3ImageInput(pixel_values=value, tiling=tiling))
        return image_inputs

    def_encode_image_input(self, image_input: Moondream3ImageInput) -> torch.Tensor:
        pixel_values = image_input.pixel_values
        if pixel_values.dim() != 4:
            raise ValueError(
                f"Expected 4D tensor for crops, got {tuple(pixel_values.shape)}."
            )

        device = self.vision.patch_emb.weight.device
        dtype = self.vision.patch_emb.weight.dtype
        pixel_values = pixel_values.to(device=device, dtype=dtype)

        features = self.vision(pixel_values)

        # Grid size = crop_size / patch_size (e.g., 378 / 14 = 27)
        grid_size = (
            self.config.vision_config.crop_size
            // self.config.vision_config.enc_patch_size
        )
        enc_dim = self.config.vision_config.enc_dim
        global_features = features[0]

        if features.shape[0] > 1:
            if image_input.tiling is None:
                raise ValueError(
                    "Missing tiling metadata for multi-crop Moondream image."
                )
            local = features[1:].contiguous().view(-1, grid_size, grid_size, enc_dim)
            reconstructed = reconstruct_from_crops(
                local,
                image_input.tiling,
                overlap_margin=self.config.vision_config.overlap_margin,
                patch_size=1,
            )
        else:
            reconstructed = global_features.view(grid_size, grid_size, enc_dim)

        recon = reconstructed.permute(2, 0, 1).contiguous()
        # Mirror HF reference behavior: reconstructed local features are pooled
        # to enc_n_layers x enc_n_layers. For moondream3-preview this is 27x27.
        pooled_size = self.config.vision_config.enc_n_layers
        if pooled_size != grid_size:
            logger.warning_once(
                "Moondream3 pooled_size (%d) differs from crop grid (%d). "
                "Using enc_n_layers to match HF reference behavior.",
                pooled_size,
                grid_size,
            )
        recon = F.adaptive_avg_pool2d(recon, output_size=(pooled_size, pooled_size))
        recon = recon.permute(1, 2, 0).contiguous().view(-1, enc_dim)

        combined = torch.cat([global_features, recon], dim=-1).unsqueeze(0)
        projected = self.vision_proj(combined).squeeze(0)

        # Note: Vision embeddings are already synchronized across TP ranks
        # because the vision projection uses RowParallelLinear which performs
        # all-reduce internally, ensuring identical outputs on all ranks.

        return projected

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
"""Generate the HF image prefix: BOS embedding + 729 image embeddings."""
        image_inputs = self._parse_image_inputs(**kwargs)
        if not image_inputs:
            return []

        device = self.vision.patch_emb.weight.device
        bos_ids = torch.tensor([self.config.bos_token_id], device=device)
        bos_embedding = self.text.embed_input_ids(bos_ids)

        embeddings: list[torch.Tensor] = []
        for image_input in image_inputs:
            image_embeddings = self._encode_image_input(image_input)
            embeddings.append(
                torch.cat([bos_embedding.to(image_embeddings.dtype), image_embeddings])
            )
        return embeddings

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
        **kwargs,
    ) -> torch.Tensor | IntermediateTensors:
        hidden_states = self.text(
            input_ids=input_ids,
            positions=positions,
            intermediate_tensors=intermediate_tensors,
            inputs_embeds=inputs_embeds,
        )
        return hidden_states

    defcompute_logits(
        self,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor | None:
        logits = self.logits_processor(self.lm_head, hidden_states)
        if logits is not None:
            logits[:, self._answer_id] = float("-inf")
        return logits

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
"""Load weights with remapping from HuggingFace format."""

        params_dict = dict(self.named_parameters())
        loaded_params: set[str] = set()

        # Get expert intermediate size for fc1 splitting

        for name, loaded_weight in weights:
            # Map from HF naming to vLLM naming
            # model.vision.* -> vision.*
            # model.text.* -> text.*
            if name.startswith("model."):
                name = name[6:]  # Remove "model." prefix

            # Specific name mappings
            # Vision projection: vision.proj_mlp.fc1 -> vision_proj.fc1
            name = name.replace("vision.proj_mlp.", "vision_proj.")

            # Text embedding: text.wte (no suffix) -> text.wte.weight
            if name == "text.wte":
                name = "text.wte.weight"

            # LM head: text.lm_head -> lm_head
            name = name.replace("text.lm_head.", "lm_head.")

            # Attention mapping
            name = name.replace(".attn.qkv.", ".attn.qkv_proj.")
            name = name.replace(".attn.proj.", ".attn.out_proj.")

            # Tau attention scaling weights
            # HF format: .attn.tau.alpha -> .attn.tau_alpha
            name = name.replace(".attn.tau.alpha", ".attn.tau_alpha")
            name = name.replace(".attn.tau.wq", ".attn.tau_wq")
            name = name.replace(".attn.tau.wv", ".attn.tau_wv")

            # MoE router mapping: mlp.router -> mlp.gate
            name = name.replace(".mlp.router.", ".mlp.gate.")

            # Handle MoE expert weights for layers 4+ with expert parallelism
            # fc1.weight: [n_experts, expert_inner_dim * 2, hidden_size] (gate+up)
            # fc2.weight: [n_experts, hidden_size, expert_inner_dim] (down)
            # Each GPU stores n_experts/tp_size experts
            # Note: Only 3D weights are MoE, 2D weights are standard MLP
            if ".mlp.fc1.weight" in name and loaded_weight.dim() == 3:
                fromvllm.distributedimport get_tensor_model_parallel_rank

                tp_size = get_tensor_model_parallel_world_size()
                tp_rank = get_tensor_model_parallel_rank()
                num_experts = loaded_weight.shape[0]
                experts_per_rank = num_experts // tp_size
                expert_start = tp_rank * experts_per_rank
                expert_end = expert_start + experts_per_rank
                # Shard by expert dimension
                loaded_weight = loaded_weight[expert_start:expert_end].contiguous()
                # Map to our custom MoE format: mlp.fc1_weight
                name = name.replace(".mlp.fc1.weight", ".mlp.fc1_weight")

            if ".mlp.fc2.weight" in name and loaded_weight.dim() == 3:
                fromvllm.distributedimport get_tensor_model_parallel_rank

                tp_size = get_tensor_model_parallel_world_size()
                tp_rank = get_tensor_model_parallel_rank()
                num_experts = loaded_weight.shape[0]
                experts_per_rank = num_experts // tp_size
                expert_start = tp_rank * experts_per_rank
                expert_end = expert_start + experts_per_rank
                # Shard by expert dimension
                loaded_weight = loaded_weight[expert_start:expert_end].contiguous()
                # Map to our custom MoE format: mlp.fc2_weight
                name = name.replace(".mlp.fc2.weight", ".mlp.fc2_weight")

            # Handle tau weights with tensor parallelism
            # tau_alpha: [num_heads] -> [num_heads/tp]
            # tau_wq: [num_heads, qkv_dim] -> [num_heads/tp, qkv_dim/tp]
            # tau_wv: [num_heads, qkv_dim] -> [num_heads/tp, qkv_dim/tp]
            if ".tau_alpha" in name:
                fromvllm.distributedimport get_tensor_model_parallel_rank

                tp_size = get_tensor_model_parallel_world_size()
                tp_rank = get_tensor_model_parallel_rank()
                num_heads = loaded_weight.shape[0]
                heads_per_partition = num_heads // tp_size
                start = tp_rank * heads_per_partition
                end = start + heads_per_partition
                loaded_weight = loaded_weight[start:end].contiguous()

            if ".tau_wq" in name or ".tau_wv" in name:
                fromvllm.distributedimport get_tensor_model_parallel_rank

                tp_size = get_tensor_model_parallel_world_size()
                tp_rank = get_tensor_model_parallel_rank()
                num_heads, qkv_dim = loaded_weight.shape
                heads_per_partition = num_heads // tp_size
                # Only shard by head dimension, keep full qkv_dim for all-gather
                head_start = tp_rank * heads_per_partition
                head_end = head_start + heads_per_partition
                loaded_weight = loaded_weight[head_start:head_end, :].contiguous()

            if name in params_dict:
                param = params_dict[name]
                weight_loader = getattr(param, "weight_loader", default_weight_loader)
                weight_loader(param, loaded_weight)
                loaded_params.add(name)

        return loaded_params
```