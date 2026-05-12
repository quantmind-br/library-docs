---
title: Which Model Should I Use
url: https://docs.fireworks.ai/guides/recommended-models
source: sitemap
fetched_at: 2026-04-27T20:18:20.471713807-03:00
rendered_js: false
word_count: 507
summary: Recommendations for choosing the right open source models from Fireworks AI, by use case and migration path from closed-source models.
tags:
    - open-source-models
    - model-recommendations
    - ai-migration
    - use-case-selection
    - llama-3
    - kimi-k2
    - fireworks-ai
category: guide
optimized: true
optimized_at: 2026-04-27T23:00:00Z
---
Choose the right open source model by use case or migrate from closed-source leaders. Recommendations based on Fireworks internal testing, customer deployments, and external benchmarks. Updated regularly.

## By Use Case

| Category | Use Case | Recommended Models |
|---|---|---|
| **Code & Development** | Code generation & reasoning | **Large:** [Kimi K2.5](https://app.fireworks.ai/models/fireworks/kimi-k2p5), [Kimi K2 0905](https://app.fireworks.ai/models/fireworks/kimi-k2-instruct-0905), [Deepseek V3.2](https://app.fireworks.ai/models/fireworks/deepseek-v3p2), [MiniMax 2.5](https://app.fireworks.ai/models/fireworks/minimax-m2p5), [GLM 4.7](https://app.fireworks.ai/models/fireworks/glm-4p7), [GLM 5](https://app.fireworks.ai/models/fireworks/glm-5) · **Medium:** [Qwen3 235B A22B](https://app.fireworks.ai/models/fireworks/qwen3-235b-a22b), [Qwen2.5-32B-Coder](https://app.fireworks.ai/models/fireworks/qwen2p5-coder-32b-instruct) |
| | Code completion & bug fixing | **Large:** [Kimi K2.5](https://app.fireworks.ai/models/fireworks/kimi-k2p5), [Kimi K2 0905](https://app.fireworks.ai/models/fireworks/kimi-k2-instruct-0905), [MiniMax 2.5](https://app.fireworks.ai/models/fireworks/minimax-m2p5) · **Medium:** [Qwen3 235B A22B](https://app.fireworks.ai/models/fireworks/qwen3-235b-a22b), [Qwen2.5-32B-Coder](https://app.fireworks.ai/models/fireworks/qwen2p5-coder-32b-instruct) · **Small:** [Qwen3 14B](https://app.fireworks.ai/models/fireworks/qwen3-14b), [Qwen3 8B](https://app.fireworks.ai/models/fireworks/qwen3-8b) |
| **AI Applications** | AI Agents with tool use | **Large:** [Kimi K2.5](https://app.fireworks.ai/models/fireworks/kimi-k2p5), [Kimi K2 0905](https://app.fireworks.ai/models/fireworks/kimi-k2-instruct-0905), [Deepseek V3.2](https://app.fireworks.ai/models/fireworks/deepseek-v3p2), [MiniMax 2.5](https://app.fireworks.ai/models/fireworks/minimax-m2p5), [GLM 4.7](https://app.fireworks.ai/models/fireworks/glm-4p7), [GLM 5](https://app.fireworks.ai/models/fireworks/glm-5) · [Qwen 3 Family](https://app.fireworks.ai/models?filter=Provider&provider=Qwen) (Large/Medium/Small) |
| | General reasoning & planning | **Large:** [Kimi K2.5](https://app.fireworks.ai/models/fireworks/kimi-k2p5), [Kimi K2 0905](https://app.fireworks.ai/models/fireworks/kimi-k2-instruct-0905), [Kimi K2 Thinking](https://app.fireworks.ai/models/fireworks/kimi-k2-thinking), [Deepseek V3.2](https://app.fireworks.ai/models/fireworks/deepseek-v3p2), [MiniMax 2.5](https://app.fireworks.ai/models/fireworks/minimax-m2p5), [Qwen3 235B A22B](https://app.fireworks.ai/models/fireworks/qwen3-235b-a22b), [GLM 4.7](https://app.fireworks.ai/models/fireworks/glm-4p7), [GLM 5](https://app.fireworks.ai/models/fireworks/glm-5) · **Medium:** [GPT-OSS-120B](https://app.fireworks.ai/models/fireworks/gpt-oss-120b), [Qwen2.5-72B-Instruct](https://app.fireworks.ai/models/fireworks/qwen2p5-72b-instruct), [Llama 3.3 70B](https://app.fireworks.ai/models/fireworks/llama-v3p3-70b-instruct) |
| | Long context & summarization | **Large:** [Kimi K2.5](https://app.fireworks.ai/models/fireworks/kimi-k2p5), [Kimi K2 0905](https://app.fireworks.ai/models/fireworks/kimi-k2-instruct-0905), [MiniMax 2.5](https://app.fireworks.ai/models/fireworks/minimax-m2p5), [GLM 5](https://app.fireworks.ai/models/fireworks/glm-5) · **Medium:** [GPT-OSS-120B](https://app.fireworks.ai/models/fireworks/gpt-oss-120b) |
| | Fast semantic search & extraction | **Medium:** [GPT-OSS-120B](https://app.fireworks.ai/models/fireworks/gpt-oss-120b) · **Small:** [GPT-OSS 20B](https://app.fireworks.ai/models/fireworks/gpt-oss-20b), [Qwen3 8B](https://app.fireworks.ai/models/fireworks/qwen3-8b), [Qwen 3 4B](https://app.fireworks.ai/models/fireworks/qwen3-4b), [Llama 3.1 8B](https://app.fireworks.ai/models/fireworks/llama-v3p1-8b-instruct), [Llama 3.2 3B](https://app.fireworks.ai/models/fireworks/llama-v3p2-3b-instruct), [Llama 3.2 1B](https://app.fireworks.ai/models/fireworks/llama-v3p2-1b-instruct) |
| **Vision & Multimodal** | Vision & document understanding | **Large:** [Kimi K2.5](https://app.fireworks.ai/models/fireworks/kimi-k2p5), [Qwen2.5-VL 72B Instruct](https://app.fireworks.ai/models/fireworks/qwen2p5-vl-72b-instruct) · **Small:** Deepseek OCR, [Qwen3 VL 30B A3B](https://app.fireworks.ai/models/fireworks/qwen3-vl-30b-a3b), [Qwen2.5-VL 3-7B](https://app.fireworks.ai/models/fireworks/qwen2p5-vl-7b-instruct) |

---

## Migrating from Closed Models

### Claude Alternatives

| Closed Source | Use Case | Latency Budget | Open Source Alternative |
|---|---|---|---|
| Claude Sonnet 4.5 | Agentic use cases, Coding, Research agents | High | [Deepseek V3.2](https://app.fireworks.ai/models/fireworks/deepseek-v3p2), [Kimi K2 0905](https://app.fireworks.ai/models/fireworks/kimi-k2-instruct-0905), [MiniMax 2.5](https://app.fireworks.ai/models/fireworks/minimax-m2p5), [GLM 4.7](https://app.fireworks.ai/models/fireworks/glm-4p7), [GLM 5](https://app.fireworks.ai/models/fireworks/glm-5) |
| Claude Haiku 4.5 | Agentic use cases, Coding, Research agents | Low | [Qwen 3 14B](https://app.fireworks.ai/models/fireworks/qwen3-14b), [Qwen 3 8B](https://app.fireworks.ai/models/fireworks/qwen3-8b), [Mistral Codestral 22B](https://app.fireworks.ai/models/fireworks/mistral-codestral-22b-v0p1) |

### OpenAI GPT Alternatives

| Closed Source | Use Case | Latency Budget | Open Source Alternative |
|---|---|---|---|
| GPT-5 | Agentic use cases, Research agents | High | [Kimi K2 Thinking](https://app.fireworks.ai/models/fireworks/kimi-k2-thinking), [Kimi K2 0905](https://app.fireworks.ai/models/fireworks/kimi-k2-instruct-0905), [Deepseek V3.2](https://app.fireworks.ai/models/fireworks/deepseek-v3p2), [MiniMax 2.5](https://app.fireworks.ai/models/fireworks/minimax-m2p5), [GLM 5](https://app.fireworks.ai/models/fireworks/glm-5) |
| GPT-5 mini & nano | Chatbots, Intent classification, Search | Low | [Qwen 3 14B](https://app.fireworks.ai/models/fireworks/qwen3-14b), [Qwen 3 8B](https://app.fireworks.ai/models/fireworks/qwen3-8b), [GPT-OSS 120B](https://app.fireworks.ai/models/fireworks/gpt-oss-120b), [GPT-OSS 20B](https://app.fireworks.ai/models/fireworks/gpt-oss-20b) |

### Google Gemini Alternatives

| Closed Source | Use Case | Latency Budget | Open Source Alternative |
|---|---|---|---|
| Gemini 3 Pro | Agentic use cases, Research agents | High | [Kimi K2 Thinking](https://app.fireworks.ai/models/fireworks/kimi-k2-thinking), [Kimi K2 0905](https://app.fireworks.ai/models/fireworks/kimi-k2-instruct-0905), [Deepseek V3.2](https://app.fireworks.ai/models/fireworks/deepseek-v3p2), [MiniMax 2.5](https://app.fireworks.ai/models/fireworks/minimax-m2p5), [GLM 5](https://app.fireworks.ai/models/fireworks/glm-5) |
| Gemini 3 Pro Flash & Flash Light | Chatbots, Intent classification, Search | Low | [Qwen 3 4B](https://app.fireworks.ai/models/fireworks/qwen3-4b), [Qwen 3 8B](https://app.fireworks.ai/models/fireworks/qwen3-8b), [Llama 3.1 8B](https://app.fireworks.ai/models/fireworks/llama-v3p1-8b-instruct), [GPT-OSS 20B](https://app.fireworks.ai/models/fireworks/gpt-oss-20b) |

## Latency Budget

- **High latency budget**: Quality is priority. Best for complex reasoning, multi-step workflows, and research tasks where accuracy matters more than speed.
- **Low latency budget**: Speed is priority. Best for user-facing applications like chatbots, real-time search, and high-throughput classification.

> [!info]
> Last updated: February 2026