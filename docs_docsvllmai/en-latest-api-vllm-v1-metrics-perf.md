---
title: perf - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/metrics/perf/
source: sitemap
fetched_at: 2026-05-07T21:41:11.597521135-03:00
rendered_js: false
word_count: 842
summary: This module provides classes for calculating computational flops and memory traffic metrics for attention components in a transformer model to facilitate MFU analysis.
tags:
    - performance-metrics
    - attention-layers
    - model-flops-utilization
    - vllm
    - memory-estimation
    - transformer-architecture
category: reference
---

Analytic flops/memory estimation module for transformer components, to help derive MFU (Model Flops Utilization) stats for a running model.

## AttentionMetrics [¶](#vllm.v1.metrics.perf.AttentionMetrics "Permanent link")

Bases: `ComponentMetrics`

Source code in `vllm/v1/metrics/perf.py`

```
classAttentionMetrics(ComponentMetrics):
    # From BaseConfigParser
    num_hidden_layers: int = Field(..., gt=0)
    hidden_size: int = Field(..., gt=0)
    num_attention_heads: int = Field(..., gt=0)
    activation_byte_size: int = Field(..., gt=0)
    tp_size: int = Field(..., gt=0)
    pp_size: int = Field(..., gt=0)

    # From BaseAttentionConfigParser
    num_key_value_heads: int = Field(..., gt=0)
    head_dim: int = Field(..., gt=0)
    cache_byte_size: int = Field(..., gt=0)

    # From BaseConfig Parser, overridden by AttentionQuantizationConfigParser
    weight_byte_size: int | float = Field(..., gt=0)

    # TODO: discern cases where we have mixture of different attention layer types
    # such as SWA, MLA, etc.

    @classmethod
    defcomponent_type(cls) -> str:
        return "attn"

    @classmethod
    defget_parser(cls) -> ParserChain:
        return ParserChain(
            BaseConfigParser(),
            BaseAttentionConfigParser(),
            AttentionQuantizationConfigParser(),
        )

    defget_num_flops_breakdown(
        self, ctx: ExecutionContext, per_gpu: bool = True
    ) -> dict[str, int]:
        L, D, q, kv, d = (
            self.num_hidden_layers,
            self.hidden_size,
            self.num_attention_heads,
            self.num_key_value_heads,
            self.head_dim,
        )
        T = ctx.total_num_tokens()
        TC = ctx.total_token_context_product()

        if per_gpu:
            L //= self.pp_size
            # tensor parallel along heads
            q = max(1, q // self.tp_size)
            kv = max(1, kv // self.tp_size)

        return {
            "qkv_proj": 2 * T * D * (q + 2 * kv) * d * L,
            "attn_qk": 2 * q * TC * d * L,
            "attn_av": 2 * q * TC * d * L,
            "out_proj": 2 * T * D * q * d * L,
        }

    defget_read_bytes_breakdown(
        self, ctx: ExecutionContext, per_gpu: bool = True
    ) -> dict[str, int]:
        L, D, q, kv, d = (
            self.num_hidden_layers,
            self.hidden_size,
            self.num_attention_heads,
            self.num_key_value_heads,
            self.head_dim,
        )
        T = ctx.total_num_tokens()

        if per_gpu:
            L //= self.pp_size
            # tensor parallel along heads
            q = max(1, q // self.tp_size)
            kv = max(1, kv // self.tp_size)

        read_bytes = {}

        read_bytes["qkv_input"] = T * D * self.activation_byte_size * L
        read_bytes["qkv_weight"] = int(D * (q + 2 * kv) * d * self.weight_byte_size * L)

        # Attention input reads differ between prefill and decode
        # Prefill: read Q, K, V activations (all in activation_byte_size)
        if ctx.prefill_num_tokens > 0:
            read_bytes["attn_input"] = (
                (ctx.prefill_num_tokens * q + 2 * ctx.prefill_context_len * kv)
                * d
                * self.activation_byte_size
                * L
            )

        # Decode: read Q activations + read K, V from cache (in cache_byte_size)
        if ctx.decode_num_tokens > 0:
            read_bytes["attn_input"] = read_bytes.get("attn_input", 0) + (
                ctx.decode_num_tokens * q * d * self.activation_byte_size * L
                + 2 * ctx.decode_context_len * kv * d * self.cache_byte_size * L
            )

        read_bytes["out_input"] = T * q * d * self.activation_byte_size * L
        read_bytes["out_weight"] = int(q * d * D * self.weight_byte_size * L)

        return read_bytes

    defget_write_bytes_breakdown(
        self, ctx: ExecutionContext, per_gpu: bool = True
    ) -> dict[str, int]:
"""Calculate write memory traffic for attention layers."""
        L, D, q, kv, d = (
            self.num_hidden_layers,
            self.hidden_size,
            self.num_attention_heads,
            self.num_key_value_heads,
            self.head_dim,
        )
        T = ctx.total_num_tokens()

        if per_gpu:
            L //= self.pp_size
            # tensor parallel along heads
            q = max(1, q // self.tp_size)
            kv = max(1, kv // self.tp_size)

        return {
            "qkv_output": T * (q + 2 * kv) * d * self.activation_byte_size * L,
            "kv_cache": 2 * T * kv * d * self.cache_byte_size * L,
            "out_output": T * D * self.activation_byte_size * L,
        }
```

### get\_write\_bytes\_breakdown [¶](#vllm.v1.metrics.perf.AttentionMetrics.get_write_bytes_breakdown "Permanent link")

Calculate write memory traffic for attention layers.

Source code in `vllm/v1/metrics/perf.py`

```
defget_write_bytes_breakdown(
    self, ctx: ExecutionContext, per_gpu: bool = True
) -> dict[str, int]:
"""Calculate write memory traffic for attention layers."""
    L, D, q, kv, d = (
        self.num_hidden_layers,
        self.hidden_size,
        self.num_attention_heads,
        self.num_key_value_heads,
        self.head_dim,
    )
    T = ctx.total_num_tokens()

    if per_gpu:
        L //= self.pp_size
        # tensor parallel along heads
        q = max(1, q // self.tp_size)
        kv = max(1, kv // self.tp_size)

    return {
        "qkv_output": T * (q + 2 * kv) * d * self.activation_byte_size * L,
        "kv_cache": 2 * T * kv * d * self.cache_byte_size * L,
        "out_output": T * D * self.activation_byte_size * L,
    }
```

## AttentionQuantizationConfigParser [¶](#vllm.v1.metrics.perf.AttentionQuantizationConfigParser "Permanent link")

Bases: `Parser`

Parses quantization configuration for attention layers. Overrides: weight\_byte\_size

Source code in `vllm/v1/metrics/perf.py`

```
classAttentionQuantizationConfigParser(Parser):
"""
    Parses quantization configuration for attention layers.
    Overrides: weight_byte_size
    """

    defparse(self, args: ParsedArgs, vllm_config: VllmConfig) -> ParsedArgs:
        cfg = vllm_config.quant_config

        if cfg is None:
            return args

        quant_method = cfg.get_name()
        if quant_method in _QUANT_WEIGHT_BYTE_SIZE:
            args.weight_byte_size = _QUANT_WEIGHT_BYTE_SIZE[quant_method]
        else:
            raise InvalidComponent(
                f"Unsupported quantization method for attention metrics: {quant_method}"
            )

        return args
```

## BaseAttentionConfigParser [¶](#vllm.v1.metrics.perf.BaseAttentionConfigParser "Permanent link")

Bases: `Parser`

Parses attention-specific configuration. Provides: num\_key\_value\_heads, head\_dim, cache\_byte\_size

Source code in `vllm/v1/metrics/perf.py`

