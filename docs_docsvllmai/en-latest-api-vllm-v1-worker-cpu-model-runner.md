---
title: cpu_model_runner - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/worker/cpu_model_runner/
source: sitemap
fetched_at: 2026-05-07T21:42:10.247448939-03:00
rendered_js: false
word_count: 0
summary: This document defines the CPUModelRunner class, which overrides GPU-specific model execution logic to enable model inference and speculative decoding on CPU hardware.
tags:
    - vllm
    - cpu-backend
    - speculative-decoding
    - model-runner
    - torch-optimization
    - inference
category: concept
---

```
classCPUModelRunner(GPUModelRunner):
    def__init__(self, vllm_config: VllmConfig, device: torch.device):
        # avoid calling accelerator APIs for methods inherited from super class
        _set_torch_accelerator_to_noop()

        with _torch_cuda_wrapper():
            super().__init__(vllm_config, device)

        assert device == torch.device("cpu")
        # Note: speculative decoding is now supported on CPU with C++ native impls

        self.use_cuda_graph = False
        self.cascade_attn_enabled = False

        self._postprocess_tensors()
        self._postprocess_triton()

    def_postprocess_tensors(self) -> None:
        # Note: replace device tensors with cpu tensors
        defreplace_tensor(obj: Any, cpu_attr_name: str, device_attr_name) -> None:
            cpu_tensor = getattr(obj, cpu_attr_name, None)
            device_tensor = getattr(obj, device_attr_name, None)
            if isinstance(cpu_tensor, torch.Tensor) and isinstance(
                device_tensor, torch.Tensor
            ):
                setattr(obj, device_attr_name, cpu_tensor)

        for v in vars(self).values():
            if isinstance(v, CpuGpuBuffer):
                v.gpu = v.cpu

        for k, v in vars(self.input_batch).items():
            if k.endswith("_cpu_tensor") and isinstance(v, torch.Tensor):
                replace_tensor(self.input_batch, k, k[:-11])

        for block_table in self.input_batch.block_table.block_tables:
            for v in vars(block_table).values():
                if isinstance(v, CpuGpuBuffer):
                    v.gpu = v.cpu

    def_postprocess_triton(self) -> None:
        importvllm.v1.worker.block_table

        vllm.v1.worker.block_table._compute_slot_mapping_kernel = (
            cpu_tl.compute_slot_mapping_kernel
        )

        # Speculative decoding fallbacks
        importvllm.v1.sample.rejection_sampler
        importvllm.v1.spec_decode.llm_base_proposer
        importvllm.v1.spec_decode.utils

        vllm.v1.spec_decode.llm_base_proposer.eagle_prepare_inputs_padded_kernel = (
            cpu_tl.eagle_prepare_inputs_padded_kernel
        )
        vllm.v1.spec_decode.llm_base_proposer.eagle_prepare_next_token_padded_kernel = (
            cpu_tl.eagle_prepare_next_token_padded_kernel
        )
        vllm.v1.spec_decode.llm_base_proposer.copy_and_expand_eagle_inputs_kernel = (
            cpu_tl.copy_and_expand_eagle_inputs_kernel
        )
        vllm.v1.spec_decode.utils.eagle_step_slot_mapping_metadata_kernel = (
            cpu_tl.eagle_step_slot_mapping_metadata_kernel
        )
        vllm.v1.sample.rejection_sampler.rejection_greedy_sample_kernel = (
            cpu_tl.rejection_greedy_sample_kernel
        )
        vllm.v1.sample.rejection_sampler.rejection_random_sample_kernel = (
            cpu_tl.rejection_random_sample_kernel
        )
        vllm.v1.sample.rejection_sampler.expand_kernel = cpu_tl.expand_kernel
        vllm.v1.sample.rejection_sampler.sample_recovered_tokens_kernel = (
            cpu_tl.sample_recovered_tokens_kernel
        )

    @instrument(span_name="Loading (CPU)")
    defload_model(self, load_dummy_weights: bool = False) -> None:
        if load_dummy_weights:
            raise ValueError(
                "Loading dummy weights (needed for elastic EP scale-up) "
                "Is not supported by the CPU Model Runner."
            )
        logger.info("Starting to load model %s...", self.model_config.model)
        self.model = get_model(vllm_config=self.vllm_config)

        if self.lora_config:
            self.model = self.load_lora_model(self.model, self.vllm_config, self.device)

        if hasattr(self, "drafter"):
            logger.info_once("Loading drafter model...")
            self.drafter.load_model(self.model)

    defget_model(self) -> nn.Module:
        return self.model

    @instrument(span_name="Warmup (CPU)")
    defwarming_up_model(self) -> None:
        logger.info("Warming up model for the compilation...")
        # Only generate graph for the generic shape
        with _set_global_compilation_settings(self.vllm_config):
            self.profile_run()
        logger.info("Warming up done.")

    definitialize_kv_cache(
        self,
        kv_cache_config: KVCacheConfig,
        is_profiling: bool = False,
    ) -> None:
        super().initialize_kv_cache(kv_cache_config, is_profiling)

        if self.speculative_config:
            if self.speculative_config.use_eagle():
                logger.info("EAGLE drafter KV cache initialized for CPU backend")
            elif self.speculative_config.uses_draft_model():
                logger.info("Draft model KV cache initialized for CPU backend")

    def_init_device_properties(self) -> None:
        pass

    def_sync_device(self) -> None:
        pass

    def_zero_block_ids(self, block_ids: list[int]) -> None:
        # CPU attention assigns -INF to logits at invalid positions,
        # so stale KV cache data never affects computation.
        pass

    # =========================================================================
    # CPU-safe overrides for speculative decoding methods
    # These methods override GPU-specific implementations that use CUDA streams
    # =========================================================================

    def_copy_draft_token_ids_to_cpu(
        self, scheduler_output: "SchedulerOutput", zeros_only: bool = False
    ) -> None:
"""CPU-safe version: no async copy needed, tensors already on CPU."""
        if self.use_async_scheduling and not (
            scheduler_output.has_structured_output_requests
            or self.input_batch.sampling_metadata.output_token_ids
        ):
            return
        self._draft_token_req_ids = self.input_batch.req_ids.copy()

        draft_token_ids: torch.Tensor = self._draft_token_ids
        if not torch.is_tensor(draft_token_ids):
            return

        num_reqs = draft_token_ids.shape[0]
        if self.draft_token_ids_cpu is not None:
            if not zeros_only:
                self.draft_token_ids_cpu[:num_reqs].copy_(draft_token_ids)
            else:
                self.draft_token_ids_cpu[:num_reqs] = 0

    def_get_draft_token_ids_cpu(self) -> tuple[list[list[int]], list[str]]:
"""CPU-safe version: no event synchronization needed."""
        if isinstance(self._draft_token_ids, list):
            return self._draft_token_ids, self.input_batch.req_ids
        req_ids = self._draft_token_req_ids
        if req_ids is None:
            return [], []
        if self.draft_token_ids_cpu is not None:
            return self.draft_token_ids_cpu[: len(req_ids)].tolist(), req_ids
        return [], []

    def_copy_valid_sampled_token_count(
        self, next_token_ids: torch.Tensor, valid_sampled_tokens_count: torch.Tensor
    ) -> None:
"""CPU-safe version: direct copy without CUDA streams."""
        if self.valid_sampled_token_count_cpu is None:
            return

        counts = valid_sampled_tokens_count
        counts_cpu = self.valid_sampled_token_count_cpu
        counts_cpu[: counts.shape[0]].copy_(counts)
        self.input_batch.prev_sampled_token_ids = next_token_ids.unsqueeze(1)

    def_get_valid_sampled_token_count(self) -> list[int]:
"""CPU-safe version: no event synchronization needed."""
        prev_sampled_token_ids = self.input_batch.prev_sampled_token_ids
        if prev_sampled_token_ids is None:
            return []

        counts_cpu = self.valid_sampled_token_count_cpu
        if counts_cpu is None:
            return []
        return counts_cpu[: prev_sampled_token_ids.shape[0]].tolist()

    def_to_list(self, sampled_token_ids: torch.Tensor) -> list[list[int]]:
"""CPU-safe version: direct tolist() without CUDA events."""
        return sampled_token_ids.tolist()
```