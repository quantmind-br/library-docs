---
title: rocm - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/platforms/rocm/
source: sitemap
fetched_at: 2026-05-07T21:34:33.957307179-03:00
rendered_js: false
word_count: 31
summary: This document defines the RocmPlatform class, which manages ROCm-specific device configurations, kernel loading, and attention backend selection within the vLLM architecture.
tags:
    - rocm
    - vllm
    - attention-backend
    - gpu-acceleration
    - model-quantization
    - platform-configuration
category: concept
---

```
classRocmPlatform(Platform):
    _enum = PlatformEnum.ROCM
    device_name: str = "rocm"
    device_type: str = "cuda"
    dispatch_key: str = "CUDA"
    ray_device_key: str = "GPU"
    dist_backend: str = "nccl"
    # rocm shares the same device control env var as CUDA
    device_control_env_var: str = "CUDA_VISIBLE_DEVICES"
    ray_noset_device_env_vars: list[str] = [
        "RAY_EXPERIMENTAL_NOSET_HIP_VISIBLE_DEVICES",
        "RAY_EXPERIMENTAL_NOSET_CUDA_VISIBLE_DEVICES",
        "RAY_EXPERIMENTAL_NOSET_ROCR_VISIBLE_DEVICES",
    ]

    supported_quantization: list[str] = [
        "awq",
        "awq_marlin",  # will be overwritten with awq
        "gptq",
        "gptq_marlin",  # will be overwritten with gptq
        "fp8",
        "deepseek_v4_fp8",
        "compressed-tensors",
        "fbgemm_fp8",
        "gguf",
        "quark",
        "mxfp4",
        "mxfp8",
        "torchao",
        "bitsandbytes",
        "modelopt",
        "modelopt_fp4",
        "modelopt_mxfp8",
        "modelopt_mixed",
        "fp8_per_tensor",
        "fp8_per_block",
        "online",
        "gpt_oss_mxfp4",
    ]

    @classmethod
    defimport_kernels(cls) -> None:
"""Import ROCm-specific kernels."""
        super().import_kernels()

        importcontextlib

        # Import ROCm-specific extension
        with contextlib.suppress(ImportError):
            importvllm._rocm_C  # noqa: F401

    @classmethod
    defget_valid_backends(
        cls,
        device_capability: DeviceCapability,
        attn_selector_config: "AttentionSelectorConfig",
        num_heads: int | None = None,
    ) -> tuple[
        list[tuple["AttentionBackendEnum", int]],
        dict["AttentionBackendEnum", list[str]],
    ]:
        valid_backends_priorities = []
        invalid_reasons = {}

        backend_priorities = _get_backend_priorities(
            attn_selector_config.use_mla,
            attn_selector_config.use_sparse,
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
                invalid_reasons[backend] = invalid_reasons_i
            else:
                valid_backends_priorities.append((backend, priority))

        return valid_backends_priorities, invalid_reasons

    @classmethod
    defget_attn_backend_cls(
        cls,
        selected_backend: "AttentionBackendEnum",
        attn_selector_config: "AttentionSelectorConfig",
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
                logger.info_once(
                    "Using %s backend (selected via --attention-backend).",
                    selected_backend.name,
                )
                return selected_backend.get_path()

        # No selected backend or the selected backend is invalid,
        # so we try finding a valid backend.
        valid_backends_priorities, invalid_reasons = cls.get_valid_backends(
            device_capability=device_capability,
            attn_selector_config=attn_selector_config,
            num_heads=num_heads,
        )
        reasons_str = (
            "{"
            + ", ".join(
                f"{backend.name}: [{', '.join(reasons)}]"
                for backend, reasons in invalid_reasons.items()
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
        valid_str = (
            "[" + ", ".join(f"'{b[0].name}'" for b in valid_backends_priorities) + "]"
        )
        if invalid_reasons:
            rejected_str = ", ".join(b.name for b in invalid_reasons)
            logger.info(
                "Found incompatible backend(s) [%s] with %s. "
                "Overriding with %s out of potential backends: %s.",
                rejected_str,
                attn_selector_config.attn_type,
                selected_backend.name,
                valid_str,
            )
        else:
            logger.info_once(
                "Using %s backend out of potential backends: %s.",
                selected_backend.name,
                valid_str,
            )

        return selected_backend.get_path()

    @classmethod
    defget_supported_vit_attn_backends(cls) -> list["AttentionBackendEnum"]:
        return [
            AttentionBackendEnum.FLASH_ATTN,
            AttentionBackendEnum.ROCM_AITER_FA,
            AttentionBackendEnum.TRITON_ATTN,
            AttentionBackendEnum.TORCH_SDPA,
        ]

    @classmethod
    defget_vit_attn_backend(
        cls,
        head_size: int,
        dtype: torch.dtype,
        backend: "AttentionBackendEnum | None" = None,
    ) -> "AttentionBackendEnum":
        if backend is not None:
            assert backend in cls.get_supported_vit_attn_backends(), (
                f"Backend {backend} is not supported for vit attention. "
                f"Supported backends are: {cls.get_supported_vit_attn_backends()}"
            )
            logger.info_once(f"Using backend {backend} for vit attention")
            return backend

        fromimportlib.utilimport find_spec

        fromvllm._aiter_opsimport rocm_aiter_ops

        if rocm_aiter_ops.is_enabled() and on_gfx9():
            logger.info_once("Using AITER Flash Attention backend for ViT model.")
            return AttentionBackendEnum.ROCM_AITER_FA

        if (
            on_gfx9()
            and find_spec("flash_attn") is not None
            and (dtype == torch.float16 or dtype == torch.bfloat16)
        ):
            logger.info_once("Using Flash Attention backend for ViT model.")
            return AttentionBackendEnum.FLASH_ATTN

        # RDNA3/RDNA4 (gfx11xx/gfx12xx): Use Flash Attention Triton backend
        if (
            on_gfx1x()
            and flash_attn_triton_available()
            and (dtype == torch.float16 or dtype == torch.bfloat16)
        ):
            logger.info_once(
                "Using Flash Attention (Triton backend) for ViT model on RDNA."
            )
            return AttentionBackendEnum.FLASH_ATTN

        logger.info_once("Using Torch SDPA backend for ViT model.")
        return AttentionBackendEnum.TORCH_SDPA

    @classmethod
    defset_device(cls, device: torch.device) -> None:
"""
        Set the device for the current platform.
        """
        torch.cuda.set_device(device)

    @classmethod
    defmanual_seed_all(cls, seed: int) -> None:
        torch.cuda.manual_seed_all(seed)

    @classmethod
    @lru_cache(maxsize=8)
    defget_device_capability(cls, device_id: int = 0) -> DeviceCapability | None:
        cap = _capability_from_gcn_arch(_GCN_ARCH)
        if cap is not None:
            return DeviceCapability(major=cap[0], minor=cap[1])

        logger.warning_once(
            "Could not derive device capability from GCN arch '%s', "
            "falling back to torch.cuda (this will initialize CUDA).",
            _GCN_ARCH,
        )
        major, minor = torch.cuda.get_device_capability(device_id)
        return DeviceCapability(major=major, minor=minor)

    @classmethod
    @with_amdsmi_context
    defis_fully_connected(cls, physical_device_ids: list[int]) -> bool:
"""
        Query if the set of gpus are fully connected by xgmi (1 hop)
        """
        handles = [amdsmi_get_processor_handles()[i] for i in physical_device_ids]
        for i, handle in enumerate(handles):
            for j, peer_handle in enumerate(handles):
                if i < j:
                    try:
                        link_type = amdsmi_topo_get_link_type(handle, peer_handle)
                        # type is 2 for XGMI
                        if link_type["hops"] != 1 or link_type["type"] != 2:
                            return False
                    except AmdSmiException as error:
                        logger.error("AMD 1 hop XGMI detection failed.", exc_info=error)
                        return False
        return True

    @classmethod
    @with_amdsmi_context
    @lru_cache(maxsize=8)
    defget_device_name(cls, device_id: int = 0) -> str:
        physical_device_id = cls.device_id_to_physical_device_id(device_id)
        handle = amdsmi_get_processor_handles()[physical_device_id]
        asic_info = amdsmi_get_gpu_asic_info(handle)
        asic_info_device_id: str = asic_info["device_id"]
        if asic_info_device_id in _ROCM_DEVICE_ID_NAME_MAP:
            return _ROCM_DEVICE_ID_NAME_MAP[asic_info_device_id]
        return asic_info["market_name"]

    @classmethod
    @with_amdsmi_context
    defget_device_uuid(cls, device_id: int = 0) -> str:
        try:
            device = amdsmi_get_processor_handles()[device_id]
        except AmdSmiException as error:
            logger.error("amdsmi device query failed ", exc_info=error)
            return ""
        try:
            device_uuid = amdsmi_get_gpu_device_uuid(device)
        except AmdSmiException as error:
            logger.error("amdsmi device uuid query failed ", exc_info=error)
        return device_uuid

    @classmethod
    defget_device_total_memory(cls, device_id: int = 0) -> int:
        device_props = torch.cuda.get_device_properties(device_id)
        return device_props.total_memory

    @classmethod
    defapply_config_platform_defaults(cls, vllm_config: "VllmConfig") -> None:
        fromvllm._aiter_opsimport rocm_aiter_ops

        compilation_config = vllm_config.compilation_config
        use_aiter_fused_moe = rocm_aiter_ops.is_fused_moe_enabled()
        use_aiter_fp8_linear = rocm_aiter_ops.is_linear_fp8_enabled()
        use_aiter_fused_se = rocm_aiter_ops.is_fusion_moe_shared_experts_enabled()

        if use_aiter_fp8_linear and "-quant_fp8" not in compilation_config.custom_ops:
            compilation_config.custom_ops.append("+quant_fp8")

        if use_aiter_fused_se and "-grouped_topk" in compilation_config.custom_ops:
            logger.warning_once(
                "VLLM_ROCM_USE_AITER_FUSION_SHARED_EXPERTS is enabled, which "
                "requires the 'grouped_topk' custom op. Overriding the "
                "user-provided '-grouped_topk'."
            )
            compilation_config.custom_ops.remove("-grouped_topk")
        # Ensure grouped_topk is always enabled when using AITER if
        # its not disabled by user
        if (
            use_aiter_fused_moe
            and "+grouped_topk" not in compilation_config.custom_ops
            and "-grouped_topk" not in compilation_config.custom_ops
        ):
            compilation_config.custom_ops.append("+grouped_topk")

        # Default dispatch to rocm's sparse_attn_indexer implementation
        compilation_config.custom_ops.append("+sparse_attn_indexer")

    @classmethod
    defcheck_and_update_config(cls, vllm_config: "VllmConfig") -> None:
        fromvllm.config.compilationimport CUDAGraphMode

        compilation_config = vllm_config.compilation_config
        parallel_config = vllm_config.parallel_config

        if compilation_config.cudagraph_mode.has_full_cudagraphs():
            # decode context parallel does not support full cudagraphs
            if parallel_config.decode_context_parallel_size > 1:
                logger.warning_once(
                    "Decode context parallel (DCP) is enabled, which is "
                    "incompatible with full CUDA graphs. "
                    "Overriding cudagraph_mode to PIECEWISE."
                )
                compilation_config.cudagraph_mode = CUDAGraphMode.PIECEWISE
            # prefill context parallel do not support full cudagraphs
            elif parallel_config.prefill_context_parallel_size > 1:
                logger.warning_once(
                    "Prefill context parallel (PCP) is enabled, which is "
                    "incompatible with full CUDA graphs. "
                    "Overriding cudagraph_mode to PIECEWISE."
                )
                compilation_config.cudagraph_mode = CUDAGraphMode.PIECEWISE

        if parallel_config.worker_cls == "auto":
            parallel_config.worker_cls = "vllm.v1.worker.gpu_worker.Worker"

    @classmethod
    defverify_model_arch(cls, model_arch: str) -> None:
        if model_arch in _ROCM_UNSUPPORTED_MODELS:
            raise ValueError(
                f"Model architecture '{model_arch}' is not supported by ROCm for now."
            )

        if model_arch in _ROCM_PARTIALLY_SUPPORTED_MODELS:
            msg = _ROCM_PARTIALLY_SUPPORTED_MODELS[model_arch]
            logger.warning(
                "Model architecture '%s' is partially supported by ROCm: %s",
                model_arch,
                msg,
            )

    @classmethod
    defverify_quantization(cls, quant: str) -> None:
        super().verify_quantization(quant)
        if quant == "awq" and not envs.VLLM_USE_TRITON_AWQ:
            logger.warning(
                "Using AWQ quantization with ROCm, but VLLM_USE_TRITON_AWQ"
                " is not set, enabling VLLM_USE_TRITON_AWQ."
            )
        os.environ["VLLM_USE_TRITON_AWQ"] = "1"

    @classmethod
    defget_punica_wrapper(cls) -> str:
        return "vllm.lora.punica_wrapper.punica_gpu.PunicaWrapperGPU"

    @classmethod
    defget_current_memory_usage(
        cls, device: torch.types.Device | None = None
    ) -> float:
        torch.cuda.empty_cache()
        torch.cuda.reset_peak_memory_stats(device)
        return torch.cuda.max_memory_allocated(device)

    @classmethod
    defget_device_communicator_cls(cls) -> str:
        return (
            "vllm.distributed.device_communicators.cuda_communicator.CudaCommunicator"  # noqa
        )

    @classmethod
    defsupports_mx(cls) -> bool:
        return any(gfx in _GCN_ARCH for gfx in ["gfx95"])

    @classmethod
    defsupports_fp8(cls) -> bool:
        return on_gfx9() or on_gfx12x()

    @classmethod
    defis_fp8_fnuz(cls) -> bool:
        # only device 0 is checked, this assumes MI300 platforms are homogeneous
        return "gfx94" in _GCN_ARCH

    @classmethod
    deffp8_dtype(cls) -> torch.dtype:
        if cls.is_fp8_fnuz():
            return torch.float8_e4m3fnuz
        else:
            return torch.float8_e4m3fn

    @classmethod
    defuse_custom_allreduce(cls) -> bool:
        # We only enable custom allreduce for MI300 series
        return any(gfx in _GCN_ARCH for gfx in ["gfx94", "gfx95"])

    @classmethod
    defopaque_attention_op(cls) -> bool:
        return True

    @classmethod
    defis_navi(cls) -> bool:
        return "gfx1" in _GCN_ARCH

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
        return _rocm_device_count_stateless(getattr(envs, cls.device_control_env_var))

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
    defnum_compute_units(cls, device_id: int = 0) -> int:
        return torch.cuda.get_device_properties(device_id).multi_processor_count

    @classmethod
    defuse_custom_op_collectives(cls) -> bool:
        return True

    @classmethod
    defget_default_ir_op_priority(
        cls, vllm_config: "VllmConfig"
    ) -> "IrOpPriorityConfig":
        fromvllm.config.compilationimport CompilationMode, CUDAGraphMode
        fromvllm.config.kernelimport IrOpPriorityConfig

        # Native used by default when compiling,
        # use vllm_c kernels where available when no codegen
        # TODO(luka/TJ) use aiter, vllm_c, native by default on ROCm
        cc = vllm_config.compilation_config
        using_inductor = cc.backend == "inductor" and cc.mode != CompilationMode.NONE
        default = ["native"] if using_inductor else ["vllm_c", "native"]

        #  Aiter rms norm perform best when CUDA Graph capture is enabled.
        # TODO(luka/TJ) remove env vars completely
        if (
            cc.cudagraph_mode != CUDAGraphMode.NONE
            and envs.VLLM_ROCM_USE_AITER
            and envs.VLLM_ROCM_USE_AITER_RMSNORM
        ):
            rms_norm = ["aiter"] + default
        else:
            rms_norm = default

        return IrOpPriorityConfig.with_default(
            default, rms_norm=rms_norm, fused_add_rms_norm=rms_norm
        )

    @classmethod
    @with_amdsmi_context
    defget_all_device_numa_nodes(cls) -> list[int] | None:
"""Get NUMA nodes for all visible GPU devices."""
        try:
            handles = amdsmi_get_processor_handles()
            numa_nodes = []
            for device_id in range(cls.device_count()):
                physical_device_id = cls.device_id_to_physical_device_id(device_id)
                try:
                    numa_node = amdsmi_topo_get_numa_node_number(
                        handles[physical_device_id]
                    )
                except AmdSmiException as e:
                    logger.warning(
                        "Could not detect NUMA node for GPU %d, "
                        "disabling automatic NUMA binding: %s",
                        device_id,
                        e,
                    )
                    return None
                numa_nodes.append(numa_node)
            return numa_nodes
        except Exception as e:
            logger.warning("Failed to get NUMA nodes for GPUs: %s", e)
            return None
```