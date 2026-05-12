---
title: datasets - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/benchmarks/datasets/
source: sitemap
fetched_at: 2026-05-07T21:15:45.203010741-03:00
rendered_js: false
word_count: 28
summary: This document defines a class for generating synthetic multimodal datasets by sampling image and video configurations based on probability buckets and modality constraints.
tags:
    - multimodal
    - synthetic-data
    - data-sampling
    - dataset-generation
    - python-class
category: reference
---

```
classRandomMultiModalDataset(RandomDataset):
"""
    Synthetic multimodal dataset (text + images) that extends RandomDataset.

    Status:
    - Images: supported via synthetic RGB data.
    - Video: supported via synthetic RGB data.
    - Audio: not yet supported.

    Sampling overview:
    1) Number of items per request is sampled uniformly from the integer range
       [floor(n·(1−r)), ceil(n·(1+r))], where n is the base count and r is
       `num_mm_items_range_ratio` in [0, 1]. r=0 keeps it fixed; r=1 allows 0.
       The maximum is further clamped to the sum of per-modality limits.
    2) Each item’s modality and shape is sampled from `bucket_config`, a dict
       mapping (height, width, num_frames) → probability. We treat
       `num_frames`=1 as image and `num_frames` > 1 as video.
       Entries with zero probability are removed and the rest are renormalized
       to sum to 1.
    3) Per-modality hard caps are enforced via `limit_mm_per_prompt`.
       When a modality reaches its cap, all of its buckets are excluded and the
       remaining probabilities are renormalized.

    Example bucket configuration:
    {(256, 256, 1): 0.5, (720, 1280, 1): 0.4, (720, 1280, 16): 0.1}
      - Two image buckets (`num_frames`=1) and one video bucket
      (`num_frames`=16).
    OBS.: Only image sampling is supported for now.
    """

    IS_MULTIMODAL = True
    DEFAULT_LIMIT_MM_PER_PROMPT = {"image": 255, "video": 1}

    DEFAULT_BASE_ITEMS_PER_REQUEST = 1
    DEFAULT_NUM_MM_ITEMS_RANGE_RATIO = 0.0
    DEFAULT_MM_ITEM_BUCKET_CONFIG = {
        (256, 256, 1): 0.5,
        (720, 1280, 1): 0.5,
        (720, 1280, 16): 0.0,
    }
    DEFAULT_ENABLE_MULTIMODAL_CHAT = False

    def__init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    defgenerate_synthetic_image(self, width: int, height: int) -> Image.Image:
"""Generate synthetic PIL image with random RGB values.

        NOTE: iid pixel sampling results in worst-case compression
        (good for stressing I/O), but very unlike real photos.
        We could consider a “low-freq” mode (e.g., noise blur)
        to emulate network realism instead of max stress.
        """
        random_pixels = self._rng.integers(
            0,
            256,
            (height, width, 3),
            dtype=np.uint8,
        )
        return Image.fromarray(random_pixels)

    defgenerate_synthetic_video(
        self, width: int, height: int, num_frames: int
    ) -> dict:
"""Generate synthetic video with random values.

        Creates a video with random pixel values, encodes it to MP4 format,
        and returns the content as bytes.
        """
        importcv2

        random_pixels = self._rng.integers(
            0,
            256,
            (num_frames, height, width, 3),
            dtype=np.uint8,
        )

        # Create a temporary video file in memory
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        fps = 30  # frames per second

        with NamedTemporaryFile(suffix=".mp4", delete=False) as temp_file:
            temp_path = temp_file.name

            # Create video writer
            video_writer = cv2.VideoWriter(
                temp_path, fourcc=fourcc, fps=fps, frameSize=(width, height)
            )

            if not video_writer.isOpened():
                raise RuntimeError("Failed to create video writer")

            for frame in random_pixels:
                video_writer.write(frame)

            video_writer.release()
            temp_file.close()

            # Read the video file content
            with open(temp_path, "rb") as f:
                video_content = f.read()

            return {"bytes": video_content}

    defmap_config_to_modality(self, config: tuple[int, int, int]) -> str:
"""Map the configuration to the modality."""
        if config[-1] == 1:
            return "image"
        elif config[-1] > 1:
            return "video"
        else:
            raise ValueError(f"Invalid multimodal item configuration: {config}")

    defnormalize_bucket_config(
        self, bucket_config: dict[tuple[int, int, int], float]
    ) -> dict[tuple[int, int, int], float]:
"""
        Remove zero probability entries
        and normalize the bucket config to sum to 1.
        """
        # Raise error if value is negative
        if any(v < 0 for v in bucket_config.values()):
            raise ValueError("Bucket config values must be non-negative.")
        # Remove zero probability entries
        bucket_config = {k: v for k, v in bucket_config.items() if v > 0}
        # if bucket config is empty, raise error
        if not bucket_config:
            raise ValueError(
                "Got invalid bucket config. Bucket config values must be non-zero."
            )
        # Normalize the remaining bucket config to sum to 1
        total = sum(bucket_config.values())
        return {k: v / total for k, v in bucket_config.items()}

    defgenerate_mm_item(
        self,
        mm_item_config: tuple[int, int, int],
    ) -> Mapping[str, Any]:
"""
        Create synthetic images and videos and
        apply process_image/process_video respectively.
        This follows the OpenAI API chat completions
        https://github.com/openai/openai-python
        """

        if self.map_config_to_modality(mm_item_config) == "image":
            return process_image(
                self.generate_synthetic_image(mm_item_config[1], mm_item_config[0])
            )
        elif self.map_config_to_modality(mm_item_config) == "video":
            return process_video(
                self.generate_synthetic_video(
                    mm_item_config[1], mm_item_config[0], mm_item_config[2]
                )
            )
        else:
            raise ValueError(f"Invalid multimodal item configuration: {mm_item_config}")

    defget_mm_item_sampling_params(
        self,
        base_items_per_request: int,
        num_mm_items_range_ratio: float,
        limit_mm_per_prompt: dict[str, int],
        bucket_config: dict[tuple[int, int, int], float],
    ) -> tuple[int, int, dict[str, int], dict[tuple[int, int, int], float]]:
"""
        Get the sampling parameters for the multimodal items.
        """
        # Enforce num_mm_items_range_ratio <= 1
        if not (0.0 <= num_mm_items_range_ratio <= 1.0):
            raise ValueError("num_mm_items_range_ratio must be in [0, 1].")

        # Ensure modalities to sample are in limit_mm_per_prompt
        for k, v in bucket_config.items():
            # get modality from bucket config
            modality = self.map_config_to_modality(k)
            if modality not in limit_mm_per_prompt:
                raise ValueError(
                    f"Modality {modality} is not in "
                    f"limit_mm_per_prompt: "
                    f"{limit_mm_per_prompt.keys()}"
                )

        # Remove zero probability entries
        # and normalize bucket config to sum to 1
        bucket_config = self.normalize_bucket_config(bucket_config)
        logger.info(
            "Normalized bucket config: %s",
            bucket_config,
        )
        # Only consider limit per prompt for modalities in bucket config
        allowed_modalities = {self.map_config_to_modality(cfg) for cfg in bucket_config}
        limit_mm_per_prompt = {
            k: v for k, v in limit_mm_per_prompt.items() if k in allowed_modalities
        }
        if not limit_mm_per_prompt:
            raise ValueError("No valid limits for modalities present in bucket_config.")

        logger.info(
            "Updated mm-limit-per-prompt: %s",
            limit_mm_per_prompt,
        )

        # Get max and min num mm items and ensure
        # it is at most the sum of limit_mm_per_prompt for all modalities
        max_num_mm_items = min(
            sum(limit_mm_per_prompt.values()),
            math.ceil(base_items_per_request * (1 + num_mm_items_range_ratio)),
        )
        # Ensure min num mm items is at least 0
        min_num_mm_items = max(
            0, math.floor(base_items_per_request * (1 - num_mm_items_range_ratio))
        )
        # Raise error if min num mm items is greater than max num mm items
        if min_num_mm_items > max_num_mm_items:
            raise ValueError(
                f"Min num mm items is greater than max mm items: "
                f"{min_num_mm_items} > {max_num_mm_items}"
            )

        logger.info(
            "Sampling number of multimodal items from [%s, %s]",
            min_num_mm_items,
            max_num_mm_items,
        )

        return (
            min_num_mm_items,
            max_num_mm_items,
            limit_mm_per_prompt,
            bucket_config,
        )

    defget_mm_item_iterator(
        self,
        min_num_mm_items: int,
        max_num_mm_items: int,
        bucket_config: dict[tuple[int, int, int], float],
        limit_mm_per_prompt: dict[str, int],
    ) -> Iterator[tuple[int, int, int]]:
"""
        Iterator over the multimodal items for each request
        whose size is between min_num_mm_items and max_num_mm_items.

        Loop over the bucket config and sample a multimodal item.
        Loop until the number of multimodal items sampled is equal to
        request_num_mm_items or limit of multimodal items per prompt
        for all modalities is reached.

        Note:
        - This function operates on a per-request shallow copy of
          `bucket_config` (tuple->float). The original dict passed to
          `sample` is not mutated. If this ever changes, a test
          is implemented and will fail.
        """
        # Get the number of multimodal items to sample
        request_num_mm_items = int(
            self._rng.integers(min_num_mm_items, max_num_mm_items + 1)
        )
        # If request_num_mm_items is 0, yield an empty iterator
        if request_num_mm_items == 0:
            return
        # Initialize modality counters
        modality_counter = {self.map_config_to_modality(k): 0 for k in bucket_config}
        # Copy the bucket config to avoid modifying the original
        bucket_config_copy = bucket_config.copy()
        # Loop over the number of multimodal items to sample
        while sum(modality_counter.values()) < request_num_mm_items:
            # Sample a multimodal item config
            mm_item_config = self._rng.choice(
                list(bucket_config_copy.keys()), p=list(bucket_config_copy.values())
            )
            modality = self.map_config_to_modality(mm_item_config)
            # Check that modality count is less than limit per prompt
            if modality_counter[modality] < limit_mm_per_prompt[modality]:
                modality_counter[modality] += 1
                yield (mm_item_config)
            else:
                # If the counter is greater than the limit per prompt
                # set all multimodal items of this modality to 0
                for k, v in bucket_config_copy.items():
                    if self.map_config_to_modality(k) == modality:
                        bucket_config_copy[k] = 0
                # If all configs are 0, break the loop
                # This should not happen as request_num_mm_items is at most
                # the sum of limit_mm_per_prompt for all modalities
                if all(v == 0 for v in bucket_config_copy.values()):
                    logger.warning(
                        "Exhausted all multimodal items of modality %s", modality
                    )
                    break
                # Renormalize the bucket config
                bucket_config_copy = self.normalize_bucket_config(bucket_config_copy)

    defsample(
        self,
        tokenizer: TokenizerLike,
        num_requests: int,
        request_id_prefix: str = "",
        no_oversample: bool = False,
        prefix_len: int = RandomDataset.DEFAULT_PREFIX_LEN,
        range_ratio: RangeRatio = RandomDataset.DEFAULT_RANGE_RATIO,
        input_len: int = RandomDataset.DEFAULT_INPUT_LEN,
        output_len: int = RandomDataset.DEFAULT_OUTPUT_LEN,
        batchsize: int = 1,
        limit_mm_per_prompt: dict[str, int] = DEFAULT_LIMIT_MM_PER_PROMPT,
        base_items_per_request: int = DEFAULT_BASE_ITEMS_PER_REQUEST,
        num_mm_items_range_ratio: float = DEFAULT_NUM_MM_ITEMS_RANGE_RATIO,
        bucket_config: dict[
            tuple[int, int, int], float
        ] = DEFAULT_MM_ITEM_BUCKET_CONFIG,
        enable_multimodal_chat: bool = DEFAULT_ENABLE_MULTIMODAL_CHAT,
        **kwargs,
    ) -> list[SampleRequest]:
        if batchsize != 1:
            raise NotImplementedError(
                "batchsize > 1 is not supported for RandomMultiModalDataset."
            )

        input_lens, output_lens, offsets = get_sampling_params(
            self._rng,
            num_requests,
            range_ratio,
            input_len,
            output_len,
            tokenizer,
        )

        (
            min_num_mm_items,
            max_num_mm_items,
            limit_mm_per_prompt,
            bucket_config,
        ) = self.get_mm_item_sampling_params(
            base_items_per_request,
            num_mm_items_range_ratio,
            limit_mm_per_prompt,
            bucket_config,
        )

        vocab_size = tokenizer.vocab_size
        # Can't use tokenizer.all_special_ids since
        # it returns ONLY ids from special_tokens_map.json
        # We want to exclude placeholder tokens and all
        # tokens that indicate start/end of image as it
        # may break prompt replacement logic.
        prohibited_tokens = list(
            tok_id
            for tok_id, token in tokenizer.added_tokens_decoder.items()
            if token.special
        )
        all_tokens = np.arange(vocab_size)
        allowed_tokens = np.array(list(set(all_tokens) - set(prohibited_tokens)))
        logger.debug(
            "Sampling from %d out of %d (vocab size)", len(allowed_tokens), vocab_size
        )
        # Generate prefix once
        prefix_token_ids = self.get_prefix(tokenizer, allowed_tokens, prefix_len)
        # Add synthetic multimodal items to each request
        mm_requests = []
        token_mismatch_total = 0
        for i in range(num_requests):
            prompt, total_input_len, token_mismatch = self.generate_token_sequence(  # noqa: E501
                tokenizer=tokenizer,
                prefix_token_ids=prefix_token_ids,
                prefix_len=prefix_len,
                vocab_size=vocab_size,
                input_len=int(input_lens[i]),
                offset=int(offsets[i]),
                index=i,
                allowed_tokens=allowed_tokens,
            )
            token_mismatch_total += token_mismatch
            # Get multimodal item iterator for a given request
            mm_item_iterator = self.get_mm_item_iterator(
                min_num_mm_items,
                max_num_mm_items,
                bucket_config,
                limit_mm_per_prompt,
            )

            mm_content = cast(
                list[dict[str, Any]],
                [
                    self.generate_mm_item(mm_item_config)
                    for mm_item_config in mm_item_iterator
                ],
            )

            if enable_multimodal_chat:
                # NOTE: For now this option is only provided for completeness
                # given that the serve.py benchmark currently does not use it.
                mm_chat_prompt: Any = prompt
                mm_chat_prompt = self.apply_multimodal_chat_transformation(
                    prompt, mm_content
                )
                sample_request = SampleRequest(
                    prompt=mm_chat_prompt,
                    prompt_len=total_input_len,
                    expected_output_len=int(output_lens[i]),
                    multi_modal_data=None,
                    request_id=request_id_prefix + str(i),
                )
            else:
                sample_request = SampleRequest(
                    prompt=prompt,
                    prompt_len=total_input_len,
                    expected_output_len=int(output_lens[i]),
                    multi_modal_data=mm_content,
                    request_id=request_id_prefix + str(i),
                )
            mm_requests.append(sample_request)

        if token_mismatch_total != 0:
            sign = "more" if token_mismatch_total > 0 else "fewer"
            logger.warning(
                "Across all generated prompts, there were %d%s tokens "
                "than expected after decoding and re-encoding. This is "
                "expected due to the imperfect nature of the sampling "
                "procedure.",
                abs(token_mismatch_total),
                sign,
            )

        return mm_requests
```