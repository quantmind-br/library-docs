---
title: Token Classify - vLLM
url: https://docs.vllm.ai/en/latest/examples/pooling/token_classify/
source: sitemap
fetched_at: 2026-05-07T21:13:32.090130623-03:00
rendered_js: false
word_count: 174
summary: This document provides examples for using the vLLM pooling API to perform token classification tasks, including offline forced alignment, offline named entity recognition (NER), and online NER via HTTP requests.
tags:
    - vllm
    - pooling-api
    - token-classification
    - named-entity-recognition
    - forced-alignment
    - multimodal
    - inference
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/pooling/token_classify.md "Edit this page")

Source [https://github.com/vllm-project/vllm/tree/main/examples/pooling/token\_classify](https://github.com/vllm-project/vllm/tree/main/examples/pooling/token_classify).

## Forced Alignment Offline[¶](#forced-alignment-offline "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
# Adapted from Qwen3-ForcedAligner inference:
# https://github.com/QwenLM/Qwen3-ASR

"""
Offline forced alignment example using Qwen3-ForcedAligner-0.6B.

Forced alignment takes audio and reference text as input and produces
word-level timestamps. The model predicts a time bin at each <timestamp>
token position; multiplying by ``timestamp_segment_time`` gives milliseconds.

Usage::

    python forced_alignment_offline.py \
        --model Qwen/Qwen3-ForcedAligner-0.6B
"""

fromargparseimport Namespace

importnumpyasnp

fromvllmimport LLM, EngineArgs
fromvllm.utils.argparse_utilsimport FlexibleArgumentParser


defparse_args():
    parser = FlexibleArgumentParser()
    parser = EngineArgs.add_cli_args(parser)
    parser.set_defaults(
        model="Qwen/Qwen3-ForcedAligner-0.6B",
        runner="pooling",
        enforce_eager=True,
        hf_overrides={"architectures": ["Qwen3ASRForcedAlignerForTokenClassification"]},
    )
    return parser.parse_args()


defbuild_prompt(words: list[str]) -> str:
"""Build the forced alignment prompt from a word list.

    Format: <|audio_start|><|audio_pad|><|audio_end|>
            word1<timestamp><timestamp>word2<timestamp><timestamp>...
    """
    body = "<timestamp><timestamp>".join(words) + "<timestamp><timestamp>"
    return f"<|audio_start|><|audio_pad|><|audio_end|>{body}"


defmain(args: Namespace):
    llm = LLM(**vars(args))

    config = llm.llm_engine.vllm_config.model_config.hf_config
    timestamp_token_id = config.timestamp_token_id
    timestamp_segment_time = config.timestamp_segment_time

    # Example: align these words against a 5-second audio clip
    words = ["Hello", "world"]
    prompt = build_prompt(words)

    # Use a 5-second silent audio as placeholder (replace with real audio)
    sample_rate = 16000
    audio = np.zeros(sample_rate * 5, dtype=np.float32)

    outputs = llm.encode(
        [{"prompt": prompt, "multi_modal_data": {"audio": audio}}],
        pooling_task="token_classify",
    )

    for output in outputs:
        logits = output.outputs.data  # [num_tokens, classify_num]
        predictions = logits.argmax(dim=-1)
        token_ids = output.prompt_token_ids

        # Extract timestamps at <timestamp> positions
        ts_predictions = [
            pred.item() * timestamp_segment_time
            for tid, pred in zip(token_ids, predictions)
            if tid == timestamp_token_id
        ]

        # Pair up start/end times per word
        for i, word in enumerate(words):
            start_ms = ts_predictions[i * 2]
            end_ms = ts_predictions[i * 2 + 1]
            print(f"{word:15s}{start_ms/1000:.3f}s - {end_ms/1000:.3f}s")


if __name__ == "__main__":
    args = parse_args()
    main(args)
```

## NER Offline[¶](#ner-offline "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
# Adapted from https://huggingface.co/boltuix/NeuroBERT-NER

fromargparseimport Namespace

fromvllmimport LLM, EngineArgs
fromvllm.utils.argparse_utilsimport FlexibleArgumentParser


defparse_args():
    parser = FlexibleArgumentParser()
    parser = EngineArgs.add_cli_args(parser)
    # Set example specific arguments
    parser.set_defaults(
        model="boltuix/NeuroBERT-NER",
        runner="pooling",
        enforce_eager=True,
        trust_remote_code=True,
    )
    return parser.parse_args()


defmain(args: Namespace):
    # Sample prompts.
    prompts = [
        "Barack Obama visited Microsoft headquarters in Seattle on January 2025."
    ]

    # Create an LLM.
    llm = LLM(**vars(args))
    tokenizer = llm.get_tokenizer()
    label_map = llm.llm_engine.vllm_config.model_config.hf_config.id2label

    # Run inference
    outputs = llm.encode(prompts, pooling_task="token_classify")

    for prompt, output in zip(prompts, outputs):
        logits = output.outputs.data
        predictions = logits.argmax(dim=-1)

        # Map predictions to labels
        tokens = tokenizer.convert_ids_to_tokens(output.prompt_token_ids)
        labels = [label_map[p.item()] for p in predictions]

        # Print results
        for token, label in zip(tokens, labels):
            if token not in tokenizer.all_special_tokens:
                print(f"{token:15} → {label}")


if __name__ == "__main__":
    args = parse_args()
    main(args)
```

## NER Online[¶](#ner-online "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
# Adapted from https://huggingface.co/boltuix/NeuroBERT-NER

"""
Example online usage of Pooling API for Named Entity Recognition (NER).

Run `vllm serve <model> --runner pooling`
to start up the server in vLLM. e.g.

vllm serve boltuix/NeuroBERT-NER
"""

importargparse

importrequests
importtorch


defpost_http_request(prompt: dict, api_url: str) -> requests.Response:
    headers = {"User-Agent": "Test Client"}
    response = requests.post(api_url, headers=headers, json=prompt)
    return response


defparse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="localhost")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--model", type=str, default="boltuix/NeuroBERT-NER")

    return parser.parse_args()


defmain(args):
    fromtransformersimport AutoConfig, AutoTokenizer

    api_url = f"http://{args.host}:{args.port}/pooling"
    model_name = args.model

    # Load tokenizer and config
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    config = AutoConfig.from_pretrained(model_name)
    label_map = config.id2label

    # Input text
    text = "Barack Obama visited Microsoft headquarters in Seattle on January 2025."
    prompt = {"model": model_name, "input": text}

    pooling_response = post_http_request(prompt=prompt, api_url=api_url)

    # Run inference
    output = pooling_response.json()["data"][0]
    logits = torch.tensor(output["data"])
    predictions = logits.argmax(dim=-1)
    inputs = tokenizer(text, return_tensors="pt")

    # Map predictions to labels
    tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
    labels = [label_map[p.item()] for p in predictions]
    assert len(tokens) == len(predictions)

    # Print results
    for token, label in zip(tokens, labels):
        if token not in tokenizer.all_special_tokens:
            print(f"{token:15} → {label}")


if __name__ == "__main__":
    args = parse_args()
    main(args)
```