```
classBaseAttentionConfigParser(Parser):
"""
    Parses attention-specific configuration.
    Provides: num_key_value_heads, head_dim, cache_byte_size
    """

    defparse(self, args: ParsedArgs, vllm_config: VllmConfig) -> ParsedArgs:
        model_config = vllm_config.model_config

        args.num_key_value_heads = model_config.get_total_num_kv_heads()
        args.head_dim = model_config.get_head_size()

        model_dtype = vllm_config.model_config.dtype
        cache_dtype = vllm_config.cache_config.cache_dtype

        kv_cache_torch_dtype = get_kv_cache_torch_dtype(cache_dtype, model_dtype)
        args.cache_byte_size = get_dtype_size(kv_cache_torch_dtype)

        return args
```

## BaseConfigParser [¶](#vllm.v1.metrics.perf.BaseConfigParser "Permanent link")

Bases: `Parser`

Parses base model configuration. Provides: vocab\_size, hidden\_size, num\_attention\_heads, num\_hidden\_layers, weight\_byte\_size, activation\_byte\_size, dp\_size, tp\_size, pp\_size, enable\_ep

Source code in `vllm/v1/metrics/perf.py`

```
classBaseConfigParser(Parser):
"""
    Parses base model configuration.
    Provides: vocab_size, hidden_size, num_attention_heads, num_hidden_layers,
    weight_byte_size, activation_byte_size, dp_size, tp_size, pp_size, enable_ep
    """

    defparse(self, args: ParsedArgs, vllm_config: VllmConfig) -> ParsedArgs:
        model_config = vllm_config.model_config

        args.vocab_size = model_config.get_vocab_size()
        args.hidden_size = model_config.get_hidden_size()
        # NOTE: model_config.get_attention_heads() divide by TP
        # so we access field manually here to get total num_heads
        args.num_attention_heads = get_required(
            model_config.hf_text_config, "num_attention_heads"
        )
        args.num_hidden_layers = get_required(
            model_config.hf_text_config, "num_hidden_layers"
        )

        model_dtype = vllm_config.model_config.dtype

        if isinstance(model_dtype, torch.dtype):
            torch_dtype = model_dtype
        elif isinstance(model_dtype, str) and model_dtype in STR_DTYPE_TO_TORCH_DTYPE:
            torch_dtype = STR_DTYPE_TO_TORCH_DTYPE[model_dtype]
        else:
            # FIXME: handle this better
            logger.warning(
                "Unknown model_dtype %s, defaulting to bfloat16",
                model_dtype,
            )
            torch_dtype = torch.bfloat16

        args.weight_byte_size = get_dtype_size(torch_dtype)

        # FIXME: handle this better by parsing whether activations use
        # bf16, fp32, etc...
        args.activation_byte_size = 2

        args.dp_size = vllm_config.parallel_config.data_parallel_size
        args.tp_size = vllm_config.parallel_config.tensor_parallel_size
        args.pp_size = vllm_config.parallel_config.pipeline_parallel_size
        args.enable_ep = vllm_config.parallel_config.enable_expert_parallel

        return args
```

## BaseFfnConfigParser [¶](#vllm.v1.metrics.perf.BaseFfnConfigParser "Permanent link")

Bases: `Parser`

Parses FFN and MoE configuration. Provides: intermediate\_size, num\_experts, num\_experts\_per\_tok, moe\_intermediate\_size, num\_shared\_experts, num\_moe\_layers

Source code in `vllm/v1/metrics/perf.py`

```
classBaseFfnConfigParser(Parser):
"""
    Parses FFN and MoE configuration.
    Provides: intermediate_size, num_experts, num_experts_per_tok,
    moe_intermediate_size, num_shared_experts, num_moe_layers
    """

    defparse(self, args: ParsedArgs, vllm_config: VllmConfig) -> ParsedArgs:
        cfg = vllm_config.model_config.hf_config
        if hasattr(cfg, "text_config") and cfg.text_config is not None:
            cfg = cfg.text_config

        args.intermediate_size = getattr(cfg, "intermediate_size", args.hidden_size * 4)

        # Try different naming conventions.
        args.num_experts = vllm_config.model_config.get_num_experts()
        args.num_experts_per_tok = getattr_from_list(
            cfg, ["num_experts_per_tok", "moe_topk"], 0
        )
        args.moe_intermediate_size = getattr_from_list(
            cfg, ["moe_intermediate_size", "intermediate_size"], 0
        )
        args.num_shared_experts = getattr_from_list(
            cfg, ["n_shared_experts", "num_shared_experts"], 0
        )

        is_moe = args.num_experts != 0
        # Assume all MoE layers by default
        args.num_moe_layers = args.num_hidden_layers if is_moe else 0

        return args
```

## ComponentMetrics [¶](#vllm.v1.metrics.perf.ComponentMetrics "Permanent link")

Bases: `BaseModel`, `ABC`

Each concrete ComponentMetrics class is associated with: - fields that are required for metric derivation (fields are specified/validated through pydantic model) - parser to parse VllmConfig into fields - metric methods that derive flops/bytes for a given execution context

Source code in `vllm/v1/metrics/perf.py`

```
classComponentMetrics(BaseModel, ABC):
"""
    Each concrete ComponentMetrics class is associated with:
    - fields that are required for metric derivation
      (fields are specified/validated through pydantic model)
    - parser to parse VllmConfig into fields
    - metric methods that derive flops/bytes for a given execution context
    """

    @classmethod
    @abstractmethod
    defcomponent_type(cls) -> str: ...

    @classmethod
    @abstractmethod
    defget_parser(cls) -> ParserChain:
"""
        Return a ParserChain that provides values for all required fields.
        The returned parser chain must populate ParsedArgs with values for every
        field defined on this ComponentMetrics class. Missing fields will cause
        a ValidationError when from_vllm_config() is called.
        See individual Parser docstrings for which args they provide, and field
        comments on ComponentMetrics subclasses for which parser provides each field.
        """
        ...

    def__init_subclass__(cls):
        _COMPONENT_METRICS_REGISTRY[cls.component_type()] = cls

    @classmethod
    deffrom_vllm_config(cls, vllm_config: VllmConfig) -> Self:
"""
        Instantiate this class from VllmConfig.
        Raises ValidationError if parsing fails.
        """

        parser = cls.get_parser()
        parsed_args = parser.parse(vllm_config)
        try:
            return cls.model_validate(parsed_args.model_dump())
        except ValidationError as e:
            raise InvalidComponent(f"Invalid {cls.component_type()} config: {e}") frome

    @classmethod
    defregistered_metrics(cls) -> Iterable[type["ComponentMetrics"]]:
        return iter(_COMPONENT_METRICS_REGISTRY.values())

    @abstractmethod
    defget_num_flops_breakdown(
        self, ctx: ExecutionContext, per_gpu: bool = True
    ) -> dict[str, int]: ...

    @abstractmethod
    defget_read_bytes_breakdown(
        self, ctx: ExecutionContext, per_gpu: bool = True
    ) -> dict[str, int]: ...

    @abstractmethod
    defget_write_bytes_breakdown(
        self, ctx: ExecutionContext, per_gpu: bool = True
    ) -> dict[str, int]: ...

    defget_num_flops(self, ctx: ExecutionContext, per_gpu: bool = True) -> int:
        return sum(self.get_num_flops_breakdown(ctx, per_gpu).values())

    defget_read_bytes(self, ctx: ExecutionContext, per_gpu: bool = True) -> int:
        return sum(self.get_read_bytes_breakdown(ctx, per_gpu).values())

    defget_write_bytes(self, ctx: ExecutionContext, per_gpu: bool = True) -> int:
        return sum(self.get_write_bytes_breakdown(ctx, per_gpu).values())
```

### from\_vllm\_config `classmethod` [¶](#vllm.v1.metrics.perf.ComponentMetrics.from_vllm_config "Permanent link")

Instantiate this class from VllmConfig. Raises ValidationError if parsing fails.

Source code in `vllm/v1/metrics/perf.py`

```
@classmethod
deffrom_vllm_config(cls, vllm_config: VllmConfig) -> Self:
"""
    Instantiate this class from VllmConfig.
    Raises ValidationError if parsing fails.
    """

    parser = cls.get_parser()
    parsed_args = parser.parse(vllm_config)
    try:
        return cls.model_validate(parsed_args.model_dump())
    except ValidationError as e:
        raise InvalidComponent(f"Invalid {cls.component_type()} config: {e}") frome
```

