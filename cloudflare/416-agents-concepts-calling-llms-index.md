---
title: Calling LLMs
url: https://developers.cloudflare.com/agents/concepts/calling-llms/index.md
source: llms
fetched_at: 2026-01-24T15:05:15.004576153-03:00
rendered_js: false
word_count: 186
summary: This document explains the differences between reasoning and instruction-based LLM models and provides guidance on selecting the appropriate model type based on task complexity and cost efficiency.
tags:
    - llm-providers
    - reasoning-models
    - instruction-models
    - model-selection
    - ai-optimization
category: concept
---

---
title: Calling LLMs · Cloudflare Agents docs
description: Different LLM providers offer models optimized for specific types
  of tasks. When building AI systems, choosing the right model is crucial for
  both performance and cost efficiency.
lastUpdated: 2025-08-15T20:11:52.000Z
chatbotDeprioritize: false
tags: LLM
source_url:
  html: https://developers.cloudflare.com/agents/concepts/calling-llms/
  md: https://developers.cloudflare.com/agents/concepts/calling-llms/index.md
---

### Understanding LLM providers and model types

Different LLM providers offer models optimized for specific types of tasks. When building AI systems, choosing the right model is crucial for both performance and cost efficiency.

#### Reasoning Models

Models like OpenAI's o1, Anthropic's Claude, and DeepSeek's R1 are particularly well-suited for complex reasoning tasks. These models excel at:

* Breaking down problems into steps
* Following complex instructions
* Maintaining context across long conversations
* Generating code and technical content

For example, when implementing a travel booking system, you might use a reasoning model to analyze travel requirements and generate appropriate booking strategies.

#### Instruction Models

Models like GPT-4 and Claude Instant are optimized for following straightforward instructions efficiently. They work well for:

* Content generation
* Simple classification tasks
* Basic question answering
* Text transformation

These models are often more cost-effective for straightforward tasks that do not require complex reasoning.