---
title: load - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/config/load/
source: sitemap
fetched_at: 2026-05-07T21:16:59.883346396-03:00
rendered_js: false
word_count: 693
summary: This document defines the LoadConfig class in vLLM, which provides configuration options for specifying how model weights are loaded, including supported formats, loading strategies, and directory paths.
tags:
    - vllm
    - model-loading
    - configuration
    - weight-formats
    - safetensors
    - pytorch
category: reference
---

Configuration for loading the model weights.

Source code in `vllm/config/load.py`

```
@config
classLoadConfig:
"""Configuration for loading the model weights."""

    load_format: str | LoadFormats = "auto"
"""
    The format of the model weights to load.

    - "auto" will try to load the weights in the safetensors format and fall
      back to the pytorch bin format if safetensors format is not available.
    - "pt" will load the weights in the pytorch bin format.
    - "safetensors" will load the weights in the safetensors format.
    - "instanttensor" will load the Safetensors weights on CUDA devices using
      InstantTensor, which enables distributed loading with pipelined prefetching
      and fast direct I/O.
    - "npcache" will load the weights in pytorch format and store a numpy cache
      to speed up the loading.
    - "dummy" will initialize the weights with random values, which is mainly
      for profiling.
    - "tensorizer" will use CoreWeave's tensorizer library for fast weight
      loading. See the Tensorize vLLM Model script in the Examples section for
      more information.
    - "runai_streamer" will load the Safetensors weights using Run:ai Model
      Streamer.
    - "runai_streamer_sharded" will load weights from pre-sharded checkpoint
      files using Run:ai Model Streamer.
    - "bitsandbytes" will load the weights using bitsandbytes quantization.
    - "sharded_state" will load weights from pre-sharded checkpoint files,
      supporting efficient loading of tensor-parallel models.
    - "gguf" will load weights from GGUF format files (details specified in
      https://github.com/ggml-org/ggml/blob/master/docs/gguf.md).
    - "mistral" will load weights from consolidated safetensors files used by
      Mistral models.
    - Other custom values can be supported via plugins.
    """
    download_dir: str | None = None
"""Directory to download and load the weights, default to the default
    cache directory of Hugging Face."""
    safetensors_load_strategy: str | None = None
"""
    Specifies the loading strategy for safetensors weights.

    - None (default): Uses memory-mapped (lazy) loading. When an NFS
      filesystem is detected and the total checkpoint size fits within 90%%
      of available RAM, prefetching is enabled automatically.
    - "lazy": Weights are memory-mapped from the file. This enables
      on-demand loading and is highly efficient for models on local storage.
      Unlike the default (None), auto-prefetch on NFS is not performed.
    - "eager": The entire file is read into CPU memory upfront before loading.
      This is recommended for models on network filesystems (e.g., Lustre, NFS)
      as it avoids inefficient random reads, significantly speeding up model
      initialization. However, it uses more CPU RAM.
    - "prefetch": Checkpoint files are read into the OS page cache before
      workers load them, speeding up the model loading phase. Useful on
      network or high-latency storage.
    - "torchao": Weights are loaded in upfront and then reconstructed
      into torchao tensor subclasses. This is used when the checkpoint
      was quantized using torchao and saved using safetensors.
      Needs `torchao >= 0.14.0`.
    """
    model_loader_extra_config: dict | TensorizerConfig = Field(default_factory=dict)
"""Extra config for model loader. This will be passed to the model loader
    corresponding to the chosen load_format."""
    device: str | None = None
"""Device to which model weights will be loaded, default to
    device_config.device"""
    ignore_patterns: list[str] | str = Field(default_factory=lambda: ["original/**/*"])
"""The list of patterns to ignore when loading the model. Default to
    "original/**/*" to avoid repeated loading of llama's checkpoints."""
    use_tqdm_on_load: bool = True
"""Whether to enable tqdm for showing progress bar when loading model
    weights."""
    pt_load_map_location: str | dict[str, str] = "cpu"
"""
    The map location for loading pytorch checkpoint, to support loading
    checkpoints can only be loaded on certain devices like "cuda", this
    is equivalent to `{"": "cuda"}`. Another supported format is mapping
    from different devices like from GPU 1 to GPU 0: `{"cuda:1": "cuda:0"}`.
    Note that when passed from command line, the strings in dictionary
    need to be double quoted for json parsing. For more details, see
    the original doc for `map_location` parameter in [`torch.load`][] parameter.
    """

    defcompute_hash(self) -> str:
"""
        WARNING: Whenever a new field is added to this config,
        ensure that it is included in the factors list if
        it affects the computation graph.

        Provide a hash that uniquely identifies all the configs
        that affect the structure of the computation
        graph from input ids/embeddings to the final hidden states,
        excluding anything before input ids/embeddings and after
        the final hidden states.
        """
        # no factors to consider.
        # this config will not affect the computation graph.
        factors: list[Any] = []
        hash_str = safe_hash(str(factors).encode(), usedforsecurity=False).hexdigest()
        return hash_str

    @field_validator("load_format", mode="after")
    def_lowercase_load_format(cls, load_format: str) -> str:
        return load_format.lower()

    @field_validator("ignore_patterns", mode="after")
    def_validate_ignore_patterns(
        cls, ignore_patterns: list[str] | str
    ) -> list[str] | str:
        if ignore_patterns != ["original/**/*"] and len(ignore_patterns) > 0:
            logger.info(
                "Ignoring the following patterns when downloading weights: %s",
                ignore_patterns,
            )

        return ignore_patterns
```

