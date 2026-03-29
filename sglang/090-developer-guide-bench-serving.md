---
title: Bench Serving Guide — SGLang
url: https://docs.sglang.io/developer_guide/bench_serving.html
source: crawler
fetched_at: 2026-02-04T08:47:16.342408778-03:00
rendered_js: false
word_count: 1006
summary: This guide explains how to use the sglang.bench_serving tool to measure and analyze the throughput and latency performance of various LLM inference backends.
tags:
    - sglang
    - benchmarking
    - llm-serving
    - throughput
    - latency-measurement
    - inference-performance
category: guide
---

## Bench Serving Guide[#](#bench-serving-guide "Link to this heading")

This guide explains how to benchmark online serving throughput and latency using `python -m sglang.bench_serving`. It supports multiple inference backends via OpenAI-compatible and native endpoints, and produces both console metrics and optional JSONL outputs.

## What it does[#](#what-it-does "Link to this heading")

- Generates synthetic or dataset-driven prompts and submits them to a target serving endpoint
- Measures throughput, time-to-first-token (TTFT), inter-token latency (ITL), per-request end-to-end latency, and more
- Supports streaming or non-streaming modes, rate control, and concurrency limits

## Supported backends and endpoints[#](#supported-backends-and-endpoints "Link to this heading")

- `sglang` / `sglang-native`: `POST /generate`
- `sglang-oai`, `vllm`, `lmdeploy`: `POST /v1/completions`
- `sglang-oai-chat`, `vllm-chat`, `lmdeploy-chat`: `POST /v1/chat/completions`
- `trt` (TensorRT-LLM): `POST /v2/models/ensemble/generate_stream`
- `gserver`: Custom server (Not Implemented yet in this script)
- `truss`: `POST /v1/models/model:predict`

If `--base-url` is provided, requests are sent to it. Otherwise, `--host` and `--port` are used. When `--model` is not provided, the script will attempt to query `GET /v1/models` for an available model ID (OpenAI-compatible endpoints).

## Prerequisites[#](#prerequisites "Link to this heading")

- Python 3.8+
- Dependencies typically used by this script: `aiohttp`, `numpy`, `requests`, `tqdm`, `transformers`, and for some datasets `datasets`, `pillow`, `pybase64`. Install as needed.
- An inference server running and reachable via the endpoints above
- If your server requires authentication, set environment variable `OPENAI_API_KEY` (used as `Authorization: Bearer <key>`)

## Quick start[#](#quick-start "Link to this heading")

Run a basic benchmark against an sglang server exposing `/generate`:

```
python3-msglang.launch_server--model-pathmeta-llama/Llama-3.1-8B-Instruct
```

```
python3-msglang.bench_serving\
--backendsglang\
--host127.0.0.1--port30000\
--num-prompts1000\
--modelmeta-llama/Llama-3.1-8B-Instruct
```

Or, using an OpenAI-compatible endpoint (completions):

```
python3-msglang.bench_serving\
--backendvllm\
--base-urlhttp://127.0.0.1:8000\
--num-prompts1000\
--modelmeta-llama/Llama-3.1-8B-Instruct
```

## Datasets[#](#datasets "Link to this heading")

Select with `--dataset-name`:

- `sharegpt` (default): loads ShareGPT-style pairs; optionally restrict with `--sharegpt-context-len` and override outputs with `--sharegpt-output-len`
- `random`: random text lengths; sampled from ShareGPT token space
- `random-ids`: random token ids (can lead to gibberish)
- `image`: generates images and wraps them in chat messages; supports custom resolutions, multiple formats, and different content types
- `generated-shared-prefix`: synthetic dataset with shared long system prompts and short questions
- `mmmu`: samples from MMMU (Math split) and includes images

Common dataset flags:

- `--num-prompts N`: number of requests
- `--random-input-len`, `--random-output-len`, `--random-range-ratio`: for random/random-ids/image
- `--image-count`: Number of images per request (for `image` dataset).
- `--apply-chat-template`: apply tokenizer chat template when constructing prompts
- `--dataset-path PATH`: file path for ShareGPT json; if blank and missing, it will be downloaded and cached

Generated Shared Prefix flags (for `generated-shared-prefix`):

- `--gsp-num-groups`
- `--gsp-prompts-per-group`
- `--gsp-system-prompt-len`
- `--gsp-question-len`
- `--gsp-output-len`

Image dataset flags (for `image`):

- `--image-count`: Number of images per request
- `--image-resolution`: Image resolution; supports presets (4k, 1080p, 720p, 360p) or custom ‘heightxwidth’ format (e.g., 1080x1920, 512x768)
- `--image-format`: Image format (jpeg or png)
- `--image-content`: Image content type (random or blank)