### get\_parser `abstractmethod` `classmethod` [¶](#vllm.v1.metrics.perf.ComponentMetrics.get_parser "Permanent link")

```
get_parser() -> ParserChain
```

Return a ParserChain that provides values for all required fields. The returned parser chain must populate ParsedArgs with values for every field defined on this ComponentMetrics class. Missing fields will cause a ValidationError when from\_vllm\_config() is called. See individual Parser docstrings for which args they provide, and field comments on ComponentMetrics subclasses for which parser provides each field.

Source code in `vllm/v1/metrics/perf.py`

```
@classmethod
@abstractmethod
defget_parser(cls) -> ParserChain:
"""
    Return a ParserChain that provides values for all required fields.
    The returned parser chain must populate ParsedArgs with values for every
    field defined on this ComponentMetrics class. Missing fields will cause
    a ValidationError when from_vllm_config() is called.
    See individual Parser docstrings for which args they provide, and field
    comments on ComponentMetrics subclasses for which parser provides each field.
    """
    ...
```

## ExecutionContext `dataclass` [¶](#vllm.v1.metrics.perf.ExecutionContext "Permanent link")

Represents an execution context for a batch of requests.

This class aggregates statistics across multiple requests in a batch, separately tracking prefill and decode phases.

Example) - Batch with one full prefill (2048 tokens) and one decode (1 token, 8192 context): ctx = ExecutionContext() ctx.add(2048, 2048, is\_prefill=True) ctx.add(1, 8192, is\_prefill=False)

Source code in `vllm/v1/metrics/perf.py`

```
@dataclass
classExecutionContext:
"""
    Represents an execution context for a batch of requests.

    This class aggregates statistics across multiple requests in a batch,
    separately tracking prefill and decode phases.

    Example)
    - Batch with one full prefill (2048 tokens) and one decode (1 token, 8192 context):
      ctx = ExecutionContext()
      ctx.add(2048, 2048, is_prefill=True)
      ctx.add(1, 8192, is_prefill=False)
    """

    # Prefill phase statistics
    num_prefill_requests: int = 0
    prefill_num_tokens: int = 0  # sum of num_tokens for prefill requests
    prefill_context_len: int = 0  # sum of context_len for prefill requests
    prefill_token_context_product: int = 0  # sum of (num_tokens * context_len)

    # Decode phase statistics
    num_decode_requests: int = 0
    decode_num_tokens: int = 0  # sum of num_tokens for decode requests
    decode_context_len: int = 0  # sum of context_len for decode requests
    decode_token_context_product: int = 0  # sum of (num_tokens * context_len)

    defadd(self, num_tokens: int, context_len: int, is_prefill: bool) -> None:
"""Add a single request's statistics to this batch context."""
        if is_prefill:
            self.num_prefill_requests += 1
            self.prefill_num_tokens += num_tokens
            self.prefill_context_len += context_len
            self.prefill_token_context_product += num_tokens * context_len
        else:
            self.num_decode_requests += 1
            self.decode_num_tokens += num_tokens
            self.decode_context_len += context_len
            self.decode_token_context_product += num_tokens * context_len

    deftotal_num_tokens(self) -> int:
"""Total number of tokens across all requests in the batch."""
        return self.prefill_num_tokens + self.decode_num_tokens

    deftotal_token_context_product(self) -> int:
"""Total sum of (num_tokens * context_len) across all requests."""
        return self.prefill_token_context_product + self.decode_token_context_product

    defnum_logits_tokens(self) -> int:
"""Number of tokens that require logits computation (unembedding).

        For prefill, only the last token per request needs logits.
        For decode, all tokens need logits.
        """
        return self.num_prefill_requests + self.decode_num_tokens

    @classmethod
    deffrom_single_request(
        cls, num_tokens: int, context_len: int, is_prefill: bool
    ) -> "ExecutionContext":
"""Create an ExecutionContext from a single request.

        This is a convenience method primarily for testing.
        """
        ctx = cls()
        ctx.add(num_tokens, context_len, is_prefill)
        return ctx
```

### add [¶](#vllm.v1.metrics.perf.ExecutionContext.add "Permanent link")

```
add(
    num_tokens: int, context_len: int, is_prefill: bool
) -> None
```

Add a single request's statistics to this batch context.

Source code in `vllm/v1/metrics/perf.py`

```
defadd(self, num_tokens: int, context_len: int, is_prefill: bool) -> None:
"""Add a single request's statistics to this batch context."""
    if is_prefill:
        self.num_prefill_requests += 1
        self.prefill_num_tokens += num_tokens
        self.prefill_context_len += context_len
        self.prefill_token_context_product += num_tokens * context_len
    else:
        self.num_decode_requests += 1
        self.decode_num_tokens += num_tokens
        self.decode_context_len += context_len
        self.decode_token_context_product += num_tokens * context_len
```

### from\_single\_request `classmethod` [¶](#vllm.v1.metrics.perf.ExecutionContext.from_single_request "Permanent link")

```
from_single_request(
    num_tokens: int, context_len: int, is_prefill: bool
) -> ExecutionContext
```

Create an ExecutionContext from a single request.

This is a convenience method primarily for testing.

Source code in `vllm/v1/metrics/perf.py`

```
@classmethod
deffrom_single_request(
    cls, num_tokens: int, context_len: int, is_prefill: bool
) -> "ExecutionContext":
"""Create an ExecutionContext from a single request.

    This is a convenience method primarily for testing.
    """
    ctx = cls()
    ctx.add(num_tokens, context_len, is_prefill)
    return ctx
```

### num\_logits\_tokens [¶](#vllm.v1.metrics.perf.ExecutionContext.num_logits_tokens "Permanent link")

```
num_logits_tokens() -> int
```

Number of tokens that require logits computation (unembedding).

For prefill, only the last token per request needs logits. For decode, all tokens need logits.

Source code in `vllm/v1/metrics/perf.py`

```
defnum_logits_tokens(self) -> int:
"""Number of tokens that require logits computation (unembedding).

    For prefill, only the last token per request needs logits.
    For decode, all tokens need logits.
    """
    return self.num_prefill_requests + self.decode_num_tokens
```

### total\_num\_tokens [¶](#vllm.v1.metrics.perf.ExecutionContext.total_num_tokens "Permanent link")

```
total_num_tokens() -> int
```

Total number of tokens across all requests in the batch.

Source code in `vllm/v1/metrics/perf.py`

```
deftotal_num_tokens(self) -> int:
"""Total number of tokens across all requests in the batch."""
    return self.prefill_num_tokens + self.decode_num_tokens
```

### total\_token\_context\_product [¶](#vllm.v1.metrics.perf.ExecutionContext.total_token_context_product "Permanent link")

```
total_token_context_product() -> int
```

Total sum of (num\_tokens * context\_len) across all requests.

Source code in `vllm/v1/metrics/perf.py`

```
deftotal_token_context_product(self) -> int:
"""Total sum of (num_tokens * context_len) across all requests."""
    return self.prefill_token_context_product + self.decode_token_context_product
```

## FfnMetrics [¶](#vllm.v1.metrics.perf.FfnMetrics "Permanent link")

Bases: `ComponentMetrics`

Source code in `vllm/v1/metrics/perf.py`

