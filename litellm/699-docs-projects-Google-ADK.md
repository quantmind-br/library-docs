---
title: Google ADK (Agent Development Kit) | liteLLM
url: https://docs.litellm.ai/docs/projects/Google%20ADK
source: sitemap
fetched_at: 2026-01-21T19:47:14.909770776-03:00
rendered_js: false
word_count: 30
summary: Google ADK is an open-source Python framework for building, evaluating, and deploying AI agents with support for Gemini and multiple other model providers via LiteLLM.
tags:
    - google-adk
    - python
    - ai-agents
    - llm-framework
    - gemini
    - litellm
category: guide
---

[Google ADK](https://github.com/google/adk-python) is an open-source, code-first Python framework for building, evaluating, and deploying sophisticated AI agents. While optimized for Gemini, ADK is model-agnostic and supports LiteLLM for using 100+ providers.

```
from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    model=LiteLlm(model="openai/gpt-4o"),# Or any LiteLLM-supported model
    name="my_agent",
    description="An agent using LiteLLM",
    instruction="You are a helpful assistant.",
    tools=[your_tools],
)
```