## Examples[#](#examples "Link to this heading")

1. To benchmark image dataset with 3 images per request, 500 prompts, 512 input length, and 512 output length, you can run:

```
python-msglang.launch_server--model-pathQwen/Qwen2.5-VL-3B-Instruct--disable-radix-cache
```

```
python-msglang.bench_serving\
--backendsglang-oai-chat\
--dataset-nameimage\
--num-prompts500\
--image-count3\
--image-resolution720p\
--random-input-len512\
--random-output-len512
```

2. To benchmark random dataset with 3000 prompts, 1024 input length, and 1024 output length, you can run:

```
python-msglang.launch_server--model-pathQwen/Qwen2.5-3B-Instruct
```

```
python3-msglang.bench_serving\
--backendsglang\
--dataset-namerandom\
--num-prompts3000\
--random-input1024\
--random-output1024\
--random-range-ratio0.5
```

## Choosing model and tokenizer[#](#choosing-model-and-tokenizer "Link to this heading")

- `--model` is required unless the backend exposes `GET /v1/models`, in which case the first model ID is auto-selected.
- `--tokenizer` defaults to `--model`. Both can be HF model IDs or local paths.
- For ModelScope workflows, setting `SGLANG_USE_MODELSCOPE=true` enables fetching via ModelScope (weights are skipped for speed).
- If your tokenizer lacks a chat template, the script warns because token counting can be less robust for gibberish outputs.

## Rate, concurrency, and streaming[#](#rate-concurrency-and-streaming "Link to this heading")

- `--request-rate`: requests per second. `inf` sends all immediately (burst). Non-infinite rate uses a Poisson process for arrival times.
- `--max-concurrency`: caps concurrent in-flight requests regardless of arrival rate.
- `--disable-stream`: switch to non-streaming mode when supported; TTFT then equals total latency for chat completions.

## Other key options[#](#other-key-options "Link to this heading")

- `--output-file FILE.jsonl`: append JSONL results to file; auto-named if unspecified
- `--output-details`: include per-request arrays (generated texts, errors, ttfts, itls, input/output lens)
- `--extra-request-body '{"top_p":0.9,"temperature":0.6}'`: merged into payload (sampling params, etc.)
- `--disable-ignore-eos`: pass through EOS behavior (varies by backend)
- `--warmup-requests N`: run warmup requests with short output first (default 1)
- `--flush-cache`: call `/flush_cache` (sglang) before main run
- `--profile`: call `/start_profile` and `/stop_profile` (requires server to enable profiling, e.g., `SGLANG_TORCH_PROFILER_DIR`)
- `--lora-name name1 name2 ...`: randomly pick one per request and pass to backend (e.g., `lora_path` for sglang)
- `--tokenize-prompt`: send integer IDs instead of text (currently supports `--backend sglang` only)

## Authentication[#](#authentication "Link to this heading")

If your target endpoint requires OpenAI-style auth, set:

```
exportOPENAI_API_KEY=sk-...yourkey...
```

The script will add `Authorization: Bearer $OPENAI_API_KEY` automatically for OpenAI-compatible routes.

## Metrics explained[#](#metrics-explained "Link to this heading")

Printed after each run:

- Request throughput (req/s)
- Input token throughput (tok/s) - includes both text and vision tokens
- Output token throughput (tok/s)
- Total token throughput (tok/s) - includes both text and vision tokens
- Total input text tokens and Total input vision tokens - per-modality breakdown
- Concurrency: aggregate time of all requests divided by wall time
- End-to-End Latency (ms): mean/median/std/p99 per-request total latency
- Time to First Token (TTFT, ms): mean/median/std/p99 for streaming mode
- Inter-Token Latency (ITL, ms): mean/median/std/p95/p99/max between tokens
- TPOT (ms): Token processing time after first token, i.e., `(latency - ttft)/(tokens-1)`
- Accept length (sglang-only, if available): speculative decoding accept length

The script also retokenizes generated text with the configured tokenizer and reports “retokenized” counts.

## JSONL output format[#](#jsonl-output-format "Link to this heading")

When `--output-file` is set, one JSON object is appended per run. Base fields:

- Arguments summary: backend, dataset, request\_rate, max\_concurrency, etc.
- Duration and totals: completed, total\_input\_tokens, total\_output\_tokens, retokenized totals
- Throughputs and latency statistics as printed in the console
- `accept_length` when available (sglang)

With `--output-details`, an extended object also includes arrays:

- `input_lens`, `output_lens`
- `ttfts`, `itls` (per request: ITL arrays)
- `generated_texts`, `errors`

## End-to-end examples[#](#end-to-end-examples "Link to this heading")

1. sglang native `/generate` (streaming):