```
classFfnMetrics(ComponentMetrics):
    # From BaseConfigParser
    num_hidden_layers: int = Field(..., gt=0)
    hidden_size: int = Field(..., gt=0)
    activation_byte_size: int = Field(..., gt=0)
    pp_size: int = Field(..., gt=0)

    # From FfnParallelParser
    ffn_tp_size: int = Field(..., gt=0)
    ffn_ep_size: int = Field(..., gt=0)

    # From BaseFfnConfigParser
    intermediate_size: int = Field(..., gt=0)
    num_experts: int = Field(0)
    num_experts_per_tok: int = Field(1)
    moe_intermediate_size: int = Field(0)
    num_shared_experts: int = Field(0)

    # From BaseConfigParser, can be overridden InterleaveMoeLayerStep or MoeLayerFreq
    num_moe_layers: int = Field(..., ge=0)

    # FIXME: might have to make this more granular
    # (i.e. dense_weight_byte_size, moe_routed_weight_byte_size,
    # moe_shared_weight_byte_size)
    # since it can differ from byte size of other components (e.g. attn)
    # and can differ even from each other.

    # From BaseConfigParser, can be overridden by FfnQuantizationConfigParser
    weight_byte_size: int | float = Field(..., gt=0)

    @model_validator(mode="after")
    defvalidate_moe_fields(self) -> Self:
"""Validate that MoE-related fields are properly set when num_moe_layers > 0."""
        if self.num_moe_layers > 0:
            assert self.num_experts, f"{self.num_experts=}"
            assert self.num_experts_per_tok, f"{self.num_experts_per_tok=}"
            assert self.moe_intermediate_size, f"{self.moe_intermediate_size=}"
        return self

    @classmethod
    defcomponent_type(cls) -> str:
        return "ffn"

    @classmethod
    defget_parser(cls) -> ParserChain:
        return ParserChain(
            BaseConfigParser(),
            FfnParallelParser(),
            BaseFfnConfigParser(),
            InterleaveMoeLayerStepParser(),
            MoeLayerFreqParser(),
            FfnQuantizationConfigParser(),
        )

    defget_num_flops_breakdown(
        self, ctx: ExecutionContext, per_gpu: bool = True
    ) -> dict[str, int]:
"""Calculate flops breakdown for FFN layers."""
        L, D, DI = self.num_hidden_layers, self.hidden_size, self.intermediate_size
        Lm, E, MI, S = (
            self.num_moe_layers,
            self.num_experts_per_tok,
            self.moe_intermediate_size,
            self.num_shared_experts,
        )
        T = ctx.total_num_tokens()

        Ld = L - Lm

        num_activated_tokens = T * E if E else 0

        if per_gpu:
            Ld //= self.pp_size
            Lm //= self.pp_size

            DI //= self.ffn_tp_size
            if MI is not None:
                MI //= self.ffn_tp_size
            if E:
                num_activated_tokens //= self.ffn_ep_size

        flops = {}

        # Dense FFN layers (SwiGLU: 3 linear layers: up, gate, down)
        if Ld:
            flops["dense_ffn"] = 2 * D * 3 * DI * T * Ld

        # MoE routed experts (each token activates E experts)
        if Lm and E:
            flops["routed_ffn"] = 2 * D * 3 * MI * num_activated_tokens * Lm

        # MoE shared experts (all S shared experts run for every token)
        if Lm and S:
            flops["shared_ffn"] = 2 * D * 3 * MI * S * T * Lm

        return flops

    defget_read_bytes_breakdown(
        self, ctx: ExecutionContext, per_gpu: bool = True
    ) -> dict[str, int]:
"""Calculate read memory traffic for FFN layers."""
        L, D, DI = self.num_hidden_layers, self.hidden_size, self.intermediate_size
        Lm, E, MI, S = (
            self.num_moe_layers,
            self.num_experts_per_tok,
            self.moe_intermediate_size,
            self.num_shared_experts,
        )
        T = ctx.total_num_tokens()
        num_experts = self.num_experts

        Ld = L - Lm

        num_activated_tokens = T * E if E else 0

        if per_gpu:
            Ld //= self.pp_size
            Lm //= self.pp_size

            DI //= self.ffn_tp_size
            if MI is not None:
                MI //= self.ffn_tp_size
            if E:
                num_activated_tokens //= self.ffn_ep_size
            if num_experts is not None:
                num_experts //= self.ffn_ep_size

        read_bytes = {}

        # Dense FFN layers (3 GEMMs: up, gate, down projections + SiLU activation)
        if Ld:
            read_bytes["dense_up_gate_input"] = int(
                T * D * self.activation_byte_size * Ld
            )
            read_bytes["dense_up_gate_weights"] = int(
                2 * D * DI * self.weight_byte_size * Ld
            )
            read_bytes["dense_silu_input"] = int(
                2 * T * DI * self.activation_byte_size * Ld
            )
            read_bytes["dense_down_input"] = int(
                T * DI * self.activation_byte_size * Ld
            )
            read_bytes["dense_down_weights"] = int(D * DI * self.weight_byte_size * Ld)

        if Lm:
            # MoE routed expert reads
            if E:
                # FIXME: Assume perfect load balancing for now.
                num_activated_experts = min(num_activated_tokens, num_experts)

                read_bytes["routed_up_gate_input"] = int(
                    num_activated_tokens * D * self.activation_byte_size * Lm
                )
                read_bytes["routed_up_gate_weights"] = int(
                    2 * D * MI * num_activated_experts * self.weight_byte_size * Lm
                )
                read_bytes["routed_silu_input"] = int(
                    2 * num_activated_tokens * MI * self.activation_byte_size * Lm
                )
                read_bytes["routed_down_input"] = int(
                    num_activated_tokens * MI * self.activation_byte_size * Lm
                )
                read_bytes["routed_down_weights"] = int(
                    D * MI * num_activated_experts * self.weight_byte_size * Lm
                )

            # MoE shared expert reads
            if S:
                read_bytes["shared_up_gate_input"] = int(
                    T * D * self.activation_byte_size * Lm
                )
                read_bytes["shared_up_gate_weights"] = int(
                    2 * D * MI * S * self.weight_byte_size * Lm
                )
                read_bytes["shared_silu_input"] = int(
                    2 * T * MI * S * self.activation_byte_size * Lm
                )
                read_bytes["shared_down_input"] = int(
                    T * MI * self.activation_byte_size * Lm
                )
                read_bytes["shared_down_weights"] = int(
                    D * MI * S * self.weight_byte_size * Lm
                )

        return read_bytes

    defget_write_bytes_breakdown(
        self, ctx: ExecutionContext, per_gpu: bool = True
    ) -> dict[str, int]:
"""Calculate write memory traffic for FFN layers."""
        L, D, DI = self.num_hidden_layers, self.hidden_size, self.intermediate_size
        Lm, E, MI, S = (
            self.num_moe_layers,
            self.num_experts_per_tok,
            self.moe_intermediate_size,
            self.num_shared_experts,
        )
        T = ctx.total_num_tokens()

        Ld = L - Lm

        num_activated_tokens = T * E if E else 0

        if per_gpu:
            Ld //= self.pp_size
            Lm //= self.pp_size

            DI //= self.ffn_tp_size
            if MI is not None:
                MI //= self.ffn_tp_size
            if E:
                num_activated_tokens //= self.ffn_ep_size

        write_bytes = {}

        # Dense FFN layers
        if Ld:
            write_bytes["dense_up_gate_output"] = int(
                2 * T * DI * self.activation_byte_size * Ld
            )
            write_bytes["dense_silu_output"] = int(
                T * DI * self.activation_byte_size * Ld
            )
            write_bytes["dense_down_output"] = int(
                T * D * self.activation_byte_size * Ld
            )

        # MoE outputs
        if Lm:
            if E:
                write_bytes["routed_up_gate_output"] = int(
                    2 * num_activated_tokens * MI * self.activation_byte_size * Lm
                )
                write_bytes["routed_silu_output"] = int(
                    num_activated_tokens * MI * self.activation_byte_size * Lm
                )
                write_bytes["routed_down_output"] = int(
                    num_activated_tokens * D * self.activation_byte_size * Lm
                )
            if S:
                write_bytes["shared_up_gate_output"] = int(
                    2 * T * S * MI * self.activation_byte_size * Lm
                )
                write_bytes["shared_silu_output"] = int(
                    T * S * MI * self.activation_byte_size * Lm
                )
                write_bytes["shared_down_output"] = int(
                    T * S * D * self.activation_byte_size * Lm
                )

        return write_bytes
```

### get\_num\_flops\_breakdown [¶](#vllm.v1.metrics.perf.FfnMetrics.get_num_flops_breakdown "Permanent link")

Calculate flops breakdown for FFN layers.

