---
title: Support Features on Ascend NPU - SGLang Documentation
url: https://docs.sglang.io/docs/hardware-platforms/ascend-npus/ascend_npu_support_features
source: sitemap
fetched_at: 2026-05-11T05:48:33.448476646-03:00
rendered_js: false
word_count: 1362
summary: This document provides a comprehensive reference list of server arguments and configuration parameters available for the sglang framework, categorized by functionality such as model loading, networking, memory management, and logging.
tags:
    - sglang
    - server-configuration
    - command-line-arguments
    - llm-serving
    - performance-tuning
    - npu-optimization
category: reference
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

This section describes the basic functions and features supported by the Ascend NPU.If you encounter issues or have any questions, please [open an issue](https://github.com/sgl-project/sglang/issues). If you want to know the meaning and usage of each parameter, click [Server Arguments](https://docs.sglang.io/docs/advanced_features/server_arguments).

## Model and tokenizer

ArgumentDefaultsOptionsServer supported`--model-path`  
`--model``None`Type: strA2, A3`--tokenizer-path``None`Type: strA2, A3`--tokenizer-mode``auto``auto`, `slow`A2, A3`--tokenizer-worker-num``1`Type: intA2, A3`--skip-tokenizer-init``False`bool flag (set to enable)A2, A3`--load-format``auto``auto`, `safetensors`, `gguf`A2, A3`--model-loader-`  
`extra-config`Type: strA2, A3`--trust-remote-code``False`bool flag (set to enable)A2, A3`--context-length``None`Type: intA2, A3`--is-embedding``False`bool flag (set to enable)A2, A3`--enable-multimodal``None`bool flag (set to enable)A2, A3`--revision``None`Type: strA2, A3`--model-impl``auto``auto`, `sglang`,&lt;br/&gt; `transformers`A2, A3

## HTTP server

ArgumentDefaultsOptionsServer supported`--host``127.0.0.1`Type: strA2, A3`--port``30000`Type: intA2, A3`--skip-server-warmup``False`bool flag (set to enable)A2, A3`--warmups``None`Type: strA2, A3`--nccl-port``None`Type: intA2, A3`--fastapi-root-path``None`Type: strA2, A3`--grpc-mode``False``False`Planned

## SSL/TLS

ArgumentDefaultsOptionsServer supported`--ssl-keyfile``None`Type: strA2, A3`--ssl-certfile``None`Type: strA2, A3`--ssl-keyfile-password``None`Type: strA2, A3`--enable-ssl-refresh``False`bool flag  
(set to enable)A2, A3`--enable-http2``False`bool flag  
(set to enable)A2, A3

## Quantization and data type

ArgumentDefaultsOptionsServer supported`--dtype``auto``auto`,&lt;br/&gt; `float16`,&lt;br/&gt; `bfloat16`A2, A3`--quantization``None``modelslim`A2, A3`--quantization-param-path``None`Type: strSpecial For GPU`--kv-cache-dtype``auto``auto`A2, A3`--enable-fp32-lm-head``False`bool flag  
(set to enable)A2, A3`--modelopt-quant``None`Type: strSpecial For GPU`--modelopt-checkpoint-`  
`restore-path``None`Type: strSpecial For GPU`--modelopt-checkpoint-`  
`save-path``None`Type: strSpecial For GPU`--modelopt-export-path``None`Type: strSpecial For GPU`--quantize-and-serve``False`bool flag  
(set to enable)Special For GPU`--rl-quant-profile``None`Type: strSpecial For GPU

## Memory and scheduling

ArgumentDefaultsOptionsServer supported`--mem-fraction-static``None`Type: floatA2, A3`--max-running-requests``None`Type: intA2, A3`--prefill-max-requests``None`Type: intA2, A3`--max-queued-requests``None`Type: intA2, A3`--max-total-tokens``None`Type: intA2, A3`--chunked-prefill-size``None`Type: intA2, A3`--max-prefill-tokens``16384`Type: intA2, A3`--schedule-policy``fcfs``lpm`, `fcfs`A2, A3`--enable-priority-`  
`scheduling``False`bool flag  
(set to enable)A2, A3`--disable-priority-preemption``False`bool flag  
(set to enable)A2, A3`--default-priority-value``None`Type: intA2, A3`--schedule-low-priority-`  
`values-first``False`bool flag  
(set to enable)A2, A3`--priority-scheduling-`  
`preemption-threshold``10`Type: intA2, A3`--schedule-conservativeness``1.0`Type: floatA2, A3`--page-size``128`Type: intA2, A3`--swa-full-tokens-ratio``0.8`Type: floatPlanned`--disable-hybrid-swa-memory``False`bool flag  
(set to enable)Planned`—radix-eviction-policy``lru``lru`,&lt;br/&gt;`lfu`A2, A3`—enable-prefill-delayer``False`bool flag  
(set to enable)A2, A3`—prefill-delayer-max-delay-passes``30`Type: intA2, A3`—prefill-delayer-token-usage-low-watermark``None`Type: floatA2, A3`—prefill-delayer-forward-passes-buckets``None`List\[float]A2, A3`—prefill-delayer-wait-seconds-buckets``None`List\[float]A2, A3`—abort-on-priority-`&lt;br/&gt;`when-disabled``False`bool flag  
(set to enable)A2, A3`--enable-dynamic-chunking``False`bool flag  
(set to enable)Experimental

## Runtime options

ArgumentDefaultsOptionsServer supported`--device``None`Type: strA2, A3`--tensor-parallel-size`  
`--tp-size``1`Type: intA2, A3`--pipeline-parallel-size`  
`--pp-size``1`Type: int; Currently `2` not supportedExperimental`—attention-context-parallel-size`&lt;br/&gt;`—attn-cp-size``1`Type: int; must be equal to —tp-sizeA2, A3`—moe-data-parallel-size`&lt;br/&gt;`—moe-dp-size``1`Type: intPlanned`—pp-max-micro-batch-size``None`Type: intExperimental`—pp-async-batch-depth``None`Type: intExperimental`—stream-interval``1`Type: intA2, A3`—incremental-streaming-output``False`bool flag (set to enable)A2, A3`—stream-response-default-include-usage``False`bool flag (set to enable)A2, A3`—enable-streaming-session``False`bool flag (set to enable)A2, A3`—random-seed``None`Type: intA2, A3`—constrained-json-`&lt;br/&gt;`whitespace-pattern``None`Type: strA2, A3`—constrained-json-`&lt;br/&gt;`disable-any-whitespace``False`bool flag (set to enable)A2, A3`—watchdog-timeout``300`Type: floatA2, A3`—soft-watchdog-timeout``300`Type: floatA2, A3`—dist-timeout``None`Type: intA2, A3`—download-dir``None`Type: strA2, A3`—model-checksum``None`Type: strPlanned`—base-gpu-id``0`Type: intA2, A3`—gpu-id-step``1`Type: intA2, A3`—sleep-on-idle``False`bool flag (set to enable)A2, A3`—use-ray``False`bool flag (set to enable)A2, A3`—custom-sigquit-handler``None`Only for engineA2, A3

## Logging

ArgumentDefaultsOptionsServer supported`--log-level``info`Type: strA2, A3`--log-level-http``None`Type: strA2, A3`--log-requests``False`bool flag  
(set to enable)A2, A3`--log-requests-level``2``0`, `1`, `2`, `3`A2, A3`--log-requests-format`text`text`, `json`A2, A3`--crash-dump-folder``None`Type: strA2, A3`--enable-metrics``False`bool flag  
(set to enable)A2, A3`--enable-mfu-metrics``False`bool flag  
(set to enable)A2, A3`--enable-metrics-for-`  
`all-schedulers``False`bool flag  
(set to enable)A2, A3`--tokenizer-metrics-`  
`custom-labels-header``x-custom-labels`Type: strA2, A3`--tokenizer-metrics-`  
`allowed-custom-labels``None`List\[str]A2, A3`--extra-metric-labels``None`Type: JSON/DictA2, A3`--bucket-time-to-`  
`first-token``None`List\[float]A2, A3`--bucket-inter-token-`  
`latency``None`List\[float]A2, A3`--bucket-e2e-request-`  
`latency``None`List\[float]A2, A3`--collect-tokens-`  
`histogram``False`bool flag  
(set to enable)A2, A3`--prompt-tokens-buckets``None`List\[str]A2, A3`--generation-tokens-buckets``None`List\[str]A2, A3`--gc-warning-threshold-secs``0.0`Type: floatA2, A3`--decode-log-interval``40`Type: intA2, A3`--enable-request-time-`  
`stats-logging``False`bool flag  
(set to enable)A2, A3`--kv-events-config``None`Type: strSpecial for GPU`--enable-trace``False`bool flag  
(set to enable)A2, A3`--oltp-traces-endpoint``localhost:4317`Type: strA2, A3`—log-requests-target``None`Type: strA2, A3`—uvicorn-access-log-exclude-prefixes``[]`List\[str]A2, A3

## RequestMetricsExporter configuration

ArgumentDefaultsOptionsServer supported`--export-metrics-to-`  
`file``False`bool flag  
(set to enable)A2, A3`--export-metrics-to-`  
`file-dir``None`Type: strA2, A3

ArgumentDefaultsOptionsServer supported`--api-key``None`Type: strA2, A3`--admin-api-key``None`Type: strA2, A3`--served-model-name``None`Type: strA2, A3`--weight-version``default`Type: strA2, A3`--chat-template``None`Type: strA2, A3`—hf-chat-template-name``None`Type: strA2, A3`—completion-template``None`Type: strA2, A3`—file-storage-path``sglang_storage`Type: strUnused reserved parameter`—enable-cache-report``False`bool flag&lt;br/&gt; (set to enable)A2, A3`—reasoning-parser``None``deepseek-r1`&lt;br/&gt;`deepseek-v3`&lt;br/&gt;`glm45`&lt;br/&gt;`gpt-oss`&lt;br/&gt;`kimi`&lt;br/&gt;`qwen3`&lt;br/&gt;`qwen3-thinking`&lt;br/&gt;`step3`A2, A3`—tool-call-parser``None``llama3`&lt;br/&gt; `pythonic`&lt;br/&gt; `qwen`&lt;br/&gt; `qwen3_coder`A2, A3`--sampling-defaults``model``openai`, `model`A2, A3

## Data parallelism

ArgumentDefaultsOptionsServer supported`--data-parallel-size`  
`--dp-size``1`Type: intA2, A3`--load-balance-method``auto``auto`,&lt;br/&gt; `round_robin`,&lt;br/&gt; `follow_bootstrap_room`,&lt;br/&gt; `total_requests`,&lt;br/&gt; `total_tokens`A2, A3

## Multi-node distributed serving

ArgumentDefaultsOptionsServer supported`--dist-init-addr`  
`--nccl-init-addr``None`Type: strA2, A3`--nnodes``1`Type: intA2, A3`--node-rank``0`Type: intA2, A3

## Model override args

ArgumentDefaultsOptionsServer supported`--json-model-override-`  
`args``{}`Type: strA2, A3`--preferred-sampling-`  
`params``None`Type: strA2, A3

## LoRA

ArgumentDefaultsOptionsServer supported`--enable-lora``False`Bool flag  
(set to enable)A2, A3`—enable-lora-overlap-loading``False`Bool flag &lt;br/&gt;(set to enable)A2, A3`—max-lora-rank``None`Type: intA2, A3`—lora-target-modules``None``all`A2, A3`—lora-paths``None`Type: List\[str] /&lt;br/&gt; JSON objectsA2, A3`—max-loras-per-batch``8`Type: intA2, A3`—max-loaded-loras``None`Type: intA2, A3`—lora-eviction-policy``lru``lru`,&lt;br/&gt; `fifo`A2, A3`—lora-backend``csgmv``triton`,&lt;br/&gt;`csgmv`,&lt;br/&gt;`ascend`,&lt;br/&gt;`torch_native`A2, A3`—experts-shared-outer-loras``None`Type: boolA2, A3`—lora-use-virtual-experts``False`bool flag  
(set to enable)A2, A3`—lora-strict-loading``False`Type: boolA2, A3`--max-lora-chunk-size``16``16`, `32`,&lt;br/&gt; `64`, `128`Special for GPU

## Kernel Backends (Attention, Sampling, Grammar, GEMM)

ArgumentDefaultsOptionsServer supported`--attention-backend``None``ascend`A2, A3`--prefill-attention-backend``None``ascend`A2, A3`--decode-attention-backend``None``ascend`A2, A3`--sampling-backend``None``pytorch`,&lt;br/&gt;`ascend`A2, A3`--grammar-backend``None``xgrammar`A2, A3`--mm-attention-backend``None``ascend_attn`A2, A3`--nsa-prefill-backend``flashmla_sparse``flashmla_sparse`,&lt;br/&gt; `flashmla_decode`,&lt;br/&gt;`fa3`,&lt;br/&gt; `tilelang`,&lt;br/&gt; `aiter`Special for GPU`--nsa-decode-backend``fa3``flashmla_prefill`,&lt;br/&gt; `flashmla_kv`,&lt;br/&gt; `fa3`,&lt;br/&gt;`tilelang`,&lt;br/&gt; `aiter`Special for GPU`--fp8-gemm-backend``auto``auto`,&lt;br/&gt; `deep_gemm`,&lt;br/&gt; `flashinfer_trtllm`,&lt;br/&gt;`flashinfer_cutlass`,&lt;br/&gt;`flashinfer_deepgemm`,&lt;br/&gt;`cutlass`,&lt;br/&gt; `triton`,&lt;br/&gt; `aiter`Special for GPU`--disable-flashinfer-`  
`autotune``False`bool flag  
(set to enable)Special for GPU

## Speculative decoding

ArgumentDefaultsOptionsServer supported`--speculative-algorithm``None``EAGLE3`,&lt;br/&gt; `NEXTN`A2, A3`--speculative-draft-model-path`  
`--speculative-draft-model``None`Type: strA2, A3`--speculative-draft-model-`  
`revision``None`Type: str,&lt;br/&gt; `branch name`,&lt;br/&gt; `tag name`,&lt;br/&gt; `commit id`A2, A3`--speculative-draft-load-format``auto``auto`,&lt;br/&gt; `dummy`A2, A3`--speculative-num-steps``None`Type: intA2, A3`--speculative-eagle-topk``None`Type: intA2, A3`--speculative-num-draft-tokens``None`Type: intA2, A3`--speculative-accept-`  
`threshold-single``1.0`Type: floatSpecial for GPU`--speculative-accept-`  
`threshold-acc``1.0`Type: floatSpecial for GPU`--speculative-token-map``None`Type: strA2, A3`--speculative-attention-`  
`mode``prefill``prefill`,&lt;br/&gt; `decode`A2, A3`--speculative-moe-runner-`  
`backend``None``auto`A2, A3`--speculative-moe-a2a-`  
`backend``None``ascend_fuseep`A2, A3`--speculative-draft-attention-backend``None``ascend`A2, A3`--speculative-draft-model-quantization``None``unquant`A2, A3

## Ngram speculative decoding

ArgumentDefaultsOptionsServer supported`--speculative-ngram-`  
`min-match-window-size``1`Type: intExperimental`--speculative-ngram-`  
`max-match-window-size``12`Type: intExperimental`--speculative-ngram-`  
`min-bfs-breadth``1`Type: intExperimental`--speculative-ngram-`  
`max-bfs-breadth``10`Type: intExperimental`--speculative-ngram-`  
`match-type``BFS``BFS`,&lt;br/&gt; `PROB`Experimental. `BFS` uses recency-based expansion; `PROB` uses frequency-based expansion.`—speculative-ngram-`&lt;br/&gt;`max-trie-depth``18`Type: intExperimental`--speculative-ngram-`  
`capacity``10000000`Type: intExperimental`--speculative-ngram-external-corpus-path``None`Type: strExperimental`--speculative-ngram-external-sam-budget``0`Type: intExperimental`--speculative-ngram-external-corpus-max-tokens``10000000`Type: intExperimental

## Expert parallelism

ArgumentDefaultsOptionsServer supported`--expert-parallel-size`  
`--ep-size`  
`--ep``1`Type: intA2, A3`--moe-a2a-backend``none``none`,&lt;br/&gt; `deepep`,&lt;br/&gt; `ascend_fuseep`(It is incompatible with eplb)A2, A3`--moe-runner-backend``auto``auto`, `triton`A2, A3`--flashinfer-mxfp4-`  
`moe-precision``default``default`,&lt;br/&gt; `bf16`Special for GPU`--enable-flashinfer-`  
`allreduce-fusion``False`bool flag  
(set to enable)Special for GPU`--deepep-mode``auto``normal`, &lt;br/&gt;`low_latency`,&lt;br/&gt; `auto`A2, A3`--deepep-config``None`Type: strSpecial for GPU`--ep-num-redundant-experts``0`Type: intA2, A3`--ep-dispatch-algorithm``None``static`,&lt;br/&gt; `dynamic`,&lt;br/&gt; `fake`A2, A3`--init-expert-location``trivial``trivial`,&lt;br/&gt; `<path.pt>`,&lt;br/&gt; `<path.json>`,&lt;br/&gt; `<json_string>`A2, A3`--enable-eplb``False`bool flag  
(set to enable)A2, A3`--eplb-algorithm``deepseek``auto`,&lt;br/&gt; `deepseek`A2, A3`—eplb-rebalance-num-iterations``1000`Type: intA2, A3`—eplb-rebalance-layers-`&lt;br/&gt;`per-chunk``None`Type: intA2, A3`—eplb-min-rebalancing-`&lt;br/&gt;`utilization-threshold``1.0`Type: floatA2, A3`—expert-distribution-`&lt;br/&gt;`recorder-mode``None``stat`,&lt;br/&gt; `stat_approx`,&lt;br/&gt; `per_pass`,&lt;br/&gt; `per_token`A2, A3`—expert-distribution-`&lt;br/&gt;`recorder-buffer-size``None`Type: intA2, A3`—enable-expert-distribution-`&lt;br/&gt;`metrics``False`bool flag (set to enable)A2, A3`—moe-dense-tp-size``None``1`A2, A3`—elastic-ep-backend``None``none`, `mooncake`Special for GPU`--mooncake-ib-device``None`Type: strSpecial for GPU

## Mamba Cache

ArgumentDefaultsOptionsServer supported`--max-mamba-cache-size``None`Type: intA2, A3`--mamba-ssm-dtype``float32``float32`,&lt;br/&gt;`bfloat16`,&lt;br/&gt;`float16`A2, A3`--mamba-full-memory-ratio``0.9`Type: floatA2, A3`--mamba-scheduler-strategy``auto``auto`,&lt;br/&gt;`no_buffer`,&lt;br/&gt;`extra_buffer`A2, A3`--mamba-track-interval``256`Type: intA2, A3

## Hierarchical cache

ArgumentDefaultsOptionsServer supported`--enable-hierarchical-`  
`cache``False`bool flag&lt;br/&gt; (set to enable).&lt;br/&gt; Currently, mamba cache is not supported.A2, A3`--hicache-ratio``2.0`Type: floatA2, A3`--hicache-size``0`Type: intA2, A3`--hicache-write-policy``write_through`Currently only `write_back` supportedA2, A3`—hicache-io-backend``kernel``kernel_ascend`,&lt;br/&gt; `direct`A2, A3`—hicache-mem-layout``layer_first``page_first_direct`,&lt;br/&gt; `page_first_kv_split`A2, A3`—hicache-storage-`&lt;br/&gt;`backend``None``file`A2, A3`—hicache-storage-`&lt;br/&gt;`prefetch-policy``best_effort``best_effort`,&lt;br/&gt; `wait_complete`,&lt;br/&gt; `timeout`Special for GPU`—hicache-storage-`&lt;br/&gt;`backend-extra-config``None`Type: strSpecial for GPU

## LMCache

ArgumentDefaultsOptionsServer supported`--enable-lmcache``False`bool flag  
(set to enable)Special for GPU

## Diffusion LLM

ArgumentDefaultsOptionsServer supported`--dllm-algorithm``None`Type: strA2, A3`--dllm-algorithm-config``None`Type: strA2, A3

## Offloading (must be used with `--disable-cuda-graph`)

ArgumentDefaultsOptionsServer supported`--cpu-offload-gb``0`Type: intA2, A3`--offload-group-size``-1`Type: int (DeepSeek only)A2, A3`--offload-num-in-group``1`Type: int (DeepSeek only)A2, A3`--offload-prefetch-step``1`Type: int (DeepSeek only)A2, A3`--offload-mode``cpu``cpu` (DeepSeek only) &lt;br/&gt;`meta` (DeepSeek only) &lt;br/&gt;`sharded_gpu` (DeepSeek only)A2, A3

## Args for multi-item scoring

ArgumentDefaultsOptionsServer supported`--multi-item-scoring-delimiter``None`Type: intA2, A3

## Optimization/debug options

ArgumentDefaultsOptionsServer supported`--disable-radix-cache``False`bool flag  
(set to enable)A2, A3`--cuda-graph-max-bs``None`Type: intA2, A3`--cuda-graph-bs``None`List\[int]A2, A3`--disable-cuda-graph``False`bool flag  
(set to enable)A2, A3`--disable-cuda-graph-`  
`padding``False`bool flag  
(set to enable)A2, A3`--enable-profile-`  
`cuda-graph``False`bool flag  
(set to enable)A2, A3`--enable-cudagraph-gc``False`bool flag  
(set to enable)A2, A3`--enable-nccl-nvls``False`bool flag  
(set to enable)Special for GPU`--enable-symm-mem``False`bool flag  
(set to enable)Special for GPU`--disable-flashinfer-`  
`cutlass-moe-fp4-allgather``False`bool flag  
(set to enable)Special for GPU`--enable-tokenizer-`  
`batch-encode``False`bool flag  
(set to enable)A2, A3`—disable-tokenizer-`&lt;br/&gt;`batch-decode``False`bool flag  
(set to enable)A2, A3`—disable-custom-`&lt;br/&gt;`all-reduce``False`bool flag  
(set to enable)Special for GPU`—enable-mscclpp``False`bool flag  
(set to enable)Special for GPU`—enable-torch-`&lt;br/&gt;`symm-mem``False`bool flag  
(set to enable)Special for GPU`—disable-overlap`&lt;br/&gt;`-schedule``False`bool flag  
(set to enable)A2, A3`—enable-mixed-`&lt;br/&gt;`chunk``False`bool flag  
(set to enable)A2, A3`—enable-dp-attention``False`bool flag  
(set to enable)A2, A3`—enable-dp-attention-local-control-broadcast``False`bool flag  
(set to enable)A2, A3`—enable-dp-lm-head``False`bool flag  
(set to enable)A2, A3`—enable-two-`&lt;br/&gt;`batch-overlap``False`bool flag  
(set to enable)Planned`—enable-single-`&lt;br/&gt;`batch-overlap``False`bool flag  
(set to enable)A2, A3`—tbo-token-`&lt;br/&gt;`distribution-threshold``0.48`Type: floatPlanned`—enable-torch-`&lt;br/&gt;`compile``False`bool flag&lt;br/&gt; (set to enable)A2, A3`—enable-torch-`&lt;br/&gt;`compile-debug-mode``False`bool flag  
(set to enable)A2, A3`—enforce-piecewise-`&lt;br/&gt;`cuda-graph``False`bool flag&lt;br/&gt; (set to enable); &lt;br/&gt; Currently, Llama-3.1-8B-Instruct and Qwen2.5-7B-Instruct models are supported.A2, A3`—piecewise-cuda-`&lt;br/&gt;`graph-tokens``None`Type: JSON&lt;br/&gt; listA2, A3`—piecewise-cuda-`&lt;br/&gt;`graph-compiler``eager``eager`A2, A3`—torch-compile-max-bs``32`Type: intA2, A3`—piecewise-cuda-`&lt;br/&gt;`graph-max-tokens``None`Type: intA2, A3`—torchao-config`“Type: strSpecial for GPU`—enable-nan-detection``False`bool flag&lt;br/&gt; (set to enable)A2, A3`—enable-p2p-check``False`bool flag  
(set to enable)Special for GPU`—triton-attention-`&lt;br/&gt;`reduce-in-fp32``False`bool flag  
(set to enable)Special for GPU`—triton-attention-`&lt;br/&gt;`num-kv-splits``8`Type: intSpecial for GPU`—triton-attention-`&lt;br/&gt;`split-tile-size``None`Type: intSpecial for GPU`—delete-ckpt-`&lt;br/&gt;`after-loading``False`bool flag&lt;br/&gt; (set to enable)A2, A3`—enable-memory-saver``False`bool flag  
(set to enable)A2, A3`—enable-weights-`&lt;br/&gt;`cpu-backup``False`bool flag  
(set to enable)A2, A3`—enable-draft-weights-`&lt;br/&gt;`cpu-backup``False`bool flag  
(set to enable)A2, A3`—allow-auto-truncate``False`bool flag  
(set to enable)A2, A3`—enable-custom-`&lt;br/&gt;`logit-processor``False`bool flag  
(set to enable)A2, A3`—flashinfer-mla-`&lt;br/&gt;`disable-ragged``False`bool flag  
(set to enable)Special for GPU`—disable-shared-`&lt;br/&gt;`experts-fusion``True`bool flag  
(set to enable)A2, A3`—enforce-shared-experts-fusion``False`bool flag  
(set to enable)A2, A3`—disable-chunked-`&lt;br/&gt;`prefix-cache``True`bool flag  
(set to enable)A2, A3`—disable-fast-`&lt;br/&gt;`image-processor``False`bool flag  
(set to enable)A2, A3`—keep-mm-feature-`&lt;br/&gt;`on-device``False`bool flag  
(set to enable)A2, A3`—enable-return-`&lt;br/&gt;`hidden-states``False`bool flag  
(set to enable)A2, A3`—enable-return-`&lt;br/&gt;`routed-experts``False`bool flag  
(set to enable)A2, A3`—scheduler-recv-`&lt;br/&gt;`interval``1`Type: intA2, A3`—numa-node``None`List\[int]A2, A3`—enable-deterministic-`&lt;br/&gt;`inference``False`bool flag&lt;br/&gt; (set to enable)Planned`--rl-on-policy-target``None``fsdp`Planned`--enable-layerwise-`  
`nvtx-marker``False`bool flag  
(set to enable)Special for GPU`--enable-attn-tp-`  
`input-scattered``False`bool flag  
(set to enable)Experimental`--enable-nsa-prefill-`  
`context-parallel``False`bool flag  
(set to enable)A2, A3`--enable-prefill-context-parallel``False`bool flag  
(set to enable)A2, A3`--prefill-cp-mode``in-seq-split`Type: strA2, A3`--enable-fused-qk-`  
`norm-rope``False`bool flag  
(set to enable)Special for GPU`--enable-precise-embedding-interpolation``False`bool flag  
(set to enable)A2, A3`--gc-threshold``None`List\[int]A2, A3

## Dynamic batch tokenizer

ArgumentDefaultsOptionsServer supported`--enable-dynamic-`  
`batch-tokenizer``False`bool flag  
(set to enable)A2, A3`--dynamic-batch-`  
`tokenizer-batch-size``32`Type: intA2, A3`--dynamic-batch-`  
`tokenizer-batch-timeout``0.002`Type: floatA2, A3

## Debug tensor dumps

ArgumentDefaultsOptionsServer supported`--debug-tensor-dump-`  
`output-folder``None`Type: strA2, A3`--debug-tensor-dump-`  
`layers``None`List\[int]A2, A3`--debug-tensor-dump-`  
`input-file``None`Type: strA2, A3

## PD disaggregation

ArgumentDefaultsOptionsServer supported`--disaggregation-mode``null``null`,&lt;br/&gt; `prefill`,&lt;br/&gt; `decode`A2, A3`--disaggregation-transfer-backend``mooncake``ascend`A2, A3`--disaggregation-bootstrap-port``8998`Type: intA2, A3`—disaggregation-ib-device``None`Type: strSpecial for GPU`—disaggregation-decode-`&lt;br/&gt;`enable-offload-kvcache``False``False`A2, A3`—num-reserved-decode-tokens``512`Type: intA2, A3`—disaggregation-decode-`&lt;br/&gt;`polling-interval``1`Type: intA2, A3

## Encode prefill disaggregation

ArgumentDefaultsOptionsServer supported`—enable-adaptive-dispatch-to-encoder``False`bool flag&lt;br/&gt; (set to enable adaptively dispatch)A2, A3`—encoder-only``False`bool flag&lt;br/&gt; (set to launch an encoder-only server)A2, A3`—language-only``False`bool flag&lt;br/&gt; (set to load weights for the language model only)A2, A3`—encoder-transfer-backend``zmq_to_scheduler``zmq_to_scheduler`, &lt;br/&gt; `zmq_to_tokenizer`,&lt;br/&gt; `mooncake`A2, A3`--encoder-urls``[]`List\[str]&lt;br/&gt; (List of encoder server urls)A2, A3

## Custom weight loader

ArgumentDefaultsOptionsServer supported`--custom-weight-loader``None`List\[str]A2, A3`--weight-loader-disable-`  
`mmap``False`bool flag  
(set to enable)A2, A3`--weight-loader-prefetch-checkpoints``False`bool flag  
(set to enable)A2, A3`--weight-loader-prefetch-num-threads``4`Type: intA2, A3`--remote-instance-weight-`  
`loader-seed-instance-ip``None`Type: strA2, A3`--remote-instance-weight-`  
`loader-seed-instance-service-port``None`Type: intA2, A3`--remote-instance-weight-`  
`loader-send-weights-group-ports``None`Type: JSON  
listA2, A3`--remote-instance-weight-`  
`loader-backend``nccl``transfer_engine`, &lt;br/&gt; `nccl`A2, A3`--remote-instance-weight-`  
`loader-start-seed-via-transfer-engine``False`bool flag  
(set to enable)Special for GPU

## For PD-Multiplexing

ArgumentDefaultsOptionsServer supported`--enable-pdmux``False`bool flag  
(set to enable)Special for GPU`--pdmux-config-path``None`Type: strSpecial for GPU`--sm-group-num``8`Type: intSpecial for GPU

## For Multi-Modal

ArgumentDefaultsOptionsServer supported`—enable-broadcast-mm-`&lt;br/&gt;`inputs-process``False`bool flag&lt;br/&gt; (set to enable)A2, A3`—mm-process-config``None`Type: JSON / DictA2, A3`—mm-enable-dp-encoder``False`bool flag  
(set to enable)A2, A3`—limit-mm-data-per-request``None`Type: JSON / DictA2, A3

## For checkpoint decryption

ArgumentDefaultsOptionsServer supported`--decrypted-config-file``None`Type: strA2, A3`--decrypted-draft-config-file``None`Type: strA2, A3`--enable-prefix-mm-cache``False`bool flag  
(set to enable)A2, A3

## Forward hooks

ArgumentDefaultsOptionsServer supported`—forward-hooks``None`Type: JSON listA2, A3

## Configuration file support

ArgumentDefaultsOptionsServer supported`—config``None`Type: strA2, A3

## Other Params

The following parameters are not supported because the third-party components that depend on are not compatible with the NPU, like Ktransformer, checkpoint-engine etc.

ArgumentDefaultsOptions`--checkpoint-engine-`  
`wait-weights-`  
`before-ready``False`bool flag (set to enable)`--kt-weight-path``None`Type: str`--kt-method``AMXINT4`Type: str`--kt-cpuinfer``None`Type: int`--kt-threadpool-count`2Type: int`--kt-num-gpu-experts``None`Type: int`--kt-max-deferred-`  
`experts-per-token``None`Type: int

The following parameters have some functional deficiencies on community

ArgumentDefaultsOptions`—tool-server``None`Type: str