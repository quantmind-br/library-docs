---
title: A New Model for Amp Tab
url: https://ampcode.com/news/new-model-for-amp-tab
source: crawler
fetched_at: 2026-02-06T02:08:36.649033616-03:00
rendered_js: false
word_count: 128
summary: This document explains the technical updates to the Amp Tab completion model, highlighting the use of synthetic data and Direct Preference Optimization to improve performance.
tags:
    - amp-tab
    - machine-learning
    - code-completion
    - dpo
    - synthetic-data
    - model-optimization
category: concept
---

Amp Tab now uses an updated custom model to provide better completions.

In order to train this model, we rebuilt our training dataset to include synthetically generated examples to improve the model's performance in specific scenarios in which the previous model produced poor or missing suggestions, such as follow-up edits.

The new model also uses DPO (Direct Preference Optimization) post-training on top of our SFT (Supervised Fine-Tuning) base. To do that, we used the model's previous bad outputs as negative examples alongside the new synthetic ground truth as positive examples, teaching it to avoid common failure patterns.

Here, see how follow-up edits work much better now. In this video, deleting a proxy variable triggers a chain of completions, including fixes to the constructor and updates to the header.