Source code in `vllm/v1/metrics/perf.py`

```
defget_num_flops_breakdown(
    self, ctx: ExecutionContext, per_gpu: bool = True
) -> dict[str, int]:
"""Calculate flops breakdown for FFN layers."""
    L, D, DI = self.num_hidden_layers, self.hidden_size, self.intermediate_size
    Lm, E, MI, S = (
        self.num_moe_layers,
        self.num_experts_per_tok,
        self.moe_intermediate_size,
        self.num_shared_experts,
    )
    T = ctx.total_num_tokens()

    Ld = L - Lm

    num_activated_tokens = T * E if E else 0

    if per_gpu:
        Ld //= self.pp_size
        Lm //= self.pp_size

        DI //= self.ffn_tp_size
        if MI is not None:
            MI //= self.ffn_tp_size
        if E:
            num_activated_tokens //= self.ffn_ep_size

    flops = {}

    # Dense FFN layers (SwiGLU: 3 linear layers: up, gate, down)
    if Ld:
        flops["dense_ffn"] = 2 * D * 3 * DI * T * Ld

    # MoE routed experts (each token activates E experts)
    if Lm and E:
        flops["routed_ffn"] = 2 * D * 3 * MI * num_activated_tokens * Lm

    # MoE shared experts (all S shared experts run for every token)
    if Lm and S:
        flops["shared_ffn"] = 2 * D * 3 * MI * S * T * Lm

    return flops
```

### get\_read\_bytes\_breakdown [¶](#vllm.v1.metrics.perf.FfnMetrics.get_read_bytes_breakdown "Permanent link")

Calculate read memory traffic for FFN layers.

Source code in `vllm/v1/metrics/perf.py`

```
defget_read_bytes_breakdown(
    self, ctx: ExecutionContext, per_gpu: bool = True
) -> dict[str, int]:
"""Calculate read memory traffic for FFN layers."""
    L, D, DI = self.num_hidden_layers, self.hidden_size, self.intermediate_size
    Lm, E, MI, S = (
        self.num_moe_layers,
        self.num_experts_per_tok,
        self.moe_intermediate_size,
        self.num_shared_experts,
    )
    T = ctx.total_num_tokens()
    num_experts = self.num_experts

    Ld = L - Lm

    num_activated_tokens = T * E if E else 0

    if per_gpu:
        Ld //= self.pp_size
        Lm //= self.pp_size

        DI //= self.ffn_tp_size
        if MI is not None:
            MI //= self.ffn_tp_size
        if E:
            num_activated_tokens //= self.ffn_ep_size
        if num_experts is not None:
            num_experts //= self.ffn_ep_size

    read_bytes = {}

    # Dense FFN layers (3 GEMMs: up, gate, down projections + SiLU activation)
    if Ld:
        read_bytes["dense_up_gate_input"] = int(
            T * D * self.activation_byte_size * Ld
        )
        read_bytes["dense_up_gate_weights"] = int(
            2 * D * DI * self.weight_byte_size * Ld
        )
        read_bytes["dense_silu_input"] = int(
            2 * T * DI * self.activation_byte_size * Ld
        )
        read_bytes["dense_down_input"] = int(
            T * DI * self.activation_byte_size * Ld
        )
        read_bytes["dense_down_weights"] = int(D * DI * self.weight_byte_size * Ld)

    if Lm:
        # MoE routed expert reads
        if E:
            # FIXME: Assume perfect load balancing for now.
            num_activated_experts = min(num_activated_tokens, num_experts)

            read_bytes["routed_up_gate_input"] = int(
                num_activated_tokens * D * self.activation_byte_size * Lm
            )
            read_bytes["routed_up_gate_weights"] = int(
                2 * D * MI * num_activated_experts * self.weight_byte_size * Lm
            )
            read_bytes["routed_silu_input"] = int(
                2 * num_activated_tokens * MI * self.activation_byte_size * Lm
            )
            read_bytes["routed_down_input"] = int(
                num_activated_tokens * MI * self.activation_byte_size * Lm
            )
            read_bytes["routed_down_weights"] = int(
                D * MI * num_activated_experts * self.weight_byte_size * Lm
            )

        # MoE shared expert reads
        if S:
            read_bytes["shared_up_gate_input"] = int(
                T * D * self.activation_byte_size * Lm
            )
            read_bytes["shared_up_gate_weights"] = int(
                2 * D * MI * S * self.weight_byte_size * Lm
            )
            read_bytes["shared_silu_input"] = int(
                2 * T * MI * S * self.activation_byte_size * Lm
            )
            read_bytes["shared_down_input"] = int(
                T * MI * self.activation_byte_size * Lm
            )
            read_bytes["shared_down_weights"] = int(
                D * MI * S * self.weight_byte_size * Lm
            )

    return read_bytes
```

### get\_write\_bytes\_breakdown [¶](#vllm.v1.metrics.perf.FfnMetrics.get_write_bytes_breakdown "Permanent link")

Calculate write memory traffic for FFN layers.

Source code in `vllm/v1/metrics/perf.py`

```
defget_write_bytes_breakdown(
    self, ctx: ExecutionContext, per_gpu: bool = True
) -> dict[str, int]:
"""Calculate write memory traffic for FFN layers."""
    L, D, DI = self.num_hidden_layers, self.hidden_size, self.intermediate_size
    Lm, E, MI, S = (
        self.num_moe_layers,
        self.num_experts_per_tok,
        self.moe_intermediate_size,
        self.num_shared_experts,
    )
    T = ctx.total_num_tokens()

    Ld = L - Lm

    num_activated_tokens = T * E if E else 0

    if per_gpu:
        Ld //= self.pp_size
        Lm //= self.pp_size

        DI //= self.ffn_tp_size
        if MI is not None:
            MI //= self.ffn_tp_size
        if E:
            num_activated_tokens //= self.ffn_ep_size

    write_bytes = {}

    # Dense FFN layers
    if Ld:
        write_bytes["dense_up_gate_output"] = int(
            2 * T * DI * self.activation_byte_size * Ld
        )
        write_bytes["dense_silu_output"] = int(
            T * DI * self.activation_byte_size * Ld
        )
        write_bytes["dense_down_output"] = int(
            T * D * self.activation_byte_size * Ld
        )

    # MoE outputs
    if Lm:
        if E:
            write_bytes["routed_up_gate_output"] = int(
                2 * num_activated_tokens * MI * self.activation_byte_size * Lm
            )
            write_bytes["routed_silu_output"] = int(
                num_activated_tokens * MI * self.activation_byte_size * Lm
            )
            write_bytes["routed_down_output"] = int(
                num_activated_tokens * D * self.activation_byte_size * Lm
            )
        if S:
            write_bytes["shared_up_gate_output"] = int(
                2 * T * S * MI * self.activation_byte_size * Lm
            )
            write_bytes["shared_silu_output"] = int(
                T * S * MI * self.activation_byte_size * Lm
            )
            write_bytes["shared_down_output"] = int(
                T * S * D * self.activation_byte_size * Lm
            )

    return write_bytes
```

### validate\_moe\_fields [¶](#vllm.v1.metrics.perf.FfnMetrics.validate_moe_fields "Permanent link")

```
validate_moe_fields() -> Self
```

Validate that MoE-related fields are properly set when num\_moe\_layers &gt; 0.

Source code in `vllm/v1/metrics/perf.py`

```
@model_validator(mode="after")
defvalidate_moe_fields(self) -> Self:
"""Validate that MoE-related fields are properly set when num_moe_layers > 0."""
    if self.num_moe_layers > 0:
        assert self.num_experts, f"{self.num_experts=}"
        assert self.num_experts_per_tok, f"{self.num_experts_per_tok=}"
        assert self.moe_intermediate_size, f"{self.moe_intermediate_size=}"
    return self
```

## FfnParallelParser [¶](#vllm.v1.metrics.perf.FfnParallelParser "Permanent link")

Bases: `Parser`

Parses FFN parallelism configuration.

Provides: ffn\_tp\_size, ffn\_ep\_size

