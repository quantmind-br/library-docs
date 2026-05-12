---
title: vllm bench throughput - vLLM
url: https://docs.vllm.ai/en/latest/cli/bench/throughput/
source: sitemap
fetched_at: 2026-05-07T21:11:01.919235991-03:00
rendered_js: false
word_count: 8352
summary: This document provides a reference for the command-line interface arguments used to configure throughput benchmarking in the vLLM project, including dataset selection, hardware-specific backend settings, and random sampling parameters.
tags:
    - vllm
    - benchmarking
    - throughput
    - cli-arguments
    - model-serving
    - performance-testing
category: reference
---

[](https://github.com/vllm-project/vllm/edit/main/docs/cli/bench/throughput.md "Edit this page")

## JSON CLI Arguments[¶](#json-cli-arguments "Permanent link")

When passing JSON CLI arguments, the following sets of arguments are equivalent:

- `--json-arg '{"key1": "value1", "key2": {"key3": "value2"}}'`
- `--json-arg.key1 value1 --json-arg.key2.key3 value2`

Additionally, list elements can be passed individually using `+`:

- `--json-arg '{"key4": ["value3", "value4", "value5"]}'`
- `--json-arg.key4+ value3 --json-arg.key4+='value4,value5'`

## Arguments[¶](#arguments "Permanent link")

#### `--backend`[¶](#-backend "Permanent link")

Possible choices: `vllm`, `hf`, `mii`, `vllm-chat`

Default: `vllm`

#### `--dataset-name`[¶](#-dataset-name "Permanent link")

Possible choices: `sharegpt`, `random`, `sonnet`, `burstgpt`, `hf`, `prefix_repetition`, `random-mm`, `random-rerank`

Name of the dataset to benchmark on.

Default: `sharegpt`

#### `--dataset`[¶](#-dataset "Permanent link")

Path to the ShareGPT dataset, will be deprecated in the next release. The dataset is expected to be a json in form of list\[dict\[..., conversations: list\[dict\[..., value: ]]]]

#### `--dataset-path`[¶](#-dataset-path "Permanent link")

Path to the dataset

#### `--input-len`[¶](#-input-len "Permanent link")

Input prompt length for each request

#### `--output-len`[¶](#-output-len "Permanent link")

Output length for each request. Overrides the output length from the dataset.

#### `--n`[¶](#-n "Permanent link")

Number of generated sequences per prompt.

Default: `1`

#### `--num-prompts`[¶](#-num-prompts "Permanent link")

Number of prompts to process.

Default: `1000`

#### `--hf-max-batch-size`[¶](#-hf-max-batch-size "Permanent link")

Maximum batch size for HF backend.

#### `--hf-enable-torch-compile`[¶](#-hf-enable-torch-compile "Permanent link")

Enable Torch compile for HF backend.

Default: `False`

#### `--output-json`[¶](#-output-json "Permanent link")

Path to save the throughput results in JSON format.

#### `--async-engine`[¶](#-async-engine "Permanent link")

Use vLLM async engine rather than LLM class.

Default: `False`

#### `--disable-detokenize`[¶](#-disable-detokenize "Permanent link")

Do not detokenize the response (i.e. do not include detokenization time in the measurement)

Default: `False`

#### `--lora-path`[¶](#-lora-path "Permanent link")

Path to the lora adapters to use. This can be an absolute path, a relative path, or a Hugging Face model identifier.

#### `--lora-assignment`[¶](#-lora-assignment "Permanent link")

Possible choices: `random`, `round-robin`

Strategy for assigning LoRA adapters to requests. 'random' (default) selects a LoRA at random for each request. 'round-robin' cycles through LoRAs deterministically.

Default: `random`

#### `--prefix-len`[¶](#-prefix-len "Permanent link")

Number of fixed prefix tokens before the random context in a request (default: 0).

Default: `0`

#### `--hf-subset`[¶](#-hf-subset "Permanent link")

Subset of the HF dataset.

#### `--hf-split`[¶](#-hf-split "Permanent link")

Split of the HF dataset.

#### `--hf-name`[¶](#-hf-name "Permanent link")

Name of the dataset on HuggingFace (e.g., 'lmms-lab/LLaVA-OneVision-Data'). Specify this when --dataset-path is a local filesystem path so the benchmark can identify the correct dataset class.

#### `--profile`[¶](#-profile "Permanent link")

Use vLLM Profiling. --profiler-config must be provided on the server.

Default: `False`

#### `--prefix-repetition-prefix-len`[¶](#-prefix-repetition-prefix-len "Permanent link")

Number of prefix tokens per request, used only for prefix repetition dataset.

#### `--prefix-repetition-suffix-len`[¶](#-prefix-repetition-suffix-len "Permanent link")

Number of suffix tokens per request, used only for prefix repetition dataset. Total input length is prefix\_len + suffix\_len.

#### `--prefix-repetition-num-prefixes`[¶](#-prefix-repetition-num-prefixes "Permanent link")

Number of prefixes to generate, used only for prefix repetition dataset. Prompts per prefix is num\_requests // num\_prefixes.

#### `--prefix-repetition-output-len`[¶](#-prefix-repetition-output-len "Permanent link")

Number of output tokens per request, used only for prefix repetition dataset.

#### `--random-input-len`[¶](#-random-input-len "Permanent link")

Number of input tokens per request, used only for random sampling.

Default: `1024`

#### `--random-output-len`[¶](#-random-output-len "Permanent link")

Number of output tokens per request, used only for random sampling.

Default: `128`

#### `--random-range-ratio`[¶](#-random-range-ratio "Permanent link")

Range ratio for sampling input/output length, used only for random sampling. A single float applies to both ISL and OSL. A JSON dict like '{"input": 0.3, "output": 0.5}' sets them independently. Values must be in [0, 1).

Default: `0.0`

#### `--random-prefix-len`[¶](#-random-prefix-len "Permanent link")

Number of fixed prefix tokens before the random context in a request. The total input length is the sum of `random-prefix-len` and a random context length sampled from \[input\_len * (1 - range\_ratio), input\_len * (1 + range\_ratio)].

Default: `0`

#### `--random-batch-size`[¶](#-random-batch-size "Permanent link")

Batch size for random sampling. Only used for embeddings benchmark.

Default: `1`

#### `--no-reranker`[¶](#-no-reranker "Permanent link")

Whether the model supports reranking natively. Only used for reranker benchmark.

Default: `False`

#### `--random-mm-base-items-per-request`[¶](#-random-mm-base-items-per-request "Permanent link")

Base number of multimodal items per request for random-mm. Actual per-request count is sampled around this base using --random-mm-num-mm-items-range-ratio.

Default: `1`

#### `--random-mm-num-mm-items-range-ratio`[¶](#-random-mm-num-mm-items-range-ratio "Permanent link")

Range ratio r in \[0, 1] for sampling items per request. We sample uniformly from the closed integer range \[floor(n*(1-r)), ceil(n*(1+r))] where n is the base items per request. r=0 keeps it fixed; r=1 allows 0 items. The maximum is clamped to the sum of per-modality limits from --random-mm-limit-mm-per-prompt. An error is raised if the computed min exceeds the max.

Default: `0.0`

#### `--random-mm-limit-mm-per-prompt`[¶](#-random-mm-limit-mm-per-prompt "Permanent link")

Per-modality hard caps for items attached per request, e.g. '{"image": 3, "video": 0}'. The sampled per-request item count is clamped to the sum of these limits. When a modality reaches its cap, its buckets are excluded and probabilities are renormalized.OBS.: Only image sampling is supported for now.

Default: `{'image': 255, 'video': 1}`

#### `--random-mm-bucket-config`[¶](#-random-mm-bucket-config "Permanent link")

The bucket config is a dictionary mapping a multimodal itemsampling configuration to a probability.Currently allows for 2 modalities: images and videos. An bucket key is a tuple of (height, width, num\_frames)The value is the probability of sampling that specific item. Example: --random-mm-bucket-config {(256, 256, 1): 0.5, (720, 1280, 1): 0.4, (720, 1280, 16): 0.10} First item: images with resolution 256x256 w.p. 0.5Second item: images with resolution 720x1280 w.p. 0.4 Third item: videos with resolution 720x1280 and 16 frames w.p. 0.1OBS.: If the probabilities do not sum to 1, they are normalized.OBS bis.: Only image sampling is supported for now.

Default: `{(256, 256, 1): 0.5, (720, 1280, 1): 0.5, (720, 1280, 16): 0.0}`

#### `--asr-min-audio-len-sec`[¶](#-asr-min-audio-len-sec "Permanent link")

Minimum audio duration in seconds for ASR dataset filtering.

Default: `0.0`

#### `--asr-max-audio-len-sec`[¶](#-asr-max-audio-len-sec "Permanent link")

Maximum audio duration in seconds for ASR dataset filtering.

Default: `inf`

#### `--disable-log-stats`[¶](#-disable-log-stats "Permanent link")

Disable logging statistics.

Default: `False`

#### `--aggregate-engine-logging`[¶](#-aggregate-engine-logging "Permanent link")

Log aggregate rather than per-engine statistics when using data parallelism.

Default: `False`

#### `--fail-on-environ-validation`, `--no-fail-on-environ-validation`[¶](#-fail-on-environ-validation-no-fail-on-environ-validation "Permanent link")

If set, the engine will raise an error if environment validation fails.

Default: `False`

#### `--shutdown-timeout`[¶](#-shutdown-timeout "Permanent link")

Shutdown timeout in seconds. 0 = abort, &gt;0 = wait.

Default: `0`

#### `--gdn-prefill-backend`[¶](#-gdn-prefill-backend "Permanent link")

Possible choices: `flashinfer`, `triton`

Select GDN prefill backend.

#### `--enable-log-requests`, `--no-enable-log-requests`[¶](#-enable-log-requests-no-enable-log-requests "Permanent link")

Enable logging request information, dependent on log level: - INFO: Request ID, parameters and LoRA request. - DEBUG: Prompt inputs (e.g: text, token IDs). You can set the minimum log level via `VLLM_LOGGING_LEVEL`.

Default: `False`

### ModelConfig[¶](#modelconfig "Permanent link")

Configuration for the model.

#### `--model`[¶](#-model "Permanent link")

Name or path of the Hugging Face model to use. It is also used as the content for `model_name` tag in metrics output when `served_model_name` is not specified.

Default: `Qwen/Qwen3-0.6B`

#### `--runner`[¶](#-runner "Permanent link")

Possible choices: `auto`, `draft`, `generate`, `pooling`

The type of model runner to use. Each vLLM instance only supports one model runner, even if the same model can be used for multiple types.

Default: `auto`

#### `--convert`[¶](#-convert "Permanent link")

Possible choices: `auto`, `classify`, `embed`, `none`

Convert the model using adapters defined in [vllm.model\_executor.models.adapters](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/adapters/#vllm.model_executor.models.adapters "            vllm.model_executor.models.adapters"). The most common use case is to adapt a text generation model to be used for pooling tasks.

Default: `auto`

#### `--tokenizer`[¶](#-tokenizer "Permanent link")

Name or path of the Hugging Face tokenizer to use. If unspecified, model name or path will be used.

#### `--tokenizer-mode`[¶](#-tokenizer-mode "Permanent link")

Possible choices: `auto`, `deepseek_v32`, `deepseek_v4`, `fastokens`, `hf`, `mistral`, `slow`

Tokenizer mode:

- "auto" will use the tokenizer from `mistral_common` for Mistral models if available, otherwise it will use the "hf" tokenizer.
- "hf" will use the fast tokenizer if available.
- "slow" will always use the slow tokenizer.
- "mistral" will always use the tokenizer from `mistral_common`.
- "deepseek\_v32" will always use the tokenizer from `deepseek_v32`.
- "deepseek\_v4" will always use the tokenizer from `deepseek_v4`.
- "qwen\_vl" will always use the tokenizer from `qwen_vl`.
- "fastokens" loads a Hugging Face fast tokenizer powered by the [fastokens](https://github.com/crusoecloud/fastokens) Rust BPE backend (requires the `fastokens` package to be installed).
- Other custom values can be supported via plugins.

Default: `auto`

#### `--trust-remote-code`, `--no-trust-remote-code`[¶](#-trust-remote-code-no-trust-remote-code "Permanent link")

Trust remote code (e.g., from HuggingFace) when downloading the model and tokenizer.

Default: `False`

#### `--dtype`[¶](#-dtype "Permanent link")

Possible choices: `auto`, `bfloat16`, `float`, `float16`, `float32`, `half`

Data type for model weights and activations:

- "auto" will use FP16 precision for FP32 and FP16 models, and BF16 precision for BF16 models.
- "half" for FP16. Recommended for AWQ quantization.
- "float16" is the same as "half".
- "bfloat16" for a balance between precision and range.
- "float" is shorthand for FP32 precision.
- "float32" for FP32 precision.

Default: `auto`

#### `--seed`[¶](#-seed "Permanent link")

Random seed for reproducibility.

We must set the global seed because otherwise, different tensor parallel workers would sample different tokens, leading to inconsistent results.

Default: `0`

#### `--hf-config-path`[¶](#-hf-config-path "Permanent link")

Name or path of the Hugging Face config to use. If unspecified, model name or path will be used.

#### `--allowed-local-media-path`[¶](#-allowed-local-media-path "Permanent link")

Allowing API requests to read local images or videos from directories specified by the server file system. This is a security risk. Should only be enabled in trusted environments.

Default: `""`

#### `--allowed-media-domains`[¶](#-allowed-media-domains "Permanent link")

If set, only media URLs that belong to this domain can be used for multi-modal inputs.

#### `--revision`[¶](#-revision "Permanent link")

The specific model version to use. It can be a branch name, a tag name, or a commit id. If unspecified, will use the default version.

#### `--code-revision`[¶](#-code-revision "Permanent link")

The specific revision to use for the model code on the Hugging Face Hub. It can be a branch name, a tag name, or a commit id. If unspecified, will use the default version.

#### `--tokenizer-revision`[¶](#-tokenizer-revision "Permanent link")

The specific revision to use for the tokenizer on the Hugging Face Hub. It can be a branch name, a tag name, or a commit id. If unspecified, will use the default version.

#### `--max-model-len`[¶](#-max-model-len "Permanent link")

Model context length (prompt and output). If unspecified, will be automatically derived from the model config.

When passing via `--max-model-len`, supports k/m/g/K/M/G in human-readable format. Examples:

- 1k -&gt; 1000
- 1K -&gt; 1024
- 25.6k -&gt; 25,600
- -1 or 'auto' -&gt; Automatically choose the maximum model length that fits in GPU memory. This will use the model's maximum context length if it fits, otherwise it will find the largest length that can be accommodated.

Parse human-readable integers like '1k', '2M', etc. Including decimal values with decimal multipliers. Also accepts -1 or 'auto' as a special value for auto-detection.

```
Examples:
- '1k' -> 1,000
- '1K' -> 1,024
- '25.6k' -> 25,600
- '-1' or 'auto' -> -1 (special value for auto-detection)
```

#### `--quantization`, `-q`[¶](#-quantization-q "Permanent link")

Method used to quantize the weights. If `None`, we first check the `quantization_config` attribute in the model config file. If that is `None`, we assume the model weights are not quantized and use `dtype` to determine the data type of the weights.

#### `--allow-deprecated-quantization`, `--no-allow-deprecated-quantization`[¶](#-allow-deprecated-quantization-no-allow-deprecated-quantization "Permanent link")

Whether to allow deprecated quantization methods.

Default: `False`

#### `--enforce-eager`, `--no-enforce-eager`[¶](#-enforce-eager-no-enforce-eager "Permanent link")

Whether to always use eager-mode PyTorch. If True, we will disable CUDA graph and always execute the model in eager mode. If False, we will use CUDA graph and eager execution in hybrid for maximal performance and flexibility.

Default: `False`

#### `--enable-return-routed-experts`, `--no-enable-return-routed-experts`[¶](#-enable-return-routed-experts-no-enable-return-routed-experts "Permanent link")

Whether to return routed experts.

Default: `False`

#### `--max-logprobs`[¶](#-max-logprobs "Permanent link")

Maximum number of log probabilities to return when `logprobs` is specified in `SamplingParams`. The default value comes the default for the OpenAI Chat Completions API. -1 means no cap, i.e. all (output\_length * vocab\_size) logprobs are allowed to be returned and it may cause OOM.

Default: `20`

#### `--logprobs-mode`[¶](#-logprobs-mode "Permanent link")

Possible choices: `processed_logits`, `processed_logprobs`, `raw_logits`, `raw_logprobs`

Indicates the content returned in the logprobs and prompt\_logprobs. Supported mode: 1) raw\_logprobs, 2) processed\_logprobs, 3) raw\_logits, 4) processed\_logits. Raw means the values before applying any logit processors, like bad words. Processed means the values after applying all processors, including temperature and top\_k/top\_p.

