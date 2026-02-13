---
title: PydanticAI
url: https://openrouter.ai/docs/guides/community/pydantic-ai.mdx
source: llms
fetched_at: 2026-02-13T15:15:51.450707-03:00
rendered_js: false
word_count: 100
summary: This document provides instructions for integrating OpenRouter with the PydanticAI framework in Python applications using its OpenAI-compatible interface.
tags:
    - pydantic-ai
    - openrouter
    - python
    - llm-integration
    - openai-compatibility
category: guide
---

***

title: PydanticAI
subtitle: Using OpenRouter with PydanticAI
headline: PydanticAI Integration | OpenRouter SDK Support
canonical-url: '[https://openrouter.ai/docs/guides/community/pydantic-ai](https://openrouter.ai/docs/guides/community/pydantic-ai)'
'og:site\_name': OpenRouter Documentation
'og:title': PydanticAI Integration - OpenRouter SDK Support
'og:description': >-
Integrate OpenRouter using PydanticAI framework. Complete guide for PydanticAI
integration with OpenRouter for Python applications.
'og:image':
type: url
value: >-
[https://openrouter.ai/dynamic-og?title=PydanticAI\&description=PydanticAI%20Integration](https://openrouter.ai/dynamic-og?title=PydanticAI\&description=PydanticAI%20Integration)
'og:image:width': 1200
'og:image:height': 630
'twitter:card': summary\_large\_image
'twitter:site': '@OpenRouterAI'
noindex: false
nofollow: false
---------------

## Using PydanticAI

[PydanticAI](https://github.com/pydantic/pydantic-ai) provides a high-level interface for working with various LLM providers, including OpenRouter.

### Installation

```bash
pip install 'pydantic-ai-slim[openai]'
```

### Configuration

You can use OpenRouter with PydanticAI through its OpenAI-compatible interface:

```python
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

model = OpenAIModel(
    "anthropic/claude-3.5-sonnet",  # or any other OpenRouter model
    base_url="https://openrouter.ai/api/v1",
    api_key="sk-or-...",
)

agent = Agent(model)
result = await agent.run("What is the meaning of life?")
print(result)
```

For more details about using PydanticAI with OpenRouter, see the [PydanticAI documentation](https://ai.pydantic.dev/models/#api_key-argument).