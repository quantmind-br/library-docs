---
title: Unit Testing - vLLM
url: https://docs.vllm.ai/en/latest/contributing/model/tests/
source: sitemap
fetched_at: 2026-05-07T21:11:30.792842643-03:00
rendered_js: false
word_count: 318
summary: This document outlines the requirements and procedures for implementing unit tests for new models contributed to the vLLM library, covering both mandatory loading tests and optional correctness validation.
tags:
    - vllm
    - unit-testing
    - model-contribution
    - model-verification
    - hugging-face
    - testing-framework
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/contributing/model/tests.md "Edit this page")

This page explains how to write unit tests to verify the implementation of your model.

## Required Tests[¶](#required-tests "Permanent link")

These tests are necessary to get your PR merged into vLLM library. Without them, the CI for your PR will fail.

### Model loading[¶](#model-loading "Permanent link")

Include an example HuggingFace repository for your model in [tests/models/registry.py](https://github.com/vllm-project/vllm/blob/main/tests/models/registry.py). This enables a unit test that loads dummy weights to ensure that the model can be initialized in vLLM.

Important

The list of models in each section should be maintained in alphabetical order.

Tip

If your model requires a development version of HF Transformers, you can set `min_transformers_version` to skip the test in CI until the model is released.

## Optional Tests[¶](#optional-tests "Permanent link")

These tests are optional to get your PR merged into vLLM library. Passing these tests provides more confidence that your implementation is correct, and helps avoid future regressions.

### Model correctness[¶](#model-correctness "Permanent link")

These tests compare the model outputs of vLLM against [HF Transformers](https://github.com/huggingface/transformers). You can add new tests under the subdirectories of [tests/models](https://github.com/vllm-project/vllm/tree/main/tests/models).

#### Generative models[¶](#generative-models "Permanent link")

For [generative models](https://docs.vllm.ai/en/latest/models/generative_models/), there are two levels of correctness tests, as defined in [tests/models/utils.py](https://github.com/vllm-project/vllm/blob/main/tests/models/utils.py):

- Exact correctness (`check_outputs_equal`): The text outputted by vLLM should exactly match the text outputted by HF.
- Logprobs similarity (`check_logprobs_close`): The logprobs outputted by vLLM should be in the top-k logprobs outputted by HF, and vice versa.

#### Pooling models[¶](#pooling-models "Permanent link")

For [pooling models](https://docs.vllm.ai/en/latest/models/pooling_models/), we simply check the cosine similarity, as defined in [tests/models/utils.py](https://github.com/vllm-project/vllm/blob/main/tests/models/utils.py).

### Multi-modal processing[¶](#multi-modal-processing "Permanent link")

#### Common tests[¶](#common-tests "Permanent link")

Adding your model to [tests/models/multimodal/processing/test\_common.py](https://github.com/vllm-project/vllm/blob/main/tests/models/multimodal/processing/test_common.py) verifies that the following input combinations result in the same outputs:

- Text + multi-modal data
- Tokens + multi-modal data
- Text + cached multi-modal data
- Tokens + cached multi-modal data

#### Model-specific tests[¶](#model-specific-tests "Permanent link")

You can add a new file under [tests/models/multimodal/processing](https://github.com/vllm-project/vllm/tree/main/tests/models/multimodal/processing) to run tests that only apply to your model.

For example, if the HF processor for your model accepts user-specified keyword arguments, you can verify that the keyword arguments are being applied correctly, such as in [tests/models/multimodal/processing/test\_phi3v.py](https://github.com/vllm-project/vllm/blob/main/tests/models/multimodal/processing/test_phi3v.py).