Source code in `vllm/v1/metrics/perf.py`

```
classFfnParallelParser(Parser):
"""
    Parses FFN parallelism configuration.

    Provides: ffn_tp_size, ffn_ep_size
    """

    defparse(self, args: ParsedArgs, vllm_config: VllmConfig) -> ParsedArgs:
        # NOTE: ffn tp_size does not equal the tp_size parameter directly.
        # e.g.) If we use DP2TP4, ffn will use TP8 (or EP8 if EP is enabled.)
        if args.enable_ep:
            ffn_tp_size, ffn_ep_size = 1, args.dp_size * args.tp_size
        else:
            ffn_tp_size, ffn_ep_size = args.dp_size * args.tp_size, 1

        args.ffn_tp_size = ffn_tp_size
        args.ffn_ep_size = ffn_ep_size

        return args
```

## FfnQuantizationConfigParser [¶](#vllm.v1.metrics.perf.FfnQuantizationConfigParser "Permanent link")

Bases: `Parser`

Parses quantization configuration for FFN layers.

Overrides: weight\_byte\_size

Source code in `vllm/v1/metrics/perf.py`

```
classFfnQuantizationConfigParser(Parser):
"""
    Parses quantization configuration for FFN layers.

    Overrides: weight_byte_size
    """

    defparse(self, args: ParsedArgs, vllm_config: VllmConfig) -> ParsedArgs:
        cfg = vllm_config.quant_config

        if cfg is None:
            return args

        quant_method = cfg.get_name()
        if quant_method in _QUANT_WEIGHT_BYTE_SIZE:
            args.weight_byte_size = _QUANT_WEIGHT_BYTE_SIZE[quant_method]
        else:
            raise InvalidComponent(
                f"Unsupported quantization method for FFN metrics: {quant_method}"
            )

        return args
```

## InterleaveMoeLayerStepParser [¶](#vllm.v1.metrics.perf.InterleaveMoeLayerStepParser "Permanent link")

Bases: `Parser`

Parses interleave\_moe\_layer\_step field for models like Llama4.

Overrides: num\_moe\_layers

Source code in `vllm/v1/metrics/perf.py`

```
classInterleaveMoeLayerStepParser(Parser):
"""
    Parses interleave_moe_layer_step field for models like Llama4.

    Overrides: num_moe_layers
    """

    defparse(self, args: ParsedArgs, vllm_config: VllmConfig) -> ParsedArgs:
        cfg = vllm_config.model_config.hf_config
        if hasattr(cfg, "text_config") and cfg.text_config is not None:
            cfg = cfg.text_config

        if (
            hasattr(cfg, "interleave_moe_layer_step")
            and cfg.interleave_moe_layer_step > 0
        ):
            args.num_moe_layers = len(
                [
                    layer
                    for layer in range(args.num_hidden_layers)
                    if (layer + 1) % cfg.interleave_moe_layer_step == 0
                ]
            )

        return args
```

## InvalidComponent [¶](#vllm.v1.metrics.perf.InvalidComponent "Permanent link")

Bases: `Exception`

Custom exception to indicate that a certain ComponentMetric is not applicable to the given VllmConfig.

Source code in `vllm/v1/metrics/perf.py`

```
classInvalidComponent(Exception):
"""
    Custom exception to indicate that a certain ComponentMetric is not
    applicable to the given VllmConfig.
    """

    pass
```

## ModelMetrics [¶](#vllm.v1.metrics.perf.ModelMetrics "Permanent link")

Source code in `vllm/v1/metrics/perf.py`

```
classModelMetrics:
    def__init__(self, vllm_config: VllmConfig) -> None:
"""
        Parse vllm_config to instantiate metrics for each component.
        is_enabled() will return False if no component metrics could be instantiated.
        """

        self.vllm_config = vllm_config

        self.metrics: list[ComponentMetrics] = []
        for metric_cls in ComponentMetrics.registered_metrics():
            try:
                metric = metric_cls.from_vllm_config(vllm_config)
                self.metrics.append(metric)
                logger.info(
                    "Instantiated ComponentMetrics [%s] with (%s)",
                    metric.component_type(),
                    str(metric),
                )
            except InvalidComponent as e:
                logger.debug(
                    "Failed to instantiate %s from %s",
                    metric_cls.component_type(),
                    str(e),
                )

    defis_enabled(self) -> bool:
        return len(self.metrics) > 0

    defget_num_flops(self, ctx: ExecutionContext, per_gpu: bool = True) -> int:
        return sum(metric.get_num_flops(ctx, per_gpu) for metric in self.metrics)

    defget_read_bytes(self, ctx: ExecutionContext, per_gpu: bool = True) -> int:
        return sum(metric.get_read_bytes(ctx, per_gpu) for metric in self.metrics)

    defget_write_bytes(self, ctx: ExecutionContext, per_gpu: bool = True) -> int:
        return sum(metric.get_write_bytes(ctx, per_gpu) for metric in self.metrics)

    defget_num_flops_breakdown(
        self, ctx: ExecutionContext, per_gpu: bool = True
    ) -> dict[str, int]:
        total = {}
        for metric in self.metrics:
            breakdown = metric.get_num_flops_breakdown(ctx, per_gpu)
            component = metric.component_type()
            prefixed = {f"{component}.{key}": val for key, val in breakdown.items()}
            total.update(prefixed)
        return total

    defget_read_bytes_breakdown(
        self, ctx: ExecutionContext, per_gpu: bool = True
    ) -> dict[str, int]:
        total = {}
        for metric in self.metrics:
            breakdown = metric.get_read_bytes_breakdown(ctx, per_gpu)
            component = metric.component_type()
            prefixed = {f"{component}.{key}": val for key, val in breakdown.items()}
            total.update(prefixed)
        return total

    defget_write_bytes_breakdown(
        self, ctx: ExecutionContext, per_gpu: bool = True
    ) -> dict[str, int]:
        total = {}
        for metric in self.metrics:
            breakdown = metric.get_write_bytes_breakdown(ctx, per_gpu)
            component = metric.component_type()
            prefixed = {f"{component}.{key}": val for key, val in breakdown.items()}
            total.update(prefixed)
        return total

    defget_step_perf_stats_per_gpu(
        self, scheduler_output: SchedulerOutput
    ) -> PerfStats:
"""
        Calculate perf stats for the current step based on scheduled tokens.
        """

        t0 = time.monotonic()

        # Build a single batch context
        ctx = ExecutionContext()

        # Process new requests (these are in prefill phase)
        for new_req in scheduler_output.scheduled_new_reqs:
            req_id = new_req.req_id
            num_tokens = scheduler_output.num_scheduled_tokens.get(req_id, 0)
            if num_tokens == 0:
                continue

            # For new requests, context_len = num_computed_tokens + num_tokens
            # num_computed_tokens represents previously computed tokens in the sequence
            context_len = new_req.num_computed_tokens + num_tokens
            ctx.add(num_tokens, context_len, is_prefill=True)

        # Process cached requests (continuing requests)
        cached_reqs = scheduler_output.scheduled_cached_reqs
        for i, req_id in enumerate(cached_reqs.req_ids):
            num_tokens = scheduler_output.num_scheduled_tokens.get(req_id, 0)
            if num_tokens == 0:
                continue

            # For cached requests, we have the current num_computed_tokens
            num_computed_tokens = cached_reqs.num_computed_tokens[i]
            context_len = num_computed_tokens + num_tokens

            # Cached requests are typically in decode phase (num_tokens == 1)
            # unless they're doing chunked prefill (num_tokens > 1)
            is_prefill = num_tokens > 1
            ctx.add(num_tokens, context_len, is_prefill)

        num_flops_breakdown = self.get_num_flops_breakdown(ctx, True)
        read_bytes_breakdown = self.get_read_bytes_breakdown(ctx, True)
        write_bytes_breakdown = self.get_write_bytes_breakdown(ctx, True)
        perf_stats = PerfStats(
            sum(num_flops_breakdown.values()),
            sum(read_bytes_breakdown.values()),
            sum(write_bytes_breakdown.values()),
        )

        if envs.VLLM_DEBUG_MFU_METRICS:
            perf_stats.debug_stats = DebugPerfStats(
                time.monotonic() - t0,
                ctx.num_prefill_requests,
                ctx.num_decode_requests,
                asdict(ctx),
                num_flops_breakdown,
                read_bytes_breakdown,
                write_bytes_breakdown,
            )

        return perf_stats
```