```
python3-msglang.bench_serving\
--backendsglang\
--host127.0.0.1--port30000\
--modelmeta-llama/Llama-3.1-8B-Instruct\
--dataset-namerandom\
--random-input-len1024--random-output-len1024--random-range-ratio0.5\
--num-prompts2000\
--request-rate100\
--max-concurrency512\
--output-filesglang_random.jsonl--output-details
```

2. OpenAI-compatible Completions (e.g., vLLM):

```
python3-msglang.bench_serving\
--backendvllm\
--base-urlhttp://127.0.0.1:8000\
--modelmeta-llama/Llama-3.1-8B-Instruct\
--dataset-namesharegpt\
--num-prompts1000\
--sharegpt-output-len256
```

3. OpenAI-compatible Chat Completions (streaming):

```
python3-msglang.bench_serving\
--backendvllm-chat\
--base-urlhttp://127.0.0.1:8000\
--modelmeta-llama/Llama-3.1-8B-Instruct\
--dataset-namerandom\
--num-prompts500\
--apply-chat-template
```

4. Images (VLM) with chat template:

```
python3-msglang.bench_serving\
--backendsglang\
--host127.0.0.1--port30000\
--modelyour-vlm-model\
--dataset-nameimage\
--image-count2\
--image-resolution720p\
--random-input-len128--random-output-len256\
--num-prompts200\
--apply-chat-template
```

4a) Images with custom resolution:

```
python3-msglang.bench_serving\
--backendsglang\
--host127.0.0.1--port30000\
--modelyour-vlm-model\
--dataset-nameimage\
--image-count1\
--image-resolution512x768\
--random-input-len64--random-output-len128\
--num-prompts100\
--apply-chat-template
```

4b) 1080p images with PNG format and blank content:

```
python3-msglang.bench_serving\
--backendsglang\
--host127.0.0.1--port30000\
--modelyour-vlm-model\
--dataset-nameimage\
--image-count1\
--image-resolution1080p\
--image-formatpng\
--image-contentblank\
--random-input-len64--random-output-len128\
--num-prompts100\
--apply-chat-template
```

5. Generated shared prefix (long system prompts + short questions):

```
python3-msglang.bench_serving\
--backendsglang\
--host127.0.0.1--port30000\
--modelmeta-llama/Llama-3.1-8B-Instruct\
--dataset-namegenerated-shared-prefix\
--gsp-num-groups64--gsp-prompts-per-group16\
--gsp-system-prompt-len2048--gsp-question-len128--gsp-output-len256\
--num-prompts1024
```

6. Tokenized prompts (ids) for strict length control (sglang only):

```
python3-msglang.bench_serving\
--backendsglang\
--host127.0.0.1--port30000\
--modelmeta-llama/Llama-3.1-8B-Instruct\
--dataset-namerandom\
--tokenize-prompt\
--random-input-len2048--random-output-len256--random-range-ratio0.2
```

7. Profiling and cache flush (sglang):

```
python3-msglang.bench_serving\
--backendsglang\
--host127.0.0.1--port30000\
--modelmeta-llama/Llama-3.1-8B-Instruct\
--profile\
--flush-cache
```

8. TensorRT-LLM streaming endpoint:

```
python3-msglang.bench_serving\
--backendtrt\
--base-urlhttp://127.0.0.1:8000\
--modelyour-trt-llm-model\
--dataset-namerandom\
--num-prompts100\
--disable-ignore-eos
```

9. Evaluating large-scale KVCache sharing with mooncake trace (sglang only):

```
python3-msglang.bench_serving\
--backendsglang\
--host127.0.0.1--port30000\
--modelmode-name\
--dataset-namemooncake\
--mooncake-slowdown-factor1.0\
--mooncake-num-rounds1000\
--mooncake-workloadconversation|mooncake|agent|synthetic
--use-trace-timestampstrue\
--random-output-len256
```

## Troubleshooting[#](#troubleshooting "Link to this heading")

- All requests failed: verify `--backend`, server URL/port, `--model`, and authentication. Check warmup errors printed by the script.
- Throughput seems too low: adjust `--request-rate` and `--max-concurrency`; verify server batch size/scheduling; ensure streaming is enabled if appropriate.
- Token counts look odd: prefer chat/instruct models with proper chat templates; otherwise tokenization of gibberish may be inconsistent.
- Image/MMMU datasets: ensure you installed extra deps (`pillow`, `datasets`, `pybase64`).
- Authentication errors (401/403): set `OPENAI_API_KEY` or disable auth on your server.

## Notes[#](#notes "Link to this heading")

- The script raises the file descriptor soft limit (`RLIMIT_NOFILE`) to help with many concurrent connections.
- For sglang, `/get_server_info` is queried post-run to report speculative decoding accept length when available.