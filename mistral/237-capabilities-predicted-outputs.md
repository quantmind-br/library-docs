---
title: Predicted outputs | Mistral Docs
url: https://docs.mistral.ai/capabilities/predicted_outputs
source: crawler
fetched_at: 2026-01-29T07:33:11.750256827-03:00
rendered_js: false
word_count: 156
summary: This document explains how the Predicted Outputs feature optimizes model response times by providing known or predictable text segments during tasks like code modification.
tags:
    - predicted-outputs
    - latency-optimization
    - performance-tuning
    - chat-completions
    - inference-efficiency
category: concept
---

Predicted Outputs **optimizes response time** by leveraging known or predictable content. This approach minimizes latency while maintaining high output quality. In tasks such as editing large texts, modifying code, or generating template-based responses, significant portions of the output are often predetermined. By predefining these expected parts with Predicted Outputs, **models can allocate more computational resources to the unpredictable elements, improving overall efficiency.**

### Code Modification

**Predicted Outputs shine in scenarios where you need to regenerate text documents or code files with minor modifications.** The key parameter introduced is the `prediction` parameter, which enables users to define predicted outputs. For example, imagine you want your model to update the model used in a fine-tuning job. You can include the code snippet you'd like to modify as both the user prompt and the predicted output.

Before continuing, we recommend reading the [Chat Competions](https://docs.mistral.ai/capabilities/completion) documentation to learn more about the chat completions API and how to use it before proceeding.