---
title: beam_search - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/beam_search/
source: sitemap
fetched_at: 2026-05-07T21:15:41.998137105-03:00
rendered_js: false
word_count: 157
summary: This document defines the data structures and utility functions used for implementing beam search in the vLLM library, specifically handling sequence tracking and score calculation.
tags:
    - beam-search
    - dataclass
    - sequence-tracking
    - log-probability
    - vllm
    - generation-strategy
category: reference
---

## BeamSearchOutput `dataclass` [¶](#vllm.beam_search.BeamSearchOutput "Permanent link")

The output of beam search. It contains the list of the best beam search sequences. The length of the list is equal to the beam width.

Source code in `vllm/beam_search.py`

```
@dataclass
classBeamSearchOutput:
"""The output of beam search.
    It contains the list of the best beam search sequences.
    The length of the list is equal to the beam width.
    """

    sequences: list[BeamSearchSequence]
```

## BeamSearchSequence `dataclass` [¶](#vllm.beam_search.BeamSearchSequence "Permanent link")

A sequence for beam search. It keeps track of the tokens and the log probability of the sequence. The text field is optional and will only be filled when the sequence is about to be returned to the user.

Source code in `vllm/beam_search.py`

```
@dataclass
classBeamSearchSequence:
"""A sequence for beam search.
    It keeps track of the tokens and the log probability of the sequence.
    The text field is optional and will only be filled when the sequence is
    about to be returned to the user.
    """

    orig_prompt: TokensInput | MultiModalInput | EncoderDecoderInput

    # NOTE: Tokens represents decoder tokens in the encoder / decoder case
    tokens: list[int]
    logprobs: list[dict[int, Logprob]]
    lora_request: LoRARequest | None = None
    cum_logprob: float = 0.0
    text: str | None = None
    finish_reason: str | None = None
    stop_reason: int | str | None = None

    defget_prompt(self):
        prompt = self.orig_prompt

        if prompt["type"] == "enc_dec":
            return self._build_encoder_decoder_inputs(prompt)

        # Handle decoder-only inputs
        prompt_text = prompt.get("prompt")
        cache_salt = prompt.get("cache_salt")

        if prompt["type"] == "token":
            return tokens_input(
                self.tokens,
                prompt=prompt_text,
                cache_salt=cache_salt,
            )

        return mm_input(
            prompt_token_ids=self.tokens,
            mm_kwargs=prompt["mm_kwargs"],
            mm_hashes=prompt["mm_hashes"],
            mm_placeholders=prompt["mm_placeholders"],
            prompt=prompt_text,
            cache_salt=cache_salt,
        )

    def_build_encoder_decoder_inputs(
        self, prompt: EncoderDecoderInput
    ) -> EncoderDecoderInput:
"""Rebuild the encoder-decoder inputs with the current beam search
        sequence's tokens.

        FIXME (alex) - the encoder multimodal cache is not properly wired up
        yet, which means that currently we are running the encoder on every
        new beam because num_computed_tokens is 0 on each new request. This
        will be fixed once the cache is correctly implemented.
        """
        dec_prompt = prompt["decoder_prompt"]

        # Rebuild decoder prompt with updated tokens,
        # but keep everything else the same.
        new_dec_prompt: DecoderOnlyEngineInput
        if dec_prompt["type"] == "multimodal":
            new_dec_prompt = mm_input(
                self.tokens,
                mm_kwargs=dec_prompt["mm_kwargs"],
                mm_hashes=dec_prompt["mm_hashes"],
                mm_placeholders=dec_prompt["mm_placeholders"],
                prompt=dec_prompt.get("prompt"),
                cache_salt=dec_prompt.get("cache_salt"),
            )
        else:
            new_dec_prompt = tokens_input(
                self.tokens,
                prompt=dec_prompt.get("prompt"),
                cache_salt=dec_prompt.get("cache_salt"),
            )

        return EncoderDecoderInput(
            type="enc_dec",
            encoder_prompt=prompt["encoder_prompt"],
            decoder_prompt=new_dec_prompt,
        )
```

### \_build\_encoder\_decoder\_inputs [¶](#vllm.beam_search.BeamSearchSequence._build_encoder_decoder_inputs "Permanent link")

Rebuild the encoder-decoder inputs with the current beam search sequence's tokens.

FIXME (alex) - the encoder multimodal cache is not properly wired up yet, which means that currently we are running the encoder on every new beam because num\_computed\_tokens is 0 on each new request. This will be fixed once the cache is correctly implemented.

Source code in `vllm/beam_search.py`

```
def_build_encoder_decoder_inputs(
    self, prompt: EncoderDecoderInput
) -> EncoderDecoderInput:
"""Rebuild the encoder-decoder inputs with the current beam search
    sequence's tokens.

    FIXME (alex) - the encoder multimodal cache is not properly wired up
    yet, which means that currently we are running the encoder on every
    new beam because num_computed_tokens is 0 on each new request. This
    will be fixed once the cache is correctly implemented.
    """
    dec_prompt = prompt["decoder_prompt"]

    # Rebuild decoder prompt with updated tokens,
    # but keep everything else the same.
    new_dec_prompt: DecoderOnlyEngineInput
    if dec_prompt["type"] == "multimodal":
        new_dec_prompt = mm_input(
            self.tokens,
            mm_kwargs=dec_prompt["mm_kwargs"],
            mm_hashes=dec_prompt["mm_hashes"],
            mm_placeholders=dec_prompt["mm_placeholders"],
            prompt=dec_prompt.get("prompt"),
            cache_salt=dec_prompt.get("cache_salt"),
        )
    else:
        new_dec_prompt = tokens_input(
            self.tokens,
            prompt=dec_prompt.get("prompt"),
            cache_salt=dec_prompt.get("cache_salt"),
        )

    return EncoderDecoderInput(
        type="enc_dec",
        encoder_prompt=prompt["encoder_prompt"],
        decoder_prompt=new_dec_prompt,
    )
```

## get\_beam\_search\_score [¶](#vllm.beam_search.get_beam_search_score "Permanent link")

```
get_beam_search_score(
    tokens: list[int],
    cumulative_logprob: float,
    eos_token_id: int,
    length_penalty: float = 1.0,
) -> float
```

Calculate the beam search score with length penalty.

Adapted from

https://github.com/huggingface/transformers/blob/ccb92be23def445f2afdea94c31286f84b89eb5b/src/transformers/generation/beam\_search.py#L938

Source code in `vllm/beam_search.py`

```
defget_beam_search_score(
    tokens: list[int],
    cumulative_logprob: float,
    eos_token_id: int,
    length_penalty: float = 1.0,
) -> float:
"""Calculate the beam search score with length penalty.

    Adapted from

    https://github.com/huggingface/transformers/blob/ccb92be23def445f2afdea94c31286f84b89eb5b/src/transformers/generation/beam_search.py#L938
    """
    seq_len = len(tokens)
    if tokens[-1] == eos_token_id:
        seq_len -= 1

    return cumulative_logprob / (seq_len**length_penalty)
```