Default: `raw_logprobs`

#### `--disable-sliding-window`, `--no-disable-sliding-window`[¶](#-disable-sliding-window-no-disable-sliding-window "Permanent link")

Whether to disable sliding window. If True, we will disable the sliding window functionality of the model, capping to sliding window size. If the model does not support sliding window, this argument is ignored.

Default: `False`

#### `--disable-cascade-attn`, `--no-disable-cascade-attn`[¶](#-disable-cascade-attn-no-disable-cascade-attn "Permanent link")

Disable cascade attention for V1. While cascade attention does not change the mathematical correctness, disabling it could be useful for preventing potential numerical issues. This defaults to True, so users must opt in to cascade attention by setting this to False. Even when this is set to False, cascade attention will only be used when the heuristic tells that it's beneficial.

Default: `True`

#### `--skip-tokenizer-init`, `--no-skip-tokenizer-init`[¶](#-skip-tokenizer-init-no-skip-tokenizer-init "Permanent link")

Skip initialization of tokenizer and detokenizer. Expects valid `prompt_token_ids` and `None` for prompt from the input. The generated output will contain token ids.

Default: `False`

#### `--enable-prompt-embeds`, `--no-enable-prompt-embeds`[¶](#-enable-prompt-embeds-no-enable-prompt-embeds "Permanent link")

If `True`, enables passing text embeddings as inputs via the `prompt_embeds` key.

WARNING: The vLLM engine may crash if incorrect shape of embeddings is passed. Only enable this flag for trusted users!

Default: `False`

#### `--served-model-name`[¶](#-served-model-name "Permanent link")

The model name(s) used in the API. If multiple names are provided, the server will respond to any of the provided names. The model name in the model field of a response will be the first name in this list. If not specified, the model name will be the same as the `--model` argument. Noted that this name(s) will also be used in `model_name` tag content of prometheus metrics, if multiple names provided, metrics tag will take the first one.

#### `--config-format`[¶](#-config-format "Permanent link")

Possible choices: `auto`, `hf`, `mistral`

The format of the model config to load:

- "auto" will try to load the config in hf format if available after trying to load in mistral format.
- "hf" will load the config in hf format.
- "mistral" will load the config in mistral format.

Default: `auto`

#### `--hf-token`[¶](#-hf-token "Permanent link")

The token to use as HTTP bearer authorization for remote files . If `True`, will use the token generated when running `hf auth login` (stored in `~/.cache/huggingface/token`).

#### `--hf-overrides`[¶](#-hf-overrides "Permanent link")

If a dictionary, contains arguments to be forwarded to the Hugging Face config. If a callable, it is called to update the HuggingFace config.

Default: `{}`

#### `--pooler-config`[¶](#-pooler-config "Permanent link")

Pooler config which controls the behaviour of output pooling in pooling models.

API docs: https://docs.vllm.ai/en/latest/api/vllm/config/#vllm.config.PoolerConfig

Should either be a valid JSON string or JSON keys passed individually.

#### `--generation-config`[¶](#-generation-config "Permanent link")

The folder path to the generation config. Defaults to `"auto"`, the generation config will be loaded from model path. If set to `"vllm"`, no generation config is loaded, vLLM defaults will be used. If set to a folder path, the generation config will be loaded from the specified folder path. If `max_new_tokens` is specified in generation config, then it sets a server-wide limit on the number of output tokens for all requests.

