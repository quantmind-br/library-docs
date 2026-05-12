---
title: RL Reward Hacking
url: https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/advanced-rl-documentation/rl-reward-hacking.md
source: llms
fetched_at: 2026-04-27T18:13:17.289600077-03:00
rendered_js: false
word_count: 417
summary: This document explains 'Reward Hacking' in Reinforcement Learning (RL), which occurs when an algorithm exploits flaws to maximize rewards without actually accomplishing the task. It also outlines various methods and strategies for countering this behavior.
tags:
    - reward-hacking
    - reinforcement-learning
    - rl-concepts
    - agent-behavior
    - model-exploitation
    - rl-techniques
category: concept
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# RL Reward Hacking

RL aims to maximize a reward metric, but the algorithm can learn tricks or exploit flaws to inflate the reward without accomplishing the actual task. This is **Reward Hacking**. It causes models to modify unit tests to pass coding challenges and is a critical blocker for real-world deployment. More examples: [Wikipedia](https://en.wikipedia.org/wiki/Reward_hacking).

## Countering Reward Hacking

In the [free gpt-oss RL notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-\(20B\)-GRPO.ipynb), countermeasures for code generation reward hacking are explored. The model was observed editing the timing function, outsourcing to other libraries, caching results, and outright cheating. After applying countermeasures, the model generates genuinely optimized matrix multiplication kernels.

## Common Reward Hacking Patterns

### Laziness

RL learns to call Numpy, Torch, or other libraries that invoke optimized CUDA kernels, bypassing the actual task.

**Counter:** Inspect generated code for imports of non-standard Python libraries and reject them.

### Caching & Cheating

RL caches output or inspects Python global variables to find the actual answer.

**Counter:** Wipe the cache with a large fake matrix. Benchmark carefully with multiple loops and turns.

### Cheating (Timing Manipulation)

RL edits the timing function to output 0 elapsed time, or accesses global/cached variables.

**Counter:**
- Restrict `locals` and `globals`
- Use `exec` to create the function and save output to an empty dict
- Disallow global variable access via `types.FunctionType(f.__code__, {})`

#reward-hacking #reinforcement-learning #rl-concepts
