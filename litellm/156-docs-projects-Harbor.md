---
title: Harbor | liteLLM
url: https://docs.litellm.ai/docs/projects/Harbor
source: sitemap
fetched_at: 2026-01-21T19:47:19.292651921-03:00
rendered_js: false
word_count: 57
summary: Harbor is a framework designed for evaluating, benchmarking, and optimizing language model agents across various providers using LiteLLM. It supports parallel experiment execution in the cloud and generating rollouts for reinforcement learning optimization.
tags:
    - agent-evaluation
    - llm-benchmarking
    - agent-optimization
    - litellm
    - cloud-computing
    - reinforcement-learning
category: guide
---

[Harbor](https://github.com/laude-institute/harbor) is a framework from the creators of Terminal-Bench for evaluating and optimizing agents and language models. It uses LiteLLM to call 100+ LLM providers.

```
# Install
pip install harbor

# Run a benchmark with any LiteLLM-supported model
harbor run --dataset terminal-bench@2.0 \
   --agent claude-code \
   --model anthropic/claude-opus-4-1 \
   --n-concurrent 4
```

Key features:

- Evaluate agents like Claude Code, OpenHands, Codex CLI
- Build and share benchmarks and environments
- Run experiments in parallel across cloud providers (Daytona, Modal)
- Generate rollouts for RL optimization
- [GitHub](https://github.com/laude-institute/harbor)
- [Documentation](https://harborframework.com/docs)