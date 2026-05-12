---
title: Basics - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/how-rft-works
source: sitemap
fetched_at: 2026-04-27T20:18:39.333160966-03:00
rendered_js: false
word_count: 229
summary: This document explains reinforcement fine-tuning, which involves training an LLM using a dataset of prompts and a reward function (evaluator) to maximize output quality without relying solely on labeled examples.
tags:
    - reinforcement-fine-tuning
    - llm-training
    - reward-function
    - agent-learning
    - model-optimization
category: concept
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
## What is reinforcement fine-tuning?

In traditional supervised fine-tuning, you provide a dataset with labeled examples showing exactly what the model should output. In reinforcement fine-tuning, you instead provide:

1. **A dataset** — Prompts for the model to respond to
2. **An evaluator** — Code that scores the model's outputs from 0.0 (bad) to 1.0 (good), also known as a reward function
3. **An agent** — An LLM application with access to tools, APIs, and data needed for your task

During training, the model generates responses to each prompt, receives scores from your reward function, and produces outputs that maximize the reward.

## Use cases

Reinforcement fine-tuning helps train models to excel at:

- **Code generation and analysis** — Writing and debugging functions with verifiable execution results
- **Structured output generation** — JSON formatting, data extraction, classification with programmatic validation
- **Domain-specific reasoning** — Legal analysis, financial modeling, medical triage with verifiable criteria
- **Tool-using agents** — Multi-step workflows where agents call external APIs with measurable success criteria

## How it works

RFT works best when:
1. You can determine whether a model's output is "good" or "bad," even if only approximately
2. You have prompts but lack perfect "golden" completions to learn from
3. The task requires multi-step reasoning where evaluating intermediate steps is hard
4. You want the model to explore creative solutions beyond your training examples