### device `class-attribute` `instance-attribute` [¶](#vllm.config.load.LoadConfig.device "Permanent link")

```
device: str | None = None
```

Device to which model weights will be loaded, default to device\_config.device

### download\_dir `class-attribute` `instance-attribute` [¶](#vllm.config.load.LoadConfig.download_dir "Permanent link")

```
download_dir: str | None = None
```

Directory to download and load the weights, default to the default cache directory of Hugging Face.

### ignore\_patterns `class-attribute` `instance-attribute` [¶](#vllm.config.load.LoadConfig.ignore_patterns "Permanent link")

```
ignore_patterns: list[str] | str = Field(
    default_factory=lambda: ["original/**/*"]
)
```

The list of patterns to ignore when loading the model. Default to "original/\**/*" to avoid repeated loading of llama's checkpoints.

### load\_format `class-attribute` `instance-attribute` [¶](#vllm.config.load.LoadConfig.load_format "Permanent link")

```
load_format: str | LoadFormats = 'auto'
```

The format of the model weights to load.

- "auto" will try to load the weights in the safetensors format and fall back to the pytorch bin format if safetensors format is not available.
- "pt" will load the weights in the pytorch bin format.
- "safetensors" will load the weights in the safetensors format.
- "instanttensor" will load the Safetensors weights on CUDA devices using InstantTensor, which enables distributed loading with pipelined prefetching and fast direct I/O.
- "npcache" will load the weights in pytorch format and store a numpy cache to speed up the loading.
- "dummy" will initialize the weights with random values, which is mainly for profiling.
- "tensorizer" will use CoreWeave's tensorizer library for fast weight loading. See the Tensorize vLLM Model script in the Examples section for more information.
- "runai\_streamer" will load the Safetensors weights using Run:ai Model Streamer.
- "runai\_streamer\_sharded" will load weights from pre-sharded checkpoint files using Run:ai Model Streamer.
- "bitsandbytes" will load the weights using bitsandbytes quantization.
- "sharded\_state" will load weights from pre-sharded checkpoint files, supporting efficient loading of tensor-parallel models.
- "gguf" will load weights from GGUF format files (details specified in https://github.com/ggml-org/ggml/blob/master/docs/gguf.md).
- "mistral" will load weights from consolidated safetensors files used by Mistral models.
- Other custom values can be supported via plugins.

Extra config for model loader. This will be passed to the model loader corresponding to the chosen load\_format.

### pt\_load\_map\_location `class-attribute` `instance-attribute` [¶](#vllm.config.load.LoadConfig.pt_load_map_location "Permanent link")

The map location for loading pytorch checkpoint, to support loading checkpoints can only be loaded on certain devices like "cuda", this is equivalent to `{"": "cuda"}`. Another supported format is mapping from different devices like from GPU 1 to GPU 0: `{"cuda:1": "cuda:0"}`. Note that when passed from command line, the strings in dictionary need to be double quoted for json parsing. For more details, see the original doc for `map_location` parameter in [`torch.load`](https://pytorch.org/docs/stable/generated/torch.load.html#torch.load) parameter.

### safetensors\_load\_strategy `class-attribute` `instance-attribute` [¶](#vllm.config.load.LoadConfig.safetensors_load_strategy "Permanent link")

```
safetensors_load_strategy: str | None = None
```

Specifies the loading strategy for safetensors weights.

- None (default): Uses memory-mapped (lazy) loading. When an NFS filesystem is detected and the total checkpoint size fits within 90%% of available RAM, prefetching is enabled automatically.
- "lazy": Weights are memory-mapped from the file. This enables on-demand loading and is highly efficient for models on local storage. Unlike the default (None), auto-prefetch on NFS is not performed.
- "eager": The entire file is read into CPU memory upfront before loading. This is recommended for models on network filesystems (e.g., Lustre, NFS) as it avoids inefficient random reads, significantly speeding up model initialization. However, it uses more CPU RAM.
- "prefetch": Checkpoint files are read into the OS page cache before workers load them, speeding up the model loading phase. Useful on network or high-latency storage.
- "torchao": Weights are loaded in upfront and then reconstructed into torchao tensor subclasses. This is used when the checkpoint was quantized using torchao and saved using safetensors. Needs `torchao >= 0.14.0`.

### use\_tqdm\_on\_load `class-attribute` `instance-attribute` [¶](#vllm.config.load.LoadConfig.use_tqdm_on_load "Permanent link")

```
use_tqdm_on_load: bool = True
```

Whether to enable tqdm for showing progress bar when loading model weights.

### compute\_hash [¶](#vllm.config.load.LoadConfig.compute_hash "Permanent link")

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

Source code in `vllm/config/load.py`

```
defcompute_hash(self) -> str:
"""
    WARNING: Whenever a new field is added to this config,
    ensure that it is included in the factors list if
    it affects the computation graph.

    Provide a hash that uniquely identifies all the configs
    that affect the structure of the computation
    graph from input ids/embeddings to the final hidden states,
    excluding anything before input ids/embeddings and after
    the final hidden states.
    """
    # no factors to consider.
    # this config will not affect the computation graph.
    factors: list[Any] = []
    hash_str = safe_hash(str(factors).encode(), usedforsecurity=False).hexdigest()
    return hash_str
```