---
title: Pydantic Model - Pydantic AI
url: https://ai.pydantic.dev/examples/pydantic-model/
source: sitemap
fetched_at: 2026-01-22T22:25:41.499765031-03:00
rendered_js: false
word_count: 58
summary: This document demonstrates how to use Pydantic AI to extract structured data from text input and map it directly to a Pydantic model using the Agent's output_type parameter.
tags:
    - pydantic-ai
    - structured-output
    - pydantic-model
    - python-sdk
    - llm-agent
    - data-extraction
category: tutorial
---

Simple example of using Pydantic AI to construct a Pydantic model from a text input.

Demonstrates:

- [structured `output_type`](https://ai.pydantic.dev/output/#structured-output)

## Running the Example

With [dependencies installed and environment variables set](https://ai.pydantic.dev/examples/setup/#usage), run:

pipuv

```
python-mpydantic_ai_examples.pydantic_model
```

```
uvrun-mpydantic_ai_examples.pydantic_model
```

This examples uses `openai:gpt-5` by default, but it works well with other models, e.g. you can run it with Gemini using:

pipuv

```
PYDANTIC_AI_MODEL=gemini-2.5-propython-mpydantic_ai_examples.pydantic_model
```

```
PYDANTIC_AI_MODEL=gemini-2.5-prouvrun-mpydantic_ai_examples.pydantic_model
```

(or `PYDANTIC_AI_MODEL=gemini-2.5-flash ...`)

## Example Code

[pydantic\_model.py](https://github.com/pydantic/pydantic-ai/blob/main/examples/pydantic_ai_examples/pydantic_model.py)

```
"""Simple example of using Pydantic AI to construct a Pydantic model from a text input.

Run with:

    uv run -m pydantic_ai_examples.pydantic_model
"""

importos

importlogfire
frompydanticimport BaseModel

frompydantic_aiimport Agent

# 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured
logfire.configure(send_to_logfire='if-token-present')
logfire.instrument_pydantic_ai()


classMyModel(BaseModel):
    city: str
    country: str


model = os.getenv('PYDANTIC_AI_MODEL', 'openai:gpt-5')
print(f'Using model: {model}')
agent = Agent(model, output_type=MyModel)

if __name__ == '__main__':
    result = agent.run_sync('The windy city in the US of A.')
    print(result.output)
    print(result.usage())
```