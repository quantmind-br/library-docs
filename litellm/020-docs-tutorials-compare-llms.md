---
title: Benchmark LLMs | liteLLM
url: https://docs.litellm.ai/docs/tutorials/compare_llms
source: sitemap
fetched_at: 2026-01-21T19:55:10.850393161-03:00
rendered_js: false
word_count: 30
summary: This document provides instructions for setting up and running performance benchmarks to compare response times, costs, and outputs across various LLM models using LiteLLM.
tags:
    - litellm
    - benchmarking
    - llm-performance
    - latency-testing
    - cost-analysis
    - python
category: tutorial
---

```
git clone https://github.com/BerriAI/litellm
```

```
cd litellm/cookbook/benchmark
```

```
pip install litellm click tqdm tabulate termcolor
```

```
Running question: When will BerriAI IPO? for model: claude-2: 100%|████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:13<00:00,  4.41s/it]

Benchmark Results for 'When will BerriAI IPO?':
+-----------------+----------------------------------------------------------------------------------+---------------------------+------------+
| Model           | Response                                                                         | Response Time (seconds)   | Cost ($)   |
+=================+==================================================================================+===========================+============+
| gpt-3.5-turbo   | As an AI language model, I cannot provide up-to-date information or predict      | 1.55 seconds              | $0.000122  |
|                 | future events. It is best to consult a reliable financial source or contact      |                           |            |
|                 | BerriAI directly for information regarding their IPO plans.                      |                           |            |
+-----------------+----------------------------------------------------------------------------------+---------------------------+------------+
| togethercompute | I'm not able to provide information about future IPO plans or dates for BerriAI  | 8.52 seconds              | $0.000531  |
| r/llama-2-70b-c | or any other company. IPO (Initial Public Offering) plans and timelines are      |                           |            |
| hat             | typically kept private by companies until they are ready to make a public        |                           |            |
|                 | announcement.  It's important to note that IPO plans can change and are subject  |                           |            |
|                 | to various factors, such as market conditions, financial performance, and        |                           |            |
|                 | regulatory approvals. Therefore, it's difficult to predict with certainty when   |                           |            |
|                 | BerriAI or any other company will go public.  If you're interested in staying    |                           |            |
|                 | up-to-date with BerriAI's latest news and developments, you may want to follow   |                           |            |
|                 | their official social media accounts, subscribe to their newsletter, or visit    |                           |            |
|                 | their website periodically for updates.                                          |                           |            |
+-----------------+----------------------------------------------------------------------------------+---------------------------+------------+
| claude-2        | I do not have any information about when or if BerriAI will have an initial      | 3.17 seconds              | $0.002084  |
|                 | public offering (IPO). As an AI assistant created by Anthropic to be helpful,    |                           |            |
|                 | harmless, and honest, I do not have insider knowledge about Anthropic's business |                           |            |
|                 | plans or strategies.                                                             |                           |            |
+-----------------+----------------------------------------------------------------------------------+---------------------------+------------+
```

**🤝 Schedule a 1-on-1 Session:** Book a [1-on-1 session](https://calendly.com/d/4mp-gd3-k5k/litellm-1-1-onboarding-chat) with Krrish and Ishaan, the founders, to discuss any issues, provide feedback, or explore how we can improve LiteLLM for you.