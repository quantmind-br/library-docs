---
title: Observability integrations | Mistral Docs
url: https://docs.mistral.ai/resources/observability-integrations
source: sitemap
fetched_at: 2026-04-26T04:11:44.159209838-03:00
rendered_js: false
word_count: 1545
summary: This document outlines the importance of observability in LLM applications, detailing key components to monitor at the call and application levels, relevant metrics for performance tracking, and available integration options.
tags:
    - llm-observability
    - llmops
    - model-monitoring
    - system-tracing
    - prompt-engineering
    - production-readiness
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Observability Integrations

Observability is essential for LLM systems across prototyping, testing, and production:
- **Visibility**: understand system behavior and debug issues.
- **Production requirement**: monitoring, scalability, security, and compliance.
- **Reproducibility**: observe and reproduce LLM system behavior.
- **Continuous improvement**: use insights to drive improvement.

## What to Observe

### Individual LLM Call Level

Monitor three key components:
1. **Input prompt**: prompt template, few-shot examples, retrieved context, memory, tools.
2. **Model**: version/identifier, configuration, hyperparameters, customizations.
3. **Output**: structure and format.

### Application Level

Observe the pattern, logistics, and sequence of LLM calls:
- **RAG**: track external document/dataset retrieval and retrieval step.
- **LLM as part of a system**: observe input/output of each step in multi-LLM chains or multi-agent systems.

## Metrics to Track

| Category | Metrics |
|----------|---------|
| **Token and cost** | Number of tokens processed, associated costs |
| **Traces and latency** | Sequence of operations, performance bottlenecks |
| **Anomalies and errors** | Error rates, negative feedback, thumbs down cases |
| **Quality** | Evaluation metrics, user feedback, annotations |

## Integrations

Mistral integrates with the following observability tools:

### LangSmith

LangSmith provides observability throughout the LLM application development lifecycle. Compatible with LangChain ecosystem and external systems.

> [!example]
> All [langchain notebooks](https://github.com/mistralai/cookbook/tree/main/third_party/langchain) in the Mistral cookbook include LangSmith integration.

### Langfuse

[Langfuse](https://langfuse.com) is an open-source LLMOps platform with tracing and monitoring for AI applications.

- Most used open-source LLMOps platform
- Model and framework agnostic
- Built for production, incrementally adoptable
- API-first, self-hostable

> [!example]
> [Step-by-step guide](https://langfuse.com/docs/integrations/mistral-sdk) on tracing Mistral models with Langfuse.

### Arize Phoenix

Phoenix is an open-source observability library for experimentation, evaluation, and troubleshooting. Built on OpenTelemetry.

- [Self-hosted](https://docs.arize.com/phoenix/setup/environments#container), [cloud](https://docs.arize.com/phoenix/hosted-phoenix), or [notebook](https://docs.arize.com/phoenix/setup/environments#notebooks)
- Provides [Mistral integration](https://docs.arize.com/phoenix/tracing/integrations-tracing/mistralai) for Client.chat and Agent.chat calls
- Strong analytical platform with copilot agent for debugging

> [!example]
> [Example notebook](https://github.com/mistralai/cookbook/blob/main/third_party/Phoenix/arize_phoenix_tracing.ipynb) showing how to trace Mistral chat.complete and tool calls.

### Weights and Biases

End-to-end AI developer platform for ML and LLM workflows. Use W&B Weave to evaluate, monitor, and iterate on GenAI applications.

- Integrated with [Mistral API](https://weave-docs.wandb.ai/guides/integrations/mistral/): add one line `weave.init('my-project')` to auto-track inputs, output, context, errors, evaluation metrics.
- Integrated with [Mistral fine-tuning service](https://docs.mistral.ai/resources/deprecated/finetuning#integration-with-weights-and-biases).

### PromptLayer

Platform for prompt management, collaboration, monitoring, and evaluation.

- No-code CMS for prompt management and versioning
- Native support for Mistral
- Prompts are model agnostic by default

### AgentOps

Open-source observability and DevTool platform for AI agents. Integrates with CrewAI, AutoGen, and LangChain.

### phospho

Text analytics platform for getting answers, taking decisions, and reducing churn through user message data mining.

- Open-source, no-code clustering and analytics
- Customizable dashboards
- Many integrations with other observability frameworks

> [!example]
> [phospho notebooks](https://github.com/mistralai/cookbook/tree/main/third_party/phospho) in the Mistral cookbook.

### MLflow

Unified, end-to-end open source MLOps platform for traditional ML and GenAI applications.

- Add Mistral integration with one line: `mlflow.mistral.autolog()`
- Full tracing of chat and embedding calls
- Complete model evaluation, versioning, and deployment

> [!example]
> [Example notebook](https://github.com/mistralai/cookbook/blob/main/third_party/MLflow/mistral-mlflow-tracing.ipynb).

### Maxim AI

Comprehensive observability for Mistral-based AI applications.

- Performance Analytics: track latency, tokens consumed, and costs
- Advanced Visualisation: understand agent trajectories through dashboards

> [!example]
> [Colab Notebook](https://github.com/mistralai/cookbook/blob/main/third_party/Maxim/cookbook_maxim_mistral_integration.ipynb) for Maxim-Mistral SDK integration.

#llm-observability #llmops #model-monitoring #system-tracing