Default: `auto`

#### `--override-generation-config`[¶](#-override-generation-config "Permanent link")

Overrides or sets generation config. e.g. `{"temperature": 0.5}`. If used with `--generation-config auto`, the override parameters will be merged with the default config from the model. If used with `--generation-config vllm`, only the override parameters are used.

Should either be a valid JSON string or JSON keys passed individually.

Default: `{}`

#### `--enable-sleep-mode`, `--no-enable-sleep-mode`[¶](#-enable-sleep-mode-no-enable-sleep-mode "Permanent link")

Enable sleep mode for the engine (only cuda and hip platforms are supported).

Default: `False`

#### `--model-impl`[¶](#-model-impl "Permanent link")

Possible choices: `auto`, `terratorch`, `transformers`, `vllm`

Which implementation of the model to use:

- "auto" will try to use the vLLM implementation, if it exists, and fall back to the Transformers implementation if no vLLM implementation is available.
- "vllm" will use the vLLM model implementation.
- "transformers" will use the Transformers model implementation.
- "terratorch" will use the TerraTorch model implementation.

Default: `auto`

#### `--override-attention-dtype`[¶](#-override-attention-dtype "Permanent link")

Override dtype for attention

#### `--logits-processors`[¶](#-logits-processors "Permanent link")

One or more logits processors' fully-qualified class names or class definitions

#### `--io-processor-plugin`[¶](#-io-processor-plugin "Permanent link")

IOProcessor plugin name to load at model startup

#### `--renderer-num-workers`[¶](#-renderer-num-workers "Permanent link")

Number of worker threads in the renderer thread pool. This pool handles async tokenization, chat template rendering, and multimodal preprocessing.

Default: `1`

### LoadConfig[¶](#loadconfig "Permanent link")

Configuration for loading the model weights.

#### `--load-format`[¶](#-load-format "Permanent link")

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

Default: `auto`

#### `--download-dir`[¶](#-download-dir "Permanent link")

Directory to download and load the weights, default to the default cache directory of Hugging Face.

#### `--safetensors-load-strategy`[¶](#-safetensors-load-strategy "Permanent link")

Specifies the loading strategy for safetensors weights.

- None (default): Uses memory-mapped (lazy) loading. When an NFS filesystem is detected and the total checkpoint size fits within 90%%%% of available RAM, prefetching is enabled automatically.
- "lazy": Weights are memory-mapped from the file. This enables on-demand loading and is highly efficient for models on local storage. Unlike the default (None), auto-prefetch on NFS is not performed.
- "eager": The entire file is read into CPU memory upfront before loading. This is recommended for models on network filesystems (e.g., Lustre, NFS) as it avoids inefficient random reads, significantly speeding up model initialization. However, it uses more CPU RAM.
- "prefetch": Checkpoint files are read into the OS page cache before workers load them, speeding up the model loading phase. Useful on network or high-latency storage.
- "torchao": Weights are loaded in upfront and then reconstructed into torchao tensor subclasses. This is used when the checkpoint was quantized using torchao and saved using safetensors. Needs `torchao >= 0.14.0`.

Extra config for model loader. This will be passed to the model loader corresponding to the chosen load\_format.

Default: `{}`

#### `--ignore-patterns`[¶](#-ignore-patterns "Permanent link")

The list of patterns to ignore when loading the model. Default to "original/\**/*" to avoid repeated loading of llama's checkpoints.

Default: `['original/**/*']`

#### `--use-tqdm-on-load`, `--no-use-tqdm-on-load`[¶](#-use-tqdm-on-load-no-use-tqdm-on-load "Permanent link")

Whether to enable tqdm for showing progress bar when loading model weights.

Default: `True`

#### `--pt-load-map-location`[¶](#-pt-load-map-location "Permanent link")

