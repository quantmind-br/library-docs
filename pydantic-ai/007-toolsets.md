---
title: Toolsets - Pydantic AI
url: https://ai.pydantic.dev/toolsets/
source: sitemap
fetched_at: 2026-01-22T22:23:46.652667541-03:00
rendered_js: false
word_count: 2207
summary: This document explains how to use toolsets in Pydantic AI to organize, reuse, and dynamically manage collections of tools for AI agents.
tags:
    - pydantic-ai
    - toolsets
    - agent-configuration
    - function-toolset
    - dynamic-tools
    - python-library
category: guide
---

A toolset represents a collection of [tools](https://ai.pydantic.dev/tools/) that can be registered with an agent in one go. They can be reused by different agents, swapped out at runtime or during testing, and composed in order to dynamically filter which tools are available, modify tool definitions, or change tool execution behavior. A toolset can contain locally defined functions, depend on an external service to provide them, or implement custom logic to list available tools and handle them being called.

Toolsets are used (among many other things) to define [MCP servers](https://ai.pydantic.dev/mcp/client/) available to an agent. Pydantic AI includes many kinds of toolsets which are described below, and you can define a [custom toolset](#building-a-custom-toolset) by inheriting from the [`AbstractToolset`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset") class.

The toolsets that will be available during an agent run can be specified in four different ways:

- at agent construction time, via the [`toolsets`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.__init__ "__init__") keyword argument to `Agent`, which takes toolset instances as well as functions that generate toolsets [dynamically](#dynamically-building-a-toolset) based on the agent [run context](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext            dataclass   ")
- at agent run time, via the `toolsets` keyword argument to [`agent.run()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run "run            async   "), [`agent.run_sync()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run_sync "run_sync"), [`agent.run_stream()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run_stream "run_stream            async   "), or [`agent.iter()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.iter "iter            async   "). These toolsets will be additional to those registered on the `Agent`
- [dynamically](#dynamically-building-a-toolset), via the [`@agent.toolset`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.toolset "toolset") decorator which lets you build a toolset based on the agent [run context](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext            dataclass   ")
- as a contextual override, via the `toolsets` keyword argument to the [`agent.override()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.iter "iter            async   ") context manager. These toolsets will replace those provided at agent construction or run time during the life of the context manager

toolsets.py

```
frompydantic_aiimport Agent, FunctionToolset
frompydantic_ai.models.testimport TestModel


defagent_tool():
    return "I'm registered directly on the agent"


defextra_tool():
    return "I'm passed as an extra tool for a specific run"


defoverride_tool():
    return 'I override all other tools'


agent_toolset = FunctionToolset(tools=[agent_tool]) # (1)!
extra_toolset = FunctionToolset(tools=[extra_tool])
override_toolset = FunctionToolset(tools=[override_tool])

test_model = TestModel() # (2)!
agent = Agent(test_model, toolsets=[agent_toolset])

result = agent.run_sync('What tools are available?')
print([t.name for t in test_model.last_model_request_parameters.function_tools])
#> ['agent_tool']

result = agent.run_sync('What tools are available?', toolsets=[extra_toolset])
print([t.name for t in test_model.last_model_request_parameters.function_tools])
#> ['agent_tool', 'extra_tool']

with agent.override(toolsets=[override_toolset]):
    result = agent.run_sync('What tools are available?', toolsets=[extra_toolset]) # (3)!
    print([t.name for t in test_model.last_model_request_parameters.function_tools])
    #> ['override_tool']
```

1. The [`FunctionToolset`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.FunctionToolset "FunctionToolset") will be explained in detail in the next section.
2. We're using [`TestModel`](https://ai.pydantic.dev/api/models/test/#pydantic_ai.models.test.TestModel "TestModel            dataclass   ") here because it makes it easy to see which tools were available on each run.
3. This `extra_toolset` will be ignored because we're inside an override context.

*(This example is complete, it can be run "as is")*

As the name suggests, a [`FunctionToolset`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.FunctionToolset "FunctionToolset") makes locally defined functions available as tools.

Functions can be added as tools in three different ways:

- via the [`@toolset.tool`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.FunctionToolset.tool "tool") decorator
- via the [`tools`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.FunctionToolset.__init__ "__init__") keyword argument to the constructor which can take either plain functions, or instances of [`Tool`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool            dataclass   ")
- via the [`toolset.add_function()`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.FunctionToolset.add_function "add_function") and [`toolset.add_tool()`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.FunctionToolset.add_tool "add_tool") methods which can take a plain function or an instance of [`Tool`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool            dataclass   ") respectively

Functions registered in any of these ways can define an initial `ctx: RunContext` argument in order to receive the agent [run context](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext            dataclass   "). The `add_function()` and `add_tool()` methods can also be used from a tool function to dynamically register new tools during a run to be available in future run steps.

function\_toolset.py

```
fromdatetimeimport datetime

frompydantic_aiimport Agent, FunctionToolset, RunContext
frompydantic_ai.models.testimport TestModel


deftemperature_celsius(city: str) -> float:
    return 21.0


deftemperature_fahrenheit(city: str) -> float:
    return 69.8


weather_toolset = FunctionToolset(tools=[temperature_celsius, temperature_fahrenheit])


@weather_toolset.tool
defconditions(ctx: RunContext, city: str) -> str:
    if ctx.run_step % 2 == 0:
        return "It's sunny"
    else:
        return "It's raining"


datetime_toolset = FunctionToolset()
datetime_toolset.add_function(lambda: datetime.now(), name='now')

test_model = TestModel()  # (1)!
agent = Agent(test_model)

result = agent.run_sync('What tools are available?', toolsets=[weather_toolset])
print([t.name for t in test_model.last_model_request_parameters.function_tools])
#> ['temperature_celsius', 'temperature_fahrenheit', 'conditions']

result = agent.run_sync('What tools are available?', toolsets=[datetime_toolset])
print([t.name for t in test_model.last_model_request_parameters.function_tools])
#> ['now']
```

1. We're using [`TestModel`](https://ai.pydantic.dev/api/models/test/#pydantic_ai.models.test.TestModel "TestModel            dataclass   ") here because it makes it easy to see which tools were available on each run.

*(This example is complete, it can be run "as is")*

Toolsets can be composed to dynamically filter which tools are available, modify tool definitions, or change tool execution behavior. Multiple toolsets can also be combined into one.

### Combining Toolsets

[`CombinedToolset`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.CombinedToolset "CombinedToolset            dataclass   ") takes a list of toolsets and lets them be used as one.

combined\_toolset.py

```
frompydantic_aiimport Agent, CombinedToolset
frompydantic_ai.models.testimport TestModel

fromfunction_toolsetimport datetime_toolset, weather_toolset

combined_toolset = CombinedToolset([weather_toolset, datetime_toolset])

test_model = TestModel() # (1)!
agent = Agent(test_model, toolsets=[combined_toolset])
result = agent.run_sync('What tools are available?')
print([t.name for t in test_model.last_model_request_parameters.function_tools])
#> ['temperature_celsius', 'temperature_fahrenheit', 'conditions', 'now']
```

1. We're using [`TestModel`](https://ai.pydantic.dev/api/models/test/#pydantic_ai.models.test.TestModel "TestModel            dataclass   ") here because it makes it easy to see which tools were available on each run.

*(This example is complete, it can be run "as is")*

### Filtering Tools

[`FilteredToolset`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.FilteredToolset "FilteredToolset            dataclass   ") wraps a toolset and filters available tools ahead of each step of the run based on a user-defined function that is passed the agent [run context](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext            dataclass   ") and each tool's [`ToolDefinition`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition "ToolDefinition            dataclass   ") and returns a boolean to indicate whether or not a given tool should be available.

To easily chain different modifications, you can also call [`filtered()`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset.filtered "filtered") on any toolset instead of directly constructing a `FilteredToolset`.

filtered\_toolset.py

```
frompydantic_aiimport Agent
frompydantic_ai.models.testimport TestModel

fromcombined_toolsetimport combined_toolset

filtered_toolset = combined_toolset.filtered(lambda ctx, tool_def: 'fahrenheit' not in tool_def.name)

test_model = TestModel() # (1)!
agent = Agent(test_model, toolsets=[filtered_toolset])
result = agent.run_sync('What tools are available?')
print([t.name for t in test_model.last_model_request_parameters.function_tools])
#> ['weather_temperature_celsius', 'weather_conditions', 'datetime_now']
```

1. We're using [`TestModel`](https://ai.pydantic.dev/api/models/test/#pydantic_ai.models.test.TestModel "TestModel            dataclass   ") here because it makes it easy to see which tools were available on each run.

*(This example is complete, it can be run "as is")*

### Prefixing Tool Names

[`PrefixedToolset`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.PrefixedToolset "PrefixedToolset            dataclass   ") wraps a toolset and adds a prefix to each tool name to prevent tool name conflicts between different toolsets.

To easily chain different modifications, you can also call [`prefixed()`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset.prefixed "prefixed") on any toolset instead of directly constructing a `PrefixedToolset`.

combined\_toolset.py

```
frompydantic_aiimport Agent, CombinedToolset
frompydantic_ai.models.testimport TestModel

fromfunction_toolsetimport datetime_toolset, weather_toolset

combined_toolset = CombinedToolset(
    [
        weather_toolset.prefixed('weather'),
        datetime_toolset.prefixed('datetime')
    ]
)

test_model = TestModel() # (1)!
agent = Agent(test_model, toolsets=[combined_toolset])
result = agent.run_sync('What tools are available?')
print([t.name for t in test_model.last_model_request_parameters.function_tools])
"""
[
    'weather_temperature_celsius',
    'weather_temperature_fahrenheit',
    'weather_conditions',
    'datetime_now',
]
"""
```

1. We're using [`TestModel`](https://ai.pydantic.dev/api/models/test/#pydantic_ai.models.test.TestModel "TestModel            dataclass   ") here because it makes it easy to see which tools were available on each run.

*(This example is complete, it can be run "as is")*

### Renaming Tools

[`RenamedToolset`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.RenamedToolset "RenamedToolset            dataclass   ") wraps a toolset and lets you rename tools using a dictionary mapping new names to original names. This is useful when the names provided by a toolset are ambiguous or would conflict with tools defined by other toolsets, but [prefixing them](#prefixing-tool-names) creates a name that is unnecessarily long or could be confusing to the model.

To easily chain different modifications, you can also call [`renamed()`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset.renamed "renamed") on any toolset instead of directly constructing a `RenamedToolset`.

renamed\_toolset.py

```
frompydantic_aiimport Agent
frompydantic_ai.models.testimport TestModel

fromcombined_toolsetimport combined_toolset

renamed_toolset = combined_toolset.renamed(
    {
        'current_time': 'datetime_now',
        'temperature_celsius': 'weather_temperature_celsius',
        'temperature_fahrenheit': 'weather_temperature_fahrenheit'
    }
)

test_model = TestModel() # (1)!
agent = Agent(test_model, toolsets=[renamed_toolset])
result = agent.run_sync('What tools are available?')
print([t.name for t in test_model.last_model_request_parameters.function_tools])
"""
['temperature_celsius', 'temperature_fahrenheit', 'weather_conditions', 'current_time']
"""
```

1. We're using [`TestModel`](https://ai.pydantic.dev/api/models/test/#pydantic_ai.models.test.TestModel "TestModel            dataclass   ") here because it makes it easy to see which tools were available on each run.

*(This example is complete, it can be run "as is")*

### Dynamic Tool Definitions

[`PreparedToolset`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.PreparedToolset "PreparedToolset            dataclass   ") lets you modify the entire list of available tools ahead of each step of the agent run using a user-defined function that takes the agent [run context](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext            dataclass   ") and a list of [`ToolDefinition`s](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition "ToolDefinition            dataclass   ") and returns a list of modified `ToolDefinition`s.

This is the toolset-specific equivalent of the [`prepare_tools`](https://ai.pydantic.dev/tools-advanced/#prepare-tools) argument to `Agent` that prepares all tool definitions registered on an agent across toolsets.

Note that it is not possible to add or rename tools using `PreparedToolset`. Instead, you can use [`FunctionToolset.add_function()`](#function-toolset) or [`RenamedToolset`](#renaming-tools).

To easily chain different modifications, you can also call [`prepared()`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset.prepared "prepared") on any toolset instead of directly constructing a `PreparedToolset`.

prepared\_toolset.py

```
fromdataclassesimport replace

frompydantic_aiimport Agent, RunContext, ToolDefinition
frompydantic_ai.models.testimport TestModel

fromrenamed_toolsetimport renamed_toolset

descriptions = {
    'temperature_celsius': 'Get the temperature in degrees Celsius',
    'temperature_fahrenheit': 'Get the temperature in degrees Fahrenheit',
    'weather_conditions': 'Get the current weather conditions',
    'current_time': 'Get the current time',
}

async defadd_descriptions(ctx: RunContext, tool_defs: list[ToolDefinition]) -> list[ToolDefinition] | None:
    return [
        replace(tool_def, description=description)
        if (description := descriptions.get(tool_def.name, None))
        else tool_def
        for tool_def
        in tool_defs
    ]

prepared_toolset = renamed_toolset.prepared(add_descriptions)

test_model = TestModel() # (1)!
agent = Agent(test_model, toolsets=[prepared_toolset])
result = agent.run_sync('What tools are available?')
print(test_model.last_model_request_parameters.function_tools)
"""
[
    ToolDefinition(
        name='temperature_celsius',
        parameters_json_schema={
            'additionalProperties': False,
            'properties': {'city': {'type': 'string'}},
            'required': ['city'],
            'type': 'object',
        },
        description='Get the temperature in degrees Celsius',
    ),
    ToolDefinition(
        name='temperature_fahrenheit',
        parameters_json_schema={
            'additionalProperties': False,
            'properties': {'city': {'type': 'string'}},
            'required': ['city'],
            'type': 'object',
        },
        description='Get the temperature in degrees Fahrenheit',
    ),
    ToolDefinition(
        name='weather_conditions',
        parameters_json_schema={
            'additionalProperties': False,
            'properties': {'city': {'type': 'string'}},
            'required': ['city'],
            'type': 'object',
        },
        description='Get the current weather conditions',
    ),
    ToolDefinition(
        name='current_time',
        parameters_json_schema={
            'additionalProperties': False,
            'properties': {},
            'type': 'object',
        },
        description='Get the current time',
    ),
]
"""
```

1. We're using [`TestModel`](https://ai.pydantic.dev/api/models/test/#pydantic_ai.models.test.TestModel "TestModel            dataclass   ") here because it makes it easy to see which tools were available on each run.

### Requiring Tool Approval

[`ApprovalRequiredToolset`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.ApprovalRequiredToolset "ApprovalRequiredToolset            dataclass   ") wraps a toolset and lets you dynamically [require approval](https://ai.pydantic.dev/deferred-tools/#human-in-the-loop-tool-approval) for a given tool call based on a user-defined function that is passed the agent [run context](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext            dataclass   "), the tool's [`ToolDefinition`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition "ToolDefinition            dataclass   "), and the validated tool call arguments. If no function is provided, all tool calls will require approval.

To easily chain different modifications, you can also call [`approval_required()`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset.approval_required "approval_required") on any toolset instead of directly constructing a `ApprovalRequiredToolset`.

See the [Human-in-the-Loop Tool Approval](https://ai.pydantic.dev/deferred-tools/#human-in-the-loop-tool-approval) documentation for more information on how to handle agent runs that call tools that require approval and how to pass in the results.

approval\_required\_toolset.py

```
frompydantic_aiimport Agent, DeferredToolRequests, DeferredToolResults
frompydantic_ai.models.testimport TestModel

fromprepared_toolsetimport prepared_toolset

approval_required_toolset = prepared_toolset.approval_required(lambda ctx, tool_def, tool_args: tool_def.name.startswith('temperature'))

test_model = TestModel(call_tools=['temperature_celsius', 'temperature_fahrenheit']) # (1)!
agent = Agent(
    test_model,
    toolsets=[approval_required_toolset],
    output_type=[str, DeferredToolRequests],
)
result = agent.run_sync('Call the temperature tools')
messages = result.all_messages()
print(result.output)
"""
DeferredToolRequests(
    calls=[],
    approvals=[
        ToolCallPart(
            tool_name='temperature_celsius',
            args={'city': 'a'},
            tool_call_id='pyd_ai_tool_call_id__temperature_celsius',
        ),
        ToolCallPart(
            tool_name='temperature_fahrenheit',
            args={'city': 'a'},
            tool_call_id='pyd_ai_tool_call_id__temperature_fahrenheit',
        ),
    ],
    metadata={},
)
"""

result = agent.run_sync(
    message_history=messages,
    deferred_tool_results=DeferredToolResults(
        approvals={
            'pyd_ai_tool_call_id__temperature_celsius': True,
            'pyd_ai_tool_call_id__temperature_fahrenheit': False,
        }
    )
)
print(result.output)
#> {"temperature_celsius":21.0,"temperature_fahrenheit":"The tool call was denied."}
```

1. We're using [`TestModel`](https://ai.pydantic.dev/api/models/test/#pydantic_ai.models.test.TestModel "TestModel            dataclass   ") here because it makes it easy to specify which tools to call.

*(This example is complete, it can be run "as is")*

### Changing Tool Execution

[`WrapperToolset`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.WrapperToolset "WrapperToolset            dataclass   ") wraps another toolset and delegates all responsibility to it.

It is is a no-op by default, but you can subclass `WrapperToolset` to change the wrapped toolset's tool execution behavior by overriding the [`call_tool()`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset.call_tool "call_tool            abstractmethod       async   ") method.

logging\_toolset.py

```
importasyncio

fromtyping_extensionsimport Any

frompydantic_aiimport Agent, RunContext, ToolsetTool, WrapperToolset
frompydantic_ai.models.testimport TestModel

fromprepared_toolsetimport prepared_toolset

LOG = []

classLoggingToolset(WrapperToolset):
    async defcall_tool(self, name: str, tool_args: dict[str, Any], ctx: RunContext, tool: ToolsetTool) -> Any:
        LOG.append(f'Calling tool {name!r} with args: {tool_args!r}')
        try:
            await asyncio.sleep(0.1 * len(LOG)) # (1)!

            result = await super().call_tool(name, tool_args, ctx, tool)
            LOG.append(f'Finished calling tool {name!r} with result: {result!r}')
        except Exception as e:
            LOG.append(f'Error calling tool {name!r}: {e}')
            raise e
        else:
            return result


logging_toolset = LoggingToolset(prepared_toolset)

agent = Agent(TestModel(), toolsets=[logging_toolset]) # (2)!
result = agent.run_sync('Call all the tools')
print(LOG)
"""
[
    "Calling tool 'temperature_celsius' with args: {'city': 'a'}",
    "Calling tool 'temperature_fahrenheit' with args: {'city': 'a'}",
    "Calling tool 'weather_conditions' with args: {'city': 'a'}",
    "Calling tool 'current_time' with args: {}",
    "Finished calling tool 'temperature_celsius' with result: 21.0",
    "Finished calling tool 'temperature_fahrenheit' with result: 69.8",
    'Finished calling tool \'weather_conditions\' with result: "It\'s raining"',
    "Finished calling tool 'current_time' with result: datetime.datetime(...)",
]
"""
```

1. All docs examples are tested in CI and their their output is verified, so we need `LOG` to always have the same order whenever this code is run. Since the tools could finish in any order, we sleep an increasing amount of time based on which number tool call we are to ensure that they finish (and log) in the same order they were called in.
2. We use [`TestModel`](https://ai.pydantic.dev/api/models/test/#pydantic_ai.models.test.TestModel "TestModel            dataclass   ") here as it will automatically call each tool.

*(This example is complete, it can be run "as is")*

If your agent needs to be able to call [external tools](https://ai.pydantic.dev/deferred-tools/#external-tool-execution) that are provided and executed by an upstream service or frontend, you can build an [`ExternalToolset`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.ExternalToolset "ExternalToolset") from a list of [`ToolDefinition`s](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition "ToolDefinition            dataclass   ") containing the tool names, arguments JSON schemas, and descriptions.

When the model calls an external tool, the call is considered to be ["deferred"](https://ai.pydantic.dev/deferred-tools/#deferred-tools), and the agent run will end with a [`DeferredToolRequests`](https://ai.pydantic.dev/api/output/#pydantic_ai.output.DeferredToolRequests "DeferredToolRequests            dataclass   ") output object with a `calls` list holding [`ToolCallPart`s](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart            dataclass   ") containing the tool name, validated arguments, and a unique tool call ID, which are expected to be passed to the upstream service or frontend that will produce the results.

When the tool call results are received from the upstream service or frontend, you can build a [`DeferredToolResults`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DeferredToolResults "DeferredToolResults            dataclass   ") object with a `calls` dictionary that maps each tool call ID to an arbitrary value to be returned to the model, a [`ToolReturn`](https://ai.pydantic.dev/tools-advanced/#advanced-tool-returns) object, or a [`ModelRetry`](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.ModelRetry "ModelRetry") exception in case the tool call failed and the model should [try again](https://ai.pydantic.dev/tools-advanced/#tool-retries). This `DeferredToolResults` object can then be provided to one of the agent run methods as `deferred_tool_results`, alongside the original run's [message history](https://ai.pydantic.dev/message-history/).

Note that you need to add `DeferredToolRequests` to the `Agent`'s or `agent.run()`'s [`output_type`](https://ai.pydantic.dev/output/#structured-output) so that the possible types of the agent run output are correctly inferred. For more information, see the [Deferred Tools](https://ai.pydantic.dev/deferred-tools/#deferred-tools) documentation.

To demonstrate, let us first define a simple agent *without* deferred tools:

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) deferred\_toolset\_agent.py

```
frompydanticimport BaseModel

frompydantic_aiimport Agent, FunctionToolset

toolset = FunctionToolset()


@toolset.tool
defget_default_language():
    return 'en-US'


@toolset.tool
defget_user_name():
    return 'David'


classPersonalizedGreeting(BaseModel):
    greeting: str
    language_code: str


agent = Agent('gateway/openai:gpt-5', toolsets=[toolset], output_type=PersonalizedGreeting)

result = agent.run_sync('Greet the user in a personalized way')
print(repr(result.output))
#> PersonalizedGreeting(greeting='Hello, David!', language_code='en-US')
```

deferred\_toolset\_agent.py

```
frompydanticimport BaseModel

frompydantic_aiimport Agent, FunctionToolset

toolset = FunctionToolset()


@toolset.tool
defget_default_language():
    return 'en-US'


@toolset.tool
defget_user_name():
    return 'David'


classPersonalizedGreeting(BaseModel):
    greeting: str
    language_code: str


agent = Agent('openai:gpt-5', toolsets=[toolset], output_type=PersonalizedGreeting)

result = agent.run_sync('Greet the user in a personalized way')
print(repr(result.output))
#> PersonalizedGreeting(greeting='Hello, David!', language_code='en-US')
```

Next, let's define a function that represents a hypothetical "run agent" API endpoint that can be called by the frontend and takes a list of messages to send to the model, a list of frontend tool definitions, and optional deferred tool results. This is where `ExternalToolset`, `DeferredToolRequests`, and `DeferredToolResults` come in:

deferred\_toolset\_api.py

```
frompydantic_aiimport (
    DeferredToolRequests,
    DeferredToolResults,
    ExternalToolset,
    ModelMessage,
    ToolDefinition,
)

fromdeferred_toolset_agentimport PersonalizedGreeting, agent


defrun_agent(
    messages: list[ModelMessage] = [],
    frontend_tools: list[ToolDefinition] = {},
    deferred_tool_results: DeferredToolResults | None = None,
) -> tuple[PersonalizedGreeting | DeferredToolRequests, list[ModelMessage]]:
    deferred_toolset = ExternalToolset(frontend_tools)
    result = agent.run_sync(
        toolsets=[deferred_toolset], # (1)!
        output_type=[agent.output_type, DeferredToolRequests], # (2)!
        message_history=messages, # (3)!
        deferred_tool_results=deferred_tool_results,
    )
    return result.output, result.new_messages()
```

1. As mentioned in the [Deferred Tools](https://ai.pydantic.dev/deferred-tools/#deferred-tools) documentation, these `toolsets` are additional to those provided to the `Agent` constructor
2. As mentioned in the [Deferred Tools](https://ai.pydantic.dev/deferred-tools/#deferred-tools) documentation, this `output_type` overrides the one provided to the `Agent` constructor, so we have to make sure to not lose it
3. We don't include an `user_prompt` keyword argument as we expect the frontend to provide it via `messages`

Now, imagine that the code below is implemented on the frontend, and `run_agent` stands in for an API call to the backend that runs the agent. This is where we actually execute the deferred tool calls and start a new run with the new result included:

deferred\_tools.py

```
frompydantic_aiimport (
    DeferredToolRequests,
    DeferredToolResults,
    ModelMessage,
    ModelRequest,
    ModelRetry,
    ToolDefinition,
    UserPromptPart,
)

fromdeferred_toolset_apiimport run_agent

frontend_tool_definitions = [
    ToolDefinition(
        name='get_preferred_language',
        parameters_json_schema={'type': 'object', 'properties': {'default_language': {'type': 'string'}}},
        description="Get the user's preferred language from their browser",
    )
]

defget_preferred_language(default_language: str) -> str:
    return 'es-MX' # (1)!

frontend_tool_functions = {'get_preferred_language': get_preferred_language}

messages: list[ModelMessage] = [
    ModelRequest(
        parts=[
            UserPromptPart(content='Greet the user in a personalized way')
        ]
    )
]

deferred_tool_results: DeferredToolResults | None = None

final_output = None
while True:
    output, new_messages = run_agent(messages, frontend_tool_definitions, deferred_tool_results)
    messages += new_messages

    if not isinstance(output, DeferredToolRequests):
        final_output = output
        break

    print(output.calls)
"""
    [
        ToolCallPart(
            tool_name='get_preferred_language',
            args={'default_language': 'en-US'},
            tool_call_id='pyd_ai_tool_call_id',
        )
    ]
    """
    deferred_tool_results = DeferredToolResults()
    for tool_call in output.calls:
        if function := frontend_tool_functions.get(tool_call.tool_name):
            result = function(**tool_call.args_as_dict())
        else:
            result = ModelRetry(f'Unknown tool {tool_call.tool_name!r}')
        deferred_tool_results.calls[tool_call.tool_call_id] = result

print(repr(final_output))
"""
PersonalizedGreeting(greeting='Hola, David! Espero que tengas un gran día!', language_code='es-MX')
"""
```

1. Imagine that this returns the frontend [`navigator.language`](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/language).

*(This example is complete, it can be run "as is")*

Toolsets can be built dynamically ahead of each agent run or run step using a function that takes the agent [run context](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext            dataclass   ") and returns a toolset or `None`. This is useful when a toolset (like an MCP server) depends on information specific to an agent run, like its [dependencies](https://ai.pydantic.dev/dependencies/).

To register a dynamic toolset, you can pass a function that takes [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext            dataclass   ") to the `toolsets` argument of the `Agent` constructor, or you can wrap a compliant function in the [`@agent.toolset`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.toolset "toolset") decorator.

By default, the function will be called again ahead of each agent run step. If you are using the decorator, you can optionally provide a `per_run_step=False` argument to indicate that the toolset only needs to be built once for the entire run.

dynamic\_toolset.py

```
fromdataclassesimport dataclass
fromtypingimport Literal

frompydantic_aiimport Agent, RunContext
frompydantic_ai.models.testimport TestModel

fromfunction_toolsetimport datetime_toolset, weather_toolset


@dataclass
classToggleableDeps:
    active: Literal['weather', 'datetime']

    deftoggle(self):
        if self.active == 'weather':
            self.active = 'datetime'
        else:
            self.active = 'weather'

test_model = TestModel()  # (1)!
agent = Agent(
    test_model,
    deps_type=ToggleableDeps  # (2)!
)

@agent.toolset
deftoggleable_toolset(ctx: RunContext[ToggleableDeps]):
    if ctx.deps.active == 'weather':
        return weather_toolset
    else:
        return datetime_toolset

@agent.tool
deftoggle(ctx: RunContext[ToggleableDeps]):
    ctx.deps.toggle()

deps = ToggleableDeps('weather')

result = agent.run_sync('Toggle the toolset', deps=deps)
print([t.name for t in test_model.last_model_request_parameters.function_tools])  # (3)!
#> ['toggle', 'now']

result = agent.run_sync('Toggle the toolset', deps=deps)
print([t.name for t in test_model.last_model_request_parameters.function_tools])
#> ['toggle', 'temperature_celsius', 'temperature_fahrenheit', 'conditions']
```

1. We're using [`TestModel`](https://ai.pydantic.dev/api/models/test/#pydantic_ai.models.test.TestModel "TestModel            dataclass   ") here because it makes it easy to see which tools were available on each run.
2. We're using the agent's dependencies to give the `toggle` tool access to the `active` via the `RunContext` argument.
3. This shows the available tools *after* the `toggle` tool was executed, as the "last model request" was the one that returned the `toggle` tool result to the model.

*(This example is complete, it can be run "as is")*

To define a fully custom toolset with its own logic to list available tools and handle them being called, you can subclass [`AbstractToolset`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset") and implement the [`get_tools()`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset.get_tools "get_tools            abstractmethod       async   ") and [`call_tool()`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset.call_tool "call_tool            abstractmethod       async   ") methods.

If you want to reuse a network connection or session across tool listings and calls during an agent run, you can implement [`__aenter__()`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset.__aenter__ "__aenter__            async   ") and [`__aexit__()`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset.__aexit__ "__aexit__            async   ").

### MCP Servers

Pydantic AI provides two toolsets that allow an agent to connect to and call tools on local and remote MCP Servers:

1. `MCPServer`: the [MCP SDK-based Client](https://ai.pydantic.dev/mcp/client/) which offers more direct control by leveraging the MCP SDK directly
2. `FastMCPToolset`: the [FastMCP-based Client](https://ai.pydantic.dev/mcp/fastmcp-client/) which offers additional capabilities like Tool Transformation, simpler OAuth configuration, and more.

### Task Management

Toolsets for task planning and progress tracking help agents organize complex work and provide visibility into agent progress:

- [`pydantic-ai-todo`](https://github.com/vstorm-co/pydantic-ai-todo) - `TodoToolset` with `read_todos` and `write_todos` tools. Included in the third-party [`pydantic-deep`](https://github.com/vstorm-co/pydantic-deepagents) [deep agent](https://ai.pydantic.dev/multi-agent-applications/#deep-agents) framework.

### File Operations

Toolsets for file operations help agents read, write, and edit files:

- [`pydantic-ai-filesystem-sandbox`](https://github.com/zby/pydantic-ai-filesystem-sandbox) - `FileSystemToolset` with a sandbox and LLM-friendly errors
- [`pydantic-deep`](https://github.com/vstorm-co/pydantic-deepagents) — Deep agent framework that includes a `FilesystemToolset` with multiple backends (in-memory, real filesystem, Docker sandbox).

### Code Execution

Toolsets for sandboxed code execution help agents run code in a sandboxed environment:

- [`mcp-run-python`](https://github.com/pydantic/mcp-run-python) - MCP server by the Pydantic team that runs Python code in a sandboxed environment. Can be used as `MCPServerStdio('uv', args=['run', 'mcp-run-python', 'stdio'])`.

### LangChain Tools

If you'd like to use tools or a [toolkit](https://python.langchain.com/docs/concepts/tools/#toolkits) from LangChain's [community tool library](https://python.langchain.com/docs/integrations/tools/) with Pydantic AI, you can use the [`LangChainToolset`](https://ai.pydantic.dev/api/ext/#pydantic_ai.ext.langchain.LangChainToolset "LangChainToolset") which takes a list of LangChain tools. Note that Pydantic AI will not validate the arguments in this case -- it's up to the model to provide arguments matching the schema specified by the LangChain tool, and up to the LangChain tool to raise an error if the arguments are invalid.

You will need to install the `langchain-community` package and any others required by the tools in question.

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway)

```
fromlangchain_community.agent_toolkitsimport SlackToolkit

frompydantic_aiimport Agent
frompydantic_ai.ext.langchainimport LangChainToolset

toolkit = SlackToolkit()
toolset = LangChainToolset(toolkit.get_tools())

agent = Agent('gateway/openai:gpt-5', toolsets=[toolset])
# ...
```

```
fromlangchain_community.agent_toolkitsimport SlackToolkit

frompydantic_aiimport Agent
frompydantic_ai.ext.langchainimport LangChainToolset

toolkit = SlackToolkit()
toolset = LangChainToolset(toolkit.get_tools())

agent = Agent('openai:gpt-5', toolsets=[toolset])
# ...
```

### ACI.dev Tools

If you'd like to use tools from the [ACI.dev tool library](https://www.aci.dev/tools) with Pydantic AI, you can use the [`ACIToolset`](https://ai.pydantic.dev/api/ext/#pydantic_ai.ext.aci.ACIToolset "ACIToolset") [toolset](https://ai.pydantic.dev/toolsets/) which takes a list of ACI tool names as well as the `linked_account_owner_id`. Note that Pydantic AI will not validate the arguments in this case -- it's up to the model to provide arguments matching the schema specified by the ACI tool, and up to the ACI tool to raise an error if the arguments are invalid.

You will need to install the `aci-sdk` package, set your ACI API key in the `ACI_API_KEY` environment variable, and pass your ACI "linked account owner ID" to the function.

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway)

```
importos

frompydantic_aiimport Agent
frompydantic_ai.ext.aciimport ACIToolset

toolset = ACIToolset(
    [
        'OPEN_WEATHER_MAP__CURRENT_WEATHER',
        'OPEN_WEATHER_MAP__FORECAST',
    ],
    linked_account_owner_id=os.getenv('LINKED_ACCOUNT_OWNER_ID'),
)

agent = Agent('gateway/openai:gpt-5', toolsets=[toolset])
```

```
importos

frompydantic_aiimport Agent
frompydantic_ai.ext.aciimport ACIToolset

toolset = ACIToolset(
    [
        'OPEN_WEATHER_MAP__CURRENT_WEATHER',
        'OPEN_WEATHER_MAP__FORECAST',
    ],
    linked_account_owner_id=os.getenv('LINKED_ACCOUNT_OWNER_ID'),
)

agent = Agent('openai:gpt-5', toolsets=[toolset])
```