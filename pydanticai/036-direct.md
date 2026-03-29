---
title: Direct Model Requests - Pydantic AI
url: https://ai.pydantic.dev/direct/
source: sitemap
fetched_at: 2026-01-22T22:23:23.428404725-03:00
rendered_js: false
word_count: 295
summary: The direct module provides low-level, imperative functions for making synchronous and asynchronous requests to LLMs with minimal abstraction. It is designed for scenarios requiring granular control over model interactions and custom implementations outside of the higher-level Agent API.
tags:
    - pydantic-ai
    - llm-api
    - direct-module
    - streaming-requests
    - tool-calling
    - opentelemetry
    - async-programming
category: api
---

The `direct` module provides low-level methods for making imperative requests to LLMs where the only abstraction is input and output schema translation, enabling you to use all models with the same API.

These methods are thin wrappers around the [`Model`](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model") implementations, offering a simpler interface when you don't need the full functionality of an [`Agent`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent "Agent            dataclass   ").

The following functions are available:

- [`model_request`](https://ai.pydantic.dev/api/direct/#pydantic_ai.direct.model_request "model_request            async   "): Make a non-streamed async request to a model
- [`model_request_sync`](https://ai.pydantic.dev/api/direct/#pydantic_ai.direct.model_request_sync "model_request_sync"): Make a non-streamed synchronous request to a model
- [`model_request_stream`](https://ai.pydantic.dev/api/direct/#pydantic_ai.direct.model_request_stream "model_request_stream"): Make a streamed async request to a model
- [`model_request_stream_sync`](https://ai.pydantic.dev/api/direct/#pydantic_ai.direct.model_request_stream_sync "model_request_stream_sync"): Make a streamed sync request to a model

## Basic Example

Here's a simple example demonstrating how to use the direct API to make a basic request:

direct\_basic.py

```
frompydantic_aiimport ModelRequest
frompydantic_ai.directimport model_request_sync

# Make a synchronous request to the model
model_response = model_request_sync(
    'anthropic:claude-haiku-4-5',
    [ModelRequest.user_text_prompt('What is the capital of France?')]
)

print(model_response.parts[0].content)
#> The capital of France is Paris.
print(model_response.usage)
#> RequestUsage(input_tokens=56, output_tokens=7)
```

*(This example is complete, it can be run "as is")*

You can also use the direct API to work with function/tool calling.

Even here we can use Pydantic to generate the JSON schema for the tool:

```
fromtypingimport Literal

frompydanticimport BaseModel

frompydantic_aiimport ModelRequest, ToolDefinition
frompydantic_ai.directimport model_request
frompydantic_ai.modelsimport ModelRequestParameters


classDivide(BaseModel):
"""Divide two numbers."""

    numerator: float
    denominator: float
    on_inf: Literal['error', 'infinity'] = 'infinity'


async defmain():
    # Make a request to the model with tool access
    model_response = await model_request(
        'openai:gpt-5-nano',
        [ModelRequest.user_text_prompt('What is 123 / 456?')],
        model_request_parameters=ModelRequestParameters(
            function_tools=[
                ToolDefinition(
                    name=Divide.__name__.lower(),
                    description=Divide.__doc__,
                    parameters_json_schema=Divide.model_json_schema(),
                )
            ],
            allow_text_output=True,  # Allow model to either use tools or respond directly
        ),
    )
    print(model_response)
"""
    ModelResponse(
        parts=[
            ToolCallPart(
                tool_name='divide',
                args={'numerator': '123', 'denominator': '456'},
                tool_call_id='pyd_ai_2e0e396768a14fe482df90a29a78dc7b',
            )
        ],
        usage=RequestUsage(input_tokens=55, output_tokens=7),
        model_name='gpt-5-nano',
        timestamp=datetime.datetime(...),
    )
    """
```

*(This example is complete, it can be run "as is" — you'll need to add `asyncio.run(main())` to run `main`)*

## When to Use the direct API vs Agent

The direct API is ideal when:

1. You need more direct control over model interactions
2. You want to implement custom behavior around model requests
3. You're building your own abstractions on top of model interactions

For most application use cases, the higher-level [`Agent`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent "Agent            dataclass   ") API provides a more convenient interface with additional features such as built-in tool execution, retrying, structured output parsing, and more.

## OpenTelemetry or Logfire Instrumentation

As with [agents](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent "Agent            dataclass   "), you can enable OpenTelemetry/Logfire instrumentation with just a few extra lines

direct\_instrumented.py

```
importlogfire

frompydantic_aiimport ModelRequest
frompydantic_ai.directimport model_request_sync

logfire.configure()
logfire.instrument_pydantic_ai()

# Make a synchronous request to the model
model_response = model_request_sync(
    'anthropic:claude-haiku-4-5',
    [ModelRequest.user_text_prompt('What is the capital of France?')],
)

print(model_response.parts[0].content)
#> The capital of France is Paris.
```

*(This example is complete, it can be run "as is")*

You can also enable OpenTelemetry on a per call basis:

direct\_instrumented.py

```
importlogfire

frompydantic_aiimport ModelRequest
frompydantic_ai.directimport model_request_sync

logfire.configure()

# Make a synchronous request to the model
model_response = model_request_sync(
    'anthropic:claude-haiku-4-5',
    [ModelRequest.user_text_prompt('What is the capital of France?')],
    instrument=True
)

print(model_response.parts[0].content)
#> The capital of France is Paris.
```

See [Debugging and Monitoring](https://ai.pydantic.dev/logfire/) for more details, including how to instrument with plain OpenTelemetry without Logfire.