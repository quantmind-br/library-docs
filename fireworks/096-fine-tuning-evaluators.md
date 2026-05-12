---
title: Evaluators - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/evaluators
source: sitemap
fetched_at: 2026-04-27T20:18:39.462848231-03:00
rendered_js: false
word_count: 383
summary: This document explains the concept of an evaluator (or reward function) used in reinforcement fine-tuning, detailing its role in guiding model outputs toward desired quality. It further breaks down evaluators into components, types, and best practices for implementation.
tags:
    - evaluator-function
    - reinforcement-learning
    - model-scoring
    - llm-judging
    - fine-tuning-guide
category: concept
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
An evaluator (also called a reward function) is code that scores model outputs from 0.0 (worst) to 1.0 (best). During reinforcement fine-tuning, your evaluator guides the model toward better responses by providing feedback on its generated outputs.

## Why evaluators matter

Unlike supervised fine-tuning where you provide perfect examples, RFT uses evaluators to define what "good" means:

- **No perfect data required** — Just prompts and a way to score outputs
- **Encourages exploration** — Models learn strategies, not just patterns
- **Noise tolerant** — Even noisy signals can improve model performance
- **Encodes domain expertise** — Complex rules and logic that are hard to demonstrate with examples

## Anatomy of an evaluator

Every evaluator has three core components:

### 1. Input data

The prompt and any ground truth data needed for evaluation:

```json
{
  "messages": [
    {"role": "system", "content": "You are a math tutor."},
    {"role": "user", "content": "What is 15 * 23?"}
  ],
  "ground_truth": "345"
}
```

### 2. Model output

The assistant's response to evaluate:

```json
{
  "role": "assistant",
  "content": "Let me calculate that step by step:\n15 * 23 = 345"
}
```

### 3. Scoring logic

Code that compares the output to your criteria:

```python
def evaluate(model_output: str, ground_truth: str) -> float:
    predicted = extract_number(model_output)
    if predicted == int(ground_truth):
        return 1.0  # Perfect
    else:
        return 0.0  # Wrong
```

## Types of evaluators

### Rule-based evaluators
Check if outputs match specific patterns or rules:
- **Exact match** — Output exactly equals expected value
- **Contains** — Output includes required text
- **Regex** — Output matches a pattern
- **Format validation** — Output follows required structure (e.g., valid JSON)

### Execution-based evaluators
Run code or commands to verify correctness:
- **Code execution** — Run generated code and check results
- **Test suites** — Pass generated code through unit tests
- **API calls** — Execute commands and verify outcomes
- **Simulations** — Run agents in environments and measure success

### LLM-as-judge evaluators
Use another model to evaluate quality:
- **Rubric scoring** — Judge outputs against criteria
- **Comparative ranking** — Compare multiple outputs
- **Natural language assessment** — Evaluate subjective qualities like helpfulness

## Scoring guidelines

| Score range | Meaning | Example |
|---|---|---|
| 1.0 | Perfect | Exact correct answer |
| 0.7–0.9 | Good | Right approach, minor error |
| 0.4–0.6 | Partial | Some correct elements |
| 0.1–0.3 | Poor | Wrong but attempted |
| 0.0 | Failure | Completely wrong |

## Best practices

Test your evaluator before training. Look for:
- **Correct scoring** — Good outputs score high, bad outputs score low
- **Reasonable runtime** — Each evaluation completes in reasonable time
- **Clear feedback** — Evaluation reasons explain scores