The map location for loading pytorch checkpoint, to support loading checkpoints can only be loaded on certain devices like "cuda", this is equivalent to `{"": "cuda"}`. Another supported format is mapping from different devices like from GPU 1 to GPU 0: `{"cuda:1": "cuda:0"}`. Note that when passed from command line, the strings in dictionary need to be double quoted for json parsing. For more details, see the original doc for `map_location` parameter in [`torch.load`](https://pytorch.org/docs/stable/generated/torch.load.html#torch.load) parameter.

Default: `cpu`

### AttentionConfig[¶](#attentionconfig "Permanent link")

Configuration for attention mechanisms in vLLM.

#### `--attention-backend`[¶](#-attention-backend "Permanent link")

Attention backend to use. Use "auto" or None for automatic selection.

### MambaConfig[¶](#mambaconfig "Permanent link")

Configuration for Mamba SSM backends.

#### `--mamba-backend`[¶](#-mamba-backend "Permanent link")

Mamba SSU backend to use.

Default: `MambaBackendEnum.TRITON`

#### `--enable-mamba-cache-stochastic-rounding`, `--no-enable-mamba-cache-stochastic-rounding`[¶](#-enable-mamba-cache-stochastic-rounding-no-enable-mamba-cache-stochastic-rounding "Permanent link")

Enable stochastic rounding when writing SSM state to fp16 cache. Uses random bits to unbias the rounding error, which can improve numerical stability for long sequences.

Default: `False`

#### `--mamba-cache-philox-rounds`[¶](#-mamba-cache-philox-rounds "Permanent link")

Number of Philox PRNG rounds for stochastic rounding random number generation. 0 uses the Triton default. Higher values improve randomness quality at the cost of compute.

Default: `0`

### StructuredOutputsConfig[¶](#structuredoutputsconfig "Permanent link")

Dataclass which contains structured outputs config for the engine.

#### `--reasoning-parser`[¶](#-reasoning-parser "Permanent link")

Select the reasoning parser depending on the model that you're using. This is used to parse the reasoning content into OpenAI API format.

Default: `""`

#### `--reasoning-parser-plugin`[¶](#-reasoning-parser-plugin "Permanent link")

Path to a dynamically reasoning parser plugin that can be dynamically loaded and registered.

Default: `""`

### ParallelConfig[¶](#parallelconfig "Permanent link")

Configuration for the distributed execution.

#### `--distributed-executor-backend`[¶](#-distributed-executor-backend "Permanent link")

Possible choices: `external_launcher`, `mp`, `ray`, `uni`

Backend to use for distributed model workers, either "ray" or "mp" (multiprocessing). If the product of pipeline\_parallel\_size and tensor\_parallel\_size is less than or equal to the number of GPUs available, "mp" will be used to keep processing on a single host. Otherwise, an error will be raised. To use "mp" you must also set nnodes, and to use "ray" you must manually set distributed\_executor\_backend to "ray".

Note: [TPU](https://docs.vllm.ai/projects/tpu/en/latest/) platform only supports Ray for distributed inference.

#### `--pipeline-parallel-size`, `-pp`[¶](#-pipeline-parallel-size-pp "Permanent link")

Number of pipeline parallel groups.

Default: `1`

#### `--master-addr`[¶](#-master-addr "Permanent link")

distributed master address for multi-node distributed inference when distributed\_executor\_backend is mp.

Default: `127.0.0.1`

#### `--master-port`[¶](#-master-port "Permanent link")

distributed master port for multi-node distributed inference when distributed\_executor\_backend is mp.

Default: `29501`

#### `--nnodes`, `-n`[¶](#-nnodes-n "Permanent link")

num of nodes for multi-node distributed inference when distributed\_executor\_backend is mp.

Default: `1`

#### `--node-rank`, `-r`[¶](#-node-rank-r "Permanent link")

distributed node rank for multi-node distributed inference when distributed\_executor\_backend is mp.

Default: `0`

#### `--distributed-timeout-seconds`[¶](#-distributed-timeout-seconds "Permanent link")

Timeout in seconds for distributed operations (e.g., init\_process\_group). If set, this value is passed to torch.distributed.init\_process\_group as the timeout parameter. If None, PyTorch's default timeout is used (600s for NCCL). Increase this for multi-node setups where model downloads may be slow.

#### `--numa-bind`, `--no-numa-bind`[¶](#-numa-bind-no-numa-bind "Permanent link")

Enable NUMA binding for GPU worker subprocesses.

Default: `False`

#### `--numa-bind-nodes`[¶](#-numa-bind-nodes "Permanent link")

NUMA node to bind each GPU worker to.

Specify one NUMA node per visible GPU, for example `[0, 0, 1, 1]` for a 4-GPU system with GPUs 0-1 on NUMA node 0 and GPUs 2-3 on NUMA node 1. If unset and `numa_bind=True`, vLLM auto-detects the GPU-to-NUMA topology. The values are passed to `numactl --membind` and `--cpunodebind`, so they must be valid `numactl` NUMA node indices.

#### `--numa-bind-cpus`[¶](#-numa-bind-cpus "Permanent link")

Optional CPU lists to bind each GPU worker to.

Specify one CPU list per visible GPU, for example `["0-3", "4-7", "8-11", "12-15"]`. When set, vLLM uses `numactl --physcpubind` instead of `--cpunodebind`. This is useful for custom policies such as binding to PCT or other high-frequency cores. Each entry must use `numactl --physcpubind` CPU-list syntax, for example `"0-3"` or `"0,2,4-7"`.

#### `--tensor-parallel-size`, `-tp`[¶](#-tensor-parallel-size-tp "Permanent link")

Number of tensor parallel groups.

Default: `1`

#### `--decode-context-parallel-size`, `-dcp`[¶](#-decode-context-parallel-size-dcp "Permanent link")

Number of decode context parallel groups, because the world size does not change by dcp, it simply reuse the GPUs of TP group, and tp\_size needs to be divisible by dcp\_size.

Default: `1`

#### `--dcp-comm-backend`[¶](#-dcp-comm-backend "Permanent link")

Possible choices: `a2a`, `ag_rs`

Communication backend for Decode Context Parallel (DCP). - "ag\_rs": AllGather + ReduceScatter (default, existing behavior) - "a2a": All-to-All exchange of partial outputs + LSE, then combine with Triton kernel. Reduces NCCL calls from 3 to 2 per layer for MLA models.

Default: `ag_rs`

#### `--dcp-kv-cache-interleave-size`[¶](#-dcp-kv-cache-interleave-size "Permanent link")

Interleave size of kv\_cache storage while using DCP. dcp\_kv\_cache\_interleave\_size has been replaced by cp\_kv\_cache\_interleave\_size, and will be deprecated when PCP is fully supported.

Default: `1`

#### `--cp-kv-cache-interleave-size`[¶](#-cp-kv-cache-interleave-size "Permanent link")

Interleave size of kv\_cache storage while using DCP or PCP. For `total_cp_rank = pcp_rank * dcp_world_size + dcp_rank`, and `total_cp_world_size = pcp_world_size * dcp_world_size`. store interleave\_size tokens on total\_cp\_rank i, then store next interleave\_size tokens on total\_cp\_rank i+1. Interleave\_size=1: token-level alignment, where token `i` is stored on total\_cp\_rank `i %% total_cp_world_size`. Interleave\_size=block\_size: block-level alignment, where tokens are first populated to the preceding ranks. Tokens are then stored in (rank i+1, block j) only after (rank i, block j) is fully occupied. Block\_size should be greater than or equal to cp\_kv\_cache\_interleave\_size. Block\_size should be divisible by cp\_kv\_cache\_interleave\_size.

Default: `1`

#### `--prefill-context-parallel-size`, `-pcp`[¶](#-prefill-context-parallel-size-pcp "Permanent link")

Number of prefill context parallel groups.

Default: `1`

#### `--data-parallel-size`, `-dp`[¶](#-data-parallel-size-dp "Permanent link")

Number of data parallel groups. MoE layers will be sharded according to the product of the tensor parallel size and data parallel size.

Default: `1`

#### `--data-parallel-rank`, `-dpn`[¶](#-data-parallel-rank-dpn "Permanent link")

Data parallel rank of this instance. When set, enables external load balancer mode for MoE data-parallel deployments. Unsupported for non-MoE models; launch independent vLLM instances instead.

#### `--data-parallel-start-rank`, `-dpr`[¶](#-data-parallel-start-rank-dpr "Permanent link")

Starting data parallel rank for secondary nodes.

#### `--data-parallel-size-local`, `-dpl`[¶](#-data-parallel-size-local-dpl "Permanent link")

Number of data parallel replicas to run on this node.

#### `--data-parallel-address`, `-dpa`[¶](#-data-parallel-address-dpa "Permanent link")

Address of data parallel cluster head-node.

#### `--data-parallel-rpc-port`, `-dpp`[¶](#-data-parallel-rpc-port-dpp "Permanent link")

Port for data parallel RPC communication.

#### `--data-parallel-backend`, `-dpb`[¶](#-data-parallel-backend-dpb "Permanent link")

Backend for data parallel, either "mp" or "ray".

Default: `mp`

#### `--data-parallel-hybrid-lb`, `--no-data-parallel-hybrid-lb`, `-dph`[¶](#-data-parallel-hybrid-lb-no-data-parallel-hybrid-lb-dph "Permanent link")

Whether to use "hybrid" DP LB mode. Applies only to online serving and when data\_parallel\_size &gt; 0. Enables running an AsyncLLM and API server on a "per-node" basis where vLLM load balances between local data parallel ranks, but an external LB balances between vLLM nodes/replicas. Set explicitly in conjunction with --data-parallel-start-rank.

Default: `False`

#### `--data-parallel-external-lb`, `--no-data-parallel-external-lb`, `-dpe`[¶](#-data-parallel-external-lb-no-data-parallel-external-lb-dpe "Permanent link")

Whether to use "external" DP LB mode. Applies only to online serving and when data\_parallel\_size &gt; 0. This is useful for a "one-pod-per-rank" wide-EP setup in Kubernetes. Supported only for MoE deployments; non-MoE models should use independent vLLM instances without --data-parallel-* arguments. Set implicitly when --data-parallel-rank is provided explicitly to vllm serve.

Default: `False`

#### `--enable-expert-parallel`, `--no-enable-expert-parallel`, `-ep`[¶](#-enable-expert-parallel-no-enable-expert-parallel-ep "Permanent link")

Use expert parallelism instead of tensor parallelism for MoE layers.

Default: `False`

#### `--enable-ep-weight-filter`, `--no-enable-ep-weight-filter`[¶](#-enable-ep-weight-filter-no-enable-ep-weight-filter "Permanent link")

Skip non-local expert weights during model loading when expert parallelism is active. Each rank only reads its own expert shard from disk, which can drastically reduce storage I/O for MoE models with per-expert weight tensors (e.g. DeepSeek, Mixtral, Kimi-K2.5). Has no effect on 3D fused-expert checkpoints (e.g. GPT-OSS) or non-MoE models.

Default: `False`

#### `--all2all-backend`[¶](#-all2all-backend "Permanent link")

Possible choices: `allgather_reducescatter`, `deepep_high_throughput`, `deepep_low_latency`, `flashinfer_all2allv`, `flashinfer_nvlink_one_sided`, `flashinfer_nvlink_two_sided`, `mori`, `naive`, `nixl_ep`, `pplx`

All2All backend for MoE expert parallel communication. Available options:

- "allgather\_reducescatter": All2all based on allgather and reducescatter
- "deepep\_high\_throughput": Use deepep high-throughput kernels
- "deepep\_low\_latency": Use deepep low-latency kernels
- "mori": Use mori kernels
- "nixl\_ep": Use nixl-ep kernels
- "flashinfer\_nvlink\_two\_sided": Use flashinfer two-sided kernels for mnnvl
- "flashinfer\_nvlink\_one\_sided": Use flashinfer high-throughput a2a kernels

Default: `allgather_reducescatter`

#### `--enable-dbo`, `--no-enable-dbo`[¶](#-enable-dbo-no-enable-dbo "Permanent link")

Enable dual batch overlap for the model executor.

Default: `False`

#### `--ubatch-size`[¶](#-ubatch-size "Permanent link")

Number of ubatch size.

Default: `0`

#### `--enable-elastic-ep`, `--no-enable-elastic-ep`[¶](#-enable-elastic-ep-no-enable-elastic-ep "Permanent link")

Enable elastic expert parallelism with stateless NCCL groups for DP/EP.

Default: `False`

#### `--dbo-decode-token-threshold`[¶](#-dbo-decode-token-threshold "Permanent link")

The threshold for dual batch overlap for batches only containing decodes. If the number of tokens in the request is greater than this threshold, microbatching will be used. Otherwise, the request will be processed in a single batch.

Default: `32`

#### `--dbo-prefill-token-threshold`[¶](#-dbo-prefill-token-threshold "Permanent link")

The threshold for dual batch overlap for batches that contain one or more prefills. If the number of tokens in the request is greater than this threshold, microbatching will be used. Otherwise, the request will be processed in a single batch.

Default: `512`

#### `--disable-nccl-for-dp-synchronization`, `--no-disable-nccl-for-dp-synchronization`[¶](#-disable-nccl-for-dp-synchronization-no-disable-nccl-for-dp-synchronization "Permanent link")

Forces the dp synchronization logic in vllm/v1/worker/dp\_utils.py to use Gloo instead of NCCL for its all reduce.

Defaults to True when async scheduling is enabled, False otherwise.

#### `--enable-eplb`, `--no-enable-eplb`[¶](#-enable-eplb-no-enable-eplb "Permanent link")

Enable expert parallelism load balancing for MoE layers.

Default: `False`

#### `--eplb-config`[¶](#-eplb-config "Permanent link")

Expert parallelism configuration.

API docs: https://docs.vllm.ai/en/latest/api/vllm/config/#vllm.config.EPLBConfig

Should either be a valid JSON string or JSON keys passed individually.

Default: `EPLBConfig(window_size=1000, step_interval=3000, num_redundant_experts=0, log_balancedness=False, log_balancedness_interval=1, use_async=False, policy='default', communicator=None)`

#### `--expert-placement-strategy`[¶](#-expert-placement-strategy "Permanent link")

Possible choices: `linear`, `round_robin`

The expert placement strategy for MoE layers:

- "linear": Experts are placed in a contiguous manner. For example, with 4 experts and 2 ranks, rank 0 will have experts \[0, 1] and rank 1 will have experts \[2, 3].
- "round\_robin": Experts are placed in a round-robin manner. For example, with 4 experts and 2 ranks, rank 0 will have experts \[0, 2] and rank 1 will have experts \[1, 3]. This strategy can help improve load balancing for grouped expert models with no redundant experts.

Default: `linear`

#### `--max-parallel-loading-workers`[¶](#-max-parallel-loading-workers "Permanent link")

Maximum number of parallel loading workers when loading model sequentially in multiple batches. To avoid RAM OOM when using tensor parallel and large models.

#### `--ray-workers-use-nsight`, `--no-ray-workers-use-nsight`[¶](#-ray-workers-use-nsight-no-ray-workers-use-nsight "Permanent link")

Whether to profile Ray workers with nsight, see https://docs.ray.io/en/latest/ray-observability/user-guides/profiling.html#profiling-nsight-profiler.

Default: `False`

#### `--disable-custom-all-reduce`, `--no-disable-custom-all-reduce`[¶](#-disable-custom-all-reduce-no-disable-custom-all-reduce "Permanent link")

Disable the custom all-reduce kernel and fall back to NCCL.

Default: `False`

#### `--worker-cls`[¶](#-worker-cls "Permanent link")

The full name of the worker class to use. If "auto", the worker class will be determined based on the platform.

Default: `auto`

#### `--worker-extension-cls`[¶](#-worker-extension-cls "Permanent link")

The full name of the worker extension class to use. The worker extension class is dynamically inherited by the worker class. This is used to inject new attributes and methods to the worker class for use in collective\_rpc calls.

Default: `""`

### CacheConfig[¶](#cacheconfig "Permanent link")

Configuration for the KV cache.

#### `--block-size`[¶](#-block-size "Permanent link")

Size of a contiguous cache block in number of tokens. Accepts None (meaning "use default"). After construction, always int.

#### `--gpu-memory-utilization`[¶](#-gpu-memory-utilization "Permanent link")

The fraction of GPU memory to be used for the model executor, which can range from 0 to 1. For example, a value of 0.5 would imply 50%% GPU memory utilization. If unspecified, will use the default value of 0.92. This is a per-instance limit, and only applies to the current vLLM instance. It does not matter if you have another vLLM instance running on the same GPU. For example, if you have two vLLM instances running on the same GPU, you can set the GPU memory utilization to 0.5 for each instance.

Default: `0.92`

#### `--kv-cache-memory-bytes`[¶](#-kv-cache-memory-bytes "Permanent link")

Size of KV Cache per GPU in bytes. By default, this is set to None and vllm can automatically infer the kv cache size based on gpu\_memory\_utilization. However, users may want to manually specify the kv cache memory size. kv\_cache\_memory\_bytes allows more fine-grain control of how much memory gets used when compared with using gpu\_memory\_utilization. Note that kv\_cache\_memory\_bytes (when not-None) ignores gpu\_memory\_utilization

Parse human-readable integers like '1k', '2M', etc. Including decimal values with decimal multipliers.

```
Examples:
- '1k' -> 1,000
- '1K' -> 1,024
- '25.6k' -> 25,600
```

#### `--kv-cache-dtype`[¶](#-kv-cache-dtype "Permanent link")

Possible choices: `auto`, `bfloat16`, `float16`, `fp8`, `fp8_ds_mla`, `fp8_e4m3`, `fp8_e5m2`, `fp8_inc`, `fp8_per_token_head`, `int8_per_token_head`, `nvfp4`, `turboquant_3bit_nc`, `turboquant_4bit_nc`, `turboquant_k3v4_nc`, `turboquant_k8v4`

Data type for kv cache storage. If "auto", will use model data type. CUDA 11.8+ supports fp8 (=fp8\_e4m3) and fp8\_e5m2. ROCm (AMD GPU) supports fp8 (=fp8\_e4m3). Intel Gaudi (HPU) supports fp8 (using fp8\_inc). Some models (namely DeepSeekV3.2) default to fp8, set to bfloat16 to use bfloat16 instead, this is an invalid option for models that do not default to fp8.

Default: `auto`

#### `--num-gpu-blocks-override`[¶](#-num-gpu-blocks-override "Permanent link")

Number of GPU blocks to use. This overrides the profiled `num_gpu_blocks` if specified. Does nothing if `None`. Used for testing preemption.

#### `--enable-prefix-caching`, `--no-enable-prefix-caching`[¶](#-enable-prefix-caching-no-enable-prefix-caching "Permanent link")

Whether to enable prefix caching.

#### `--prefix-caching-hash-algo`[¶](#-prefix-caching-hash-algo "Permanent link")

Possible choices: `sha256`, `sha256_cbor`, `xxhash`, `xxhash_cbor`

Set the hash algorithm for prefix caching:

- "sha256" uses Pickle for object serialization before hashing. This is the current default, as SHA256 is the most secure choice to avoid potential hash collisions.
- "sha256\_cbor" provides a reproducible, cross-language compatible hash. It serializes objects using canonical CBOR and hashes them with SHA-256.
- "xxhash" uses Pickle serialization with xxHash (128-bit) for faster, non-cryptographic hashing. Requires the optional `xxhash` package. IMPORTANT: Use of a hashing algorithm that is not considered cryptographically secure theoretically increases the risk of hash collisions, which can cause undefined behavior or even leak private information in multi-tenant environments. Even if collisions are still very unlikely, it is important to consider your security risk tolerance against the performance benefits before turning this on.
- "xxhash\_cbor" combines canonical CBOR serialization with xxHash for reproducible hashing. Requires the optional `xxhash` package.

Default: `sha256`

#### `--calculate-kv-scales`, `--no-calculate-kv-scales`[¶](#-calculate-kv-scales-no-calculate-kv-scales "Permanent link")

Deprecated: This option is deprecated and will be removed in v0.19. It enables dynamic calculation of `k_scale` and `v_scale` when kv\_cache\_dtype is fp8. If `False`, the scales will be loaded from the model checkpoint if available. Otherwise, the scales will default to 1.0.

Default: `False`

#### `--kv-cache-dtype-skip-layers`[¶](#-kv-cache-dtype-skip-layers "Permanent link")

Layer patterns to skip KV cache quantization. Accepts layer indices (e.g., '0', '2', '4') or attention type names (e.g., 'sliding\_window').

Default: `[]`

#### `--kv-sharing-fast-prefill`, `--no-kv-sharing-fast-prefill`[¶](#-kv-sharing-fast-prefill-no-kv-sharing-fast-prefill "Permanent link")

This feature is work in progress and no prefill optimization takes place with this flag enabled currently.

In some KV sharing setups, e.g. YOCO (https://arxiv.org/abs/2405.05254), some layers can skip tokens corresponding to prefill. This flag enables attention metadata for eligible layers to be overridden with metadata necessary for implementing this optimization in some models (e.g. Gemma3n)

Default: `False`

#### `--mamba-cache-dtype`[¶](#-mamba-cache-dtype "Permanent link")

Possible choices: `auto`, `float16`, `float32`

The data type to use for the Mamba cache (both the conv as well as the ssm state). If set to 'auto', the data type will be inferred from the model config.

Default: `auto`

#### `--mamba-ssm-cache-dtype`[¶](#-mamba-ssm-cache-dtype "Permanent link")

Possible choices: `auto`, `float16`, `float32`

The data type to use for the Mamba cache (ssm state only, conv state will still be controlled by mamba\_cache\_dtype). If set to 'auto', the data type for the ssm state will be determined by mamba\_cache\_dtype.

Default: `auto`

#### `--mamba-block-size`[¶](#-mamba-block-size "Permanent link")

Size of a contiguous cache block in number of tokens for mamba cache. Can be set only when prefix caching is enabled. Value must be a multiple of 8 to align with causal\_conv1d kernel.

#### `--mamba-cache-mode`[¶](#-mamba-cache-mode "Permanent link")

Possible choices: `align`, `all`, `none`

The cache strategy for Mamba layers. - "none": set when prefix caching is disabled. - "all": cache the mamba state of all tokens at position i * block\_size. This is the default behavior (for models that support it) when prefix caching is enabled. - "align": only cache the mamba state of the last token of each scheduler step and when the token is at position i * block\_size.

Default: `none`

#### `--kv-offloading-size`[¶](#-kv-offloading-size "Permanent link")

Size of the KV cache offloading buffer in GiB. When TP &gt; 1, this is the total buffer size summed across all TP ranks. By default, this is set to None, which means no KV offloading is enabled. When set, vLLM will enable KV cache offloading to CPU using the kv\_offloading\_backend.

#### `--kv-offloading-backend`[¶](#-kv-offloading-backend "Permanent link")

Possible choices: `lmcache`, `native`

The backend to use for KV cache offloading. Supported backends include 'native' (vLLM native CPU offloading), 'lmcache'. KV offloading is only activated when kv\_offloading\_size is set.

Default: `native`

### OffloadConfig[¶](#offloadconfig "Permanent link")

Configuration for model weight offloading to reduce GPU memory usage.

#### `--offload-backend`[¶](#-offload-backend "Permanent link")

Possible choices: `auto`, `prefetch`, `uva`

The backend for weight offloading. Options: - "auto": Selects based on which sub-config has non-default values (prefetch if offload\_group\_size &gt; 0, uva if cpu\_offload\_gb &gt; 0). - "uva": UVA (Unified Virtual Addressing) zero-copy offloading. - "prefetch": Async prefetch with group-based layer offloading.

Default: `auto`

#### `--cpu-offload-gb`[¶](#-cpu-offload-gb "Permanent link")

The space in GiB to offload to CPU, per GPU. Default is 0, which means no offloading. Intuitively, this argument can be seen as a virtual way to increase the GPU memory size. For example, if you have one 24 GB GPU and set this to 10, virtually you can think of it as a 34 GB GPU. Then you can load a 13B model with BF16 weight, which requires at least 26GB GPU memory. Note that this requires fast CPU-GPU interconnect, as part of the model is loaded from CPU memory to GPU memory on the fly in each model forward pass. This uses UVA (Unified Virtual Addressing) for zero-copy access.

Default: `0`

#### `--cpu-offload-params`[¶](#-cpu-offload-params "Permanent link")

The set of parameter name segments to target for CPU offloading. Unmatched parameters are not offloaded. If this set is empty, parameters are offloaded non-selectively until the memory limit defined by `cpu_offload_gb` is reached. Examples: - For parameter name "mlp.experts.w2\_weight": - "experts" or "experts.w2\_weight" will match. - "expert" or "w2" will NOT match (must be exact segments). This allows distinguishing parameters like "w2\_weight" and "w2\_weight\_scale".

Default: `set()`

#### `--offload-group-size`[¶](#-offload-group-size "Permanent link")

Group every N layers together. Offload last `offload_num_in_group` layers of each group. Default is 0 (disabled). Example: group\_size=8, num\_in\_group=2 offloads layers 6,7,14,15,22,23,... Unlike cpu\_offload\_gb, this uses explicit async prefetching to hide transfer latency.

Default: `0`

#### `--offload-num-in-group`[¶](#-offload-num-in-group "Permanent link")

Number of layers to offload per group. Must be &lt;= offload\_group\_size. Default is 1.

Default: `1`

#### `--offload-prefetch-step`[¶](#-offload-prefetch-step "Permanent link")

Number of layers to prefetch ahead. Higher values hide more latency but use more GPU memory. Default is 1.

Default: `1`

#### `--offload-params`[¶](#-offload-params "Permanent link")

The set of parameter name segments to target for prefetch offloading. Unmatched parameters are not offloaded. If this set is empty, ALL parameters of each offloaded layer are offloaded. Uses segment matching: "w13\_weight" matches "mlp.experts.w13\_weight" but not "mlp.experts.w13\_weight\_scale".

Default: `set()`

### MultiModalConfig[¶](#multimodalconfig "Permanent link")

Controls the behavior of multimodal models.

#### `--language-model-only`, `--no-language-model-only`[¶](#-language-model-only-no-language-model-only "Permanent link")

If True, disables all multimodal inputs by setting all modality limits to 0. Equivalent to setting `--limit-mm-per-prompt` to 0 for every modality.

Default: `False`

#### `--limit-mm-per-prompt`[¶](#-limit-mm-per-prompt "Permanent link")

The maximum number of input items and options allowed per prompt for each modality.

Defaults to 999 for each modality.

Legacy format (count only):

Configurable format (with options): {"video": {"count": 1, "num\_frames": 32, "width": 512, "height": 512}, "image": {"count": 5, "width": 512, "height": 512}}

Mixed format (combining both): {"image": 16, "video": {"count": 1, "num\_frames": 32, "width": 512, "height": 512}}

Should either be a valid JSON string or JSON keys passed individually.

Default: `{}`

#### `--enable-mm-embeds`, `--no-enable-mm-embeds`[¶](#-enable-mm-embeds-no-enable-mm-embeds "Permanent link")

If `True`, enables passing multimodal embeddings: for `LLM` class, this refers to tensor inputs under `multi_modal_data`; for the OpenAI-compatible server, this refers to chat messages with content `"type": "*_embeds"`.

When enabled with `--limit-mm-per-prompt` set to 0 for a modality, precomputed embeddings skip count validation for that modality, saving memory by not loading encoder modules while still enabling embeddings as an input. Limits greater than 0 still apply to embeddings.

WARNING: The vLLM engine may crash if incorrect shape of embeddings is passed. Only enable this flag for trusted users!

Default: `False`

#### `--media-io-kwargs`[¶](#-media-io-kwargs "Permanent link")

Additional args passed to process media inputs, keyed by modalities. For example, to set num\_frames for video, set `--media-io-kwargs '{"video": {"num_frames": 40} }'`

Should either be a valid JSON string or JSON keys passed individually.

Default: `{}`

#### `--mm-processor-kwargs`[¶](#-mm-processor-kwargs "Permanent link")

Arguments to be forwarded to the model's processor for multi-modal data, e.g., image processor. Overrides for the multi-modal processor obtained from `transformers.AutoProcessor.from_pretrained`.

The available overrides depend on the model that is being run.

For example, for Phi-3-Vision: `{"num_crops": 4}`.

Should either be a valid JSON string or JSON keys passed individually.

#### `--mm-processor-cache-gb`[¶](#-mm-processor-cache-gb "Permanent link")

The size (in GiB) of the multi-modal processor cache, which is used to avoid re-processing past multi-modal inputs.

This cache is duplicated for each API process and engine core process, resulting in a total memory usage of `mm_processor_cache_gb * (api_server_count + data_parallel_size)`.

Set to `0` to disable this cache completely (not recommended).

Default: `4`

#### `--mm-processor-cache-type`[¶](#-mm-processor-cache-type "Permanent link")

Possible choices: `lru`, `shm`

Type of cache to use for the multi-modal preprocessor/mapper. If `shm`, use shared memory FIFO cache. If `lru`, use mirrored LRU cache.

Default: `lru`

#### `--mm-shm-cache-max-object-size-mb`[¶](#-mm-shm-cache-max-object-size-mb "Permanent link")

Size limit (in MiB) for each object stored in the multi-modal processor shared memory cache. Only effective when `mm_processor_cache_type` is `"shm"`.

Default: `128`

#### `--mm-encoder-only`, `--no-mm-encoder-only`[¶](#-mm-encoder-only-no-mm-encoder-only "Permanent link")

When enabled, skips the language component of the model.

This is usually only valid in disaggregated Encoder process.

Default: `False`

#### `--mm-encoder-tp-mode`[¶](#-mm-encoder-tp-mode "Permanent link")

Possible choices: `data`, `weights`

Indicates how to optimize multi-modal encoder inference using tensor parallelism (TP).

- `"weights"`: Within the same vLLM engine, split the weights of each layer across TP ranks. (default TP behavior)
- `"data"`: Within the same vLLM engine, split the batched input data across TP ranks to process the data in parallel, while hosting the full weights on each TP rank. This batch-level DP is not to be confused with API request-level DP (which is controlled by `--data-parallel-size`). This is only supported on a per-model basis and falls back to `"weights"` if the encoder does not support DP.

Default: `weights`

#### `--mm-encoder-attn-backend`[¶](#-mm-encoder-attn-backend "Permanent link")

Optional override for the multi-modal encoder attention backend when using vision transformers. Accepts any value from `vllm.v1.attention.backends.registry.AttentionBackendEnum` (e.g. `FLASH_ATTN`).

#### `--mm-encoder-attn-dtype`[¶](#-mm-encoder-attn-dtype "Permanent link")

Possible choices: `fp8`, `None`

Optional dtype override for ViT encoder attention. Set to `"fp8"` to enable FP8 quantization via the FlashInfer cuDNN backend. When set to `"fp8"` without a scale file, dynamic scaling is used automatically. See docs/features/quantization/fp8\_vit\_attn.md for details.

#### `--mm-encoder-fp8-scale-path`[¶](#-mm-encoder-fp8-scale-path "Permanent link")

Path to a JSON file containing per-layer FP8 Q/K/V scales for ViT encoder attention. When provided (with `mm_encoder_attn_dtype="fp8"`), static scaling is used. When omitted, dynamic scaling is used.

#### `--mm-encoder-fp8-scale-save-path`[¶](#-mm-encoder-fp8-scale-save-path "Permanent link")

When set with dynamic FP8 scaling (`mm_encoder_attn_dtype="fp8"` and no `mm_encoder_fp8_scale_path`), saves the calibrated scales to this file after the amax history buffer is full. The saved file can then be used as `mm_encoder_fp8_scale_path` in subsequent runs.

#### `--mm-encoder-fp8-scale-save-margin`[¶](#-mm-encoder-fp8-scale-save-margin "Permanent link")

Safety margin multiplied onto scales when auto-saving. A value &gt; 1 leaves headroom so that inputs with larger activations than the calibration set do not overflow FP8 range. Default 1.5.

Default: `1.5`

#### `--interleave-mm-strings`, `--no-interleave-mm-strings`[¶](#-interleave-mm-strings-no-interleave-mm-strings "Permanent link")

Enable fully interleaved support for multimodal prompts, while using --chat-template-content-format=string.

Default: `False`

#### `--skip-mm-profiling`, `--no-skip-mm-profiling`[¶](#-skip-mm-profiling-no-skip-mm-profiling "Permanent link")

When enabled, skips multimodal memory profiling and only profiles with language backbone model during engine initialization.

This reduces engine startup time but shifts the responsibility to users for estimating the peak memory usage of the activation of multimodal encoder and embedding cache.

Default: `False`

#### `--video-pruning-rate`[¶](#-video-pruning-rate "Permanent link")

Sets pruning rate for video pruning via Efficient Video Sampling. Value sits in range [0;1) and determines fraction of media tokens from each video to be pruned.

#### `--mm-tensor-ipc`[¶](#-mm-tensor-ipc "Permanent link")

Possible choices: `direct_rpc`, `torch_shm`

IPC (inter-process communication) method for multimodal tensors. - "direct\_rpc": Use msgspec serialization via RPC - "torch\_shm": Use torch.multiprocessing shared memory for zero-copy IPC Defaults to "direct\_rpc".

Default: `direct_rpc`

### LoRAConfig[¶](#loraconfig "Permanent link")

Configuration for LoRA.

#### `--enable-lora`, `--no-enable-lora`[¶](#-enable-lora-no-enable-lora "Permanent link")

If True, enable handling of LoRA adapters.

#### `--max-loras`[¶](#-max-loras "Permanent link")

Max number of LoRAs in a single batch.

Default: `1`

#### `--max-lora-rank`[¶](#-max-lora-rank "Permanent link")

Possible choices: `1`, `8`, `16`, `32`, `64`, `128`, `256`, `320`, `512`

Max LoRA rank.

Default: `16`

#### `--lora-dtype`[¶](#-lora-dtype "Permanent link")

Data type for LoRA. If auto, will default to base model dtype.

Default: `auto`

#### `--enable-tower-connector-lora`, `--no-enable-tower-connector-lora`[¶](#-enable-tower-connector-lora-no-enable-tower-connector-lora "Permanent link")

If `True`, LoRA support for the tower (vision encoder) and connector of multimodal models will be enabled. This is an experimental feature and currently only supports some MM models such as the Qwen VL series. The default is False.

Default: `False`

#### `--max-cpu-loras`[¶](#-max-cpu-loras "Permanent link")

Maximum number of LoRAs to store in CPU memory. Must be &gt;= than `max_loras`.

#### `--fully-sharded-loras`, `--no-fully-sharded-loras`[¶](#-fully-sharded-loras-no-fully-sharded-loras "Permanent link")

By default, only half of the LoRA computation is sharded with tensor parallelism. Enabling this will use the fully sharded layers. At high sequence length, max rank or tensor parallel size, this is likely faster.

Default: `False`

#### `--lora-target-modules`[¶](#-lora-target-modules "Permanent link")

Restrict LoRA to specific module suffixes (e.g., \["o\_proj", "qkv\_proj"]). If None, all supported LoRA modules are used. This allows deployment-time control over which modules have LoRA applied, useful for performance tuning.

#### `--default-mm-loras`[¶](#-default-mm-loras "Permanent link")

Dictionary mapping specific modalities to LoRA model paths; this field is only applicable to multimodal models and should be leveraged when a model always expects a LoRA to be active when a given modality is present. Note that currently, if a request provides multiple additional modalities, each of which have their own LoRA, we do NOT apply default\_mm\_loras because we currently only support one lora adapter per prompt. When run in offline mode, the lora IDs for n modalities will be automatically assigned to 1-n with the names of the modalities in alphabetic order.

Should either be a valid JSON string or JSON keys passed individually.

#### `--specialize-active-lora`, `--no-specialize-active-lora`[¶](#-specialize-active-lora-no-specialize-active-lora "Permanent link")

Whether to construct lora kernel grid by the number of active LoRA adapters. When set to True, separate cuda graphs will be captured for different counts of active LoRAs (powers of 2 up to max\_loras), which can improve performance for variable LoRA usage patterns at the cost of increased startup time and memory usage. Only takes effect when cudagraph\_specialize\_lora is True.

Default: `False`

### ObservabilityConfig[¶](#observabilityconfig "Permanent link")

Configuration for observability - metrics and tracing.

#### `--show-hidden-metrics-for-version`[¶](#-show-hidden-metrics-for-version "Permanent link")

Enable deprecated Prometheus metrics that have been hidden since the specified version. For example, if a previously deprecated metric has been hidden since the v0.7.0 release, you use `--show-hidden-metrics-for-version=0.7` as a temporary escape hatch while you migrate to new metrics. The metric is likely to be removed completely in an upcoming release.

#### `--otlp-traces-endpoint`[¶](#-otlp-traces-endpoint "Permanent link")

Target URL to which OpenTelemetry traces will be sent.

#### `--collect-detailed-traces`[¶](#-collect-detailed-traces "Permanent link")

Possible choices: `all`, `model`, `worker`, `None`, `model,worker`, `model,all`, `worker,model`, `worker,all`, `all,model`, `all,worker`

It makes sense to set this only if `--otlp-traces-endpoint` is set. If set, it will collect detailed traces for the specified modules. This involves use of possibly costly and or blocking operations and hence might have a performance impact.

Note that collecting detailed timing information for each request can be expensive.

#### `--kv-cache-metrics`, `--no-kv-cache-metrics`[¶](#-kv-cache-metrics-no-kv-cache-metrics "Permanent link")

Enable KV cache residency metrics (lifetime, idle time, reuse gaps). Uses sampling to minimize overhead. Requires log stats to be enabled (i.e., --disable-log-stats not set).

Default: `False`

#### `--kv-cache-metrics-sample`[¶](#-kv-cache-metrics-sample "Permanent link")

Sampling rate for KV cache metrics (0.0, 1.0]. Default 0.01 = 1%% of blocks.

Default: `0.01`

#### `--cudagraph-metrics`, `--no-cudagraph-metrics`[¶](#-cudagraph-metrics-no-cudagraph-metrics "Permanent link")

Enable CUDA graph metrics (number of padded/unpadded tokens, runtime cudagraph dispatch modes, and their observed frequencies at every logging interval).

Default: `False`

#### `--enable-layerwise-nvtx-tracing`, `--no-enable-layerwise-nvtx-tracing`[¶](#-enable-layerwise-nvtx-tracing-no-enable-layerwise-nvtx-tracing "Permanent link")

Enable layerwise NVTX tracing. This traces the execution of each layer or module in the model and attach information such as input/output shapes to nvtx range markers. Noted that this doesn't work with CUDA graphs enabled.

Default: `False`

#### `--enable-mfu-metrics`, `--no-enable-mfu-metrics`[¶](#-enable-mfu-metrics-no-enable-mfu-metrics "Permanent link")

Enable Model FLOPs Utilization (MFU) metrics.

Default: `False`

#### `--enable-logging-iteration-details`, `--no-enable-logging-iteration-details`[¶](#-enable-logging-iteration-details-no-enable-logging-iteration-details "Permanent link")

Enable detailed logging of iteration details. If set, vllm EngineCore will log iteration details This includes number of context/generation requests and tokens and the elapsed cpu time for the iteration.

Default: `False`

### SchedulerConfig[¶](#schedulerconfig "Permanent link")

Scheduler configuration.

#### `--max-num-batched-tokens`[¶](#-max-num-batched-tokens "Permanent link")

Maximum number of tokens that can be processed in a single iteration.

The default value here is mainly for convenience when testing. In real usage, this should be set in `EngineArgs.create_engine_config`.

Parse human-readable integers like '1k', '2M', etc. Including decimal values with decimal multipliers.

```
Examples:
- '1k' -> 1,000
- '1K' -> 1,024
- '25.6k' -> 25,600
```

#### `--max-num-seqs`[¶](#-max-num-seqs "Permanent link")

Maximum number of sequences to be processed in a single iteration.

The default value here is mainly for convenience when testing. In real usage, this should be set in `EngineArgs.create_engine_config`.

#### `--max-num-partial-prefills`[¶](#-max-num-partial-prefills "Permanent link")

For chunked prefill, the maximum number of sequences that can be partially prefilled concurrently.

Default: `1`

#### `--max-long-partial-prefills`[¶](#-max-long-partial-prefills "Permanent link")

For chunked prefill, the maximum number of prompts longer than long\_prefill\_token\_threshold that will be prefilled concurrently. Setting this less than max\_num\_partial\_prefills will allow shorter prompts to jump the queue in front of longer prompts in some cases, improving latency.

Default: `1`

#### `--long-prefill-token-threshold`[¶](#-long-prefill-token-threshold "Permanent link")

For chunked prefill, a request is considered long if the prompt is longer than this number of tokens.

Default: `0`

#### `--scheduling-policy`[¶](#-scheduling-policy "Permanent link")

Possible choices: `fcfs`, `priority`

The scheduling policy to use:

- "fcfs" means first come first served, i.e. requests are handled in order of arrival.
- "priority" means requests are handled based on given priority (lower value means earlier handling) and time of arrival deciding any ties).

Default: `fcfs`

#### `--enable-chunked-prefill`, `--no-enable-chunked-prefill`[¶](#-enable-chunked-prefill-no-enable-chunked-prefill "Permanent link")

If True, prefill requests can be chunked based on the remaining `max_num_batched_tokens`.

The default value here is mainly for convenience when testing. In real usage, this should be set in `EngineArgs.create_engine_config`.

#### `--disable-chunked-mm-input`, `--no-disable-chunked-mm-input`[¶](#-disable-chunked-mm-input-no-disable-chunked-mm-input "Permanent link")

If set to true and chunked prefill is enabled, we do not want to partially schedule a multimodal item. Only used in V1 This ensures that if a request has a mixed prompt (like text tokens TTTT followed by image tokens IIIIIIIIII) where only some image tokens can be scheduled (like TTTTIIIII, leaving IIIII), it will be scheduled as TTTT in one step and IIIIIIIIII in the next.

Default: `False`

#### `--scheduler-cls`[¶](#-scheduler-cls "Permanent link")

The scheduler class to use. "vllm.v1.core.sched.scheduler.Scheduler" is the default scheduler. Can be a class directly or the path to a class of form "mod.custom\_class".

#### `--scheduler-reserve-full-isl`, `--no-scheduler-reserve-full-isl`[¶](#-scheduler-reserve-full-isl-no-scheduler-reserve-full-isl "Permanent link")

If True, the scheduler checks whether the full input sequence length fits in the KV cache before admitting a new request, rather than only checking the first chunk. Prevents over-admission and KV cache thrashing with chunked prefill.

Default: `True`

#### `--disable-hybrid-kv-cache-manager`, `--no-disable-hybrid-kv-cache-manager`[¶](#-disable-hybrid-kv-cache-manager-no-disable-hybrid-kv-cache-manager "Permanent link")

If set to True, KV cache manager will allocate the same size of KV cache for all attention layers even if there are multiple type of attention layers like full attention and sliding window attention. If set to None, the default value will be determined based on the environment and starting configuration.

#### `--async-scheduling`, `--no-async-scheduling`[¶](#-async-scheduling-no-async-scheduling "Permanent link")

If set to False, disable async scheduling. Async scheduling helps to avoid gaps in GPU utilization, leading to better latency and throughput.

#### `--stream-interval`[¶](#-stream-interval "Permanent link")

The interval (or buffer size) for streaming in terms of token length. A smaller value (1) makes streaming smoother by sending each token immediately, while a larger value (e.g., 10) reduces host overhead and may increase throughput by batching multiple tokens before sending.

Default: `1`

### CompilationConfig[¶](#compilationconfig "Permanent link")

Configuration for compilation.

```
You must pass CompilationConfig to VLLMConfig constructor.
VLLMConfig's post_init does further initialization. If used outside of the
VLLMConfig, some fields will be left in an improper state.

It contains PassConfig, which controls the custom fusion/transformation passes.
The rest has three parts:

- Top-level Compilation control:
    - [`mode`][vllm.config.CompilationConfig.mode]
    - [`debug_dump_path`][vllm.config.CompilationConfig.debug_dump_path]
    - [`cache_dir`][vllm.config.CompilationConfig.cache_dir]
    - [`backend`][vllm.config.CompilationConfig.backend]
    - [`custom_ops`][vllm.config.CompilationConfig.custom_ops]
    - [`splitting_ops`][vllm.config.CompilationConfig.splitting_ops]
    - [`compile_mm_encoder`][vllm.config.CompilationConfig.compile_mm_encoder]
- CudaGraph capture:
    - [`cudagraph_mode`][vllm.config.CompilationConfig.cudagraph_mode]
    - [`cudagraph_capture_sizes`]
    [vllm.config.CompilationConfig.cudagraph_capture_sizes]
    - [`max_cudagraph_capture_size`]
    [vllm.config.CompilationConfig.max_cudagraph_capture_size]
    - [`cudagraph_num_of_warmups`]
    [vllm.config.CompilationConfig.cudagraph_num_of_warmups]
    - [`cudagraph_copy_inputs`]
    [vllm.config.CompilationConfig.cudagraph_copy_inputs]
- Inductor compilation:
    - [`compile_sizes`][vllm.config.CompilationConfig.compile_sizes]
    - [`compile_ranges_endpoints`]
        [vllm.config.CompilationConfig.compile_ranges_endpoints]
    - [`inductor_compile_config`]
    [vllm.config.CompilationConfig.inductor_compile_config]
    - [`inductor_passes`][vllm.config.CompilationConfig.inductor_passes]
    - custom inductor passes

Why we have different sizes for cudagraph and inductor:
- cudagraph: a cudagraph captured for a specific size can only be used
    for the same size. We need to capture all the sizes we want to use.
- inductor: a graph compiled by inductor for a general shape can be used
    for different sizes. Inductor can also compile for specific sizes,
    where it can have more information to optimize the graph with fully
    static shapes. However, we find the general shape compilation is
    sufficient for most cases. It might be beneficial to compile for
    certain small batchsizes, where inductor is good at optimizing.
```

#### `--cudagraph-capture-sizes`[¶](#-cudagraph-capture-sizes "Permanent link")

Sizes to capture cudagraph. - None (default): capture sizes are inferred from vllm config. - list\[int]: capture sizes are specified as given.

#### `--max-cudagraph-capture-size`[¶](#-max-cudagraph-capture-size "Permanent link")

The maximum cudagraph capture size.

If cudagraph\_capture\_sizes is specified, this will be set to the largest size in that list (or checked for consistency if specified). If cudagraph\_capture\_sizes is not specified, the list of sizes is generated automatically following the pattern:

```
[1, 2, 4] + list(range(8, 256, 8)) + list(
range(256, max_cudagraph_capture_size + 1, 16))
```

If not specified, max\_cudagraph\_capture\_size is set to min(max\_num\_seqs\*2, 512) by default. This voids OOM in tight memory scenarios with small max\_num\_seqs, and prevents capture of many large graphs (&gt;512) that would greatly increase startup time with limited performance benefit.

### KernelConfig[¶](#kernelconfig "Permanent link")

Configuration for kernel selection and warmup behavior.

#### `--ir-op-priority`[¶](#-ir-op-priority "Permanent link")

vLLM IR op priority for dispatching/lowering during the forward pass. Platform defaults appended automatically during VllmConfig.**post\_init**.

API docs: https://docs.vllm.ai/en/latest/api/vllm/config/#vllm.config.IrOpPriorityConfig

Should either be a valid JSON string or JSON keys passed individually.

Default: `IrOpPriorityConfig(rms_norm=[], fused_add_rms_norm=[])`

#### `--enable-flashinfer-autotune`, `--no-enable-flashinfer-autotune`[¶](#-enable-flashinfer-autotune-no-enable-flashinfer-autotune "Permanent link")

If True, run FlashInfer autotuning during kernel warmup.

#### `--moe-backend`[¶](#-moe-backend "Permanent link")

Possible choices: `aiter`, `auto`, `cutlass`, `deep_gemm`, `deep_gemm_mega_moe`, `emulation`, `flashinfer_cutedsl`, `flashinfer_cutlass`, `flashinfer_trtllm`, `humming`, `marlin`, `triton`, `triton_unfused`

Backend for MoE expert computation kernels. Available options:

- "auto": Automatically select the best backend based on model and hardware
- "triton": Use Triton-based fused MoE kernels
- "deep\_gemm": Use DeepGEMM kernels (FP8 block-quantized only)
- "deep\_gemm\_mega\_moe": Use DeepGEMM mega MoE kernels
- "cutlass": Use vLLM CUTLASS kernels
- "flashinfer\_trtllm": Use FlashInfer with TRTLLM-GEN kernels
- "flashinfer\_cutlass": Use FlashInfer with CUTLASS kernels
- "flashinfer\_cutedsl": Use FlashInfer with CuteDSL kernels (FP4 only)
- "marlin": Use Marlin kernels (weight-only quantization)
- "humming": Use Humming Mixed Precision kernels
- "triton\_unfused": Use Triton unfused MoE kernels
- "aiter": Use AMD AITer kernels (ROCm only)
- "emulation": use BF16/FP16 GEMM, dequantizing weights and running QDQ on activations.

Default: `auto`

### VllmConfig[¶](#vllmconfig "Permanent link")

Dataclass which contains all vllm-related configuration. This simplifies passing around the distinct configurations in the codebase.

#### `--speculative-config`, `-sc`[¶](#-speculative-config-sc "Permanent link")

Speculative decoding configuration.

API docs: https://docs.vllm.ai/en/latest/api/vllm/config/#vllm.config.SpeculativeConfig

Should either be a valid JSON string or JSON keys passed individually.

#### `--kv-transfer-config`[¶](#-kv-transfer-config "Permanent link")

The configurations for distributed KV cache transfer.

API docs: https://docs.vllm.ai/en/latest/api/vllm/config/#vllm.config.KVTransferConfig

Should either be a valid JSON string or JSON keys passed individually.

#### `--kv-events-config`[¶](#-kv-events-config "Permanent link")

The configurations for event publishing.

API docs: https://docs.vllm.ai/en/latest/api/vllm/config/#vllm.config.KVEventsConfig

Should either be a valid JSON string or JSON keys passed individually.

#### `--ec-transfer-config`[¶](#-ec-transfer-config "Permanent link")

The configurations for distributed EC cache transfer.

API docs: https://docs.vllm.ai/en/latest/api/vllm/config/#vllm.config.ECTransferConfig

Should either be a valid JSON string or JSON keys passed individually.

#### `--compilation-config`, `-cc`[¶](#-compilation-config-cc "Permanent link")

`torch.compile` and cudagraph capture configuration for the model.

As a shorthand, one can append compilation arguments via -cc.parameter=argument such as `-cc.mode=3` (same as `-cc='{"mode":3}'`).

You can specify the full compilation config like so: `{"mode": 3, "cudagraph_capture_sizes": [1, 2, 4, 8]}`

API docs: https://docs.vllm.ai/en/latest/api/vllm/config/#vllm.config.CompilationConfig

Should either be a valid JSON string or JSON keys passed individually.

Default: `{'mode': None, 'debug_dump_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend': 'inductor', 'custom_ops': [], 'ir_enable_torch_wrap': None, 'splitting_ops': None, 'compile_mm_encoder': False, 'cudagraph_mm_encoder': False, 'encoder_cudagraph_token_budgets': [], 'encoder_cudagraph_max_vision_items_per_batch': 0, 'encoder_cudagraph_max_frames_per_batch': None, 'compile_sizes': None, 'compile_ranges_endpoints': None, 'inductor_compile_config': {'enable_auto_functionalized_v2': False, 'combo_kernels': True, 'benchmark_combo_kernel': True}, 'inductor_passes': {}, 'cudagraph_mode': None, 'cudagraph_num_of_warmups': 0, 'cudagraph_capture_sizes': None, 'cudagraph_copy_inputs': False, 'cudagraph_specialize_lora': True, 'use_inductor_graph_partition': None, 'pass_config': {}, 'max_cudagraph_capture_size': None, 'dynamic_shapes_config': {'type': <DynamicShapesType.BACKED: 'backed'>, 'evaluate_guards': False, 'assume_32_bit_indexing': False}, 'local_cache_dir': None, 'fast_moe_cold_start': None, 'static_all_moe_layers': []}`

#### `--attention-config`, `-ac`[¶](#-attention-config-ac "Permanent link")

Attention configuration.

API docs: https://docs.vllm.ai/en/latest/api/vllm/config/#vllm.config.AttentionConfig

Should either be a valid JSON string or JSON keys passed individually.

Default: `AttentionConfig(backend=None, flash_attn_version=None, use_prefill_decode_attention=False, flash_attn_max_num_splits_for_cuda_graph=32, tq_max_kv_splits_for_cuda_graph=32, use_cudnn_prefill=False, use_trtllm_ragged_deepseek_prefill=False, use_trtllm_attention=None, disable_flashinfer_prefill=None, disable_flashinfer_q_quantization=False, mla_prefill_backend=None, use_prefill_query_quantization=False, use_fp4_indexer_cache=False, use_non_causal=False)`

#### `--reasoning-config`[¶](#-reasoning-config "Permanent link")

The configurations for reasoning model.

API docs: https://docs.vllm.ai/en/latest/api/vllm/config/#vllm.config.ReasoningConfig

Should either be a valid JSON string or JSON keys passed individually.

#### `--kernel-config`[¶](#-kernel-config "Permanent link")

Kernel configuration.

API docs: https://docs.vllm.ai/en/latest/api/vllm/config/#vllm.config.KernelConfig

Should either be a valid JSON string or JSON keys passed individually.

Default: `KernelConfig(ir_op_priority=IrOpPriorityConfig(rms_norm=[], fused_add_rms_norm=[]), enable_flashinfer_autotune=None, moe_backend='auto')`

#### `--additional-config`[¶](#-additional-config "Permanent link")

Additional config for specified platform. Different platforms may support different configs. Make sure the configs are valid for the platform you are using. Contents must be hashable.

Default: `{}`

#### `--structured-outputs-config`[¶](#-structured-outputs-config "Permanent link")

Structured outputs configuration.

API docs: https://docs.vllm.ai/en/latest/api/vllm/config/#vllm.config.StructuredOutputsConfig

Should either be a valid JSON string or JSON keys passed individually.

Default: `StructuredOutputsConfig(backend='auto', disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_plugin='', enable_in_reasoning=False)`

#### `--profiler-config`[¶](#-profiler-config "Permanent link")

Profiling configuration.

API docs: https://docs.vllm.ai/en/latest/api/vllm/config/#vllm.config.ProfilerConfig

Should either be a valid JSON string or JSON keys passed individually.

Default: `ProfilerConfig(profiler=None, torch_profiler_dir='', torch_profiler_with_stack=True, torch_profiler_with_flops=False, torch_profiler_use_gzip=True, torch_profiler_dump_cuda_time_total=True, torch_profiler_record_shapes=False, torch_profiler_with_memory=False, ignore_frontend=False, delay_iterations=0, max_iterations=0, warmup_iterations=0, active_iterations=5, wait_iterations=0)`

#### `--optimization-level`[¶](#-optimization-level "Permanent link")

The optimization level. These levels trade startup time cost for performance, with -O0 having the best startup time and -O3 having the best performance. -O2 is used by default. See OptimizationLevel for full description.

Default: `2`

#### `--performance-mode`[¶](#-performance-mode "Permanent link")

Possible choices: `balanced`, `interactivity`, `throughput`

Performance mode for runtime behavior, 'balanced' is the default. 'interactivity' favors low end-to-end per-request latency at small batch sizes (fine-grained CUDA graphs, latency-oriented kernels). 'throughput' favors aggregate tokens/sec at high concurrency (larger CUDA graphs, more aggressive batching, throughput-oriented kernels).

Default: `balanced`

#### `--weight-transfer-config`[¶](#-weight-transfer-config "Permanent link")

The configurations for weight transfer during RL training.

API docs: https://docs.vllm.ai/en/latest/api/vllm/config/#vllm.config.WeightTransferConfig

Should either be a valid JSON string or JSON keys passed individually.