---
title: interface - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/platforms/interface/
source: sitemap
fetched_at: 2026-05-07T21:34:33.042030398-03:00
rendered_js: false
word_count: 164
summary: This document defines the base Platform class for vLLM, providing a unified interface for hardware-specific configuration, device management, kernel loading, and compilation strategies across different accelerators.
tags:
    - vllm
    - platform-abstraction
    - hardware-acceleration
    - device-management
    - kernel-interface
    - compilation-backend
category: concept
---

```
classPlatform:
    _enum: PlatformEnum
    device_name: str
    device_type: str

    # available dispatch keys:
    # check https://github.com/pytorch/pytorch/blob/313dac6c1ca0fa0cde32477509cce32089f8532a/torchgen/model.py#L134 # noqa
    # use "CPU" as a fallback for platforms not registered in PyTorch
    dispatch_key: str = "CPU"

    # available ray device keys:
    # https://github.com/ray-project/ray/blob/10ba5adadcc49c60af2c358a33bb943fb491a171/python/ray/_private/ray_constants.py#L438 # noqa
    # empty string means the device does not support ray
    ray_device_key: str = ""

    # platform-agnostic way to specify the device control environment variable,
    # .e.g. CUDA_VISIBLE_DEVICES for CUDA.
    # hint: search for "get_visible_accelerator_ids_env_var" in
    # https://github.com/ray-project/ray/tree/master/python/ray/_private/accelerators # noqa
    device_control_env_var: str = "VLLM_DEVICE_CONTROL_ENV_VAR_PLACEHOLDER"

    # environment variables that need to be set to 1 to prevent ray from
    # setting the visible devices e.g.
    # RAY_EXPERIMENTAL_NOSET_CUDA_VISIBLE_DEVICES
    ray_noset_device_env_vars: list[str] = []

    # The torch.compile backend for compiling simple and
    # standalone functions. The default value is "inductor" to keep
    # the same behavior as PyTorch.
    # NOTE: for the forward part of the model, vLLM has another separate
    # compilation strategy.
    simple_compile_backend: str = "inductor"

    # The backend used for distributed communication.
    dist_backend: str = ""

    supported_quantization: list[str] = []

    additional_env_vars: list[str] = []

    _global_graph_pool: Any | None = None

    @property
    defpass_key(self) -> str:
"""Inductor config key for the PassManager custom pass"""
        return "post_grad_custom_post_pass"

    @property
    defsupported_dtypes(self) -> list[torch.dtype]:
"""Returns the supported dtypes for the current platform."""
        # Be careful with the order of the dtypes. The first dtype will
        # be used as the default dtype fallback for the current platform,
        # when encountering unsupported dtypes in "auto" dtype.
        return [torch.bfloat16, torch.float16, torch.float32]

    defis_cuda(self) -> bool:
        return self._enum == PlatformEnum.CUDA

    defis_rocm(self) -> bool:
        return self._enum == PlatformEnum.ROCM

    defis_tpu(self) -> bool:
        return self._enum == PlatformEnum.TPU

    defis_xpu(self) -> bool:
        return self._enum == PlatformEnum.XPU

    defis_cpu(self) -> bool:
        return self._enum == PlatformEnum.CPU

    defis_zen_cpu(self) -> bool:
        return False

    defis_out_of_tree(self) -> bool:
        return self._enum == PlatformEnum.OOT

    defis_unspecified(self) -> bool:
        return self._enum == PlatformEnum.UNSPECIFIED

    defget_max_output_tokens(self, prompt_len: int) -> int:
        return sys.maxsize

    defis_cuda_alike(self) -> bool:
"""Stateless version of [torch.cuda.is_available][]."""
        return self._enum in (PlatformEnum.CUDA, PlatformEnum.ROCM)

    defis_sleep_mode_available(self) -> bool:
        # TODO: Actually only mi3xx has the sleep mode support now
        # for ROCm, but currently we don't have a way to detect the
        # exact GPU model statelessly here. So we return True for
        # all ROCm platforms for now.
        return self._enum in (PlatformEnum.CUDA, PlatformEnum.ROCM)

    @classmethod
    defget_pass_manager_cls(cls) -> str:
"""
        Get the pass manager class for this platform.
        It will be registered as a custom pass under the current_platform.pass_key.
        """
        return "vllm.compilation.passes.pass_manager.PostGradPassManager"

    @classmethod
    defget_compile_backend(cls) -> str:
"""
        Get the custom compile backend for current platform.
        """
        return cls.simple_compile_backend

    @classmethod
    defimport_ir_kernels(cls) -> None:
"""
        The default implementation imports ``vllm.kernels``, which registers
        the built-in IR op implementations. Out-of-tree (OOT) platforms should
        override this method to import their own kernel modules.
        """
        importvllm.kernels  # noqa: F401

    @classmethod
    defdevice_id_to_physical_device_id(cls, device_id: int):
        # Treat empty device control env var as unset. This is a valid
        # configuration in Ray setups where the engine is launched in
        # a CPU-only placement group located on a GPU node.
        if (
            cls.device_control_env_var in os.environ
            and os.environ[cls.device_control_env_var] != ""
        ):
            device_ids = os.environ[cls.device_control_env_var].split(",")
            physical_device_id = device_ids[device_id]
            return int(physical_device_id)
        else:
            return device_id

    @classmethod
    defimport_kernels(cls) -> None:
"""Import any platform-specific C kernels."""
        try:
            importvllm._C  # noqa: F401
        except ImportError as e:
            logger.warning("Failed to import from vllm._C: %r", e)
        with contextlib.suppress(ImportError):
            importvllm._moe_C  # noqa: F401

    @classmethod
    defget_attn_backend_cls(
        cls,
        selected_backend: "AttentionBackendEnum",
        attn_selector_config: "AttentionSelectorConfig",
        num_heads: int | None = None,
    ) -> str:
"""Get the attention backend class of a device."""
        return ""

    @classmethod
    defget_supported_vit_attn_backends(cls) -> list["AttentionBackendEnum"]:
        return [
            AttentionBackendEnum.TORCH_SDPA,
        ]

    @classmethod
    defget_vit_attn_backend(
        cls,
        head_size: int,
        dtype: torch.dtype,
        backend: "AttentionBackendEnum | None" = None,
    ) -> "AttentionBackendEnum":
"""
        Get the vision attention backend class of a device.

        NOTE: ViT Attention should be checked and override in the platform-specific
        implementation. we should not override this in any other places, like
        the model_executor/models/<model_name>.py.

        We check if the backend is None or not:
            1. If not, check if the backend is supported by the platform.
            2. If None, continue to the default selection logic.
        """
        if backend is not None:
            assert backend in cls.get_supported_vit_attn_backends(), (
                f"Backend {backend} is not supported for vit attention"
                f"Supported backends are: {cls.get_supported_vit_attn_backends()}"
            )
            logger.info_once(f"Using backend {backend} for vit attention")
            return backend

        logger.info_once(
            f"Using default backend {AttentionBackendEnum.TORCH_SDPA} for vit attention"
        )
        return AttentionBackendEnum.TORCH_SDPA

    @classmethod
    defget_device_capability(
        cls,
        device_id: int = 0,
    ) -> DeviceCapability | None:
"""Stateless version of [torch.cuda.get_device_capability][]."""
        return None

    @classmethod
    defhas_device_capability(
        cls,
        capability: tuple[int, int] | int,
        device_id: int = 0,
    ) -> bool:
"""
        Test whether this platform is compatible with a device capability.

        The `capability` argument can either be:

        - A tuple `(major, minor)`.
        - An integer `<major><minor>`. (See
        [`DeviceCapability.to_int`][vllm.platforms.interface.DeviceCapability.to_int])
        """
        current_capability = cls.get_device_capability(device_id=device_id)
        if current_capability is None:
            return False

        if isinstance(capability, tuple):
            return current_capability >= capability

        return current_capability.to_int() >= capability

    @classmethod
    defis_device_capability(
        cls,
        capability: tuple[int, int] | int,
        device_id: int = 0,
    ) -> bool:
"""
        Test whether this platform has exactly the specified device capability.

        The `capability` argument can either be:

        - A tuple `(major, minor)`.
        - An integer `<major><minor>`. (See
        [`DeviceCapability.to_int`][vllm.platforms.interface.DeviceCapability.to_int])
        """
        current_capability = cls.get_device_capability(device_id=device_id)
        if current_capability is None:
            return False

        if isinstance(capability, tuple):
            return current_capability == capability

        return current_capability.to_int() == capability

    @classmethod
    defis_device_capability_family(
        cls,
        capability: int,
        device_id: int = 0,
    ) -> bool:
"""
        Returns True if the device capability is any <major>.x.
        Mirrors CUDA 13 'family' architecture semantics (e.g. 10.x, 11.x, 12.x).
        """
        current_capability = cls.get_device_capability(device_id=device_id)
        if current_capability is None:
            return False
        return (current_capability.to_int() // 10) == (capability // 10)

    @classmethod
    defget_device_name(cls, device_id: int = 0) -> str:
"""Get the name of a device."""
        raise NotImplementedError

    @classmethod
    defget_device_uuid(cls, device_id: int = 0) -> str:
"""Get the uuid of a device, e.g. the PCI bus ID."""
        raise NotImplementedError

    @classmethod
    defget_device_total_memory(cls, device_id: int = 0) -> int:
"""Get the total memory of a device in bytes."""
        raise NotImplementedError

    @classmethod
    definference_mode(cls):
"""A device-specific wrapper of `torch.inference_mode`.

        This wrapper is recommended because some hardware backends such as TPU
        do not support `torch.inference_mode`. In such a case, they will fall
        back to `torch.no_grad` by overriding this method.
        """
        return torch.inference_mode(mode=True)

    @classmethod
    defset_device(cls, device: torch.device) -> None:
"""
        Set the device for the current platform.
        """
        raise NotImplementedError

    @classmethod
    defmanual_seed_all(cls, seed: int) -> None:
"""Set RNG seed across all devices for the current platform."""
        raise NotImplementedError

    @classmethod
    defpre_register_and_update(
        cls, parser: FlexibleArgumentParser | None = None
    ) -> None:
"""
        Do some pre-registration or update action for the current platform.

        This function is called before global VllmConfig is initialized or cli
        arguments are parsed. It's used for out-of-tree platforms to register or
        update the configuration.

        For example, the out-of-tree quantization config can be imported and
        registered here dynamically.
        """
        pass

    @classmethod
    defapply_config_platform_defaults(cls, vllm_config: "VllmConfig") -> None:
"""
        Apply the platform-specific default values to the config.

        This function is called during the initialization of global VllmConfig, after
        parsing cli arguments.
        It can modify the defaults of the config according to the platform. For example,
        it can enable custom_ops based on the enabled features.

        The config is passed by reference, so it can be modified in place.
        """
        pass

    @classmethod
    defcheck_and_update_config(cls, vllm_config: "VllmConfig") -> None:
"""
        Check and update the configuration for the current platform.

        It can raise an exception if the configuration is not compatible with
        the current platform, or it can update the configuration to make it
        compatible with the current platform.

        The config is passed by reference, so it can be modified in place.
        """
        pass

    @classmethod
    def_find_non_ssm_backend(
        cls, vllm_config: "VllmConfig"
    ) -> "type[AttentionBackend] | None":
"""Find the first non-SSM attention backend from model layers."""
        fromvllm.config.vllmimport get_layers_from_vllm_config
        fromvllm.model_executor.layers.attention_layer_baseimport (
            AttentionLayerBase,
        )

        attn_layers = get_layers_from_vllm_config(
            vllm_config,
            AttentionLayerBase,  # type: ignore[type-abstract]
        )
        for layer in attn_layers.values():
            b = layer.get_attn_backend()
            if not b.is_ssm():
                return b
        return None

    @classmethod
    defupdate_block_size_for_backend(cls, vllm_config: "VllmConfig") -> None:
"""
        Ensure block_size is compatible with the attention backend.
        For hybrid models, also aligns block_size with mamba page sizes.
        """
        fromvllm.config.cacheimport CacheConfig
        fromvllm.config.vllmimport set_current_vllm_config

        cache_config = vllm_config.cache_config
        model_config = vllm_config.model_config

        # model_config may be None during testing.
        if not model_config:
            return

        backend_cls = cls._find_non_ssm_backend(vllm_config)
        if backend_cls is None:
            return

        # Phase 1: Pick block size from backend (skip if user set --block-size)
        if not cache_config.user_specified_block_size:
            with set_current_vllm_config(vllm_config):
                preferred = backend_cls.get_preferred_block_size(
                    CacheConfig.DEFAULT_BLOCK_SIZE
                )
            if preferred != CacheConfig.DEFAULT_BLOCK_SIZE:
                logger.info(
                    "Setting kv cache block size to %d for %s backend.",
                    preferred,
                    backend_cls.get_name(),
                )
            cache_config.block_size = preferred

        # Phase 2: Align block/mamba sizes for hybrid models
        # (may override user settings).
        if model_config.is_hybrid:
            cls._align_hybrid_block_size(vllm_config, backend_cls)

    @classmethod
    def_align_hybrid_block_size(
        cls,
        vllm_config: "VllmConfig",
        backend_cls: "type[AttentionBackend]",
    ) -> None:
"""
        For hybrid attention/mamba models, ensure that the attention page
        size is >= the mamba page size, and pad the mamba page size to match.
        """
        frommathimport lcm

        fromvllm.config.vllmimport set_current_vllm_config
        fromvllm.model_executor.modelsimport ModelRegistry
        fromvllm.utils.math_utilsimport cdiv
        fromvllm.utils.torch_utilsimport STR_DTYPE_TO_TORCH_DTYPE
        fromvllm.v1.attention.backendimport MultipleOf
        fromvllm.v1.kv_cache_interfaceimport (
            FullAttentionSpec,
            MambaSpec,
            MLAAttentionSpec,
            get_kv_quant_mode,
        )

        cache_config = vllm_config.cache_config
        model_config = vllm_config.model_config
        parallel_config = vllm_config.parallel_config

        if cache_config.cache_dtype == "auto":
            kv_cache_dtype = model_config.dtype
        else:
            kv_cache_dtype = STR_DTYPE_TO_TORCH_DTYPE[cache_config.cache_dtype]

        kv_quant_mode = get_kv_quant_mode(cache_config.cache_dtype)

        # Compute attention page size for 1 token
        if model_config.use_mla:
            attn_page_size_1_token = MLAAttentionSpec(
                block_size=1,
                num_kv_heads=model_config.get_num_kv_heads(parallel_config),
                head_size=model_config.get_head_size(),
                dtype=kv_cache_dtype,
                kv_quant_mode=kv_quant_mode,
            ).page_size_bytes
        elif cache_config.cache_dtype.startswith("turboquant_"):
            # TQ has a packed K|V layout; the standard FullAttentionSpec
            # formula over-sizes it and trips unify_kv_cache_spec_page_size
            # when all attention layers are TQ. With mixed skip+TQ the skip
            # layers still use the standard layout — take max so mamba
            # padding covers the largest actual page.
            fromvllm.model_executor.layers.quantization.turboquant.configimport (
                TurboQuantConfig,
            )
            fromvllm.v1.kv_cache_interfaceimport TQFullAttentionSpec

            tq_cfg = TurboQuantConfig.from_cache_dtype(
                cache_config.cache_dtype, model_config.get_head_size()
            )
            tq_page = TQFullAttentionSpec(
                block_size=1,
                num_kv_heads=model_config.get_num_kv_heads(parallel_config),
                head_size=model_config.get_head_size(),
                head_size_v=model_config.get_head_size(),
                dtype=kv_cache_dtype,
                kv_quant_mode=kv_quant_mode,
                tq_slot_size=tq_cfg.slot_size_aligned,
            ).page_size_bytes
            if cache_config.kv_cache_dtype_skip_layers:
                skip_page = FullAttentionSpec(
                    block_size=1,
                    num_kv_heads=model_config.get_num_kv_heads(parallel_config),
                    head_size=model_config.get_head_size(),
                    dtype=model_config.dtype,
                ).page_size_bytes
                # lcm, not max: skip_page is often not a multiple of
                # tq_page, so max would leave per-layer page sizes
                # un-unifiable downstream.
                attn_page_size_1_token = lcm(tq_page, skip_page)
            else:
                attn_page_size_1_token = tq_page
        else:
            attn_page_size_1_token = FullAttentionSpec(
                block_size=1,
                num_kv_heads=model_config.get_num_kv_heads(parallel_config),
                head_size=model_config.get_head_size(),
                dtype=kv_cache_dtype,
                kv_quant_mode=kv_quant_mode,
            ).page_size_bytes

        # Compute mamba page size
        model_cls, _ = ModelRegistry.resolve_model_cls(
            model_config.architecture,
            model_config=model_config,
        )
        mamba_page_size = MambaSpec(
            shapes=model_cls.get_mamba_state_shape_from_config(vllm_config),
            dtypes=model_cls.get_mamba_state_dtype_from_config(vllm_config),
            block_size=-1,
        ).page_size_bytes

        if mamba_page_size == 0:
            return

        # mamba_block_size here should either be user specified value or None
        mamba_block_size = (
            cache_config.mamba_block_size
            if cache_config.user_specified_mamba_block_size
            else None
        )

        # Get kernel block alignment from the backend's supported sizes
        with set_current_vllm_config(vllm_config):
            kernel_block_alignment_size = max(
                min(
                    s.base if isinstance(s, MultipleOf) else s
                    for s in backend_cls.get_supported_kernel_block_sizes()
                ),
                cache_config.block_size,
            )

        if cache_config.mamba_cache_mode == "all":
            # With prefix caching, align to mamba chunk size for kernel perf
            # TODO(tdoublep): this constraint can be relaxed fairly
            # easily by changing the way we layout chunks in the
            # mamba2 kernels.
            base_chunk_size = mamba_block_size or model_config.get_mamba_chunk_size()
            assert base_chunk_size is not None
            attn_tokens_per_mamba_state = cdiv(mamba_page_size, attn_page_size_1_token)
            chunk_size = lcm(base_chunk_size, kernel_block_alignment_size)
            attn_block_size = chunk_size * cdiv(attn_tokens_per_mamba_state, chunk_size)
            cache_config.mamba_block_size = attn_block_size
        else:
            # Without prefix caching, use minimum block size that satisfies
            # both backend alignment and mamba page size compatibility
            attn_block_size = kernel_block_alignment_size * cdiv(
                mamba_page_size,
                kernel_block_alignment_size * attn_page_size_1_token,
            )

        if cache_config.block_size < attn_block_size:
            cache_config.block_size = attn_block_size
            logger.info(
                "Setting attention block size to %d tokens "
                "to ensure that attention page size is >= mamba page size.",
                attn_block_size,
            )

        if cache_config.mamba_cache_mode == "align":
            cache_config.mamba_block_size = cache_config.block_size

        # Pad mamba page size to exactly match attention page size
        attn_page_size = cache_config.block_size * attn_page_size_1_token
        assert attn_page_size >= mamba_page_size

        if attn_page_size == mamba_page_size:
            return

        if (
            cache_config.mamba_page_size_padded is None
            or cache_config.mamba_page_size_padded != attn_page_size
        ):
            cache_config.mamba_page_size_padded = attn_page_size
            mamba_padding_pct = (
                100 * (attn_page_size - mamba_page_size) / mamba_page_size
            )
            logger.info(
                "Padding mamba page size by %.2f%% to ensure "
                "that mamba page size and attention page size are "
                "exactly equal.",
                mamba_padding_pct,
            )

    @classmethod
    defverify_model_arch(cls, model_arch: str) -> None:
"""
        Verify whether the current platform supports the specified model
        architecture.

        - This will raise an Error or Warning based on the model support on
        the current platform.
        - By default all models are considered supported.
        """
        pass

    @classmethod
    defverify_quantization(cls, quant: str) -> None:
"""
        Verify whether the quantization is supported by the current platform.
        """
        if cls.supported_quantization and quant not in cls.supported_quantization:
            raise ValueError(
                f"{quant} quantization is currently not supported in {cls.device_name}."
            )

    @classmethod
    defget_cpu_architecture(cls) -> CpuArchEnum:
"""
        Determine the CPU architecture of the current system.
        Returns CpuArchEnum indicating the architecture type.
        """
        machine = platform.machine().lower()

        if machine in ("x86_64", "amd64", "i386", "i686"):
            return CpuArchEnum.X86
        elif machine.startswith("arm") or machine.startswith("aarch"):
            return CpuArchEnum.ARM
        elif machine.startswith("ppc"):
            return CpuArchEnum.POWERPC
        elif machine == "s390x":
            return CpuArchEnum.S390X
        elif machine.startswith("riscv"):
            return CpuArchEnum.RISCV

        return CpuArchEnum.OTHER if machine else CpuArchEnum.UNKNOWN

    @classmethod
    defis_pin_memory_available(cls) -> bool:
"""Checks whether pin memory is available on the current platform."""
        if in_wsl():
            # Pinning memory in WSL is not supported.
            # https://docs.nvidia.com/cuda/wsl-user-guide/index.html#known-limitations-for-linux-cuda-applications
            logger.warning(
                "Using 'pin_memory=False' as WSL is detected. "
                "This may slow down the performance."
            )
            return False
        return True

    @classmethod
    defget_current_memory_usage(
        cls, device: torch.types.Device | None = None
    ) -> float:
"""
        Return the memory usage in bytes.
        """
        raise NotImplementedError

    @classmethod
    defget_punica_wrapper(cls) -> str:
"""
        Return the punica wrapper for current platform.
        """
        raise NotImplementedError

    @classmethod
    defget_infinity_values(cls, dtype: torch.dtype) -> tuple[float, float]:
"""
        Return the platform specific values for (-inf, inf)
        """
        return float("-inf"), float("inf")

    @classmethod
    defcan_update_inplace(cls) -> bool:
"""
        Checks if the platform allows inplace memory updates
        """
        return True

    @classmethod
    defget_lora_vocab_padding_size(cls) -> int:
"""
        Returns how much padding the LoRA logits need for kernels
        """
        return 256

    @classmethod
    defget_device_communicator_cls(cls) -> str:
"""
        Get device specific communicator class for distributed communication.
        """
        return "vllm.distributed.device_communicators.base_device_communicator.DeviceCommunicatorBase"  # noqa

    @classmethod
    defis_integrated_gpu(cls, device_id: int = 0) -> bool:
"""
        Returns whether the GPU is an integrated (UMA) device that shares
        system memory with the CPU.

        On UMA systems (e.g. NVIDIA GH200, DGX Spark, Jetson Orin),
        cudaMemGetInfo may underreport free memory because it does not
        account for reclaimable OS memory (page cache, buffers).
        """
        return False

    @classmethod
    defsupports_mx(cls) -> bool:
"""
        Returns whether the current platform supports MX types.
        """
        return False

    @classmethod
    defsupports_fp8(cls) -> bool:
"""
        Returns whether the current platform supports FP8 types.
        """
        return False

    @classmethod
    defis_fp8_fnuz(cls) -> bool:
"""
        Returns whether the preferred FP8 type is FNUZ on the current platform.

        There are two representations of FP8, OCP FP8 and FNUZ FP8.
        The OCP specification can be found at https://tinyurl.com/b7jvwpft.
        The FNUZ specification can be found at https://tinyurl.com/5n6hwwu5.

        AMD's MI300 and MI325 have native hardware support for FNUZ. All other
        hardware has converged on the OCP FP8 standard.
        """
        return False

    @classmethod
    deffp8_dtype(cls) -> torch.dtype:
"""
        Returns the preferred FP8 type on the current platform.

        See the documentation for is_fp8_fnuz for details.
        """
        return torch.float8_e4m3fn

    @classmethod
    defuse_all_gather(cls) -> bool:
"""
        Whether to use allgather in LogitsProcessor to gather the logits.
        """
        return True

    @classmethod
    defuse_custom_allreduce(cls) -> bool:
"""
        Returns if custom allreduce is supported on the current platform
        """
        return False

    @classmethod
    defopaque_attention_op(cls) -> bool:
"""
        Returns True if we register attention as one giant opaque custom op
        on the current platform
        """
        return False

    @classmethod
    defvalidate_request(
        cls,
        processed_inputs: "EngineInput",
        params: "SamplingParams | PoolingParams",
    ) -> None:
"""Raises if this request is unsupported on this platform"""

    def__getattr__(self, key: str):
        # Pickle checks dunder methods like __getstate__. If we return None
        # for them, pickle treats it like a real value and tries to call it.
        if key.startswith("__") and key.endswith("__"):
            raise AttributeError(key)

        device = getattr(torch, self.device_type, None)
        if device is not None and hasattr(device, key):
            attr = getattr(device, key)
            # NOTE: `hasattr(device, key)=True` can only avoid AttributeError,
            # but the value of this attr could be `None`.
            if attr is not None:
                return attr

        logger.warning(
            "Current platform %s does not have '%s' attribute.",
            self.device_type,
            key,
        )
        return None

    defget_global_graph_pool(self) -> Any:
"""
        Return the global graph pool for this platform.
        """
        cls = self.__class__
        if cls._global_graph_pool is None:
            cls._global_graph_pool = self.graph_pool_handle()
        return cls._global_graph_pool

    @classmethod
    defget_static_graph_wrapper_cls(cls) -> str:
"""
        Get static graph wrapper class for static graph.
        """
        return "vllm.compilation.base_static_graph.AbstractStaticGraphWrapper"

    @classmethod
    defstateless_init_device_torch_dist_pg(
        cls,
        backend: str,
        prefix_store: "PrefixStore",
        group_rank: int,
        group_size: int,
        timeout: timedelta,
    ) -> "ProcessGroup":
"""
        Init platform-specific torch distributed process group.
        """
        raise NotImplementedError

    @classmethod
    defcheck_if_supports_dtype(cls, dtype: torch.dtype):
"""
        Check if the dtype is supported by the current platform.
        """
        raise NotImplementedError

    @classmethod
    defsupport_hybrid_kv_cache(cls) -> bool:
"""
        Returns if the hybrid kv cache is supported by the current platform.
        """
        return False

    @classmethod
    defsupport_static_graph_mode(cls) -> bool:
"""
        Returns if the graph mode is supported by the current platform.
        """
        return False

    @classmethod
    defsupport_deep_gemm(cls) -> bool:
"""
        Returns if DeepGEMM is supported by the current platform.
        """
        return False

    @classmethod
    defuse_custom_op_collectives(cls) -> bool:
"""
        Whether this platform should use torch.ops.vllm.* custom ops for collectives.

        Returns False by default - platforms must explicitly opt-in.
        """
        return False

    @classmethod
    defuse_sync_weight_loader(cls) -> bool:
"""
        Returns if the current platform needs to sync weight loader.
        """
        return False

    @classmethod
    defmake_synced_weight_loader(cls, original_weight_loader):
"""
        Wrap the original weight loader to make it synced.
        """
        if not cls.use_sync_weight_loader():
            return original_weight_loader

        def_synced_weight_loader(param, *args, **kwargs):
            out = original_weight_loader(param, *args, **kwargs)
            if param.device != torch.device("cpu"):
                torch._sync(param)
            return out

        return _synced_weight_loader

    @classmethod
    defget_nixl_supported_devices(cls) -> dict[str, tuple[str, ...]]:
"""
        Returns a mapping from device_type to a tuple of supported
        kv_buffer_device for nixl.
        """
        return {}

    @classmethod
    defget_nixl_memory_type(cls) -> str | None:
"""
        Returns the nixl memory type for the current platform.
        """
        return None

    @classmethod
    defcheck_max_model_len(cls, max_model_len: int) -> int:
"""
        Check max_model_len for the current platform.
        """
        return max_model_len

    @classmethod
    defset_additional_forward_context(cls, *args, **kwargs) -> dict[str, Any]:
"""
        Set some additional forward context for the current platform if needs.
        """
        return {}

    @classmethod
    defnum_compute_units(cls, device_id: int = 0) -> int:
"""
        Get the number of compute units for the current platform.
        (NVIDIA SM / AMD CU / Intel EU)
        """
        raise NotImplementedError(
            "num_compute_units is not implemented for the current platform."
        )

    @classmethod
    defget_default_ir_op_priority(
        cls, vllm_config: "VllmConfig"
    ) -> "IrOpPriorityConfig":
"""Get the default IR op priority for the current platform."""
        fromvllm.config.kernelimport IrOpPriorityConfig

        # Native always used by default. Platforms can override this behavior.
        return IrOpPriorityConfig.with_default(["native"])
```