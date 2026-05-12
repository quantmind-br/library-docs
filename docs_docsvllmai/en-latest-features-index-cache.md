---
title: IndexCache - vLLM
url: https://docs.vllm.ai/en/latest/features/index_cache/
source: sitemap
fetched_at: 2026-05-07T21:14:09.935132196-03:00
rendered_js: false
word_count: 203
summary: This document explains how to utilize IndexCache in vLLM to optimize DeepSeek-V3.2 models by caching and reusing top-k indices to reduce redundant computations.
tags:
    - vllm
    - deepseek
    - model-optimization
    - sparse-attention
    - index-cache
    - inference-performance
category: configuration
---

[](https://github.com/vllm-project/vllm/edit/main/docs/features/index_cache.md "Edit this page")

IndexCache reduces redundant top-k computation in DeepSeek-V3.2 (DSA) models by caching and reusing top-k indices across layers.

## Background[¶](#background "Permanent link")

DeepSeek-V3.2 uses a DeepSeek Sparse Attention (DSA) mechanism where top-k token selection is computed per layer. For deep models with many layers, this computation can be expensive. IndexCache allows skipping redundant top-k computations by reusing indices from previous layers.

See: [IndexCache Paper](https://arxiv.org/abs/2603.12201)

## Usage[¶](#usage "Permanent link")

### CLI[¶](#cli "Permanent link")

```
vllmservedeepseek-ai/DeepSeek-V3.2\
--hf-overrides'{"use_index_cache": true, "index_topk_freq": 4}'...
```

### Configuration Reference[¶](#configuration-reference "Permanent link")

Parameter Type Default Description `use_index_cache` bool false Enable IndexCache. Must be set to true to use this feature `index_topk_freq` int 1 Frequency (in layers) at which top-k is computed. 1 = compute on every layer (disabled), 4 = compute on 1/4 of layers `index_topk_pattern` str null Per-layer F/S pattern. Overrides index\_topk\_freq if set. Each character maps to one DSA layer: F = Full, S = Shared

### Configuration Examples[¶](#configuration-examples "Permanent link")

**Using `index_topk_freq`** (compute every N layers):

```
vllmservedeepseek-ai/DeepSeek-V3.2\
--hf-overrides'{"use_index_cache": true, "index_topk_freq": 4}'...
```

**Using `index_topk_pattern`** (explicit per-layer control):

```
# custom pattern for 61 layers: F = compute, S = reuse
vllmservedeepseek-ai/DeepSeek-V3.2\
--hf-overrides'{"use_index_cache": true, "index_topk_pattern": "FFSFSSSFSSFFFSSSFFFSFSSSSSSFFSFFSFFSSFFFFFFSFFFFFSFFSSSSSSFSF"}'
```

## How It Works[¶](#how-it-works "Permanent link")

1. When IndexCache is enabled, layers marked with `"F"` (Full) calculate and store top-k indices
2. Subsequent layers marked with `"S"` (Shared) receive the cached indices from the previous layer instead of recomputing
3. The cached indices are passed through the layer stack, reducing total computation

## Requirements[¶](#requirements "Permanent link")

- DeepSeek-V3.2 or compatible DSA model
- `use_index_cache: true` via `--hf-overrides`