---
title: OpenAI Agents SDK | liteLLM
url: https://docs.litellm.ai/docs/projects/openai-agents
source: sitemap
fetched_at: 2026-01-21T19:47:26.55544727-03:00
rendered_js: false
word_count: 33
summary: This document explains how to use the LiteLLM extension with the OpenAI Agents SDK to integrate various model providers into multi-agent workflows.
tags:
    - openai-agents-sdk
    - litellm
    - multi-agent-systems
    - python-sdk
    - llm-integration
category: tutorial
---

The [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) is a lightweight framework for building multi-agent workflows. It includes an official LiteLLM extension that lets you use any of the 100+ supported providers (Anthropic, Gemini, Mistral, Bedrock, etc.)

```
from agents import Agent, Runner
from agents.extensions.models.litellm_model import LitellmModel

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    model=LitellmModel(model="provider/model-name")
)

result = Runner.run_sync(agent,"your_prompt_here")
print("Result:", result.final_output)
```