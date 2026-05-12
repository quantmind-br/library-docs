---
title: Reproducibility - vLLM
url: https://docs.vllm.ai/en/latest/usage/reproducibility/
source: sitemap
fetched_at: 2026-05-07T21:15:30.856212836-03:00
rendered_js: false
word_count: 258
summary: This document details the configuration requirements and limitations for achieving deterministic, reproducible output results when using the vLLM inference engine.
tags:
    - vllm
    - reproducibility
    - random-seed
    - deterministic-inference
    - batch-invariance
    - model-output
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/usage/reproducibility.md "Edit this page")

vLLM does not guarantee the reproducibility of the results by default, for the sake of performance. To achieve reproducible results:

- In offline mode, you can either set `VLLM_ENABLE_V1_MULTIPROCESSING=0` which makes scheduling deterministic, or enable [batch invariance](https://docs.vllm.ai/en/latest/features/batch_invariance/) to make the outputs insensitive to scheduling.
- In online mode, you can only enable [batch invariance](https://docs.vllm.ai/en/latest/features/batch_invariance/).

Example: [examples/features/batch\_invariance/reproducibility\_offline.py](https://github.com/vllm-project/vllm/blob/main/examples/features/batch_invariance/reproducibility_offline.py)

Warning

Setting `VLLM_ENABLE_V1_MULTIPROCESSING=0` will change the random state of user code (i.e. the code that constructs [LLM](https://docs.vllm.ai/en/latest/api/vllm/#vllm.LLM "            LLM") class).

Note

Even with the above settings, vLLM only provides reproducibility when it runs on the same hardware and the same vLLM version.

## Setting the global seed[¶](#setting-the-global-seed "Permanent link")

The `seed` parameter in vLLM is used to control the random states for various random number generators.

If a specific seed value is provided, the random states for `random`, `np.random`, and `torch.manual_seed` will be set accordingly.

### Default Behavior[¶](#default-behavior "Permanent link")

In V1, the `seed` parameter defaults to `0` which sets the random state for each worker, so the results will remain consistent for each vLLM run even if `temperature > 0`.

It is impossible to un-specify a seed for V1 because different workers need to sample the same outputs for workflows such as speculative decoding. For more information, see: [Pull Request #17929](https://github.com/vllm-project/vllm/pull/17929)

Note

The random state in user code (i.e. the code that constructs [LLM](https://docs.vllm.ai/en/latest/api/vllm/#vllm.LLM "            LLM") class) is updated by vLLM only if the workers are run in the same process as user code, i.e.: `VLLM_ENABLE_V1_MULTIPROCESSING=0`.

By default, `VLLM_ENABLE_V1_MULTIPROCESSING=1` so you can use vLLM without having to worry about accidentally making deterministic subsequent operations that rely on random state.