### \_\_init\__ [¶](#vllm.v1.metrics.perf.ModelMetrics.__init__ "Permanent link")

Parse vllm\_config to instantiate metrics for each component. is\_enabled() will return False if no component metrics could be instantiated.

Source code in `vllm/v1/metrics/perf.py`

```
def__init__(self, vllm_config: VllmConfig) -> None:
"""
    Parse vllm_config to instantiate metrics for each component.
    is_enabled() will return False if no component metrics could be instantiated.
    """

    self.vllm_config = vllm_config

    self.metrics: list[ComponentMetrics] = []
    for metric_cls in ComponentMetrics.registered_metrics():
        try:
            metric = metric_cls.from_vllm_config(vllm_config)
            self.metrics.append(metric)
            logger.info(
                "Instantiated ComponentMetrics [%s] with (%s)",
                metric.component_type(),
                str(metric),
            )
        except InvalidComponent as e:
            logger.debug(
                "Failed to instantiate %s from %s",
                metric_cls.component_type(),
                str(e),
            )
```

### get\_step\_perf\_stats\_per\_gpu [¶](#vllm.v1.metrics.perf.ModelMetrics.get_step_perf_stats_per_gpu "Permanent link")

```
get_step_perf_stats_per_gpu(
    scheduler_output: SchedulerOutput,
) -> PerfStats
```

Calculate perf stats for the current step based on scheduled tokens.

Source code in `vllm/v1/metrics/perf.py`

```
defget_step_perf_stats_per_gpu(
    self, scheduler_output: SchedulerOutput
) -> PerfStats:
"""
    Calculate perf stats for the current step based on scheduled tokens.
    """

    t0 = time.monotonic()

    # Build a single batch context
    ctx = ExecutionContext()

    # Process new requests (these are in prefill phase)
    for new_req in scheduler_output.scheduled_new_reqs:
        req_id = new_req.req_id
        num_tokens = scheduler_output.num_scheduled_tokens.get(req_id, 0)
        if num_tokens == 0:
            continue

        # For new requests, context_len = num_computed_tokens + num_tokens
        # num_computed_tokens represents previously computed tokens in the sequence
        context_len = new_req.num_computed_tokens + num_tokens
        ctx.add(num_tokens, context_len, is_prefill=True)

    # Process cached requests (continuing requests)
    cached_reqs = scheduler_output.scheduled_cached_reqs
    for i, req_id in enumerate(cached_reqs.req_ids):
        num_tokens = scheduler_output.num_scheduled_tokens.get(req_id, 0)
        if num_tokens == 0:
            continue

        # For cached requests, we have the current num_computed_tokens
        num_computed_tokens = cached_reqs.num_computed_tokens[i]
        context_len = num_computed_tokens + num_tokens

        # Cached requests are typically in decode phase (num_tokens == 1)
        # unless they're doing chunked prefill (num_tokens > 1)
        is_prefill = num_tokens > 1
        ctx.add(num_tokens, context_len, is_prefill)

    num_flops_breakdown = self.get_num_flops_breakdown(ctx, True)
    read_bytes_breakdown = self.get_read_bytes_breakdown(ctx, True)
    write_bytes_breakdown = self.get_write_bytes_breakdown(ctx, True)
    perf_stats = PerfStats(
        sum(num_flops_breakdown.values()),
        sum(read_bytes_breakdown.values()),
        sum(write_bytes_breakdown.values()),
    )

    if envs.VLLM_DEBUG_MFU_METRICS:
        perf_stats.debug_stats = DebugPerfStats(
            time.monotonic() - t0,
            ctx.num_prefill_requests,
            ctx.num_decode_requests,
            asdict(ctx),
            num_flops_breakdown,
            read_bytes_breakdown,
            write_bytes_breakdown,
        )

    return perf_stats
```

## MoeLayerFreqParser [¶](#vllm.v1.metrics.perf.MoeLayerFreqParser "Permanent link")

Bases: `Parser`

Parses moe\_layer\_freq and first\_k\_dense\_replace fields for models like Deepseek.

Overrides: num\_moe\_layers

Source code in `vllm/v1/metrics/perf.py`

```
classMoeLayerFreqParser(Parser):
"""
    Parses moe_layer_freq and first_k_dense_replace fields for models like Deepseek.

    Overrides: num_moe_layers
    """

    defparse(self, args: ParsedArgs, vllm_config: VllmConfig) -> ParsedArgs:
        cfg = vllm_config.model_config.hf_config
        if hasattr(cfg, "text_config") and cfg.text_config is not None:
            cfg = cfg.text_config

        if hasattr(cfg, "moe_layer_freq") and hasattr(cfg, "first_k_dense_replace"):
            args.num_moe_layers = len(
                [
                    layer
                    for layer in range(args.num_hidden_layers)
                    if layer >= cfg.first_k_dense_replace
                    and layer % cfg.moe_layer_freq == 0
                ]
            )

        return args
```

## ParsedArgs [¶](#vllm.v1.metrics.perf.ParsedArgs "Permanent link")

Syntactic sugar so that Parsers can use dot notations to access/update the parsed arguments.

e.g.) args = ParsedArgs() args.x = 3 args.y = args.x + 1

Source code in `vllm/v1/metrics/perf.py`

```
classParsedArgs:
"""
    Syntactic sugar so that Parsers can use dot notations
    to access/update the parsed arguments.

    e.g.)
        args = ParsedArgs()
        args.x = 3
        args.y = args.x + 1
    """

    def__getattr__(self, name: str) -> Any:
        raise AttributeError(f"'{type(self).__name__}' has no attribute '{name}'")

    def__setattr__(self, name: str, value: Any) -> None:
        object.__setattr__(self, name, value)

    defmodel_dump(self) -> dict[str, Any]:
        return vars(self).copy()
```

## Parser [¶](#vllm.v1.metrics.perf.Parser "Permanent link")

Bases: `Protocol`

Source code in `vllm/v1/metrics/perf.py`

```
classParser(Protocol):
    defparse(self, args: ParsedArgs, vllm_config: VllmConfig) -> ParsedArgs:
"""
        Parse the vllm config and update the current ParsedArgs and pass it on.
        If the parser isn't applicable to the vllm_config, it will do nothing.
        """
        ...
```

### parse [¶](#vllm.v1.metrics.perf.Parser.parse "Permanent link")

Parse the vllm config and update the current ParsedArgs and pass it on. If the parser isn't applicable to the vllm\_config, it will do nothing.

Source code in `vllm/v1/metrics/perf.py`

```
defparse(self, args: ParsedArgs, vllm_config: VllmConfig) -> ParsedArgs:
"""
    Parse the vllm config and update the current ParsedArgs and pass it on.
    If the parser isn't applicable to the vllm_config, it will do nothing.
    """
    ...
```

## ParserChain [¶](#vllm.v1.metrics.perf.ParserChain "Permanent link")

Applies chain of parser in a sequential order. Later parsers might overwrite results from previous parsers, so parsers should be chained in the appropriate order if they are not mutually exclusive.

Source code in `vllm/v1/metrics/perf.py`

```
classParserChain:
"""
    Applies chain of parser in a sequential order.
    Later parsers might overwrite results from previous parsers,
    so parsers should be chained in the appropriate order if they
    are not mutually exclusive.
    """

    def__init__(self, *parsers: Parser) -> None:
        self.parsers = list(parsers)

    defadd_parser(self, parser: Parser) -> None:
        self.parsers.append(parser)

    defparse(self, vllm_config: VllmConfig) -> ParsedArgs:
        args = ParsedArgs()
        for parser in self.parsers:
            args = parser.parse(args, vllm_config)
        return args
```

