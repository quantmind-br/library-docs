---
title: vllm - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/
source: sitemap
fetched_at: 2026-05-07T21:15:36.634771528-03:00
rendered_js: false
word_count: 6602
summary: This document provides technical documentation and class definitions for the vLLM inference engine, covering core configuration arguments and output schemas for completions, embeddings, and classification tasks.
tags:
    - vllm
    - llm-inference
    - api-reference
    - python-dataclasses
    - model-serving
    - engine-configuration
category: reference
---

vLLM: a high-throughput and memory-efficient inference engine for LLMs

Modules:

Name Description `assets` `beam_search` `benchmarks` `collect_env` `compilation` `config` `connections` `device_allocator` `distributed` `engine` `entrypoints` `env_override` `envs` `exceptions`

Custom exceptions for vLLM.

`forward_context` `inputs` `ir` `kernels`

Kernel implementations for vLLM.

`logger`

Logging configuration for vLLM.

`logging_utils` `logits_process` `logprobs` `lora` `model_executor` `model_inspection`

Model inspection utilities for vLLM.

`multimodal` `outputs` `parser` `platforms` `plugins` `pooling_params` `profiler` `ray` `reasoning` `renderers` `sampling_params`

Sampling parameters for text generation.

`scalar_type` `sequence`

Sequence and its related classes.

`third_party` `tokenizers` `tool_parsers` `tracing` `transformers_utils` `triton_utils` `usage` `utils` `v1` `version` `vllm_flash_attn`

## PromptType `module-attribute` [¶](#vllm.PromptType "Permanent link")

Schema for any prompt, regardless of model type.

This is the input format accepted by most [`LLM`](https://docs.vllm.ai/en/latest/api/vllm/entrypoints/llm/#vllm.entrypoints.llm.LLM "            LLM") APIs.

## AsyncEngineArgs `dataclass` [¶](#vllm.AsyncEngineArgs "Permanent link")

Bases: `EngineArgs`

Arguments for asynchronous vLLM engine.

Source code in `vllm/engine/arg_utils.py`

```
@dataclass
classAsyncEngineArgs(EngineArgs):
"""Arguments for asynchronous vLLM engine."""

    enable_log_requests: bool = False

    @staticmethod
    defadd_cli_args(
        parser: FlexibleArgumentParser, async_args_only: bool = False
    ) -> FlexibleArgumentParser:
        # Initialize plugin to update the parser, for example, The plugin may
        # add a new kind of quantization method to --quantization argument or
        # a new device to --device argument.
        load_general_plugins()
        if not async_args_only:
            parser = EngineArgs.add_cli_args(parser)
        parser.add_argument(
            "--enable-log-requests",
            action=argparse.BooleanOptionalAction,
            default=AsyncEngineArgs.enable_log_requests,
            help="Enable logging request information, dependent on log level:\n"
            "- INFO: Request ID, parameters and LoRA request.\n"
            "- DEBUG: Prompt inputs (e.g: text, token IDs).\n"
            "You can set the minimum log level via `VLLM_LOGGING_LEVEL`.",
        )
        current_platform.pre_register_and_update(parser)
        return parser
```

## ClassificationOutput `dataclass` [¶](#vllm.ClassificationOutput "Permanent link")

The output data of one classification output of a request.

Parameters:

Name Type Description Default `probs` `list[float]`

The probability vector, which is a list of floats. Its length depends on the number of classes.

*required*

Source code in `vllm/outputs.py`

```
@dataclass
classClassificationOutput:
"""The output data of one classification output of a request.

    Args:
        probs: The probability vector, which is a list of floats.
            Its length depends on the number of classes.
    """

    probs: list[float]

    @staticmethod
    deffrom_base(pooling_output: PoolingOutput):
        # pooling_output shape: (num_classes)
        pooled_data = pooling_output.data
        if pooled_data.ndim != 1:
            raise ValueError("pooled_data should be a 1-D probability vector")

        return ClassificationOutput(pooled_data.tolist())

    @property
    defnum_classes(self) -> int:
        return len(self.probs)

    def__repr__(self) -> str:
        return f"ClassificationOutput(num_classes={self.num_classes})"
```

## CompletionOutput `dataclass` [¶](#vllm.CompletionOutput "Permanent link")

The output data of one completion output of a request.

Parameters:

Name Type Description Default `index` `int`

The index of the output in the request.

*required* `text` `str`

The generated output text.

*required* `token_ids` `Sequence[int]`

The token IDs of the generated output text.

*required* `cumulative_logprob` `float | None`

The cumulative log probability of the generated output text.

*required* `logprobs` `SampleLogprobs | None`

The log probabilities of the top probability words at each position if the logprobs are requested.

*required* `finish_reason` `str | None`

The reason why the sequence is finished.

`None` `stop_reason` `int | str | None`

The stop string or token id that caused the completion to stop, None if the completion finished for some other reason including encountering the EOS token.

`None` `lora_request` `LoRARequest | None`

The LoRA request that was used to generate the output.

`None`

Source code in `vllm/outputs.py`

```
@dataclass
classCompletionOutput:
"""The output data of one completion output of a request.

    Args:
        index: The index of the output in the request.
        text: The generated output text.
        token_ids: The token IDs of the generated output text.
        cumulative_logprob: The cumulative log probability of the generated
            output text.
        logprobs: The log probabilities of the top probability words at each
            position if the logprobs are requested.
        finish_reason: The reason why the sequence is finished.
        stop_reason: The stop string or token id that caused the completion
            to stop, None if the completion finished for some other reason
            including encountering the EOS token.
        lora_request: The LoRA request that was used to generate the output.
    """

    index: int
    text: str
    token_ids: GenericSequence[int]
    cumulative_logprob: float | None
    logprobs: SampleLogprobs | None
    routed_experts: np.ndarray | None = None  # [seq_len,layer_num,topk]
    finish_reason: str | None = None
    stop_reason: int | str | None = None
    lora_request: LoRARequest | None = None

    deffinished(self) -> bool:
        return self.finish_reason is not None

    def__repr__(self) -> str:
        return (
            f"CompletionOutput(index={self.index}, "
            f"text={self.text!r}, "
            f"token_ids={self.token_ids}, "
            f"routed_experts={self.routed_experts}, "
            f"cumulative_logprob={self.cumulative_logprob}, "
            f"logprobs={self.logprobs}, "
            f"finish_reason={self.finish_reason}, "
            f"stop_reason={self.stop_reason})"
        )
```

## EmbeddingOutput `dataclass` [¶](#vllm.EmbeddingOutput "Permanent link")

The output data of one embedding output of a request.

Parameters:

Name Type Description Default `embedding` `list[float]`

The embedding vector, which is a list of floats. Its length depends on the hidden dimension of the model.

*required*

Source code in `vllm/outputs.py`

```
@dataclass
classEmbeddingOutput:
"""The output data of one embedding output of a request.

    Args:
        embedding: The embedding vector, which is a list of floats.
            Its length depends on the hidden dimension of the model.
    """

    embedding: list[float]

    @staticmethod
    deffrom_base(pooling_output: PoolingOutput):
        pooled_data = pooling_output.data
        if pooled_data.ndim != 1:
            raise ValueError("pooled_data should be a 1-D embedding vector")

        return EmbeddingOutput(pooled_data.tolist())

    @property
    defhidden_size(self) -> int:
        return len(self.embedding)

    def__repr__(self) -> str:
        return f"EmbeddingOutput(hidden_size={self.hidden_size})"
```

## EngineArgs `dataclass` [¶](#vllm.EngineArgs "Permanent link")

Arguments for vLLM engine.

Source code in `vllm/engine/arg_utils.py`

```
@dataclass
classEngineArgs:
"""Arguments for vLLM engine."""

    model: str = ModelConfig.model
    enable_return_routed_experts: bool = ModelConfig.enable_return_routed_experts
    model_weights: str = ModelConfig.model_weights
    served_model_name: str | list[str] | None = ModelConfig.served_model_name
    tokenizer: str | None = ModelConfig.tokenizer
    hf_config_path: str | None = ModelConfig.hf_config_path
    runner: RunnerOption = ModelConfig.runner
    convert: ConvertOption = ModelConfig.convert
    skip_tokenizer_init: bool = ModelConfig.skip_tokenizer_init
    enable_prompt_embeds: bool = ModelConfig.enable_prompt_embeds
    tokenizer_mode: TokenizerMode | str = ModelConfig.tokenizer_mode
    trust_remote_code: bool = ModelConfig.trust_remote_code
    allowed_local_media_path: str = ModelConfig.allowed_local_media_path
    allowed_media_domains: list[str] | None = ModelConfig.allowed_media_domains
    download_dir: str | None = LoadConfig.download_dir
    safetensors_load_strategy: str | None = LoadConfig.safetensors_load_strategy
    load_format: str | LoadFormats = LoadConfig.load_format
    config_format: str = ModelConfig.config_format
    dtype: ModelDType = ModelConfig.dtype
    kv_cache_dtype: CacheDType = CacheConfig.cache_dtype
    seed: int = ModelConfig.seed
    max_model_len: int = ModelConfig.max_model_len
    cudagraph_capture_sizes: list[int] | None = (
        CompilationConfig.cudagraph_capture_sizes
    )
    max_cudagraph_capture_size: int | None = get_field(
        CompilationConfig, "max_cudagraph_capture_size"
    )
    ir_op_priority: IrOpPriorityConfig = get_field(KernelConfig, "ir_op_priority")
    # Note: Specifying a custom executor backend by passing a class
    # is intended for expert use only. The API may change without
    # notice.
    distributed_executor_backend: (
        str | DistributedExecutorBackend | type[Executor] | None
    ) = ParallelConfig.distributed_executor_backend
    # number of P/D disaggregation (or other disaggregation) workers
    pipeline_parallel_size: int = ParallelConfig.pipeline_parallel_size
    master_addr: str = ParallelConfig.master_addr
    master_port: int = ParallelConfig.master_port
    nnodes: int = ParallelConfig.nnodes
    node_rank: int = ParallelConfig.node_rank
    distributed_timeout_seconds: int | None = ParallelConfig.distributed_timeout_seconds
    numa_bind: bool = ParallelConfig.numa_bind
    numa_bind_nodes: list[int] | None = ParallelConfig.numa_bind_nodes
    numa_bind_cpus: list[str] | None = ParallelConfig.numa_bind_cpus
    tensor_parallel_size: int = ParallelConfig.tensor_parallel_size
    prefill_context_parallel_size: int = ParallelConfig.prefill_context_parallel_size
    decode_context_parallel_size: int = ParallelConfig.decode_context_parallel_size
    dcp_comm_backend: DCPCommBackend = ParallelConfig.dcp_comm_backend
    dcp_kv_cache_interleave_size: int = ParallelConfig.dcp_kv_cache_interleave_size
    cp_kv_cache_interleave_size: int = ParallelConfig.cp_kv_cache_interleave_size
    data_parallel_size: int = ParallelConfig.data_parallel_size
    data_parallel_rank: int | None = None
    data_parallel_start_rank: int | None = None
    data_parallel_size_local: int | None = None
    data_parallel_address: str | None = None
    data_parallel_rpc_port: int | None = None
    data_parallel_hybrid_lb: bool = False
    data_parallel_external_lb: bool = False
    data_parallel_backend: DataParallelBackend = ParallelConfig.data_parallel_backend
    enable_expert_parallel: bool = ParallelConfig.enable_expert_parallel
    enable_ep_weight_filter: bool = ParallelConfig.enable_ep_weight_filter
    moe_backend: MoEBackend = KernelConfig.moe_backend
    all2all_backend: All2AllBackend = ParallelConfig.all2all_backend
    enable_elastic_ep: bool = ParallelConfig.enable_elastic_ep
    enable_dbo: bool = ParallelConfig.enable_dbo
    ubatch_size: int = ParallelConfig.ubatch_size
    dbo_decode_token_threshold: int = ParallelConfig.dbo_decode_token_threshold
    dbo_prefill_token_threshold: int = ParallelConfig.dbo_prefill_token_threshold
    disable_nccl_for_dp_synchronization: bool | None = (
        ParallelConfig.disable_nccl_for_dp_synchronization
    )
    eplb_config: EPLBConfig = get_field(ParallelConfig, "eplb_config")
    enable_eplb: bool = ParallelConfig.enable_eplb
    expert_placement_strategy: ExpertPlacementStrategy = (
        ParallelConfig.expert_placement_strategy
    )
    _api_process_count: int = ParallelConfig._api_process_count
    _api_process_rank: int = ParallelConfig._api_process_rank
    max_parallel_loading_workers: int | None = (
        ParallelConfig.max_parallel_loading_workers
    )
    block_size: int | None = None
    enable_prefix_caching: bool | None = None
    prefix_caching_hash_algo: PrefixCachingHashAlgo = (
        CacheConfig.prefix_caching_hash_algo
    )
    disable_sliding_window: bool = ModelConfig.disable_sliding_window
    disable_cascade_attn: bool = ModelConfig.disable_cascade_attn
    offload_backend: str = OffloadConfig.offload_backend
    cpu_offload_gb: float = UVAOffloadConfig.cpu_offload_gb
    cpu_offload_params: set[str] = get_field(UVAOffloadConfig, "cpu_offload_params")
    offload_group_size: int = PrefetchOffloadConfig.offload_group_size
    offload_num_in_group: int = PrefetchOffloadConfig.offload_num_in_group
    offload_prefetch_step: int = PrefetchOffloadConfig.offload_prefetch_step
    offload_params: set[str] = get_field(PrefetchOffloadConfig, "offload_params")
    gpu_memory_utilization: float = CacheConfig.gpu_memory_utilization
    kv_cache_memory_bytes: int | None = CacheConfig.kv_cache_memory_bytes
    max_num_batched_tokens: int | None = None
    max_num_partial_prefills: int = SchedulerConfig.max_num_partial_prefills
    max_long_partial_prefills: int = SchedulerConfig.max_long_partial_prefills
    long_prefill_token_threshold: int = SchedulerConfig.long_prefill_token_threshold
    max_num_seqs: int | None = None
    max_logprobs: int = ModelConfig.max_logprobs
    logprobs_mode: LogprobsMode = ModelConfig.logprobs_mode
    disable_log_stats: bool = False
    aggregate_engine_logging: bool = False
    revision: str | None = ModelConfig.revision
    code_revision: str | None = ModelConfig.code_revision
    hf_token: bool | str | None = ModelConfig.hf_token
    hf_overrides: HfOverrides = get_field(ModelConfig, "hf_overrides")
    tokenizer_revision: str | None = ModelConfig.tokenizer_revision
    quantization: QuantizationMethods | str | None = ModelConfig.quantization
    quantization_config: "dict[str, Any] | OnlineQuantizationConfigArgs | None" = None
    allow_deprecated_quantization: bool = ModelConfig.allow_deprecated_quantization
    enforce_eager: bool = ModelConfig.enforce_eager
    disable_custom_all_reduce: bool = ParallelConfig.disable_custom_all_reduce
    language_model_only: bool = MultiModalConfig.language_model_only
    limit_mm_per_prompt: dict[str, int | dict[str, int]] = get_field(
        MultiModalConfig, "limit_per_prompt"
    )
    enable_mm_embeds: bool = MultiModalConfig.enable_mm_embeds
    interleave_mm_strings: bool = MultiModalConfig.interleave_mm_strings
    media_io_kwargs: dict[str, dict[str, Any]] = get_field(
        MultiModalConfig, "media_io_kwargs"
    )
    mm_processor_kwargs: dict[str, Any] | None = MultiModalConfig.mm_processor_kwargs
    mm_processor_cache_gb: float = MultiModalConfig.mm_processor_cache_gb
    mm_processor_cache_type: MMCacheType | None = (
        MultiModalConfig.mm_processor_cache_type
    )
    mm_shm_cache_max_object_size_mb: int = (
        MultiModalConfig.mm_shm_cache_max_object_size_mb
    )
    mm_encoder_only: bool = MultiModalConfig.mm_encoder_only
    mm_encoder_tp_mode: MMEncoderTPMode = MultiModalConfig.mm_encoder_tp_mode
    mm_encoder_attn_backend: AttentionBackendEnum | str | None = (
        MultiModalConfig.mm_encoder_attn_backend
    )
    mm_encoder_attn_dtype: str | None = MultiModalConfig.mm_encoder_attn_dtype
    mm_encoder_fp8_scale_path: str | None = MultiModalConfig.mm_encoder_fp8_scale_path
    mm_encoder_fp8_scale_save_path: str | None = (
        MultiModalConfig.mm_encoder_fp8_scale_save_path
    )
    mm_encoder_fp8_scale_save_margin: float = (
        MultiModalConfig.mm_encoder_fp8_scale_save_margin
    )
    io_processor_plugin: str | None = None
    renderer_num_workers: int = 1
    skip_mm_profiling: bool = MultiModalConfig.skip_mm_profiling
    video_pruning_rate: float | None = MultiModalConfig.video_pruning_rate
    mm_tensor_ipc: MMTensorIPC = MultiModalConfig.mm_tensor_ipc
    # LoRA fields
    enable_lora: bool = False
    max_loras: int = LoRAConfig.max_loras
    max_lora_rank: MaxLoRARanks = LoRAConfig.max_lora_rank
    default_mm_loras: dict[str, str] | None = LoRAConfig.default_mm_loras
    fully_sharded_loras: bool = LoRAConfig.fully_sharded_loras
    max_cpu_loras: int | None = LoRAConfig.max_cpu_loras
    lora_dtype: str | torch.dtype | None = LoRAConfig.lora_dtype
    lora_target_modules: list[str] | None = LoRAConfig.target_modules
    enable_tower_connector_lora: bool = LoRAConfig.enable_tower_connector_lora
    specialize_active_lora: bool = LoRAConfig.specialize_active_lora

    ray_workers_use_nsight: bool = ParallelConfig.ray_workers_use_nsight
    num_gpu_blocks_override: int | None = CacheConfig.num_gpu_blocks_override
    model_loader_extra_config: dict = get_field(LoadConfig, "model_loader_extra_config")
    ignore_patterns: str | list[str] = get_field(LoadConfig, "ignore_patterns")

    enable_chunked_prefill: bool | None = None
    disable_chunked_mm_input: bool = SchedulerConfig.disable_chunked_mm_input

    scheduler_reserve_full_isl: bool = SchedulerConfig.scheduler_reserve_full_isl

    disable_hybrid_kv_cache_manager: bool | None = (
        SchedulerConfig.disable_hybrid_kv_cache_manager
    )

    structured_outputs_config: StructuredOutputsConfig = get_field(
        VllmConfig, "structured_outputs_config"
    )
    reasoning_parser: str = StructuredOutputsConfig.reasoning_parser
    reasoning_parser_plugin: str | None = None

    speculative_config: dict[str, Any] | None = None

    show_hidden_metrics_for_version: str | None = (
        ObservabilityConfig.show_hidden_metrics_for_version
    )
    otlp_traces_endpoint: str | None = ObservabilityConfig.otlp_traces_endpoint
    collect_detailed_traces: list[DetailedTraceModules] | None = (
        ObservabilityConfig.collect_detailed_traces
    )
    kv_cache_metrics: bool = ObservabilityConfig.kv_cache_metrics
    kv_cache_metrics_sample: float = get_field(
        ObservabilityConfig, "kv_cache_metrics_sample"
    )
    cudagraph_metrics: bool = ObservabilityConfig.cudagraph_metrics
    enable_layerwise_nvtx_tracing: bool = (
        ObservabilityConfig.enable_layerwise_nvtx_tracing
    )
    enable_mfu_metrics: bool = ObservabilityConfig.enable_mfu_metrics
    enable_logging_iteration_details: bool = (
        ObservabilityConfig.enable_logging_iteration_details
    )
    enable_mm_processor_stats: bool = ObservabilityConfig.enable_mm_processor_stats
    scheduling_policy: SchedulerPolicy = SchedulerConfig.policy
    scheduler_cls: str | type[object] | None = SchedulerConfig.scheduler_cls

    pooler_config: PoolerConfig | None = ModelConfig.pooler_config
    compilation_config: CompilationConfig = get_field(VllmConfig, "compilation_config")
    attention_config: AttentionConfig = get_field(VllmConfig, "attention_config")
    mamba_config: MambaConfig = get_field(VllmConfig, "mamba_config")
    kernel_config: KernelConfig = get_field(VllmConfig, "kernel_config")
    enable_flashinfer_autotune: bool = get_field(
        KernelConfig, "enable_flashinfer_autotune"
    )
    worker_cls: str = ParallelConfig.worker_cls
    worker_extension_cls: str = ParallelConfig.worker_extension_cls

    profiler_config: ProfilerConfig = get_field(VllmConfig, "profiler_config")

    kv_transfer_config: KVTransferConfig | None = None
    kv_events_config: KVEventsConfig | None = None

    ec_transfer_config: ECTransferConfig | None = None
    reasoning_config: ReasoningConfig = get_field(VllmConfig, "reasoning_config")

    generation_config: str = ModelConfig.generation_config
    enable_sleep_mode: bool = ModelConfig.enable_sleep_mode
    override_generation_config: dict[str, Any] = get_field(
        ModelConfig, "override_generation_config"
    )
    model_impl: str = ModelConfig.model_impl
    override_attention_dtype: str | None = ModelConfig.override_attention_dtype
    attention_backend: AttentionBackendEnum | None = AttentionConfig.backend

    calculate_kv_scales: bool = CacheConfig.calculate_kv_scales
    kv_cache_dtype_skip_layers: list[str] = get_field(
        CacheConfig, "kv_cache_dtype_skip_layers"
    )
    mamba_cache_dtype: MambaDType = CacheConfig.mamba_cache_dtype
    mamba_ssm_cache_dtype: MambaDType = CacheConfig.mamba_ssm_cache_dtype
    mamba_block_size: int | None = get_field(CacheConfig, "mamba_block_size")
    mamba_cache_mode: MambaCacheMode = CacheConfig.mamba_cache_mode

    mamba_backend: MambaBackendEnum = MambaBackendEnum.TRITON
    enable_mamba_cache_stochastic_rounding: bool = (
        MambaConfig.enable_stochastic_rounding
    )
    mamba_cache_philox_rounds: int = MambaConfig.stochastic_rounding_philox_rounds

    additional_config: dict[str, Any] = get_field(VllmConfig, "additional_config")

    use_tqdm_on_load: bool = LoadConfig.use_tqdm_on_load
    pt_load_map_location: str | dict[str, str] = LoadConfig.pt_load_map_location

    logits_processors: list[str | type[LogitsProcessor]] | None = (
        ModelConfig.logits_processors
    )
"""Custom logitproc types"""

    async_scheduling: bool | None = SchedulerConfig.async_scheduling

    stream_interval: int = SchedulerConfig.stream_interval

    kv_sharing_fast_prefill: bool = CacheConfig.kv_sharing_fast_prefill
    optimization_level: OptimizationLevel = VllmConfig.optimization_level
    performance_mode: PerformanceMode = VllmConfig.performance_mode

    kv_offloading_size: float | None = CacheConfig.kv_offloading_size
    kv_offloading_backend: KVOffloadingBackend = CacheConfig.kv_offloading_backend
    tokens_only: bool = False

    shutdown_timeout: int = 0

    weight_transfer_config: WeightTransferConfig | None = get_field(
        VllmConfig,
        "weight_transfer_config",
    )

    fail_on_environ_validation: bool = False
    gdn_prefill_backend: Literal["flashinfer", "triton"] | None = None

    def__post_init__(self):
        # support `EngineArgs(compilation_config={...})`
        # without having to manually construct a
        # CompilationConfig object
        if isinstance(self.compilation_config, dict):
            self.compilation_config = CompilationConfig(**self.compilation_config)
        if isinstance(self.attention_config, dict):
            self.attention_config = AttentionConfig(**self.attention_config)
        if isinstance(self.mamba_config, dict):
            self.mamba_config = MambaConfig(**self.mamba_config)
        if isinstance(self.kernel_config, dict):
            self.kernel_config = KernelConfig(**self.kernel_config)
        if isinstance(self.eplb_config, dict):
            self.eplb_config = EPLBConfig(**self.eplb_config)
        if isinstance(self.weight_transfer_config, dict):
            self.weight_transfer_config = WeightTransferConfig(
                **self.weight_transfer_config
            )
        if isinstance(self.ir_op_priority, dict):
            self.ir_op_priority = IrOpPriorityConfig(**self.ir_op_priority)

        fromvllm.config.quantizationimport resolve_online_quant_config

        self.quantization_config = resolve_online_quant_config(
            self.quantization, self.quantization_config
        )

        # Setup plugins
        fromvllm.pluginsimport load_general_plugins

        load_general_plugins()
        # when use hf offline,replace model and tokenizer id to local model path
        if huggingface_hub.constants.HF_HUB_OFFLINE:
            model_id = self.model
            self.model = get_model_path(self.model, self.revision)
            if model_id is not self.model:
                logger.info(
                    "HF_HUB_OFFLINE is True, replace model_id [%s] to model_path [%s]",
                    model_id,
                    self.model,
                )
            if self.tokenizer is not None:
                tokenizer_id = self.tokenizer
                self.tokenizer = get_model_path(self.tokenizer, self.tokenizer_revision)
                if tokenizer_id is not self.tokenizer:
                    logger.info(
                        "HF_HUB_OFFLINE is True, replace tokenizer_id [%s] "
                        "to tokenizer_path [%s]",
                        tokenizer_id,
                        self.tokenizer,
                    )

    @staticmethod
    defadd_cli_args(parser: FlexibleArgumentParser) -> FlexibleArgumentParser:
"""Shared CLI arguments for vLLM engine."""

        # Model arguments
        model_kwargs = get_kwargs(ModelConfig)
        model_group = parser.add_argument_group(
            title="ModelConfig",
            description=ModelConfig.__doc__,
        )
        if not ("serve" in sys.argv[1:] and "--help" in sys.argv[1:]):
            model_group.add_argument("--model", **model_kwargs["model"])
        model_group.add_argument("--runner", **model_kwargs["runner"])
        model_group.add_argument("--convert", **model_kwargs["convert"])
        model_group.add_argument("--tokenizer", **model_kwargs["tokenizer"])
        model_group.add_argument("--tokenizer-mode", **model_kwargs["tokenizer_mode"])
        model_group.add_argument(
            "--trust-remote-code", **model_kwargs["trust_remote_code"]
        )
        model_group.add_argument("--dtype", **model_kwargs["dtype"])
        model_group.add_argument("--seed", **model_kwargs["seed"])
        model_group.add_argument("--hf-config-path", **model_kwargs["hf_config_path"])
        model_group.add_argument(
            "--allowed-local-media-path", **model_kwargs["allowed_local_media_path"]
        )
        model_group.add_argument(
            "--allowed-media-domains", **model_kwargs["allowed_media_domains"]
        )
        model_group.add_argument("--revision", **model_kwargs["revision"])
        model_group.add_argument("--code-revision", **model_kwargs["code_revision"])
        model_group.add_argument(
            "--tokenizer-revision", **model_kwargs["tokenizer_revision"]
        )
        model_group.add_argument("--max-model-len", **model_kwargs["max_model_len"])
        model_group.add_argument("--quantization", "-q", **model_kwargs["quantization"])
        model_group.add_argument(
            "--allow-deprecated-quantization",
            **model_kwargs["allow_deprecated_quantization"],
        )
        model_group.add_argument("--enforce-eager", **model_kwargs["enforce_eager"])
        model_group.add_argument(
            "--enable-return-routed-experts",
            **model_kwargs["enable_return_routed_experts"],
        )
        model_group.add_argument("--max-logprobs", **model_kwargs["max_logprobs"])
        model_group.add_argument("--logprobs-mode", **model_kwargs["logprobs_mode"])
        model_group.add_argument(
            "--disable-sliding-window", **model_kwargs["disable_sliding_window"]
        )
        model_group.add_argument(
            "--disable-cascade-attn", **model_kwargs["disable_cascade_attn"]
        )
        model_group.add_argument(
            "--skip-tokenizer-init", **model_kwargs["skip_tokenizer_init"]
        )
        model_group.add_argument(
            "--enable-prompt-embeds", **model_kwargs["enable_prompt_embeds"]
        )
        model_group.add_argument(
            "--served-model-name", **model_kwargs["served_model_name"]
        )
        model_group.add_argument("--config-format", **model_kwargs["config_format"])
        # This one is a special case because it can bool
        # or str. TODO: Handle this in get_kwargs
        model_group.add_argument(
            "--hf-token",
            type=str,
            nargs="?",
            const=True,
            default=model_kwargs["hf_token"]["default"],
            help=model_kwargs["hf_token"]["help"],
        )
        model_group.add_argument("--hf-overrides", **model_kwargs["hf_overrides"])
        model_group.add_argument("--pooler-config", **model_kwargs["pooler_config"])
        model_group.add_argument(
            "--generation-config", **model_kwargs["generation_config"]
        )
        model_group.add_argument(
            "--override-generation-config", **model_kwargs["override_generation_config"]
        )
        model_group.add_argument(
            "--enable-sleep-mode", **model_kwargs["enable_sleep_mode"]
        )
        model_group.add_argument("--model-impl", **model_kwargs["model_impl"])
        model_group.add_argument(
            "--override-attention-dtype", **model_kwargs["override_attention_dtype"]
        )
        model_group.add_argument(
            "--logits-processors", **model_kwargs["logits_processors"]
        )
        model_group.add_argument(
            "--io-processor-plugin", **model_kwargs["io_processor_plugin"]
        )
        model_group.add_argument(
            "--renderer-num-workers",
            **model_kwargs["renderer_num_workers"],
        )

        # Model loading arguments
        load_kwargs = get_kwargs(LoadConfig)
        load_group = parser.add_argument_group(
            title="LoadConfig",
            description=LoadConfig.__doc__,
        )
        load_group.add_argument("--load-format", **load_kwargs["load_format"])
        load_group.add_argument("--download-dir", **load_kwargs["download_dir"])
        load_group.add_argument(
            "--safetensors-load-strategy", **load_kwargs["safetensors_load_strategy"]
        )
        load_group.add_argument(
            "--model-loader-extra-config", **load_kwargs["model_loader_extra_config"]
        )
        load_group.add_argument("--ignore-patterns", **load_kwargs["ignore_patterns"])
        load_group.add_argument("--use-tqdm-on-load", **load_kwargs["use_tqdm_on_load"])
        load_group.add_argument(
            "--pt-load-map-location", **load_kwargs["pt_load_map_location"]
        )

        # Attention arguments
        attention_kwargs = get_kwargs(AttentionConfig)
        attention_group = parser.add_argument_group(
            title="AttentionConfig",
            description=AttentionConfig.__doc__,
        )
        attention_group.add_argument(
            "--attention-backend", **attention_kwargs["backend"]
        )

        # Mamba arguments
        mamba_kwargs = get_kwargs(MambaConfig)
        mamba_group = parser.add_argument_group(
            title="MambaConfig",
            description=MambaConfig.__doc__,
        )
        mamba_group.add_argument("--mamba-backend", **mamba_kwargs["backend"])
        mamba_group.add_argument(
            "--enable-mamba-cache-stochastic-rounding",
            **mamba_kwargs["enable_stochastic_rounding"],
        )
        mamba_group.add_argument(
            "--mamba-cache-philox-rounds",
            **mamba_kwargs["stochastic_rounding_philox_rounds"],
        )

        # Structured outputs arguments
        structured_outputs_kwargs = get_kwargs(StructuredOutputsConfig)
        structured_outputs_group = parser.add_argument_group(
            title="StructuredOutputsConfig",
            description=StructuredOutputsConfig.__doc__,
        )
        structured_outputs_group.add_argument(
            "--reasoning-parser",
            # Choices need to be validated after parsing to include plugins
            **structured_outputs_kwargs["reasoning_parser"],
        )
        structured_outputs_group.add_argument(
            "--reasoning-parser-plugin",
            **structured_outputs_kwargs["reasoning_parser_plugin"],
        )

        # Parallel arguments
        parallel_kwargs = get_kwargs(ParallelConfig)
        parallel_group = parser.add_argument_group(
            title="ParallelConfig",
            description=ParallelConfig.__doc__,
        )
        parallel_group.add_argument(
            "--distributed-executor-backend",
            **parallel_kwargs["distributed_executor_backend"],
        )
        parallel_group.add_argument(
            "--pipeline-parallel-size",
            "-pp",
            **parallel_kwargs["pipeline_parallel_size"],
        )
        parallel_group.add_argument("--master-addr", **parallel_kwargs["master_addr"])
        parallel_group.add_argument("--master-port", **parallel_kwargs["master_port"])
        parallel_group.add_argument("--nnodes", "-n", **parallel_kwargs["nnodes"])
        parallel_group.add_argument("--node-rank", "-r", **parallel_kwargs["node_rank"])
        parallel_group.add_argument(
            "--distributed-timeout-seconds",
            **parallel_kwargs["distributed_timeout_seconds"],
        )
        parallel_group.add_argument("--numa-bind", **parallel_kwargs["numa_bind"])
        parallel_group.add_argument(
            "--numa-bind-nodes", **parallel_kwargs["numa_bind_nodes"]
        )
        parallel_group.add_argument(
            "--numa-bind-cpus", **parallel_kwargs["numa_bind_cpus"]
        )
        parallel_group.add_argument(
            "--tensor-parallel-size", "-tp", **parallel_kwargs["tensor_parallel_size"]
        )
        parallel_group.add_argument(
            "--decode-context-parallel-size",
            "-dcp",
            **parallel_kwargs["decode_context_parallel_size"],
        )
        parallel_group.add_argument(
            "--dcp-comm-backend",
            **parallel_kwargs["dcp_comm_backend"],
        )
        parallel_group.add_argument(
            "--dcp-kv-cache-interleave-size",
            **parallel_kwargs["dcp_kv_cache_interleave_size"],
        )
        parallel_group.add_argument(
            "--cp-kv-cache-interleave-size",
            **parallel_kwargs["cp_kv_cache_interleave_size"],
        )
        parallel_group.add_argument(
            "--prefill-context-parallel-size",
            "-pcp",
            **parallel_kwargs["prefill_context_parallel_size"],
        )
        parallel_group.add_argument(
            "--data-parallel-size", "-dp", **parallel_kwargs["data_parallel_size"]
        )
        parallel_group.add_argument(
            "--data-parallel-rank",
            "-dpn",
            type=int,
            help="Data parallel rank of this instance. "
            "When set, enables external load balancer mode for MoE "
            "data-parallel deployments. Unsupported for non-MoE models; "
            "launch independent vLLM instances instead.",
        )
        parallel_group.add_argument(
            "--data-parallel-start-rank",
            "-dpr",
            type=int,
            help="Starting data parallel rank for secondary nodes.",
        )
        parallel_group.add_argument(
            "--data-parallel-size-local",
            "-dpl",
            type=int,
            help="Number of data parallel replicas to run on this node.",
        )
        parallel_group.add_argument(
            "--data-parallel-address",
            "-dpa",
            type=str,
            help="Address of data parallel cluster head-node.",
        )
        parallel_group.add_argument(
            "--data-parallel-rpc-port",
            "-dpp",
            type=int,
            help="Port for data parallel RPC communication.",
        )
        parallel_group.add_argument(
            "--data-parallel-backend",
            "-dpb",
            type=str,
            default="mp",
            help='Backend for data parallel, either "mp" or "ray".',
        )
        parallel_group.add_argument(
            "--data-parallel-hybrid-lb",
            "-dph",
            **parallel_kwargs["data_parallel_hybrid_lb"],
        )
        parallel_group.add_argument(
            "--data-parallel-external-lb",
            "-dpe",
            **parallel_kwargs["data_parallel_external_lb"],
        )
        parallel_group.add_argument(
            "--enable-expert-parallel",
            "-ep",
            **parallel_kwargs["enable_expert_parallel"],
        )
        parallel_group.add_argument(
            "--enable-ep-weight-filter",
            **parallel_kwargs["enable_ep_weight_filter"],
        )
        parallel_group.add_argument(
            "--all2all-backend", **parallel_kwargs["all2all_backend"]
        )
        parallel_group.add_argument("--enable-dbo", **parallel_kwargs["enable_dbo"])
        parallel_group.add_argument(
            "--ubatch-size",
            **parallel_kwargs["ubatch_size"],
        )
        parallel_group.add_argument(
            "--enable-elastic-ep", **parallel_kwargs["enable_elastic_ep"]
        )
        parallel_group.add_argument(
            "--dbo-decode-token-threshold",
            **parallel_kwargs["dbo_decode_token_threshold"],
        )
        parallel_group.add_argument(
            "--dbo-prefill-token-threshold",
            **parallel_kwargs["dbo_prefill_token_threshold"],
        )
        parallel_group.add_argument(
            "--disable-nccl-for-dp-synchronization",
            **parallel_kwargs["disable_nccl_for_dp_synchronization"],
        )
        parallel_group.add_argument("--enable-eplb", **parallel_kwargs["enable_eplb"])
        parallel_group.add_argument("--eplb-config", **parallel_kwargs["eplb_config"])
        parallel_group.add_argument(
            "--expert-placement-strategy",
            **parallel_kwargs["expert_placement_strategy"],
        )

        parallel_group.add_argument(
            "--max-parallel-loading-workers",
            **parallel_kwargs["max_parallel_loading_workers"],
        )
        parallel_group.add_argument(
            "--ray-workers-use-nsight", **parallel_kwargs["ray_workers_use_nsight"]
        )
        parallel_group.add_argument(
            "--disable-custom-all-reduce",
            **parallel_kwargs["disable_custom_all_reduce"],
        )
        parallel_group.add_argument("--worker-cls", **parallel_kwargs["worker_cls"])
        parallel_group.add_argument(
            "--worker-extension-cls", **parallel_kwargs["worker_extension_cls"]
        )

        # KV cache arguments
        cache_kwargs = get_kwargs(CacheConfig)
        cache_group = parser.add_argument_group(
            title="CacheConfig",
            description=CacheConfig.__doc__,
        )
        cache_group.add_argument("--block-size", **cache_kwargs["block_size"])
        cache_group.add_argument(
            "--gpu-memory-utilization", **cache_kwargs["gpu_memory_utilization"]
        )
        cache_group.add_argument(
            "--kv-cache-memory-bytes", **cache_kwargs["kv_cache_memory_bytes"]
        )
        cache_group.add_argument("--kv-cache-dtype", **cache_kwargs["cache_dtype"])
        cache_group.add_argument(
            "--num-gpu-blocks-override", **cache_kwargs["num_gpu_blocks_override"]
        )
        cache_group.add_argument(
            "--enable-prefix-caching",
            **{
                **cache_kwargs["enable_prefix_caching"],
                "default": None,
            },
        )
        cache_group.add_argument(
            "--prefix-caching-hash-algo", **cache_kwargs["prefix_caching_hash_algo"]
        )
        cache_group.add_argument(
            "--calculate-kv-scales", **cache_kwargs["calculate_kv_scales"]
        )
        cache_group.add_argument(
            "--kv-cache-dtype-skip-layers", **cache_kwargs["kv_cache_dtype_skip_layers"]
        )
        cache_group.add_argument(
            "--kv-sharing-fast-prefill", **cache_kwargs["kv_sharing_fast_prefill"]
        )
        cache_group.add_argument(
            "--mamba-cache-dtype", **cache_kwargs["mamba_cache_dtype"]
        )
        cache_group.add_argument(
            "--mamba-ssm-cache-dtype", **cache_kwargs["mamba_ssm_cache_dtype"]
        )
        cache_group.add_argument(
            "--mamba-block-size", **cache_kwargs["mamba_block_size"]
        )
        cache_group.add_argument(
            "--mamba-cache-mode", **cache_kwargs["mamba_cache_mode"]
        )
        cache_group.add_argument(
            "--kv-offloading-size", **cache_kwargs["kv_offloading_size"]
        )
        cache_group.add_argument(
            "--kv-offloading-backend", **cache_kwargs["kv_offloading_backend"]
        )

        # Model weight offload related configs
        offload_kwargs = get_kwargs(OffloadConfig)
        uva_kwargs = get_kwargs(UVAOffloadConfig)
        prefetch_kwargs = get_kwargs(PrefetchOffloadConfig)
        offload_group = parser.add_argument_group(
            title="OffloadConfig",
            description=OffloadConfig.__doc__,
        )
        offload_group.add_argument(
            "--offload-backend", **offload_kwargs["offload_backend"]
        )
        offload_group.add_argument("--cpu-offload-gb", **uva_kwargs["cpu_offload_gb"])
        offload_group.add_argument(
            "--cpu-offload-params", **uva_kwargs["cpu_offload_params"]
        )
        offload_group.add_argument(
            "--offload-group-size",
            **prefetch_kwargs["offload_group_size"],
        )
        offload_group.add_argument(
            "--offload-num-in-group",
            **prefetch_kwargs["offload_num_in_group"],
        )
        offload_group.add_argument(
            "--offload-prefetch-step",
            **prefetch_kwargs["offload_prefetch_step"],
        )
        offload_group.add_argument(
            "--offload-params", **prefetch_kwargs["offload_params"]
        )

        # Multimodal related configs
        multimodal_kwargs = get_kwargs(MultiModalConfig)
        multimodal_group = parser.add_argument_group(
            title="MultiModalConfig",
            description=MultiModalConfig.__doc__,
        )
        multimodal_group.add_argument(
            "--language-model-only", **multimodal_kwargs["language_model_only"]
        )
        multimodal_group.add_argument(
            "--limit-mm-per-prompt", **multimodal_kwargs["limit_per_prompt"]
        )
        multimodal_group.add_argument(
            "--enable-mm-embeds", **multimodal_kwargs["enable_mm_embeds"]
        )
        multimodal_group.add_argument(
            "--media-io-kwargs", **multimodal_kwargs["media_io_kwargs"]
        )
        multimodal_group.add_argument(
            "--mm-processor-kwargs", **multimodal_kwargs["mm_processor_kwargs"]
        )
        multimodal_group.add_argument(
            "--mm-processor-cache-gb", **multimodal_kwargs["mm_processor_cache_gb"]
        )
        multimodal_group.add_argument(
            "--mm-processor-cache-type", **multimodal_kwargs["mm_processor_cache_type"]
        )
        multimodal_group.add_argument(
            "--mm-shm-cache-max-object-size-mb",
            **multimodal_kwargs["mm_shm_cache_max_object_size_mb"],
        )
        multimodal_group.add_argument(
            "--mm-encoder-only", **multimodal_kwargs["mm_encoder_only"]
        )
        multimodal_group.add_argument(
            "--mm-encoder-tp-mode", **multimodal_kwargs["mm_encoder_tp_mode"]
        )
        multimodal_group.add_argument(
            "--mm-encoder-attn-backend",
            **multimodal_kwargs["mm_encoder_attn_backend"],
        )
        multimodal_group.add_argument(
            "--mm-encoder-attn-dtype",
            **multimodal_kwargs["mm_encoder_attn_dtype"],
        )
        multimodal_group.add_argument(
            "--mm-encoder-fp8-scale-path",
            **multimodal_kwargs["mm_encoder_fp8_scale_path"],
        )
        multimodal_group.add_argument(
            "--mm-encoder-fp8-scale-save-path",
            **multimodal_kwargs["mm_encoder_fp8_scale_save_path"],
        )
        multimodal_group.add_argument(
            "--mm-encoder-fp8-scale-save-margin",
            **multimodal_kwargs["mm_encoder_fp8_scale_save_margin"],
        )
        multimodal_group.add_argument(
            "--interleave-mm-strings", **multimodal_kwargs["interleave_mm_strings"]
        )
        multimodal_group.add_argument(
            "--skip-mm-profiling", **multimodal_kwargs["skip_mm_profiling"]
        )

        multimodal_group.add_argument(
            "--video-pruning-rate", **multimodal_kwargs["video_pruning_rate"]
        )
        multimodal_group.add_argument(
            "--mm-tensor-ipc", **multimodal_kwargs["mm_tensor_ipc"]
        )

        # LoRA related configs
        lora_kwargs = get_kwargs(LoRAConfig)
        lora_group = parser.add_argument_group(
            title="LoRAConfig",
            description=LoRAConfig.__doc__,
        )
        lora_group.add_argument(
            "--enable-lora",
            action=argparse.BooleanOptionalAction,
            help="If True, enable handling of LoRA adapters.",
        )
        lora_group.add_argument("--max-loras", **lora_kwargs["max_loras"])
        lora_group.add_argument("--max-lora-rank", **lora_kwargs["max_lora_rank"])
        lora_group.add_argument(
            "--lora-dtype",
            **lora_kwargs["lora_dtype"],
        )
        lora_group.add_argument(
            "--enable-tower-connector-lora",
            **lora_kwargs["enable_tower_connector_lora"],
        )
        lora_group.add_argument("--max-cpu-loras", **lora_kwargs["max_cpu_loras"])
        lora_group.add_argument(
            "--fully-sharded-loras", **lora_kwargs["fully_sharded_loras"]
        )
        lora_group.add_argument(
            "--lora-target-modules", **lora_kwargs["target_modules"]
        )
        lora_group.add_argument("--default-mm-loras", **lora_kwargs["default_mm_loras"])
        lora_group.add_argument(
            "--specialize-active-lora", **lora_kwargs["specialize_active_lora"]
        )

        # Observability arguments
        observability_kwargs = get_kwargs(ObservabilityConfig)
        observability_group = parser.add_argument_group(
            title="ObservabilityConfig",
            description=ObservabilityConfig.__doc__,
        )
        observability_group.add_argument(
            "--show-hidden-metrics-for-version",
            **observability_kwargs["show_hidden_metrics_for_version"],
        )
        observability_group.add_argument(
            "--otlp-traces-endpoint", **observability_kwargs["otlp_traces_endpoint"]
        )
        # TODO: generalise this special case
        choices = observability_kwargs["collect_detailed_traces"]["choices"]
        metavar = f"{{{','.join(choices)}}}"
        observability_kwargs["collect_detailed_traces"]["metavar"] = metavar
        observability_kwargs["collect_detailed_traces"]["choices"] += [
            ",".join(p) for p in permutations(get_args(DetailedTraceModules), r=2)
        ]
        observability_group.add_argument(
            "--collect-detailed-traces",
            **observability_kwargs["collect_detailed_traces"],
        )
        observability_group.add_argument(
            "--kv-cache-metrics", **observability_kwargs["kv_cache_metrics"]
        )
        observability_group.add_argument(
            "--kv-cache-metrics-sample",
            **observability_kwargs["kv_cache_metrics_sample"],
        )
        observability_group.add_argument(
            "--cudagraph-metrics",
            **observability_kwargs["cudagraph_metrics"],
        )
        observability_group.add_argument(
            "--enable-layerwise-nvtx-tracing",
            **observability_kwargs["enable_layerwise_nvtx_tracing"],
        )
        observability_group.add_argument(
            "--enable-mfu-metrics",
            **observability_kwargs["enable_mfu_metrics"],
        )
        observability_group.add_argument(
            "--enable-logging-iteration-details",
            **observability_kwargs["enable_logging_iteration_details"],
        )

        # Scheduler arguments
        scheduler_kwargs = get_kwargs(SchedulerConfig)
        scheduler_group = parser.add_argument_group(
            title="SchedulerConfig",
            description=SchedulerConfig.__doc__,
        )
        scheduler_group.add_argument(
            "--max-num-batched-tokens",
            **{
                **scheduler_kwargs["max_num_batched_tokens"],
                "default": None,
            },
        )
        scheduler_group.add_argument(
            "--max-num-seqs",
            **{
                **scheduler_kwargs["max_num_seqs"],
                "default": None,
            },
        )
        scheduler_group.add_argument(
            "--max-num-partial-prefills", **scheduler_kwargs["max_num_partial_prefills"]
        )
        scheduler_group.add_argument(
            "--max-long-partial-prefills",
            **scheduler_kwargs["max_long_partial_prefills"],
        )
        scheduler_group.add_argument(
            "--long-prefill-token-threshold",
            **scheduler_kwargs["long_prefill_token_threshold"],
        )
        # multi-step scheduling has been removed; corresponding arguments
        # are no longer supported.
        scheduler_group.add_argument(
            "--scheduling-policy", **scheduler_kwargs["policy"]
        )
        scheduler_group.add_argument(
            "--enable-chunked-prefill",
            **{
                **scheduler_kwargs["enable_chunked_prefill"],
                "default": None,
            },
        )
        scheduler_group.add_argument(
            "--disable-chunked-mm-input", **scheduler_kwargs["disable_chunked_mm_input"]
        )
        scheduler_group.add_argument(
            "--scheduler-cls", **scheduler_kwargs["scheduler_cls"]
        )
        scheduler_group.add_argument(
            "--scheduler-reserve-full-isl",
            **scheduler_kwargs["scheduler_reserve_full_isl"],
        )
        scheduler_group.add_argument(
            "--disable-hybrid-kv-cache-manager",
            **scheduler_kwargs["disable_hybrid_kv_cache_manager"],
        )
        scheduler_group.add_argument(
            "--async-scheduling", **scheduler_kwargs["async_scheduling"]
        )
        scheduler_group.add_argument(
            "--stream-interval", **scheduler_kwargs["stream_interval"]
        )

        # Compilation arguments
        compilation_kwargs = get_kwargs(CompilationConfig)
        compilation_group = parser.add_argument_group(
            title="CompilationConfig",
            description=CompilationConfig.__doc__,
        )
        compilation_group.add_argument(
            "--cudagraph-capture-sizes", **compilation_kwargs["cudagraph_capture_sizes"]
        )
        compilation_group.add_argument(
            "--max-cudagraph-capture-size",
            **compilation_kwargs["max_cudagraph_capture_size"],
        )

        # Kernel arguments
        kernel_kwargs = get_kwargs(KernelConfig)
        kernel_group = parser.add_argument_group(
            title="KernelConfig",
            description=KernelConfig.__doc__,
        )
        kernel_group.add_argument("--ir-op-priority", **kernel_kwargs["ir_op_priority"])
        kernel_group.add_argument(
            "--enable-flashinfer-autotune",
            **kernel_kwargs["enable_flashinfer_autotune"],
        )
        moe_backend_kwargs = kernel_kwargs["moe_backend"]
        moe_backend_kwargs["type"] = lambda s: s.lower().replace("-", "_")
        kernel_group.add_argument("--moe-backend", **moe_backend_kwargs)

        # vLLM arguments
        vllm_kwargs = get_kwargs(VllmConfig)
        vllm_group = parser.add_argument_group(
            title="VllmConfig",
            description=VllmConfig.__doc__,
        )
        # We construct SpeculativeConfig using fields from other configs in
        # create_engine_config. So we set the type to a JSON string here to
        # delay the Pydantic validation that comes with SpeculativeConfig.
        vllm_kwargs["speculative_config"]["type"] = optional_type(json.loads)
        vllm_group.add_argument(
            "--speculative-config", "-sc", **vllm_kwargs["speculative_config"]
        )
        vllm_group.add_argument(
            "--kv-transfer-config", **vllm_kwargs["kv_transfer_config"]
        )
        vllm_group.add_argument("--kv-events-config", **vllm_kwargs["kv_events_config"])
        vllm_group.add_argument(
            "--ec-transfer-config", **vllm_kwargs["ec_transfer_config"]
        )
        vllm_group.add_argument(
            "--compilation-config", "-cc", **vllm_kwargs["compilation_config"]
        )
        vllm_group.add_argument(
            "--attention-config", "-ac", **vllm_kwargs["attention_config"]
        )
        vllm_group.add_argument("--reasoning-config", **vllm_kwargs["reasoning_config"])
        vllm_group.add_argument("--kernel-config", **vllm_kwargs["kernel_config"])
        vllm_group.add_argument(
            "--additional-config", **vllm_kwargs["additional_config"]
        )
        vllm_group.add_argument(
            "--structured-outputs-config", **vllm_kwargs["structured_outputs_config"]
        )
        vllm_group.add_argument("--profiler-config", **vllm_kwargs["profiler_config"])
        vllm_group.add_argument(
            "--optimization-level", **vllm_kwargs["optimization_level"]
        )
        vllm_group.add_argument("--performance-mode", **vllm_kwargs["performance_mode"])
        vllm_group.add_argument(
            "--weight-transfer-config", **vllm_kwargs["weight_transfer_config"]
        )

        # Other arguments
        parser.add_argument(
            "--disable-log-stats",
            action="store_true",
            help="Disable logging statistics.",
        )

        parser.add_argument(
            "--aggregate-engine-logging",
            action="store_true",
            help="Log aggregate rather than per-engine statistics "
            "when using data parallelism.",
        )

        parser.add_argument(
            "--fail-on-environ-validation",
            help="If set, the engine will raise an error if "
            "environment validation fails.",
            default=False,
            action=argparse.BooleanOptionalAction,
        )

        parser.add_argument(
            "--shutdown-timeout",
            type=int,
            default=0,
            help="Shutdown timeout in seconds. 0 = abort, >0 = wait.",
        )

        parser.add_argument(
            "--gdn-prefill-backend",
            dest="gdn_prefill_backend",
            choices=["flashinfer", "triton"],
            default=None,
            help="Select GDN prefill backend.",
        )
        return parser

    @classmethod
    deffrom_cli_args(cls, args: argparse.Namespace):
        # Get the list of attributes of this dataclass.
        attrs = [attr.name for attr in dataclasses.fields(cls)]
        # Set the attributes from the parsed arguments.
        engine_args = cls(
            **{attr: getattr(args, attr) for attr in attrs if hasattr(args, attr)}
        )
        return engine_args

    defcreate_model_config(self) -> ModelConfig:
        # gguf file needs a specific model loader
        if is_gguf(self.model):
            self.quantization = self.load_format = "gguf"

        if not envs.VLLM_ENABLE_V1_MULTIPROCESSING:
            logger.warning(
                "The global random seed is set to %d. Since "
                "VLLM_ENABLE_V1_MULTIPROCESSING is set to False, this may "
                "affect the random state of the Python process that "
                "launched vLLM.",
                self.seed,
            )

        return ModelConfig(
            model=self.model,
            model_weights=self.model_weights,
            hf_config_path=self.hf_config_path,
            runner=self.runner,
            convert=self.convert,
            tokenizer=self.tokenizer,  # type: ignore[arg-type]
            tokenizer_mode=self.tokenizer_mode,
            trust_remote_code=self.trust_remote_code,
            allowed_local_media_path=self.allowed_local_media_path,
            allowed_media_domains=self.allowed_media_domains,
            dtype=self.dtype,
            seed=self.seed,
            revision=self.revision,
            code_revision=self.code_revision,
            hf_token=self.hf_token,
            hf_overrides=self.hf_overrides,
            tokenizer_revision=self.tokenizer_revision,
            max_model_len=self.max_model_len,
            quantization=self.quantization,
            quantization_config=self.quantization_config,
            allow_deprecated_quantization=self.allow_deprecated_quantization,
            enforce_eager=self.enforce_eager,
            enable_return_routed_experts=self.enable_return_routed_experts,
            max_logprobs=self.max_logprobs,
            logprobs_mode=self.logprobs_mode,
            disable_sliding_window=self.disable_sliding_window,
            disable_cascade_attn=self.disable_cascade_attn,
            skip_tokenizer_init=self.skip_tokenizer_init,
            enable_prompt_embeds=self.enable_prompt_embeds,
            served_model_name=self.served_model_name,
            language_model_only=self.language_model_only,
            limit_mm_per_prompt=self.limit_mm_per_prompt,
            enable_mm_embeds=self.enable_mm_embeds,
            interleave_mm_strings=self.interleave_mm_strings,
            media_io_kwargs=self.media_io_kwargs,
            skip_mm_profiling=self.skip_mm_profiling,
            config_format=self.config_format,
            mm_processor_kwargs=self.mm_processor_kwargs,
            mm_processor_cache_gb=self.mm_processor_cache_gb,
            mm_processor_cache_type=self.mm_processor_cache_type,
            mm_shm_cache_max_object_size_mb=self.mm_shm_cache_max_object_size_mb,
            mm_encoder_only=self.mm_encoder_only,
            mm_encoder_tp_mode=self.mm_encoder_tp_mode,
            mm_encoder_attn_backend=self.mm_encoder_attn_backend,
            mm_encoder_attn_dtype=self.mm_encoder_attn_dtype,
            mm_encoder_fp8_scale_path=self.mm_encoder_fp8_scale_path,
            mm_encoder_fp8_scale_save_path=self.mm_encoder_fp8_scale_save_path,
            mm_encoder_fp8_scale_save_margin=self.mm_encoder_fp8_scale_save_margin,
            pooler_config=self.pooler_config,
            generation_config=self.generation_config,
            override_generation_config=self.override_generation_config,
            enable_sleep_mode=self.enable_sleep_mode,
            model_impl=self.model_impl,
            override_attention_dtype=self.override_attention_dtype,
            logits_processors=self.logits_processors,
            video_pruning_rate=self.video_pruning_rate,
            mm_tensor_ipc=self.mm_tensor_ipc,
            io_processor_plugin=self.io_processor_plugin,
            renderer_num_workers=self.renderer_num_workers,
        )

    defvalidate_tensorizer_args(self):
        fromvllm.model_executor.model_loader.tensorizerimport TensorizerConfig

        for key in self.model_loader_extra_config:
            if key in TensorizerConfig._fields:
                self.model_loader_extra_config["tensorizer_config"][key] = (
                    self.model_loader_extra_config[key]
                )

    defcreate_load_config(self) -> LoadConfig:
        if self.quantization == "bitsandbytes":
            self.load_format = "bitsandbytes"

        if self.load_format == "tensorizer":
            if hasattr(self.model_loader_extra_config, "to_serializable"):
                self.model_loader_extra_config = (
                    self.model_loader_extra_config.to_serializable()
                )
            self.model_loader_extra_config["tensorizer_config"] = {}
            self.model_loader_extra_config["tensorizer_config"]["tensorizer_dir"] = (
                self.model
            )
            self.validate_tensorizer_args()

        return LoadConfig(
            load_format=self.load_format,
            download_dir=self.download_dir,
            safetensors_load_strategy=self.safetensors_load_strategy,
            model_loader_extra_config=self.model_loader_extra_config,
            ignore_patterns=self.ignore_patterns,
            use_tqdm_on_load=self.use_tqdm_on_load,
            pt_load_map_location=self.pt_load_map_location,
        )

    defcreate_speculative_config(
        self,
        target_model_config: ModelConfig,
        target_parallel_config: ParallelConfig,
    ) -> SpeculativeConfig | None:
"""Initializes and returns a SpeculativeConfig object based on
        `speculative_config`.

        This function utilizes `speculative_config` to create a
        SpeculativeConfig object. The `speculative_config` can either be
        provided as a JSON string input via CLI arguments or directly as a
        dictionary from the engine.
        """
        if self.speculative_config is None:
            return None

        # Note(Shangming): These parameters are not obtained from the cli arg
        # '--speculative-config' and must be passed in when creating the engine
        # config.
        self.speculative_config.update(
            {
                "target_model_config": target_model_config,
                "target_parallel_config": target_parallel_config,
            }
        )
        return SpeculativeConfig(**self.speculative_config)

    defcreate_engine_config(
        self,
        usage_context: UsageContext | None = None,
        headless: bool = False,
    ) -> VllmConfig:
"""
        Create the VllmConfig.

        NOTE: If VllmConfig is incompatible, we raise an error.
        """
        current_platform.pre_register_and_update()

        device_config = DeviceConfig(device=cast(Device, current_platform.device_type))

        envs.validate_environ(self.fail_on_environ_validation)

        # Check if the model is a speculator and override model/tokenizer/config
        # BEFORE creating ModelConfig, so the config is created with the target model
        # Skip speculator detection for cloud storage models (eg: S3, GCS) since
        # HuggingFace cannot load configs directly from S3 URLs. S3 models can still
        # use speculators with explicit --speculative-config.
        if not is_cloud_storage(self.model):
            (self.model, self.tokenizer, self.speculative_config) = (
                maybe_override_with_speculators(
                    model=self.model,
                    tokenizer=self.tokenizer,
                    revision=self.revision,
                    trust_remote_code=self.trust_remote_code,
                    vllm_speculative_config=self.speculative_config,
                    hf_token=self.hf_token,
                )
            )

        model_config = self.create_model_config()
        self.model = model_config.model
        self.model_weights = model_config.model_weights
        self.tokenizer = model_config.tokenizer

        self._check_feature_supported()
        self._set_default_chunked_prefill_and_prefix_caching_args(model_config)
        self._set_default_reasoning_config_args()
        sliding_window: int | None = None
        if not is_interleaved(model_config.hf_text_config):
            # Only set CacheConfig.sliding_window if the model is all sliding
            # window. Otherwise CacheConfig.sliding_window will override the
            # global layers in interleaved sliding window models.
            sliding_window = model_config.get_sliding_window()

        # Resolve "auto" kv_cache_dtype to actual value from model config
        resolved_cache_dtype = resolve_kv_cache_dtype_string(
            self.kv_cache_dtype, model_config
        )

        assert self.enable_prefix_caching is not None, (
            "enable_prefix_caching must be set by this point"
        )

        cache_config = CacheConfig(
            block_size=self.block_size,  # type: ignore[arg-type]
            gpu_memory_utilization=self.gpu_memory_utilization,
            kv_cache_memory_bytes=self.kv_cache_memory_bytes,
            cache_dtype=resolved_cache_dtype,  # type: ignore[arg-type]
            is_attention_free=model_config.is_attention_free,
            num_gpu_blocks_override=self.num_gpu_blocks_override,
            sliding_window=sliding_window,
            enable_prefix_caching=self.enable_prefix_caching,
            prefix_caching_hash_algo=self.prefix_caching_hash_algo,
            calculate_kv_scales=self.calculate_kv_scales,
            kv_cache_dtype_skip_layers=self.kv_cache_dtype_skip_layers,
            kv_sharing_fast_prefill=self.kv_sharing_fast_prefill,
            mamba_cache_dtype=self.mamba_cache_dtype,
            mamba_ssm_cache_dtype=self.mamba_ssm_cache_dtype,
            mamba_block_size=self.mamba_block_size,
            mamba_cache_mode=self.mamba_cache_mode,
            kv_offloading_size=self.kv_offloading_size,
            kv_offloading_backend=self.kv_offloading_backend,
        )

        if resolved_cache_dtype.startswith("turboquant_"):
            fromvllm.model_executor.layers.quantization.turboquant.configimport (
                TurboQuantConfig,
            )

            boundary = TurboQuantConfig.get_boundary_skip_layers(model_config)
            existing = set(cache_config.kv_cache_dtype_skip_layers)
            cache_config.kv_cache_dtype_skip_layers = sorted(
                existing | set(boundary), key=int
            )

        ray_runtime_env = None
        if is_ray_initialized():
            # Ray Serve LLM calls `create_engine_config` in the context
            # of a Ray task, therefore we check is_ray_initialized()
            # as opposed to is_in_ray_actor().
            importray

            ray_runtime_env = ray.get_runtime_context().runtime_env
            # Avoid logging sensitive environment variables
            sanitized_env = ray_runtime_env.to_dict() if ray_runtime_env else {}
            if "env_vars" in sanitized_env:
                sanitized_env["env_vars"] = {
                    k: "***" for k in sanitized_env["env_vars"]
                }
            logger.info("Using ray runtime env (env vars redacted): %s", sanitized_env)

        # Get the current placement group if Ray is initialized and
        # we are in a Ray actor. If so, then the placement group will be
        # passed to spawned processes.
        placement_group = None
        if is_in_ray_actor():
            importray

            # This call initializes Ray automatically if it is not initialized,
            # but we should not do this here.
            placement_group = ray.util.get_current_placement_group()

        assert not headless or not self.data_parallel_hybrid_lb, (
            "data_parallel_hybrid_lb is not applicable in headless mode"
        )
        assert not (self.data_parallel_hybrid_lb and self.data_parallel_external_lb), (
            "data_parallel_hybrid_lb and data_parallel_external_lb cannot both be True."
        )
        assert self.data_parallel_backend == "mp" or self.nnodes == 1, (
            "nnodes > 1 is only supported with data_parallel_backend=mp"
        )
        inferred_data_parallel_rank = 0
        if self.nnodes > 1:
            world_size = (
                self.data_parallel_size
                * self.pipeline_parallel_size
                * self.tensor_parallel_size
            )
            world_size_within_dp = (
                self.pipeline_parallel_size * self.tensor_parallel_size
            )
            local_world_size = world_size // self.nnodes
            assert world_size % self.nnodes == 0, (
                f"world_size={world_size} must be divisible by nnodes={self.nnodes}."
            )
            assert self.node_rank < self.nnodes, (
                f"node_rank={self.node_rank} must be less than nnodes={self.nnodes}."
            )
            inferred_data_parallel_rank = (
                self.node_rank * local_world_size
            ) // world_size_within_dp
            if self.data_parallel_size > 1 and self.data_parallel_external_lb:
                self.data_parallel_rank = inferred_data_parallel_rank
                logger.info(
                    "Inferred data_parallel_rank %d from node_rank %d for external lb",
                    self.data_parallel_rank,
                    self.node_rank,
                )
            elif self.data_parallel_size_local is None:
                # Infer data parallel size local for internal dplb:
                self.data_parallel_size_local = max(
                    local_world_size // world_size_within_dp, 1
                )
        data_parallel_external_lb = (
            self.data_parallel_external_lb or self.data_parallel_rank is not None
        )
        if (
            self.data_parallel_size > 1
            and data_parallel_external_lb
            and not model_config.is_moe
        ):
            raise ValueError(
                "Non-MoE models do not support external data parallel mode. "
                "For external load balancing, launch independent vLLM "
                "instances without --data-parallel-* arguments."
            )
        # Local DP rank = 1, use pure-external LB.
        if data_parallel_external_lb:
            assert self.data_parallel_rank is not None, (
                "data_parallel_rank or node_rank must be specified if "
                "data_parallel_external_lb is enable."
            )
            assert self.data_parallel_size_local in (1, None), (
                "data_parallel_size_local must be 1 or None when data_parallel_rank "
                "is set"
            )
            data_parallel_size_local = 1
            # Use full external lb if we have local_size of 1.
            self.data_parallel_hybrid_lb = False
        elif self.data_parallel_size_local is not None:
            data_parallel_size_local = self.data_parallel_size_local

            if self.data_parallel_start_rank and not headless:
                # Infer hybrid LB mode.
                self.data_parallel_hybrid_lb = True

            if self.data_parallel_hybrid_lb and data_parallel_size_local == 1:
                # Use full external lb if we have local_size of 1.
                logger.warning(
                    "data_parallel_hybrid_lb is not eligible when "
                    "data_parallel_size_local = 1, autoswitch to "
                    "data_parallel_external_lb."
                )
                data_parallel_external_lb = True
                self.data_parallel_hybrid_lb = False

            if data_parallel_size_local == self.data_parallel_size:
                # Disable hybrid LB mode if set for a single node
                self.data_parallel_hybrid_lb = False

            self.data_parallel_rank = (
                self.data_parallel_start_rank or inferred_data_parallel_rank
            )
            if self.nnodes > 1:
                logger.info(
                    "Inferred data_parallel_rank %d from node_rank %d",
                    self.data_parallel_rank,
                    self.node_rank,
                )
        else:
            assert not self.data_parallel_hybrid_lb, (
                "data_parallel_size_local must be set to use data_parallel_hybrid_lb."
            )

            if self.data_parallel_backend == "ray" and (
                envs.VLLM_RAY_DP_PACK_STRATEGY == "span"
            ):
                # Data parallel size defaults to 1 if DP ranks are spanning
                # multiple nodes
                data_parallel_size_local = 1
            else:
                # Otherwise local DP size defaults to global DP size if not set
                data_parallel_size_local = self.data_parallel_size

        # DP address, used in multi-node case for torch distributed group
        # and ZMQ sockets.
        if self.data_parallel_address is None:
            if self.data_parallel_backend == "ray":
                host_ip = get_ip()
                logger.info(
                    "Using host IP %s as ray-based data parallel address", host_ip
                )
                data_parallel_address = host_ip
            else:
                assert self.data_parallel_backend == "mp", (
                    "data_parallel_backend can only be ray or mp, got %s",
                    self.data_parallel_backend,
                )
                data_parallel_address = (
                    self.master_addr or ParallelConfig.data_parallel_master_ip
                )
        else:
            data_parallel_address = self.data_parallel_address

        # This port is only used when there are remote data parallel engines,
        # otherwise the local IPC transport is used.
        data_parallel_rpc_port = (
            self.data_parallel_rpc_port
            if (self.data_parallel_rpc_port is not None)
            else ParallelConfig.data_parallel_rpc_port
        )

        if self.tokens_only and not model_config.skip_tokenizer_init:
            model_config.skip_tokenizer_init = True
            logger.info("Skipping tokenizer initialization for tokens-only mode.")

        parallel_config = ParallelConfig(
            pipeline_parallel_size=self.pipeline_parallel_size,
            tensor_parallel_size=self.tensor_parallel_size,
            prefill_context_parallel_size=self.prefill_context_parallel_size,
            data_parallel_size=self.data_parallel_size,
            data_parallel_rank=self.data_parallel_rank or 0,
            data_parallel_external_lb=data_parallel_external_lb,
            data_parallel_size_local=data_parallel_size_local,
            master_addr=self.master_addr,
            master_port=self.master_port,
            nnodes=self.nnodes,
            node_rank=self.node_rank,
            distributed_timeout_seconds=self.distributed_timeout_seconds,
            data_parallel_master_ip=data_parallel_address,
            data_parallel_rpc_port=data_parallel_rpc_port,
            data_parallel_backend=self.data_parallel_backend,
            data_parallel_hybrid_lb=self.data_parallel_hybrid_lb,
            is_moe_model=model_config.is_moe,
            enable_expert_parallel=self.enable_expert_parallel,
            enable_ep_weight_filter=self.enable_ep_weight_filter,
            all2all_backend=self.all2all_backend,
            enable_elastic_ep=self.enable_elastic_ep,
            enable_dbo=self.enable_dbo,
            ubatch_size=self.ubatch_size,
            dbo_decode_token_threshold=self.dbo_decode_token_threshold,
            dbo_prefill_token_threshold=self.dbo_prefill_token_threshold,
            disable_nccl_for_dp_synchronization=self.disable_nccl_for_dp_synchronization,
            enable_eplb=self.enable_eplb,
            eplb_config=self.eplb_config,
            expert_placement_strategy=self.expert_placement_strategy,
            max_parallel_loading_workers=self.max_parallel_loading_workers,
            disable_custom_all_reduce=self.disable_custom_all_reduce,
            ray_workers_use_nsight=self.ray_workers_use_nsight,
            ray_runtime_env=ray_runtime_env,
            placement_group=placement_group,
            distributed_executor_backend=self.distributed_executor_backend,
            worker_cls=self.worker_cls,
            worker_extension_cls=self.worker_extension_cls,
            decode_context_parallel_size=self.decode_context_parallel_size,
            dcp_comm_backend=self.dcp_comm_backend,
            dcp_kv_cache_interleave_size=self.dcp_kv_cache_interleave_size,
            cp_kv_cache_interleave_size=self.cp_kv_cache_interleave_size,
            _api_process_count=self._api_process_count,
            _api_process_rank=self._api_process_rank,
            numa_bind=self.numa_bind,
            numa_bind_nodes=self.numa_bind_nodes,
            numa_bind_cpus=self.numa_bind_cpus,
        )

        speculative_config = self.create_speculative_config(
            target_model_config=model_config,
            target_parallel_config=parallel_config,
        )

        self._set_default_max_num_seqs_and_batched_tokens_args(
            usage_context,
            model_config,
            parallel_config,
        )

        assert self.max_num_batched_tokens is not None, (
            "max_num_batched_tokens must be set by this point"
        )
        assert self.max_num_seqs is not None, "max_num_seqs must be set by this point"
        assert self.enable_chunked_prefill is not None, (
            "enable_chunked_prefill must be set by this point"
        )
        assert model_config.max_model_len is not None, (
            "max_model_len must be set by this point"
        )
        scheduler_config = SchedulerConfig(
            runner_type=model_config.runner_type,
            max_num_batched_tokens=self.max_num_batched_tokens,
            max_num_seqs=self.max_num_seqs,
            max_model_len=model_config.max_model_len,
            enable_chunked_prefill=self.enable_chunked_prefill,
            disable_chunked_mm_input=self.disable_chunked_mm_input,
            is_multimodal_model=model_config.is_multimodal_model,
            is_encoder_decoder=model_config.is_encoder_decoder,
            policy=self.scheduling_policy,
            scheduler_cls=self.scheduler_cls,
            max_num_partial_prefills=self.max_num_partial_prefills,
            max_long_partial_prefills=self.max_long_partial_prefills,
            long_prefill_token_threshold=self.long_prefill_token_threshold,
            scheduler_reserve_full_isl=self.scheduler_reserve_full_isl,
            disable_hybrid_kv_cache_manager=self.disable_hybrid_kv_cache_manager,
            async_scheduling=self.async_scheduling,
            stream_interval=self.stream_interval,
        )

        if not model_config.is_multimodal_model and self.default_mm_loras:
            raise ValueError(
                "Default modality-specific LoRA(s) were provided for a "
                "non multimodal model"
            )

        lora_config = (
            LoRAConfig(
                max_lora_rank=self.max_lora_rank,
                max_loras=self.max_loras,
                default_mm_loras=self.default_mm_loras,
                fully_sharded_loras=self.fully_sharded_loras,
                lora_dtype=self.lora_dtype,
                target_modules=self.lora_target_modules,
                enable_tower_connector_lora=self.enable_tower_connector_lora,
                specialize_active_lora=self.specialize_active_lora,
                max_cpu_loras=self.max_cpu_loras
                if self.max_cpu_loras and self.max_cpu_loras > 0
                else None,
            )
            if self.enable_lora
            else None
        )

        if (
            lora_config is not None
            and speculative_config is not None
            and scheduler_config.max_num_batched_tokens
            < (
                scheduler_config.max_num_seqs
                * (speculative_config.num_speculative_tokens + 1)
            )
        ):
            raise ValueError(
                "Consider increasing max_num_batched_tokens or "
                "decreasing num_speculative_tokens"
            )

        # bitsandbytes pre-quantized model need a specific model loader
        if model_config.quantization == "bitsandbytes":
            self.quantization = self.load_format = "bitsandbytes"

        # Attention config overrides
        attention_config = copy.deepcopy(self.attention_config)
        if self.attention_backend is not None:
            if attention_config.backend is not None:
                raise ValueError(
                    "attention_backend and attention_config.backend "
                    "are mutually exclusive"
                )
            # Reuse the validator to handle "auto" and string-to-enum conversion
            attention_config.backend = AttentionConfig.validate_backend_before(
                self.attention_backend
            )

        # TurboQuant requires FlashAttention 2 — FA3 boundary layers assert
        # FlashAttentionImpl which fails with TurboQuantAttentionImpl.
        if resolved_cache_dtype.startswith("turboquant_") and (
            attention_config.flash_attn_version is None
            or attention_config.flash_attn_version >= 3
        ):
            logger.warning(
                "TurboQuant is not yet compatible with FlashAttention >= 3. "
                "Overriding flash_attn_version to 2. To silence this "
                "warning, pass --attention-config.flash_attn_version=2"
            )
            attention_config.flash_attn_version = 2

        # Mamba config overrides
        mamba_config = copy.deepcopy(self.mamba_config)
        # Convert string to enum if needed (CLI parsing returns a string)
        if isinstance(self.mamba_backend, str):
            mamba_config.backend = MambaBackendEnum[self.mamba_backend.upper()]
        else:
            mamba_config.backend = self.mamba_backend
        if self.enable_mamba_cache_stochastic_rounding:
            mamba_config.enable_stochastic_rounding = (
                self.enable_mamba_cache_stochastic_rounding
            )
        if self.mamba_cache_philox_rounds:
            mamba_config.stochastic_rounding_philox_rounds = (
                self.mamba_cache_philox_rounds
            )

        # Kernel config overrides
        kernel_config = copy.deepcopy(self.kernel_config)
        if self.enable_flashinfer_autotune is not None:
            if kernel_config.enable_flashinfer_autotune is not None:
                raise ValueError(
                    "enable_flashinfer_autotune and "
                    "kernel_config.enable_flashinfer_autotune "
                    "are mutually exclusive"
                )
            kernel_config.enable_flashinfer_autotune = self.enable_flashinfer_autotune
        if self.moe_backend != "auto":
            kernel_config.moe_backend = self.moe_backend

        # Transfer top-level ir_op_priority into KernelConfig.ir_op_priority
        for op_name, op_priority in asdict(self.ir_op_priority).items():
            # Empty means unset
            if not op_priority:
                continue

            # Priority cannot be set 2x for the same op
            if getattr(kernel_config.ir_op_priority, op_name):
                raise ValueError(
                    f"Op priority for {op_name} specified via both ir_op_priority "
                    f"and KernelConfig.ir_op_priority, only one allowed at a time."
                )

            # Set the attribute
            setattr(kernel_config.ir_op_priority, op_name, op_priority)

        load_config = self.create_load_config()

        # Pass reasoning_parser into StructuredOutputsConfig
        if self.reasoning_parser:
            self.structured_outputs_config.reasoning_parser = self.reasoning_parser

        if self.reasoning_parser_plugin:
            self.structured_outputs_config.reasoning_parser_plugin = (
                self.reasoning_parser_plugin
            )

        observability_config = ObservabilityConfig(
            show_hidden_metrics_for_version=self.show_hidden_metrics_for_version,
            otlp_traces_endpoint=self.otlp_traces_endpoint,
            collect_detailed_traces=self.collect_detailed_traces,
            kv_cache_metrics=self.kv_cache_metrics,
            kv_cache_metrics_sample=self.kv_cache_metrics_sample,
            cudagraph_metrics=self.cudagraph_metrics,
            enable_layerwise_nvtx_tracing=self.enable_layerwise_nvtx_tracing,
            enable_mfu_metrics=self.enable_mfu_metrics,
            enable_mm_processor_stats=self.enable_mm_processor_stats,
            enable_logging_iteration_details=self.enable_logging_iteration_details,
        )

        # Compilation config overrides
        compilation_config = copy.deepcopy(self.compilation_config)
        if self.cudagraph_capture_sizes is not None:
            if compilation_config.cudagraph_capture_sizes is not None:
                raise ValueError(
                    "cudagraph_capture_sizes and compilation_config."
                    "cudagraph_capture_sizes are mutually exclusive"
                )
            compilation_config.cudagraph_capture_sizes = self.cudagraph_capture_sizes
        if self.max_cudagraph_capture_size is not None:
            if compilation_config.max_cudagraph_capture_size is not None:
                raise ValueError(
                    "max_cudagraph_capture_size and compilation_config."
                    "max_cudagraph_capture_size are mutually exclusive"
                )
            compilation_config.max_cudagraph_capture_size = (
                self.max_cudagraph_capture_size
            )

        offload_config = OffloadConfig(
            offload_backend=self.offload_backend,
            uva=UVAOffloadConfig(
                cpu_offload_gb=self.cpu_offload_gb,
                cpu_offload_params=self.cpu_offload_params,
            ),
            prefetch=PrefetchOffloadConfig(
                offload_group_size=self.offload_group_size,
                offload_num_in_group=self.offload_num_in_group,
                offload_prefetch_step=self.offload_prefetch_step,
                offload_params=self.offload_params,
            ),
        )

        if self.gdn_prefill_backend is not None:
            self.additional_config["gdn_prefill_backend"] = self.gdn_prefill_backend

        config = VllmConfig(
            model_config=model_config,
            cache_config=cache_config,
            parallel_config=parallel_config,
            scheduler_config=scheduler_config,
            device_config=device_config,
            load_config=load_config,
            offload_config=offload_config,
            attention_config=attention_config,
            mamba_config=mamba_config,
            kernel_config=kernel_config,
            lora_config=lora_config,
            speculative_config=speculative_config,
            structured_outputs_config=self.structured_outputs_config,
            observability_config=observability_config,
            compilation_config=compilation_config,
            kv_transfer_config=self.kv_transfer_config,
            kv_events_config=self.kv_events_config,
            ec_transfer_config=self.ec_transfer_config,
            reasoning_config=self.reasoning_config,
            profiler_config=self.profiler_config,
            additional_config=self.additional_config,
            optimization_level=self.optimization_level,
            performance_mode=self.performance_mode,
            weight_transfer_config=self.weight_transfer_config,
            shutdown_timeout=self.shutdown_timeout,
        )

        return config

    def_check_feature_supported(self):
"""Raise an error if the feature is not supported."""
        # No Concurrent Partial Prefills so far.
        if (
            self.max_num_partial_prefills != SchedulerConfig.max_num_partial_prefills
            or self.max_long_partial_prefills
            != SchedulerConfig.max_long_partial_prefills
        ):
            _raise_unsupported_error(feature_name="Concurrent Partial Prefill")

        if self.pipeline_parallel_size > 1:
            supports_pp = getattr(
                self.distributed_executor_backend, "supports_pp", False
            )
            if not supports_pp and self.distributed_executor_backend not in (
                ParallelConfig.distributed_executor_backend,
                "ray",
                "mp",
                "external_launcher",
            ):
                name = (
                    "Pipeline Parallelism without Ray distributed "
                    "executor or multiprocessing executor or external "
                    "launcher"
                )
                _raise_unsupported_error(feature_name=name)

    @classmethod
    defget_batch_defaults(
        cls,
        world_size: int,
    ) -> tuple[dict[UsageContext | None, int], dict[UsageContext | None, int]]:
        fromvllm.usage.usage_libimport UsageContext

        default_max_num_batched_tokens: dict[UsageContext | None, int]
        default_max_num_seqs: dict[UsageContext | None, int]

        # When no user override, set the default values based on the usage
        # context.
        # Use different default values for different hardware.

        # Try to query the device name on the current platform. If it fails,
        # it may be because the platform that imports vLLM is not the same
        # as the platform that vLLM is running on (e.g. the case of scaling
        # vLLM with Ray) and has no GPUs. In this case we use the default
        # values for non-H100/H200 GPUs.
        try:
            device_memory = current_platform.get_device_total_memory()
            device_name = current_platform.get_device_name().lower()
        except Exception:
            # This is only used to set default_max_num_batched_tokens
            device_memory = 0
            device_name = ""

        # NOTE(Kuntai): Setting large `max_num_batched_tokens` for A100 reduces
        # throughput, see PR #17885 for more details.
        # So here we do an extra device name check to prevent such regression.
        if device_memory >= 70 * GiB_bytes and "a100" not in device_name:
            # For GPUs like H100 and MI300x, use larger default values.
            default_max_num_batched_tokens = {
                UsageContext.LLM_CLASS: 16384,
                UsageContext.OPENAI_API_SERVER: 8192,
            }
            default_max_num_seqs = {
                UsageContext.LLM_CLASS: 1024,
                UsageContext.OPENAI_API_SERVER: 1024,
            }
        else:
            # TODO(woosuk): Tune the default values for other hardware.
            default_max_num_batched_tokens = {
                UsageContext.LLM_CLASS: 8192,
                UsageContext.OPENAI_API_SERVER: 2048,
            }
            default_max_num_seqs = {
                UsageContext.LLM_CLASS: 256,
                UsageContext.OPENAI_API_SERVER: 256,
            }

        # tpu specific default values.
        if current_platform.is_tpu():
            chip_name = current_platform.get_device_name()

            if chip_name == "V6E":
                default_max_num_batched_tokens = {
                    UsageContext.LLM_CLASS: 2048,
                    UsageContext.OPENAI_API_SERVER: 1024,
                }
            elif chip_name == "V5E":
                default_max_num_batched_tokens = {
                    UsageContext.LLM_CLASS: 1024,
                    UsageContext.OPENAI_API_SERVER: 512,
                }
            elif chip_name == "V5P":
                default_max_num_batched_tokens = {
                    UsageContext.LLM_CLASS: 512,
                    UsageContext.OPENAI_API_SERVER: 256,
                }

        # cpu specific default values.
        if current_platform.is_cpu():
            default_max_num_batched_tokens = {
                UsageContext.LLM_CLASS: 4096 * world_size,
                UsageContext.OPENAI_API_SERVER: 2048 * world_size,
            }
            default_max_num_seqs = {
                UsageContext.LLM_CLASS: 256 * world_size,
                UsageContext.OPENAI_API_SERVER: 128 * world_size,
            }

        return default_max_num_batched_tokens, default_max_num_seqs

    def_set_default_chunked_prefill_and_prefix_caching_args(
        self, model_config: ModelConfig
    ) -> None:
        default_chunked_prefill = model_config.is_chunked_prefill_supported
        default_prefix_caching = model_config.is_prefix_caching_supported

        if self.enable_chunked_prefill is None:
            self.enable_chunked_prefill = default_chunked_prefill

            logger.debug(
                "%s chunked prefill by default",
                "Enabling" if default_chunked_prefill else "Disabling",
            )
        elif (
            model_config.runner_type == "generate"
            and not self.enable_chunked_prefill
            and default_chunked_prefill
        ):
            logger.warning_once(
                "This model does not officially support disabling chunked prefill. "
                "Disabling this manually may cause the engine to crash "
                "or produce incorrect outputs.",
            )
        elif (
            model_config.runner_type == "pooling"
            and self.enable_chunked_prefill
            and not default_chunked_prefill
        ):
            logger.warning_once(
                "This model does not officially support chunked prefill. "
                "Enabling this manually may cause the engine to crash "
                "or produce incorrect outputs.",
            )

        if self.enable_prefix_caching is None:
            self.enable_prefix_caching = default_prefix_caching

            logger.debug(
                "%s prefix caching by default",
                "Enabling" if default_prefix_caching else "Disabling",
            )
        elif (
            model_config.runner_type == "pooling"
            and self.enable_prefix_caching
            and not default_prefix_caching
        ):
            logger.warning_once(
                "This model does not officially support prefix caching. "
                "Enabling this manually may cause the engine to crash "
                "or produce incorrect outputs.",
            )

        # Disable chunked prefill and prefix caching for:
        # RISCV CPUs in V1
        if current_platform.is_cpu() and current_platform.get_cpu_architecture() in (
            CpuArchEnum.RISCV,
        ):
            logger.info(
                "Chunked prefill is not supported for"
                "RISC-V CPUs; "
                "disabling it for V1 backend."
            )
            self.enable_chunked_prefill = False
            logger.info(
                "Prefix caching is not supported for "
                "RISC-V CPUs; "
                "disabling it for V1 backend."
            )
            self.enable_prefix_caching = False

    def_set_default_reasoning_config_args(self):
        if not self.reasoning_parser:
            return
        if self.reasoning_config is None:
            self.reasoning_config = ReasoningConfig()
        self.reasoning_config.reasoning_parser = self.reasoning_parser

    def_set_default_max_num_seqs_and_batched_tokens_args(
        self,
        usage_context: UsageContext | None,
        model_config: ModelConfig,
        parallel_config: ParallelConfig,
    ):
        world_size = self.pipeline_parallel_size * self.tensor_parallel_size
        (
            default_max_num_batched_tokens,
            default_max_num_seqs,
        ) = self.get_batch_defaults(world_size)

        orig_max_num_batched_tokens = self.max_num_batched_tokens
        orig_max_num_seqs = self.max_num_seqs

        if self.max_num_batched_tokens is None:
            if parallel_config.use_batched_dp_moe:
                self.max_num_batched_tokens = (
                    SchedulerConfig.DEFAULT_MAX_NUM_BATCHED_TOKENS_FOR_BATCHED_DP
                )
            else:
                self.max_num_batched_tokens = default_max_num_batched_tokens.get(
                    usage_context,
                    SchedulerConfig.DEFAULT_MAX_NUM_BATCHED_TOKENS,
                )

        if self.max_num_seqs is None:
            self.max_num_seqs = default_max_num_seqs.get(
                usage_context,
                SchedulerConfig.DEFAULT_MAX_NUM_SEQS,
            )

        # If throughput mode is set, double max_num_batched_tokens and max_num_seqs.
        if self.performance_mode == "throughput":
            if orig_max_num_batched_tokens is None:
                self.max_num_batched_tokens *= 2
            if orig_max_num_seqs is None:
                self.max_num_seqs *= 2

        if orig_max_num_batched_tokens is None:
            assert model_config.max_model_len is not None, (
                "max_model_len must be set by this point"
            )
            if not self.enable_chunked_prefill:
                # If max_model_len is too short, use the default for higher throughput.
                self.max_num_batched_tokens = max(
                    model_config.max_model_len,
                    self.max_num_batched_tokens,
                )

            # When using default settings,
            # Ensure max_num_batched_tokens does not exceed model limit.
            # Some models (e.g., Whisper) have embeddings tied to max length.
            self.max_num_batched_tokens = min(
                self.max_num_seqs * model_config.max_model_len,
                self.max_num_batched_tokens,
            )

            logger.debug(
                "Defaulting max_num_batched_tokens to %d for %s usage context.",
                self.max_num_batched_tokens,
                usage_context.value if usage_context else None,
            )

        if orig_max_num_seqs is None:
            assert self.max_num_batched_tokens is not None  # For type checking
            self.max_num_seqs = min(self.max_num_seqs, self.max_num_batched_tokens)

            logger.debug(
                "Defaulting max_num_seqs to %d for %s usage context.",
                self.max_num_seqs,
                usage_context.value if usage_context else None,
            )
```

### logits\_processors `class-attribute` `instance-attribute` [¶](#vllm.EngineArgs.logits_processors "Permanent link")

Custom logitproc types

### \_check\_feature\_supported [¶](#vllm.EngineArgs._check_feature_supported "Permanent link")

```
_check_feature_supported()
```

Raise an error if the feature is not supported.

Source code in `vllm/engine/arg_utils.py`

```
def_check_feature_supported(self):
"""Raise an error if the feature is not supported."""
    # No Concurrent Partial Prefills so far.
    if (
        self.max_num_partial_prefills != SchedulerConfig.max_num_partial_prefills
        or self.max_long_partial_prefills
        != SchedulerConfig.max_long_partial_prefills
    ):
        _raise_unsupported_error(feature_name="Concurrent Partial Prefill")

    if self.pipeline_parallel_size > 1:
        supports_pp = getattr(
            self.distributed_executor_backend, "supports_pp", False
        )
        if not supports_pp and self.distributed_executor_backend not in (
            ParallelConfig.distributed_executor_backend,
            "ray",
            "mp",
            "external_launcher",
        ):
            name = (
                "Pipeline Parallelism without Ray distributed "
                "executor or multiprocessing executor or external "
                "launcher"
            )
            _raise_unsupported_error(feature_name=name)
```

### add\_cli\_args `staticmethod` [¶](#vllm.EngineArgs.add_cli_args "Permanent link")

Shared CLI arguments for vLLM engine.

Source code in `vllm/engine/arg_utils.py`

```
@staticmethod
defadd_cli_args(parser: FlexibleArgumentParser) -> FlexibleArgumentParser:
"""Shared CLI arguments for vLLM engine."""

    # Model arguments
    model_kwargs = get_kwargs(ModelConfig)
    model_group = parser.add_argument_group(
        title="ModelConfig",
        description=ModelConfig.__doc__,
    )
    if not ("serve" in sys.argv[1:] and "--help" in sys.argv[1:]):
        model_group.add_argument("--model", **model_kwargs["model"])
    model_group.add_argument("--runner", **model_kwargs["runner"])
    model_group.add_argument("--convert", **model_kwargs["convert"])
    model_group.add_argument("--tokenizer", **model_kwargs["tokenizer"])
    model_group.add_argument("--tokenizer-mode", **model_kwargs["tokenizer_mode"])
    model_group.add_argument(
        "--trust-remote-code", **model_kwargs["trust_remote_code"]
    )
    model_group.add_argument("--dtype", **model_kwargs["dtype"])
    model_group.add_argument("--seed", **model_kwargs["seed"])
    model_group.add_argument("--hf-config-path", **model_kwargs["hf_config_path"])
    model_group.add_argument(
        "--allowed-local-media-path", **model_kwargs["allowed_local_media_path"]
    )
    model_group.add_argument(
        "--allowed-media-domains", **model_kwargs["allowed_media_domains"]
    )
    model_group.add_argument("--revision", **model_kwargs["revision"])
    model_group.add_argument("--code-revision", **model_kwargs["code_revision"])
    model_group.add_argument(
        "--tokenizer-revision", **model_kwargs["tokenizer_revision"]
    )
    model_group.add_argument("--max-model-len", **model_kwargs["max_model_len"])
    model_group.add_argument("--quantization", "-q", **model_kwargs["quantization"])
    model_group.add_argument(
        "--allow-deprecated-quantization",
        **model_kwargs["allow_deprecated_quantization"],
    )
    model_group.add_argument("--enforce-eager", **model_kwargs["enforce_eager"])
    model_group.add_argument(
        "--enable-return-routed-experts",
        **model_kwargs["enable_return_routed_experts"],
    )
    model_group.add_argument("--max-logprobs", **model_kwargs["max_logprobs"])
    model_group.add_argument("--logprobs-mode", **model_kwargs["logprobs_mode"])
    model_group.add_argument(
        "--disable-sliding-window", **model_kwargs["disable_sliding_window"]
    )
    model_group.add_argument(
        "--disable-cascade-attn", **model_kwargs["disable_cascade_attn"]
    )
    model_group.add_argument(
        "--skip-tokenizer-init", **model_kwargs["skip_tokenizer_init"]
    )
    model_group.add_argument(
        "--enable-prompt-embeds", **model_kwargs["enable_prompt_embeds"]
    )
    model_group.add_argument(
        "--served-model-name", **model_kwargs["served_model_name"]
    )
    model_group.add_argument("--config-format", **model_kwargs["config_format"])
    # This one is a special case because it can bool
    # or str. TODO: Handle this in get_kwargs
    model_group.add_argument(
        "--hf-token",
        type=str,
        nargs="?",
        const=True,
        default=model_kwargs["hf_token"]["default"],
        help=model_kwargs["hf_token"]["help"],
    )
    model_group.add_argument("--hf-overrides", **model_kwargs["hf_overrides"])
    model_group.add_argument("--pooler-config", **model_kwargs["pooler_config"])
    model_group.add_argument(
        "--generation-config", **model_kwargs["generation_config"]
    )
    model_group.add_argument(
        "--override-generation-config", **model_kwargs["override_generation_config"]
    )
    model_group.add_argument(
        "--enable-sleep-mode", **model_kwargs["enable_sleep_mode"]
    )
    model_group.add_argument("--model-impl", **model_kwargs["model_impl"])
    model_group.add_argument(
        "--override-attention-dtype", **model_kwargs["override_attention_dtype"]
    )
    model_group.add_argument(
        "--logits-processors", **model_kwargs["logits_processors"]
    )
    model_group.add_argument(
        "--io-processor-plugin", **model_kwargs["io_processor_plugin"]
    )
    model_group.add_argument(
        "--renderer-num-workers",
        **model_kwargs["renderer_num_workers"],
    )

    # Model loading arguments
    load_kwargs = get_kwargs(LoadConfig)
    load_group = parser.add_argument_group(
        title="LoadConfig",
        description=LoadConfig.__doc__,
    )
    load_group.add_argument("--load-format", **load_kwargs["load_format"])
    load_group.add_argument("--download-dir", **load_kwargs["download_dir"])
    load_group.add_argument(
        "--safetensors-load-strategy", **load_kwargs["safetensors_load_strategy"]
    )
    load_group.add_argument(
        "--model-loader-extra-config", **load_kwargs["model_loader_extra_config"]
    )
    load_group.add_argument("--ignore-patterns", **load_kwargs["ignore_patterns"])
    load_group.add_argument("--use-tqdm-on-load", **load_kwargs["use_tqdm_on_load"])
    load_group.add_argument(
        "--pt-load-map-location", **load_kwargs["pt_load_map_location"]
    )

    # Attention arguments
    attention_kwargs = get_kwargs(AttentionConfig)
    attention_group = parser.add_argument_group(
        title="AttentionConfig",
        description=AttentionConfig.__doc__,
    )
    attention_group.add_argument(
        "--attention-backend", **attention_kwargs["backend"]
    )

    # Mamba arguments
    mamba_kwargs = get_kwargs(MambaConfig)
    mamba_group = parser.add_argument_group(
        title="MambaConfig",
        description=MambaConfig.__doc__,
    )
    mamba_group.add_argument("--mamba-backend", **mamba_kwargs["backend"])
    mamba_group.add_argument(
        "--enable-mamba-cache-stochastic-rounding",
        **mamba_kwargs["enable_stochastic_rounding"],
    )
    mamba_group.add_argument(
        "--mamba-cache-philox-rounds",
        **mamba_kwargs["stochastic_rounding_philox_rounds"],
    )

    # Structured outputs arguments
    structured_outputs_kwargs = get_kwargs(StructuredOutputsConfig)
    structured_outputs_group = parser.add_argument_group(
        title="StructuredOutputsConfig",
        description=StructuredOutputsConfig.__doc__,
    )
    structured_outputs_group.add_argument(
        "--reasoning-parser",
        # Choices need to be validated after parsing to include plugins
        **structured_outputs_kwargs["reasoning_parser"],
    )
    structured_outputs_group.add_argument(
        "--reasoning-parser-plugin",
        **structured_outputs_kwargs["reasoning_parser_plugin"],
    )

    # Parallel arguments
    parallel_kwargs = get_kwargs(ParallelConfig)
    parallel_group = parser.add_argument_group(
        title="ParallelConfig",
        description=ParallelConfig.__doc__,
    )
    parallel_group.add_argument(
        "--distributed-executor-backend",
        **parallel_kwargs["distributed_executor_backend"],
    )
    parallel_group.add_argument(
        "--pipeline-parallel-size",
        "-pp",
        **parallel_kwargs["pipeline_parallel_size"],
    )
    parallel_group.add_argument("--master-addr", **parallel_kwargs["master_addr"])
    parallel_group.add_argument("--master-port", **parallel_kwargs["master_port"])
    parallel_group.add_argument("--nnodes", "-n", **parallel_kwargs["nnodes"])
    parallel_group.add_argument("--node-rank", "-r", **parallel_kwargs["node_rank"])
    parallel_group.add_argument(
        "--distributed-timeout-seconds",
        **parallel_kwargs["distributed_timeout_seconds"],
    )
    parallel_group.add_argument("--numa-bind", **parallel_kwargs["numa_bind"])
    parallel_group.add_argument(
        "--numa-bind-nodes", **parallel_kwargs["numa_bind_nodes"]
    )
    parallel_group.add_argument(
        "--numa-bind-cpus", **parallel_kwargs["numa_bind_cpus"]
    )
    parallel_group.add_argument(
        "--tensor-parallel-size", "-tp", **parallel_kwargs["tensor_parallel_size"]
    )
    parallel_group.add_argument(
        "--decode-context-parallel-size",
        "-dcp",
        **parallel_kwargs["decode_context_parallel_size"],
    )
    parallel_group.add_argument(
        "--dcp-comm-backend",
        **parallel_kwargs["dcp_comm_backend"],
    )
    parallel_group.add_argument(
        "--dcp-kv-cache-interleave-size",
        **parallel_kwargs["dcp_kv_cache_interleave_size"],
    )
    parallel_group.add_argument(
        "--cp-kv-cache-interleave-size",
        **parallel_kwargs["cp_kv_cache_interleave_size"],
    )
    parallel_group.add_argument(
        "--prefill-context-parallel-size",
        "-pcp",
        **parallel_kwargs["prefill_context_parallel_size"],
    )
    parallel_group.add_argument(
        "--data-parallel-size", "-dp", **parallel_kwargs["data_parallel_size"]
    )
    parallel_group.add_argument(
        "--data-parallel-rank",
        "-dpn",
        type=int,
        help="Data parallel rank of this instance. "
        "When set, enables external load balancer mode for MoE "
        "data-parallel deployments. Unsupported for non-MoE models; "
        "launch independent vLLM instances instead.",
    )
    parallel_group.add_argument(
        "--data-parallel-start-rank",
        "-dpr",
        type=int,
        help="Starting data parallel rank for secondary nodes.",
    )
    parallel_group.add_argument(
        "--data-parallel-size-local",
        "-dpl",
        type=int,
        help="Number of data parallel replicas to run on this node.",
    )
    parallel_group.add_argument(
        "--data-parallel-address",
        "-dpa",
        type=str,
        help="Address of data parallel cluster head-node.",
    )
    parallel_group.add_argument(
        "--data-parallel-rpc-port",
        "-dpp",
        type=int,
        help="Port for data parallel RPC communication.",
    )
    parallel_group.add_argument(
        "--data-parallel-backend",
        "-dpb",
        type=str,
        default="mp",
        help='Backend for data parallel, either "mp" or "ray".',
    )
    parallel_group.add_argument(
        "--data-parallel-hybrid-lb",
        "-dph",
        **parallel_kwargs["data_parallel_hybrid_lb"],
    )
    parallel_group.add_argument(
        "--data-parallel-external-lb",
        "-dpe",
        **parallel_kwargs["data_parallel_external_lb"],
    )
    parallel_group.add_argument(
        "--enable-expert-parallel",
        "-ep",
        **parallel_kwargs["enable_expert_parallel"],
    )
    parallel_group.add_argument(
        "--enable-ep-weight-filter",
        **parallel_kwargs["enable_ep_weight_filter"],
    )
    parallel_group.add_argument(
        "--all2all-backend", **parallel_kwargs["all2all_backend"]
    )
    parallel_group.add_argument("--enable-dbo", **parallel_kwargs["enable_dbo"])
    parallel_group.add_argument(
        "--ubatch-size",
        **parallel_kwargs["ubatch_size"],
    )
    parallel_group.add_argument(
        "--enable-elastic-ep", **parallel_kwargs["enable_elastic_ep"]
    )
    parallel_group.add_argument(
        "--dbo-decode-token-threshold",
        **parallel_kwargs["dbo_decode_token_threshold"],
    )
    parallel_group.add_argument(
        "--dbo-prefill-token-threshold",
        **parallel_kwargs["dbo_prefill_token_threshold"],
    )
    parallel_group.add_argument(
        "--disable-nccl-for-dp-synchronization",
        **parallel_kwargs["disable_nccl_for_dp_synchronization"],
    )
    parallel_group.add_argument("--enable-eplb", **parallel_kwargs["enable_eplb"])
    parallel_group.add_argument("--eplb-config", **parallel_kwargs["eplb_config"])
    parallel_group.add_argument(
        "--expert-placement-strategy",
        **parallel_kwargs["expert_placement_strategy"],
    )

    parallel_group.add_argument(
        "--max-parallel-loading-workers",
        **parallel_kwargs["max_parallel_loading_workers"],
    )
    parallel_group.add_argument(
        "--ray-workers-use-nsight", **parallel_kwargs["ray_workers_use_nsight"]
    )
    parallel_group.add_argument(
        "--disable-custom-all-reduce",
        **parallel_kwargs["disable_custom_all_reduce"],
    )
    parallel_group.add_argument("--worker-cls", **parallel_kwargs["worker_cls"])
    parallel_group.add_argument(
        "--worker-extension-cls", **parallel_kwargs["worker_extension_cls"]
    )

    # KV cache arguments
    cache_kwargs = get_kwargs(CacheConfig)
    cache_group = parser.add_argument_group(
        title="CacheConfig",
        description=CacheConfig.__doc__,
    )
    cache_group.add_argument("--block-size", **cache_kwargs["block_size"])
    cache_group.add_argument(
        "--gpu-memory-utilization", **cache_kwargs["gpu_memory_utilization"]
    )
    cache_group.add_argument(
        "--kv-cache-memory-bytes", **cache_kwargs["kv_cache_memory_bytes"]
    )
    cache_group.add_argument("--kv-cache-dtype", **cache_kwargs["cache_dtype"])
    cache_group.add_argument(
        "--num-gpu-blocks-override", **cache_kwargs["num_gpu_blocks_override"]
    )
    cache_group.add_argument(
        "--enable-prefix-caching",
        **{
            **cache_kwargs["enable_prefix_caching"],
            "default": None,
        },
    )
    cache_group.add_argument(
        "--prefix-caching-hash-algo", **cache_kwargs["prefix_caching_hash_algo"]
    )
    cache_group.add_argument(
        "--calculate-kv-scales", **cache_kwargs["calculate_kv_scales"]
    )
    cache_group.add_argument(
        "--kv-cache-dtype-skip-layers", **cache_kwargs["kv_cache_dtype_skip_layers"]
    )
    cache_group.add_argument(
        "--kv-sharing-fast-prefill", **cache_kwargs["kv_sharing_fast_prefill"]
    )
    cache_group.add_argument(
        "--mamba-cache-dtype", **cache_kwargs["mamba_cache_dtype"]
    )
    cache_group.add_argument(
        "--mamba-ssm-cache-dtype", **cache_kwargs["mamba_ssm_cache_dtype"]
    )
    cache_group.add_argument(
        "--mamba-block-size", **cache_kwargs["mamba_block_size"]
    )
    cache_group.add_argument(
        "--mamba-cache-mode", **cache_kwargs["mamba_cache_mode"]
    )
    cache_group.add_argument(
        "--kv-offloading-size", **cache_kwargs["kv_offloading_size"]
    )
    cache_group.add_argument(
        "--kv-offloading-backend", **cache_kwargs["kv_offloading_backend"]
    )

    # Model weight offload related configs
    offload_kwargs = get_kwargs(OffloadConfig)
    uva_kwargs = get_kwargs(UVAOffloadConfig)
    prefetch_kwargs = get_kwargs(PrefetchOffloadConfig)
    offload_group = parser.add_argument_group(
        title="OffloadConfig",
        description=OffloadConfig.__doc__,
    )
    offload_group.add_argument(
        "--offload-backend", **offload_kwargs["offload_backend"]
    )
    offload_group.add_argument("--cpu-offload-gb", **uva_kwargs["cpu_offload_gb"])
    offload_group.add_argument(
        "--cpu-offload-params", **uva_kwargs["cpu_offload_params"]
    )
    offload_group.add_argument(
        "--offload-group-size",
        **prefetch_kwargs["offload_group_size"],
    )
    offload_group.add_argument(
        "--offload-num-in-group",
        **prefetch_kwargs["offload_num_in_group"],
    )
    offload_group.add_argument(
        "--offload-prefetch-step",
        **prefetch_kwargs["offload_prefetch_step"],
    )
    offload_group.add_argument(
        "--offload-params", **prefetch_kwargs["offload_params"]
    )

    # Multimodal related configs
    multimodal_kwargs = get_kwargs(MultiModalConfig)
    multimodal_group = parser.add_argument_group(
        title="MultiModalConfig",
        description=MultiModalConfig.__doc__,
    )
    multimodal_group.add_argument(
        "--language-model-only", **multimodal_kwargs["language_model_only"]
    )
    multimodal_group.add_argument(
        "--limit-mm-per-prompt", **multimodal_kwargs["limit_per_prompt"]
    )
    multimodal_group.add_argument(
        "--enable-mm-embeds", **multimodal_kwargs["enable_mm_embeds"]
    )
    multimodal_group.add_argument(
        "--media-io-kwargs", **multimodal_kwargs["media_io_kwargs"]
    )
    multimodal_group.add_argument(
        "--mm-processor-kwargs", **multimodal_kwargs["mm_processor_kwargs"]
    )
    multimodal_group.add_argument(
        "--mm-processor-cache-gb", **multimodal_kwargs["mm_processor_cache_gb"]
    )
    multimodal_group.add_argument(
        "--mm-processor-cache-type", **multimodal_kwargs["mm_processor_cache_type"]
    )
    multimodal_group.add_argument(
        "--mm-shm-cache-max-object-size-mb",
        **multimodal_kwargs["mm_shm_cache_max_object_size_mb"],
    )
    multimodal_group.add_argument(
        "--mm-encoder-only", **multimodal_kwargs["mm_encoder_only"]
    )
    multimodal_group.add_argument(
        "--mm-encoder-tp-mode", **multimodal_kwargs["mm_encoder_tp_mode"]
    )
    multimodal_group.add_argument(
        "--mm-encoder-attn-backend",
        **multimodal_kwargs["mm_encoder_attn_backend"],
    )
    multimodal_group.add_argument(
        "--mm-encoder-attn-dtype",
        **multimodal_kwargs["mm_encoder_attn_dtype"],
    )
    multimodal_group.add_argument(
        "--mm-encoder-fp8-scale-path",
        **multimodal_kwargs["mm_encoder_fp8_scale_path"],
    )
    multimodal_group.add_argument(
        "--mm-encoder-fp8-scale-save-path",
        **multimodal_kwargs["mm_encoder_fp8_scale_save_path"],
    )
    multimodal_group.add_argument(
        "--mm-encoder-fp8-scale-save-margin",
        **multimodal_kwargs["mm_encoder_fp8_scale_save_margin"],
    )
    multimodal_group.add_argument(
        "--interleave-mm-strings", **multimodal_kwargs["interleave_mm_strings"]
    )
    multimodal_group.add_argument(
        "--skip-mm-profiling", **multimodal_kwargs["skip_mm_profiling"]
    )

    multimodal_group.add_argument(
        "--video-pruning-rate", **multimodal_kwargs["video_pruning_rate"]
    )
    multimodal_group.add_argument(
        "--mm-tensor-ipc", **multimodal_kwargs["mm_tensor_ipc"]
    )

    # LoRA related configs
    lora_kwargs = get_kwargs(LoRAConfig)
    lora_group = parser.add_argument_group(
        title="LoRAConfig",
        description=LoRAConfig.__doc__,
    )
    lora_group.add_argument(
        "--enable-lora",
        action=argparse.BooleanOptionalAction,
        help="If True, enable handling of LoRA adapters.",
    )
    lora_group.add_argument("--max-loras", **lora_kwargs["max_loras"])
    lora_group.add_argument("--max-lora-rank", **lora_kwargs["max_lora_rank"])
    lora_group.add_argument(
        "--lora-dtype",
        **lora_kwargs["lora_dtype"],
    )
    lora_group.add_argument(
        "--enable-tower-connector-lora",
        **lora_kwargs["enable_tower_connector_lora"],
    )
    lora_group.add_argument("--max-cpu-loras", **lora_kwargs["max_cpu_loras"])
    lora_group.add_argument(
        "--fully-sharded-loras", **lora_kwargs["fully_sharded_loras"]
    )
    lora_group.add_argument(
        "--lora-target-modules", **lora_kwargs["target_modules"]
    )
    lora_group.add_argument("--default-mm-loras", **lora_kwargs["default_mm_loras"])
    lora_group.add_argument(
        "--specialize-active-lora", **lora_kwargs["specialize_active_lora"]
    )

    # Observability arguments
    observability_kwargs = get_kwargs(ObservabilityConfig)
    observability_group = parser.add_argument_group(
        title="ObservabilityConfig",
        description=ObservabilityConfig.__doc__,
    )
    observability_group.add_argument(
        "--show-hidden-metrics-for-version",
        **observability_kwargs["show_hidden_metrics_for_version"],
    )
    observability_group.add_argument(
        "--otlp-traces-endpoint", **observability_kwargs["otlp_traces_endpoint"]
    )
    # TODO: generalise this special case
    choices = observability_kwargs["collect_detailed_traces"]["choices"]
    metavar = f"{{{','.join(choices)}}}"
    observability_kwargs["collect_detailed_traces"]["metavar"] = metavar
    observability_kwargs["collect_detailed_traces"]["choices"] += [
        ",".join(p) for p in permutations(get_args(DetailedTraceModules), r=2)
    ]
    observability_group.add_argument(
        "--collect-detailed-traces",
        **observability_kwargs["collect_detailed_traces"],
    )
    observability_group.add_argument(
        "--kv-cache-metrics", **observability_kwargs["kv_cache_metrics"]
    )
    observability_group.add_argument(
        "--kv-cache-metrics-sample",
        **observability_kwargs["kv_cache_metrics_sample"],
    )
    observability_group.add_argument(
        "--cudagraph-metrics",
        **observability_kwargs["cudagraph_metrics"],
    )
    observability_group.add_argument(
        "--enable-layerwise-nvtx-tracing",
        **observability_kwargs["enable_layerwise_nvtx_tracing"],
    )
    observability_group.add_argument(
        "--enable-mfu-metrics",
        **observability_kwargs["enable_mfu_metrics"],
    )
    observability_group.add_argument(
        "--enable-logging-iteration-details",
        **observability_kwargs["enable_logging_iteration_details"],
    )

    # Scheduler arguments
    scheduler_kwargs = get_kwargs(SchedulerConfig)
    scheduler_group = parser.add_argument_group(
        title="SchedulerConfig",
        description=SchedulerConfig.__doc__,
    )
    scheduler_group.add_argument(
        "--max-num-batched-tokens",
        **{
            **scheduler_kwargs["max_num_batched_tokens"],
            "default": None,
        },
    )
    scheduler_group.add_argument(
        "--max-num-seqs",
        **{
            **scheduler_kwargs["max_num_seqs"],
            "default": None,
        },
    )
    scheduler_group.add_argument(
        "--max-num-partial-prefills", **scheduler_kwargs["max_num_partial_prefills"]
    )
    scheduler_group.add_argument(
        "--max-long-partial-prefills",
        **scheduler_kwargs["max_long_partial_prefills"],
    )
    scheduler_group.add_argument(
        "--long-prefill-token-threshold",
        **scheduler_kwargs["long_prefill_token_threshold"],
    )
    # multi-step scheduling has been removed; corresponding arguments
    # are no longer supported.
    scheduler_group.add_argument(
        "--scheduling-policy", **scheduler_kwargs["policy"]
    )
    scheduler_group.add_argument(
        "--enable-chunked-prefill",
        **{
            **scheduler_kwargs["enable_chunked_prefill"],
            "default": None,
        },
    )
    scheduler_group.add_argument(
        "--disable-chunked-mm-input", **scheduler_kwargs["disable_chunked_mm_input"]
    )
    scheduler_group.add_argument(
        "--scheduler-cls", **scheduler_kwargs["scheduler_cls"]
    )
    scheduler_group.add_argument(
        "--scheduler-reserve-full-isl",
        **scheduler_kwargs["scheduler_reserve_full_isl"],
    )
    scheduler_group.add_argument(
        "--disable-hybrid-kv-cache-manager",
        **scheduler_kwargs["disable_hybrid_kv_cache_manager"],
    )
    scheduler_group.add_argument(
        "--async-scheduling", **scheduler_kwargs["async_scheduling"]
    )
    scheduler_group.add_argument(
        "--stream-interval", **scheduler_kwargs["stream_interval"]
    )

    # Compilation arguments
    compilation_kwargs = get_kwargs(CompilationConfig)
    compilation_group = parser.add_argument_group(
        title="CompilationConfig",
        description=CompilationConfig.__doc__,
    )
    compilation_group.add_argument(
        "--cudagraph-capture-sizes", **compilation_kwargs["cudagraph_capture_sizes"]
    )
    compilation_group.add_argument(
        "--max-cudagraph-capture-size",
        **compilation_kwargs["max_cudagraph_capture_size"],
    )

    # Kernel arguments
    kernel_kwargs = get_kwargs(KernelConfig)
    kernel_group = parser.add_argument_group(
        title="KernelConfig",
        description=KernelConfig.__doc__,
    )
    kernel_group.add_argument("--ir-op-priority", **kernel_kwargs["ir_op_priority"])
    kernel_group.add_argument(
        "--enable-flashinfer-autotune",
        **kernel_kwargs["enable_flashinfer_autotune"],
    )
    moe_backend_kwargs = kernel_kwargs["moe_backend"]
    moe_backend_kwargs["type"] = lambda s: s.lower().replace("-", "_")
    kernel_group.add_argument("--moe-backend", **moe_backend_kwargs)

    # vLLM arguments
    vllm_kwargs = get_kwargs(VllmConfig)
    vllm_group = parser.add_argument_group(
        title="VllmConfig",
        description=VllmConfig.__doc__,
    )
    # We construct SpeculativeConfig using fields from other configs in
    # create_engine_config. So we set the type to a JSON string here to
    # delay the Pydantic validation that comes with SpeculativeConfig.
    vllm_kwargs["speculative_config"]["type"] = optional_type(json.loads)
    vllm_group.add_argument(
        "--speculative-config", "-sc", **vllm_kwargs["speculative_config"]
    )
    vllm_group.add_argument(
        "--kv-transfer-config", **vllm_kwargs["kv_transfer_config"]
    )
    vllm_group.add_argument("--kv-events-config", **vllm_kwargs["kv_events_config"])
    vllm_group.add_argument(
        "--ec-transfer-config", **vllm_kwargs["ec_transfer_config"]
    )
    vllm_group.add_argument(
        "--compilation-config", "-cc", **vllm_kwargs["compilation_config"]
    )
    vllm_group.add_argument(
        "--attention-config", "-ac", **vllm_kwargs["attention_config"]
    )
    vllm_group.add_argument("--reasoning-config", **vllm_kwargs["reasoning_config"])
    vllm_group.add_argument("--kernel-config", **vllm_kwargs["kernel_config"])
    vllm_group.add_argument(
        "--additional-config", **vllm_kwargs["additional_config"]
    )
    vllm_group.add_argument(
        "--structured-outputs-config", **vllm_kwargs["structured_outputs_config"]
    )
    vllm_group.add_argument("--profiler-config", **vllm_kwargs["profiler_config"])
    vllm_group.add_argument(
        "--optimization-level", **vllm_kwargs["optimization_level"]
    )
    vllm_group.add_argument("--performance-mode", **vllm_kwargs["performance_mode"])
    vllm_group.add_argument(
        "--weight-transfer-config", **vllm_kwargs["weight_transfer_config"]
    )

    # Other arguments
    parser.add_argument(
        "--disable-log-stats",
        action="store_true",
        help="Disable logging statistics.",
    )

    parser.add_argument(
        "--aggregate-engine-logging",
        action="store_true",
        help="Log aggregate rather than per-engine statistics "
        "when using data parallelism.",
    )

    parser.add_argument(
        "--fail-on-environ-validation",
        help="If set, the engine will raise an error if "
        "environment validation fails.",
        default=False,
        action=argparse.BooleanOptionalAction,
    )

    parser.add_argument(
        "--shutdown-timeout",
        type=int,
        default=0,
        help="Shutdown timeout in seconds. 0 = abort, >0 = wait.",
    )

    parser.add_argument(
        "--gdn-prefill-backend",
        dest="gdn_prefill_backend",
        choices=["flashinfer", "triton"],
        default=None,
        help="Select GDN prefill backend.",
    )
    return parser
```

### create\_engine\_config [¶](#vllm.EngineArgs.create_engine_config "Permanent link")

```
create_engine_config(
    usage_context: UsageContext | None = None,
    headless: bool = False,
) -> VllmConfig
```

Create the VllmConfig.

NOTE: If VllmConfig is incompatible, we raise an error.

Source code in `vllm/engine/arg_utils.py`

```
defcreate_engine_config(
    self,
    usage_context: UsageContext | None = None,
    headless: bool = False,
) -> VllmConfig:
"""
    Create the VllmConfig.

    NOTE: If VllmConfig is incompatible, we raise an error.
    """
    current_platform.pre_register_and_update()

    device_config = DeviceConfig(device=cast(Device, current_platform.device_type))

    envs.validate_environ(self.fail_on_environ_validation)

    # Check if the model is a speculator and override model/tokenizer/config
    # BEFORE creating ModelConfig, so the config is created with the target model
    # Skip speculator detection for cloud storage models (eg: S3, GCS) since
    # HuggingFace cannot load configs directly from S3 URLs. S3 models can still
    # use speculators with explicit --speculative-config.
    if not is_cloud_storage(self.model):
        (self.model, self.tokenizer, self.speculative_config) = (
            maybe_override_with_speculators(
                model=self.model,
                tokenizer=self.tokenizer,
                revision=self.revision,
                trust_remote_code=self.trust_remote_code,
                vllm_speculative_config=self.speculative_config,
                hf_token=self.hf_token,
            )
        )

    model_config = self.create_model_config()
    self.model = model_config.model
    self.model_weights = model_config.model_weights
    self.tokenizer = model_config.tokenizer

    self._check_feature_supported()
    self._set_default_chunked_prefill_and_prefix_caching_args(model_config)
    self._set_default_reasoning_config_args()
    sliding_window: int | None = None
    if not is_interleaved(model_config.hf_text_config):
        # Only set CacheConfig.sliding_window if the model is all sliding
        # window. Otherwise CacheConfig.sliding_window will override the
        # global layers in interleaved sliding window models.
        sliding_window = model_config.get_sliding_window()

    # Resolve "auto" kv_cache_dtype to actual value from model config
    resolved_cache_dtype = resolve_kv_cache_dtype_string(
        self.kv_cache_dtype, model_config
    )

    assert self.enable_prefix_caching is not None, (
        "enable_prefix_caching must be set by this point"
    )

    cache_config = CacheConfig(
        block_size=self.block_size,  # type: ignore[arg-type]
        gpu_memory_utilization=self.gpu_memory_utilization,
        kv_cache_memory_bytes=self.kv_cache_memory_bytes,
        cache_dtype=resolved_cache_dtype,  # type: ignore[arg-type]
        is_attention_free=model_config.is_attention_free,
        num_gpu_blocks_override=self.num_gpu_blocks_override,
        sliding_window=sliding_window,
        enable_prefix_caching=self.enable_prefix_caching,
        prefix_caching_hash_algo=self.prefix_caching_hash_algo,
        calculate_kv_scales=self.calculate_kv_scales,
        kv_cache_dtype_skip_layers=self.kv_cache_dtype_skip_layers,
        kv_sharing_fast_prefill=self.kv_sharing_fast_prefill,
        mamba_cache_dtype=self.mamba_cache_dtype,
        mamba_ssm_cache_dtype=self.mamba_ssm_cache_dtype,
        mamba_block_size=self.mamba_block_size,
        mamba_cache_mode=self.mamba_cache_mode,
        kv_offloading_size=self.kv_offloading_size,
        kv_offloading_backend=self.kv_offloading_backend,
    )

    if resolved_cache_dtype.startswith("turboquant_"):
        fromvllm.model_executor.layers.quantization.turboquant.configimport (
            TurboQuantConfig,
        )

        boundary = TurboQuantConfig.get_boundary_skip_layers(model_config)
        existing = set(cache_config.kv_cache_dtype_skip_layers)
        cache_config.kv_cache_dtype_skip_layers = sorted(
            existing | set(boundary), key=int
        )

    ray_runtime_env = None
    if is_ray_initialized():
        # Ray Serve LLM calls `create_engine_config` in the context
        # of a Ray task, therefore we check is_ray_initialized()
        # as opposed to is_in_ray_actor().
        importray

        ray_runtime_env = ray.get_runtime_context().runtime_env
        # Avoid logging sensitive environment variables
        sanitized_env = ray_runtime_env.to_dict() if ray_runtime_env else {}
        if "env_vars" in sanitized_env:
            sanitized_env["env_vars"] = {
                k: "***" for k in sanitized_env["env_vars"]
            }
        logger.info("Using ray runtime env (env vars redacted): %s", sanitized_env)

    # Get the current placement group if Ray is initialized and
    # we are in a Ray actor. If so, then the placement group will be
    # passed to spawned processes.
    placement_group = None
    if is_in_ray_actor():
        importray

        # This call initializes Ray automatically if it is not initialized,
        # but we should not do this here.
        placement_group = ray.util.get_current_placement_group()

    assert not headless or not self.data_parallel_hybrid_lb, (
        "data_parallel_hybrid_lb is not applicable in headless mode"
    )
    assert not (self.data_parallel_hybrid_lb and self.data_parallel_external_lb), (
        "data_parallel_hybrid_lb and data_parallel_external_lb cannot both be True."
    )
    assert self.data_parallel_backend == "mp" or self.nnodes == 1, (
        "nnodes > 1 is only supported with data_parallel_backend=mp"
    )
    inferred_data_parallel_rank = 0
    if self.nnodes > 1:
        world_size = (
            self.data_parallel_size
            * self.pipeline_parallel_size
            * self.tensor_parallel_size
        )
        world_size_within_dp = (
            self.pipeline_parallel_size * self.tensor_parallel_size
        )
        local_world_size = world_size // self.nnodes
        assert world_size % self.nnodes == 0, (
            f"world_size={world_size} must be divisible by nnodes={self.nnodes}."
        )
        assert self.node_rank < self.nnodes, (
            f"node_rank={self.node_rank} must be less than nnodes={self.nnodes}."
        )
        inferred_data_parallel_rank = (
            self.node_rank * local_world_size
        ) // world_size_within_dp
        if self.data_parallel_size > 1 and self.data_parallel_external_lb:
            self.data_parallel_rank = inferred_data_parallel_rank
            logger.info(
                "Inferred data_parallel_rank %d from node_rank %d for external lb",
                self.data_parallel_rank,
                self.node_rank,
            )
        elif self.data_parallel_size_local is None:
            # Infer data parallel size local for internal dplb:
            self.data_parallel_size_local = max(
                local_world_size // world_size_within_dp, 1
            )
    data_parallel_external_lb = (
        self.data_parallel_external_lb or self.data_parallel_rank is not None
    )
    if (
        self.data_parallel_size > 1
        and data_parallel_external_lb
        and not model_config.is_moe
    ):
        raise ValueError(
            "Non-MoE models do not support external data parallel mode. "
            "For external load balancing, launch independent vLLM "
            "instances without --data-parallel-* arguments."
        )
    # Local DP rank = 1, use pure-external LB.
    if data_parallel_external_lb:
        assert self.data_parallel_rank is not None, (
            "data_parallel_rank or node_rank must be specified if "
            "data_parallel_external_lb is enable."
        )
        assert self.data_parallel_size_local in (1, None), (
            "data_parallel_size_local must be 1 or None when data_parallel_rank "
            "is set"
        )
        data_parallel_size_local = 1
        # Use full external lb if we have local_size of 1.
        self.data_parallel_hybrid_lb = False
    elif self.data_parallel_size_local is not None:
        data_parallel_size_local = self.data_parallel_size_local

        if self.data_parallel_start_rank and not headless:
            # Infer hybrid LB mode.
            self.data_parallel_hybrid_lb = True

        if self.data_parallel_hybrid_lb and data_parallel_size_local == 1:
            # Use full external lb if we have local_size of 1.
            logger.warning(
                "data_parallel_hybrid_lb is not eligible when "
                "data_parallel_size_local = 1, autoswitch to "
                "data_parallel_external_lb."
            )
            data_parallel_external_lb = True
            self.data_parallel_hybrid_lb = False

        if data_parallel_size_local == self.data_parallel_size:
            # Disable hybrid LB mode if set for a single node
            self.data_parallel_hybrid_lb = False

        self.data_parallel_rank = (
            self.data_parallel_start_rank or inferred_data_parallel_rank
        )
        if self.nnodes > 1:
            logger.info(
                "Inferred data_parallel_rank %d from node_rank %d",
                self.data_parallel_rank,
                self.node_rank,
            )
    else:
        assert not self.data_parallel_hybrid_lb, (
            "data_parallel_size_local must be set to use data_parallel_hybrid_lb."
        )

        if self.data_parallel_backend == "ray" and (
            envs.VLLM_RAY_DP_PACK_STRATEGY == "span"
        ):
            # Data parallel size defaults to 1 if DP ranks are spanning
            # multiple nodes
            data_parallel_size_local = 1
        else:
            # Otherwise local DP size defaults to global DP size if not set
            data_parallel_size_local = self.data_parallel_size

    # DP address, used in multi-node case for torch distributed group
    # and ZMQ sockets.
    if self.data_parallel_address is None:
        if self.data_parallel_backend == "ray":
            host_ip = get_ip()
            logger.info(
                "Using host IP %s as ray-based data parallel address", host_ip
            )
            data_parallel_address = host_ip
        else:
            assert self.data_parallel_backend == "mp", (
                "data_parallel_backend can only be ray or mp, got %s",
                self.data_parallel_backend,
            )
            data_parallel_address = (
                self.master_addr or ParallelConfig.data_parallel_master_ip
            )
    else:
        data_parallel_address = self.data_parallel_address

    # This port is only used when there are remote data parallel engines,
    # otherwise the local IPC transport is used.
    data_parallel_rpc_port = (
        self.data_parallel_rpc_port
        if (self.data_parallel_rpc_port is not None)
        else ParallelConfig.data_parallel_rpc_port
    )

    if self.tokens_only and not model_config.skip_tokenizer_init:
        model_config.skip_tokenizer_init = True
        logger.info("Skipping tokenizer initialization for tokens-only mode.")

    parallel_config = ParallelConfig(
        pipeline_parallel_size=self.pipeline_parallel_size,
        tensor_parallel_size=self.tensor_parallel_size,
        prefill_context_parallel_size=self.prefill_context_parallel_size,
        data_parallel_size=self.data_parallel_size,
        data_parallel_rank=self.data_parallel_rank or 0,
        data_parallel_external_lb=data_parallel_external_lb,
        data_parallel_size_local=data_parallel_size_local,
        master_addr=self.master_addr,
        master_port=self.master_port,
        nnodes=self.nnodes,
        node_rank=self.node_rank,
        distributed_timeout_seconds=self.distributed_timeout_seconds,
        data_parallel_master_ip=data_parallel_address,
        data_parallel_rpc_port=data_parallel_rpc_port,
        data_parallel_backend=self.data_parallel_backend,
        data_parallel_hybrid_lb=self.data_parallel_hybrid_lb,
        is_moe_model=model_config.is_moe,
        enable_expert_parallel=self.enable_expert_parallel,
        enable_ep_weight_filter=self.enable_ep_weight_filter,
        all2all_backend=self.all2all_backend,
        enable_elastic_ep=self.enable_elastic_ep,
        enable_dbo=self.enable_dbo,
        ubatch_size=self.ubatch_size,
        dbo_decode_token_threshold=self.dbo_decode_token_threshold,
        dbo_prefill_token_threshold=self.dbo_prefill_token_threshold,
        disable_nccl_for_dp_synchronization=self.disable_nccl_for_dp_synchronization,
        enable_eplb=self.enable_eplb,
        eplb_config=self.eplb_config,
        expert_placement_strategy=self.expert_placement_strategy,
        max_parallel_loading_workers=self.max_parallel_loading_workers,
        disable_custom_all_reduce=self.disable_custom_all_reduce,
        ray_workers_use_nsight=self.ray_workers_use_nsight,
        ray_runtime_env=ray_runtime_env,
        placement_group=placement_group,
        distributed_executor_backend=self.distributed_executor_backend,
        worker_cls=self.worker_cls,
        worker_extension_cls=self.worker_extension_cls,
        decode_context_parallel_size=self.decode_context_parallel_size,
        dcp_comm_backend=self.dcp_comm_backend,
        dcp_kv_cache_interleave_size=self.dcp_kv_cache_interleave_size,
        cp_kv_cache_interleave_size=self.cp_kv_cache_interleave_size,
        _api_process_count=self._api_process_count,
        _api_process_rank=self._api_process_rank,
        numa_bind=self.numa_bind,
        numa_bind_nodes=self.numa_bind_nodes,
        numa_bind_cpus=self.numa_bind_cpus,
    )

    speculative_config = self.create_speculative_config(
        target_model_config=model_config,
        target_parallel_config=parallel_config,
    )

    self._set_default_max_num_seqs_and_batched_tokens_args(
        usage_context,
        model_config,
        parallel_config,
    )

    assert self.max_num_batched_tokens is not None, (
        "max_num_batched_tokens must be set by this point"
    )
    assert self.max_num_seqs is not None, "max_num_seqs must be set by this point"
    assert self.enable_chunked_prefill is not None, (
        "enable_chunked_prefill must be set by this point"
    )
    assert model_config.max_model_len is not None, (
        "max_model_len must be set by this point"
    )
    scheduler_config = SchedulerConfig(
        runner_type=model_config.runner_type,
        max_num_batched_tokens=self.max_num_batched_tokens,
        max_num_seqs=self.max_num_seqs,
        max_model_len=model_config.max_model_len,
        enable_chunked_prefill=self.enable_chunked_prefill,
        disable_chunked_mm_input=self.disable_chunked_mm_input,
        is_multimodal_model=model_config.is_multimodal_model,
        is_encoder_decoder=model_config.is_encoder_decoder,
        policy=self.scheduling_policy,
        scheduler_cls=self.scheduler_cls,
        max_num_partial_prefills=self.max_num_partial_prefills,
        max_long_partial_prefills=self.max_long_partial_prefills,
        long_prefill_token_threshold=self.long_prefill_token_threshold,
        scheduler_reserve_full_isl=self.scheduler_reserve_full_isl,
        disable_hybrid_kv_cache_manager=self.disable_hybrid_kv_cache_manager,
        async_scheduling=self.async_scheduling,
        stream_interval=self.stream_interval,
    )

    if not model_config.is_multimodal_model and self.default_mm_loras:
        raise ValueError(
            "Default modality-specific LoRA(s) were provided for a "
            "non multimodal model"
        )

    lora_config = (
        LoRAConfig(
            max_lora_rank=self.max_lora_rank,
            max_loras=self.max_loras,
            default_mm_loras=self.default_mm_loras,
            fully_sharded_loras=self.fully_sharded_loras,
            lora_dtype=self.lora_dtype,
            target_modules=self.lora_target_modules,
            enable_tower_connector_lora=self.enable_tower_connector_lora,
            specialize_active_lora=self.specialize_active_lora,
            max_cpu_loras=self.max_cpu_loras
            if self.max_cpu_loras and self.max_cpu_loras > 0
            else None,
        )
        if self.enable_lora
        else None
    )

    if (
        lora_config is not None
        and speculative_config is not None
        and scheduler_config.max_num_batched_tokens
        < (
            scheduler_config.max_num_seqs
            * (speculative_config.num_speculative_tokens + 1)
        )
    ):
        raise ValueError(
            "Consider increasing max_num_batched_tokens or "
            "decreasing num_speculative_tokens"
        )

    # bitsandbytes pre-quantized model need a specific model loader
    if model_config.quantization == "bitsandbytes":
        self.quantization = self.load_format = "bitsandbytes"

    # Attention config overrides
    attention_config = copy.deepcopy(self.attention_config)
    if self.attention_backend is not None:
        if attention_config.backend is not None:
            raise ValueError(
                "attention_backend and attention_config.backend "
                "are mutually exclusive"
            )
        # Reuse the validator to handle "auto" and string-to-enum conversion
        attention_config.backend = AttentionConfig.validate_backend_before(
            self.attention_backend
        )

    # TurboQuant requires FlashAttention 2 — FA3 boundary layers assert
    # FlashAttentionImpl which fails with TurboQuantAttentionImpl.
    if resolved_cache_dtype.startswith("turboquant_") and (
        attention_config.flash_attn_version is None
        or attention_config.flash_attn_version >= 3
    ):
        logger.warning(
            "TurboQuant is not yet compatible with FlashAttention >= 3. "
            "Overriding flash_attn_version to 2. To silence this "
            "warning, pass --attention-config.flash_attn_version=2"
        )
        attention_config.flash_attn_version = 2

    # Mamba config overrides
    mamba_config = copy.deepcopy(self.mamba_config)
    # Convert string to enum if needed (CLI parsing returns a string)
    if isinstance(self.mamba_backend, str):
        mamba_config.backend = MambaBackendEnum[self.mamba_backend.upper()]
    else:
        mamba_config.backend = self.mamba_backend
    if self.enable_mamba_cache_stochastic_rounding:
        mamba_config.enable_stochastic_rounding = (
            self.enable_mamba_cache_stochastic_rounding
        )
    if self.mamba_cache_philox_rounds:
        mamba_config.stochastic_rounding_philox_rounds = (
            self.mamba_cache_philox_rounds
        )

    # Kernel config overrides
    kernel_config = copy.deepcopy(self.kernel_config)
    if self.enable_flashinfer_autotune is not None:
        if kernel_config.enable_flashinfer_autotune is not None:
            raise ValueError(
                "enable_flashinfer_autotune and "
                "kernel_config.enable_flashinfer_autotune "
                "are mutually exclusive"
            )
        kernel_config.enable_flashinfer_autotune = self.enable_flashinfer_autotune
    if self.moe_backend != "auto":
        kernel_config.moe_backend = self.moe_backend

    # Transfer top-level ir_op_priority into KernelConfig.ir_op_priority
    for op_name, op_priority in asdict(self.ir_op_priority).items():
        # Empty means unset
        if not op_priority:
            continue

        # Priority cannot be set 2x for the same op
        if getattr(kernel_config.ir_op_priority, op_name):
            raise ValueError(
                f"Op priority for {op_name} specified via both ir_op_priority "
                f"and KernelConfig.ir_op_priority, only one allowed at a time."
            )

        # Set the attribute
        setattr(kernel_config.ir_op_priority, op_name, op_priority)

    load_config = self.create_load_config()

    # Pass reasoning_parser into StructuredOutputsConfig
    if self.reasoning_parser:
        self.structured_outputs_config.reasoning_parser = self.reasoning_parser

    if self.reasoning_parser_plugin:
        self.structured_outputs_config.reasoning_parser_plugin = (
            self.reasoning_parser_plugin
        )

    observability_config = ObservabilityConfig(
        show_hidden_metrics_for_version=self.show_hidden_metrics_for_version,
        otlp_traces_endpoint=self.otlp_traces_endpoint,
        collect_detailed_traces=self.collect_detailed_traces,
        kv_cache_metrics=self.kv_cache_metrics,
        kv_cache_metrics_sample=self.kv_cache_metrics_sample,
        cudagraph_metrics=self.cudagraph_metrics,
        enable_layerwise_nvtx_tracing=self.enable_layerwise_nvtx_tracing,
        enable_mfu_metrics=self.enable_mfu_metrics,
        enable_mm_processor_stats=self.enable_mm_processor_stats,
        enable_logging_iteration_details=self.enable_logging_iteration_details,
    )

    # Compilation config overrides
    compilation_config = copy.deepcopy(self.compilation_config)
    if self.cudagraph_capture_sizes is not None:
        if compilation_config.cudagraph_capture_sizes is not None:
            raise ValueError(
                "cudagraph_capture_sizes and compilation_config."
                "cudagraph_capture_sizes are mutually exclusive"
            )
        compilation_config.cudagraph_capture_sizes = self.cudagraph_capture_sizes
    if self.max_cudagraph_capture_size is not None:
        if compilation_config.max_cudagraph_capture_size is not None:
            raise ValueError(
                "max_cudagraph_capture_size and compilation_config."
                "max_cudagraph_capture_size are mutually exclusive"
            )
        compilation_config.max_cudagraph_capture_size = (
            self.max_cudagraph_capture_size
        )

    offload_config = OffloadConfig(
        offload_backend=self.offload_backend,
        uva=UVAOffloadConfig(
            cpu_offload_gb=self.cpu_offload_gb,
            cpu_offload_params=self.cpu_offload_params,
        ),
        prefetch=PrefetchOffloadConfig(
            offload_group_size=self.offload_group_size,
            offload_num_in_group=self.offload_num_in_group,
            offload_prefetch_step=self.offload_prefetch_step,
            offload_params=self.offload_params,
        ),
    )

    if self.gdn_prefill_backend is not None:
        self.additional_config["gdn_prefill_backend"] = self.gdn_prefill_backend

    config = VllmConfig(
        model_config=model_config,
        cache_config=cache_config,
        parallel_config=parallel_config,
        scheduler_config=scheduler_config,
        device_config=device_config,
        load_config=load_config,
        offload_config=offload_config,
        attention_config=attention_config,
        mamba_config=mamba_config,
        kernel_config=kernel_config,
        lora_config=lora_config,
        speculative_config=speculative_config,
        structured_outputs_config=self.structured_outputs_config,
        observability_config=observability_config,
        compilation_config=compilation_config,
        kv_transfer_config=self.kv_transfer_config,
        kv_events_config=self.kv_events_config,
        ec_transfer_config=self.ec_transfer_config,
        reasoning_config=self.reasoning_config,
        profiler_config=self.profiler_config,
        additional_config=self.additional_config,
        optimization_level=self.optimization_level,
        performance_mode=self.performance_mode,
        weight_transfer_config=self.weight_transfer_config,
        shutdown_timeout=self.shutdown_timeout,
    )

    return config
```

### create\_speculative\_config [¶](#vllm.EngineArgs.create_speculative_config "Permanent link")

Initializes and returns a SpeculativeConfig object based on `speculative_config`.

This function utilizes `speculative_config` to create a SpeculativeConfig object. The `speculative_config` can either be provided as a JSON string input via CLI arguments or directly as a dictionary from the engine.

Source code in `vllm/engine/arg_utils.py`

```
defcreate_speculative_config(
    self,
    target_model_config: ModelConfig,
    target_parallel_config: ParallelConfig,
) -> SpeculativeConfig | None:
"""Initializes and returns a SpeculativeConfig object based on
    `speculative_config`.

    This function utilizes `speculative_config` to create a
    SpeculativeConfig object. The `speculative_config` can either be
    provided as a JSON string input via CLI arguments or directly as a
    dictionary from the engine.
    """
    if self.speculative_config is None:
        return None

    # Note(Shangming): These parameters are not obtained from the cli arg
    # '--speculative-config' and must be passed in when creating the engine
    # config.
    self.speculative_config.update(
        {
            "target_model_config": target_model_config,
            "target_parallel_config": target_parallel_config,
        }
    )
    return SpeculativeConfig(**self.speculative_config)
```

## LLM [¶](#vllm.LLM "Permanent link")

An LLM for generating texts from given prompts and sampling parameters.

This class includes a tokenizer, a language model (possibly distributed across multiple GPUs), and GPU memory space allocated for intermediate states (aka KV cache). Given a batch of prompts and sampling parameters, this class generates texts from the model, using an intelligent batching mechanism and efficient memory management.

Parameters:

Name Type Description Default `model` `str`

The name or path of a HuggingFace Transformers model.

*required* `tokenizer` `str | None`

The name or path of a HuggingFace Transformers tokenizer.

`None` `tokenizer_mode` `TokenizerMode | str`

The tokenizer mode. "auto" will use the fast tokenizer if available, and "slow" will always use the slow tokenizer.

`'auto'` `skip_tokenizer_init` `bool`

If true, skip initialization of tokenizer and detokenizer. Expect valid prompt\_token\_ids and None for prompt from the input.

`False` `trust_remote_code` `bool`

Trust remote code (e.g., from HuggingFace) when downloading the model and tokenizer.

`False` `allowed_local_media_path` `str`

Allowing API requests to read local images or videos from directories specified by the server file system. This is a security risk. Should only be enabled in trusted environments.

`''` `allowed_media_domains` `list[str] | None`

If set, only media URLs that belong to this domain can be used for multi-modal inputs.

`None` `tensor_parallel_size` `int`

The number of GPUs to use for distributed execution with tensor parallelism.

`1` `dtype` `ModelDType`

The data type for the model weights and activations. Currently, we support `float32`, `float16`, and `bfloat16`. If `auto`, we use the `dtype` attribute of the Transformers model's config. However, if the `dtype` in the config is `float32`, we will use `float16` instead.

`'auto'` `quantization` `QuantizationMethods | None`

The method used to quantize the model weights. Currently, we support "awq", "gptq", and "fp8" (experimental). If None, we first check the `quantization_config` attribute in the model config file. If that is None, we assume the model weights are not quantized and use `dtype` to determine the data type of the weights.

`None` `revision` `str | None`

The specific model version to use. It can be a branch name, a tag name, or a commit id.

`None` `tokenizer_revision` `str | None`

The specific tokenizer version to use. It can be a branch name, a tag name, or a commit id.

`None` `chat_template` `Path | str | None`

The chat template to apply.

`None` `seed` `int`

The seed to initialize the random number generator for sampling.

`0` `gpu_memory_utilization` `float`

The ratio (between 0 and 1) of GPU memory to reserve for the model weights, activations, and KV cache. Higher values will increase the KV cache size and thus improve the model's throughput. However, if the value is too high, it may cause out-of- memory (OOM) errors.

`0.92` `kv_cache_memory_bytes` `int | None`

Size of KV Cache per GPU in bytes. By default, this is set to None and vllm can automatically infer the kv cache size based on gpu\_memory\_utilization. However, users may want to manually specify the kv cache memory size. kv\_cache\_memory\_bytes allows more fine-grain control of how much memory gets used when compared with using gpu\_memory\_utilization. Note that kv\_cache\_memory\_bytes (when not-None) ignores gpu\_memory\_utilization

`None` `cpu_offload_gb` `float`

The size (GiB) of CPU memory to use for offloading the model weights. This virtually increases the GPU memory space you can use to hold the model weights, at the cost of CPU-GPU data transfer for every forward pass.

`0` `offload_group_size` `int`

Prefetch offloading: Group every N layers together. Offload last `offload_num_in_group` layers of each group. Default is 0 (disabled).

`0` `offload_num_in_group` `int`

Prefetch offloading: Number of layers to offload per group. Default is 1.

`1` `offload_prefetch_step` `int`

Prefetch offloading: Number of layers to prefetch ahead. Higher values hide more latency but use more GPU memory. Default is 1.

`1` `offload_params` `set[str] | None`

Prefetch offloading: Set of parameter name segments to selectively offload. Only parameters whose names contain one of these segments will be offloaded (e.g., {"gate\_up\_proj", "down\_proj"} for MLP weights, or {"w13\_weight", "w2\_weight"} for MoE expert weights). If None or empty, all parameters are offloaded.

`None` `enforce_eager` `bool`

Whether to enforce eager execution. If True, we will disable CUDA graph and always execute the model in eager mode. If False, we will use CUDA graph and eager execution in hybrid.

`False` `enable_return_routed_experts` `bool`

Whether to return routed experts.

`False` `disable_custom_all_reduce` `bool`

See [ParallelConfig](https://docs.vllm.ai/en/latest/api/vllm/config/#vllm.config.ParallelConfig "            ParallelConfig").

`False` `hf_token` `bool | str | None`

The token to use as HTTP bearer authorization for remote files . If `True`, will use the token generated when running `hf auth login` (stored in `~/.cache/huggingface/token`).

`None` `hf_overrides` `HfOverrides | None`

If a dictionary, contains arguments to be forwarded to the HuggingFace config. If a callable, it is called to update the HuggingFace config.

`None` `mm_processor_kwargs` `dict[str, Any] | None`

Arguments to be forwarded to the model's processor for multi-modal data, e.g., image processor. Overrides for the multi-modal processor obtained from `AutoProcessor.from_pretrained`. The available overrides depend on the model that is being run. For example, for Phi-3-Vision: `{"num_crops": 4}`.

`None` `pooler_config` `PoolerConfig | None`

Initialize non-default pooling config for the pooling model, e.g., `PoolerConfig(seq_pooling_type="MEAN", use_activation=False)`.

`None` `compilation_config` `int | dict[str, Any] | CompilationConfig | None`

Either an integer or a dictionary. If it is an integer, it is used as the mode of compilation optimization. If it is a dictionary, it can specify the full compilation configuration.

`None` `attention_config` `dict[str, Any] | AttentionConfig | None`

Configuration for attention mechanisms. Can be a dictionary or an AttentionConfig instance. If a dictionary, it will be converted to an AttentionConfig. Allows specifying the attention backend and other attention-related settings.

`None` `**kwargs` `Any`

Arguments for [`EngineArgs`](#vllm.EngineArgs "            EngineArgs            dataclass   ").

`{}`

Note

This class is intended to be used for offline inference. For online serving, use the [AsyncLLMEngine](#vllm.AsyncLLMEngine "            AsyncLLMEngine            module-attribute   ") class instead.

Source code in `vllm/entrypoints/llm.py`

```
classLLM:
"""An LLM for generating texts from given prompts and sampling parameters.

    This class includes a tokenizer, a language model (possibly distributed
    across multiple GPUs), and GPU memory space allocated for intermediate
    states (aka KV cache). Given a batch of prompts and sampling parameters,
    this class generates texts from the model, using an intelligent batching
    mechanism and efficient memory management.

    Args:
        model: The name or path of a HuggingFace Transformers model.
        tokenizer: The name or path of a HuggingFace Transformers tokenizer.
        tokenizer_mode: The tokenizer mode. "auto" will use the fast tokenizer
            if available, and "slow" will always use the slow tokenizer.
        skip_tokenizer_init: If true, skip initialization of tokenizer and
            detokenizer. Expect valid prompt_token_ids and None for prompt
            from the input.
        trust_remote_code: Trust remote code (e.g., from HuggingFace) when
            downloading the model and tokenizer.
        allowed_local_media_path: Allowing API requests to read local images
            or videos from directories specified by the server file system.
            This is a security risk. Should only be enabled in trusted
            environments.
        allowed_media_domains: If set, only media URLs that belong to this
            domain can be used for multi-modal inputs.
        tensor_parallel_size: The number of GPUs to use for distributed
            execution with tensor parallelism.
        dtype: The data type for the model weights and activations. Currently,
            we support `float32`, `float16`, and `bfloat16`. If `auto`, we use
            the `dtype` attribute of the Transformers model's config. However,
            if the `dtype` in the config is `float32`, we will use `float16` instead.
        quantization: The method used to quantize the model weights. Currently,
            we support "awq", "gptq", and "fp8" (experimental).
            If None, we first check the `quantization_config` attribute in the
            model config file. If that is None, we assume the model weights are
            not quantized and use `dtype` to determine the data type of
            the weights.
        revision: The specific model version to use. It can be a branch name,
            a tag name, or a commit id.
        tokenizer_revision: The specific tokenizer version to use. It can be a
            branch name, a tag name, or a commit id.
        chat_template: The chat template to apply.
        seed: The seed to initialize the random number generator for sampling.
        gpu_memory_utilization: The ratio (between 0 and 1) of GPU memory to
            reserve for the model weights, activations, and KV cache. Higher
            values will increase the KV cache size and thus improve the model's
            throughput. However, if the value is too high, it may cause out-of-
            memory (OOM) errors.
        kv_cache_memory_bytes: Size of KV Cache per GPU in bytes. By default,
            this is set to None and vllm can automatically infer the kv cache
            size based on gpu_memory_utilization. However, users may want to
            manually specify the kv cache memory size. kv_cache_memory_bytes
            allows more fine-grain control of how much memory gets used when
            compared with using gpu_memory_utilization. Note that
            kv_cache_memory_bytes (when not-None) ignores
            gpu_memory_utilization
        cpu_offload_gb: The size (GiB) of CPU memory to use for offloading
            the model weights. This virtually increases the GPU memory space
            you can use to hold the model weights, at the cost of CPU-GPU data
            transfer for every forward pass.
        offload_group_size: Prefetch offloading: Group every N layers
            together. Offload last `offload_num_in_group` layers of each group.
            Default is 0 (disabled).
        offload_num_in_group: Prefetch offloading: Number of layers to
            offload per group. Default is 1.
        offload_prefetch_step: Prefetch offloading: Number of layers to
            prefetch ahead. Higher values hide more latency but use more GPU
            memory. Default is 1.
        offload_params: Prefetch offloading: Set of parameter name segments
            to selectively offload. Only parameters whose names contain one of
            these segments will be offloaded (e.g., {"gate_up_proj", "down_proj"}
            for MLP weights, or {"w13_weight", "w2_weight"} for MoE expert
            weights). If None or empty, all parameters are offloaded.
        enforce_eager: Whether to enforce eager execution. If True, we will
            disable CUDA graph and always execute the model in eager mode.
            If False, we will use CUDA graph and eager execution in hybrid.
        enable_return_routed_experts: Whether to return routed experts.
        disable_custom_all_reduce: See
            [ParallelConfig][vllm.config.ParallelConfig].
        hf_token: The token to use as HTTP bearer authorization for remote files
            . If `True`, will use the token generated when running
            `hf auth login` (stored in `~/.cache/huggingface/token`).
        hf_overrides: If a dictionary, contains arguments to be forwarded to the
            HuggingFace config. If a callable, it is called to update the
            HuggingFace config.
        mm_processor_kwargs: Arguments to be forwarded to the model's processor
            for multi-modal data, e.g., image processor. Overrides for the
            multi-modal processor obtained from `AutoProcessor.from_pretrained`.
            The available overrides depend on the model that is being run.
            For example, for Phi-3-Vision: `{"num_crops": 4}`.
        pooler_config: Initialize non-default pooling config for the pooling model,
            e.g., `PoolerConfig(seq_pooling_type="MEAN", use_activation=False)`.
        compilation_config: Either an integer or a dictionary. If it is an
            integer, it is used as the mode of compilation optimization. If it
            is a dictionary, it can specify the full compilation configuration.
        attention_config: Configuration for attention mechanisms. Can be a
            dictionary or an AttentionConfig instance. If a dictionary, it will
            be converted to an AttentionConfig. Allows specifying the attention
            backend and other attention-related settings.
        **kwargs: Arguments for [`EngineArgs`][vllm.EngineArgs].

    Note:
        This class is intended to be used for offline inference. For online
        serving, use the [AsyncLLMEngine][vllm.AsyncLLMEngine] class instead.
    """

    def__init__(
        self,
        model: str,
        *,
        runner: RunnerOption = "auto",
        convert: ConvertOption = "auto",
        tokenizer: str | None = None,
        tokenizer_mode: TokenizerMode | str = "auto",
        skip_tokenizer_init: bool = False,
        trust_remote_code: bool = False,
        allowed_local_media_path: str = "",
        allowed_media_domains: list[str] | None = None,
        tensor_parallel_size: int = 1,
        dtype: ModelDType = "auto",
        quantization: QuantizationMethods | None = None,
        revision: str | None = None,
        tokenizer_revision: str | None = None,
        chat_template: Path | str | None = None,
        seed: int = 0,
        gpu_memory_utilization: float = 0.92,
        cpu_offload_gb: float = 0,
        offload_group_size: int = 0,
        offload_num_in_group: int = 1,
        offload_prefetch_step: int = 1,
        offload_params: set[str] | None = None,
        enforce_eager: bool = False,
        enable_return_routed_experts: bool = False,
        disable_custom_all_reduce: bool = False,
        hf_token: bool | str | None = None,
        hf_overrides: HfOverrides | None = None,
        mm_processor_kwargs: dict[str, Any] | None = None,
        pooler_config: PoolerConfig | None = None,
        structured_outputs_config: dict[str, Any]
        | StructuredOutputsConfig
        | None = None,
        profiler_config: dict[str, Any] | ProfilerConfig | None = None,
        attention_config: dict[str, Any] | AttentionConfig | None = None,
        kv_cache_memory_bytes: int | None = None,
        compilation_config: int | dict[str, Any] | CompilationConfig | None = None,
        quantization_config: dict[str, Any]
        | OnlineQuantizationConfigArgs
        | None = None,
        logits_processors: list[str | type[LogitsProcessor]] | None = None,
        **kwargs: Any,
    ) -> None:
"""LLM constructor."""

        if "swap_space" in kwargs:
            kwargs.pop("swap_space")
            importwarnings

            warnings.warn(
                "The 'swap_space' parameter is deprecated and ignored. "
                "It will be removed in a future version.",
                DeprecationWarning,
                stacklevel=2,
            )

        if "disable_log_stats" not in kwargs:
            kwargs["disable_log_stats"] = True

        if "worker_cls" in kwargs:
            worker_cls = kwargs["worker_cls"]
            # if the worker_cls is not qualified string name,
            # we serialize it using cloudpickle to avoid pickling issues
            if isinstance(worker_cls, type):
                kwargs["worker_cls"] = cloudpickle.dumps(worker_cls)

        if "kv_transfer_config" in kwargs and isinstance(
            kwargs["kv_transfer_config"], dict
        ):
            fromvllm.config.kv_transferimport KVTransferConfig

            raw_config_dict = kwargs["kv_transfer_config"]
            try:
                kwargs["kv_transfer_config"] = KVTransferConfig(**raw_config_dict)
            except ValidationError as e:
                logger.error(
                    "Failed to convert 'kv_transfer_config' dict to "
                    "KVTransferConfig object. Dict: %s. Error: %s",
                    raw_config_dict,
                    e,
                )
                # Consider re-raising a more specific vLLM error or ValueError
                # to provide better context to the user.
                raise ValueError(f"Invalid 'kv_transfer_config' provided: {e}") frome

        if hf_overrides is None:
            hf_overrides = {}

        def_make_config(value: Any, cls: type[_R]) -> _R:
"""Convert dict/None/instance to a config instance."""
            if value is None:
                return cls()
            if isinstance(value, dict):
                return cls(**{k: v for k, v in value.items() if is_init_field(cls, k)})  # type: ignore[arg-type]
            return value

        if isinstance(compilation_config, int):
            compilation_config_instance = CompilationConfig(
                mode=CompilationMode(compilation_config)
            )
        else:
            compilation_config_instance = _make_config(
                compilation_config, CompilationConfig
            )

        structured_outputs_instance = _make_config(
            structured_outputs_config, StructuredOutputsConfig
        )
        profiler_config_instance = _make_config(profiler_config, ProfilerConfig)
        attention_config_instance = _make_config(attention_config, AttentionConfig)

        # warn about single-process data parallel usage.
        _dp_size = int(kwargs.get("data_parallel_size", 1))
        _distributed_executor_backend = kwargs.get("distributed_executor_backend")
        if (
            _dp_size > 1
            and not _distributed_executor_backend == "external_launcher"
            and not current_platform.is_tpu()
        ):
            raise ValueError(
                f"LLM(data_parallel_size={_dp_size}) is not supported for single-"
                "process usage and may hang. Please use "
                "the explicit multi-process data-parallel example at "
                "'examples/features/data_parallel/data_parallel_offline.py'."
            )

        engine_args = EngineArgs(
            model=model,
            runner=runner,
            convert=convert,
            tokenizer=tokenizer,
            tokenizer_mode=tokenizer_mode,
            skip_tokenizer_init=skip_tokenizer_init,
            trust_remote_code=trust_remote_code,
            allowed_local_media_path=allowed_local_media_path,
            allowed_media_domains=allowed_media_domains,
            tensor_parallel_size=tensor_parallel_size,
            dtype=dtype,
            quantization=quantization,
            revision=revision,
            tokenizer_revision=tokenizer_revision,
            seed=seed,
            gpu_memory_utilization=gpu_memory_utilization,
            kv_cache_memory_bytes=kv_cache_memory_bytes,
            cpu_offload_gb=cpu_offload_gb,
            offload_group_size=offload_group_size,
            offload_num_in_group=offload_num_in_group,
            offload_prefetch_step=offload_prefetch_step,
            offload_params=offload_params or set(),
            enforce_eager=enforce_eager,
            enable_return_routed_experts=enable_return_routed_experts,
            disable_custom_all_reduce=disable_custom_all_reduce,
            hf_token=hf_token,
            hf_overrides=hf_overrides,
            mm_processor_kwargs=mm_processor_kwargs,
            pooler_config=pooler_config,
            structured_outputs_config=structured_outputs_instance,
            profiler_config=profiler_config_instance,
            attention_config=attention_config_instance,
            compilation_config=compilation_config_instance,
            quantization_config=quantization_config,
            logits_processors=logits_processors,
            **kwargs,
        )

        log_non_default_args(engine_args)

        self.llm_engine = LLMEngine.from_engine_args(
            engine_args=engine_args, usage_context=UsageContext.LLM_CLASS
        )
        self.model_config = self.llm_engine.model_config
        self.engine_class = type(self.llm_engine)

        self.request_counter = Counter()
        self.default_sampling_params: dict[str, Any] | None = None

        supported_tasks = self.llm_engine.get_supported_tasks()
        self.supported_tasks = supported_tasks
        self.pooling_task = self.model_config.get_pooling_task(supported_tasks)
        if self.pooling_task is not None:
            logger.info("Supported pooling task: %s", self.pooling_task)

        self.runner_type = self.model_config.runner_type
        self.renderer = self.llm_engine.renderer
        self.chat_template = load_chat_template(chat_template)
        self.input_processor = self.llm_engine.input_processor
        self.chat_template_config = ChatTemplateConfig(chat_template=self.chat_template)
        self.pooling_io_processors = init_pooling_io_processors(
            supported_tasks=supported_tasks,
            vllm_config=self.llm_engine.vllm_config,
            renderer=self.renderer,
            chat_template_config=self.chat_template_config,
        )
        # Cache for __repr__ to avoid repeated collective_rpc calls
        self._cached_repr: str | None = None

    @classmethod
    deffrom_engine_args(cls, engine_args: EngineArgs) -> "LLM":
"""Create an LLM instance from EngineArgs."""
        return cls(**vars(engine_args))

    defget_tokenizer(self) -> TokenizerLike:
        return self.llm_engine.get_tokenizer()

    defget_world_size(self, include_dp: bool = True) -> int:
"""Get the world size from the parallel config.

        Args:
            include_dp: If True (default), returns the world size including
                data parallelism (TP * PP * DP). If False, returns the world
                size without data parallelism (TP * PP).

        Returns:
            The world size (tensor_parallel_size * pipeline_parallel_size),
            optionally multiplied by data_parallel_size if include_dp is True.
        """
        parallel_config = self.llm_engine.vllm_config.parallel_config
        if include_dp:
            return parallel_config.world_size_across_dp
        return parallel_config.world_size

    defreset_mm_cache(self) -> None:
        self.renderer.clear_mm_cache()
        self.llm_engine.reset_mm_cache()

    defget_default_sampling_params(self) -> SamplingParams:
        if self.default_sampling_params is None:
            self.default_sampling_params = self.model_config.get_diff_sampling_param()
        if self.default_sampling_params:
            return SamplingParams.from_optional(**self.default_sampling_params)
        return SamplingParams()

    defgenerate(
        self,
        prompts: PromptType | Sequence[PromptType],
        sampling_params: SamplingParams | Sequence[SamplingParams] | None = None,
        *,
        use_tqdm: bool | Callable[..., tqdm] = True,
        lora_request: Sequence[LoRARequest] | LoRARequest | None = None,
        priority: list[int] | None = None,
        tokenization_kwargs: dict[str, Any] | None = None,
        mm_processor_kwargs: dict[str, Any] | None = None,
    ) -> list[RequestOutput]:
"""Generates the completions for the input prompts.

        This class automatically batches the given prompts, considering
        the memory constraint. For the best performance, put all of your prompts
        into a single list and pass it to this method.

        Args:
            prompts: The prompts to the LLM. You may pass a sequence of prompts
                for batch inference. See [PromptType][vllm.inputs.PromptType]
                for more details about the format of each prompt.
            sampling_params: The sampling parameters for text generation. If
                None, we use the default sampling parameters.
                When it is a single value, it is applied to every prompt.
                When it is a list, the list must have the same length as the
                prompts and it is paired one by one with the prompt.
            use_tqdm: If `True`, shows a tqdm progress bar.
                If a callable (e.g., `functools.partial(tqdm, leave=False)`),
                it is used to create the progress bar.
                If `False`, no progress bar is created.
            lora_request: LoRA request to use for generation, if any.
            priority: The priority of the requests, if any.
                Only applicable when priority scheduling policy is enabled.
                If provided, must be a list of integers matching the length
                of `prompts`, where each priority value corresponds to the prompt
                at the same index.
            tokenization_kwargs: Overrides for `tokenizer.encode`.
            mm_processor_kwargs: Overrides for `processor.__call__`.

        Returns:
            A list of `RequestOutput` objects containing the
            generated completions in the same order as the input prompts.
        """
        runner_type = self.model_config.runner_type
        if runner_type != "generate":
            raise ValueError(
                "LLM.generate() is only supported for generative models. "
                "Try passing `--runner generate` to use the model as a "
                "generative model."
            )

        if sampling_params is None:
            sampling_params = self.get_default_sampling_params()

        return self._run_completion(
            prompts=prompts,
            params=sampling_params,
            output_type=RequestOutput,
            use_tqdm=use_tqdm,
            lora_request=lora_request,
            tokenization_kwargs=tokenization_kwargs,
            priority=priority,
            mm_processor_kwargs=mm_processor_kwargs,
        )

    defenqueue(
        self,
        prompts: PromptType | Sequence[PromptType],
        sampling_params: SamplingParams | Sequence[SamplingParams] | None = None,
        lora_request: Sequence[LoRARequest] | LoRARequest | None = None,
        priority: list[int] | None = None,
        use_tqdm: bool | Callable[..., tqdm] = True,
        tokenization_kwargs: dict[str, Any] | None = None,
        mm_processor_kwargs: dict[str, Any] | None = None,
    ) -> list[str]:
"""Enqueue prompts for generation without waiting for completion.

        This method adds requests to the engine queue but does not start
        processing them. Use wait_for_completion() to process the queued
        requests and get results.

        Args:
            prompts: The prompts to the LLM. See generate() for details.
            sampling_params: The sampling parameters for text generation.
            lora_request: LoRA request to use for generation, if any.
            priority: The priority of the requests, if any.
            use_tqdm: If True, shows a tqdm progress bar while adding requests.
            tokenization_kwargs: Overrides for `tokenizer.encode`.
            mm_processor_kwargs: Overrides for `processor.__call__`.

        Returns:
            A list of request IDs for the enqueued requests.
        """
        runner_type = self.model_config.runner_type
        if runner_type != "generate":
            raise ValueError("LLM.enqueue() is only supported for generative models.")

        if sampling_params is None:
            sampling_params = self.get_default_sampling_params()

        return self._add_completion_requests(
            prompts=prompts,
            params=sampling_params,
            use_tqdm=use_tqdm,
            lora_request=lora_request,
            priority=priority,
            tokenization_kwargs=tokenization_kwargs,
            mm_processor_kwargs=mm_processor_kwargs,
        )

    @overload
    defwait_for_completion(
        self,
        *,
        use_tqdm: bool | Callable[..., tqdm] = True,
    ) -> list[RequestOutput | PoolingRequestOutput]: ...

    @overload
    defwait_for_completion(
        self,
        output_type: type[_O] | tuple[type[_O], ...],
        *,
        use_tqdm: bool | Callable[..., tqdm] = True,
    ) -> list[_O]: ...

    defwait_for_completion(
        self,
        output_type: type[Any] | tuple[type[Any], ...] | None = None,
        *,
        use_tqdm: bool | Callable[..., tqdm] = True,
    ) -> list[Any]:
"""Wait for all enqueued requests to complete and return results.

        This method processes all requests currently in the engine queue
        and returns their outputs. Use after enqueue() to get results.

        Args:
            output_type: The expected output type, defaults to RequestOutput.
            use_tqdm: If True, shows a tqdm progress bar.

        Returns:
            A list of output objects for all completed requests.
        """
        if output_type is None:
            output_type = (RequestOutput, PoolingRequestOutput)

        return self._run_engine(output_type, use_tqdm=use_tqdm)

    def_resolve_mm_lora(
        self,
        prompt: EngineInput,
        lora_request: LoRARequest | None,
    ) -> LoRARequest | None:
        if prompt["type"] != "multimodal":
            return lora_request

        lora_config = self.llm_engine.vllm_config.lora_config
        default_mm_loras = None if lora_config is None else lora_config.default_mm_loras
        if not default_mm_loras:
            return lora_request

        prompt_modalities = prompt["mm_placeholders"].keys()
        intersection = set(prompt_modalities).intersection(default_mm_loras.keys())
        if not intersection:
            return lora_request

        if len(intersection) > 1:
            # TODO: Would be nice to be able to have multiple loras per prompt
            logger.warning(
                "Multiple modality specific loras were registered and would be "
                "used by a single prompt consuming several modalities; "
                "currently we only support one lora per request; as such, "
                "lora(s) registered with modalities: %s will be skipped",
                intersection,
            )
            return lora_request

        # Build the LoRA request; the ID of the default mm lora is the
        # index of the modality name sorted alphabetically + 1.
        modality_name = intersection.pop()
        modality_lora_path = default_mm_loras[modality_name]
        modality_lora_id = sorted(default_mm_loras).index(modality_name) + 1

        # If we have a collision, warn if there is a collision,
        # but always send the explicitly provided request.
        if lora_request:
            if lora_request.lora_int_id != modality_lora_id:
                logger.warning(
                    "A modality with a registered lora and a lora_request "
                    "with a different ID were provided; falling back to the "
                    "lora_request as we only apply one LoRARequest per prompt"
                )
            return lora_request

        return LoRARequest(
            modality_name,
            modality_lora_id,
            modality_lora_path,
        )

    defcollective_rpc(
        self,
        method: str | Callable[..., _R],
        timeout: float | None = None,
        args: tuple = (),
        kwargs: dict[str, Any] | None = None,
    ) -> list[_R]:
"""
        Execute an RPC call on all workers.

        Args:
            method: Name of the worker method to execute, or a callable that
                is serialized and sent to all workers to execute.

                If the method is a callable, it should accept an additional
                `self` argument, in addition to the arguments passed in `args`
                and `kwargs`. The `self` argument will be the worker object.
            timeout: Maximum time in seconds to wait for execution. Raises a
                [`TimeoutError`][] on timeout. `None` means wait indefinitely.
            args: Positional arguments to pass to the worker method.
            kwargs: Keyword arguments to pass to the worker method.

        Returns:
            A list containing the results from each worker.

        Note:
            It is recommended to use this API to only pass control messages,
            and set up data-plane communication to pass data.
        """

        return self.llm_engine.collective_rpc(method, timeout, args, kwargs)

    defapply_model(self, func: Callable[[nn.Module], _R]) -> list[_R]:
"""
        Run a function directly on the model inside each worker,
        returning the result for each of them.

        !!! warning
            To reduce the overhead of data transfer, avoid returning large
            arrays or tensors from this method. If you must return them,
            make sure you move them to CPU first to avoid taking up additional
            VRAM!
        """
        return self.llm_engine.apply_model(func)

    defbeam_search(
        self,
        prompts: list[TokensPrompt | TextPrompt],
        params: BeamSearchParams,
        lora_request: list[LoRARequest] | LoRARequest | None = None,
        use_tqdm: bool = False,
        concurrency_limit: int | None = None,
    ) -> list[BeamSearchOutput]:
"""
        Generate sequences using beam search.

        Args:
            prompts: A list of prompts. Each prompt can be a string or a list
                of token IDs.
            params: The beam search parameters.
            lora_request: LoRA request to use for generation, if any.
            use_tqdm: Whether to use tqdm to display the progress bar.
            concurrency_limit: The maximum number of concurrent requests.
                If None, the number of concurrent requests is unlimited.
        """
        # TODO: how does beam search work together with length penalty,
        # frequency, penalty, and stopping criteria, etc.?
        beam_width = params.beam_width
        max_tokens = params.max_tokens
        temperature = params.temperature
        ignore_eos = params.ignore_eos
        length_penalty = params.length_penalty

        tokenizer = self.renderer.get_tokenizer()
        eos_token_id = tokenizer.eos_token_id
        sort_beams_key = create_sort_beams_key_function(eos_token_id, length_penalty)

        engine_inputs = self._preprocess_cmpl(prompts)
        lora_requests = self._lora_request_to_seq(lora_request, len(engine_inputs))

        if use_tqdm and concurrency_limit is not None:
            logger.warning(
                "Progress bar is not supported when using concurrency_limit. "
                "Disabling progress bar."
            )
            use_tqdm = False

        if concurrency_limit is None:
            concurrency_limit = len(engine_inputs)

        # generate 2 * beam_width candidates at each step
        # following the huggingface transformers implementation
        # at https://github.com/huggingface/transformers/blob/e15687fffe5c9d20598a19aeab721ae0a7580f8a/src/transformers/generation/beam_search.py#L534 # noqa
        sampling_params = SamplingParams(
            logprobs=2 * beam_width,
            max_tokens=1,
            temperature=temperature,
            skip_clone=True,  # Internal beam search, safe to skip clone
        )
        instances: list[BeamSearchInstance] = []

        for lora_req, prompt in zip(lora_requests, engine_inputs):
            if prompt["type"] == "embeds":
                raise NotImplementedError(
                    "Embedding prompt not supported for beam search"
                )

            instances.append(
                BeamSearchInstance(
                    prompt,
                    lora_request=lora_req,
                    logprobs=None,
                ),
            )

        for prompt_start in range(0, len(instances), concurrency_limit):
            instances_batch = instances[prompt_start : prompt_start + concurrency_limit]

            token_iter = range(max_tokens)
            if use_tqdm:
                token_iter = tqdm(
                    token_iter, desc="Beam search", unit="token", unit_scale=False
                )
                logger.warning(
                    "The progress bar shows the upper bound on token steps and "
                    "may finish early due to stopping conditions. It does not "
                    "reflect instance-level progress."
                )
            for _ in token_iter:
                all_beams: list[BeamSearchSequence] = list(
                    sum((instance.beams for instance in instances_batch), [])
                )
                pos = [0] + list(
                    itertools.accumulate(
                        len(instance.beams) for instance in instances_batch
                    )
                )
                instance_start_and_end: list[tuple[int, int]] = list(
                    zip(pos[:-1], pos[1:])
                )

                if len(all_beams) == 0:
                    break

                # only runs for one step
                # we don't need to use tqdm here
                output = self._render_and_run_requests(
                    prompts=(beam.get_prompt() for beam in all_beams),
                    params=self._params_to_seq(sampling_params, len(all_beams)),
                    output_type=RequestOutput,
                    lora_requests=[beam.lora_request for beam in all_beams],
                    use_tqdm=False,
                )

                for (start, end), instance in zip(
                    instance_start_and_end, instances_batch
                ):
                    instance_new_beams = []
                    for i in range(start, end):
                        current_beam = all_beams[i]
                        result = output[i]

                        if result.outputs[0].logprobs is not None:
                            # if `result.outputs[0].logprobs` is None, it means
                            # the sequence is completed because of the
                            # max-model-len or abortion. we don't need to add
                            # it to the new beams.
                            logprobs = result.outputs[0].logprobs[0]
                            for token_id, logprob_obj in logprobs.items():
                                new_beam = BeamSearchSequence(
                                    current_beam.orig_prompt,
                                    tokens=current_beam.tokens + [token_id],
                                    logprobs=current_beam.logprobs + [logprobs],
                                    lora_request=current_beam.lora_request,
                                    cum_logprob=current_beam.cum_logprob
                                    + logprob_obj.logprob,
                                )

                                if token_id == eos_token_id and not ignore_eos:
                                    instance.completed.append(new_beam)
                                else:
                                    instance_new_beams.append(new_beam)
                    sorted_beams = sorted(
                        instance_new_beams, key=sort_beams_key, reverse=True
                    )
                    instance.beams = sorted_beams[:beam_width]

        outputs = []
        for instance in instances:
            instance.completed.extend(instance.beams)
            sorted_completed = sorted(
                instance.completed, key=sort_beams_key, reverse=True
            )
            best_beams = sorted_completed[:beam_width]

            for beam in best_beams:
                beam.text = tokenizer.decode(beam.tokens)

            outputs.append(BeamSearchOutput(sequences=best_beams))

        return outputs

    def_preprocess_cmpl(
        self,
        prompts: Sequence[PromptType],
        tokenization_kwargs: dict[str, Any] | None = None,
        mm_processor_kwargs: dict[str, Any] | None = None,
    ) -> Sequence[EngineInput]:
"""
        Convert prompt inputs from LLM APIs (other than [LLM.chat][]) into
        a format that can be passed to `_add_request`.

        Refer to [LLM.generate][] for a complete description of the arguments.

        Returns:
            A list of `EngineInput` objects ready to be passed into LLMEngine.
        """
        renderer = self.renderer
        model_config = self.model_config

        parsed_prompts = [
            parse_model_prompt(model_config, prompt) for prompt in prompts
        ]
        tok_params = renderer.default_cmpl_tok_params.with_kwargs(
            **(tokenization_kwargs or {})
        )
        prompt_extras = (
            None
            if mm_processor_kwargs is None
            else {"mm_processor_kwargs": mm_processor_kwargs}
        )

        return renderer.render_cmpl(
            parsed_prompts,
            tok_params,
            prompt_extras=prompt_extras,
        )

    def_preprocess_cmpl_one(
        self,
        prompt: PromptType,
        tokenization_kwargs: dict[str, Any] | None = None,
        mm_processor_kwargs: dict[str, Any] | None = None,
    ) -> EngineInput:
        (engine_input,) = self._preprocess_cmpl(
            [prompt],
            tokenization_kwargs,
            mm_processor_kwargs=mm_processor_kwargs,
        )
        return engine_input

    def_preprocess_chat(
        self,
        conversations: Sequence[list[ChatCompletionMessageParam]],
        chat_template: str | None = None,
        chat_template_content_format: ChatTemplateContentFormatOption = "auto",
        chat_template_kwargs: dict[str, Any] | None = None,
        add_generation_prompt: bool = True,
        continue_final_message: bool = False,
        tools: list[dict[str, Any]] | None = None,
        tokenization_kwargs: dict[str, Any] | None = None,
        mm_processor_kwargs: dict[str, Any] | None = None,
    ) -> Sequence[EngineInput]:
"""
        Convert a list of conversations into prompts so that they can then
        be used as input for other LLM APIs.

        Refer to [LLM.chat][] for a complete description of the arguments.

        Returns:
            A list of `EngineInput` objects ready to be passed into LLMEngine.
        """
        renderer = self.renderer

        chat_params = ChatParams(
            chat_template=chat_template,
            chat_template_content_format=chat_template_content_format,
            chat_template_kwargs=merge_kwargs(
                chat_template_kwargs,
                dict(
                    add_generation_prompt=add_generation_prompt,
                    continue_final_message=continue_final_message,
                    tools=tools,
                    tokenize=(
                        is_mistral_tokenizer(renderer.tokenizer)
                        or self.model_config.enable_prompt_embeds
                    ),
                ),
            ),
            mm_processor_kwargs=mm_processor_kwargs,
        )
        tok_params = renderer.default_chat_tok_params.with_kwargs(
            **(tokenization_kwargs or {})
        )
        prompt_extras = (
            None
            if mm_processor_kwargs is None
            else {"mm_processor_kwargs": mm_processor_kwargs}
        )

        _, engine_inputs = renderer.render_chat(
            conversations,
            chat_params,
            tok_params,
            prompt_extras=prompt_extras,
        )

        return engine_inputs

    def_preprocess_chat_one(
        self,
        conversation: list[ChatCompletionMessageParam],
        chat_template: str | None = None,
        chat_template_content_format: ChatTemplateContentFormatOption = "auto",
        chat_template_kwargs: dict[str, Any] | None = None,
        add_generation_prompt: bool = True,
        continue_final_message: bool = False,
        tools: list[dict[str, Any]] | None = None,
        tokenization_kwargs: dict[str, Any] | None = None,
        mm_processor_kwargs: dict[str, Any] | None = None,
    ) -> EngineInput:
        (engine_input,) = self._preprocess_chat(
            [conversation],
            chat_template=chat_template,
            chat_template_content_format=chat_template_content_format,
            chat_template_kwargs=chat_template_kwargs,
            add_generation_prompt=add_generation_prompt,
            continue_final_message=continue_final_message,
            tools=tools,
            tokenization_kwargs=tokenization_kwargs,
            mm_processor_kwargs=mm_processor_kwargs,
        )

        return engine_input

    defchat(
        self,
        messages: list[ChatCompletionMessageParam]
        | Sequence[list[ChatCompletionMessageParam]],
        sampling_params: SamplingParams | Sequence[SamplingParams] | None = None,
        use_tqdm: bool | Callable[..., tqdm] = True,
        lora_request: Sequence[LoRARequest] | LoRARequest | None = None,
        chat_template: str | None = None,
        chat_template_content_format: ChatTemplateContentFormatOption = "auto",
        add_generation_prompt: bool = True,
        continue_final_message: bool = False,
        tools: list[dict[str, Any]] | None = None,
        chat_template_kwargs: dict[str, Any] | None = None,
        tokenization_kwargs: dict[str, Any] | None = None,
        mm_processor_kwargs: dict[str, Any] | None = None,
    ) -> list[RequestOutput]:
"""
        Generate responses for a chat conversation.

        The chat conversation is converted into a text prompt using the
        tokenizer and calls the [generate][vllm.LLM.generate] method to generate
        the responses.

        Multi-modal inputs can be passed in the same way you would pass them
        to the OpenAI API.

        Args:
            messages: A sequence of conversations or a single conversation.

                - Each conversation is represented as a list of messages.
                - Each message is a dictionary with 'role' and 'content' keys.

            sampling_params: The sampling parameters for text generation.
                If None, we use the default sampling parameters. When it
                is a single value, it is applied to every prompt. When it
                is a list, the list must have the same length as the
                prompts and it is paired one by one with the prompt.
            use_tqdm: If `True`, shows a tqdm progress bar.
                If a callable (e.g., `functools.partial(tqdm, leave=False)`),
                it is used to create the progress bar.
                If `False`, no progress bar is created.
            lora_request: LoRA request to use for generation, if any.
            chat_template: The template to use for structuring the chat.
                If not provided, the model's default chat template will be used.
            chat_template_content_format: The format to render message content.

                - "string" will render the content as a string.
                  Example: `"Who are you?"`
                - "openai" will render the content as a list of dictionaries,
                  similar to OpenAI schema.
                  Example: `[{"type": "text", "text": "Who are you?"}]`

            add_generation_prompt: If True, adds a generation template
                to each message.
            continue_final_message: If True, continues the final message in
                the conversation instead of starting a new one. Cannot be
                `True` if `add_generation_prompt` is also `True`.
            chat_template_kwargs: Additional kwargs to pass to the chat
                template.
            tokenization_kwargs: Overrides for `tokenizer.encode`.
            mm_processor_kwargs: Overrides for `processor.__call__`.

        Returns:
            A list of `RequestOutput` objects containing the generated
            responses in the same order as the input messages.
        """
        model_config = self.model_config
        runner_type = model_config.runner_type
        if runner_type != "generate":
            raise ValueError(
                "LLM.chat() is only supported for generative models. "
                "Try passing `--runner generate` to use the model as a "
                "generative model."
            )

        if sampling_params is None:
            sampling_params = self.get_default_sampling_params()

        return self._run_chat(
            messages=messages,
            params=sampling_params,
            output_type=RequestOutput,
            use_tqdm=use_tqdm,
            lora_request=lora_request,
            chat_template=chat_template,
            chat_template_content_format=chat_template_content_format,
            chat_template_kwargs=chat_template_kwargs,
            add_generation_prompt=add_generation_prompt,
            continue_final_message=continue_final_message,
            tools=tools,
            tokenization_kwargs=tokenization_kwargs,
            mm_processor_kwargs=mm_processor_kwargs,
        )

    defencode(
        self,
        prompts: PromptType | Sequence[PromptType] | DataPrompt,
        pooling_params: PoolingParams | Sequence[PoolingParams] | None = None,
        *,
        use_tqdm: bool | Callable[..., tqdm] = True,
        lora_request: list[LoRARequest] | LoRARequest | None = None,
        pooling_task: PoolingTask | None = None,
        tokenization_kwargs: dict[str, Any] | None = None,
    ) -> list[PoolingRequestOutput]:
"""Apply pooling to the hidden states corresponding to the input
        prompts.

        This class automatically batches the given prompts, considering
        the memory constraint. For the best performance, put all of your prompts
        into a single list and pass it to this method.

        Args:
            prompts: The prompts to the LLM. You may pass a sequence of prompts
                for batch inference. See [PromptType][vllm.inputs.PromptType]
                for more details about the format of each prompt.
            pooling_params: The pooling parameters for pooling. If None, we
                use the default pooling parameters.
            use_tqdm: If `True`, shows a tqdm progress bar.
                If a callable (e.g., `functools.partial(tqdm, leave=False)`),
                it is used to create the progress bar.
                If `False`, no progress bar is created.
            lora_request: LoRA request to use for generation, if any.
            pooling_task: Override the pooling task to use.
            tokenization_kwargs: Overrides for `tokenizer.encode`.

        Returns:
            A list of `PoolingRequestOutput` objects containing the
            pooled hidden states in the same order as the input prompts.
        """

        if isinstance(prompts, dict) and "data" in prompts and pooling_task != "plugin":
            raise ValueError(
                "The 'data' field is only supported for the 'plugin' pooling task."
            )
        self._verify_pooling_task(pooling_task)
        assert pooling_task is not None and pooling_task in self.pooling_io_processors

        io_processor = self.pooling_io_processors[pooling_task]

        if pooling_params is None:
            pooling_params = PoolingParams()

        ctx = OfflineInputsContext(
            prompts=prompts,
            pooling_params=pooling_params,
            tokenization_kwargs=tokenization_kwargs,
        )

        engine_inputs = io_processor.pre_process_offline(ctx)
        n_inputs = len(engine_inputs)
        assert ctx.pooling_params is not None

        params_seq = self._params_to_seq(ctx.pooling_params, n_inputs)

        for param in params_seq:
            if param.task is None:
                param.task = pooling_task
            elif pooling_task == "plugin":
                # `plugin` task uses io_processor.parse_request to verify inputs.
                # We actually allow plugin to overwrite pooling_task.
                pass
            elif param.task != pooling_task:
                msg = f"You cannot overwrite {param.task=!r} with {pooling_task=!r}!"
                raise ValueError(msg)

        seq_lora_requests = self._lora_request_to_seq(lora_request, n_inputs)
        seq_priority = self._priority_to_seq(None, n_inputs)

        self._render_and_add_requests(
            prompts=engine_inputs,
            params=params_seq,
            lora_requests=seq_lora_requests,
            priorities=seq_priority,
        )

        outputs = self._run_engine(use_tqdm=use_tqdm, output_type=PoolingRequestOutput)
        outputs = io_processor.post_process_offline(
            ctx=OfflineOutputsContext(outputs=outputs)
        )
        return outputs

    def_verify_pooling_task(self, pooling_task: PoolingTask | None):
        if self.runner_type != "pooling":
            raise ValueError(
                "LLM.encode() is only supported for pooling models. "
                "Try passing `--runner pooling` to use the model as a "
                "pooling model."
            )

        if pooling_task is None:
            raise ValueError(
"""
                pooling_task required for `LLM.encode`.
                Please use one of the more specific methods or set the pooling_task when using `LLM.encode`:
                  - For embeddings, use `LLM.embed(...)` or `pooling_task="embed"`.
                  - For classification logits, use `LLM.classify(...)` or `pooling_task="classify"`.
                  - For similarity scores, use `LLM.score(...)`.
                  - For rewards, `pooling_task="classify"` or `pooling_task="token_classify"`.
                  - For token classification, use `pooling_task="token_classify"`.
                  - For multi-vector retrieval, use `pooling_task="token_embed"`.
                """  # noqa: E501
            )

        if (
            pooling_task in ("embed", "token_embed")
            and pooling_task not in self.supported_tasks
        ):
            raise ValueError(
                "Embedding API is not supported by this model. "
                "Try converting the model using `--convert embed`."
            )

        if (
            pooling_task in ("classify", "token_classify")
            and pooling_task not in self.supported_tasks
        ):
            raise ValueError(
                "Classification API is not supported by this model. "
                "Try converting the model using `--convert classify`."
            )

        # plugin task uses io_processor.parse_request to verify inputs
        if pooling_task != "plugin" and pooling_task != self.pooling_task:
            if pooling_task not in self.supported_tasks:
                raise ValueError(
                    f"Unsupported task: {pooling_task!r} "
                    f"Supported tasks: {self.supported_tasks}"
                )
            else:
                raise ValueError(
                    f"Try switching the model's pooling_task "
                    f'via `PoolerConfig(task="{pooling_task}")`'
                )

        if pooling_task == "plugin" and "plugin" not in self.pooling_io_processors:
            raise ValueError(
                "No IOProcessor plugin installed. Please refer "
                "to the documentation and to the "
                "'prithvi_geospatial_mae_io_processor' "
                "offline inference example for more details."
            )

    defembed(
        self,
        prompts: PromptType | Sequence[PromptType],
        *,
        use_tqdm: bool | Callable[..., tqdm] = True,
        pooling_params: PoolingParams | Sequence[PoolingParams] | None = None,
        lora_request: list[LoRARequest] | LoRARequest | None = None,
        tokenization_kwargs: dict[str, Any] | None = None,
    ) -> list[EmbeddingRequestOutput]:
"""
        Generate an embedding vector for each prompt.

        This class automatically batches the given prompts, considering
        the memory constraint. For the best performance, put all of your prompts
        into a single list and pass it to this method.

        Args:
            prompts: The prompts to the LLM. You may pass a sequence of prompts
                for batch inference. See [PromptType][vllm.inputs.PromptType]
                for more details about the format of each prompt.
            pooling_params: The pooling parameters for pooling. If None, we
                use the default pooling parameters.
            use_tqdm: If `True`, shows a tqdm progress bar.
                If a callable (e.g., `functools.partial(tqdm, leave=False)`),
                it is used to create the progress bar.
                If `False`, no progress bar is created.
            lora_request: LoRA request to use for generation, if any.
            tokenization_kwargs: Overrides for `tokenizer.encode`.

        Returns:
            A list of `EmbeddingRequestOutput` objects containing the
            embedding vectors in the same order as the input prompts.
        """

        items = self.encode(
            prompts,
            use_tqdm=use_tqdm,
            pooling_params=pooling_params,
            lora_request=lora_request,
            pooling_task="embed",
            tokenization_kwargs=tokenization_kwargs,
        )

        return [EmbeddingRequestOutput.from_base(item) for item in items]

    defclassify(
        self,
        prompts: PromptType | Sequence[PromptType],
        *,
        pooling_params: PoolingParams | Sequence[PoolingParams] | None = None,
        use_tqdm: bool | Callable[..., tqdm] = True,
        lora_request: list[LoRARequest] | LoRARequest | None = None,
        tokenization_kwargs: dict[str, Any] | None = None,
    ) -> list[ClassificationRequestOutput]:
"""
        Generate class logits for each prompt.

        This class automatically batches the given prompts, considering
        the memory constraint. For the best performance, put all of your prompts
        into a single list and pass it to this method.

        Args:
            prompts: The prompts to the LLM. You may pass a sequence of prompts
                for batch inference. See [PromptType][vllm.inputs.PromptType]
                for more details about the format of each prompt.
            pooling_params: The pooling parameters for pooling. If None, we
                use the default pooling parameters.
            use_tqdm: If `True`, shows a tqdm progress bar.
                If a callable (e.g., `functools.partial(tqdm, leave=False)`),
                it is used to create the progress bar.
                If `False`, no progress bar is created.
            lora_request: LoRA request to use for generation, if any.
            tokenization_kwargs: Overrides for `tokenizer.encode`.

        Returns:
            A list of `ClassificationRequestOutput` objects containing the
            embedding vectors in the same order as the input prompts.
        """

        items = self.encode(
            prompts,
            use_tqdm=use_tqdm,
            pooling_params=pooling_params,
            lora_request=lora_request,
            pooling_task="classify",
            tokenization_kwargs=tokenization_kwargs,
        )

        return [ClassificationRequestOutput.from_base(item) for item in items]

    defreward(
        self,
        prompts: PromptType | Sequence[PromptType],
        /,
        *,
        pooling_params: PoolingParams | Sequence[PoolingParams] | None = None,
        use_tqdm: bool | Callable[..., tqdm] = True,
        lora_request: list[LoRARequest] | LoRARequest | None = None,
        tokenization_kwargs: dict[str, Any] | None = None,
    ) -> list[PoolingRequestOutput]:
"""
        Generate rewards for each prompt.

        Args:
            prompts: The prompts to the LLM. You may pass a sequence of prompts
                for batch inference. See [PromptType][vllm.inputs.PromptType]
                for more details about the format of each prompt.
            pooling_params: The pooling parameters for pooling. If None, we
                use the default pooling parameters.
            use_tqdm: If `True`, shows a tqdm progress bar.
                If a callable (e.g., `functools.partial(tqdm, leave=False)`),
                it is used to create the progress bar.
                If `False`, no progress bar is created.
            lora_request: LoRA request to use for generation, if any.
            tokenization_kwargs: Overrides for `tokenizer.encode`.

        Returns:
            A list of `PoolingRequestOutput` objects containing the
            pooled hidden states in the same order as the input prompts.
        """
        logger.warning_once(
            "`llm.reward` api is deprecated and will be removed in v0.23. "
            'Please use `LLM.encode` with `pooling_task="classify"` or '
            '`pooling_task="token_classify"` instead.'
        )
        return self.encode(
            prompts,
            use_tqdm=use_tqdm,
            lora_request=lora_request,
            pooling_params=pooling_params,
            pooling_task="token_classify",
            tokenization_kwargs=tokenization_kwargs,
        )

    defscore(
        self,
        data_1: ScoreInput | list[ScoreInput],
        data_2: ScoreInput | list[ScoreInput],
        /,
        *,
        use_tqdm: bool | Callable[..., tqdm] = True,
        pooling_params: PoolingParams | None = None,
        lora_request: list[LoRARequest] | LoRARequest | None = None,
        tokenization_kwargs: dict[str, Any] | None = None,
        chat_template: str | None = None,
    ) -> list[ScoringRequestOutput]:
"""Generate similarity scores for all pairs `<text,text_pair>` or
          `<multi-modal data, multi-modal data pair>`.

        The inputs can be `1 -> 1`, `1 -> N` or `N -> N`.
        In the `1 - N` case the `data_1` input will be replicated `N`
        times to pair with the `data_2` inputs.
        The input pairs are used to build a list of prompts for the
        cross encoder model. This class automatically batches the prompts,
        considering the memory constraint. For the best performance, put all
        of your inputs into a single list and pass it to this method.

        Supports both text and multi-modal data (images, etc.) when used with
        appropriate multi-modal models. For multi-modal inputs, ensure the
        prompt structure matches the model's expected input format.

        Args:
            data_1: Can be a single prompt, a list of prompts or
                `ScoreMultiModalParam`, which can contain either text or
                multi-modal data. When a list, it must have the same length as
                the `data_2` list.
            data_2: The data to pair with the query to form the input to
                the LLM. Can be text or multi-modal data. See [PromptType]
                [vllm.inputs.PromptType] for more details about the format of
                each prompt.
            pooling_params: The pooling parameters for pooling. If None, we
                use the default pooling parameters.
            use_tqdm: If `True`, shows a tqdm progress bar.
                If a callable (e.g., `functools.partial(tqdm, leave=False)`),
                it is used to create the progress bar.
                If `False`, no progress bar is created.
            lora_request: LoRA request to use for generation, if any.
            chat_template: The chat template to use for the scoring. If None, we
                use the model's default chat template.
            tokenization_kwargs: Overrides for `tokenizer.encode`.
        Returns:
            A list of `ScoringRequestOutput` objects containing the
            generated scores in the same order as the input prompts.
        """

        if self.runner_type != "pooling":
            raise ValueError(
                "LLM.score() is only supported for pooling models. "
                "Try passing `--runner pooling` to use the model as a "
                "pooling model."
            )

        score_type: str | None = SCORE_TYPE_MAP.get(self.pooling_task, None)  # type: ignore[arg-type]
        if (
            score_type == "cross-encoder"
            and getattr(self.model_config.hf_config, "num_labels", 0) != 1
        ):
            raise ValueError("Scoring API is only enabled for num_labels == 1.")

        if score_type is None or score_type not in self.pooling_io_processors:
            raise ValueError("This model does not support the Scoring API.")

        io_processor = self.pooling_io_processors[score_type]
        assert isinstance(io_processor, ScoringIOProcessor)

        pooling_task = io_processor.pooling_task
        scoring_data = io_processor.valid_inputs(data_1, data_2)
        n_queries = len(scoring_data.data_1)

        if pooling_params is None:
            pooling_params = PoolingParams()

        ctx = OfflineInputsContext(
            prompts=scoring_data,
            pooling_params=pooling_params,
            tokenization_kwargs=tokenization_kwargs,
            chat_template=chat_template,
            n_queries=n_queries,
        )

        engine_inputs = io_processor.pre_process_offline(ctx)
        n_inputs = len(engine_inputs)

        seq_lora_requests = self._lora_request_to_seq(lora_request, n_inputs)
        params_seq = self._params_to_seq(ctx.pooling_params, n_inputs)

        for param in params_seq:
            if param.task is None:
                param.task = pooling_task
            elif param.task != pooling_task:
                msg = f"You cannot overwrite {param.task=!r} with {pooling_task=!r}!"
                raise ValueError(msg)

        seq_priority = self._priority_to_seq(None, n_inputs)

        self._render_and_add_requests(
            prompts=engine_inputs,
            params=params_seq,
            lora_requests=seq_lora_requests,
            priorities=seq_priority,
        )

        outputs = self._run_engine(use_tqdm=use_tqdm, output_type=PoolingRequestOutput)
        outputs = io_processor.post_process_offline(
            ctx=OfflineOutputsContext(outputs=outputs, n_queries=n_queries),
        )

        return [ScoringRequestOutput.from_base(item) for item in outputs]

    defstart_profile(self, profile_prefix: str | None = None) -> None:
"""Start profiling with optional custom trace prefix.

        Args:
            profile_prefix: Optional prefix for the trace file names. If provided,
                           trace files will be named as "<prefix>_dp<X>_pp<Y>_tp<Z>".
                           If not provided, default naming will be used.
        """
        self.llm_engine.start_profile(profile_prefix)

    defstop_profile(self) -> None:
        self.llm_engine.stop_profile()

    defreset_prefix_cache(
        self, reset_running_requests: bool = False, reset_connector: bool = False
    ) -> bool:
        return self.llm_engine.reset_prefix_cache(
            reset_running_requests, reset_connector
        )

    defsleep(self, level: int = 1, mode: PauseMode = "abort"):
"""
        Put the engine to sleep. The engine should not process any requests.
        The caller should guarantee that no requests are being processed
        during the sleep period, before `wake_up` is called.

        Args:
            level: The sleep level.
                - Level 0: Pause scheduling but continue accepting requests.
                           Requests are queued but not processed.
                - Level 1: Offload model weights to CPU, discard KV cache.
                           The content of kv cache is forgotten. Good for
                           sleeping and waking up the engine to run the same
                           model again. Please make sure there's enough CPU
                           memory to store the model weights.
                - Level 2: Discard all GPU memory (weights + KV cache).
                           Good for sleeping and waking up the engine to run
                           a different model or update the model, where
                           previous model weights are not needed. It reduces
                           CPU memory pressure.
            mode: How to handle any existing requests, can be "abort", "wait",
                or "keep".
        """
        self.llm_engine.sleep(level=level, mode=mode)

    defwake_up(self, tags: list[str] | None = None):
"""
        Wake up the engine from sleep mode. See the [sleep][vllm.LLM.sleep]
        method for more details.

        Args:
            tags: An optional list of tags to reallocate the engine memory
                for specific memory allocations. Values must be in
                `("weights", "kv_cache", "scheduling")`. If None, all memory
                is reallocated. wake_up should be called with all tags
                (or None) before the engine is used again.
                Use tags=["scheduling"] to resume from level 0 sleep.
        """
        self.llm_engine.wake_up(tags)

    defget_metrics(self) -> list["Metric"]:
"""Return a snapshot of aggregated metrics from Prometheus.

        Returns:
            A `MetricSnapshot` instance capturing the current state
            of all aggregated metrics from Prometheus.

        Note:
            This method is only available with the V1 LLM engine.
        """
        return self.llm_engine.get_metrics()

    def_params_to_seq(
        self,
        params: _P | Sequence[_P],
        num_requests: int,
    ) -> Sequence[_P]:
        if isinstance(params, Sequence):
            if len(params) != num_requests:
                raise ValueError(
                    f"The lengths of prompts ({num_requests}) "
                    f"and params ({len(params)}) must be the same."
                )

            return params

        return [params] * num_requests

    def_lora_request_to_seq(
        self,
        lora_request: LoRARequest | None | Sequence[LoRARequest | None],
        num_requests: int,
    ) -> Sequence[LoRARequest | None]:
        if isinstance(lora_request, Sequence):
            if len(lora_request) != num_requests:
                raise ValueError(
                    f"The lengths of prompts ({num_requests}) "
                    f"and lora_request ({len(lora_request)}) must be the same."
                )

            return lora_request

        return [lora_request] * num_requests

    def_priority_to_seq(
        self,
        priority: list[int] | None,
        num_requests: int,
    ) -> Sequence[int]:
        if priority is not None:
            if len(priority) != num_requests:
                raise ValueError(
                    f"The lengths of prompts ({num_requests}) "
                    f"and priority ({len(priority)}) must be the same."
                )

            return priority

        return [0] * num_requests

    def_add_completion_requests(
        self,
        prompts: PromptType | Sequence[PromptType],
        params: SamplingParams
        | PoolingParams
        | Sequence[SamplingParams | PoolingParams],
        *,
        use_tqdm: bool | Callable[..., tqdm] = True,
        lora_request: Sequence[LoRARequest] | LoRARequest | None = None,
        priority: list[int] | None = None,
        tokenization_kwargs: dict[str, Any] | None = None,
        mm_processor_kwargs: dict[str, Any] | None = None,
    ) -> list[str]:
        seq_prompts = prompt_to_seq(prompts)
        seq_params = self._params_to_seq(params, len(seq_prompts))
        seq_lora_requests = self._lora_request_to_seq(lora_request, len(seq_prompts))
        seq_priority = self._priority_to_seq(priority, len(seq_prompts))

        return self._render_and_add_requests(
            prompts=(
                self._preprocess_cmpl_one(
                    prompt,
                    tokenization_kwargs,
                    mm_processor_kwargs=mm_processor_kwargs,
                )
                for prompt in maybe_tqdm(
                    seq_prompts,
                    use_tqdm=use_tqdm,
                    desc="Rendering prompts",
                )
            ),
            params=seq_params,
            lora_requests=seq_lora_requests,
            priorities=seq_priority,
        )

    def_run_completion(
        self,
        prompts: PromptType | Sequence[PromptType],
        params: SamplingParams
        | PoolingParams
        | Sequence[SamplingParams | PoolingParams],
        output_type: type[_O],
        *,
        use_tqdm: bool | Callable[..., tqdm] = True,
        lora_request: Sequence[LoRARequest] | LoRARequest | None = None,
        priority: list[int] | None = None,
        tokenization_kwargs: dict[str, Any] | None = None,
        mm_processor_kwargs: dict[str, Any] | None = None,
    ):
        self._add_completion_requests(
            prompts=prompts,
            params=params,
            use_tqdm=use_tqdm,
            lora_request=lora_request,
            priority=priority,
            tokenization_kwargs=tokenization_kwargs,
            mm_processor_kwargs=mm_processor_kwargs,
        )
        return self._run_engine(use_tqdm=use_tqdm, output_type=output_type)

    def_run_chat(
        self,
        messages: list[ChatCompletionMessageParam]
        | Sequence[list[ChatCompletionMessageParam]],
        params: SamplingParams
        | PoolingParams
        | Sequence[SamplingParams | PoolingParams],
        output_type: type[_O],
        *,
        use_tqdm: bool | Callable[..., tqdm] = True,
        lora_request: Sequence[LoRARequest] | LoRARequest | None = None,
        chat_template: str | None = None,
        chat_template_content_format: ChatTemplateContentFormatOption = "auto",
        add_generation_prompt: bool = True,
        continue_final_message: bool = False,
        tools: list[dict[str, Any]] | None = None,
        chat_template_kwargs: dict[str, Any] | None = None,
        tokenization_kwargs: dict[str, Any] | None = None,
        mm_processor_kwargs: dict[str, Any] | None = None,
    ):
        seq_convs = conversation_to_seq(messages)
        seq_params = self._params_to_seq(params, len(seq_convs))
        seq_lora_requests = self._lora_request_to_seq(lora_request, len(seq_convs))

        # When thinking is enabled or tools are provided, and the model
        # uses special tokens for structured output (e.g. Gemma4's
        # <|channel>, <|tool_call>, <|"|>), automatically set
        # skip_special_tokens=False so these tokens are preserved in
        # output.text for downstream parsing.
        needs_parsing = (
            chat_template_kwargs and chat_template_kwargs.get("enable_thinking")
        ) or tools
        if needs_parsing:
            self._adjust_params_for_parsing(seq_params)

        return self._render_and_run_requests(
            prompts=(
                self._preprocess_chat_one(
                    conversation,
                    chat_template=chat_template,
                    chat_template_content_format=chat_template_content_format,
                    chat_template_kwargs=chat_template_kwargs,
                    add_generation_prompt=add_generation_prompt,
                    continue_final_message=continue_final_message,
                    tools=tools,
                    tokenization_kwargs=tokenization_kwargs,
                    mm_processor_kwargs=mm_processor_kwargs,
                )
                for conversation in maybe_tqdm(
                    seq_convs,
                    use_tqdm=use_tqdm,
                    desc="Rendering conversations",
                )
            ),
            params=seq_params,
            output_type=output_type,
            lora_requests=seq_lora_requests,
            use_tqdm=use_tqdm,
        )

    def_adjust_params_for_parsing(
        self, params: Sequence[SamplingParams | PoolingParams]
    ) -> None:
"""Set ``skip_special_tokens=False`` when the model encodes
        structured output syntax as special tokens.

        Models like Gemma4 register thinking delimiters
        (``<|channel>``/``<channel|>``) and tool call tokens
        (``<|tool_call>``/``<tool_call|>``/``<|"|>``) as special tokens.
        The default ``skip_special_tokens=True`` strips them from
        ``output.text``, breaking parsing of both reasoning blocks and
        tool calls.

        This is a no-op for models whose structured tokens are regular
        text tokens (e.g. DeepSeek's ``<think>``/``</think>``).
        """
        # The offline API currently lacks a unified rendering pipeline.
        # Until the planned Renderer refactor is complete, we hardcode
        # this token preservation logic specifically for Gemma4 models
        # to avoid regressions on other models.
        hf_config = getattr(self.model_config, "hf_config", None)
        architectures = getattr(hf_config, "architectures", [])

        if any("Gemma4" in arch for arch in architectures):
            tokenizer = self.renderer.get_tokenizer()
            vocab = tokenizer.get_vocab()
            special_ids = set(getattr(tokenizer, "all_special_ids", []))

            # Tokens used for thinking delimiters and tool call syntax
            # that some models (Gemma4) register as special tokens.
            structured_tokens = (
                "<|channel>",
                "<channel|>",  # thinking delimiters
                "<|tool_call>",
                "<tool_call|>",  # tool call delimiters
                '<|"|>',  # string quoting in tool args
            )
            needs_special = any(
                vocab.get(tok) in special_ids
                for tok in structured_tokens
                if tok in vocab
            )
            if needs_special:
                for sp in params:
                    if isinstance(sp, SamplingParams) and sp.skip_special_tokens:
                        sp.skip_special_tokens = False

    def_render_and_run_requests(
        self,
        prompts: Iterable[EngineInput],
        params: Sequence[SamplingParams | PoolingParams],
        output_type: type[_O],
        *,
        lora_requests: Sequence[LoRARequest | None] | None = None,
        priorities: Sequence[int] | None = None,
        use_tqdm: bool | Callable[..., tqdm] = True,
    ):
        if isinstance(prompts, (list, tuple)):
            logger.warning_once(
                "Rendering all prompts before adding them to the engine "
                "is less efficient than performing both on the same prompt "
                "before processing the next prompt. You should instead pass "
                "a generator that renders one prompt per iteration, as that allows "
                "engine execution to begin for the first prompt while processing "
                "the next prompt."
            )

        self._render_and_add_requests(
            prompts=prompts,
            params=params,
            lora_requests=lora_requests,
            priorities=priorities,
        )

        return self._run_engine(output_type, use_tqdm=use_tqdm)

    def_render_and_add_requests(
        self,
        prompts: Iterable[EngineInput],
        params: Sequence[SamplingParams | PoolingParams],
        *,
        lora_requests: Sequence[LoRARequest | None] | None = None,
        priorities: Sequence[int] | None = None,
    ) -> list[str]:
        added_request_ids: list[str] = []

        try:
            for i, prompt in enumerate(prompts):
                request_id = self._add_request(
                    prompt,
                    params[i],
                    lora_request=self._resolve_mm_lora(
                        prompt,
                        None if lora_requests is None else lora_requests[i],
                    ),
                    priority=0 if priorities is None else priorities[i],
                )
                added_request_ids.append(request_id)
        except Exception as e:
            if added_request_ids:
                self.llm_engine.abort_request(added_request_ids, internal=True)
            raise e

        return added_request_ids

    def_add_request(
        self,
        prompt: EngineInput,
        params: SamplingParams | PoolingParams,
        lora_request: LoRARequest | None = None,
        priority: int = 0,
    ) -> str:
        if isinstance(params, SamplingParams):
            # We only care about the final output
            params.output_kind = RequestOutputKind.FINAL_ONLY

        request_id = str(next(self.request_counter))

        return self.llm_engine.add_request(
            request_id,
            prompt,
            params,
            lora_request=lora_request,
            priority=priority,
        )

    def_run_engine(
        self,
        output_type: type[_O] | tuple[type[_O], ...],
        *,
        use_tqdm: bool | Callable[..., tqdm] = True,
    ) -> list[_O]:
        # Initialize tqdm.
        if use_tqdm:
            num_requests = self.llm_engine.get_num_unfinished_requests()
            tqdm_func = use_tqdm if callable(use_tqdm) else tqdm
            pbar = tqdm_func(
                total=num_requests,
                desc="Processed prompts",
                dynamic_ncols=True,
                postfix=(f"est. speed input: {0:.2f} toks/s, output: {0:.2f} toks/s"),
            )

        # Run the engine.
        outputs: list[_O] = []
        total_in_toks = 0
        total_out_toks = 0
        while self.llm_engine.has_unfinished_requests():
            step_outputs = self.llm_engine.step()
            for output in step_outputs:
                assert isinstance(output, output_type)
                if output.finished:
                    outputs.append(output)  # type: ignore[arg-type]
                    if use_tqdm:
                        if isinstance(output, RequestOutput):
                            # Calculate tokens only for RequestOutput
                            n = len(output.outputs)
                            assert output.prompt_token_ids is not None
                            total_in_toks += len(output.prompt_token_ids) * n
                            in_spd = total_in_toks / pbar.format_dict["elapsed"]
                            total_out_toks += sum(
                                len(stp.token_ids) for stp in output.outputs
                            )
                            out_spd = total_out_toks / pbar.format_dict["elapsed"]
                            pbar.postfix = (
                                f"est. speed input: {in_spd:.2f} toks/s, "
                                f"output: {out_spd:.2f} toks/s"
                            )
                            pbar.update(n)
                        else:
                            pbar.update(1)
                        if pbar.n == num_requests:
                            pbar.refresh()

        if use_tqdm:
            pbar.close()
        # Sort the outputs by request ID.
        # This is necessary because some requests may be finished earlier than
        # its previous requests.
        return sorted(outputs, key=lambda x: int(x.request_id))

    definit_weight_transfer_engine(
        self, request: WeightTransferInitRequest | dict
    ) -> None:
"""
        Initialize weight transfer for RL training.

        Args:
            request: Weight transfer initialization request with backend-specific info
        """
        init_info_dict = (
            request["init_info"] if isinstance(request, dict) else request.init_info
        )

        self.llm_engine.collective_rpc(
            "init_weight_transfer_engine", kwargs={"init_info": init_info_dict}
        )

    defupdate_weights(self, request: WeightTransferUpdateRequest | dict) -> None:
"""
        Update the weights of the model.

        Args:
            request: Weight update request with backend-specific update info
        """
        update_info_dict = (
            request["update_info"] if isinstance(request, dict) else request.update_info
        )

        self.llm_engine.collective_rpc(
            "update_weights", kwargs={"update_info": update_info_dict}
        )

    def__repr__(self) -> str:
"""Return a transformers-style hierarchical view of the model."""
        # Cache the result to avoid repeated collective_rpc calls
        if self._cached_repr is None:
            results = self.llm_engine.collective_rpc("get_model_inspection")
            # In distributed settings, we get results from all workers
            # Just return the first one (they should all be the same)
            if results:
                self._cached_repr = results[0]
            else:
                self._cached_repr = f"LLM(model={self.model_config.model!r})"
        return self._cached_repr
```

### \_\_init\__ [¶](#vllm.LLM.__init__ "Permanent link")

```
__init__(
    model: str,
    *,
    runner: RunnerOption = "auto",
    convert: ConvertOption = "auto",
    tokenizer: str | None = None,
    tokenizer_mode: TokenizerMode | str = "auto",
    skip_tokenizer_init: bool = False,
    trust_remote_code: bool = False,
    allowed_local_media_path: str = "",
    allowed_media_domains: list[str] | None = None,
    tensor_parallel_size: int = 1,
    dtype: ModelDType = "auto",
    quantization: QuantizationMethods | None = None,
    revision: str | None = None,
    tokenizer_revision: str | None = None,
    chat_template: Path | str | None = None,
    seed: int = 0,
    gpu_memory_utilization: float = 0.92,
    cpu_offload_gb: float = 0,
    offload_group_size: int = 0,
    offload_num_in_group: int = 1,
    offload_prefetch_step: int = 1,
    offload_params: set[str] | None = None,
    enforce_eager: bool = False,
    enable_return_routed_experts: bool = False,
    disable_custom_all_reduce: bool = False,
    hf_token: bool | str | None = None,
    hf_overrides: HfOverrides | None = None,
    mm_processor_kwargs: dict[str, Any] | None = None,
    pooler_config: PoolerConfig | None = None,
    structured_outputs_config: dict[str, Any]
    | StructuredOutputsConfig
    | None = None,
    profiler_config: dict[str, Any]
    | ProfilerConfig
    | None = None,
    attention_config: dict[str, Any]
    | AttentionConfig
    | None = None,
    kv_cache_memory_bytes: int | None = None,
    compilation_config: int
    | dict[str, Any]
    | CompilationConfig
    | None = None,
    quantization_config: dict[str, Any]
    | OnlineQuantizationConfigArgs
    | None = None,
    logits_processors: list[str | type[LogitsProcessor]]
    | None = None,
    **kwargs: Any,
) -> None
```

LLM constructor.

Source code in `vllm/entrypoints/llm.py`

```
def__init__(
    self,
    model: str,
    *,
    runner: RunnerOption = "auto",
    convert: ConvertOption = "auto",
    tokenizer: str | None = None,
    tokenizer_mode: TokenizerMode | str = "auto",
    skip_tokenizer_init: bool = False,
    trust_remote_code: bool = False,
    allowed_local_media_path: str = "",
    allowed_media_domains: list[str] | None = None,
    tensor_parallel_size: int = 1,
    dtype: ModelDType = "auto",
    quantization: QuantizationMethods | None = None,
    revision: str | None = None,
    tokenizer_revision: str | None = None,
    chat_template: Path | str | None = None,
    seed: int = 0,
    gpu_memory_utilization: float = 0.92,
    cpu_offload_gb: float = 0,
    offload_group_size: int = 0,
    offload_num_in_group: int = 1,
    offload_prefetch_step: int = 1,
    offload_params: set[str] | None = None,
    enforce_eager: bool = False,
    enable_return_routed_experts: bool = False,
    disable_custom_all_reduce: bool = False,
    hf_token: bool | str | None = None,
    hf_overrides: HfOverrides | None = None,
    mm_processor_kwargs: dict[str, Any] | None = None,
    pooler_config: PoolerConfig | None = None,
    structured_outputs_config: dict[str, Any]
    | StructuredOutputsConfig
    | None = None,
    profiler_config: dict[str, Any] | ProfilerConfig | None = None,
    attention_config: dict[str, Any] | AttentionConfig | None = None,
    kv_cache_memory_bytes: int | None = None,
    compilation_config: int | dict[str, Any] | CompilationConfig | None = None,
    quantization_config: dict[str, Any]
    | OnlineQuantizationConfigArgs
    | None = None,
    logits_processors: list[str | type[LogitsProcessor]] | None = None,
    **kwargs: Any,
) -> None:
"""LLM constructor."""

    if "swap_space" in kwargs:
        kwargs.pop("swap_space")
        importwarnings

        warnings.warn(
            "The 'swap_space' parameter is deprecated and ignored. "
            "It will be removed in a future version.",
            DeprecationWarning,
            stacklevel=2,
        )

    if "disable_log_stats" not in kwargs:
        kwargs["disable_log_stats"] = True

    if "worker_cls" in kwargs:
        worker_cls = kwargs["worker_cls"]
        # if the worker_cls is not qualified string name,
        # we serialize it using cloudpickle to avoid pickling issues
        if isinstance(worker_cls, type):
            kwargs["worker_cls"] = cloudpickle.dumps(worker_cls)

    if "kv_transfer_config" in kwargs and isinstance(
        kwargs["kv_transfer_config"], dict
    ):
        fromvllm.config.kv_transferimport KVTransferConfig

        raw_config_dict = kwargs["kv_transfer_config"]
        try:
            kwargs["kv_transfer_config"] = KVTransferConfig(**raw_config_dict)
        except ValidationError as e:
            logger.error(
                "Failed to convert 'kv_transfer_config' dict to "
                "KVTransferConfig object. Dict: %s. Error: %s",
                raw_config_dict,
                e,
            )
            # Consider re-raising a more specific vLLM error or ValueError
            # to provide better context to the user.
            raise ValueError(f"Invalid 'kv_transfer_config' provided: {e}") frome

    if hf_overrides is None:
        hf_overrides = {}

    def_make_config(value: Any, cls: type[_R]) -> _R:
"""Convert dict/None/instance to a config instance."""
        if value is None:
            return cls()
        if isinstance(value, dict):
            return cls(**{k: v for k, v in value.items() if is_init_field(cls, k)})  # type: ignore[arg-type]
        return value

    if isinstance(compilation_config, int):
        compilation_config_instance = CompilationConfig(
            mode=CompilationMode(compilation_config)
        )
    else:
        compilation_config_instance = _make_config(
            compilation_config, CompilationConfig
        )

    structured_outputs_instance = _make_config(
        structured_outputs_config, StructuredOutputsConfig
    )
    profiler_config_instance = _make_config(profiler_config, ProfilerConfig)
    attention_config_instance = _make_config(attention_config, AttentionConfig)

    # warn about single-process data parallel usage.
    _dp_size = int(kwargs.get("data_parallel_size", 1))
    _distributed_executor_backend = kwargs.get("distributed_executor_backend")
    if (
        _dp_size > 1
        and not _distributed_executor_backend == "external_launcher"
        and not current_platform.is_tpu()
    ):
        raise ValueError(
            f"LLM(data_parallel_size={_dp_size}) is not supported for single-"
            "process usage and may hang. Please use "
            "the explicit multi-process data-parallel example at "
            "'examples/features/data_parallel/data_parallel_offline.py'."
        )

    engine_args = EngineArgs(
        model=model,
        runner=runner,
        convert=convert,
        tokenizer=tokenizer,
        tokenizer_mode=tokenizer_mode,
        skip_tokenizer_init=skip_tokenizer_init,
        trust_remote_code=trust_remote_code,
        allowed_local_media_path=allowed_local_media_path,
        allowed_media_domains=allowed_media_domains,
        tensor_parallel_size=tensor_parallel_size,
        dtype=dtype,
        quantization=quantization,
        revision=revision,
        tokenizer_revision=tokenizer_revision,
        seed=seed,
        gpu_memory_utilization=gpu_memory_utilization,
        kv_cache_memory_bytes=kv_cache_memory_bytes,
        cpu_offload_gb=cpu_offload_gb,
        offload_group_size=offload_group_size,
        offload_num_in_group=offload_num_in_group,
        offload_prefetch_step=offload_prefetch_step,
        offload_params=offload_params or set(),
        enforce_eager=enforce_eager,
        enable_return_routed_experts=enable_return_routed_experts,
        disable_custom_all_reduce=disable_custom_all_reduce,
        hf_token=hf_token,
        hf_overrides=hf_overrides,
        mm_processor_kwargs=mm_processor_kwargs,
        pooler_config=pooler_config,
        structured_outputs_config=structured_outputs_instance,
        profiler_config=profiler_config_instance,
        attention_config=attention_config_instance,
        compilation_config=compilation_config_instance,
        quantization_config=quantization_config,
        logits_processors=logits_processors,
        **kwargs,
    )

    log_non_default_args(engine_args)

    self.llm_engine = LLMEngine.from_engine_args(
        engine_args=engine_args, usage_context=UsageContext.LLM_CLASS
    )
    self.model_config = self.llm_engine.model_config
    self.engine_class = type(self.llm_engine)

    self.request_counter = Counter()
    self.default_sampling_params: dict[str, Any] | None = None

    supported_tasks = self.llm_engine.get_supported_tasks()
    self.supported_tasks = supported_tasks
    self.pooling_task = self.model_config.get_pooling_task(supported_tasks)
    if self.pooling_task is not None:
        logger.info("Supported pooling task: %s", self.pooling_task)

    self.runner_type = self.model_config.runner_type
    self.renderer = self.llm_engine.renderer
    self.chat_template = load_chat_template(chat_template)
    self.input_processor = self.llm_engine.input_processor
    self.chat_template_config = ChatTemplateConfig(chat_template=self.chat_template)
    self.pooling_io_processors = init_pooling_io_processors(
        supported_tasks=supported_tasks,
        vllm_config=self.llm_engine.vllm_config,
        renderer=self.renderer,
        chat_template_config=self.chat_template_config,
    )
    # Cache for __repr__ to avoid repeated collective_rpc calls
    self._cached_repr: str | None = None
```

### \_\_repr\__ [¶](#vllm.LLM.__repr__ "Permanent link")

Return a transformers-style hierarchical view of the model.

Source code in `vllm/entrypoints/llm.py`

```
def__repr__(self) -> str:
"""Return a transformers-style hierarchical view of the model."""
    # Cache the result to avoid repeated collective_rpc calls
    if self._cached_repr is None:
        results = self.llm_engine.collective_rpc("get_model_inspection")
        # In distributed settings, we get results from all workers
        # Just return the first one (they should all be the same)
        if results:
            self._cached_repr = results[0]
        else:
            self._cached_repr = f"LLM(model={self.model_config.model!r})"
    return self._cached_repr
```

### \_adjust\_params\_for\_parsing [¶](#vllm.LLM._adjust_params_for_parsing "Permanent link")

Set `skip_special_tokens=False` when the model encodes structured output syntax as special tokens.

Models like Gemma4 register thinking delimiters (`<|channel>`/`<channel|>`) and tool call tokens (`<|tool_call>`/`<tool_call|>`/`<|"|>`) as special tokens. The default `skip_special_tokens=True` strips them from `output.text`, breaking parsing of both reasoning blocks and tool calls.

This is a no-op for models whose structured tokens are regular text tokens (e.g. DeepSeek's `<think>`/`</think>`).

Source code in `vllm/entrypoints/llm.py`

```
def_adjust_params_for_parsing(
    self, params: Sequence[SamplingParams | PoolingParams]
) -> None:
"""Set ``skip_special_tokens=False`` when the model encodes
    structured output syntax as special tokens.

    Models like Gemma4 register thinking delimiters
    (``<|channel>``/``<channel|>``) and tool call tokens
    (``<|tool_call>``/``<tool_call|>``/``<|"|>``) as special tokens.
    The default ``skip_special_tokens=True`` strips them from
    ``output.text``, breaking parsing of both reasoning blocks and
    tool calls.

    This is a no-op for models whose structured tokens are regular
    text tokens (e.g. DeepSeek's ``<think>``/``</think>``).
    """
    # The offline API currently lacks a unified rendering pipeline.
    # Until the planned Renderer refactor is complete, we hardcode
    # this token preservation logic specifically for Gemma4 models
    # to avoid regressions on other models.
    hf_config = getattr(self.model_config, "hf_config", None)
    architectures = getattr(hf_config, "architectures", [])

    if any("Gemma4" in arch for arch in architectures):
        tokenizer = self.renderer.get_tokenizer()
        vocab = tokenizer.get_vocab()
        special_ids = set(getattr(tokenizer, "all_special_ids", []))

        # Tokens used for thinking delimiters and tool call syntax
        # that some models (Gemma4) register as special tokens.
        structured_tokens = (
            "<|channel>",
            "<channel|>",  # thinking delimiters
            "<|tool_call>",
            "<tool_call|>",  # tool call delimiters
            '<|"|>',  # string quoting in tool args
        )
        needs_special = any(
            vocab.get(tok) in special_ids
            for tok in structured_tokens
            if tok in vocab
        )
        if needs_special:
            for sp in params:
                if isinstance(sp, SamplingParams) and sp.skip_special_tokens:
                    sp.skip_special_tokens = False
```

### \_preprocess\_chat [¶](#vllm.LLM._preprocess_chat "Permanent link")

```
_preprocess_chat(
    conversations: Sequence[
        list[ChatCompletionMessageParam]
    ],
    chat_template: str | None = None,
    chat_template_content_format: ChatTemplateContentFormatOption = "auto",
    chat_template_kwargs: dict[str, Any] | None = None,
    add_generation_prompt: bool = True,
    continue_final_message: bool = False,
    tools: list[dict[str, Any]] | None = None,
    tokenization_kwargs: dict[str, Any] | None = None,
    mm_processor_kwargs: dict[str, Any] | None = None,
) -> Sequence[EngineInput]
```

Convert a list of conversations into prompts so that they can then be used as input for other LLM APIs.

Refer to [LLM.chat](https://docs.vllm.ai/en/latest/models/generative_models/#llmchat) for a complete description of the arguments.

Returns:

Type Description `Sequence[EngineInput]`

A list of `EngineInput` objects ready to be passed into LLMEngine.

Source code in `vllm/entrypoints/llm.py`

```
def_preprocess_chat(
    self,
    conversations: Sequence[list[ChatCompletionMessageParam]],
    chat_template: str | None = None,
    chat_template_content_format: ChatTemplateContentFormatOption = "auto",
    chat_template_kwargs: dict[str, Any] | None = None,
    add_generation_prompt: bool = True,
    continue_final_message: bool = False,
    tools: list[dict[str, Any]] | None = None,
    tokenization_kwargs: dict[str, Any] | None = None,
    mm_processor_kwargs: dict[str, Any] | None = None,
) -> Sequence[EngineInput]:
"""
    Convert a list of conversations into prompts so that they can then
    be used as input for other LLM APIs.

    Refer to [LLM.chat][] for a complete description of the arguments.

    Returns:
        A list of `EngineInput` objects ready to be passed into LLMEngine.
    """
    renderer = self.renderer

    chat_params = ChatParams(
        chat_template=chat_template,
        chat_template_content_format=chat_template_content_format,
        chat_template_kwargs=merge_kwargs(
            chat_template_kwargs,
            dict(
                add_generation_prompt=add_generation_prompt,
                continue_final_message=continue_final_message,
                tools=tools,
                tokenize=(
                    is_mistral_tokenizer(renderer.tokenizer)
                    or self.model_config.enable_prompt_embeds
                ),
            ),
        ),
        mm_processor_kwargs=mm_processor_kwargs,
    )
    tok_params = renderer.default_chat_tok_params.with_kwargs(
        **(tokenization_kwargs or {})
    )
    prompt_extras = (
        None
        if mm_processor_kwargs is None
        else {"mm_processor_kwargs": mm_processor_kwargs}
    )

    _, engine_inputs = renderer.render_chat(
        conversations,
        chat_params,
        tok_params,
        prompt_extras=prompt_extras,
    )

    return engine_inputs
```

### \_preprocess\_cmpl [¶](#vllm.LLM._preprocess_cmpl "Permanent link")

Convert prompt inputs from LLM APIs (other than [LLM.chat](https://docs.vllm.ai/en/latest/models/generative_models/#llmchat)) into a format that can be passed to `_add_request`.

Refer to [LLM.generate](https://docs.vllm.ai/en/latest/models/generative_models/#llmgenerate) for a complete description of the arguments.

Returns:

Type Description `Sequence[EngineInput]`

A list of `EngineInput` objects ready to be passed into LLMEngine.

Source code in `vllm/entrypoints/llm.py`

```
def_preprocess_cmpl(
    self,
    prompts: Sequence[PromptType],
    tokenization_kwargs: dict[str, Any] | None = None,
    mm_processor_kwargs: dict[str, Any] | None = None,
) -> Sequence[EngineInput]:
"""
    Convert prompt inputs from LLM APIs (other than [LLM.chat][]) into
    a format that can be passed to `_add_request`.

    Refer to [LLM.generate][] for a complete description of the arguments.

    Returns:
        A list of `EngineInput` objects ready to be passed into LLMEngine.
    """
    renderer = self.renderer
    model_config = self.model_config

    parsed_prompts = [
        parse_model_prompt(model_config, prompt) for prompt in prompts
    ]
    tok_params = renderer.default_cmpl_tok_params.with_kwargs(
        **(tokenization_kwargs or {})
    )
    prompt_extras = (
        None
        if mm_processor_kwargs is None
        else {"mm_processor_kwargs": mm_processor_kwargs}
    )

    return renderer.render_cmpl(
        parsed_prompts,
        tok_params,
        prompt_extras=prompt_extras,
    )
```

### apply\_model [¶](#vllm.LLM.apply_model "Permanent link")

Run a function directly on the model inside each worker, returning the result for each of them.

Warning

To reduce the overhead of data transfer, avoid returning large arrays or tensors from this method. If you must return them, make sure you move them to CPU first to avoid taking up additional VRAM!

Source code in `vllm/entrypoints/llm.py`

```
defapply_model(self, func: Callable[[nn.Module], _R]) -> list[_R]:
"""
    Run a function directly on the model inside each worker,
    returning the result for each of them.

    !!! warning
        To reduce the overhead of data transfer, avoid returning large
        arrays or tensors from this method. If you must return them,
        make sure you move them to CPU first to avoid taking up additional
        VRAM!
    """
    return self.llm_engine.apply_model(func)
```

### beam\_search [¶](#vllm.LLM.beam_search "Permanent link")

Generate sequences using beam search.

Parameters:

Name Type Description Default `prompts` `list[TokensPrompt | TextPrompt]`

A list of prompts. Each prompt can be a string or a list of token IDs.

*required* `params` `BeamSearchParams`

The beam search parameters.

*required* `lora_request` `list[LoRARequest] | LoRARequest | None`

LoRA request to use for generation, if any.

`None` `use_tqdm` `bool`

Whether to use tqdm to display the progress bar.

`False` `concurrency_limit` `int | None`

The maximum number of concurrent requests. If None, the number of concurrent requests is unlimited.

`None`

Source code in `vllm/entrypoints/llm.py`

```
defbeam_search(
    self,
    prompts: list[TokensPrompt | TextPrompt],
    params: BeamSearchParams,
    lora_request: list[LoRARequest] | LoRARequest | None = None,
    use_tqdm: bool = False,
    concurrency_limit: int | None = None,
) -> list[BeamSearchOutput]:
"""
    Generate sequences using beam search.

    Args:
        prompts: A list of prompts. Each prompt can be a string or a list
            of token IDs.
        params: The beam search parameters.
        lora_request: LoRA request to use for generation, if any.
        use_tqdm: Whether to use tqdm to display the progress bar.
        concurrency_limit: The maximum number of concurrent requests.
            If None, the number of concurrent requests is unlimited.
    """
    # TODO: how does beam search work together with length penalty,
    # frequency, penalty, and stopping criteria, etc.?
    beam_width = params.beam_width
    max_tokens = params.max_tokens
    temperature = params.temperature
    ignore_eos = params.ignore_eos
    length_penalty = params.length_penalty

    tokenizer = self.renderer.get_tokenizer()
    eos_token_id = tokenizer.eos_token_id
    sort_beams_key = create_sort_beams_key_function(eos_token_id, length_penalty)

    engine_inputs = self._preprocess_cmpl(prompts)
    lora_requests = self._lora_request_to_seq(lora_request, len(engine_inputs))

    if use_tqdm and concurrency_limit is not None:
        logger.warning(
            "Progress bar is not supported when using concurrency_limit. "
            "Disabling progress bar."
        )
        use_tqdm = False

    if concurrency_limit is None:
        concurrency_limit = len(engine_inputs)

    # generate 2 * beam_width candidates at each step
    # following the huggingface transformers implementation
    # at https://github.com/huggingface/transformers/blob/e15687fffe5c9d20598a19aeab721ae0a7580f8a/src/transformers/generation/beam_search.py#L534 # noqa
    sampling_params = SamplingParams(
        logprobs=2 * beam_width,
        max_tokens=1,
        temperature=temperature,
        skip_clone=True,  # Internal beam search, safe to skip clone
    )
    instances: list[BeamSearchInstance] = []

    for lora_req, prompt in zip(lora_requests, engine_inputs):
        if prompt["type"] == "embeds":
            raise NotImplementedError(
                "Embedding prompt not supported for beam search"
            )

        instances.append(
            BeamSearchInstance(
                prompt,
                lora_request=lora_req,
                logprobs=None,
            ),
        )

    for prompt_start in range(0, len(instances), concurrency_limit):
        instances_batch = instances[prompt_start : prompt_start + concurrency_limit]

        token_iter = range(max_tokens)
        if use_tqdm:
            token_iter = tqdm(
                token_iter, desc="Beam search", unit="token", unit_scale=False
            )
            logger.warning(
                "The progress bar shows the upper bound on token steps and "
                "may finish early due to stopping conditions. It does not "
                "reflect instance-level progress."
            )
        for _ in token_iter:
            all_beams: list[BeamSearchSequence] = list(
                sum((instance.beams for instance in instances_batch), [])
            )
            pos = [0] + list(
                itertools.accumulate(
                    len(instance.beams) for instance in instances_batch
                )
            )
            instance_start_and_end: list[tuple[int, int]] = list(
                zip(pos[:-1], pos[1:])
            )

            if len(all_beams) == 0:
                break

            # only runs for one step
            # we don't need to use tqdm here
            output = self._render_and_run_requests(
                prompts=(beam.get_prompt() for beam in all_beams),
                params=self._params_to_seq(sampling_params, len(all_beams)),
                output_type=RequestOutput,
                lora_requests=[beam.lora_request for beam in all_beams],
                use_tqdm=False,
            )

            for (start, end), instance in zip(
                instance_start_and_end, instances_batch
            ):
                instance_new_beams = []
                for i in range(start, end):
                    current_beam = all_beams[i]
                    result = output[i]

                    if result.outputs[0].logprobs is not None:
                        # if `result.outputs[0].logprobs` is None, it means
                        # the sequence is completed because of the
                        # max-model-len or abortion. we don't need to add
                        # it to the new beams.
                        logprobs = result.outputs[0].logprobs[0]
                        for token_id, logprob_obj in logprobs.items():
                            new_beam = BeamSearchSequence(
                                current_beam.orig_prompt,
                                tokens=current_beam.tokens + [token_id],
                                logprobs=current_beam.logprobs + [logprobs],
                                lora_request=current_beam.lora_request,
                                cum_logprob=current_beam.cum_logprob
                                + logprob_obj.logprob,
                            )

                            if token_id == eos_token_id and not ignore_eos:
                                instance.completed.append(new_beam)
                            else:
                                instance_new_beams.append(new_beam)
                sorted_beams = sorted(
                    instance_new_beams, key=sort_beams_key, reverse=True
                )
                instance.beams = sorted_beams[:beam_width]

    outputs = []
    for instance in instances:
        instance.completed.extend(instance.beams)
        sorted_completed = sorted(
            instance.completed, key=sort_beams_key, reverse=True
        )
        best_beams = sorted_completed[:beam_width]

        for beam in best_beams:
            beam.text = tokenizer.decode(beam.tokens)

        outputs.append(BeamSearchOutput(sequences=best_beams))

    return outputs
```

### chat [¶](#vllm.LLM.chat "Permanent link")

```
chat(
    messages: list[ChatCompletionMessageParam]
    | Sequence[list[ChatCompletionMessageParam]],
    sampling_params: SamplingParams
    | Sequence[SamplingParams]
    | None = None,
    use_tqdm: bool | Callable[..., tqdm] = True,
    lora_request: Sequence[LoRARequest]
    | LoRARequest
    | None = None,
    chat_template: str | None = None,
    chat_template_content_format: ChatTemplateContentFormatOption = "auto",
    add_generation_prompt: bool = True,
    continue_final_message: bool = False,
    tools: list[dict[str, Any]] | None = None,
    chat_template_kwargs: dict[str, Any] | None = None,
    tokenization_kwargs: dict[str, Any] | None = None,
    mm_processor_kwargs: dict[str, Any] | None = None,
) -> list[RequestOutput]
```

Generate responses for a chat conversation.

The chat conversation is converted into a text prompt using the tokenizer and calls the [generate](#vllm.LLM.generate "            generate") method to generate the responses.

Multi-modal inputs can be passed in the same way you would pass them to the OpenAI API.

Parameters:

Name Type Description Default `messages` `list[ChatCompletionMessageParam] | Sequence[list[ChatCompletionMessageParam]]`

A sequence of conversations or a single conversation.

- Each conversation is represented as a list of messages.
- Each message is a dictionary with 'role' and 'content' keys.

*required* `sampling_params` `SamplingParams | Sequence[SamplingParams] | None`

The sampling parameters for text generation. If None, we use the default sampling parameters. When it is a single value, it is applied to every prompt. When it is a list, the list must have the same length as the prompts and it is paired one by one with the prompt.

`None` `use_tqdm` `bool | Callable[..., tqdm]`

If `True`, shows a tqdm progress bar. If a callable (e.g., `functools.partial(tqdm, leave=False)`), it is used to create the progress bar. If `False`, no progress bar is created.

`True` `lora_request` `Sequence[LoRARequest] | LoRARequest | None`

LoRA request to use for generation, if any.

`None` `chat_template` `str | None`

The template to use for structuring the chat. If not provided, the model's default chat template will be used.

`None` `chat_template_content_format` `ChatTemplateContentFormatOption`

The format to render message content.

- "string" will render the content as a string. Example: `"Who are you?"`
- "openai" will render the content as a list of dictionaries, similar to OpenAI schema. Example: `[{"type": "text", "text": "Who are you?"}]`

`'auto'` `add_generation_prompt` `bool`

If True, adds a generation template to each message.

`True` `continue_final_message` `bool`

If True, continues the final message in the conversation instead of starting a new one. Cannot be `True` if `add_generation_prompt` is also `True`.

`False` `chat_template_kwargs` `dict[str, Any] | None`

Additional kwargs to pass to the chat template.

`None` `tokenization_kwargs` `dict[str, Any] | None`

Overrides for `tokenizer.encode`.

`None` `mm_processor_kwargs` `dict[str, Any] | None`

Overrides for `processor.__call__`.

`None`

Returns:

Type Description `list[RequestOutput]`

A list of `RequestOutput` objects containing the generated

`list[RequestOutput]`

responses in the same order as the input messages.

Source code in `vllm/entrypoints/llm.py`

```
defchat(
    self,
    messages: list[ChatCompletionMessageParam]
    | Sequence[list[ChatCompletionMessageParam]],
    sampling_params: SamplingParams | Sequence[SamplingParams] | None = None,
    use_tqdm: bool | Callable[..., tqdm] = True,
    lora_request: Sequence[LoRARequest] | LoRARequest | None = None,
    chat_template: str | None = None,
    chat_template_content_format: ChatTemplateContentFormatOption = "auto",
    add_generation_prompt: bool = True,
    continue_final_message: bool = False,
    tools: list[dict[str, Any]] | None = None,
    chat_template_kwargs: dict[str, Any] | None = None,
    tokenization_kwargs: dict[str, Any] | None = None,
    mm_processor_kwargs: dict[str, Any] | None = None,
) -> list[RequestOutput]:
"""
    Generate responses for a chat conversation.

    The chat conversation is converted into a text prompt using the
    tokenizer and calls the [generate][vllm.LLM.generate] method to generate
    the responses.

    Multi-modal inputs can be passed in the same way you would pass them
    to the OpenAI API.

    Args:
        messages: A sequence of conversations or a single conversation.

            - Each conversation is represented as a list of messages.
            - Each message is a dictionary with 'role' and 'content' keys.

        sampling_params: The sampling parameters for text generation.
            If None, we use the default sampling parameters. When it
            is a single value, it is applied to every prompt. When it
            is a list, the list must have the same length as the
            prompts and it is paired one by one with the prompt.
        use_tqdm: If `True`, shows a tqdm progress bar.
            If a callable (e.g., `functools.partial(tqdm, leave=False)`),
            it is used to create the progress bar.
            If `False`, no progress bar is created.
        lora_request: LoRA request to use for generation, if any.
        chat_template: The template to use for structuring the chat.
            If not provided, the model's default chat template will be used.
        chat_template_content_format: The format to render message content.

            - "string" will render the content as a string.
              Example: `"Who are you?"`
            - "openai" will render the content as a list of dictionaries,
              similar to OpenAI schema.
              Example: `[{"type": "text", "text": "Who are you?"}]`

        add_generation_prompt: If True, adds a generation template
            to each message.
        continue_final_message: If True, continues the final message in
            the conversation instead of starting a new one. Cannot be
            `True` if `add_generation_prompt` is also `True`.
        chat_template_kwargs: Additional kwargs to pass to the chat
            template.
        tokenization_kwargs: Overrides for `tokenizer.encode`.
        mm_processor_kwargs: Overrides for `processor.__call__`.

    Returns:
        A list of `RequestOutput` objects containing the generated
        responses in the same order as the input messages.
    """
    model_config = self.model_config
    runner_type = model_config.runner_type
    if runner_type != "generate":
        raise ValueError(
            "LLM.chat() is only supported for generative models. "
            "Try passing `--runner generate` to use the model as a "
            "generative model."
        )

    if sampling_params is None:
        sampling_params = self.get_default_sampling_params()

    return self._run_chat(
        messages=messages,
        params=sampling_params,
        output_type=RequestOutput,
        use_tqdm=use_tqdm,
        lora_request=lora_request,
        chat_template=chat_template,
        chat_template_content_format=chat_template_content_format,
        chat_template_kwargs=chat_template_kwargs,
        add_generation_prompt=add_generation_prompt,
        continue_final_message=continue_final_message,
        tools=tools,
        tokenization_kwargs=tokenization_kwargs,
        mm_processor_kwargs=mm_processor_kwargs,
    )
```

### classify [¶](#vllm.LLM.classify "Permanent link")

Generate class logits for each prompt.

This class automatically batches the given prompts, considering the memory constraint. For the best performance, put all of your prompts into a single list and pass it to this method.

Parameters:

Name Type Description Default `prompts` `PromptType | Sequence[PromptType]`

The prompts to the LLM. You may pass a sequence of prompts for batch inference. See [PromptType](https://docs.vllm.ai/en/latest/api/vllm/inputs/#vllm.inputs.PromptType "            PromptType            module-attribute   ") for more details about the format of each prompt.

*required* `pooling_params` `PoolingParams | Sequence[PoolingParams] | None`

The pooling parameters for pooling. If None, we use the default pooling parameters.

`None` `use_tqdm` `bool | Callable[..., tqdm]`

If `True`, shows a tqdm progress bar. If a callable (e.g., `functools.partial(tqdm, leave=False)`), it is used to create the progress bar. If `False`, no progress bar is created.

`True` `lora_request` `list[LoRARequest] | LoRARequest | None`

LoRA request to use for generation, if any.

`None` `tokenization_kwargs` `dict[str, Any] | None`

Overrides for `tokenizer.encode`.

`None`

Returns:

Type Description `list[ClassificationRequestOutput]`

A list of `ClassificationRequestOutput` objects containing the

`list[ClassificationRequestOutput]`

embedding vectors in the same order as the input prompts.

Source code in `vllm/entrypoints/llm.py`

```
defclassify(
    self,
    prompts: PromptType | Sequence[PromptType],
    *,
    pooling_params: PoolingParams | Sequence[PoolingParams] | None = None,
    use_tqdm: bool | Callable[..., tqdm] = True,
    lora_request: list[LoRARequest] | LoRARequest | None = None,
    tokenization_kwargs: dict[str, Any] | None = None,
) -> list[ClassificationRequestOutput]:
"""
    Generate class logits for each prompt.

    This class automatically batches the given prompts, considering
    the memory constraint. For the best performance, put all of your prompts
    into a single list and pass it to this method.

    Args:
        prompts: The prompts to the LLM. You may pass a sequence of prompts
            for batch inference. See [PromptType][vllm.inputs.PromptType]
            for more details about the format of each prompt.
        pooling_params: The pooling parameters for pooling. If None, we
            use the default pooling parameters.
        use_tqdm: If `True`, shows a tqdm progress bar.
            If a callable (e.g., `functools.partial(tqdm, leave=False)`),
            it is used to create the progress bar.
            If `False`, no progress bar is created.
        lora_request: LoRA request to use for generation, if any.
        tokenization_kwargs: Overrides for `tokenizer.encode`.

    Returns:
        A list of `ClassificationRequestOutput` objects containing the
        embedding vectors in the same order as the input prompts.
    """

    items = self.encode(
        prompts,
        use_tqdm=use_tqdm,
        pooling_params=pooling_params,
        lora_request=lora_request,
        pooling_task="classify",
        tokenization_kwargs=tokenization_kwargs,
    )

    return [ClassificationRequestOutput.from_base(item) for item in items]
```

### collective\_rpc [¶](#vllm.LLM.collective_rpc "Permanent link")

Execute an RPC call on all workers.

Parameters:

Name Type Description Default `method` `str | Callable[..., _R]`

Name of the worker method to execute, or a callable that is serialized and sent to all workers to execute.

If the method is a callable, it should accept an additional `self` argument, in addition to the arguments passed in `args` and `kwargs`. The `self` argument will be the worker object.

*required* `timeout` `float | None`

Maximum time in seconds to wait for execution. Raises a [`TimeoutError`](https://docs.python.org/3/library/exceptions.html#TimeoutError) on timeout. `None` means wait indefinitely.

`None` `args` `tuple`

Positional arguments to pass to the worker method.

`()` `kwargs` `dict[str, Any] | None`

Keyword arguments to pass to the worker method.

`None`

Returns:

Type Description `list[_R]`

A list containing the results from each worker.

Note

It is recommended to use this API to only pass control messages, and set up data-plane communication to pass data.

Source code in `vllm/entrypoints/llm.py`

```
defcollective_rpc(
    self,
    method: str | Callable[..., _R],
    timeout: float | None = None,
    args: tuple = (),
    kwargs: dict[str, Any] | None = None,
) -> list[_R]:
"""
    Execute an RPC call on all workers.

    Args:
        method: Name of the worker method to execute, or a callable that
            is serialized and sent to all workers to execute.

            If the method is a callable, it should accept an additional
            `self` argument, in addition to the arguments passed in `args`
            and `kwargs`. The `self` argument will be the worker object.
        timeout: Maximum time in seconds to wait for execution. Raises a
            [`TimeoutError`][] on timeout. `None` means wait indefinitely.
        args: Positional arguments to pass to the worker method.
        kwargs: Keyword arguments to pass to the worker method.

    Returns:
        A list containing the results from each worker.

    Note:
        It is recommended to use this API to only pass control messages,
        and set up data-plane communication to pass data.
    """

    return self.llm_engine.collective_rpc(method, timeout, args, kwargs)
```

### embed [¶](#vllm.LLM.embed "Permanent link")

Generate an embedding vector for each prompt.

This class automatically batches the given prompts, considering the memory constraint. For the best performance, put all of your prompts into a single list and pass it to this method.

Parameters:

Name Type Description Default `prompts` `PromptType | Sequence[PromptType]`

The prompts to the LLM. You may pass a sequence of prompts for batch inference. See [PromptType](https://docs.vllm.ai/en/latest/api/vllm/inputs/#vllm.inputs.PromptType "            PromptType            module-attribute   ") for more details about the format of each prompt.

*required* `pooling_params` `PoolingParams | Sequence[PoolingParams] | None`

The pooling parameters for pooling. If None, we use the default pooling parameters.

`None` `use_tqdm` `bool | Callable[..., tqdm]`

If `True`, shows a tqdm progress bar. If a callable (e.g., `functools.partial(tqdm, leave=False)`), it is used to create the progress bar. If `False`, no progress bar is created.

`True` `lora_request` `list[LoRARequest] | LoRARequest | None`

LoRA request to use for generation, if any.

`None` `tokenization_kwargs` `dict[str, Any] | None`

Overrides for `tokenizer.encode`.

`None`

Returns:

Type Description `list[EmbeddingRequestOutput]`

A list of `EmbeddingRequestOutput` objects containing the

`list[EmbeddingRequestOutput]`

embedding vectors in the same order as the input prompts.

Source code in `vllm/entrypoints/llm.py`

```
defembed(
    self,
    prompts: PromptType | Sequence[PromptType],
    *,
    use_tqdm: bool | Callable[..., tqdm] = True,
    pooling_params: PoolingParams | Sequence[PoolingParams] | None = None,
    lora_request: list[LoRARequest] | LoRARequest | None = None,
    tokenization_kwargs: dict[str, Any] | None = None,
) -> list[EmbeddingRequestOutput]:
"""
    Generate an embedding vector for each prompt.

    This class automatically batches the given prompts, considering
    the memory constraint. For the best performance, put all of your prompts
    into a single list and pass it to this method.

    Args:
        prompts: The prompts to the LLM. You may pass a sequence of prompts
            for batch inference. See [PromptType][vllm.inputs.PromptType]
            for more details about the format of each prompt.
        pooling_params: The pooling parameters for pooling. If None, we
            use the default pooling parameters.
        use_tqdm: If `True`, shows a tqdm progress bar.
            If a callable (e.g., `functools.partial(tqdm, leave=False)`),
            it is used to create the progress bar.
            If `False`, no progress bar is created.
        lora_request: LoRA request to use for generation, if any.
        tokenization_kwargs: Overrides for `tokenizer.encode`.

    Returns:
        A list of `EmbeddingRequestOutput` objects containing the
        embedding vectors in the same order as the input prompts.
    """

    items = self.encode(
        prompts,
        use_tqdm=use_tqdm,
        pooling_params=pooling_params,
        lora_request=lora_request,
        pooling_task="embed",
        tokenization_kwargs=tokenization_kwargs,
    )

    return [EmbeddingRequestOutput.from_base(item) for item in items]
```

### encode [¶](#vllm.LLM.encode "Permanent link")

Apply pooling to the hidden states corresponding to the input prompts.

This class automatically batches the given prompts, considering the memory constraint. For the best performance, put all of your prompts into a single list and pass it to this method.

Parameters:

Name Type Description Default `prompts` `PromptType | Sequence[PromptType] | DataPrompt`

The prompts to the LLM. You may pass a sequence of prompts for batch inference. See [PromptType](https://docs.vllm.ai/en/latest/api/vllm/inputs/#vllm.inputs.PromptType "            PromptType            module-attribute   ") for more details about the format of each prompt.

*required* `pooling_params` `PoolingParams | Sequence[PoolingParams] | None`

The pooling parameters for pooling. If None, we use the default pooling parameters.

`None` `use_tqdm` `bool | Callable[..., tqdm]`

If `True`, shows a tqdm progress bar. If a callable (e.g., `functools.partial(tqdm, leave=False)`), it is used to create the progress bar. If `False`, no progress bar is created.

`True` `lora_request` `list[LoRARequest] | LoRARequest | None`

LoRA request to use for generation, if any.

`None` `pooling_task` `PoolingTask | None`

Override the pooling task to use.

`None` `tokenization_kwargs` `dict[str, Any] | None`

Overrides for `tokenizer.encode`.

`None`

Returns:

Type Description `list[PoolingRequestOutput]`

A list of `PoolingRequestOutput` objects containing the

`list[PoolingRequestOutput]`

pooled hidden states in the same order as the input prompts.

Source code in `vllm/entrypoints/llm.py`

```
defencode(
    self,
    prompts: PromptType | Sequence[PromptType] | DataPrompt,
    pooling_params: PoolingParams | Sequence[PoolingParams] | None = None,
    *,
    use_tqdm: bool | Callable[..., tqdm] = True,
    lora_request: list[LoRARequest] | LoRARequest | None = None,
    pooling_task: PoolingTask | None = None,
    tokenization_kwargs: dict[str, Any] | None = None,
) -> list[PoolingRequestOutput]:
"""Apply pooling to the hidden states corresponding to the input
    prompts.

    This class automatically batches the given prompts, considering
    the memory constraint. For the best performance, put all of your prompts
    into a single list and pass it to this method.

    Args:
        prompts: The prompts to the LLM. You may pass a sequence of prompts
            for batch inference. See [PromptType][vllm.inputs.PromptType]
            for more details about the format of each prompt.
        pooling_params: The pooling parameters for pooling. If None, we
            use the default pooling parameters.
        use_tqdm: If `True`, shows a tqdm progress bar.
            If a callable (e.g., `functools.partial(tqdm, leave=False)`),
            it is used to create the progress bar.
            If `False`, no progress bar is created.
        lora_request: LoRA request to use for generation, if any.
        pooling_task: Override the pooling task to use.
        tokenization_kwargs: Overrides for `tokenizer.encode`.

    Returns:
        A list of `PoolingRequestOutput` objects containing the
        pooled hidden states in the same order as the input prompts.
    """

    if isinstance(prompts, dict) and "data" in prompts and pooling_task != "plugin":
        raise ValueError(
            "The 'data' field is only supported for the 'plugin' pooling task."
        )
    self._verify_pooling_task(pooling_task)
    assert pooling_task is not None and pooling_task in self.pooling_io_processors

    io_processor = self.pooling_io_processors[pooling_task]

    if pooling_params is None:
        pooling_params = PoolingParams()

    ctx = OfflineInputsContext(
        prompts=prompts,
        pooling_params=pooling_params,
        tokenization_kwargs=tokenization_kwargs,
    )

    engine_inputs = io_processor.pre_process_offline(ctx)
    n_inputs = len(engine_inputs)
    assert ctx.pooling_params is not None

    params_seq = self._params_to_seq(ctx.pooling_params, n_inputs)

    for param in params_seq:
        if param.task is None:
            param.task = pooling_task
        elif pooling_task == "plugin":
            # `plugin` task uses io_processor.parse_request to verify inputs.
            # We actually allow plugin to overwrite pooling_task.
            pass
        elif param.task != pooling_task:
            msg = f"You cannot overwrite {param.task=!r} with {pooling_task=!r}!"
            raise ValueError(msg)

    seq_lora_requests = self._lora_request_to_seq(lora_request, n_inputs)
    seq_priority = self._priority_to_seq(None, n_inputs)

    self._render_and_add_requests(
        prompts=engine_inputs,
        params=params_seq,
        lora_requests=seq_lora_requests,
        priorities=seq_priority,
    )

    outputs = self._run_engine(use_tqdm=use_tqdm, output_type=PoolingRequestOutput)
    outputs = io_processor.post_process_offline(
        ctx=OfflineOutputsContext(outputs=outputs)
    )
    return outputs
```

### enqueue [¶](#vllm.LLM.enqueue "Permanent link")

```
enqueue(
    prompts: PromptType | Sequence[PromptType],
    sampling_params: SamplingParams
    | Sequence[SamplingParams]
    | None = None,
    lora_request: Sequence[LoRARequest]
    | LoRARequest
    | None = None,
    priority: list[int] | None = None,
    use_tqdm: bool | Callable[..., tqdm] = True,
    tokenization_kwargs: dict[str, Any] | None = None,
    mm_processor_kwargs: dict[str, Any] | None = None,
) -> list[str]
```

Enqueue prompts for generation without waiting for completion.

This method adds requests to the engine queue but does not start processing them. Use wait\_for\_completion() to process the queued requests and get results.

Parameters:

Name Type Description Default `prompts` `PromptType | Sequence[PromptType]`

The prompts to the LLM. See generate() for details.

*required* `sampling_params` `SamplingParams | Sequence[SamplingParams] | None`

The sampling parameters for text generation.

`None` `lora_request` `Sequence[LoRARequest] | LoRARequest | None`

LoRA request to use for generation, if any.

`None` `priority` `list[int] | None`

The priority of the requests, if any.

`None` `use_tqdm` `bool | Callable[..., tqdm]`

If True, shows a tqdm progress bar while adding requests.

`True` `tokenization_kwargs` `dict[str, Any] | None`

Overrides for `tokenizer.encode`.

`None` `mm_processor_kwargs` `dict[str, Any] | None`

Overrides for `processor.__call__`.

`None`

Returns:

Type Description `list[str]`

A list of request IDs for the enqueued requests.

Source code in `vllm/entrypoints/llm.py`

```
defenqueue(
    self,
    prompts: PromptType | Sequence[PromptType],
    sampling_params: SamplingParams | Sequence[SamplingParams] | None = None,
    lora_request: Sequence[LoRARequest] | LoRARequest | None = None,
    priority: list[int] | None = None,
    use_tqdm: bool | Callable[..., tqdm] = True,
    tokenization_kwargs: dict[str, Any] | None = None,
    mm_processor_kwargs: dict[str, Any] | None = None,
) -> list[str]:
"""Enqueue prompts for generation without waiting for completion.

    This method adds requests to the engine queue but does not start
    processing them. Use wait_for_completion() to process the queued
    requests and get results.

    Args:
        prompts: The prompts to the LLM. See generate() for details.
        sampling_params: The sampling parameters for text generation.
        lora_request: LoRA request to use for generation, if any.
        priority: The priority of the requests, if any.
        use_tqdm: If True, shows a tqdm progress bar while adding requests.
        tokenization_kwargs: Overrides for `tokenizer.encode`.
        mm_processor_kwargs: Overrides for `processor.__call__`.

    Returns:
        A list of request IDs for the enqueued requests.
    """
    runner_type = self.model_config.runner_type
    if runner_type != "generate":
        raise ValueError("LLM.enqueue() is only supported for generative models.")

    if sampling_params is None:
        sampling_params = self.get_default_sampling_params()

    return self._add_completion_requests(
        prompts=prompts,
        params=sampling_params,
        use_tqdm=use_tqdm,
        lora_request=lora_request,
        priority=priority,
        tokenization_kwargs=tokenization_kwargs,
        mm_processor_kwargs=mm_processor_kwargs,
    )
```

### from\_engine\_args `classmethod` [¶](#vllm.LLM.from_engine_args "Permanent link")

Create an LLM instance from EngineArgs.

Source code in `vllm/entrypoints/llm.py`

```
@classmethod
deffrom_engine_args(cls, engine_args: EngineArgs) -> "LLM":
"""Create an LLM instance from EngineArgs."""
    return cls(**vars(engine_args))
```

### generate [¶](#vllm.LLM.generate "Permanent link")

```
generate(
    prompts: PromptType | Sequence[PromptType],
    sampling_params: SamplingParams
    | Sequence[SamplingParams]
    | None = None,
    *,
    use_tqdm: bool | Callable[..., tqdm] = True,
    lora_request: Sequence[LoRARequest]
    | LoRARequest
    | None = None,
    priority: list[int] | None = None,
    tokenization_kwargs: dict[str, Any] | None = None,
    mm_processor_kwargs: dict[str, Any] | None = None,
) -> list[RequestOutput]
```

Generates the completions for the input prompts.

This class automatically batches the given prompts, considering the memory constraint. For the best performance, put all of your prompts into a single list and pass it to this method.

Parameters:

Name Type Description Default `prompts` `PromptType | Sequence[PromptType]`

The prompts to the LLM. You may pass a sequence of prompts for batch inference. See [PromptType](https://docs.vllm.ai/en/latest/api/vllm/inputs/#vllm.inputs.PromptType "            PromptType            module-attribute   ") for more details about the format of each prompt.

*required* `sampling_params` `SamplingParams | Sequence[SamplingParams] | None`

The sampling parameters for text generation. If None, we use the default sampling parameters. When it is a single value, it is applied to every prompt. When it is a list, the list must have the same length as the prompts and it is paired one by one with the prompt.

`None` `use_tqdm` `bool | Callable[..., tqdm]`

If `True`, shows a tqdm progress bar. If a callable (e.g., `functools.partial(tqdm, leave=False)`), it is used to create the progress bar. If `False`, no progress bar is created.

`True` `lora_request` `Sequence[LoRARequest] | LoRARequest | None`

LoRA request to use for generation, if any.

`None` `priority` `list[int] | None`

The priority of the requests, if any. Only applicable when priority scheduling policy is enabled. If provided, must be a list of integers matching the length of `prompts`, where each priority value corresponds to the prompt at the same index.

`None` `tokenization_kwargs` `dict[str, Any] | None`

Overrides for `tokenizer.encode`.

`None` `mm_processor_kwargs` `dict[str, Any] | None`

Overrides for `processor.__call__`.

`None`

Returns:

Type Description `list[RequestOutput]`

A list of `RequestOutput` objects containing the

`list[RequestOutput]`

generated completions in the same order as the input prompts.

Source code in `vllm/entrypoints/llm.py`

```
defgenerate(
    self,
    prompts: PromptType | Sequence[PromptType],
    sampling_params: SamplingParams | Sequence[SamplingParams] | None = None,
    *,
    use_tqdm: bool | Callable[..., tqdm] = True,
    lora_request: Sequence[LoRARequest] | LoRARequest | None = None,
    priority: list[int] | None = None,
    tokenization_kwargs: dict[str, Any] | None = None,
    mm_processor_kwargs: dict[str, Any] | None = None,
) -> list[RequestOutput]:
"""Generates the completions for the input prompts.

    This class automatically batches the given prompts, considering
    the memory constraint. For the best performance, put all of your prompts
    into a single list and pass it to this method.

    Args:
        prompts: The prompts to the LLM. You may pass a sequence of prompts
            for batch inference. See [PromptType][vllm.inputs.PromptType]
            for more details about the format of each prompt.
        sampling_params: The sampling parameters for text generation. If
            None, we use the default sampling parameters.
            When it is a single value, it is applied to every prompt.
            When it is a list, the list must have the same length as the
            prompts and it is paired one by one with the prompt.
        use_tqdm: If `True`, shows a tqdm progress bar.
            If a callable (e.g., `functools.partial(tqdm, leave=False)`),
            it is used to create the progress bar.
            If `False`, no progress bar is created.
        lora_request: LoRA request to use for generation, if any.
        priority: The priority of the requests, if any.
            Only applicable when priority scheduling policy is enabled.
            If provided, must be a list of integers matching the length
            of `prompts`, where each priority value corresponds to the prompt
            at the same index.
        tokenization_kwargs: Overrides for `tokenizer.encode`.
        mm_processor_kwargs: Overrides for `processor.__call__`.

    Returns:
        A list of `RequestOutput` objects containing the
        generated completions in the same order as the input prompts.
    """
    runner_type = self.model_config.runner_type
    if runner_type != "generate":
        raise ValueError(
            "LLM.generate() is only supported for generative models. "
            "Try passing `--runner generate` to use the model as a "
            "generative model."
        )

    if sampling_params is None:
        sampling_params = self.get_default_sampling_params()

    return self._run_completion(
        prompts=prompts,
        params=sampling_params,
        output_type=RequestOutput,
        use_tqdm=use_tqdm,
        lora_request=lora_request,
        tokenization_kwargs=tokenization_kwargs,
        priority=priority,
        mm_processor_kwargs=mm_processor_kwargs,
    )
```

### get\_metrics [¶](#vllm.LLM.get_metrics "Permanent link")

Return a snapshot of aggregated metrics from Prometheus.

Returns:

Type Description `list[Metric]`

A `MetricSnapshot` instance capturing the current state

`list[Metric]`

of all aggregated metrics from Prometheus.

Note

This method is only available with the V1 LLM engine.

Source code in `vllm/entrypoints/llm.py`

```
defget_metrics(self) -> list["Metric"]:
"""Return a snapshot of aggregated metrics from Prometheus.

    Returns:
        A `MetricSnapshot` instance capturing the current state
        of all aggregated metrics from Prometheus.

    Note:
        This method is only available with the V1 LLM engine.
    """
    return self.llm_engine.get_metrics()
```

### get\_world\_size [¶](#vllm.LLM.get_world_size "Permanent link")

```
get_world_size(include_dp: bool = True) -> int
```

Get the world size from the parallel config.

Parameters:

Name Type Description Default `include_dp` `bool`

If True (default), returns the world size including data parallelism (TP * PP * DP). If False, returns the world size without data parallelism (TP * PP).

`True`

Returns:

Type Description `int`

The world size (tensor\_parallel\_size * pipeline\_parallel\_size),

`int`

optionally multiplied by data\_parallel\_size if include\_dp is True.

Source code in `vllm/entrypoints/llm.py`

```
defget_world_size(self, include_dp: bool = True) -> int:
"""Get the world size from the parallel config.

    Args:
        include_dp: If True (default), returns the world size including
            data parallelism (TP * PP * DP). If False, returns the world
            size without data parallelism (TP * PP).

    Returns:
        The world size (tensor_parallel_size * pipeline_parallel_size),
        optionally multiplied by data_parallel_size if include_dp is True.
    """
    parallel_config = self.llm_engine.vllm_config.parallel_config
    if include_dp:
        return parallel_config.world_size_across_dp
    return parallel_config.world_size
```

### init\_weight\_transfer\_engine [¶](#vllm.LLM.init_weight_transfer_engine "Permanent link")

Initialize weight transfer for RL training.

Parameters:

Name Type Description Default `request` `WeightTransferInitRequest | dict`

Weight transfer initialization request with backend-specific info

*required*

Source code in `vllm/entrypoints/llm.py`

```
definit_weight_transfer_engine(
    self, request: WeightTransferInitRequest | dict
) -> None:
"""
    Initialize weight transfer for RL training.

    Args:
        request: Weight transfer initialization request with backend-specific info
    """
    init_info_dict = (
        request["init_info"] if isinstance(request, dict) else request.init_info
    )

    self.llm_engine.collective_rpc(
        "init_weight_transfer_engine", kwargs={"init_info": init_info_dict}
    )
```

### reward [¶](#vllm.LLM.reward "Permanent link")

Generate rewards for each prompt.

Parameters:

Name Type Description Default `prompts` `PromptType | Sequence[PromptType]`

The prompts to the LLM. You may pass a sequence of prompts for batch inference. See [PromptType](https://docs.vllm.ai/en/latest/api/vllm/inputs/#vllm.inputs.PromptType "            PromptType            module-attribute   ") for more details about the format of each prompt.

*required* `pooling_params` `PoolingParams | Sequence[PoolingParams] | None`

The pooling parameters for pooling. If None, we use the default pooling parameters.

`None` `use_tqdm` `bool | Callable[..., tqdm]`

If `True`, shows a tqdm progress bar. If a callable (e.g., `functools.partial(tqdm, leave=False)`), it is used to create the progress bar. If `False`, no progress bar is created.

`True` `lora_request` `list[LoRARequest] | LoRARequest | None`

LoRA request to use for generation, if any.

`None` `tokenization_kwargs` `dict[str, Any] | None`

Overrides for `tokenizer.encode`.

`None`

Returns:

Type Description `list[PoolingRequestOutput]`

A list of `PoolingRequestOutput` objects containing the

`list[PoolingRequestOutput]`

pooled hidden states in the same order as the input prompts.

Source code in `vllm/entrypoints/llm.py`

```
defreward(
    self,
    prompts: PromptType | Sequence[PromptType],
    /,
    *,
    pooling_params: PoolingParams | Sequence[PoolingParams] | None = None,
    use_tqdm: bool | Callable[..., tqdm] = True,
    lora_request: list[LoRARequest] | LoRARequest | None = None,
    tokenization_kwargs: dict[str, Any] | None = None,
) -> list[PoolingRequestOutput]:
"""
    Generate rewards for each prompt.

    Args:
        prompts: The prompts to the LLM. You may pass a sequence of prompts
            for batch inference. See [PromptType][vllm.inputs.PromptType]
            for more details about the format of each prompt.
        pooling_params: The pooling parameters for pooling. If None, we
            use the default pooling parameters.
        use_tqdm: If `True`, shows a tqdm progress bar.
            If a callable (e.g., `functools.partial(tqdm, leave=False)`),
            it is used to create the progress bar.
            If `False`, no progress bar is created.
        lora_request: LoRA request to use for generation, if any.
        tokenization_kwargs: Overrides for `tokenizer.encode`.

    Returns:
        A list of `PoolingRequestOutput` objects containing the
        pooled hidden states in the same order as the input prompts.
    """
    logger.warning_once(
        "`llm.reward` api is deprecated and will be removed in v0.23. "
        'Please use `LLM.encode` with `pooling_task="classify"` or '
        '`pooling_task="token_classify"` instead.'
    )
    return self.encode(
        prompts,
        use_tqdm=use_tqdm,
        lora_request=lora_request,
        pooling_params=pooling_params,
        pooling_task="token_classify",
        tokenization_kwargs=tokenization_kwargs,
    )
```

### score [¶](#vllm.LLM.score "Permanent link")

```
score(
    data_1: ScoreInput | list[ScoreInput],
    data_2: ScoreInput | list[ScoreInput],
    /,
    *,
    use_tqdm: bool | Callable[..., tqdm] = True,
    pooling_params: PoolingParams | None = None,
    lora_request: list[LoRARequest]
    | LoRARequest
    | None = None,
    tokenization_kwargs: dict[str, Any] | None = None,
    chat_template: str | None = None,
) -> list[ScoringRequestOutput]
```

Generate similarity scores for all pairs `<text,text_pair>` or `<multi-modal data, multi-modal data pair>`.

The inputs can be `1 -> 1`, `1 -> N` or `N -> N`. In the `1 - N` case the `data_1` input will be replicated `N` times to pair with the `data_2` inputs. The input pairs are used to build a list of prompts for the cross encoder model. This class automatically batches the prompts, considering the memory constraint. For the best performance, put all of your inputs into a single list and pass it to this method.

Supports both text and multi-modal data (images, etc.) when used with appropriate multi-modal models. For multi-modal inputs, ensure the prompt structure matches the model's expected input format.

Parameters:

Name Type Description Default `data_1` `ScoreInput | list[ScoreInput]`

Can be a single prompt, a list of prompts or `ScoreMultiModalParam`, which can contain either text or multi-modal data. When a list, it must have the same length as the `data_2` list.

*required* `data_2` `ScoreInput | list[ScoreInput]`

The data to pair with the query to form the input to the LLM. Can be text or multi-modal data. See [PromptType](https://docs.vllm.ai/en/latest/api/vllm/inputs/#vllm.inputs.PromptType "            PromptType            module-attribute   ") for more details about the format of each prompt.

*required* `pooling_params` `PoolingParams | None`

The pooling parameters for pooling. If None, we use the default pooling parameters.

`None` `use_tqdm` `bool | Callable[..., tqdm]`

If `True`, shows a tqdm progress bar. If a callable (e.g., `functools.partial(tqdm, leave=False)`), it is used to create the progress bar. If `False`, no progress bar is created.

`True` `lora_request` `list[LoRARequest] | LoRARequest | None`

LoRA request to use for generation, if any.

`None` `chat_template` `str | None`

The chat template to use for the scoring. If None, we use the model's default chat template.

`None` `tokenization_kwargs` `dict[str, Any] | None`

Overrides for `tokenizer.encode`.

`None`

Returns: A list of `ScoringRequestOutput` objects containing the generated scores in the same order as the input prompts.

Source code in `vllm/entrypoints/llm.py`

```
defscore(
    self,
    data_1: ScoreInput | list[ScoreInput],
    data_2: ScoreInput | list[ScoreInput],
    /,
    *,
    use_tqdm: bool | Callable[..., tqdm] = True,
    pooling_params: PoolingParams | None = None,
    lora_request: list[LoRARequest] | LoRARequest | None = None,
    tokenization_kwargs: dict[str, Any] | None = None,
    chat_template: str | None = None,
) -> list[ScoringRequestOutput]:
"""Generate similarity scores for all pairs `<text,text_pair>` or
      `<multi-modal data, multi-modal data pair>`.

    The inputs can be `1 -> 1`, `1 -> N` or `N -> N`.
    In the `1 - N` case the `data_1` input will be replicated `N`
    times to pair with the `data_2` inputs.
    The input pairs are used to build a list of prompts for the
    cross encoder model. This class automatically batches the prompts,
    considering the memory constraint. For the best performance, put all
    of your inputs into a single list and pass it to this method.

    Supports both text and multi-modal data (images, etc.) when used with
    appropriate multi-modal models. For multi-modal inputs, ensure the
    prompt structure matches the model's expected input format.

    Args:
        data_1: Can be a single prompt, a list of prompts or
            `ScoreMultiModalParam`, which can contain either text or
            multi-modal data. When a list, it must have the same length as
            the `data_2` list.
        data_2: The data to pair with the query to form the input to
            the LLM. Can be text or multi-modal data. See [PromptType]
            [vllm.inputs.PromptType] for more details about the format of
            each prompt.
        pooling_params: The pooling parameters for pooling. If None, we
            use the default pooling parameters.
        use_tqdm: If `True`, shows a tqdm progress bar.
            If a callable (e.g., `functools.partial(tqdm, leave=False)`),
            it is used to create the progress bar.
            If `False`, no progress bar is created.
        lora_request: LoRA request to use for generation, if any.
        chat_template: The chat template to use for the scoring. If None, we
            use the model's default chat template.
        tokenization_kwargs: Overrides for `tokenizer.encode`.
    Returns:
        A list of `ScoringRequestOutput` objects containing the
        generated scores in the same order as the input prompts.
    """

    if self.runner_type != "pooling":
        raise ValueError(
            "LLM.score() is only supported for pooling models. "
            "Try passing `--runner pooling` to use the model as a "
            "pooling model."
        )

    score_type: str | None = SCORE_TYPE_MAP.get(self.pooling_task, None)  # type: ignore[arg-type]
    if (
        score_type == "cross-encoder"
        and getattr(self.model_config.hf_config, "num_labels", 0) != 1
    ):
        raise ValueError("Scoring API is only enabled for num_labels == 1.")

    if score_type is None or score_type not in self.pooling_io_processors:
        raise ValueError("This model does not support the Scoring API.")

    io_processor = self.pooling_io_processors[score_type]
    assert isinstance(io_processor, ScoringIOProcessor)

    pooling_task = io_processor.pooling_task
    scoring_data = io_processor.valid_inputs(data_1, data_2)
    n_queries = len(scoring_data.data_1)

    if pooling_params is None:
        pooling_params = PoolingParams()

    ctx = OfflineInputsContext(
        prompts=scoring_data,
        pooling_params=pooling_params,
        tokenization_kwargs=tokenization_kwargs,
        chat_template=chat_template,
        n_queries=n_queries,
    )

    engine_inputs = io_processor.pre_process_offline(ctx)
    n_inputs = len(engine_inputs)

    seq_lora_requests = self._lora_request_to_seq(lora_request, n_inputs)
    params_seq = self._params_to_seq(ctx.pooling_params, n_inputs)

    for param in params_seq:
        if param.task is None:
            param.task = pooling_task
        elif param.task != pooling_task:
            msg = f"You cannot overwrite {param.task=!r} with {pooling_task=!r}!"
            raise ValueError(msg)

    seq_priority = self._priority_to_seq(None, n_inputs)

    self._render_and_add_requests(
        prompts=engine_inputs,
        params=params_seq,
        lora_requests=seq_lora_requests,
        priorities=seq_priority,
    )

    outputs = self._run_engine(use_tqdm=use_tqdm, output_type=PoolingRequestOutput)
    outputs = io_processor.post_process_offline(
        ctx=OfflineOutputsContext(outputs=outputs, n_queries=n_queries),
    )

    return [ScoringRequestOutput.from_base(item) for item in outputs]
```

### sleep [¶](#vllm.LLM.sleep "Permanent link")

```
sleep(level: int = 1, mode: PauseMode = 'abort')
```

Put the engine to sleep. The engine should not process any requests. The caller should guarantee that no requests are being processed during the sleep period, before `wake_up` is called.

Parameters:

Name Type Description Default `level` `int`

The sleep level. - Level 0: Pause scheduling but continue accepting requests. Requests are queued but not processed. - Level 1: Offload model weights to CPU, discard KV cache. The content of kv cache is forgotten. Good for sleeping and waking up the engine to run the same model again. Please make sure there's enough CPU memory to store the model weights. - Level 2: Discard all GPU memory (weights + KV cache). Good for sleeping and waking up the engine to run a different model or update the model, where previous model weights are not needed. It reduces CPU memory pressure.

`1` `mode` `PauseMode`

How to handle any existing requests, can be "abort", "wait", or "keep".

`'abort'`

Source code in `vllm/entrypoints/llm.py`

```
defsleep(self, level: int = 1, mode: PauseMode = "abort"):
"""
    Put the engine to sleep. The engine should not process any requests.
    The caller should guarantee that no requests are being processed
    during the sleep period, before `wake_up` is called.

    Args:
        level: The sleep level.
            - Level 0: Pause scheduling but continue accepting requests.
                       Requests are queued but not processed.
            - Level 1: Offload model weights to CPU, discard KV cache.
                       The content of kv cache is forgotten. Good for
                       sleeping and waking up the engine to run the same
                       model again. Please make sure there's enough CPU
                       memory to store the model weights.
            - Level 2: Discard all GPU memory (weights + KV cache).
                       Good for sleeping and waking up the engine to run
                       a different model or update the model, where
                       previous model weights are not needed. It reduces
                       CPU memory pressure.
        mode: How to handle any existing requests, can be "abort", "wait",
            or "keep".
    """
    self.llm_engine.sleep(level=level, mode=mode)
```

### start\_profile [¶](#vllm.LLM.start_profile "Permanent link")

```
start_profile(profile_prefix: str | None = None) -> None
```

Start profiling with optional custom trace prefix.

Parameters:

Name Type Description Default `profile_prefix` `str | None`

Optional prefix for the trace file names. If provided, trace files will be named as "\_dp\_pp\_tp". If not provided, default naming will be used.

`None`

Source code in `vllm/entrypoints/llm.py`

```
defstart_profile(self, profile_prefix: str | None = None) -> None:
"""Start profiling with optional custom trace prefix.

    Args:
        profile_prefix: Optional prefix for the trace file names. If provided,
                       trace files will be named as "<prefix>_dp<X>_pp<Y>_tp<Z>".
                       If not provided, default naming will be used.
    """
    self.llm_engine.start_profile(profile_prefix)
```

### update\_weights [¶](#vllm.LLM.update_weights "Permanent link")

Update the weights of the model.

Parameters:

Name Type Description Default `request` `WeightTransferUpdateRequest | dict`

Weight update request with backend-specific update info

*required*

Source code in `vllm/entrypoints/llm.py`

```
defupdate_weights(self, request: WeightTransferUpdateRequest | dict) -> None:
"""
    Update the weights of the model.

    Args:
        request: Weight update request with backend-specific update info
    """
    update_info_dict = (
        request["update_info"] if isinstance(request, dict) else request.update_info
    )

    self.llm_engine.collective_rpc(
        "update_weights", kwargs={"update_info": update_info_dict}
    )
```

### wait\_for\_completion [¶](#vllm.LLM.wait_for_completion "Permanent link")

Wait for all enqueued requests to complete and return results.

This method processes all requests currently in the engine queue and returns their outputs. Use after enqueue() to get results.

Parameters:

Name Type Description Default `output_type` `type[Any] | tuple[type[Any], ...] | None`

The expected output type, defaults to RequestOutput.

`None` `use_tqdm` `bool | Callable[..., tqdm]`

If True, shows a tqdm progress bar.

`True`

Returns:

Type Description `list[Any]`

A list of output objects for all completed requests.

Source code in `vllm/entrypoints/llm.py`

```
defwait_for_completion(
    self,
    output_type: type[Any] | tuple[type[Any], ...] | None = None,
    *,
    use_tqdm: bool | Callable[..., tqdm] = True,
) -> list[Any]:
"""Wait for all enqueued requests to complete and return results.

    This method processes all requests currently in the engine queue
    and returns their outputs. Use after enqueue() to get results.

    Args:
        output_type: The expected output type, defaults to RequestOutput.
        use_tqdm: If True, shows a tqdm progress bar.

    Returns:
        A list of output objects for all completed requests.
    """
    if output_type is None:
        output_type = (RequestOutput, PoolingRequestOutput)

    return self._run_engine(output_type, use_tqdm=use_tqdm)
```

### wake\_up [¶](#vllm.LLM.wake_up "Permanent link")

```
wake_up(tags: list[str] | None = None)
```

Wake up the engine from sleep mode. See the [sleep](#vllm.LLM.sleep "            sleep") method for more details.

Parameters:

Name Type Description Default `tags` `list[str] | None`

An optional list of tags to reallocate the engine memory for specific memory allocations. Values must be in `("weights", "kv_cache", "scheduling")`. If None, all memory is reallocated. wake\_up should be called with all tags (or None) before the engine is used again. Use tags=\["scheduling"] to resume from level 0 sleep.

`None`

Source code in `vllm/entrypoints/llm.py`

```
defwake_up(self, tags: list[str] | None = None):
"""
    Wake up the engine from sleep mode. See the [sleep][vllm.LLM.sleep]
    method for more details.

    Args:
        tags: An optional list of tags to reallocate the engine memory
            for specific memory allocations. Values must be in
            `("weights", "kv_cache", "scheduling")`. If None, all memory
            is reallocated. wake_up should be called with all tags
            (or None) before the engine is used again.
            Use tags=["scheduling"] to resume from level 0 sleep.
    """
    self.llm_engine.wake_up(tags)
```

## PoolingOutput `dataclass` [¶](#vllm.PoolingOutput "Permanent link")

The output data of one pooling output of a request.

Parameters:

Name Type Description Default `data` `Tensor`

The extracted hidden states.

*required*

Source code in `vllm/outputs.py`

```
@dataclass
classPoolingOutput:
"""The output data of one pooling output of a request.

    Args:
        data: The extracted hidden states.
    """

    data: torch.Tensor

    def__repr__(self) -> str:
        return f"PoolingOutput(data={self.data})"

    def__eq__(self, other: object) -> bool:
        return isinstance(other, self.__class__) and bool(
            (self.data == other.data).all()
        )
```

## PoolingParams [¶](#vllm.PoolingParams "Permanent link")

Bases: `Struct`

API parameters for pooling models.

Attributes:

Name Type Description `use_activation` `bool | None`

Whether to apply activation function to the pooler outputs. `None` uses the pooler's default, which is `True` in most cases.

`dimensions` `int | None`

Reduce the dimensions of embeddings if model support matryoshka representation.

Source code in `vllm/pooling_params.py`

```
classPoolingParams(
    msgspec.Struct,
    omit_defaults=True,  # type: ignore[call-arg]
    array_like=True,
):  # type: ignore[call-arg]
"""API parameters for pooling models.

    Attributes:
        use_activation: Whether to apply activation function to the pooler outputs.
            `None` uses the pooler's default, which is `True` in most cases.
        dimensions: Reduce the dimensions of embeddings
            if model support matryoshka representation.
    """

    # --8<-- [start:common-pooling-params]
    use_activation: bool | None = None
    # --8<-- [end:common-pooling-params]

    ## for embeddings models
    # --8<-- [start:embed-pooling-params]
    dimensions: int | None = None
    # --8<-- [end:embed-pooling-params]

    ## for step pooling models
    step_tag_id: int | None = None
    returned_token_ids: list[int] | None = None

    ## Internal use only
    task: PoolingTask | None = None
    requires_token_ids: bool = False
    skip_reading_prefix_cache: bool | None = None
    late_interaction_params: LateInteractionParams | None = None
    extra_kwargs: dict[str, Any] | None = None
    output_kind: RequestOutputKind = RequestOutputKind.FINAL_ONLY

    @property
    defall_parameters(self) -> list[str]:
        return ["dimensions", "use_activation"]

    @property
    defvalid_parameters(self):
        return {
            "embed": ["dimensions", "use_activation"],
            "classify": ["use_activation"],
            "token_embed": ["dimensions", "use_activation"],
            "token_classify": ["use_activation"],
        }

    defclone(self) -> "PoolingParams":
"""Returns a deep copy of the PoolingParams instance."""
        return deepcopy(self)

    defverify(self, model_config: ModelConfig) -> None:
        # plugin task uses io_processor.parse_request to verify inputs,
        # skipping PoolingParams verify
        if self.task == "plugin":
            if self.skip_reading_prefix_cache is None:
                self.skip_reading_prefix_cache = True
            return

        # skipping verify, let plugins configure and validate pooling params
        if self.task not in self.valid_parameters:
            return

        # NOTE: Task validation needs to done against the model instance,
        # which is not available in model config. So, it's not included
        # in this method
        self._merge_default_parameters(model_config)
        self._set_default_parameters(model_config)
        self._verify_valid_parameters()

    def_merge_default_parameters(self, model_config: ModelConfig) -> None:
        pooler_config = model_config.pooler_config
        if pooler_config is None:
            return

        assert self.task is not None, "task must be set"
        valid_parameters = self.valid_parameters[self.task]

        for k in valid_parameters:
            if getattr(pooler_config, k, None) is None:
                continue

            if getattr(self, k, None) is None:
                setattr(self, k, getattr(pooler_config, k))

        if self.skip_reading_prefix_cache is None:
            # If prefix caching is enabled,
            # the output of all pooling may less than n_prompt_tokens,
            # we need to skip reading cache at this request.
            if self.task in ["token_embed", "token_classify"]:
                self.skip_reading_prefix_cache = True
            else:
                self.skip_reading_prefix_cache = False

        self._verify_step_pooling(pooler_config, valid_parameters)

    def_verify_step_pooling(
        self,
        pooler_config: PoolerConfig,
        valid_parameters: list[str],
    ):
        step_pooling_parameters = ["step_tag_id", "returned_token_ids"]
        if pooler_config.tok_pooling_type != "STEP":
            invalid_parameters = []
            for k in step_pooling_parameters:
                if getattr(self, k, None) is not None:
                    invalid_parameters.append(k)

            if invalid_parameters:
                raise ValueError(
                    f"Task {self.task} only supports {valid_parameters} "
                    f"parameters, does not support "
                    f"{invalid_parameters} parameters"
                )
        else:
            for k in step_pooling_parameters:
                if getattr(pooler_config, k, None) is None:
                    continue

                if getattr(self, k, None) is None:
                    setattr(self, k, getattr(pooler_config, k))

    def_set_default_parameters(self, model_config: ModelConfig):
        if self.task in ["embed", "token_embed"]:
            if self.use_activation is None:
                self.use_activation = True

            if self.dimensions is not None:
                if not model_config.is_matryoshka:
                    raise ValueError(
                        f'Model "{model_config.served_model_name}" does not '
                        f"support matryoshka representation, "
                        f"changing output dimensions will lead to poor results."
                    )

                mds = model_config.matryoshka_dimensions
                if mds is not None:
                    if self.dimensions not in mds:
                        raise ValueError(
                            f"Model {model_config.served_model_name!r} "
                            f"only supports {str(mds)} matryoshka dimensions, "
                            f"use other output dimensions will "
                            f"lead to poor results."
                        )
                elif self.dimensions < 1:
                    raise ValueError("Dimensions must be greater than 0")

        elif self.task in ["classify", "token_classify"]:
            if self.use_activation is None:
                self.use_activation = True
        else:
            raise ValueError(f"Unknown pooling task: {self.task!r}")

    def_verify_valid_parameters(self):
        assert self.task is not None, "task must be set"
        valid_parameters = self.valid_parameters[self.task]
        invalid_parameters = []
        for k in self.all_parameters:
            if k in valid_parameters:
                continue

            if getattr(self, k, None) is not None:
                invalid_parameters.append(k)

        if invalid_parameters:
            raise ValueError(
                f"Task {self.task!r} only supports {valid_parameters} "
                f"parameters, does not support "
                f"{invalid_parameters} parameters"
            )

    def__repr__(self) -> str:
        return (
            f"PoolingParams("
            f"task={self.task}, "
            f"dimensions={self.dimensions}, "
            f"use_activation={self.use_activation}, "
            f"step_tag_id={self.step_tag_id}, "
            f"returned_token_ids={self.returned_token_ids}, "
            f"requires_token_ids={self.requires_token_ids}, "
            f"skip_reading_prefix_cache={self.skip_reading_prefix_cache}, "
            f"late_interaction_params={self.late_interaction_params}, "
            f"extra_kwargs={self.extra_kwargs})"
        )

    def__post_init__(self) -> None:
        assert self.output_kind == RequestOutputKind.FINAL_ONLY, (
            "For pooling output_kind has to be FINAL_ONLY"
        )
```

### clone [¶](#vllm.PoolingParams.clone "Permanent link")

Returns a deep copy of the PoolingParams instance.

Source code in `vllm/pooling_params.py`

```
defclone(self) -> "PoolingParams":
"""Returns a deep copy of the PoolingParams instance."""
    return deepcopy(self)
```

## PoolingRequestOutput [¶](#vllm.PoolingRequestOutput "Permanent link")

Bases: `Generic[_O]`

The output data of a pooling request to the LLM.

Parameters:

Name Type Description Default `request_id` `str`

A unique identifier for the pooling request.

*required* `outputs` `PoolingOutput`

The pooling results for the given input.

*required* `prompt_token_ids` `list[int]`

A list of token IDs used in the prompt.

*required* `num_cached_tokens` `int`

The number of tokens with prefix cache hit.

*required* `finished` `bool`

A flag indicating whether the pooling is completed.

*required*

Source code in `vllm/outputs.py`

```
classPoolingRequestOutput(Generic[_O]):
"""
    The output data of a pooling request to the LLM.

    Args:
        request_id (str): A unique identifier for the pooling request.
        outputs (PoolingOutput): The pooling results for the given input.
        prompt_token_ids (list[int]): A list of token IDs used in the prompt.
        num_cached_tokens: The number of tokens with prefix cache hit.
        finished (bool): A flag indicating whether the pooling is completed.
    """

    def__init__(
        self,
        request_id: str,
        outputs: _O,
        prompt_token_ids: list[int],
        num_cached_tokens: int,
        finished: bool,
    ):
        self.request_id = request_id
        self.prompt_token_ids = prompt_token_ids
        self.num_cached_tokens = num_cached_tokens
        self.finished = finished
        self.outputs = outputs

    def__repr__(self):
        return (
            f"{type(self).__name__}(request_id={self.request_id!r}, "
            f"outputs={self.outputs!r}, "
            f"prompt_token_ids={self.prompt_token_ids}, "
            f"num_cached_tokens={self.num_cached_tokens}, "
            f"finished={self.finished})"
        )
```

## RequestOutput [¶](#vllm.RequestOutput "Permanent link")

The output data of a completion request to the LLM.

Parameters:

Name Type Description Default `request_id` `str`

The unique ID of the request.

*required* `prompt` `str | None`

The prompt string of the request. For encoder/decoder models, this is the decoder input prompt.

*required* `prompt_token_ids` `list[int] | None`

The token IDs of the prompt. For encoder/decoder models, this is the decoder input prompt token ids.

*required* `prompt_logprobs` `PromptLogprobs | None`

The log probabilities to return per prompt token.

*required* `outputs` `list[CompletionOutput]`

The output sequences of the request.

*required* `finished` `bool`

Whether the whole request is finished.

*required* `metrics` `RequestStateStats | None`

Metrics associated with the request.

`None` `lora_request` `LoRARequest | None`

The LoRA request that was used to generate the output.

`None` `encoder_prompt` `str | None`

The encoder prompt string of the request. None if decoder-only.

`None` `encoder_prompt_token_ids` `list[int] | None`

The token IDs of the encoder prompt. None if decoder-only.

`None` `num_cached_tokens` `int | None`

The number of tokens with prefix cache hit.

`None` `kv_transfer_params` `dict[str, Any] | None`

The params for remote K/V transfer.

`None`

Source code in `vllm/outputs.py`

```
classRequestOutput:
"""The output data of a completion request to the LLM.

    Args:
        request_id: The unique ID of the request.
        prompt: The prompt string of the request.
                For encoder/decoder models, this is the
                decoder input prompt.
        prompt_token_ids: The token IDs of the prompt.
                          For encoder/decoder models, this is the
                          decoder input prompt token ids.
        prompt_logprobs: The log probabilities to return per prompt token.
        outputs: The output sequences of the request.
        finished: Whether the whole request is finished.
        metrics: Metrics associated with the request.
        lora_request: The LoRA request that was used to generate the output.
        encoder_prompt: The encoder prompt string of the request.
                        None if decoder-only.
        encoder_prompt_token_ids: The token IDs of the encoder prompt.
                                  None if decoder-only.
        num_cached_tokens: The number of tokens with prefix cache hit.
        kv_transfer_params: The params for remote K/V transfer.
    """

    def__init__(
        self,
        request_id: str,
        prompt: str | None,
        prompt_token_ids: list[int] | None,
        prompt_logprobs: PromptLogprobs | None,
        outputs: list[CompletionOutput],
        finished: bool,
        metrics: RequestStateStats | None = None,
        lora_request: LoRARequest | None = None,
        encoder_prompt: str | None = None,
        encoder_prompt_token_ids: list[int] | None = None,
        num_cached_tokens: int | None = None,
        *,
        kv_transfer_params: dict[str, Any] | None = None,
        prompt_routed_experts: np.ndarray | None = None,
        # Forward compatibility, code that uses args added in new release can
        # still run with older versions of vLLM without breaking.
        **kwargs: Any,
    ) -> None:
        if kwargs:
            logger.warning_once(
                "RequestOutput: Ignoring extra arguments: %s", str(kwargs)
            )
        self.request_id = request_id
        self.prompt = prompt
        self.prompt_token_ids = prompt_token_ids
        self.prompt_logprobs = prompt_logprobs
        self.outputs = outputs
        self.finished = finished
        self.metrics = metrics
        self.lora_request = lora_request
        self.encoder_prompt = encoder_prompt
        self.encoder_prompt_token_ids = encoder_prompt_token_ids
        self.num_cached_tokens = num_cached_tokens
        self.kv_transfer_params = kv_transfer_params
        self.prompt_routed_experts = prompt_routed_experts

    defadd(self, next_output: "RequestOutput", aggregate: bool) -> None:
"""Merge subsequent RequestOutput into this one"""

        self.finished |= next_output.finished
        self.kv_transfer_params = next_output.kv_transfer_params
        if next_output.prompt_routed_experts is not None:
            self.prompt_routed_experts = next_output.prompt_routed_experts

        for next_completion in next_output.outputs:
            for i, completion in enumerate(self.outputs):
                if completion.index == next_completion.index:
                    if aggregate:
                        # Merge outputs with same index
                        completion.text += next_completion.text
                        if not isinstance(completion.token_ids, MutableSequence):
                            completion.token_ids = list(completion.token_ids)
                        completion.token_ids.extend(next_completion.token_ids)
                        if next_completion.logprobs:
                            assert completion.logprobs is not None
                            completion.logprobs.extend(next_completion.logprobs)  # type: ignore[arg-type]
                        completion.cumulative_logprob = (
                            next_completion.cumulative_logprob
                        )
                        completion.finish_reason = next_completion.finish_reason
                        completion.stop_reason = next_completion.stop_reason
                    else:
                        # Replace the output with the new one
                        self.outputs[i] = next_completion
                    break
            else:
                self.outputs.append(next_completion)

    def__repr__(self) -> str:
        return (
            f"RequestOutput(request_id={self.request_id}, "
            f"prompt={self.prompt!r}, "
            f"prompt_token_ids={self.prompt_token_ids}, "
            f"encoder_prompt={self.encoder_prompt!r}, "
            f"encoder_prompt_token_ids={self.encoder_prompt_token_ids}, "
            f"prompt_logprobs={self.prompt_logprobs}, "
            f"outputs={self.outputs}, "
            f"finished={self.finished}, "
            f"metrics={self.metrics}, "
            f"lora_request={self.lora_request}, "
            f"num_cached_tokens={self.num_cached_tokens})"
        )
```

### add [¶](#vllm.RequestOutput.add "Permanent link")

Merge subsequent RequestOutput into this one

Source code in `vllm/outputs.py`

```
defadd(self, next_output: "RequestOutput", aggregate: bool) -> None:
"""Merge subsequent RequestOutput into this one"""

    self.finished |= next_output.finished
    self.kv_transfer_params = next_output.kv_transfer_params
    if next_output.prompt_routed_experts is not None:
        self.prompt_routed_experts = next_output.prompt_routed_experts

    for next_completion in next_output.outputs:
        for i, completion in enumerate(self.outputs):
            if completion.index == next_completion.index:
                if aggregate:
                    # Merge outputs with same index
                    completion.text += next_completion.text
                    if not isinstance(completion.token_ids, MutableSequence):
                        completion.token_ids = list(completion.token_ids)
                    completion.token_ids.extend(next_completion.token_ids)
                    if next_completion.logprobs:
                        assert completion.logprobs is not None
                        completion.logprobs.extend(next_completion.logprobs)  # type: ignore[arg-type]
                    completion.cumulative_logprob = (
                        next_completion.cumulative_logprob
                    )
                    completion.finish_reason = next_completion.finish_reason
                    completion.stop_reason = next_completion.stop_reason
                else:
                    # Replace the output with the new one
                    self.outputs[i] = next_completion
                break
        else:
            self.outputs.append(next_completion)
```

## SamplingParams [¶](#vllm.SamplingParams "Permanent link")

Bases: `PydanticMsgspecMixin`, `Struct`

Sampling parameters for text generation.

Overall, we follow the sampling parameters from the OpenAI text completion API (https://platform.openai.com/docs/api-reference/completions/create). In addition, we support beam search, which is not supported by OpenAI.

Source code in `vllm/sampling_params.py`

```
classSamplingParams(
    PydanticMsgspecMixin,
    msgspec.Struct,
    omit_defaults=True,  # type: ignore[call-arg]
    # required for @cached_property.
    dict=True,
):  # type: ignore[call-arg]
"""Sampling parameters for text generation.

    Overall, we follow the sampling parameters from the OpenAI text completion
    API (https://platform.openai.com/docs/api-reference/completions/create).
    In addition, we support beam search, which is not supported by OpenAI.
    """

    n: int = 1
"""Number of outputs to return for the given prompt request.

    The maximum allowed value is controlled by the ``VLLM_MAX_N_SEQUENCES``
    environment variable (default: 16384).

    NOTE:
        `AsyncLLM` streams outputs by default. When `n > 1`, all `n` outputs
        are generated and streamed cumulatively per request. To see all `n`
        outputs upon completion, use `output_kind=RequestOutputKind.FINAL_ONLY`
        in `SamplingParams`."""
    presence_penalty: float = 0.0
"""Penalizes new tokens based on whether they appear in the generated text
    so far. Values > 0 encourage the model to use new tokens, while values < 0
    encourage the model to repeat tokens."""
    frequency_penalty: float = 0.0
"""Penalizes new tokens based on their frequency in the generated text so
    far. Values > 0 encourage the model to use new tokens, while values < 0
    encourage the model to repeat tokens."""
    repetition_penalty: float = 1.0
"""Penalizes new tokens based on whether they appear in the prompt and the
    generated text so far. Values > 1 encourage the model to use new tokens,
    while values < 1 encourage the model to repeat tokens."""
    temperature: float = 1.0
"""Controls the randomness of the sampling. Lower values make the model
    more deterministic, while higher values make the model more random. Zero
    means greedy sampling."""
    top_p: float = 1.0
"""Controls the cumulative probability of the top tokens to consider. Must
    be in (0, 1]. Set to 1 to consider all tokens."""
    top_k: int = 0
"""Controls the number of top tokens to consider. Set to 0 (or -1) to
    consider all tokens."""
    min_p: float = 0.0
"""Represents the minimum probability for a token to be considered,
    relative to the probability of the most likely token. Must be in [0, 1].
    Set to 0 to disable this."""
    seed: int | None = None
"""Random seed to use for the generation."""
    stop: str | list[str] | None = None
"""String(s) that stop the generation when they are generated. The returned
    output will not contain the stop strings."""
    stop_token_ids: list[int] | None = None
"""Token IDs that stop the generation when they are generated. The returned
    output will contain the stop tokens unless the stop tokens are special
    tokens."""
    ignore_eos: bool = False
"""Whether to ignore the EOS token and continue generating
    tokens after the EOS token is generated."""
    max_tokens: int | None = 16
"""Maximum number of tokens to generate per output sequence."""
    min_tokens: int = 0
"""Minimum number of tokens to generate per output sequence before EOS or
    `stop_token_ids` can be generated"""
    logprobs: int | None = None
"""Number of log probabilities to return per output token. When set to
    `None`, no probability is returned. If set to a non-`None` value, the
    result includes the log probabilities of the specified number of most
    likely tokens, as well as the chosen tokens. Note that the implementation
    follows the OpenAI API: The API will always return the log probability of
    the sampled token, so there may be up to `logprobs+1` elements in the
    response. When set to -1, return all `vocab_size` log probabilities."""
    prompt_logprobs: int | None = None
"""Number of log probabilities to return per prompt token.
    When set to -1, return all `vocab_size` log probabilities."""
    logprob_token_ids: list[int] | None = None
"""Specific token IDs to return logprobs for. More efficient than
    logprobs=-1 when you only need logprobs for a small set of tokens.
    When set, logprobs for exactly these token IDs will be returned,
    in addition to the sampled token. This is useful for scoring tasks
    where you want to compare probabilities of specific label tokens."""
    flat_logprobs: bool = False
"""Whether to return logprobs in flatten format (i.e. FlatLogprob)
    for better performance.
    NOTE: GC costs of FlatLogprobs is significantly smaller than
    list[dict[int, Logprob]]. After enabled, PromptLogprobs and
    SampleLogprobs would populated as FlatLogprobs."""
    # NOTE: This parameter is only exposed at the engine level for now.
    # It is not exposed in the OpenAI API server, as the OpenAI API does
    # not support returning only a list of token IDs.
    detokenize: bool = True
"""Whether to detokenize the output."""
    skip_special_tokens: bool = True
"""Whether to skip special tokens in the output."""
    spaces_between_special_tokens: bool = True
"""Whether to add spaces between special tokens in the output."""
    include_stop_str_in_output: bool = False
"""Whether to include the stop strings in output text."""
    output_kind: RequestOutputKind = RequestOutputKind.CUMULATIVE
    skip_clone: bool = False
"""Internal flag indicating that this SamplingParams instance is safe to
    reuse without cloning. When True, clone() will return self without
    performing a deep copy. This should only be set when the params object
    is guaranteed to be dedicated to a single request and won't be modified
    in ways that would affect other uses."""

    # The below fields are not supposed to be used as an input.
    # They are set in post_init.
    output_text_buffer_length: int = 0
    _eos_token_id: int | None = None
    _all_stop_token_ids: set[int] = msgspec.field(default_factory=set)

    # Fields used to construct logits processors
    structured_outputs: StructuredOutputsParams | None = None
"""Parameters for configuring structured outputs."""
    logit_bias: dict[int, float] | None = None
"""If provided, the engine will construct a logits processor that applies
    these logit biases."""
    allowed_token_ids: list[int] | None = None
"""If provided, the engine will construct a logits processor which only
    retains scores for the given token ids."""
    extra_args: dict[str, Any] | None = None
"""Arbitrary additional args, that can be used by custom sampling
    implementations, plugins, etc. Not used by any in-tree sampling
    implementations."""

    # Fields used for bad words
    bad_words: list[str] | None = None
"""Words that are not allowed to be generated. More precisely, only the
    last token of a corresponding token sequence is not allowed when the next
    generated token can complete the sequence."""
    _bad_words_token_ids: list[list[int]] | None = None

    skip_reading_prefix_cache: bool | None = None
    thinking_token_budget: int | None = None
"""Maximum number of tokens allowed for thinking operations."""

    repetition_detection: RepetitionDetectionParams | None = None
"""Parameters for detecting repetitive N-gram patterns in output tokens.
    If such repetition is detected, generation will be ended early. LLMs can
    sometimes generate repetitive, unhelpful token patterns, stopping only
    when they hit the maximum output length (e.g. 'abcdabcdabcd...' or
    '\\emoji \\emoji \\emoji ...'). This feature can detect such behavior
    and terminate early, saving time and tokens."""

    @staticmethod
    deffrom_optional(
        n: int | None = 1,
        presence_penalty: float | None = 0.0,
        frequency_penalty: float | None = 0.0,
        repetition_penalty: float | None = 1.0,
        temperature: float | None = 1.0,
        top_p: float | None = 1.0,
        top_k: int = 0,
        min_p: float = 0.0,
        seed: int | None = None,
        stop: str | list[str] | None = None,
        stop_token_ids: list[int] | None = None,
        bad_words: list[str] | None = None,
        thinking_token_budget: int | None = None,
        include_stop_str_in_output: bool = False,
        ignore_eos: bool = False,
        max_tokens: int | None = 16,
        min_tokens: int = 0,
        logprobs: int | None = None,
        prompt_logprobs: int | None = None,
        detokenize: bool = True,
        skip_special_tokens: bool = True,
        spaces_between_special_tokens: bool = True,
        output_kind: RequestOutputKind = RequestOutputKind.CUMULATIVE,
        structured_outputs: StructuredOutputsParams | None = None,
        logit_bias: dict[int, float] | dict[str, float] | None = None,
        allowed_token_ids: list[int] | None = None,
        extra_args: dict[str, Any] | None = None,
        skip_clone: bool = False,
        repetition_detection: RepetitionDetectionParams | None = None,
    ) -> "SamplingParams":
        if logit_bias is not None:
            # Convert token_id to integer
            # Clamp the bias between -100 and 100 per OpenAI API spec
            logit_bias = {
                int(token): min(100.0, max(-100.0, bias))
                for token, bias in logit_bias.items()
            }

        return SamplingParams(
            n=1 if n is None else n,
            presence_penalty=0.0 if presence_penalty is None else presence_penalty,
            frequency_penalty=0.0 if frequency_penalty is None else frequency_penalty,
            repetition_penalty=1.0
            if repetition_penalty is None
            else repetition_penalty,
            temperature=1.0 if temperature is None else temperature,
            top_p=1.0 if top_p is None else top_p,
            top_k=top_k,
            min_p=min_p,
            seed=seed,
            stop=stop,
            stop_token_ids=stop_token_ids,
            bad_words=bad_words,
            thinking_token_budget=thinking_token_budget,
            include_stop_str_in_output=include_stop_str_in_output,
            ignore_eos=ignore_eos,
            max_tokens=max_tokens,
            min_tokens=min_tokens,
            logprobs=logprobs,
            prompt_logprobs=prompt_logprobs,
            detokenize=detokenize,
            skip_special_tokens=skip_special_tokens,
            spaces_between_special_tokens=spaces_between_special_tokens,
            output_kind=output_kind,
            structured_outputs=structured_outputs,
            logit_bias=logit_bias,
            allowed_token_ids=allowed_token_ids,
            extra_args=extra_args,
            skip_clone=skip_clone,
            repetition_detection=repetition_detection,
        )

    def__post_init__(self) -> None:
        if 0 < self.temperature < _MAX_TEMP:
            logger.warning(
                "temperature %s is less than %s, which may cause numerical "
                "errors nan or inf in tensors. We have maxed it out to %s.",
                self.temperature,
                _MAX_TEMP,
                _MAX_TEMP,
            )
            self.temperature = max(self.temperature, _MAX_TEMP)

        if self.seed == -1:
            self.seed = None

        if self.stop is None:
            self.stop = []
        elif isinstance(self.stop, str):
            self.stop = [self.stop]

        if self.stop_token_ids is None:
            self.stop_token_ids = []

        if self.bad_words is None:
            self.bad_words = []

        if self.logprobs is True:
            self.logprobs = 1

        if self.prompt_logprobs is True:
            self.prompt_logprobs = 1

        # Number of characters to hold back for stop string evaluation
        # until sequence is finished.
        if self.stop and not self.include_stop_str_in_output:
            self.output_text_buffer_length = max(len(s) for s in self.stop) - 1

        self._verify_args()

        if self.temperature < _SAMPLING_EPS:
            # Zero temperature means greedy sampling.
            self.top_p = 1.0
            self.top_k = 0
            self.min_p = 0.0
            self._verify_greedy_sampling()

        # eos_token_id is added to this by the engine
        self._all_stop_token_ids.update(self.stop_token_ids)

        if self.skip_reading_prefix_cache is None:
            # If prefix caching is enabled,
            # the output of prompt logprobs may less than n_prompt_tokens,
            # we need to skip reading cache at this request.
            self.skip_reading_prefix_cache = self.prompt_logprobs is not None

    def_verify_args(self) -> None:
        if not isinstance(self.n, int):
            raise ValueError(f"n must be an int, but is of type {type(self.n)}")
        if self.n < 1:
            raise ValueError(f"n must be at least 1, got {self.n}.")
        max_n = envs.VLLM_MAX_N_SEQUENCES
        if self.n > max_n:
            raise ValueError(
                f"n must be at most {max_n}, got {self.n}. "
                "To increase this limit, set the VLLM_MAX_N_SEQUENCES "
                "environment variable."
            )
        if not -2.0 <= self.presence_penalty <= 2.0:
            raise ValueError(
                f"presence_penalty must be in [-2, 2], got {self.presence_penalty}."
            )
        if not -2.0 <= self.frequency_penalty <= 2.0:
            raise ValueError(
                f"frequency_penalty must be in [-2, 2], got {self.frequency_penalty}."
            )
        if self.repetition_penalty <= 0.0:
            raise ValueError(
                "repetition_penalty must be greater than zero, got "
                f"{self.repetition_penalty}."
            )
        if self.temperature < 0.0:
            raise VLLMValidationError(
                f"temperature must be non-negative, got {self.temperature}.",
                parameter="temperature",
                value=self.temperature,
            )
        if not 0.0 < self.top_p <= 1.0:
            raise VLLMValidationError(
                f"top_p must be in (0, 1], got {self.top_p}.",
                parameter="top_p",
                value=self.top_p,
            )
        # quietly accept -1 as disabled, but prefer 0
        if self.top_k < -1:
            raise ValueError(
                f"top_k must be 0 (disable), or at least 1, got {self.top_k}."
            )
        if not isinstance(self.top_k, int):
            raise TypeError(
                f"top_k must be an integer, got {type(self.top_k).__name__}"
            )
        if not 0.0 <= self.min_p <= 1.0:
            raise ValueError(f"min_p must be in [0, 1], got {self.min_p}.")
        if self.max_tokens is not None and self.max_tokens < 1:
            raise VLLMValidationError(
                f"max_tokens must be at least 1, got {self.max_tokens}.",
                parameter="max_tokens",
                value=self.max_tokens,
            )
        if self.min_tokens < 0:
            raise ValueError(
                f"min_tokens must be greater than or equal to 0, got {self.min_tokens}."
            )
        if self.max_tokens is not None and self.min_tokens > self.max_tokens:
            raise ValueError(
                f"min_tokens must be less than or equal to "
                f"max_tokens={self.max_tokens}, got {self.min_tokens}."
            )
        if self.logprobs is not None and self.logprobs != -1 and self.logprobs < 0:
            raise VLLMValidationError(
                f"logprobs must be non-negative or -1, got {self.logprobs}.",
                parameter="logprobs",
                value=self.logprobs,
            )
        if (
            self.prompt_logprobs is not None
            and self.prompt_logprobs != -1
            and self.prompt_logprobs < 0
        ):
            raise VLLMValidationError(
                f"prompt_logprobs must be non-negative or -1, got "
                f"{self.prompt_logprobs}.",
                parameter="prompt_logprobs",
                value=self.prompt_logprobs,
            )
        assert isinstance(self.stop_token_ids, list)
        if not all(isinstance(st_id, int) for st_id in self.stop_token_ids):
            raise ValueError(
                f"stop_token_ids must contain only integers, got {self.stop_token_ids}."
            )
        assert isinstance(self.stop, list)
        if any(not stop_str for stop_str in self.stop):
            raise ValueError("stop cannot contain an empty string.")
        if self.stop and not self.detokenize:
            raise ValueError(
                "stop strings are only supported when detokenize is True. "
                "Set detokenize=True to use stop."
            )

    def_verify_greedy_sampling(self) -> None:
        if self.n > 1:
            raise ValueError(f"n must be 1 when using greedy sampling, got {self.n}.")

    defupdate_from_generation_config(
        self,
        generation_config: dict[str, Any],
        eos_token_id: int | None = None,
    ) -> None:
"""Update if there are non-default values from generation_config"""
        if not self.ignore_eos:
            self._eos_token_id = eos_token_id

        if eos_token_id is not None:
            # Add the eos token id into the sampling_params to support
            # min_tokens processing.
            self._all_stop_token_ids.add(eos_token_id)

        # Update eos_token_id for generation
        if (eos_ids := generation_config.get("eos_token_id")) is not None:
            # it can be either int or list of int
            eos_ids = {eos_ids} if isinstance(eos_ids, int) else set(eos_ids)
            if eos_token_id is not None:
                # We don't need to include the primary eos_token_id in
                # stop_token_ids since it's handled separately for stopping
                # purposes.
                eos_ids.discard(eos_token_id)
            if eos_ids:
                self._all_stop_token_ids.update(eos_ids)
                if not self.ignore_eos:
                    assert self.stop_token_ids is not None
                    eos_ids.update(self.stop_token_ids)
                    self.stop_token_ids = list(eos_ids)

    defupdate_from_tokenizer(self, tokenizer: TokenizerLike) -> None:
        if not self.bad_words:
            return
        self._bad_words_token_ids = []
        for bad_word in self.bad_words:
            # To prohibit words both at the beginning
            # and in the middle of text
            # (related to add_prefix_space tokenizer parameter)
            for add_prefix_space in [False, True]:
                prefix = " " if add_prefix_space else ""
                prompt = prefix + bad_word.lstrip()
                prompt_token_ids = tokenizer.encode(
                    text=prompt, add_special_tokens=False
                )

                # If no space at the beginning
                # or if prefix space produces a new word token
                if (not add_prefix_space) or (
                    add_prefix_space
                    and prompt_token_ids[0] != self._bad_words_token_ids[-1][0]
                    and len(prompt_token_ids) == len(self._bad_words_token_ids[-1])
                ):
                    self._bad_words_token_ids.append(prompt_token_ids)

        invalid_token_ids = [
            token_id
            for bad_words_token_ids in self._bad_words_token_ids
            for token_id in bad_words_token_ids
            if token_id < 0 or token_id > tokenizer.max_token_id
        ]
        if len(invalid_token_ids) > 0:
            raise VLLMValidationError(
                f"The model vocabulary size is {tokenizer.max_token_id+1},"
                f" but the following tokens"
                f" were specified as bad: {invalid_token_ids}."
                f" All token id values should be integers satisfying:"
                f" 0 <= token_id <= {tokenizer.max_token_id}.",
                parameter="bad_words",
                value=self.bad_words,
            )

    @cached_property
    defsampling_type(self) -> SamplingType:
        if self.temperature < _SAMPLING_EPS:
            return SamplingType.GREEDY
        if self.seed is not None:
            return SamplingType.RANDOM_SEED
        return SamplingType.RANDOM

    @property
    defeos_token_id(self) -> int | None:
        return self._eos_token_id

    @property
    defall_stop_token_ids(self) -> set[int]:
        return self._all_stop_token_ids

    @property
    defbad_words_token_ids(self) -> list[list[int]] | None:
        # For internal use only. Backward compatibility not guaranteed
        return self._bad_words_token_ids

    @property
    defnum_logprobs(self) -> int | None:
"""Number of sample logprobs to return per output token, or `None` if
        no sample logprobs were requested. Takes `logprob_token_ids` into
        account: when `logprobs` is unset but `logprob_token_ids` is set,
        returns `len(logprob_token_ids)`."""
        if self.logprobs is not None:
            return self.logprobs
        return len(self.logprob_token_ids) if self.logprob_token_ids else None

    defclone(self) -> "SamplingParams":
"""If skip_clone is True, uses shallow copy instead of deep copy."""
        if self.skip_clone:
            return copy.copy(self)

        return copy.deepcopy(self)

    defverify(
        self,
        model_config: ModelConfig,
        speculative_config: SpeculativeConfig | None,
        structured_outputs_config: StructuredOutputsConfig | None,
        tokenizer: TokenizerLike | None,
    ) -> None:
        self._validate_logprobs(model_config)
        self._validate_logit_bias(model_config)
        self._validate_logits_processors(model_config)
        self._validate_allowed_token_ids(tokenizer)
        self._validate_spec_decode(speculative_config)
        self._validate_structured_outputs(structured_outputs_config, tokenizer)

    def_validate_logprobs(self, model_config: ModelConfig) -> None:
        max_logprobs = model_config.max_logprobs
        if max_logprobs == -1:
            max_logprobs = model_config.get_vocab_size()

        # Validate sample logprobs.
        if num_logprobs := self.logprobs:
            if num_logprobs == -1:
                num_logprobs = model_config.get_vocab_size()
            if num_logprobs > max_logprobs:
                raise VLLMValidationError(
                    f"Requested sample logprobs of {num_logprobs}, "
                    f"which is greater than max allowed: {max_logprobs}",
                    parameter="logprobs",
                    value=num_logprobs,
                )

        # Validate logprob_token_ids.
        if self.logprob_token_ids is not None:
            n = len(self.logprob_token_ids)
            if n > MAX_LOGPROB_TOKEN_IDS:
                raise VLLMValidationError(
                    f"Requested logprob_token_ids of length {n}, "
                    f"which is greater than max allowed: {MAX_LOGPROB_TOKEN_IDS}",
                    parameter="logprob_token_ids",
                    value=n,
                )

        # Validate prompt logprobs.
        if num_prompt_logprobs := self.prompt_logprobs:
            if num_prompt_logprobs == -1:
                num_prompt_logprobs = model_config.get_vocab_size()
            if num_prompt_logprobs > max_logprobs:
                raise VLLMValidationError(
                    f"Requested prompt logprobs of {num_prompt_logprobs}, "
                    f"which is greater than max allowed: {max_logprobs}",
                    parameter="prompt_logprobs",
                    value=num_prompt_logprobs,
                )

    def_validate_logit_bias(self, model_config: ModelConfig) -> None:
"""Validate logit_bias token IDs are within vocabulary range."""
        if not self.logit_bias:
            return

        vocab_size = model_config.get_vocab_size()
        invalid_token_ids = [
            token_id
            for token_id in self.logit_bias
            if token_id < 0 or token_id >= vocab_size
        ]

        if invalid_token_ids:
            raise VLLMValidationError(
                f"token_id(s) {invalid_token_ids} in logit_bias contain "
                f"out-of-vocab token ids. Vocabulary size: {vocab_size}",
                parameter="logit_bias",
                value=invalid_token_ids,
            )

    def_validate_logits_processors(self, model_config: ModelConfig) -> None:
        fromvllm.v1.sample.logits_processorimport (
            validate_logits_processors_parameters,
        )

        validate_logits_processors_parameters(model_config.logits_processors, self)

    def_validate_allowed_token_ids(self, tokenizer: TokenizerLike | None) -> None:
        allowed_token_ids = self.allowed_token_ids
        if allowed_token_ids is None:
            return

        if len(allowed_token_ids) == 0:
            raise VLLMValidationError(
                "allowed_token_ids is not None and empty!",
                parameter="allowed_token_ids",
                value=allowed_token_ids,
            )

        if tokenizer is not None:
            vocab_size = len(tokenizer)
            invalid_token_ids = [
                token_id
                for token_id in allowed_token_ids
                if token_id < 0 or token_id >= vocab_size
            ]
            if invalid_token_ids:
                raise VLLMValidationError(
                    "allowed_token_ids contains out-of-vocab token id!",
                    parameter="allowed_token_ids",
                    value=invalid_token_ids,
                )

    def_validate_spec_decode(
        self,
        speculative_config: SpeculativeConfig | None,
    ) -> None:
        if speculative_config is None:
            return

        # Some sampling parameters are not yet compatible with spec decoding.
        if self.min_p > _SAMPLING_EPS or self.logit_bias:
            raise ValueError(
                "The min_p and logit_bias sampling parameters "
                "are not yet supported with speculative decoding."
            )

    def_validate_structured_outputs(
        self,
        structured_outputs_config: StructuredOutputsConfig | None,
        tokenizer: TokenizerLike | None,
    ) -> None:
        if structured_outputs_config is None or self.structured_outputs is None:
            return

        if tokenizer is None:
            raise ValueError(
                "Structured outputs requires a tokenizer so it can't be used with 'skip_tokenizer_init'"  # noqa: E501
            )

        backend = structured_outputs_config.backend
        if _backend := self.structured_outputs._backend:
            # Request-level backend selection is not supported.
            # The values may differ if `params` is reused and was set
            # to a specific backend based on `auto` behavior in a previous
            # request. We remember that it was set as a result of `auto`
            # using the `_backend_was_auto` field set in the params.
            if backend != _backend and not (
                backend == "auto" and self.structured_outputs._backend_was_auto
            ):
                raise ValueError(
                    "Request-level structured output backend selection is not "
                    f"supported. The request specified '{_backend}', but vLLM "
                    f"was initialised with '{backend}'. This error can be "
                    "resolved by removing '_backend' from the request."
                )
        else:
            self.structured_outputs._backend = backend

        # Request content validation
        if (
            isinstance(self.structured_outputs.choice, list)
            and not self.structured_outputs.choice
        ):
            # It is invalid for choice to be an empty list
            raise ValueError(
                f"Choice '{self.structured_outputs.choice}' cannot be an empty list"  # noqa: E501
            )
        # Reject empty string grammar early to avoid engine-side crashes
        if (
            isinstance(self.structured_outputs.grammar, str)
            and self.structured_outputs.grammar.strip() == ""
        ):
            raise ValueError("structured_outputs.grammar cannot be an empty string")

        fromvllm.v1.structured_output.backend_guidanceimport (
            has_guidance_unsupported_json_features,
            validate_guidance_grammar,
        )
        fromvllm.v1.structured_output.backend_lm_format_enforcerimport (
            validate_structured_output_request_lm_format_enforcer,
        )
        fromvllm.v1.structured_output.backend_outlinesimport (
            validate_structured_output_request_outlines,
        )
        fromvllm.v1.structured_output.backend_xgrammarimport validate_xgrammar_grammar

        if backend.startswith("xgrammar"):
            # xgrammar with no fallback
            validate_xgrammar_grammar(self)
        elif backend.startswith("guidance"):
            if _is_non_tekken_mistral(tokenizer=tokenizer):
                raise ValueError(
                    "Non-tekken Mistral tokenizers are not supported for the 'guidance'"
                    " structured output backend. Please either use a more recent "
                    "Mistral model, the ['xgrammar', 'outlines'] "
                    "backends or tokenizer_mode='hf' instead."
                )
            # TODO: ideally we would have the LLTokenizer here as Lark syntax
            # allows <|special_token|> and similar, see
            # https://github.com/guidance-ai/llguidance/blob/main/docs/syntax.md#special-tokens
            # Without tokenizer these are disallowed in grammars.
            validate_guidance_grammar(
                self,
                tokenizer=_get_llg_tokenizer(tokenizer),
            )
        elif backend == "outlines":
            # outlines backend
            validate_structured_output_request_outlines(self)
        elif backend == "lm-format-enforcer":
            # lm format enforcer backend
            if is_mistral_tokenizer(tokenizer):
                raise ValueError(
                    "Mistral tokenizer is not supported for the 'lm-format-enforcer' "
                    "structured output backend. Please use ['xgrammar', 'outlines'] "
                    "backends or tokenizer_mode='hf' instead."
                )
            validate_structured_output_request_lm_format_enforcer(self)
        else:
            # NOTE: backend must be "auto" here, because we have
            # checked supported_backends above.
            # In this mode, we set opinionated defaults based on what we think
            # will satisfy the most use cases without having to worry about
            # this setting. We include fallback behavior here, but not with any
            # other setting where a specific backend was specified.
            try:
                validate_xgrammar_grammar(self)
                self.structured_outputs._backend = "xgrammar"
            except ValueError:
                # The request either failed validation
                # or includes some jsonschema feature(s) that
                # are not supported in xgrammar.

                skip_guidance = _is_non_tekken_mistral(tokenizer)

                # Check if schema has features unsupported by guidance
                so_params = self.structured_outputs
                if not skip_guidance and so_params.json:
                    if isinstance(so_params.json, str):
                        schema = json_mod.loads(so_params.json)
                    else:
                        schema = so_params.json
                    skip_guidance = has_guidance_unsupported_json_features(schema)

                if skip_guidance:
                    # Fall back to outlines if the tokenizer is non-tekken Mistral or
                    # the schema contains features unsupported by guidance
                    validate_structured_output_request_outlines(self)
                    self.structured_outputs._backend = "outlines"
                else:
                    # Fall back to guidance by default.
                    validate_guidance_grammar(
                        self,
                        tokenizer=_get_llg_tokenizer(tokenizer),
                    )
                    self.structured_outputs._backend = "guidance"
            # Remember that this backend was set automatically
            self.structured_outputs._backend_was_auto = True

        # Run post-init validation. This is also important to ensure subsequent
        # roundtrip serialization/deserialization won't fail.
        self.structured_outputs.__post_init__()

    def__repr__(self) -> str:
        return (
            f"SamplingParams(n={self.n}, "
            f"presence_penalty={self.presence_penalty}, "
            f"frequency_penalty={self.frequency_penalty}, "
            f"repetition_penalty={self.repetition_penalty}, "
            f"temperature={self.temperature}, "
            f"top_p={self.top_p}, "
            f"top_k={self.top_k}, "
            f"min_p={self.min_p}, "
            f"seed={self.seed}, "
            f"stop={self.stop}, "
            f"stop_token_ids={self.stop_token_ids}, "
            f"bad_words={self.bad_words}, "
            f"thinking_token_budget={self.thinking_token_budget}, "
            f"include_stop_str_in_output={self.include_stop_str_in_output}, "
            f"ignore_eos={self.ignore_eos}, "
            f"max_tokens={self.max_tokens}, "
            f"min_tokens={self.min_tokens}, "
            f"logprobs={self.logprobs}, "
            f"prompt_logprobs={self.prompt_logprobs}, "
            f"skip_special_tokens={self.skip_special_tokens}, "
            "spaces_between_special_tokens="
            f"{self.spaces_between_special_tokens}, "
            f"structured_outputs={self.structured_outputs}, "
            f"extra_args={self.extra_args})"
        )

    @staticmethod
    deffor_sampler_warmup() -> "SamplingParams":
"""Set parameters to exercise all sampler logic."""
        return SamplingParams(
            temperature=0.9,
            top_p=0.9,
            top_k=50,
            min_p=0.1,
            frequency_penalty=0.5,
            presence_penalty=0.5,
            repetition_penalty=1.2,
            min_tokens=2,
            logit_bias={0: -1.0, 1: 0.5},
            _bad_words_token_ids=[[0], [1, 2]],
            logprobs=5,
            prompt_logprobs=1,
        )
```

### allowed\_token\_ids `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.allowed_token_ids "Permanent link")

```
allowed_token_ids: list[int] | None = None
```

If provided, the engine will construct a logits processor which only retains scores for the given token ids.

### bad\_words `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.bad_words "Permanent link")

Words that are not allowed to be generated. More precisely, only the last token of a corresponding token sequence is not allowed when the next generated token can complete the sequence.

### detokenize `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.detokenize "Permanent link")

Whether to detokenize the output.

Arbitrary additional args, that can be used by custom sampling implementations, plugins, etc. Not used by any in-tree sampling implementations.

### flat\_logprobs `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.flat_logprobs "Permanent link")

```
flat_logprobs: bool = False
```

Whether to return logprobs in flatten format (i.e. FlatLogprob) for better performance. NOTE: GC costs of FlatLogprobs is significantly smaller than list\[dict\[int, Logprob]]. After enabled, PromptLogprobs and SampleLogprobs would populated as FlatLogprobs.

### frequency\_penalty `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.frequency_penalty "Permanent link")

```
frequency_penalty: float = 0.0
```

Penalizes new tokens based on their frequency in the generated text so far. Values &gt; 0 encourage the model to use new tokens, while values &lt; 0 encourage the model to repeat tokens.

### ignore\_eos `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.ignore_eos "Permanent link")

Whether to ignore the EOS token and continue generating tokens after the EOS token is generated.

### include\_stop\_str\_in\_output `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.include_stop_str_in_output "Permanent link")

```
include_stop_str_in_output: bool = False
```

Whether to include the stop strings in output text.

### logit\_bias `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.logit_bias "Permanent link")

If provided, the engine will construct a logits processor that applies these logit biases.

### logprob\_token\_ids `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.logprob_token_ids "Permanent link")

```
logprob_token_ids: list[int] | None = None
```

Specific token IDs to return logprobs for. More efficient than logprobs=-1 when you only need logprobs for a small set of tokens. When set, logprobs for exactly these token IDs will be returned, in addition to the sampled token. This is useful for scoring tasks where you want to compare probabilities of specific label tokens.

### logprobs `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.logprobs "Permanent link")

```
logprobs: int | None = None
```

Number of log probabilities to return per output token. When set to `None`, no probability is returned. If set to a non-`None` value, the result includes the log probabilities of the specified number of most likely tokens, as well as the chosen tokens. Note that the implementation follows the OpenAI API: The API will always return the log probability of the sampled token, so there may be up to `logprobs+1` elements in the response. When set to -1, return all `vocab_size` log probabilities.

### max\_tokens `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.max_tokens "Permanent link")

```
max_tokens: int | None = 16
```

Maximum number of tokens to generate per output sequence.

### min\_p `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.min_p "Permanent link")

Represents the minimum probability for a token to be considered, relative to the probability of the most likely token. Must be in \[0, 1]. Set to 0 to disable this.

### min\_tokens `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.min_tokens "Permanent link")

Minimum number of tokens to generate per output sequence before EOS or `stop_token_ids` can be generated

### n `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.n "Permanent link")

Number of outputs to return for the given prompt request.

The maximum allowed value is controlled by the `VLLM_MAX_N_SEQUENCES` environment variable (default: 16384).

NOTE

`AsyncLLM` streams outputs by default. When `n > 1`, all `n` outputs are generated and streamed cumulatively per request. To see all `n` outputs upon completion, use `output_kind=RequestOutputKind.FINAL_ONLY` in `SamplingParams`.

### num\_logprobs `property` [¶](#vllm.SamplingParams.num_logprobs "Permanent link")

Number of sample logprobs to return per output token, or `None` if no sample logprobs were requested. Takes `logprob_token_ids` into account: when `logprobs` is unset but `logprob_token_ids` is set, returns `len(logprob_token_ids)`.

### presence\_penalty `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.presence_penalty "Permanent link")

```
presence_penalty: float = 0.0
```

Penalizes new tokens based on whether they appear in the generated text so far. Values &gt; 0 encourage the model to use new tokens, while values &lt; 0 encourage the model to repeat tokens.

### prompt\_logprobs `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.prompt_logprobs "Permanent link")

```
prompt_logprobs: int | None = None
```

Number of log probabilities to return per prompt token. When set to -1, return all `vocab_size` log probabilities.

### repetition\_detection `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.repetition_detection "Permanent link")

Parameters for detecting repetitive N-gram patterns in output tokens. If such repetition is detected, generation will be ended early. LLMs can sometimes generate repetitive, unhelpful token patterns, stopping only when they hit the maximum output length (e.g. 'abcdabcdabcd...' or '\\emoji \\emoji \\emoji ...'). This feature can detect such behavior and terminate early, saving time and tokens.

### repetition\_penalty `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.repetition_penalty "Permanent link")

```
repetition_penalty: float = 1.0
```

Penalizes new tokens based on whether they appear in the prompt and the generated text so far. Values &gt; 1 encourage the model to use new tokens, while values &lt; 1 encourage the model to repeat tokens.

### seed `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.seed "Permanent link")

Random seed to use for the generation.

### skip\_clone `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.skip_clone "Permanent link")

Internal flag indicating that this SamplingParams instance is safe to reuse without cloning. When True, clone() will return self without performing a deep copy. This should only be set when the params object is guaranteed to be dedicated to a single request and won't be modified in ways that would affect other uses.

### skip\_special\_tokens `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.skip_special_tokens "Permanent link")

```
skip_special_tokens: bool = True
```

Whether to skip special tokens in the output.

### spaces\_between\_special\_tokens `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.spaces_between_special_tokens "Permanent link")

```
spaces_between_special_tokens: bool = True
```

Whether to add spaces between special tokens in the output.

### stop `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.stop "Permanent link")

String(s) that stop the generation when they are generated. The returned output will not contain the stop strings.

### stop\_token\_ids `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.stop_token_ids "Permanent link")

```
stop_token_ids: list[int] | None = None
```

Token IDs that stop the generation when they are generated. The returned output will contain the stop tokens unless the stop tokens are special tokens.

### structured\_outputs `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.structured_outputs "Permanent link")

Parameters for configuring structured outputs.

### temperature `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.temperature "Permanent link")

Controls the randomness of the sampling. Lower values make the model more deterministic, while higher values make the model more random. Zero means greedy sampling.

### thinking\_token\_budget `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.thinking_token_budget "Permanent link")

```
thinking_token_budget: int | None = None
```

Maximum number of tokens allowed for thinking operations.

### top\_k `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.top_k "Permanent link")

Controls the number of top tokens to consider. Set to 0 (or -1) to consider all tokens.

### top\_p `class-attribute` `instance-attribute` [¶](#vllm.SamplingParams.top_p "Permanent link")

Controls the cumulative probability of the top tokens to consider. Must be in (0, 1]. Set to 1 to consider all tokens.

### \_validate\_logit\_bias [¶](#vllm.SamplingParams._validate_logit_bias "Permanent link")

```
_validate_logit_bias(model_config: ModelConfig) -> None
```

Validate logit\_bias token IDs are within vocabulary range.

Source code in `vllm/sampling_params.py`

```
def_validate_logit_bias(self, model_config: ModelConfig) -> None:
"""Validate logit_bias token IDs are within vocabulary range."""
    if not self.logit_bias:
        return

    vocab_size = model_config.get_vocab_size()
    invalid_token_ids = [
        token_id
        for token_id in self.logit_bias
        if token_id < 0 or token_id >= vocab_size
    ]

    if invalid_token_ids:
        raise VLLMValidationError(
            f"token_id(s) {invalid_token_ids} in logit_bias contain "
            f"out-of-vocab token ids. Vocabulary size: {vocab_size}",
            parameter="logit_bias",
            value=invalid_token_ids,
        )
```

### clone [¶](#vllm.SamplingParams.clone "Permanent link")

If skip\_clone is True, uses shallow copy instead of deep copy.

Source code in `vllm/sampling_params.py`

```
defclone(self) -> "SamplingParams":
"""If skip_clone is True, uses shallow copy instead of deep copy."""
    if self.skip_clone:
        return copy.copy(self)

    return copy.deepcopy(self)
```

### for\_sampler\_warmup `staticmethod` [¶](#vllm.SamplingParams.for_sampler_warmup "Permanent link")

Set parameters to exercise all sampler logic.

Source code in `vllm/sampling_params.py`

```
@staticmethod
deffor_sampler_warmup() -> "SamplingParams":
"""Set parameters to exercise all sampler logic."""
    return SamplingParams(
        temperature=0.9,
        top_p=0.9,
        top_k=50,
        min_p=0.1,
        frequency_penalty=0.5,
        presence_penalty=0.5,
        repetition_penalty=1.2,
        min_tokens=2,
        logit_bias={0: -1.0, 1: 0.5},
        _bad_words_token_ids=[[0], [1, 2]],
        logprobs=5,
        prompt_logprobs=1,
    )
```

### update\_from\_generation\_config [¶](#vllm.SamplingParams.update_from_generation_config "Permanent link")

```
update_from_generation_config(
    generation_config: dict[str, Any],
    eos_token_id: int | None = None,
) -> None
```

Update if there are non-default values from generation\_config

Source code in `vllm/sampling_params.py`

```
defupdate_from_generation_config(
    self,
    generation_config: dict[str, Any],
    eos_token_id: int | None = None,
) -> None:
"""Update if there are non-default values from generation_config"""
    if not self.ignore_eos:
        self._eos_token_id = eos_token_id

    if eos_token_id is not None:
        # Add the eos token id into the sampling_params to support
        # min_tokens processing.
        self._all_stop_token_ids.add(eos_token_id)

    # Update eos_token_id for generation
    if (eos_ids := generation_config.get("eos_token_id")) is not None:
        # it can be either int or list of int
        eos_ids = {eos_ids} if isinstance(eos_ids, int) else set(eos_ids)
        if eos_token_id is not None:
            # We don't need to include the primary eos_token_id in
            # stop_token_ids since it's handled separately for stopping
            # purposes.
            eos_ids.discard(eos_token_id)
        if eos_ids:
            self._all_stop_token_ids.update(eos_ids)
            if not self.ignore_eos:
                assert self.stop_token_ids is not None
                eos_ids.update(self.stop_token_ids)
                self.stop_token_ids = list(eos_ids)
```

## ScoringOutput `dataclass` [¶](#vllm.ScoringOutput "Permanent link")

The output data of one scoring output of a request.

Parameters:

Name Type Description Default `score` `float`

The similarity score, which is a scalar value.

*required*

Source code in `vllm/outputs.py`

```
@dataclass
classScoringOutput:
"""The output data of one scoring output of a request.

    Args:
        score: The similarity score, which is a scalar value.
    """

    score: float

    @staticmethod
    deffrom_base(pooling_output: PoolingOutput):
        # pooling_output shape:
        #   classify task: (num_classes) num_classes == 1
        #   embed task: a scalar value
        pooled_data = pooling_output.data.squeeze()
        if pooled_data.ndim != 0:
            raise ValueError("pooled_data should be a scalar score")

        return ScoringOutput(pooled_data.item())

    def__repr__(self) -> str:
        return f"ScoringOutput(score={self.score})"
```

## TextPrompt [¶](#vllm.TextPrompt "Permanent link")

Bases: `_PromptOptions`

Schema for a text prompt.

Source code in `vllm/inputs/llm.py`

```
classTextPrompt(_PromptOptions):
"""Schema for a text prompt."""

    prompt: str
"""The input text to be tokenized before passing to the model."""
```

### prompt `instance-attribute` [¶](#vllm.TextPrompt.prompt "Permanent link")

The input text to be tokenized before passing to the model.

## TokensPrompt [¶](#vllm.TokensPrompt "Permanent link")

Bases: `_PromptOptions`

Schema for a tokenized prompt.

Source code in `vllm/inputs/llm.py`

```
classTokensPrompt(_PromptOptions):
"""Schema for a tokenized prompt."""

    prompt_token_ids: list[int]
"""A list of token IDs to pass to the model."""

    prompt: NotRequired[str]
"""The prompt text corresponding to the token IDs, if available."""

    token_type_ids: NotRequired[list[int]]
"""A list of token type IDs to pass to the cross encoder model."""
```

### prompt `instance-attribute` [¶](#vllm.TokensPrompt.prompt "Permanent link")

The prompt text corresponding to the token IDs, if available.

### prompt\_token\_ids `instance-attribute` [¶](#vllm.TokensPrompt.prompt_token_ids "Permanent link")

A list of token IDs to pass to the model.

### token\_type\_ids `instance-attribute` [¶](#vllm.TokensPrompt.token_type_ids "Permanent link")

A list of token type IDs to pass to the cross encoder model.

## initialize\_ray\_cluster [¶](#vllm.initialize_ray_cluster "Permanent link")

```
initialize_ray_cluster(
    parallel_config: ParallelConfig,
    ray_address: str | None = None,
    require_gpu_on_driver: bool = True,
)
```

Initialize the distributed cluster with Ray.

it will connect to the Ray cluster and create a placement group for the workers, which includes the specification of the resources for each distributed worker.

Parameters:

Name Type Description Default `parallel_config` `ParallelConfig`

The configurations for parallel execution.

*required* `ray_address` `str | None`

The address of the Ray cluster. If None, uses the default Ray cluster address.

`None` `require_gpu_on_driver` `bool`

If True (default), require at least one GPU on the current (driver) node and pin the first PG bundle to it. Set to False for executors like RayExecutorV2 where all GPU work is delegated to remote Ray actors.

`True`

Source code in `vllm/v1/executor/ray_utils.py`

```
definitialize_ray_cluster(
    parallel_config: ParallelConfig,
    ray_address: str | None = None,
    require_gpu_on_driver: bool = True,
):
"""Initialize the distributed cluster with Ray.

    it will connect to the Ray cluster and create a placement group
    for the workers, which includes the specification of the resources
    for each distributed worker.

    Args:
        parallel_config: The configurations for parallel execution.
        ray_address: The address of the Ray cluster. If None, uses
            the default Ray cluster address.
        require_gpu_on_driver: If True (default), require at least one GPU
            on the current (driver) node and pin the first PG bundle to it.
            Set to False for executors like RayExecutorV2 where all GPU work
            is delegated to remote Ray actors.
    """
    assert_ray_available()
    fromvllm.platformsimport current_platform

    # Disable Ray usage stats collection
    if os.environ.get("RAY_USAGE_STATS_ENABLED", "0") != "1":
        os.environ["RAY_USAGE_STATS_ENABLED"] = "0"

    # Prevalidate GPU requirements before Ray processing
    if current_platform.is_cuda() and parallel_config.world_size > 1:
        available_gpus = current_platform.device_count()
        if parallel_config.world_size > available_gpus:
            logger.warning(
                "Tensor parallel size (%d) exceeds available GPUs (%d). "
                "This may result in Ray placement group allocation failures. "
                "Consider reducing tensor_parallel_size to %d or less, "
                "or ensure your Ray cluster has %d GPUs available.",
                parallel_config.world_size,
                available_gpus,
                available_gpus,
                parallel_config.world_size,
            )

    if ray.is_initialized():
        logger.info("Ray is already initialized. Skipping Ray initialization.")
    elif current_platform.is_rocm() or current_platform.is_xpu():
        # Try to connect existing ray instance and create a new one if not found
        try:
            ray.init("auto")
        except ConnectionError:
            logger.warning(
                "No existing RAY instance detected. "
                "A new instance will be launched with current node resources."
            )
            ray.init(
                address=ray_address,
                num_gpus=parallel_config.world_size,
                runtime_env=parallel_config.ray_runtime_env,
            )
    else:
        ray.init(address=ray_address, runtime_env=parallel_config.ray_runtime_env)

    device_str = current_platform.ray_device_key
    if not device_str:
        raise ValueError(
            f"current platform {current_platform.device_name} does not support ray."
        )

    # Create or get the placement group for worker processes
    if parallel_config.placement_group:
        current_placement_group = parallel_config.placement_group
    else:
        current_placement_group = ray.util.get_current_placement_group()

    if current_placement_group:
        logger.info("Using the existing placement group")

        # We are in a placement group
        bundles = current_placement_group.bundle_specs
        # Verify that we can use the placement group.
        device_bundles = 0
        for bundle in bundles:
            bundle_devices = bundle.get(device_str, 0)
            if bundle_devices > 1:
                raise ValueError(
                    f"Placement group bundle cannot have more than 1 {device_str}."
                )
            if bundle_devices:
                device_bundles += 1
        if parallel_config.world_size > device_bundles:
            raise ValueError(
                f"The number of required {device_str}s exceeds the total "
                f"number of available {device_str}s in the placement group. "
                f"Required number of devices: {parallel_config.world_size}. "
                f"Total number of devices: {device_bundles}."
            )
    else:
        logger.info("No current placement group found. Creating a new placement group.")
        num_devices_in_cluster = ray.cluster_resources().get(device_str, 0)
        # Log a warning message and delay resource allocation failure response.
        # Avoid immediate rejection to allow user-initiated placement group
        # created and wait cluster to be ready
        if parallel_config.world_size > num_devices_in_cluster:
            logger.warning(
                "The number of required %ss exceeds the total "
                "number of available %ss in the placement group.",
                device_str,
                device_str,
            )
        # Create a new placement group
        placement_group_specs: list[dict[str, float]] = [
            {device_str: 1.0} for _ in range(parallel_config.world_size)
        ]

        # vLLM engine is also a worker to execute model with an accelerator,
        # so it requires to have the device in a current node. Check if
        # the current node has at least one device.
        current_ip = get_ip()
        current_node_id = ray.get_runtime_context().get_node_id()
        current_node_resource = available_resources_per_node()[current_node_id]
        # TODO (jeffreywang): require_gpu_on_driver should be always False
        # after deprecating RayDistributedExecutor.
        if require_gpu_on_driver:
            if current_node_resource.get(device_str, 0) < 1:
                raise ValueError(
                    f"Current node has no {device_str} available. "
                    f"{current_node_resource=}. vLLM engine cannot start "
                    f"without {device_str}. Make sure you have at least 1 "
                    f"{device_str} available in a node "
                    f"{current_node_id=}{current_ip=}."
                )
            # This way, at least bundle is required to be created in a
            # current node.
            placement_group_specs[0][f"node:{current_ip}"] = 0.001

        # By default, Ray packs resources as much as possible.
        current_placement_group = ray.util.placement_group(
            placement_group_specs, strategy="PACK"
        )
        _wait_until_pg_ready(current_placement_group)

    assert current_placement_group is not None
    _verify_bundles(
        current_placement_group, parallel_config, device_str, require_gpu_on_driver
    )
    # Set the placement group in the parallel config
    parallel_config.placement_group = current_placement_group
```