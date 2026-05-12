---
title: create_txt_slices_dataset - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/benchmarks/datasets/create_txt_slices_dataset/
source: sitemap
fetched_at: 2026-05-07T21:15:45.329553934-03:00
rendered_js: false
word_count: 0
summary: This function converts raw text files into a JSONL format containing sliced prompts and output token lengths for machine learning benchmarking or training.
tags:
    - data-preprocessing
    - text-tokenization
    - dataset-generation
    - jsonl-conversion
    - prompt-engineering
category: api
---

```
defcreate_txt_slices_jsonl(
    *,
    input_path: str,
    output_path: str,
    tokenizer_name: str,
    num_prompts: int,
    input_len: int,
    output_len: int,
    range_ratio: RangeRatio = 0.0,
    seed: int = 0,
    trust_remote_code: bool = False,
) -> None:
"""Read *input_path*, slice it into prompts, and write JSONL to
    *output_path*."""

    tokenizer = AutoTokenizer.from_pretrained(
        tokenizer_name, trust_remote_code=trust_remote_code
    )

    text = load_text(input_path)
    if not text:
        raise ValueError("The text file is empty and cannot be sampled from.")

    token_ids = tokenizer(text, add_special_tokens=False).input_ids
    if not token_ids:
        raise ValueError("Tokenizing the text produced zero tokens; cannot sample.")

    rng_np = np.random.default_rng(seed)
    rng_py = random.Random(seed)

    input_lens, output_lens, _ = get_sampling_params(
        rng_np,
        num_prompts,
        range_ratio,
        input_len,
        output_len,
        tokenizer,
    )

    num_available_tokens = len(token_ids)

    records: list[dict[str, object]] = []
    for i in range(num_prompts):
        req_input_len = int(input_lens[i])
        req_output_len = int(output_lens[i])

        # Randomly select a start position and slice with cycling
        start_pos = rng_py.randint(0, num_available_tokens - 1)
        prompt_token_ids = [
            token_ids[(start_pos + j) % num_available_tokens]
            for j in range(req_input_len)
        ]
        prompt = tokenizer.decode(prompt_token_ids, skip_special_tokens=False)

        records.append({"prompt": prompt, "output_tokens": req_output_len})

    with open(output_path, "w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    logger.info(
        "Wrote %d prompts to %s",
        len(records),
        output_path,
    )
```