## PerfMetricsProm [¶](#vllm.v1.metrics.perf.PerfMetricsProm "Permanent link")

Record performance metrics in Prometheus.

Average TFLOPS (tera floating-point operations per second) can be calculated using a PromQL query:

rate(vllm:estimated\_flops\_per\_gpu\_total\[1m]) / 1e12

Average memory bandwidth in GB/s can be calculated using:

(rate(vllm:estimated\_read\_bytes\_per\_gpu\_total\[1m]) + rate(vllm:estimated\_write\_bytes\_per\_gpu\_total\[1m])) / 1e9

Source code in `vllm/v1/metrics/perf.py`

```
classPerfMetricsProm:
"""Record performance metrics in Prometheus.

    Average TFLOPS (tera floating-point operations per second) can be
    calculated using a PromQL query:

      rate(vllm:estimated_flops_per_gpu_total[1m]) / 1e12

    Average memory bandwidth in GB/s can be calculated using:

      (rate(vllm:estimated_read_bytes_per_gpu_total[1m]) +
       rate(vllm:estimated_write_bytes_per_gpu_total[1m])) / 1e9
    """

    _counter_cls = prometheus_client.Counter

    def__init__(
        self,
        vllm_config: VllmConfig,
        labelnames: list[str],
        per_engine_labelvalues: dict[int, list[object]],
    ):
        counter_flops = self._counter_cls(
            name="vllm:estimated_flops_per_gpu_total",
            documentation=(
                "Estimated number of floating point operations per GPU "
                "(for Model Flops Utilization calculations)."
            ),
            labelnames=labelnames,
        )
        self.counter_flops = create_metric_per_engine(
            counter_flops, per_engine_labelvalues
        )

        counter_read_bytes = self._counter_cls(
            name="vllm:estimated_read_bytes_per_gpu_total",
            documentation=(
                "Estimated number of bytes read from memory per GPU "
                "(for Model Flops Utilization calculations)."
            ),
            labelnames=labelnames,
        )
        self.counter_read_bytes = create_metric_per_engine(
            counter_read_bytes, per_engine_labelvalues
        )

        counter_write_bytes = self._counter_cls(
            name="vllm:estimated_write_bytes_per_gpu_total",
            documentation=(
                "Estimated number of bytes written to memory per GPU "
                "(for Model Flops Utilization calculations)."
            ),
            labelnames=labelnames,
        )
        self.counter_write_bytes = create_metric_per_engine(
            counter_write_bytes, per_engine_labelvalues
        )

    defobserve(self, perf_stats: PerfStats, engine_idx: int = 0):
        if not (
            perf_stats.num_flops_per_gpu
            or perf_stats.num_read_bytes_per_gpu
            or perf_stats.num_write_bytes_per_gpu
        ):
            return
        self.counter_flops[engine_idx].inc(perf_stats.num_flops_per_gpu)
        self.counter_read_bytes[engine_idx].inc(perf_stats.num_read_bytes_per_gpu)
        self.counter_write_bytes[engine_idx].inc(perf_stats.num_write_bytes_per_gpu)
```

## UnembedMetrics [¶](#vllm.v1.metrics.perf.UnembedMetrics "Permanent link")

Bases: `ComponentMetrics`

Source code in `vllm/v1/metrics/perf.py`

```
classUnembedMetrics(ComponentMetrics):
    # From BaseConfigParser
    hidden_size: int = Field(..., gt=0)
    vocab_size: int = Field(..., gt=0)
    weight_byte_size: int = Field(..., gt=0)
    activation_byte_size: int = Field(..., gt=0)

    tp_size: int

    @classmethod
    defcomponent_type(cls) -> str:
        return "unembed"

    @classmethod
    defget_parser(cls) -> ParserChain:
        return ParserChain(
            BaseConfigParser(),
        )

    defget_num_flops_breakdown(
        self, ctx: ExecutionContext, per_gpu: bool = True
    ) -> dict[str, int]:
"""Calculate flops breakdown for unembedding layer."""
        D, V = self.hidden_size, self.vocab_size
        T = ctx.num_logits_tokens()

        if per_gpu:
            V //= self.tp_size

        return {
            "unembed": 2 * T * D * V,
        }

    defget_read_bytes_breakdown(
        self, ctx: ExecutionContext, per_gpu: bool = True
    ) -> dict[str, int]:
"""Calculate read memory traffic for unembedding layer."""
        D, V = self.hidden_size, self.vocab_size
        T = ctx.num_logits_tokens()

        if per_gpu:
            V //= self.tp_size

        return {
            "input": T * D * self.activation_byte_size,
            "weight": D * V * self.weight_byte_size,
        }

    defget_write_bytes_breakdown(
        self, ctx: ExecutionContext, per_gpu: bool = True
    ) -> dict[str, int]:
"""Calculate write memory traffic for unembedding layer."""
        V = self.vocab_size
        T = ctx.num_logits_tokens()

        if per_gpu:
            V //= self.tp_size

        return {
            "output": T * V * self.activation_byte_size,
        }
```

### get\_num\_flops\_breakdown [¶](#vllm.v1.metrics.perf.UnembedMetrics.get_num_flops_breakdown "Permanent link")

Calculate flops breakdown for unembedding layer.

Source code in `vllm/v1/metrics/perf.py`

```
defget_num_flops_breakdown(
    self, ctx: ExecutionContext, per_gpu: bool = True
) -> dict[str, int]:
"""Calculate flops breakdown for unembedding layer."""
    D, V = self.hidden_size, self.vocab_size
    T = ctx.num_logits_tokens()

    if per_gpu:
        V //= self.tp_size

    return {
        "unembed": 2 * T * D * V,
    }
```

### get\_read\_bytes\_breakdown [¶](#vllm.v1.metrics.perf.UnembedMetrics.get_read_bytes_breakdown "Permanent link")

Calculate read memory traffic for unembedding layer.

Source code in `vllm/v1/metrics/perf.py`

```
defget_read_bytes_breakdown(
    self, ctx: ExecutionContext, per_gpu: bool = True
) -> dict[str, int]:
"""Calculate read memory traffic for unembedding layer."""
    D, V = self.hidden_size, self.vocab_size
    T = ctx.num_logits_tokens()

    if per_gpu:
        V //= self.tp_size

    return {
        "input": T * D * self.activation_byte_size,
        "weight": D * V * self.weight_byte_size,
    }
```

### get\_write\_bytes\_breakdown [¶](#vllm.v1.metrics.perf.UnembedMetrics.get_write_bytes_breakdown "Permanent link")

Calculate write memory traffic for unembedding layer.

Source code in `vllm/v1/metrics/perf.py`

```
defget_write_bytes_breakdown(
    self, ctx: ExecutionContext, per_gpu: bool = True
) -> dict[str, int]:
"""Calculate write memory traffic for unembedding layer."""
    V = self.vocab_size
    T = ctx.num_logits_tokens()

    if per_gpu:
        V //= self.tp_size

    return {
        "output": T * V * self.activation_byte_size,
    }
```

## get\_required [¶](#vllm.v1.metrics.perf.get_required "Permanent link")

Get an attr from an object, or throw a InvalidComponentError if it's not set.

Source code in `vllm/v1/metrics/perf.py`

```
defget_required(obj: object, attr: str):
"""Get an attr from an object, or throw a InvalidComponentError if it's not set."""
    if not hasattr(obj, attr):
        raise InvalidComponent(f"Missing required attr {attr} in config")
    return getattr(obj, attr)
```

## getattr\_from\_list [¶](#vllm.v1.metrics.perf.getattr_from_list "Permanent link")

Try to get the first attr that exists in the object from a list of attrs. Otherwise return None.

Source code in `vllm/v1/metrics/perf.py`

```
defgetattr_from_list(obj: object, attrs: list[str], default: object = None):
"""Try to get the first attr that exists in the object
    from a list of attrs. Otherwise return None."""
    for attr in attrs:
        if hasattr(obj, attr):
            return getattr(obj, attr)
    return default
```