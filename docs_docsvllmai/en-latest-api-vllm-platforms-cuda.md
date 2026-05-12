---
title: cuda - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/platforms/cuda/
source: sitemap
fetched_at: 2026-05-07T21:34:31.921996181-03:00
rendered_js: false
word_count: 27
summary: This document defines the CudaPlatformBase class, providing an abstraction layer for managing CUDA-enabled hardware operations, configuration validation, and attention backend selection within the vLLM framework.
tags:
    - cuda
    - platform-abstraction
    - vllm
    - gpu-management
    - attention-backend
    - pytorch
category: concept
---

```
classCudaPlatformBase(Platform):
    _enum = PlatformEnum.CUDA
    device_name: str = "cuda"
    device_type: str = "cuda"
    dispatch_key: str = "CUDA"
    ray_device_key: str = "GPU"
    dist_backend: str = "nccl"
    device_control_env_var: str = "CUDA_VISIBLE_DEVICES"
    ray_noset_device_env_vars: list[str] = [
        "RAY_EXPERIMENTAL_NOSET_CUDA_VISIBLE_DEVICES",
    ]

    @property
    defsupported_dtypes(self) -> list[torch.dtype]:
        if self.has_device_capability(80):
            # Ampere and Hopper or later NVIDIA GPUs.
            return [torch.bfloat16, torch.float16, torch.float32]
        if self.has_device_capability(60):
            # Pascal, Volta and Turing NVIDIA GPUs, BF16 is not supported
            return [torch.float16, torch.float32]
        # Kepler and Maxwell NVIDIA GPUs, only FP32 is supported,
        # though vLLM doesn't support these GPUs.
        return [torch.float32]

    @classmethod
    defset_device(cls, device: torch.device) -> None:
"""
        Set the device for the current platform.
        """
        torch.cuda.set_device(device)
        # With this trick we can force the device to be set eagerly
        # see https://github.com/pytorch/pytorch/issues/155668
        # for why and when it is needed
        _ = torch.zeros(1, device=device)

    @classmethod
    defmanual_seed_all(cls, seed: int) -> None:
        torch.cuda.manual_seed_all(seed)

    @classmethod
    defget_device_capability(cls, device_id: int = 0) -> DeviceCapability | None:
        raise NotImplementedError

    @classmethod
    defget_device_name(cls, device_id: int = 0) -> str:
        raise NotImplementedError

    @classmethod
    defget_device_total_memory(cls, device_id: int = 0) -> int:
        raise NotImplementedError

    @classmethod
    defis_fully_connected(cls, device_ids: list[int]) -> bool:
        raise NotImplementedError

    @classmethod
    deflog_warnings(cls):
        pass

    @classmethod
    defcheck_and_update_config(cls, vllm_config: VllmConfig) -> None:
        parallel_config = vllm_config.parallel_config
        model_config = vllm_config.model_config

        if parallel_config.worker_cls == "auto":
            parallel_config.worker_cls = "vllm.v1.worker.gpu_worker.Worker"

        scheduler_config = vllm_config.scheduler_config
        # Note: model_config may be None during testing
        if (
            model_config is not None
            and model_config.is_mm_prefix_lm
            and scheduler_config.is_multimodal_model
            and not scheduler_config.disable_chunked_mm_input
        ):
            logger.warning(
                "Forcing --disable_chunked_mm_input for models "
                "with multimodal-bidirectional attention."
            )
            scheduler_config.disable_chunked_mm_input = True

    @classmethod
    defget_current_memory_usage(
        cls, device: torch.types.Device | None = None
    ) -> float:
        torch.cuda.empty_cache()
        torch.cuda.reset_peak_memory_stats(device)
        return torch.cuda.max_memory_allocated(device)

    @classmethod
    defget_valid_backends(
        cls,
        device_capability: DeviceCapability,
        attn_selector_config: AttentionSelectorConfig,
        num_heads: int | None = None,
    ) -> tuple[
        list[tuple[AttentionBackendEnum, int]],
        dict[AttentionBackendEnum, tuple[int, list[str]]],
    ]:
        valid_backends_priorities = []
        invalid_reasons: dict[AttentionBackendEnum, tuple[int, list[str]]] = {}

        backend_priorities = _get_backend_priorities(
            attn_selector_config.use_mla,
            device_capability,
            num_heads,
            attn_selector_config.kv_cache_dtype,
        )
        for priority, backend in enumerate(backend_priorities):
            try:
                backend_class = backend.get_class()
                invalid_reasons_i = backend_class.validate_configuration(
                    device_capability=device_capability,
                    **attn_selector_config._asdict(),
                )
            except ImportError:
                invalid_reasons_i = ["ImportError"]
            if invalid_reasons_i:
                invalid_reasons[backend] = (priority, invalid_reasons_i)
            else:
                valid_backends_priorities.append((backend, priority))

        return valid_backends_priorities, invalid_reasons

    @classmethod
    defget_attn_backend_cls(
        cls,
        selected_backend: AttentionBackendEnum | None,
        attn_selector_config: AttentionSelectorConfig,
        num_heads: int | None = None,
    ) -> str:
        device_capability = cls.get_device_capability()
        assert device_capability is not None

        # First try checking just the selected backend, if there is one.
        if selected_backend is not None:
            try:
                backend_class = selected_backend.get_class()
                invalid_reasons = backend_class.validate_configuration(
                    device_capability=device_capability,
                    **attn_selector_config._asdict(),
                )
            except ImportError:
                invalid_reasons = ["ImportError"]
            if invalid_reasons:
                raise ValueError(
                    f"Selected backend {selected_backend} is not valid for "
                    f"this configuration. Reason: {invalid_reasons}"
                )
            else:
                logger.info("Using %s backend.", selected_backend)
                return selected_backend.get_path()

        # No selected backend or the selected backend is invalid,
        # so we try finding a valid backend.
        valid_backends_priorities, all_invalid_reasons = cls.get_valid_backends(
            device_capability=device_capability,
            attn_selector_config=attn_selector_config,
            num_heads=num_heads,
        )
        reasons_str = (
            "{"
            + ", ".join(
                f"{backend.name}: [{', '.join(reasons)}]"
                for backend, (_, reasons) in all_invalid_reasons.items()
            )
            + "}"
        )
        config_str = attn_selector_config.__repr__()
        logger.debug_once(
            f"Some attention backends are not valid for {cls.device_name} with "
            f"{config_str}. Reasons: {reasons_str}."
        )
        if len(valid_backends_priorities) == 0:
            raise ValueError(
                f"No valid attention backend found for {cls.device_name} "
                f"with {config_str}. Reasons: {reasons_str}."
            )

        # We have found some valid backends. Select the one with the
        # highest priority.
        sorted_indices = sorted(
            range(len(valid_backends_priorities)),
            key=lambda i: valid_backends_priorities[i][1],
        )
        selected_index = sorted_indices[0]
        selected_backend = valid_backends_priorities[selected_index][0]
        selected_priority = valid_backends_priorities[selected_index][1]

        # If the user specified --block-size (but not --attention-backend),
        # check whether that constraint precluded any higher-priority backends.
        if attn_selector_config.block_size is not None:
            excluded = [
                backend
                for backend, (priority, reasons) in all_invalid_reasons.items()
                if priority < selected_priority
                and reasons == ["block_size not supported"]
            ]
            if excluded:
                names = ", ".join(b.name for b in excluded)
                logger.warning(
                    "--block-size %d precluded higher-priority backend(s) "
                    "%s. Using %s instead, which may result in reduced "
                    "performance. Consider removing --block-size to "
                    "auto-select the optimal block size.",
                    attn_selector_config.block_size,
                    names,
                    selected_backend.name,
                )

        logger.info_once(
            "Using %s attention backend out of potential backends: %s.",
            selected_backend.name,
            "[" + ", ".join(f"'{b[0].name}'" for b in valid_backends_priorities) + "]",
        )

        return selected_backend.get_path()

    @classmethod
    defget_supported_vit_attn_backends(cls) -> list[AttentionBackendEnum]:
        if cls.has_device_capability(80):
            return [
                AttentionBackendEnum.FLASH_ATTN,
                AttentionBackendEnum.TRITON_ATTN,
                AttentionBackendEnum.TORCH_SDPA,
                AttentionBackendEnum.FLASHINFER,
            ]
        else:
            return [
                AttentionBackendEnum.FLASH_ATTN,
                AttentionBackendEnum.TORCH_SDPA,
                AttentionBackendEnum.TRITON_ATTN,
                AttentionBackendEnum.FLASHINFER,
            ]

    @classmethod
    defget_vit_attn_backend(
        cls,
        head_size: int,
        dtype: torch.dtype,
        backend: AttentionBackendEnum | None = None,
    ) -> AttentionBackendEnum:
        if backend is not None:
            assert backend in cls.get_supported_vit_attn_backends(), (
                f"Backend {backend} is not supported for vit attention. "
                f"Supported backends are: {cls.get_supported_vit_attn_backends()}"
            )
            logger.info_once(f"Using backend {backend} for vit attention")
            return backend

        cc = cls.get_device_capability()
        for vit_attn_backend in cls.get_supported_vit_attn_backends():
            if vit_attn_backend == AttentionBackendEnum.TORCH_SDPA:
                return vit_attn_backend
            try:
                backend_class = vit_attn_backend.get_class()
                is_backend_supported = backend_class.supports_head_size(
                    head_size
                ) and backend_class.supports_dtype(dtype)
                if cc is not None:
                    is_backend_supported = (
                        is_backend_supported
                        and backend_class.supports_compute_capability(cc)
                    )
                if is_backend_supported:
                    logger.info_once(
                        f"Using backend {vit_attn_backend} for vit attention",
                    )
                    return vit_attn_backend
            except ImportError:
                pass

        return AttentionBackendEnum.TORCH_SDPA

    @classmethod
    defget_punica_wrapper(cls) -> str:
        return "vllm.lora.punica_wrapper.punica_gpu.PunicaWrapperGPU"

    @classmethod
    defget_device_communicator_cls(cls) -> str:
        return (
            "vllm.distributed.device_communicators.cuda_communicator.CudaCommunicator"  # noqa
        )

    @classmethod
    defsupports_fp8(cls) -> bool:
        return cls.has_device_capability(89)

    @classmethod
    defuse_custom_allreduce(cls) -> bool:
        return True

    @classmethod
    defopaque_attention_op(cls) -> bool:
        return True

    @classmethod
    defget_static_graph_wrapper_cls(cls) -> str:
        return "vllm.compilation.cuda_graph.CUDAGraphWrapper"

    @classmethod
    defstateless_init_device_torch_dist_pg(
        cls,
        backend: str,
        prefix_store: PrefixStore,
        group_rank: int,
        group_size: int,
        timeout: timedelta,
    ) -> ProcessGroup:
        assert is_nccl_available()
        pg: ProcessGroup = ProcessGroup(
            prefix_store,
            group_rank,
            group_size,
        )
        fromtorch.distributed.distributed_c10dimport ProcessGroupNCCL

        backend_options = ProcessGroupNCCL.Options()
        backend_options._timeout = timeout

        backend_class = ProcessGroupNCCL(
            prefix_store, group_rank, group_size, backend_options
        )
        backend_type = ProcessGroup.BackendType.NCCL
        device = torch.device("cuda")
        pg._set_default_backend(backend_type)
        backend_class._set_sequence_number_for_group()

        pg._register_backend(device, backend_type, backend_class)
        return pg

    @classmethod
    defdevice_count(cls) -> int:
        return _cuda_device_count_stateless(envs.CUDA_VISIBLE_DEVICES)

    @classmethod
    defcheck_if_supports_dtype(cls, dtype: torch.dtype):
        if dtype == torch.bfloat16:  # noqa: SIM102
            if not cls.has_device_capability(80):
                capability = cls.get_device_capability()
                gpu_name = cls.get_device_name()

                if capability is None:
                    compute_str = "does not have a compute capability"
                else:
                    version_str = capability.as_version_str()
                    compute_str = f"has compute capability {version_str}"

                raise ValueError(
                    "Bfloat16 is only supported on GPUs "
                    "with compute capability of at least 8.0. "
                    f"Your {gpu_name} GPU {compute_str}. "
                    "You can use float16 instead by explicitly setting the "
                    "`dtype` flag in CLI, for example: --dtype=half."
                )

    @classmethod
    definsert_blocks_to_device(
        cls,
        src_cache: torch.Tensor,
        dst_cache: torch.Tensor,
        src_block_indices: torch.Tensor,
        dst_block_indices: torch.Tensor,
    ) -> None:
"""Copy blocks from src_cache to dst_cache on GPU."""
        _src_cache = src_cache[:, src_block_indices]
        dst_cache[:, dst_block_indices] = _src_cache.to(dst_cache.device)

    @classmethod
    defswap_out_blocks_to_host(
        cls,
        src_cache: torch.Tensor,
        dst_cache: torch.Tensor,
        src_block_indices: torch.Tensor,
        dst_block_indices: torch.Tensor,
    ) -> None:
"""Copy blocks from GPU to host (CPU)."""
        _src_cache = src_cache[:, src_block_indices]
        dst_cache[:, dst_block_indices] = _src_cache.cpu()

    @classmethod
    defsupport_hybrid_kv_cache(cls) -> bool:
        return True

    @classmethod
    defsupport_static_graph_mode(cls) -> bool:
        return True

    @classmethod
    defsupport_deep_gemm(cls) -> bool:
"""Currently, only Hopper and Blackwell GPUs are supported."""
        return cls.is_device_capability(90) or cls.is_device_capability_family(100)

    @classmethod
    defis_integrated_gpu(cls, device_id: int = 0) -> bool:
        return bool(torch.cuda.get_device_properties(device_id).is_integrated)

    @classmethod
    defnum_compute_units(cls, device_id: int = 0) -> int:
        return torch.cuda.get_device_properties(device_id).multi_processor_count

    @classmethod
    defuse_custom_op_collectives(cls) -> bool:
        return True

    @classmethod
    defget_default_ir_op_priority(cls, vllm_config: VllmConfig) -> IrOpPriorityConfig:
        fromvllm.config.compilationimport CompilationMode
        fromvllm.config.kernelimport IrOpPriorityConfig

        # Native used by default when compiling,
        # use vllm_c kernels where available when no codegen
        cc = vllm_config.compilation_config
        using_inductor = cc.backend == "inductor" and cc.mode != CompilationMode.NONE
        default = ["native"] if using_inductor else ["vllm_c", "native"]

        # Use oink if enabled for rms_norm
        # TODO(Laurawly/luka): remove this env var,
        #  users can just use IR op priority directly
        rms_norm = default
        if envs.VLLM_USE_OINK_OPS:
            rms_norm = ["oink"] + default

        return IrOpPriorityConfig.with_default(
            default, rms_norm=rms_norm, fused_add_rms_norm=rms_norm
        )
```