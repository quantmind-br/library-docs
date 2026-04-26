---
title: Fine-tuning API (legacy) | Mistral Docs
url: https://docs.mistral.ai/resources/deprecated/customization
source: sitemap
fetched_at: 2026-04-26T04:11:26.997723578-03:00
rendered_js: false
word_count: 1897
summary: This document outlines the development lifecycle for creating custom LLM applications, focusing on defining model behavior through system prompts, fine-tuning, and content moderation.
tags:
    - llm-customization
    - fine-tuning
    - system-prompt
    - model-alignment
    - content-moderation
    - llm-evaluation
    - application-development
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

> [!danger]
> This feature is deprecated and no longer actively supported.

## Overview

LLM applications are built around **human-AI collaboration**, requiring iterative development cycles with continuous end-user feedback and rigorous evals to align custom model behavior.

See [Fine-tuning examples](https://docs.mistral.ai/resources/cookbooks?useCase=Finetuning).

## Key Terms

- **Application behavior**: User interaction (usability, performance, safety, adaptability) — includes Objectives and Values
- **Model behavior**: Expected, appropriate, acceptable LLM acting in a specific context — includes Objectives and Values
- **Objectives**: Whether model behavior aligns with expected application behavior
- **Values**: Developer policy (rules, Constitution, fictional character morals)

## Steering Model Behavior

1. **System prompt**: Provide context and guidelines before user input
   - Include: clear instructions, persona/tone, style guidance, value definitions, output format
2. **Tune a model**: Train on intended application behavior
   - Application tuning: dataset of desired behavior examples
   - Safety tuning: dataset of unsafe inputs with safe outputs
3. **Deploy moderation layer**: Input/output classifier as extra security

## Build Process

### Step 1: Define Objectives

How you want users to interact with your LLM product:
- Standalone products (conversational assistants)
- Pre-existing products for specific tasks (Summarize, Translate, function calling with API access)

### Step 2: Identify Values

Content Moderation guidelines — see [Llama Guard](https://ai.meta.com/research/publications/llama-guard-llm-based-input-output-safeguard-for-human-ai-conversations/) and [ML Commons Taxonomy](https://drive.google.com/file/d/1V8KFfk8awaAXc83nZZzDV2bHgPT8jbJY/view) categories.

### Step 3: Create Evals

Two methods to evaluate LLMs:

| Method | Description |
|--------|-------------|
| **Automated - Metrics** | Derive metric from pre-annotated data |
| **Automated - LLM-based** | Use another LLM (e.g., Mistral Large) to judge output |
| **Human-based** | Content Annotators evaluate and collect annotations |

### Step 4: Test with Mistral Large

Test your application hypothesis with Mistral Large and collect interaction data (e.g., private beta).

### Step 5: Decide on Custom Model

If system prompt works, skip to Step 6. Otherwise:
- Use [fine-tuning guide](https://docs.mistral.ai/resources/deprecated/finetuning)
- Prepare tuning dataset considering:
  - **Data Comprehension**: Include content policies per use case
  - **Data Variety**: Diversity across query length, structure, tone, topic, complexity, demographics
  - **Deduplication**: Remove duplicates to prevent memorization
  - **Avoid Data Contamination**: Isolate evaluation data from training
  - **Ethical Data Practices**: Clear labeling guidelines, annotator diversity

### Step 6: Fine-tune

Mistral supports two customization methods:
1. **OSS**: [FT Codebase](https://github.com/mistralai/mistral-finetune/)
2. **AI Studio**: Upload/validate training data, run job, access via custom model API endpoint

### Step 7: Evaluate

Include Safety Evals:
- **Development Evals**: Ongoing during training, adversarial queries, academic benchmarks
- **Assurance Evals**: Governance at milestones by external group, standardized datasets
- **Red Teaming**: Adversarial testing by specialist teams
- **External Evals**: Independent domain experts for stress-testing

### Step 8: Deploy

Either retrain with new data or switch Mistral Large API for custom model endpoint.

### Step 9: Monitor

Continuously update custom model, evals, and testing based on real application data.

## Developer Examples

**Tak** ([phospho.ai](https://tak.phospho.ai/)): B2C internet search app powered by Mistral Large with RAG and function calling. Multiple agents chained with consistently formatted outputs.

**phospho** ([phospho.ai](https://phospho.ai/)): Open-source text analytics platform for LLM apps. Used user queries and GPT-4-turbo function calls to fine-tune Mistral 7B.

### phospho Fine-tuning Results

- **Dataset split**: 70% train, 15% eval, 15% test
- **Training duration**: ~150 steps (each token seen ~3 times)
- **Learning rate**: 6e-5

**Performance improvement**:
- F1 score increased from 20% to 78%
- Accuracy: 87% → 96%
- Recall: 20% → 90%
- Token reduction: 34% decrease (excluding user query)

Fine-tuning aligned Mistral 7B behavior with GPT-4-turbo while maintaining structured output and reducing costs. #llm-customization #fine-tuning #system-prompt #model-alignment