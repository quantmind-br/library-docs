---
title: Test a model in the API playground | Mistral Docs
url: https://docs.mistral.ai/getting-started/quickstarts/studio/test-model-playground
source: sitemap
fetched_at: 2026-04-26T04:07:27.258056828-03:00
rendered_js: false
word_count: 353
summary: This document explains how to use the Mistral Studio playground to test prompts, tune generation parameters, and compare performance across different AI models.
tags:
    - model-evaluation
    - prompt-testing
    - hyperparameter-tuning
    - mistral-studio
    - generative-ai
category: tutorial
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Use the [Studio playground](https://console.mistral.ai) to send prompts to Mistral models, adjust generation parameters, and compare outputs — no code required.

**What you can do:**
- **Interactive testing**: type a prompt, get a response in seconds
- **Model comparison**: switch between models to see output differences
- **Parameter tuning**: adjust temperature, max tokens, and other settings in real time

**Time to complete:** ~5 minutes

**Prerequisites:** Active Studio account with Experiment or Scale plan. Complete [Activate Studio and generate an API key](https://docs.mistral.ai/getting-started/quickstarts/studio/activate-and-generate-api-key) first if needed.

## Steps

1. Go to [Studio](https://console.mistral.ai) → click **Playground** in the left sidebar.
2. Open the **Model** dropdown and select a model (e.g., `mistral-small-latest` for speed, `mistral-large-latest` for quality).
3. Type a prompt:

> Explain the difference between supervised and unsupervised learning in three sentences.

4. Click **Send** (or press Enter). Review the output for quality, accuracy, and style.

## Parameters

The right sidebar exposes generation parameters:

| Parameter | Effect |
|-----------|--------|
| **Temperature** | Lower (0.1) = deterministic; higher (0.9) = more creative |
| **Max tokens** | Limits response length; controls cost and verbosity |
| **Top P** | Alternative to temperature for controlling diversity |

## Experiment

1. Set **Temperature** to `0.1` and send the same prompt.
2. Set **Temperature** to `0.9` and send again.
3. Compare: low-temperature is more focused; high-temperature shows more variation.

Switch to a different model and send the same prompt to compare model behavior.

## Outcome

You can:
- Send prompts to Mistral models
- Adjust temperature and observe effects on output
- Compare responses across different models

This helps you make informed choices when integrating models into your application.

#model-evaluation #prompt-testing #parameter-tuning