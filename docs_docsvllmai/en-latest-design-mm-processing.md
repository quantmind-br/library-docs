---
title: Multi-Modal Data Processing - vLLM
url: https://docs.vllm.ai/en/latest/design/mm_processing/
source: sitemap
fetched_at: 2026-05-07T21:12:22.755633543-03:00
rendered_js: false
word_count: 616
summary: This document explains the design and implementation of the BaseMultiModalProcessor in vLLM, detailing how it handles prompt updates, tokenized inputs, and performance optimizations through result caching.
tags:
    - vllm
    - multi-modal
    - data-processing
    - prompt-engineering
    - tokenization
    - caching
    - hugging-face
category: concept
---

[](https://github.com/vllm-project/vllm/edit/main/docs/design/mm_processing.md "Edit this page")

To enable various optimizations in vLLM such as [chunked prefill](https://docs.vllm.ai/en/latest/configuration/optimization/#chunked-prefill) and [prefix caching](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/), we use [BaseMultiModalProcessor](https://docs.vllm.ai/en/latest/api/vllm/multimodal/processing/#vllm.multimodal.processing.BaseMultiModalProcessor "            BaseMultiModalProcessor") to provide the correspondence between placeholder feature tokens (e.g. `<image>`) and multi-modal inputs (e.g. the raw input image) based on the outputs of HF processor.

Here are the main features of [BaseMultiModalProcessor](https://docs.vllm.ai/en/latest/api/vllm/multimodal/processing/#vllm.multimodal.processing.BaseMultiModalProcessor "            BaseMultiModalProcessor"):

## Prompt Update Detection[¶](#prompt-update-detection "Permanent link")

One of the main responsibilities of HF processor is to update the prompt with placeholder tokens. For example:

- Insert feature placeholder tokens (e.g. `<image><image>...<image>`, the number of which equals to the feature size) at the start of the string.
- Replace existing input placeholder tokens (e.g. `<image>` for a single image) with feature placeholder tokens (e.g. `<image><image>...<image>`, the number of which equals to the feature size).

The information about which tokens have been updated is key to finding the correspondence between placeholder feature tokens and multi-modal inputs.

In vLLM, this information is specified using [PromptUpdate](https://docs.vllm.ai/en/latest/api/vllm/multimodal/processing/#vllm.multimodal.processing.PromptUpdate "            PromptUpdate            dataclass   ") in [\_get\_prompt\_updates](https://docs.vllm.ai/en/latest/api/vllm/multimodal/processing/#vllm.multimodal.processing.BaseMultiModalProcessor._get_prompt_updates "            _get_prompt_updates            abstractmethod   "). We can automatically detect whether HF has updated the prompt by checking the existence of the updated tokens.

## Tokenized Prompt Inputs[¶](#tokenized-prompt-inputs "Permanent link")

To enable tokenization in a separate process, we support passing input token IDs alongside multi-modal data.

### The problem[¶](#the-problem "Permanent link")

Consider that HF processors follow these main steps:

1. Tokenize the text
2. Process multi-modal inputs
3. Perform prompt updates

And we require that:

- For text + multi-modal inputs, apply all steps 1--3.
- For tokenized + multi-modal inputs, apply only steps 2--3.

How can we achieve this without rewriting HF processors? We can try to call the HF processor several times on different inputs:

- For text + multi-modal inputs, simply call the HF processor directly.
- For tokenized + multi-modal inputs, call the processor only on the multi-modal inputs.

While HF processors support text + multi-modal inputs natively, this is not so for tokenized + multi-modal inputs: an error is thrown if the number of input placeholder tokens do not correspond to the number of multi-modal inputs.

Moreover, since the tokenized text has not passed through the HF processor, we have to apply Step 3 by ourselves to keep the output tokens and multi-modal data consistent with each other.

### Dummy text[¶](#dummy-text "Permanent link")

We work around the first issue by requiring each model to define how to generate dummy text based on the number of multi-modal inputs, via [get\_dummy\_text](https://docs.vllm.ai/en/latest/api/vllm/multimodal/processing/#vllm.multimodal.processing.BaseDummyInputsBuilder.get_dummy_text "            get_dummy_text            abstractmethod   "). This lets us generate dummy text corresponding to the multi-modal inputs and input them together to obtain the processed multi-modal data.

### Automatic prompt updating[¶](#automatic-prompt-updating "Permanent link")

We address the second issue by implementing model-agnostic code in [\_apply\_prompt\_updates](https://docs.vllm.ai/en/latest/api/vllm/multimodal/processing/#vllm.multimodal.processing.BaseMultiModalProcessor._apply_prompt_updates "            _apply_prompt_updates") to automatically update the prompt with feature placeholder tokens based on the specification outputted by [\_get\_prompt\_updates](https://docs.vllm.ai/en/latest/api/vllm/multimodal/processing/#vllm.multimodal.processing.BaseMultiModalProcessor._get_prompt_updates "            _get_prompt_updates            abstractmethod   ").

### Summary[¶](#summary "Permanent link")

With the help of dummy text and automatic prompt updating, our multi-modal processor can finally accept both text and token prompts with multi-modal data. The detailed logic is shown in [\_apply\_hf\_processor\_main](https://docs.vllm.ai/en/latest/api/vllm/multimodal/processing/#vllm.multimodal.processing.BaseMultiModalProcessor._apply_hf_processor_main "            _apply_hf_processor_main").

## Processor Output Caching[¶](#processor-output-caching "Permanent link")

Some HF processors, such as the one for Qwen2-VL, are [very slow](https://github.com/vllm-project/vllm/issues/9238). To alleviate this problem, we cache the multi-modal outputs of HF processor to avoid processing the same multi-modal input (e.g. image) again.

When new data is passed in, we first check which items are in the cache, and which ones are missing. The missing items are passed into the HF processor in a single batch and cached, before being merged with the existing items in the cache.

Since we only process the missing multi-modal data items, the number of input placeholder tokens no longer corresponds to the number of the multi-modal inputs, so they can't be passed alongside the text prompt to HF processor. Therefore, we process the text and multi-modal inputs separately, using [dummy text](#dummy-text) to avoid HF errors. Since this skips HF's prompt updating code, we apply [automatic prompt updating](#automatic-prompt-updating) afterwards to keep the output tokens and multi-modal data consistent with each other.