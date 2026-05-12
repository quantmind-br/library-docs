---
title: Benchmark CLI - vLLM
url: https://docs.vllm.ai/en/latest/benchmarking/cli/
source: sitemap
fetched_at: 2026-05-07T21:10:54.566548497-03:00
rendered_js: false
word_count: 2693
summary: This document provides a comprehensive guide on performing benchmark tests for vLLM, including supported datasets, command-line usage, result visualization, and configurations for custom and multimodal data.
tags:
    - vllm
    - benchmarking
    - performance-testing
    - llm
    - datasets
    - cli
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/benchmarking/cli.md "Edit this page")

This section guides you through running benchmark tests with the extensive datasets supported on vLLM.

It's a living document, updated as new features and datasets become available.

Tip

The benchmarks described on this page are mainly for evaluating specific vLLM features as well as regression testing.

For benchmarking production vLLM servers, we recommend [GuideLLM](https://github.com/vllm-project/guidellm), an established performance benchmarking framework with live progress updates and automatic report generation. It is also more flexible than `vllm bench serve` in terms of dataset loading, request formatting, and workload patterns.

## Dataset Overview[¶](#dataset-overview "Permanent link")

Dataset Online Offline Data Path ShareGPT ✅ ✅ `wget https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split.json` ShareGPT4V (Image) ✅ ✅ `wget https://huggingface.co/datasets/Lin-Chen/ShareGPT4V/resolve/main/sharegpt4v_instruct_gpt4-vision_cap100k.json`  
Note that the images need to be downloaded separately. For example, to download COCO's 2017 Train images:  
`wget http://images.cocodataset.org/zips/train2017.zip` ShareGPT4Video (Video) ✅ ✅ `git clone https://huggingface.co/datasets/ShareGPT4Video/ShareGPT4Video` BurstGPT ✅ ✅ `wget https://github.com/HPMLL/BurstGPT/releases/download/v1.1/BurstGPT_without_fails_2.csv` Sonnet (deprecated) ✅ ✅ Local file: `benchmarks/sonnet.txt` Random ✅ ✅ `synthetic` RandomMultiModal (Image/Video) ✅ ✅ `synthetic` RandomForReranking ✅ ✅ `synthetic` Prefix Repetition ✅ ✅ `synthetic` HuggingFace-VisionArena ✅ ✅ `lmarena-ai/VisionArena-Chat` HuggingFace-MMVU ✅ ✅ `yale-nlp/MMVU` HuggingFace-InstructCoder ✅ ✅ `likaixin/InstructCoder` HuggingFace-AIMO ✅ ✅ `AI-MO/aimo-validation-aime`, `AI-MO/NuminaMath-1.5`, `AI-MO/NuminaMath-CoT` HuggingFace-Other ✅ ✅ `lmms-lab/LLaVA-OneVision-Data`, `Aeala/ShareGPT_Vicuna_unfiltered` HuggingFace-MTBench ✅ ✅ `philschmid/mt-bench` HuggingFace-Blazedit ✅ ✅ `vdaita/edit_5k_char`, `vdaita/edit_10k_char` HuggingFace-ASR ✅ ✅ `openslr/librispeech_asr`, `facebook/voxpopuli`, `LIUM/tedlium`, `edinburghcstr/ami`, `speechcolab/gigaspeech`, `kensho/spgispeech` Spec Bench ✅ ✅ `wget https://raw.githubusercontent.com/hemingkx/Spec-Bench/refs/heads/main/data/spec_bench/question.jsonl` SPEED-Bench ✅ ✅ `curl -LsSf https://raw.githubusercontent.com/NVIDIA-NeMo/Skills/refs/heads/main/nemo_skills/dataset/speed-bench/prepare.py \| python3 -` Custom ✅ ✅ Local file: `data.jsonl` Custom MM ✅ ✅ Local file: `mm_data.jsonl`

Legend:

- ✅ - supported
- 🟡 - Partial support
- 🚧 - to be supported

Note

HuggingFace dataset's `dataset-name` should be set to `hf`. For local `dataset-path`, please set `hf-name` to its Hugging Face ID like

```
--dataset-path/datasets/VisionArena-Chat/--hf-namelmarena-ai/VisionArena-Chat
```

## Examples[¶](#examples "Permanent link")

### 🚀 Online Benchmark[¶](#online-benchmark "Permanent link")

Show more

First start serving your model:

```
vllmserveNousResearch/Hermes-3-Llama-3.1-8B
```

Then run the benchmarking script:

```
# download dataset
# wget https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split.json
vllmbenchserve\
--backendvllm\
--modelNousResearch/Hermes-3-Llama-3.1-8B\
--endpoint/v1/completions\
--dataset-namesharegpt\
--dataset-path<yourdatapath>/ShareGPT_V3_unfiltered_cleaned_split.json\
--num-prompts10
```

If successful, you will see the following output:

```
============ Serving Benchmark Result ============
Successful requests:                     10
Benchmark duration (s):                  5.78
Total input tokens:                      1369
Total generated tokens:                  2212
Request throughput (req/s):              1.73
Output token throughput (tok/s):         382.89
Total token throughput (tok/s):          619.85
---------------Time to First Token----------------
Mean TTFT (ms):                          71.54
Median TTFT (ms):                        73.88
P99 TTFT (ms):                           79.49
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          7.91
Median TPOT (ms):                        7.96
P99 TPOT (ms):                           8.03
---------------Inter-token Latency----------------
Mean ITL (ms):                           7.74
Median ITL (ms):                         7.70
P99 ITL (ms):                            8.39
==================================================
```

#### Results Visualization[¶](#results-visualization "Permanent link")

The `--plot-timeline` and `--plot-dataset-stats` can be used to generate respectively the requests completion timeline and dataset prompt and output tokens statistics, which can be useful for debugging purpose or for deeper analysis.

```
vllmbenchserve\
--backendvllm\
--modelmeta-llama/Llama-3.1-8B-Instruct\
--endpoint/v1/completions\
--dataset-namesharegpt\
--dataset-path<yourdatapath>/ShareGPT_V3_unfiltered_cleaned_split.json\
--num-prompts100\
--plot-timeline\
--timeline-itl-thresholds2,5\
--plot-dataset-stats\
--save-result
```

##### Interactive Timeline[¶](#interactive-timeline "Permanent link")

The generated timeline is an interactive visualization in the form of an HTML file that can be rendered in most browsers. To customize the ITL color thresholds, one can use `--timeline-itl-thresholds` flag (default: 25ms, 50ms)

Example output:

##### Dataset statistics[¶](#dataset-statistics "Permanent link")

The generated figure shows the input prompt and output tokens distribution.

Example output: [![Dataset Statistics](https://docs.vllm.ai/en/latest/assets/contributing/vllm_bench_serve_dataset_stats.png)](https://docs.vllm.ai/en/latest/assets/contributing/vllm_bench_serve_dataset_stats.png)

#### Custom Dataset[¶](#custom-dataset "Permanent link")

If the dataset you want to benchmark is not supported yet in vLLM, even then you can benchmark on it using [`CustomDataset`](https://docs.vllm.ai/en/latest/api/vllm/benchmarks/datasets/datasets/#vllm.benchmarks.datasets.datasets.CustomDataset "            CustomDataset"). Your data needs to be in `.jsonl` format and needs to have "prompt" field per entry, e.g., data.jsonl

```
{"prompt":"What is the capital of India?"}
{"prompt":"What is the capital of Iran?"}
{"prompt":"What is the capital of China?"}

# start server
vllmservemeta-llama/Llama-3.1-8B-Instruct

# run benchmarking script
vllmbenchserve--port9001--save-result--save-detailed\
--backendvllm\
--modelmeta-llama/Llama-3.1-8B-Instruct\
--endpoint/v1/completions\
--dataset-namecustom\
--dataset-path<path-to-your-data-jsonl>\
--custom-skip-chat-template\
--num-prompts80\
--max-concurrency1\
--temperature=0.3\
--top-p=0.75\
--result-dir"./log/"
```

You can skip applying chat template if your data already has it by using `--custom-skip-chat-template`.

#### Custom multimodal dataset[¶](#custom-multimodal-dataset "Permanent link")

If the multimodal dataset you want to benchmark is not supported yet in vLLM, then you can benchmark on it using [`CustomMMDataset`](https://docs.vllm.ai/en/latest/api/vllm/benchmarks/datasets/datasets/#vllm.benchmarks.datasets.datasets.CustomMMDataset "            CustomMMDataset"). Your data needs to be in `.jsonl` format and needs to have "prompt" and "image\_files" field per entry, e.g., `mm_data.jsonl`:

```
{"prompt":"How many animals are present in the given image?","image_files":["/path/to/image/folder/horsepony.jpg"]}
{"prompt":"What colour is the bird shown in the image?","image_files":["/path/to/image/folder/flycatcher.jpeg"]}

# need a model with vision capability here
vllmserveQwen/Qwen2-VL-7B-Instruct

# run benchmarking script
vllmbenchserve--save-result--save-detailed\
--backendopenai-chat\
--modelQwen/Qwen2-VL-7B-Instruct\
--endpoint/v1/chat/completions\
--dataset-namecustom_mm\
--dataset-path<path-to-your-mm-data-jsonl>\
--allowed-local-media-path/path/to/image/folder
```

Note that we need to use the `openai-chat` backend and `/v1/chat/completions` endpoint for multimodal inputs.

#### VisionArena Benchmark for Vision Language Models[¶](#visionarena-benchmark-for-vision-language-models "Permanent link")

```
# need a model with vision capability here
vllmserveQwen/Qwen2-VL-7B-Instruct

vllmbenchserve\
--backendopenai-chat\
--modelQwen/Qwen2-VL-7B-Instruct\
--endpoint/v1/chat/completions\
--dataset-namehf\
--dataset-pathlmarena-ai/VisionArena-Chat\
--hf-splittrain\
--num-prompts1000
```

#### InstructCoder Benchmark with Speculative Decoding[¶](#instructcoder-benchmark-with-speculative-decoding "Permanent link")

```
vllmservemeta-llama/Meta-Llama-3-8B-Instruct\
--speculative-config$'{"method": "ngram",
    "num_speculative_tokens": 5, "prompt_lookup_max": 5,
    "prompt_lookup_min": 2}'

vllmbenchserve\
--modelmeta-llama/Meta-Llama-3-8B-Instruct\
--dataset-namehf\
--dataset-pathlikaixin/InstructCoder\
--num-prompts2048
```

#### Spec Bench Benchmark with Speculative Decoding[¶](#spec-bench-benchmark-with-speculative-decoding "Permanent link")

```
vllmservemeta-llama/Meta-Llama-3-8B-Instruct\
--speculative-config$'{"method": "ngram",
    "num_speculative_tokens": 5, "prompt_lookup_max": 5,
    "prompt_lookup_min": 2}'
```

[SpecBench dataset](https://github.com/hemingkx/Spec-Bench)

Run all categories:

```
# Download the dataset using:
# wget https://raw.githubusercontent.com/hemingkx/Spec-Bench/refs/heads/main/data/spec_bench/question.jsonl

vllmbenchserve\
--modelmeta-llama/Meta-Llama-3-8B-Instruct\
--dataset-namespec_bench\
--dataset-path"<YOUR_DOWNLOADED_PATH>/data/spec_bench/question.jsonl"\
--num-prompts-1
```

Available categories include `[writing, roleplay, reasoning, math, coding, extraction, stem, humanities, translation, summarization, qa, math_reasoning, rag]`.

Run only a specific category like "summarization":

```
vllmbenchserve\
--modelmeta-llama/Meta-Llama-3-8B-Instruct\
--dataset-namespec_bench\
--dataset-path"<YOUR_DOWNLOADED_PATH>/data/spec_bench/question.jsonl"\
--num-prompts-1
--spec-bench-category"summarization"
```

#### SPEED-Bench Benchmark with Speculative Decoding[¶](#speed-bench-benchmark-with-speculative-decoding "Permanent link")

[SPEED-Bench](https://huggingface.co/datasets/nvidia/SPEED-Bench) is a unified and diverse dataset for speculative decoding, supporting acceptance rate and length measurements using the Qualitative split and throughput measurements using the Throughput splits in 5 configuration of input sequence length (1k, 2k, 8k, 16k, 32k).

Note

This dataset is governed by the [NVIDIA Evaluation Dataset License Agreement](https://huggingface.co/datasets/nvidia/SPEED-Bench/blob/main/License.pdf). For each dataset a user elects to use, the user is responsible for checking if the dataset license is fit for the intended purpose. The `prepare.py` script automatically fetches data from all the source datasets.

First, download the dataset to a folder, using this one liner:

```
curl-LsSfhttps://raw.githubusercontent.com/NVIDIA-NeMo/Skills/refs/heads/main/nemo_skills/dataset/speed-bench/prepare.py\|python3-
```

The command supports also the following arguments:

- `--config`: download only a subset of the dataset: `qualitative`, `throughput_1k`, `throughput_2k`, `throughput_8k`, `throughput_16k` and `throughput_32k`. By default, it will download all subsets.
- `--output_dir`: download to a specified folder. By default, it will download to the current directory.

Start a server with speculative decoding:

```
vllmservemeta-llama/Llama-3.3-70B-Instruct\
--speculative-config$'{"method": "eagle3",
    "num_speculative_tokens": 3,
    "model": "nvidia/Llama-3.3-70B-Instruct-Eagle3"}'
```

Run all categories in the Qualitative split:

```
vllmbenchserve\
--modelmeta-llama/Llama-3.3-70B-Instruct\
--dataset-namespeed_bench\
--dataset-path"<YOUR_DOWNLOADED_PATH>/data/speed_bench"\
--num-prompts-1
```

Available categories include `[writing, roleplay, reasoning, math, coding, stem, humanities, multilingual, summarization, qa, rag]`.

Run only a specific category like "multilingual":

```
vllmbenchserve\
--modelmeta-llama/Llama-3.3-70B-Instruct\
--dataset-namespeed_bench\
--dataset-path"<YOUR_DOWNLOADED_PATH>/data/speed_bench"\
--num-prompts-1
--speed-bench-category"multilingual"
```

Run all categories in the Throughput split (2k ISL):

```
vllmbenchserve\
--modelmeta-llama/Llama-3.3-70B-Instruct\
--dataset-namespeed_bench\
--speed-bench-dataset-subsetthroughput_2k
--dataset-path"<YOUR_DOWNLOADED_PATH>/data/speed_bench/"\
--num-prompts-1
```

Available categories include `[high_entropy, mixed, low_entropy]`, where high entropy data contains unstructued data such as creative writing while low entropy data contains more structured data such as coding, more details are in the dataset card.

#### Other HuggingFaceDataset Examples[¶](#other-huggingfacedataset-examples "Permanent link")

```
vllmserveQwen/Qwen2-VL-7B-Instruct
```

`lmms-lab/LLaVA-OneVision-Data`:

```
vllmbenchserve\
--backendopenai-chat\
--modelQwen/Qwen2-VL-7B-Instruct\
--endpoint/v1/chat/completions\
--dataset-namehf\
--dataset-pathlmms-lab/LLaVA-OneVision-Data\
--hf-splittrain\
--hf-subset"chart2text(cauldron)"\
--num-prompts10
```

`Aeala/ShareGPT_Vicuna_unfiltered`:

```
vllmbenchserve\
--backendopenai-chat\
--modelQwen/Qwen2-VL-7B-Instruct\
--endpoint/v1/chat/completions\
--dataset-namehf\
--dataset-pathAeala/ShareGPT_Vicuna_unfiltered\
--hf-splittrain\
--num-prompts10
```

`AI-MO/aimo-validation-aime`:

```
vllmbenchserve\
--modelQwen/QwQ-32B\
--dataset-namehf\
--dataset-pathAI-MO/aimo-validation-aime\
--num-prompts10\
--seed42
```

`philschmid/mt-bench`:

```
vllmbenchserve\
--modelQwen/QwQ-32B\
--dataset-namehf\
--dataset-pathphilschmid/mt-bench\
--num-prompts80
```

`vdaita/edit_5k_char` or `vdaita/edit_10k_char`:

```
vllmbenchserve\
--modelQwen/QwQ-32B\
--dataset-namehf\
--dataset-pathvdaita/edit_5k_char\
--num-prompts90\
--blazedit-min-distance0.01\
--blazedit-max-distance0.99
```

`openslr/librispeech_asr`, `facebook/voxpopuli`, `LIUM/tedlium`, `edinburghcstr/ami`, `speechcolab/gigaspeech`, `kensho/spgispeech`

```
vllmbenchserve\
--modelopenai/whisper-large-v3-turbo\
--backendopenai-audio\
--dataset-namehf\
--dataset-pathfacebook/voxpopuli--hf-subseten--hf-splittest--no-stream--trust-remote-code\
--num-prompts99999999\
--no-oversample\
--endpoint/v1/audio/transcriptions\
--ready-check-timeout-sec600\
--save-result\
--max-concurrency512
```

#### Running With Sampling Parameters[¶](#running-with-sampling-parameters "Permanent link")

When using OpenAI-compatible backends such as `vllm`, optional sampling parameters can be specified. Example client command:

```
vllmbenchserve\
--backendvllm\
--modelNousResearch/Hermes-3-Llama-3.1-8B\
--endpoint/v1/completions\
--dataset-namesharegpt\
--dataset-path<yourdatapath>/ShareGPT_V3_unfiltered_cleaned_split.json\
--top-k10\
--top-p0.9\
--temperature0.5\
--num-prompts10
```

#### Running With Ramp-Up Request Rate[¶](#running-with-ramp-up-request-rate "Permanent link")

The benchmark tool also supports ramping up the request rate over the duration of the benchmark run. This can be useful for stress testing the server or finding the maximum throughput that it can handle, given some latency budget.

Two ramp-up strategies are supported:

- `linear`: Increases the request rate linearly from a start value to an end value.
- `exponential`: Increases the request rate exponentially.

The following arguments can be used to control the ramp-up:

- `--ramp-up-strategy`: The ramp-up strategy to use (`linear` or `exponential`).
- `--ramp-up-start-rps`: The request rate at the beginning of the benchmark.
- `--ramp-up-end-rps`: The request rate at the end of the benchmark.

#### Load Pattern Configuration[¶](#load-pattern-configuration "Permanent link")

vLLM's benchmark serving script provides sophisticated load pattern simulation capabilities through three key parameters that control request generation and concurrency behavior:

##### Load Pattern Control Parameters[¶](#load-pattern-control-parameters "Permanent link")

- `--request-rate`: Controls the target request generation rate (requests per second). Set to `inf` for maximum throughput testing or finite values for controlled load simulation.
- `--burstiness`: Controls traffic variability using a Gamma distribution (range: &gt; 0). Lower values create bursty traffic, higher values create uniform traffic.
- `--max-concurrency`: Limits concurrent outstanding requests. If this argument is not provided, concurrency is unlimited. Set a value to simulate backpressure.

These parameters work together to create realistic load patterns with carefully chosen defaults. The `--request-rate` parameter defaults to `inf` (infinite), which sends all requests immediately for maximum throughput testing. When set to finite values, it uses either a Poisson process (default `--burstiness=1.0`) or Gamma distribution for realistic request timing. The `--burstiness` parameter only takes effect when `--request-rate` is not infinite - a value of 1.0 creates natural Poisson traffic, while lower values (0.1-0.5) create bursty patterns and higher values (2.0-5.0) create uniform spacing. The `--max-concurrency` parameter defaults to `None` (unlimited) but can be set to simulate real-world constraints where a load balancer or API gateway limits concurrent connections. When combined, these parameters allow you to simulate everything from unrestricted stress testing (`--request-rate=inf`) to production-like scenarios with realistic arrival patterns and resource constraints.

The `--burstiness` parameter mathematically controls request arrival patterns using a Gamma distribution where:

- Shape parameter: `burstiness` value
- Coefficient of Variation (CV): \\(\\frac{1}{\\sqrt{burstiness}}\\)
- Traffic characteristics:
  
  - `burstiness = 0.1`: Highly bursty traffic (CV ≈ 3.16) - stress testing
  - `burstiness = 1.0`: Natural Poisson traffic (CV = 1.0) - realistic simulation
  - `burstiness = 5.0`: Uniform traffic (CV ≈ 0.45) - controlled load testing

[![Load Pattern Examples](https://docs.vllm.ai/en/latest/assets/contributing/load-pattern-examples.png)](https://docs.vllm.ai/en/latest/assets/contributing/load-pattern-examples.png)

*Figure: Load pattern examples for each use case. Top row: Request arrival timelines showing cumulative requests over time. Bottom row: Inter-arrival time distributions showing traffic variability patterns. Each column represents a different use case with its specific parameter settings and resulting traffic characteristics.*

Load Pattern Recommendations by Use Case:

Use Case Burstiness Request Rate Max Concurrency Description Maximum Throughput N/A Infinite Limited **Most common**: Simulates load balancer/gateway limits with unlimited user demand Realistic Testing 1.0 Moderate (5-20) Infinite Natural Poisson traffic patterns for baseline performance Stress Testing 0.1-0.5 High (20-100) Infinite Challenging burst patterns to test resilience Latency Profiling 2.0-5.0 Low (1-10) Infinite Uniform load for consistent timing analysis Capacity Planning 1.0 Variable Limited Test resource limits with realistic constraints SLA Validation 1.0 Target rate SLA limit Production-like constraints for compliance testing

These load patterns help evaluate different aspects of your vLLM deployment, from basic performance characteristics to resilience under challenging traffic conditions.

The **Maximum Throughput** pattern (`--request-rate=inf --max-concurrency=<limit>`) is the most commonly used configuration for production benchmarking. This simulates real-world deployment architectures where:

- Users send requests as fast as they can (infinite rate)
- A load balancer or API gateway controls the maximum concurrent connections
- The system operates at its concurrency limit, revealing true throughput capacity
- `--burstiness` has no effect since request timing is not controlled when rate is infinite

This pattern helps determine optimal concurrency settings for your production load balancer configuration.

To effectively configure load patterns, especially for **Capacity Planning** and **SLA Validation** use cases, you need to understand your system's resource limits. During startup, vLLM reports KV cache configuration that directly impacts your load testing parameters:

```
GPU KV cache size: 15,728,640 tokens
Maximum concurrency for 8,192 tokens per request: 1920
```

Where:

- GPU KV cache size: Total tokens that can be cached across all concurrent requests
- Maximum concurrency: Theoretical maximum concurrent requests for the given `max_model_len`
- Calculation: `max_concurrency = kv_cache_size / max_model_len`

Using KV cache metrics for load pattern configuration:

- For Capacity Planning: Set `--max-concurrency` to 80-90% of the reported maximum to test realistic resource constraints
- For SLA Validation: Use the reported maximum as your SLA limit to ensure compliance testing matches production capacity
- For Realistic Testing: Monitor memory usage when approaching theoretical limits to understand sustainable request rates
- Request rate guidance: Use the KV cache size to estimate sustainable request rates for your specific workload and sequence lengths

### 📈 Offline Throughput Benchmark[¶](#offline-throughput-benchmark "Permanent link")

Show more

```
vllmbenchthroughput\
--modelNousResearch/Hermes-3-Llama-3.1-8B\
--dataset-namesonnet\
--dataset-pathvllm/benchmarks/sonnet.txt\
--num-prompts10
```

If successful, you will see the following output

```
Throughput: 7.15 requests/s, 4656.00 total tokens/s, 1072.15 output tokens/s
Total num prompt tokens:  5014
Total num output tokens:  1500
```

#### VisionArena Benchmark for Vision Language Models[¶](#visionarena-benchmark-for-vision-language-models_1 "Permanent link")

```
vllmbenchthroughput\
--modelQwen/Qwen2-VL-7B-Instruct\
--backendvllm-chat\
--dataset-namehf\
--dataset-pathlmarena-ai/VisionArena-Chat\
--num-prompts1000\
--hf-splittrain
```

The `num prompt tokens` now includes image token counts

```
Throughput: 2.55 requests/s, 4036.92 total tokens/s, 326.90 output tokens/s
Total num prompt tokens:  14527
Total num output tokens:  1280
```

#### InstructCoder Benchmark with Speculative Decoding[¶](#instructcoder-benchmark-with-speculative-decoding_1 "Permanent link")

```
VLLM_WORKER_MULTIPROC_METHOD=spawn\
vllmbenchthroughput\
--dataset-name=hf\
--dataset-path=likaixin/InstructCoder\
--model=meta-llama/Meta-Llama-3-8B-Instruct\
--input-len=1000\
--output-len=100\
--num-prompts=2048\
--async-engine\
--speculative-config$'{"method": "ngram",
    "num_speculative_tokens": 5, "prompt_lookup_max": 5,
    "prompt_lookup_min": 2}'

Throughput: 104.77 requests/s, 23836.22 total tokens/s, 10477.10 output tokens/s
Total num prompt tokens:  261136
Total num output tokens:  204800
```

#### Other HuggingFaceDataset Examples[¶](#other-huggingfacedataset-examples_1 "Permanent link")

`lmms-lab/LLaVA-OneVision-Data`:

```
vllmbenchthroughput\
--modelQwen/Qwen2-VL-7B-Instruct\
--backendvllm-chat\
--dataset-namehf\
--dataset-pathlmms-lab/LLaVA-OneVision-Data\
--hf-splittrain\
--hf-subset"chart2text(cauldron)"\
--num-prompts10
```

`Aeala/ShareGPT_Vicuna_unfiltered`:

```
vllmbenchthroughput\
--modelQwen/Qwen2-VL-7B-Instruct\
--backendvllm-chat\
--dataset-namehf\
--dataset-pathAeala/ShareGPT_Vicuna_unfiltered\
--hf-splittrain\
--num-prompts10
```

`AI-MO/aimo-validation-aime`:

```
vllmbenchthroughput\
--modelQwen/QwQ-32B\
--backendvllm\
--dataset-namehf\
--dataset-pathAI-MO/aimo-validation-aime\
--hf-splittrain\
--num-prompts10
```

Benchmark with LoRA adapters:

```
# download dataset
# wget https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split.json
vllmbenchthroughput\
--modelmeta-llama/Llama-2-7b-hf\
--backendvllm\
--dataset_path<yourdatapath>/ShareGPT_V3_unfiltered_cleaned_split.json\
--dataset_namesharegpt\
--num-prompts10\
--max-loras2\
--max-lora-rank8\
--enable-lora\
--lora-pathyard1/llama-2-7b-sql-lora-test
```

#### Synthetic Random Multimodal (random-mm)[¶](#synthetic-random-multimodal-random-mm "Permanent link")

Generate synthetic multimodal inputs for offline throughput testing without external datasets. Use `--backend vllm-chat` so that image tokens are counted correctly.

```
vllmbenchthroughput\
--modelQwen/Qwen2-VL-7B-Instruct\
--backendvllm-chat\
--dataset-namerandom-mm\
--num-prompts100\
--random-input-len300\
--random-output-len40\
--random-mm-base-items-per-request2\
--random-mm-limit-mm-per-prompt'{"image": 3, "video": 0}'\
--random-mm-bucket-config'{(256, 256, 1): 0.7, (720, 1280, 1): 0.3}'
```

### 🛠️ Structured Output Benchmark[¶](#structured-output-benchmark "Permanent link")

Show more

Benchmark the performance of structured output generation (JSON, grammar, regex).

#### Server Setup[¶](#server-setup "Permanent link")

```
vllmserveNousResearch/Hermes-3-Llama-3.1-8B
```

#### JSON Schema Benchmark[¶](#json-schema-benchmark "Permanent link")

```
python3benchmarks/benchmark_serving_structured_output.py\
--backendvllm\
--modelNousResearch/Hermes-3-Llama-3.1-8B\
--datasetjson\
--structured-output-ratio1.0\
--request-rate10\
--num-prompts1000
```

#### Grammar-based Generation Benchmark[¶](#grammar-based-generation-benchmark "Permanent link")

```
python3benchmarks/benchmark_serving_structured_output.py\
--backendvllm\
--modelNousResearch/Hermes-3-Llama-3.1-8B\
--datasetgrammar\
--structure-typegrammar\
--request-rate10\
--num-prompts1000
```

#### Regex-based Generation Benchmark[¶](#regex-based-generation-benchmark "Permanent link")

```
python3benchmarks/benchmark_serving_structured_output.py\
--backendvllm\
--modelNousResearch/Hermes-3-Llama-3.1-8B\
--datasetregex\
--request-rate10\
--num-prompts1000
```

#### Choice-based Generation Benchmark[¶](#choice-based-generation-benchmark "Permanent link")

```
python3benchmarks/benchmark_serving_structured_output.py\
--backendvllm\
--modelNousResearch/Hermes-3-Llama-3.1-8B\
--datasetchoice\
--request-rate10\
--num-prompts1000
```

#### XGrammar Benchmark Dataset[¶](#xgrammar-benchmark-dataset "Permanent link")

```
python3benchmarks/benchmark_serving_structured_output.py\
--backendvllm\
--modelNousResearch/Hermes-3-Llama-3.1-8B\
--datasetxgrammar_bench\
--request-rate10\
--num-prompts1000
```

### 📚 Long Document QA Benchmark[¶](#long-document-qa-benchmark "Permanent link")

Show more

Benchmark the performance of long document question-answering with prefix caching.

#### Basic Long Document QA Test[¶](#basic-long-document-qa-test "Permanent link")

```
python3benchmarks/benchmark_long_document_qa_throughput.py\
--modelmeta-llama/Llama-2-7b-chat-hf\
--enable-prefix-caching\
--num-documents16\
--document-length2000\
--output-len50\
--repeat-count5
```

#### Different Repeat Modes[¶](#different-repeat-modes "Permanent link")

```
# Random mode (default) - shuffle prompts randomly
python3benchmarks/benchmark_long_document_qa_throughput.py\
--modelmeta-llama/Llama-2-7b-chat-hf\
--enable-prefix-caching\
--num-documents8\
--document-length3000\
--repeat-count3\
--repeat-moderandom

# Tile mode - repeat entire prompt list in sequence
python3benchmarks/benchmark_long_document_qa_throughput.py\
--modelmeta-llama/Llama-2-7b-chat-hf\
--enable-prefix-caching\
--num-documents8\
--document-length3000\
--repeat-count3\
--repeat-modetile

# Interleave mode - repeat each prompt consecutively
python3benchmarks/benchmark_long_document_qa_throughput.py\
--modelmeta-llama/Llama-2-7b-chat-hf\
--enable-prefix-caching\
--num-documents8\
--document-length3000\
--repeat-count3\
--repeat-modeinterleave
```

### 🗂️ Prefix Caching Benchmark[¶](#prefix-caching-benchmark "Permanent link")

Show more

Benchmark the efficiency of automatic prefix caching.

#### Fixed Prompt with Prefix Caching[¶](#fixed-prompt-with-prefix-caching "Permanent link")

```
python3benchmarks/benchmark_prefix_caching.py\
--modelmeta-llama/Llama-2-7b-chat-hf\
--enable-prefix-caching\
--num-prompts1\
--repeat-count100\
--input-length-range128:256
```

#### ShareGPT Dataset with Prefix Caching[¶](#sharegpt-dataset-with-prefix-caching "Permanent link")

```
# download dataset
# wget https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split.json

python3benchmarks/benchmark_prefix_caching.py\
--modelmeta-llama/Llama-2-7b-chat-hf\
--dataset-path/path/ShareGPT_V3_unfiltered_cleaned_split.json\
--enable-prefix-caching\
--num-prompts20\
--repeat-count5\
--input-length-range128:256
```

##### Prefix Repetition Dataset[¶](#prefix-repetition-dataset "Permanent link")

```
vllmbenchserve\
--backendopenai\
--modelmeta-llama/Llama-2-7b-chat-hf\
--dataset-nameprefix_repetition\
--num-prompts100\
--prefix-repetition-prefix-len512\
--prefix-repetition-suffix-len128\
--prefix-repetition-num-prefixes5\
--prefix-repetition-output-len128
```

### 🧪 Hashing Benchmarks[¶](#hashing-benchmarks "Permanent link")

Show more

Two helper scripts live in `benchmarks/` to compare hashing options used by prefix caching and related utilities. They are standalone (no server required) and help choose a hash algorithm before enabling prefix caching in production.

- `benchmarks/benchmark_hash.py`: Micro-benchmark that measures per-call latency of three implementations on a representative `(bytes, tuple[int])` payload.

```
pythonbenchmarks/benchmark_hash.py--iterations20000--seed42
```

- `benchmarks/benchmark_prefix_block_hash.py`: End-to-end block hashing benchmark that runs the full prefix-cache hash pipeline (`hash_block_tokens`) across many fake blocks and reports throughput.

```
pythonbenchmarks/benchmark_prefix_block_hash.py--num-blocks20000--block-size32--trials5
```

Supported algorithms: `sha256`, `sha256_cbor`, `xxhash`, `xxhash_cbor`. Install optional deps to exercise all variants:

```
uvpipinstallxxhashcbor2
```

If an algorithm’s dependency is missing, the script will skip it and continue.

### ⚡ Request Prioritization Benchmark[¶](#request-prioritization-benchmark "Permanent link")

Show more

Benchmark the performance of request prioritization in vLLM.

#### Basic Prioritization Test[¶](#basic-prioritization-test "Permanent link")

```
python3benchmarks/benchmark_prioritization.py\
--modelmeta-llama/Llama-2-7b-chat-hf\
--input-len128\
--output-len64\
--num-prompts100\
--scheduling-policypriority
```

#### Multiple Sequences per Prompt[¶](#multiple-sequences-per-prompt "Permanent link")

```
python3benchmarks/benchmark_prioritization.py\
--modelmeta-llama/Llama-2-7b-chat-hf\
--input-len128\
--output-len64\
--num-prompts100\
--scheduling-policypriority\
--n2
```

### 👁️ Multi-Modal Benchmark[¶](#multi-modal-benchmark "Permanent link")

Show more

Benchmark the performance of multi-modal requests in vLLM.

#### Images (ShareGPT4V)[¶](#images-sharegpt4v "Permanent link")

Start vLLM:

```
vllmserveQwen/Qwen2.5-VL-7B-Instruct\
--dtypebfloat16\
--limit-mm-per-prompt'{"image": 1}'\
--allowed-local-media-path/path/to/sharegpt4v/images
```

Send requests with images:

```
vllmbenchserve\
--backendopenai-chat\
--modelQwen/Qwen2.5-VL-7B-Instruct\
--dataset-namesharegpt\
--dataset-path/path/to/ShareGPT4V/sharegpt4v_instruct_gpt4-vision_cap100k.json\
--num-prompts100\
--save-result\
--result-dir~/vllm_benchmark_results\
--save-detailed\
--endpoint/v1/chat/completions
```

#### Videos (ShareGPT4Video)[¶](#videos-sharegpt4video "Permanent link")

Start vLLM:

```
vllmserveQwen/Qwen2.5-VL-7B-Instruct\
--dtypebfloat16\
--limit-mm-per-prompt'{"video": 1}'\
--allowed-local-media-path/path/to/sharegpt4video/videos
```

Send requests with videos:

```
vllmbenchserve\
--backendopenai-chat\
--modelQwen/Qwen2.5-VL-7B-Instruct\
--dataset-namesharegpt\
--dataset-path/path/to/ShareGPT4Video/llava_v1_5_mix665k_with_video_chatgpt72k_share4video28k.json\
--num-prompts100\
--save-result\
--result-dir~/vllm_benchmark_results\
--save-detailed\
--endpoint/v1/chat/completions
```

#### Synthetic Random Images (random-mm)[¶](#synthetic-random-images-random-mm "Permanent link")

Generate synthetic image inputs alongside random text prompts to stress-test vision models without external datasets.

Notes:

- For online benchmarks, use `--backend openai-chat` with endpoint `/v1/chat/completions`.
- For offline benchmarks, use `--backend vllm-chat` (see [Offline Throughput Benchmark](#-offline-throughput-benchmark) for an example).

Start the server (example):

```
vllmserveQwen/Qwen2.5-VL-3B-Instruct\
--dtypebfloat16\
--max-model-len16384\
--limit-mm-per-prompt'{"image": 3, "video": 0}'\
--mm-processor-kwargsmax_pixels=1003520
```

Benchmark. It is recommended to use the flag `--ignore-eos` to simulate real responses. You can set the size of the output via the arg `random-output-len`.

Ex.1: Fixed number of items and a single image resolution, enforcing generation of approx 40 tokens:

```
vllmbenchserve\
--backendopenai-chat\
--modelQwen/Qwen2.5-VL-3B-Instruct\
--endpoint/v1/chat/completions\
--dataset-namerandom-mm\
--num-prompts100\
--max-concurrency10\
--random-prefix-len25\
--random-input-len300\
--random-output-len40\
--random-range-ratio0.2\
--random-mm-base-items-per-request2\
--random-mm-limit-mm-per-prompt'{"image": 3, "video": 0}'\
--random-mm-bucket-config'{(224, 224, 1): 1.0}'\
--request-rateinf\
--ignore-eos\
--seed42
```

The number of items per request can be controlled by passing multiple image buckets:

```
--random-mm-base-items-per-request2\
--random-mm-num-mm-items-range-ratio0.5\
--random-mm-limit-mm-per-prompt'{"image": 4, "video": 0}'\
--random-mm-bucket-config'{(256, 256, 1): 0.7, (720, 1280, 1): 0.3}'\
```

Flags specific to `random-mm`:

- `--random-mm-base-items-per-request`: base number of multimodal items per request.
- `--random-mm-num-mm-items-range-ratio`: vary item count uniformly in the closed integer range \[floor(n·(1−r)), ceil(n·(1+r))]. Set r=0 to keep it fixed; r=1 allows 0 items.
- `--random-mm-limit-mm-per-prompt`: per-modality hard caps, e.g. '{"image": 3, "video": 0}'.
- `--random-mm-bucket-config`: dict mapping (H, W, T) → probability. Entries with probability 0 are removed; remaining probabilities are renormalized to sum to 1. Use T=1 for images. Set any T&gt;1 for videos (video sampling not yet supported).

Behavioral notes:

- If the requested base item count cannot be satisfied under the provided per-prompt limits, the tool raises an error rather than silently clamping.

How sampling works:

- Determine per-request item count k by sampling uniformly from the integer range defined by `--random-mm-base-items-per-request` and `--random-mm-num-mm-items-range-ratio`, then clamp k to at most the sum of per-modality limits.
- For each of the k items, sample a bucket (H, W, T) according to the normalized probabilities in `--random-mm-bucket-config`, while tracking how many items of each modality have been added.
- If a modality (e.g., image) reaches its limit from `--random-mm-limit-mm-per-prompt`, all buckets of that modality are excluded and the remaining bucket probabilities are renormalized before continuing. This should be seen as an edge case, and if this behavior can be avoided by setting `--random-mm-limit-mm-per-prompt` to a large number. Note that this might result in errors due to engine config `--limit-mm-per-prompt`.
- The resulting request contains synthetic image data in `multi_modal_data` (OpenAI Chat format). When `random-mm` is used with the OpenAI Chat backend, prompts remain text and MM content is attached via `multi_modal_data`.

### 🔬 Multimodal Processor Benchmark[¶](#multimodal-processor-benchmark "Permanent link")

Benchmark per-stage latency of the multimodal (MM) input processor pipeline, including the encoder forward pass. This is useful for profiling preprocessing bottlenecks in vision-language models.

Show more

The benchmark measures the following stages for each request:

Stage Description `get_mm_hashes_secs` Time spent hashing multimodal inputs `get_cache_missing_items_secs` Time spent looking up the processor cache `apply_hf_processor_secs` Time spent in the HuggingFace processor `merge_mm_kwargs_secs` Time spent merging multimodal kwargs `apply_prompt_updates_secs` Time spent updating prompt tokens `preprocessor_total_secs` Total preprocessing time `encoder_forward_secs` Time spent in the encoder model forward pass `num_encoder_calls` Number of encoder invocations per request

The benchmark also reports end-to-end latency (TTFT + decode time) per request. Use `--metric-percentiles` to select which percentiles to report (default: p99) and `--output-json` to save results.

#### Basic Example with Synthetic Data (random-mm)[¶](#basic-example-with-synthetic-data-random-mm "Permanent link")

```
vllmbenchmm-processor\
--modelQwen/Qwen2-VL-7B-Instruct\
--dataset-namerandom-mm\
--num-prompts50\
--random-input-len300\
--random-output-len40\
--random-mm-base-items-per-request2\
--random-mm-limit-mm-per-prompt'{"image": 3, "video": 0}'\
--random-mm-bucket-config'{(256, 256, 1): 0.7, (720, 1280, 1): 0.3}'
```

#### Using a HuggingFace Dataset[¶](#using-a-huggingface-dataset "Permanent link")

```
vllmbenchmm-processor\
--modelQwen/Qwen2-VL-7B-Instruct\
--dataset-namehf\
--dataset-pathlmarena-ai/VisionArena-Chat\
--hf-splittrain\
--num-prompts100
```

#### Warmup, Custom Percentiles, and JSON Output[¶](#warmup-custom-percentiles-and-json-output "Permanent link")

```
vllmbenchmm-processor\
--modelQwen/Qwen2-VL-7B-Instruct\
--dataset-namerandom-mm\
--num-prompts200\
--num-warmups5\
--random-input-len300\
--random-output-len40\
--random-mm-base-items-per-request1\
--metric-percentiles50,90,95,99\
--output-jsonresults.json
```

See [`vllm bench mm-processor`](https://docs.vllm.ai/en/latest/cli/bench/mm_processor/) for the full argument reference.

### Embedding Benchmark[¶](#embedding-benchmark "Permanent link")

Benchmark the performance of embedding requests in vLLM.

Show more

#### Text Embeddings[¶](#text-embeddings "Permanent link")

Unlike generative models which use Completions API or Chat Completions API, you should set `--backend openai-embeddings` and `--endpoint /v1/embeddings` to use the Embeddings API.

You can use any text dataset to benchmark the model, such as ShareGPT.

Start the server:

```
vllmservejinaai/jina-embeddings-v3--trust-remote-code
```

Run the benchmark:

```
# download dataset
# wget https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split.json
vllmbenchserve\
--modeljinaai/jina-embeddings-v3\
--backendopenai-embeddings\
--endpoint/v1/embeddings\
--dataset-namesharegpt\
--dataset-path<yourdatapath>/ShareGPT_V3_unfiltered_cleaned_split.json
```

#### Multi-modal Embeddings[¶](#multi-modal-embeddings "Permanent link")

Unlike generative models which use Completions API or Chat Completions API, you should set `--endpoint /v1/embeddings` to use the Embeddings API. The backend to use depends on the model:

- CLIP: `--backend openai-embeddings-clip`
- VLM2Vec: `--backend openai-embeddings-vlm2vec`

For other models, please add your own implementation inside [vllm/benchmarks/lib/endpoint\_request\_func.py](https://github.com/vllm-project/vllm/blob/main/vllm/benchmarks/lib/endpoint_request_func.py) to match the expected instruction format.

You can use any text or multi-modal dataset to benchmark the model, as long as the model supports it. For example, you can use ShareGPT and VisionArena to benchmark vision-language embeddings.

Serve and benchmark CLIP:

```
# Run this in another process
vllmserveopenai/clip-vit-base-patch32

# Run these one by one after the server is up
# download dataset
# wget https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split.json
vllmbenchserve\
--modelopenai/clip-vit-base-patch32\
--backendopenai-embeddings-clip\
--endpoint/v1/embeddings\
--dataset-namesharegpt\
--dataset-path<yourdatapath>/ShareGPT_V3_unfiltered_cleaned_split.json

vllmbenchserve\
--modelopenai/clip-vit-base-patch32\
--backendopenai-embeddings-clip\
--endpoint/v1/embeddings\
--dataset-namehf\
--dataset-pathlmarena-ai/VisionArena-Chat
```

Serve and benchmark VLM2Vec:

```
# Run this in another process
vllmserveTIGER-Lab/VLM2Vec-Full--runnerpooling\
--trust-remote-code\
--chat-templateexamples/template_vlm2vec_phi3v.jinja

# Run these one by one after the server is up
# download dataset
# wget https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split.json
vllmbenchserve\
--modelTIGER-Lab/VLM2Vec-Full\
--backendopenai-embeddings-vlm2vec\
--endpoint/v1/embeddings\
--dataset-namesharegpt\
--dataset-path<yourdatapath>/ShareGPT_V3_unfiltered_cleaned_split.json

vllmbenchserve\
--modelTIGER-Lab/VLM2Vec-Full\
--backendopenai-embeddings-vlm2vec\
--endpoint/v1/embeddings\
--dataset-namehf\
--dataset-pathlmarena-ai/VisionArena-Chat
```

### Reranker Benchmark[¶](#reranker-benchmark "Permanent link")

Benchmark the performance of rerank requests in vLLM.

Show more

Unlike generative models which use Completions API or Chat Completions API, you should set `--backend vllm-rerank` and `--endpoint /v1/rerank` to use the Reranker API.

For reranking, the only supported dataset is `--dataset-name random-rerank`

Start the server:

```
vllmserveBAAI/bge-reranker-v2-m3
```

Run the benchmark:

```
vllmbenchserve\
--modelBAAI/bge-reranker-v2-m3\
--backendvllm-rerank\
--endpoint/v1/rerank\
--dataset-namerandom-rerank\
--tokenizerBAAI/bge-reranker-v2-m3\
--random-input-len512\
--num-prompts10\
--random-batch-size5
```

For reranker models, this will create `num_prompts / random_batch_size` requests with `random_batch_size` "documents" where each one has close to `random_input_len` tokens. In the example above, this results in 2 rerank requests with 5 "documents" each where each document has close to 512 tokens.

Please note that the `/v1/rerank` is also supported by embedding models. So if you're running with an embedding model, also set `--no_reranker`. Because in this case the query is treated as an individual prompt by the server, here we send `random_batch_size - 1` documents to account for the extra prompt which is the query. The token accounting to report the throughput numbers correctly is also adjusted.