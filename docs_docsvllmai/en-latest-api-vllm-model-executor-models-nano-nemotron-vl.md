---
title: nano_nemotron_vl - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/nano_nemotron_vl/
source: sitemap
fetched_at: 2026-05-07T21:32:12.244881195-03:00
rendered_js: false
word_count: 0
summary: This document defines the NemotronH_Nano_VL_V2 model architecture within the vLLM framework, providing logic for multimodal feature extraction, dynamic resolution processing, and projection layers for image, video, and audio inputs.
tags:
    - vllm
    - multimodal-model
    - feature-extraction
    - computer-vision
    - neural-network-architecture
    - dynamic-resolution
category: concept
---

```
@MULTIMODAL_REGISTRY.register_processor(
    NanoNemotronVLMultiModalProcessor,
    info=NanoNemotronVLProcessingInfo,
    dummy_inputs=NanoNemotronVLDummyInputsBuilder,
)
classNemotronH_Nano_VL_V2(
    nn.Module, HasInnerState, IsHybrid, SupportsMultiModal, SupportsMultiModalPruning
):
    requires_sequential_video_encoding = True
"""Temporarily needed for dynamic res video w/ conv3d, doesn't support bs>1 yet"""

    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            "language_model.backbone": "language_model.model",
        },
    )

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return "<image>"
        if modality.startswith("video"):
            return "<video>"
        if modality.startswith("audio"):
            return AUDIO_CONTEXT
        return None

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        model_config = vllm_config.model_config
        config = model_config.hf_config
        multimodal_config = model_config.multimodal_config
        image_size = config.force_image_size
        patch_size = config.patch_size
        self.patch_size = patch_size
        self.template = config.template
        self.num_image_token = int(
            (image_size // patch_size) ** 2 * (config.downsample_ratio**2)
        )
        self.downsample_ratio = config.downsample_ratio
        self.ps_version = config.ps_version
        self.image_tag_type = config.image_tag_type
        self.video_pruning_rate = multimodal_config.video_pruning_rate

        vision_config = getattr(config, "vision_config", config)
        self.video_temporal_patch_size: int = getattr(
            vision_config, "video_temporal_patch_size", 1
        )

        with self._mark_language_model(vllm_config):
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config,
                hf_config=config.text_config,
                prefix=maybe_prefix(prefix, "language_model"),
            )
        llm_dtype = self.language_model.config.dtype
        assert isinstance(llm_dtype, torch.dtype)
        self.llm_dtype = llm_dtype
        with self._mark_tower_model(vllm_config, {"image", "video", "audio"}):
            self.vision_model = self.get_vit_model_from_radio_config(config).to(
                llm_dtype
            )

            # Construct the vision projection.
            vit_hidden_size = config.vit_hidden_size
            vision_projection_hidden_size = config.projector_hidden_size
            llm_hidden_size = config.text_config.hidden_size

            mlp1 = nn.Sequential(
                RMSNorm(
                    hidden_size=vit_hidden_size
                    * int(round(1 / self.downsample_ratio)) ** 2,
                    eps=1e-5,
                ),
                nn.Linear(
                    vit_hidden_size * int(round(1 / self.downsample_ratio)) ** 2,
                    vision_projection_hidden_size,
                    bias=False,
                ),
                ReLUSquaredActivation(),
                nn.Linear(vision_projection_hidden_size, llm_hidden_size, bias=False),
            )
            self.mlp1 = mlp1.to(llm_dtype)
            self.sound_encoder: ProjectedParakeet | None = None
            if getattr(config, "sound_config", None) is not None:
                logger.info_once(
                    "Found sound config, initializing sound encoder for Nemotron AVLM",
                    scope="global",
                )
                self.sound_encoder = ProjectedParakeet(
                    config.sound_config,
                    dtype=llm_dtype,
                    llm_hidden_size=llm_hidden_size,
                    max_model_len=model_config.max_model_len,
                )

        self.config = config
        self.model_config = vllm_config.model_config

        # Pre-tokenize special tokens for video processing
        # to avoid repeated tokenization
        tokenizer = cached_tokenizer_from_config(model_config)
        self._img_start_token_ids = tokenizer.encode(
            IMG_START, add_special_tokens=False
        )
        self._img_end_token_ids = tokenizer.encode(IMG_END, add_special_tokens=False)
        self._img_context_token_ids = tokenizer.encode(
            IMG_CONTEXT, add_special_tokens=False
        )
        self.dynamic_resolution = BaseNanoNemotronVLProcessor.use_dynamic_resolution(
            config
        )
        if self.dynamic_resolution:
            logger.info_once(
                "Dynamic resolution is enabled for NanoNemotronVLProcessor",
                scope="global",
            )

    defpixel_shuffle(self, x, scale_factor=0.5):
        n, h, w, c = x.size()
        r = int(1 / scale_factor)
        new_h = h // r
        new_w = w // r
        new_c = c * r * r

        x = x.view(n, new_h, r, new_w, r, c)
        if self.ps_version == "v1":
            warnings.warn(
                "In ps_version 'v1', the height and width have not "
                "been swapped back, which results in a transposed image.",
                stacklevel=2,
            )
            x = x.permute(0, 3, 1, 2, 4, 5).reshape(n, new_w, new_h, new_c)
        else:
            x = x.permute(0, 1, 3, 2, 4, 5).reshape(n, new_h, new_w, new_c)
        return x

    defpixel_shuffle_dynamic_res(
        self, x: torch.Tensor, *, imgs_sizes: list[tuple[int, int]]
    ) -> torch.Tensor:
        patch_dim = self.patch_size
        seq_lens = calc_seq_lens(imgs_sizes, patch_dim)
        splits = torch.split(x, seq_lens, dim=-2)
        out = []
        for i, sv in enumerate(splits):
            h = imgs_sizes[i][0] // patch_dim
            w = imgs_sizes[i][1] // patch_dim
            sv = sv.reshape(sv.shape[0], h, w, -1)
            sv = self.pixel_shuffle(sv, scale_factor=self.downsample_ratio)
            sv = sv.flatten(1, 2)
            out.append(sv)

        x = torch.cat(out, dim=-2)

        return x

    defextract_feature_dynamic(
        self, pixel_values: torch.Tensor, imgs_sizes: list[tuple[int, int]]
    ):
"""Dynamic resolution extract_feature for images."""
        _, vit_embeds = self.vision_model(pixel_values, imgs_sizes=imgs_sizes)
        vit_embeds = vit_embeds.to(dtype=torch.bfloat16)
        vit_embeds = self.pixel_shuffle_dynamic_res(vit_embeds, imgs_sizes=imgs_sizes)
        vit_embeds = self.mlp1(vit_embeds)
        return vit_embeds

    defextract_feature(
        self,
        pixel_values: torch.Tensor,
        num_frames: int | None = None,
    ) -> torch.Tensor:
        # Process images in a micro-batch of at most 128 frames per call
        #   This is done on purpose to ensure peak GPU ram usage of huge batch
        #   (namely for really long videos with EVS ON) won't cause any problems
        #   as we don't support chunked prefill for video media
        # When num_frames is provided and temporal_patch_size > 1, consecutive
        #   frames are grouped into tubelets — the batch size must be a multiple
        #   of T so chunk boundaries don't split a tubelet.
        N, _C, H, W = pixel_values.shape

        T = self.video_temporal_patch_size if num_frames is not None else 1
        micro_batch_size = 128 - (128 % T)
        patch_size = self.patch_size
        H_patches = H // patch_size
        W_patches = W // patch_size

        vit_embeds_list = []
        for i in range(0, N, micro_batch_size):
            chunk = pixel_values[i : i + micro_batch_size]
            if num_frames is not None and T > 1:
                _, vit_embeds = self.vision_model(chunk, num_frames=chunk.shape[0])
            else:
                _, vit_embeds = self.vision_model(chunk)
            vit_embeds = vit_embeds.to(dtype=torch.bfloat16)
            vit_embeds = vit_embeds.reshape(
                vit_embeds.shape[0], H_patches, W_patches, -1
            )
            vit_embeds = self.pixel_shuffle(
                vit_embeds, scale_factor=self.downsample_ratio
            )
            vit_embeds = vit_embeds.reshape(
                vit_embeds.shape[0], -1, vit_embeds.shape[-1]
            )
            vit_embeds = self.mlp1(vit_embeds)
            vit_embeds_list.append(vit_embeds)

        vit_embeds = torch.cat(vit_embeds_list, dim=0)
        return vit_embeds

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> NanoNemotronVLImageInputs | None:
        if image_embeds := kwargs.pop("image_embeds", None):
            return NanoNemotronVLImageEmbeddingInputs(
                type="image_embeds",
                data=image_embeds,
            )

        pixel_values_flat = kwargs.pop("pixel_values_flat", None)
        if pixel_values_flat is None:
            return None

        if self.dynamic_resolution:
            pixel_values_flat = DynamicResolutionImageTiler.stack(
                pixel_values_flat, self.patch_size
            )
            return NanoNemotronVLImagePixelInputsDynamic(
                pixel_values_flat=pixel_values_flat, **kwargs
            )
        else:
            return NanoNemotronVLImagePixelInputs(
                pixel_values_flat=pixel_values_flat,
                num_patches=kwargs.pop("image_num_patches"),
                **kwargs,
            )

    def_process_image_input_dynamic(
        self, image_input: NanoNemotronVLImagePixelInputsDynamic
    ) -> tuple[torch.Tensor, ...]:
        image_embeds = self.extract_feature_dynamic(
            image_input.pixel_values_flat, image_input.imgs_sizes
        )
        num_tokens_per_image = image_input.num_tokens_per_image

        if len(num_tokens_per_image) == 1:
            return (image_embeds.view(-1, self.config.text_config.hidden_size),)

        image_embeds = image_embeds.view(-1, self.config.text_config.hidden_size)
        return image_embeds.split(num_tokens_per_image)

    def_process_image_input(
        self, image_input: NanoNemotronVLImagePixelInputs
    ) -> tuple[torch.Tensor, ...]:
        image_embeds = self.extract_feature(image_input["pixel_values_flat"])
        num_patches = image_input["num_patches"]

        # Only one image in the current batch
        if len(num_patches) == 1:
            return (image_embeds.view(-1, self.config.text_config.hidden_size),)

        # NOTE: Image embeddings are split into separate tensors for each image
        # by the size of each embedding.
        feature_size = image_embeds.shape[1]
        image_embeds = image_embeds.view(-1, self.config.text_config.hidden_size)
        image_feature_sizes = [
            num_patches * feature_size for num_patches in num_patches
        ]
        return image_embeds.split(image_feature_sizes)

    def_process_video_input(
        self, video_input: NanoNemotronVLVideoPixelInputs
    ) -> tuple[torch.Tensor, ...]:
"""Process video input and create final embeddings with video content
        and indicator tokens."""
        T = self.video_temporal_patch_size

        if T > 1:
            video_embeddings = self._extract_video_embeddings_temporal(video_input)
        else:
            video_embeddings = self._process_image_input(video_input)

        final_video_embeddings: tuple[torch.Tensor, ...] = ()

        downsample_ratio = self.config.downsample_ratio
        patch_size = self.config.patch_size
        pixel_values = video_input["pixel_values_flat"]
        frame_h, frame_w = pixel_values.shape[-2], pixel_values.shape[-1]
        rows = int(frame_h * downsample_ratio // patch_size)
        cols = int(frame_w * downsample_ratio // patch_size)
        video_pruning_rate = self.video_pruning_rate
        video_num_frames = video_input["num_patches"].tolist()
        video_frames_indices = video_input["frames_indices"].split(video_num_frames)
        # Calculate video feature dimensions (number of frames and
        # their feature size (AKA tokens per frame))
        # TODO: Maybe this can be optimized to avoid the loop?
        for i, single_video_embeddings in enumerate(video_embeddings):
            num_frames = video_num_frames[i]
            frames_indices = video_frames_indices[i].tolist()
            frame_duration_ms = video_input["frame_duration_ms"][i].item()
            num_tubelets = math.ceil(num_frames / T) if T > 1 else num_frames
            assert single_video_embeddings.shape[0] % num_tubelets == 0

            if video_pruning_rate is not None and video_pruning_rate > 0.0:
                # Start of EVS-specific code
                retention_mask = compute_retention_mask(
                    single_video_embeddings,
                    video_size_thw=(num_tubelets, rows, cols),
                    spatial_merge_size=1,
                    q=video_pruning_rate,
                )

                # apply retention mask
                single_video_embeddings = single_video_embeddings[retention_mask]

                # calculate the actual number of retained tokens per frame
                retention_mask_thw = retention_mask.reshape(num_tubelets, rows, cols)
                num_tokens_per_frame = (
                    retention_mask_thw.sum(dim=(1, 2)).long().tolist()
                )
                # End of EVS-specific code
            else:
                feature_size = single_video_embeddings.shape[0] // num_tubelets
                num_tokens_per_frame = [feature_size] * num_tubelets

            final_video_embeddings += (
                self._create_final_video_embeddings(
                    single_video_embeddings,
                    num_tokens_per_frame,
                    frames_indices,
                    frame_duration_ms,
                    video_temporal_patch_size=T,
                ),
            )

        return final_video_embeddings

    def_extract_video_embeddings_temporal(
        self, video_input: NanoNemotronVLVideoPixelInputs
    ) -> tuple[torch.Tensor, ...]:
"""Extract per-video embeddings with temporal compression.

        Each video is processed separately through extract_feature with
        num_frames, which uses the fixed-resolution temporal path in RADIO
        (no attention mask, flash attention).
        """
        pixel_values = video_input["pixel_values_flat"]
        num_frames_per_video = video_input["num_patches"].tolist()
        hidden_size = self.config.text_config.hidden_size

        results: list[torch.Tensor] = []
        frame_offset = 0
        for nf in num_frames_per_video:
            video_frames = pixel_values[frame_offset : frame_offset + nf]
            frame_offset += nf

            vit_embeds = self.extract_feature(video_frames, num_frames=nf)
            results.append(vit_embeds.view(-1, hidden_size))

        return tuple(results)

    def_process_audio_input(
        self, audio_input: NanoNemotronVLAudioFeatureInputs
    ) -> tuple[torch.Tensor, ...]:
        assert self.sound_encoder is not None
        input_audio_features = audio_input.input_audio_features
        feature_attention_mask = audio_input.feature_attention_mask
        audio_num_clips = audio_input.audio_num_clips
        target_device = next(self.sound_encoder.parameters()).device

        input_audio_features = input_audio_features.to(
            dtype=self.llm_dtype, device=target_device
        )
        feature_attention_mask = feature_attention_mask.to(device=target_device)
        sound_embeds = self.sound_encoder(input_audio_features, feature_attention_mask)

        valid_input_lens = feature_attention_mask.sum(dim=1)
        valid_output_lens = self.sound_encoder.encoder._get_subsampling_output_length(
            valid_input_lens
        ).tolist()
        grouped_embeds = []
        clip_offset = 0
        for num_clips in audio_num_clips:
            embeds = []
            for clip_idx in range(clip_offset, clip_offset + num_clips):
                valid_len = valid_output_lens[clip_idx]
                embeds.append(sound_embeds[clip_idx, :valid_len])
            grouped_embeds.append(torch.cat(embeds, dim=0))
            clip_offset += num_clips

        return tuple(grouped_embeds)

    def_create_final_video_embeddings(
        self,
        video_embeddings: torch.Tensor,
        num_tokens_per_frame: list[int],
        frames_indices: list[int],
        frame_duration_ms: int,
        video_temporal_patch_size: int = 1,
    ) -> torch.Tensor:
"""Create final embeddings that combine video embeddings with
        text embeddings of indicator tokens.

        These final embeddings contain:
        - Actual video embeddings in positions corresponding to video content
        - Text embeddings for indicator tokens (<img>, </img>, and
          frame separation text) in their respective positions

        These embeddings will replace the placeholder embeddings to create
        input_embeds for the LLM.
        """
        tokenizer = cached_tokenizer_from_config(self.model_config)

        # Generate video replacement token IDs using get_video_repl
        # This tokenizes each frame separator independently, then uses pre-tokenized
        # special tokens to ensure consistent tokenization regardless of
        # num_tokens_per_frame values.
        video_repl = NanoNemotronVLProcessor.get_video_repl(
            tokens_per_frame=num_tokens_per_frame,
            frames_indices=frames_indices,
            frame_duration_ms=frame_duration_ms,
            tokenizer=tokenizer,
            img_start_token_ids=self._img_start_token_ids,
            img_end_token_ids=self._img_end_token_ids,
            img_context_token_ids=self._img_context_token_ids,
            video_temporal_patch_size=video_temporal_patch_size,
        )
        device = video_embeddings.device

        # video_repl.full is a list of token IDs
        repl_token_ids = torch.tensor(video_repl.full, device=device)

        # Get embedding token IDs for image context (use pre-tokenized version)
        embed_token_ids = torch.tensor(self._img_context_token_ids, device=device)

        # Create mask for video embedding positions
        is_video_embed = torch.isin(repl_token_ids, embed_token_ids)

        # Create final video embeddings, merging text embeddings for indicator
        # tokens with video embeddings
        text_embeddings = self.get_language_model().embed_input_ids(repl_token_ids)
        final_video_embeddings = _merge_multimodal_embeddings(
            inputs_embeds=text_embeddings,
            multimodal_embeddings=video_embeddings,
            is_multimodal=is_video_embed,
        )

        return final_video_embeddings

    def_parse_and_validate_video_input(
        self, **kwargs: object
    ) -> NanoNemotronVLVideoPixelInputs | None:
        pixel_values_flat_video = kwargs.pop("pixel_values_flat_video", None)
        video_num_patches = kwargs.pop("video_num_patches", None)
        video_embeds = kwargs.pop("video_embeds", None)
        frames_indices = kwargs.pop("frames_indices", None)
        frame_duration_ms = kwargs.pop("frame_duration_ms", None)

        if pixel_values_flat_video is None and video_embeds is None:
            return None

        if video_embeds is not None:
            return NanoNemotronVLVideoEmbeddingInputs(
                type="video_embeds",
                data=video_embeds,
            )

        if pixel_values_flat_video is not None:
            if torch.is_tensor(frames_indices):
                frames_indices = frames_indices.flatten()
            else:
                frames_indices = torch.cat([f.flatten() for f in frames_indices], dim=0)

            if torch.is_tensor(frame_duration_ms):
                frame_duration_ms = frame_duration_ms.flatten()
            else:
                frame_duration_ms = torch.cat(
                    [f.flatten() for f in frame_duration_ms], dim=0
                )

            if (
                torch.is_tensor(pixel_values_flat_video)
                and pixel_values_flat_video.ndim == 5
            ):
                # batched._reduce_data stacked same-shape videos into
                # [num_videos, nf, 3, H, W]; unstack back to a list so the
                # same-H,W cat path below handles it uniformly.
                pixel_values_flat_video = list(pixel_values_flat_video)

            if not torch.is_tensor(pixel_values_flat_video):
                pixel_values_flat_video = torch.cat(pixel_values_flat_video, dim=0)

            expected_h = pixel_values_flat_video.shape[-2]
            expected_w = pixel_values_flat_video.shape[-1]
            num_frames = video_num_patches[0].item()
            resolve_bindings = {"h": expected_h, "w": expected_w, "f": num_frames}

            return NanoNemotronVLVideoPixelInputs(
                type="pixel_values_videos",
                pixel_values_flat=pixel_values_flat_video,
                num_patches=video_num_patches,
                frames_indices=frames_indices,
                frame_duration_ms=frame_duration_ms,
                resolve_bindings=resolve_bindings,
            )

        raise AssertionError("This line should be unreachable.")

    def_parse_and_validate_multimodal_inputs(self, **kwargs: object) -> dict:
        modalities = {}
        # Preserve the order of modalities if there are multiple of them
        # from the order of kwargs.
        for input_key in kwargs:
            if (
                input_key in ("pixel_values_flat", "image_embeds")
                and "images" not in modalities
            ):
                modalities["images"] = self._parse_and_validate_image_input(**kwargs)
            if input_key in ("pixel_values_flat_video",) and "videos" not in modalities:
                modalities["videos"] = self._parse_and_validate_video_input(**kwargs)
            if (
                input_key
                in (
                    "input_audio_features",
                    "feature_attention_mask",
                    "audio_num_clips",
                )
                and "audios" not in modalities
            ):
                modalities["audios"] = NanoNemotronVLAudioFeatureInputs(
                    **kwargs, validate=False
                )

        return modalities

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
        # Validate the multimodal input keyword arguments
        modalities = self._parse_and_validate_multimodal_inputs(**kwargs)
        if modalities is None:
            return []

        # # The result multimodal_embeddings is tuple of tensors, with each
        # tensor corresponding to a multimodal data item (image or video).
        multimodal_embeddings: tuple[torch.Tensor, ...] = ()

        # NOTE: It is important to iterate over the keys in this dictionary
        # to preserve the order of the modalities.
        for modality in modalities:
            if modality == "images":
                image_input = modalities["images"]
                if image_input["type"] == "image_embeds":
                    image_embeddings = image_input["data"]
                elif self.dynamic_resolution:
                    assert image_input["type"] == "pixel_values_dynamic"
                    image_embeddings = self._process_image_input_dynamic(image_input)
                else:
                    image_embeddings = self._process_image_input(image_input)
                multimodal_embeddings += tuple(image_embeddings)
            if modality == "videos":
                video_input = modalities["videos"]
                video_embeddings = self._process_video_input(video_input)
                multimodal_embeddings += tuple(video_embeddings)
            if modality == "audios":
                audio_input = modalities["audios"]
                audio_embeddings = self._process_audio_input(audio_input)
                multimodal_embeddings += tuple(audio_embeddings)

        return multimodal_embeddings

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

        hidden_states = self.language_model(
            input_ids=input_ids,
            positions=positions,
            intermediate_tensors=intermediate_tensors,
            inputs_embeds=inputs_embeds,
            **kwargs,
        )

        return hidden_states

    defget_mm_mapping(self) -> MultiModelKeys:
"""
        Get the module prefix in multimodal models
        """
        return MultiModelKeys.from_string_field(
            language_model="language_model",
            connector=["mlp1", "sound_encoder.projection"],
            tower_model=["vision_model", "sound_encoder.encoder"],
        )

    defcompute_logits(
        self,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor | None:
        return self.language_model.compute_logits(hidden_states)

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]):
        mm_config = self.model_config.multimodal_config
        load_multimodal_weights = not all(
            mm_config.get_limit_per_prompt(modality) == 0
            for modality in ("image", "video", "audio")
        )
        adapter_dict = dict(self.mlp1.named_parameters())

        defis_llm(name: str) -> bool:
            return name.startswith("language_model")

        defis_adapter_weights(weight: tuple[str, torch.Tensor]):
            return weight[0].startswith("mlp1")

        defis_vision_weights(name: str) -> bool:
            return name.startswith("vision_model.radio_model.")

        defis_sound_weights(name: str) -> bool:
            return name.startswith("sound")

        # Separate weights by component
        llm_weights = []
        vision_weights = []
        sound_weights = []

        for name, w in weights:
            if is_llm(name):
                # Strip 'language_model.' prefix for LLM weights
                llm_weights.append((".".join(name.split(".")[1:]), w))
            elif is_adapter_weights((name, w)):
                if not load_multimodal_weights:
                    continue
                # Load vision-language adapter weights directly
                trimmed_name = ".".join(name.split(".")[1:])
                param = adapter_dict[trimmed_name]
                with torch.no_grad():
                    default_weight_loader(param, w)
            elif is_vision_weights(name):
                if not load_multimodal_weights:
                    continue
                # Convert: vision_model.radio_model.* → radio_model.*
                hf_key = name[len("vision_model.") :]  # Remove "vision_model." prefix
                vision_weights.append((hf_key, w))
            elif is_sound_weights(name):
                if not load_multimodal_weights:
                    continue
                assert self.sound_encoder is not None
                sound_weights.append((name, w))

        self.language_model.load_weights(llm_weights)
        if load_multimodal_weights:
            self.vision_model.load_weights(vision_weights)
            if self.sound_encoder is not None and len(sound_weights) > 0:
                self.sound_encoder.load_weights(sound_weights)

    defget_vit_model_from_radio_config(self, hf_config):
        hf_config_vision = hf_config.vision_config
        model_name = hf_config_vision.args.get("model")
        if model_name is None:
            raise ValueError(f"Unsupported vit model type: {model_name}")

        preferred_resolution = getattr(hf_config_vision, "preferred_resolution", None)
        image_size = preferred_resolution[0] if preferred_resolution else 224
        patch_size = getattr(hf_config_vision, "patch_size", 16)

        # video_temporal_patch_size and separate_video_embedder are
        # top-level vision_config attributes, not inside args.
        video_temporal_patch_size = getattr(
            hf_config_vision, "video_temporal_patch_size", 1
        )
        separate_video_embedder = getattr(
            hf_config_vision, "separate_video_embedder", True
        )

        radio_config = RadioConfig(
            model_name=model_name,
            image_size=image_size,
            patch_size=patch_size,
            norm_mean=hf_config.norm_mean,
            norm_std=hf_config.norm_std,
            video_temporal_patch_size=video_temporal_patch_size,
            separate_video_embedder=separate_video_embedder,
            **hf_config_vision.args,
        )

        return RadioModel(config=radio_config)

    defcopy_inputs_before_cuda_graphs(self, input_buffers, **kwargs):
        return self.language_model.mamba_cache.copy_inputs_before_cuda_graphs(
            input_buffers, **kwargs
        )

    defget_seqlen_agnostic_capture_inputs(self, batch_size: int):
        return self.language_model.mamba_cache.get_seqlen_agnostic_capture_inputs(
            batch_size
        )

    @classmethod
    defget_mamba_state_shape_from_config(cls, vllm_config: "VllmConfig"):
        text_config = vllm_config.model_config.hf_config.text_config
        temp_vllm_config = vllm_config.with_hf_config(text_config)
        return NemotronHForCausalLM.get_mamba_state_shape_from_config(temp_vllm_config)

    @classmethod
    defget_mamba_state_dtype_from_config(cls, vllm_config: "VllmConfig"):
        text_config = vllm_config.model_config.hf_config.text_config
        temp_vllm_config = vllm_config.with_hf_config(text_config)
        return NemotronHForCausalLM.get_mamba_state_dtype_from_config(temp_vllm_config)

    @classmethod
    defget_mamba_state_copy_func(cls):
        return NemotronHForCausalLM.get_mamba_state_copy_func()
```