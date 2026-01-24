---
title: Output Refinement - DSPy
url: https://dspy.ai/tutorials/output_refinement/best-of-n-and-refine/
source: sitemap
fetched_at: 2026-01-23T08:04:14.344673095-03:00
rendered_js: false
word_count: 327
summary: This document explains how to use the BestOfN and Refine modules in DSPy to improve prediction quality through multiple model calls and iterative feedback loops.
tags:
    - dspy
    - output-refinement
    - reward-functions
    - llm-optimization
    - best-of-n
    - iterative-feedback
category: tutorial
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/tutorials/output_refinement/best-of-n-and-refine.md "Edit this page")

## Output Refinement: BestOfN and Refine[¶](#output-refinement-bestofn-and-refine "Permanent link")

Both `BestOfN` and `Refine` are DSPy modules designed to improve the reliability and quality of predictions by making multiple `LM` calls with different rollout IDs to bypass caching. Both modules stop when they have reached `N` attempts or when the `reward_fn` returns an award above the `threshold`.

## BestOfN[¶](#bestofn "Permanent link")

`BestOfN` is a module that runs the provided module multiple times (up to `N`) with different rollout IDs. It returns either the first prediction that passes a specified threshold or the one with the highest reward if none meets the threshold.

### Basic Usage[¶](#basic-usage "Permanent link")

Lets say we wanted to have the best chance of getting a one word answer from the model. We could use `BestOfN` to try multiple rollout IDs and return the best result.

```
importdspy

defone_word_answer(args, pred: dspy.Prediction) -> float:
    return 1.0 if len(pred.answer.split()) == 1 else 0.0

best_of_3 = dspy.BestOfN(
    module=dspy.ChainOfThought("question -> answer"), 
    N=3, 
    reward_fn=one_word_answer, 
    threshold=1.0
)

result = best_of_3(question="What is the capital of Belgium?")
print(result.answer)  # Brussels
```

### Error Handling[¶](#error-handling "Permanent link")

By default, if the module encounters an error during an attempt, it will continue trying until it reaches `N` attempts. You can adjust this behavior with the `fail_count` parameter:

```
best_of_3 = dspy.BestOfN(
    module=qa, 
    N=3, 
    reward_fn=one_word_answer, 
    threshold=1.0,
    fail_count=1
)

best_of_3(question="What is the capital of Belgium?")
# raises an error after the first failure
```

## Refine[¶](#refine "Permanent link")

`Refine` extends the functionality of `BestOfN` by adding an automatic feedback loop. After each unsuccessful attempt (except the final one), it automatically generates detailed feedback about the module's performance and uses this feedback as hints for subsequent runs.

### Basic Usage[¶](#basic-usage_1 "Permanent link")

```
importdspy

defone_word_answer(args, pred: dspy.Prediction) -> float:
    return 1.0 if len(pred.answer.split()) == 1 else 0.0

refine = dspy.Refine(
    module=dspy.ChainOfThought("question -> answer"), 
    N=3, 
    reward_fn=one_word_answer, 
    threshold=1.0
)

result = refine(question="What is the capital of Belgium?")
print(result.answer)  # Brussels
```

### Error Handling[¶](#error-handling_1 "Permanent link")

Like `BestOfN`, `Refine` will try up to `N` times by default, even if errors occur. You can control this with the `fail_count` parameter:

```
# Stop after the first error
refine = dspy.Refine(
    module=qa, 
    N=3, 
    reward_fn=one_word_answer, 
    threshold=1.0,
    fail_count=1
)
```

## Comparison: BestOfN vs. Refine[¶](#comparison-bestofn-vs-refine "Permanent link")

Both modules serve similar purposes but differ in their approach:

- `BestOfN` simply tries different rollout IDs and selects the best resulting prediction as defined by the `reward_fn`.
- `Refine` adds an feedback loop, using the lm to generate a detailed feedback about the module's own performance using the previous prediction and the code in the `reward_fn`. This feedback is then used as hints for subsequent runs.

## Practical Examples[¶](#practical-examples "Permanent link")

### Ensuring Factual Correctness[¶](#ensuring-factual-correctness "Permanent link")

```
importdspy

classFactualityJudge(dspy.Signature):
"""Determine if a statement is factually accurate."""
    statement: str = dspy.InputField()
    is_factual: bool = dspy.OutputField()

factuality_judge = dspy.ChainOfThought(FactualityJudge)

deffactuality_reward(args, pred: dspy.Prediction) -> float:
    statement = pred.answer    
    result = factuality_judge(statement)    
    return 1.0 if result.is_factual else 0.0

refined_qa = dspy.Refine(
    module=dspy.ChainOfThought("question -> answer"),
    N=3,
    reward_fn=factuality_reward,
    threshold=1.0
)

result = refined_qa(question="Tell me about Belgium's capital city.")
print(result.answer)
```

### Summarization - Controlling Response Length[¶](#summarization-controlling-response-length "Permanent link")

```
importdspy

defideal_length_reward(args, pred: dspy.Prediction) -> float:
"""
    Reward the summary for being close to 75 words with a tapering off for longer summaries.
    """
    word_count = len(pred.summary.split())
    distance = abs(word_count - 75)
    return max(0.0, 1.0 - (distance / 125))

optimized_summarizer = dspy.BestOfN(
    module=dspy.ChainOfThought("text -> summary"),
    N=50,
    reward_fn=ideal_length_reward,
    threshold=0.9
)

result = optimized_summarizer(
    text="[Long text to summarize...]"
)
print(result.summary)
```

## Migration from `dspy.Suggest` and `dspy.Assert`[¶](#migration-from-dspysuggest-and-dspyassert "Permanent link")

`BestOfN` and `Refine` are the replacements for `dspy.Suggest` and `dspy.Assert` as of DSPy 2.6.