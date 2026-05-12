---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/benchmarks/datasets/utils/
source: sitemap
fetched_at: 2026-05-07T21:15:46.958567638-03:00
rendered_js: false
word_count: 9
summary: This function calculates and samples randomized input lengths, output lengths, and vocabulary offsets for a batch of requests based on a provided configuration and tokenizer.
tags:
    - python-function
    - random-sampling
    - token-length
    - data-generation
    - tokenizer-integration
category: reference
---

```
defget_sampling_params(
    rng: np.random.Generator,
    num_requests: int,
    range_ratio: RangeRatio,
    input_len: int,
    output_len: int,
    tokenizer: TokenizerLike,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
"""
    Sample per-request input/output token lengths and vocab offsets.

    Lengths are drawn uniformly from integer ranges around the configured
    means, controlled by *range_ratio*.  It may be a single ``float``
    (applied to both input and output) or a ``dict`` with ``"input"`` and
    ``"output"`` keys for independent control.

    Tokenizer special tokens are subtracted from ``input_len`` before
    computing the sampling interval.

    Returns:
        (input_lens, output_lens, offsets) – three 1-D ``np.ndarray`` of
        shape ``(num_requests,)``.
    """
    input_range_ratio, output_range_ratio = _resolve_range_ratios(range_ratio)

    if not (0.0 <= input_range_ratio < 1.0):
        raise ValueError("input_range_ratio must be in [0, 1).")
    if not (0.0 <= output_range_ratio < 1.0):
        raise ValueError("output_range_ratio must be in [0, 1).")
    num_special_tokens = int(tokenizer.num_special_tokens_to_add())
    real_input_len = max(0, int(input_len) - num_special_tokens)
    input_low = math.floor(real_input_len * (1 - input_range_ratio))
    input_high = math.ceil(real_input_len * (1 + input_range_ratio))
    output_low = math.floor(output_len * (1 - output_range_ratio))
    output_high = math.ceil(output_len * (1 + output_range_ratio))
    # Ensure the lower bound for output length is at least 1 to
    # prevent sampling 0 tokens.
    output_low = max(output_low, 1)
    output_high = max(output_high, 1)

    if input_low > input_high:
        raise ValueError(
            f"Invalid input sampling interval: low={input_low} > high={input_high}"
        )
    if output_low > output_high:
        raise ValueError(
            f"Invalid output sampling interval: low={output_low} > high={output_high}"
        )

    logger.info(
        "Sampling input_len from [%s, %s] and output_len from [%s, %s]",
        input_low,
        input_high,
        output_low,
        output_high,
    )

    input_lens = rng.integers(input_low, input_high + 1, size=num_requests)
    output_lens = rng.integers(output_low, output_high + 1, size=num_requests)
    offsets = rng.integers(0, tokenizer.vocab_size, size=num_requests)
    return input_lens, output_lens, offsets
```