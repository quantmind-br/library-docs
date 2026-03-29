---
title: Choices Methods in SGLang — SGLang
url: https://docs.sglang.io/references/frontend/choices_methods.html
source: crawler
fetched_at: 2026-02-04T08:48:13.786303465-03:00
rendered_js: false
word_count: 251
summary: This document explains the different selection methods available for SGLang's choices primitive, detailing how each algorithm evaluates and selects options based on token probabilities.
tags:
    - sglang
    - choices-primitive
    - llm-inference
    - token-normalization
    - greedy-selection
    - unconditional-likelihood
category: reference
---

## Contents

## Choices Methods in SGLang[#](#choices-methods-in-sglang "Link to this heading")

This doc describes the choices methods supported by SGLang.

The optional `choices_method` arg determines how options supplied to SGLang’s `choices` primitive are selected. Only the `RuntimeEndpoint` backend supports the `choices_method` arg. Other backends, such as `OpenAI`, have bespoke selection implementations due to API limitations.

## Methods[#](#methods "Link to this heading")

### Token Length Normalized[#](#token-length-normalized "Link to this heading")

Token length normalized is the default SGLang choices method. It selects the option with the highest average logprob across all of its tokens.

Usage example (alternatively, simply omit the `choices_method` arg):

```
@sgl.function
defexample(s):
    s += sgl.user("What is the capital of France?")
    s += sgl.assistant(
        sgl.gen(
            "answer",
            choices=["London", "Paris", "Berlin"],
            choices_method=sgl.token_length_normalized,
        )
    )
```

This can perform poorly if an option contains many tokens, where its later tokens are predicted with high confidence based on its earlier tokens. For instance, even strong models will fail the above example if the specified options are `["Paris", "Antidisestablishmentarianism"]`.

### Greedy Token Selection[#](#greedy-token-selection "Link to this heading")

Greedy token selection simply selects the option with the highest logprob for its initial token. For overlapping options where one option is a subset of a longer option, the logprobs of the shorter option are extended using its average logprob for comparison against the longer option.

Usage example:

```
@sgl.function
defexample(s):
    s += sgl.user("What is the capital of France?")
    s += sgl.assistant(
        sgl.gen(
            "answer",
            choices=["London", "Paris", "Berlin"],
            choices_method=sgl.greedy_token_selection,
        )
    )
```

This can perform poorly if an option misleads the model down a bad path based on an attractive initial token. For instance, greedy selection will result in an incorrect response for this example:

```
@sgl.function
defus_president_example(s):
    s += sgl.user("Name a US president.")
    s += sgl.assistant(
        sgl.gen(
            "answer",
            choices=["Donald Duck", "Millard Fillmore"],
            choices_method=sgl.greedy_token_selection,
        )
    )
```

### Unconditional Likelihood Normalized[#](#unconditional-likelihood-normalized "Link to this heading")

Unconditional likelihood normalized selects the option with the highest average token logprob once normalized by the unconditional token logprobs, as described in [this EleutherAI blogpost](https://blog.eleuther.ai/multiple-choice-normalization/). This method incurs an additional LLM call to obtain the unconditional likelihoods.

Usage example:

```
@sgl.function
defexample(s):
    s += sgl.user("What is the capital of France?")
    s += sgl.assistant(
        sgl.gen(
            "answer",
            choices=["London", "Paris", "Berlin"],
            choices_method=sgl.unconditional_likelihood_normalized,
        )
    )
```