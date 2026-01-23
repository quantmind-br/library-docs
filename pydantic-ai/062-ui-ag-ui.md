---
title: AG-UI - Pydantic AI
url: https://ai.pydantic.dev/ui/ag-ui/
source: sitemap
fetched_at: 2026-01-22T22:26:21.602882219-03:00
rendered_js: false
word_count: 1253
summary: This document explains how to implement the Agent-User Interaction (AG-UI) Protocol within Pydantic AI to standardize communication between AI agents and frontend applications. It details installation steps and provides multiple methods for handling streamed events using adapters and ASGI applications.
tags:
    - pydantic-ai
    - ag-ui-protocol
    - fastapi
    - agent-interaction
    - streaming-events
    - asgi
    - ai-agents
category: guide
---

## Agent-User Interaction (AG-UI) Protocol

The [Agent-User Interaction (AG-UI) Protocol](https://docs.ag-ui.com/introduction) is an open standard introduced by the [CopilotKit](https://webflow.copilotkit.ai/blog/introducing-ag-ui-the-protocol-where-agents-meet-users) team that standardises how frontend applications communicate with AI agents, with support for streaming, frontend tools, shared state, and custom events.

Note

The AG-UI integration was originally built by the team at [Rocket Science](https://www.rocketscience.gg/) and contributed in collaboration with the Pydantic AI and CopilotKit teams. Thanks Rocket Science!

## Installation

The only dependencies are:

- [ag-ui-protocol](https://docs.ag-ui.com/introduction): to provide the AG-UI types and encoder.
- [starlette](https://www.starlette.io): to handle [ASGI](https://asgi.readthedocs.io/en/latest/) requests from a framework like FastAPI.

You can install Pydantic AI with the `ag-ui` extra to ensure you have all the required AG-UI dependencies:

pipuv

```
pipinstall'pydantic-ai-slim[ag-ui]'
```

```
uvadd'pydantic-ai-slim[ag-ui]'
```

To run the examples you'll also need:

- [uvicorn](https://www.uvicorn.org/) or another ASGI compatible server

## Usage

There are three ways to run a Pydantic AI agent based on AG-UI run input with streamed AG-UI events as output, from most to least flexible. If you're using a Starlette-based web framework like FastAPI, you'll typically want to use the second method.

1. The [`AGUIAdapter.run_stream()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.run_stream "run_stream") method, when called on an [`AGUIAdapter`](https://ai.pydantic.dev/api/ui/ag_ui/#pydantic_ai.ui.ag_ui.AGUIAdapter "AGUIAdapter            dataclass   ") instantiated with an agent and an AG-UI [`RunAgentInput`](https://docs.ag-ui.com/sdk/python/core/types#runagentinput) object, will run the agent and return a stream of AG-UI events. It also takes optional [`Agent.iter()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.iter "iter            async   ") arguments including `deps`. Use this if you're using a web framework not based on Starlette (e.g. Django or Flask) or want to modify the input or output some way.
2. The [`AGUIAdapter.dispatch_request()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.dispatch_request "dispatch_request            async       classmethod   ") class method takes an agent and a Starlette request (e.g. from FastAPI) coming from an AG-UI frontend, and returns a streaming Starlette response of AG-UI events that you can return directly from your endpoint. It also takes optional [`Agent.iter()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.iter "iter            async   ") arguments including `deps`, that you can vary for each request (e.g. based on the authenticated user). This is a convenience method that combines [`AGUIAdapter.from_request()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.from_request "from_request            async       classmethod   "), [`AGUIAdapter.run_stream()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.run_stream "run_stream"), and [`AGUIAdapter.streaming_response()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.streaming_response "streaming_response").
3. [`AGUIApp`](https://ai.pydantic.dev/api/ui/ag_ui/#pydantic_ai.ui.ag_ui.app.AGUIApp "AGUIApp") represents an ASGI application that handles every AG-UI request by running the agent. It also takes optional [`Agent.iter()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.iter "iter            async   ") arguments including `deps`, but these will be the same for each request, with the exception of the AG-UI state that's injected as described under [state management](#state-management). This ASGI app can be [mounted](https://fastapi.tiangolo.com/advanced/sub-applications/) at a given path in an existing FastAPI app.

### Handle run input and output directly

This example uses [`AGUIAdapter.run_stream()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.run_stream "run_stream") and performs its own request parsing and response generation. This can be modified to work with any web framework.

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) run\_ag\_ui.py

```
importjson
fromhttpimport HTTPStatus

fromfastapiimport FastAPI
fromfastapi.requestsimport Request
fromfastapi.responsesimport Response, StreamingResponse
frompydanticimport ValidationError

frompydantic_aiimport Agent
frompydantic_ai.uiimport SSE_CONTENT_TYPE
frompydantic_ai.ui.ag_uiimport AGUIAdapter

agent = Agent('gateway/openai:gpt-5', instructions='Be fun!')

app = FastAPI()


@app.post('/')
async defrun_agent(request: Request) -> Response:
    accept = request.headers.get('accept', SSE_CONTENT_TYPE)
    try:
        run_input = AGUIAdapter.build_run_input(await request.body())  # (1)
    except ValidationError as e:
        return Response(
            content=json.dumps(e.json()),
            media_type='application/json',
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
        )

    adapter = AGUIAdapter(agent=agent, run_input=run_input, accept=accept)
    event_stream = adapter.run_stream() # (2)

    sse_event_stream = adapter.encode_stream(event_stream)
    return StreamingResponse(sse_event_stream, media_type=accept) # (3)
```

1. [`AGUIAdapter.build_run_input()`](https://ai.pydantic.dev/api/ui/ag_ui/#pydantic_ai.ui.ag_ui.AGUIAdapter.build_run_input "build_run_input            classmethod   ") takes the request body as bytes and returns an AG-UI [`RunAgentInput`](https://docs.ag-ui.com/sdk/python/core/types#runagentinput) object. You can also use the [`AGUIAdapter.from_request()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.from_request "from_request            async       classmethod   ") class method to build an adapter directly from a request.
2. [`AGUIAdapter.run_stream()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.run_stream "run_stream") runs the agent and returns a stream of AG-UI events. It supports the same optional arguments as [`Agent.run_stream_events()`](https://ai.pydantic.dev/agents/#running-agents), including `deps`. You can also use [`AGUIAdapter.run_stream_native()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.run_stream_native "run_stream_native") to run the agent and return a stream of Pydantic AI events instead, which can then be transformed into AG-UI events using [`AGUIAdapter.transform_stream()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.transform_stream "transform_stream").
3. [`AGUIAdapter.encode_stream()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.encode_stream "encode_stream") encodes the stream of AG-UI events as strings according to the accept header value. You can also use [`AGUIAdapter.streaming_response()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.streaming_response "streaming_response") to generate a streaming response directly from the AG-UI event stream returned by `run_stream()`.

run\_ag\_ui.py

```
importjson
fromhttpimport HTTPStatus

fromfastapiimport FastAPI
fromfastapi.requestsimport Request
fromfastapi.responsesimport Response, StreamingResponse
frompydanticimport ValidationError

frompydantic_aiimport Agent
frompydantic_ai.uiimport SSE_CONTENT_TYPE
frompydantic_ai.ui.ag_uiimport AGUIAdapter

agent = Agent('openai:gpt-5', instructions='Be fun!')

app = FastAPI()


@app.post('/')
async defrun_agent(request: Request) -> Response:
    accept = request.headers.get('accept', SSE_CONTENT_TYPE)
    try:
        run_input = AGUIAdapter.build_run_input(await request.body())  # (1)
    except ValidationError as e:
        return Response(
            content=json.dumps(e.json()),
            media_type='application/json',
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
        )

    adapter = AGUIAdapter(agent=agent, run_input=run_input, accept=accept)
    event_stream = adapter.run_stream() # (2)

    sse_event_stream = adapter.encode_stream(event_stream)
    return StreamingResponse(sse_event_stream, media_type=accept) # (3)
```

1. [`AGUIAdapter.build_run_input()`](https://ai.pydantic.dev/api/ui/ag_ui/#pydantic_ai.ui.ag_ui.AGUIAdapter.build_run_input "build_run_input            classmethod   ") takes the request body as bytes and returns an AG-UI [`RunAgentInput`](https://docs.ag-ui.com/sdk/python/core/types#runagentinput) object. You can also use the [`AGUIAdapter.from_request()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.from_request "from_request            async       classmethod   ") class method to build an adapter directly from a request.
2. [`AGUIAdapter.run_stream()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.run_stream "run_stream") runs the agent and returns a stream of AG-UI events. It supports the same optional arguments as [`Agent.run_stream_events()`](https://ai.pydantic.dev/agents/#running-agents), including `deps`. You can also use [`AGUIAdapter.run_stream_native()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.run_stream_native "run_stream_native") to run the agent and return a stream of Pydantic AI events instead, which can then be transformed into AG-UI events using [`AGUIAdapter.transform_stream()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.transform_stream "transform_stream").
3. [`AGUIAdapter.encode_stream()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.encode_stream "encode_stream") encodes the stream of AG-UI events as strings according to the accept header value. You can also use [`AGUIAdapter.streaming_response()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.streaming_response "streaming_response") to generate a streaming response directly from the AG-UI event stream returned by `run_stream()`.

Since `app` is an ASGI application, it can be used with any ASGI server:

This will expose the agent as an AG-UI server, and your frontend can start sending requests to it.

### Handle a Starlette request

This example uses [`AGUIAdapter.dispatch_request()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.dispatch_request "dispatch_request            async       classmethod   ") to directly handle a FastAPI request and return a response. Something analogous to this will work with any Starlette-based web framework.

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) handle\_ag\_ui\_request.py

```
fromfastapiimport FastAPI
fromstarlette.requestsimport Request
fromstarlette.responsesimport Response

frompydantic_aiimport Agent
frompydantic_ai.ui.ag_uiimport AGUIAdapter

agent = Agent('gateway/openai:gpt-5', instructions='Be fun!')

app = FastAPI()

@app.post('/')
async defrun_agent(request: Request) -> Response:
    return await AGUIAdapter.dispatch_request(request, agent=agent) # (1)
```

1. This method essentially does the same as the previous example, but it's more convenient to use when you're already using a Starlette/FastAPI app.

handle\_ag\_ui\_request.py

```
fromfastapiimport FastAPI
fromstarlette.requestsimport Request
fromstarlette.responsesimport Response

frompydantic_aiimport Agent
frompydantic_ai.ui.ag_uiimport AGUIAdapter

agent = Agent('openai:gpt-5', instructions='Be fun!')

app = FastAPI()

@app.post('/')
async defrun_agent(request: Request) -> Response:
    return await AGUIAdapter.dispatch_request(request, agent=agent) # (1)
```

1. This method essentially does the same as the previous example, but it's more convenient to use when you're already using a Starlette/FastAPI app.

Since `app` is an ASGI application, it can be used with any ASGI server:

```
uvicornhandle_ag_ui_request:app
```

This will expose the agent as an AG-UI server, and your frontend can start sending requests to it.

### Stand-alone ASGI app

This example uses [`AGUIApp`](https://ai.pydantic.dev/api/ui/ag_ui/#pydantic_ai.ui.ag_ui.app.AGUIApp "AGUIApp") to turn the agent into a stand-alone ASGI application:

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) ag\_ui\_app.py

```
frompydantic_aiimport Agent
frompydantic_ai.ui.ag_ui.appimport AGUIApp

agent = Agent('gateway/openai:gpt-5', instructions='Be fun!')
app = AGUIApp(agent)
```

ag\_ui\_app.py

```
frompydantic_aiimport Agent
frompydantic_ai.ui.ag_ui.appimport AGUIApp

agent = Agent('openai:gpt-5', instructions='Be fun!')
app = AGUIApp(agent)
```

Since `app` is an ASGI application, it can be used with any ASGI server:

This will expose the agent as an AG-UI server, and your frontend can start sending requests to it.

## Design

The Pydantic AI AG-UI integration supports all features of the spec:

- [Events](https://docs.ag-ui.com/concepts/events)
- [Messages](https://docs.ag-ui.com/concepts/messages)
- [State Management](https://docs.ag-ui.com/concepts/state)
- [Tools](https://docs.ag-ui.com/concepts/tools)

The integration receives messages in the form of a [`RunAgentInput`](https://docs.ag-ui.com/sdk/python/core/types#runagentinput) object that describes the details of the requested agent run including message history, state, and available tools.

These are converted to Pydantic AI types and passed to the agent's run method. Events from the agent, including tool calls, are converted to AG-UI events and streamed back to the caller as Server-Sent Events (SSE).

A user request may require multiple round trips between client UI and Pydantic AI server, depending on the tools and events needed.

## Features

### State management

The integration provides full support for [AG-UI state management](https://docs.ag-ui.com/concepts/state), which enables real-time synchronization between agents and frontend applications.

In the example below we have document state which is shared between the UI and server using the [`StateDeps`](https://ai.pydantic.dev/api/ag_ui/#pydantic_ai.ag_ui.StateDeps "StateDeps            dataclass   ") [dependencies type](https://ai.pydantic.dev/dependencies/) that can be used to automatically validate state contained in [`RunAgentInput.state`](https://docs.ag-ui.com/sdk/js/core/types#runagentinput) using a Pydantic `BaseModel` specified as a generic parameter.

Custom dependencies type with AG-UI state

If you want to use your own dependencies type to hold AG-UI state as well as other things, it needs to implements the [`StateHandler`](https://ai.pydantic.dev/api/ag_ui/#pydantic_ai.ag_ui.StateHandler "StateHandler") protocol, meaning it needs to be a [dataclass](https://docs.python.org/3/library/dataclasses.html) with a non-optional `state` field. This lets Pydantic AI ensure that state is properly isolated between requests by building a new dependencies object each time.

If the `state` field's type is a Pydantic `BaseModel` subclass, the raw state dictionary on the request is automatically validated. If not, you can validate the raw value yourself in your dependencies dataclass's `__post_init__` method.

If AG-UI state is provided but your dependencies do not implement [`StateHandler`](https://ai.pydantic.dev/api/ag_ui/#pydantic_ai.ag_ui.StateHandler "StateHandler"), Pydantic AI will emit a warning and ignore the state. Use [`StateDeps`](https://ai.pydantic.dev/api/ag_ui/#pydantic_ai.ag_ui.StateDeps "StateDeps            dataclass   ") or a custom [`StateHandler`](https://ai.pydantic.dev/api/ag_ui/#pydantic_ai.ag_ui.StateHandler "StateHandler") implementation to receive and validate the incoming state.

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) ag\_ui\_state.py

```
frompydanticimport BaseModel

frompydantic_aiimport Agent
frompydantic_ai.uiimport StateDeps
frompydantic_ai.ui.ag_ui.appimport AGUIApp


classDocumentState(BaseModel):
"""State for the document being written."""

    document: str = ''


agent = Agent(
    'gateway/openai:gpt-5',
    instructions='Be fun!',
    deps_type=StateDeps[DocumentState],
)
app = AGUIApp(agent, deps=StateDeps(DocumentState()))
```

ag\_ui\_state.py

```
frompydanticimport BaseModel

frompydantic_aiimport Agent
frompydantic_ai.uiimport StateDeps
frompydantic_ai.ui.ag_ui.appimport AGUIApp


classDocumentState(BaseModel):
"""State for the document being written."""

    document: str = ''


agent = Agent(
    'openai:gpt-5',
    instructions='Be fun!',
    deps_type=StateDeps[DocumentState],
)
app = AGUIApp(agent, deps=StateDeps(DocumentState()))
```

Since `app` is an ASGI application, it can be used with any ASGI server:

```
uvicornag_ui_state:app--host0.0.0.0--port9000
```

### Tools

AG-UI frontend tools are seamlessly provided to the Pydantic AI agent, enabling rich user experiences with frontend user interfaces.

### Events

Pydantic AI tools can send [AG-UI events](https://docs.ag-ui.com/concepts/events) simply by returning a [`ToolReturn`](https://ai.pydantic.dev/tools-advanced/#advanced-tool-returns) object with a [`BaseEvent`](https://docs.ag-ui.com/sdk/python/core/events#baseevent) (or a list of events) as `metadata`, which allows for custom events and state updates.

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) ag\_ui\_tool\_events.py

```
fromag_ui.coreimport CustomEvent, EventType, StateSnapshotEvent
frompydanticimport BaseModel

frompydantic_aiimport Agent, RunContext, ToolReturn
frompydantic_ai.uiimport StateDeps
frompydantic_ai.ui.ag_ui.appimport AGUIApp


classDocumentState(BaseModel):
"""State for the document being written."""

    document: str = ''


agent = Agent(
    'gateway/openai:gpt-5',
    instructions='Be fun!',
    deps_type=StateDeps[DocumentState],
)
app = AGUIApp(agent, deps=StateDeps(DocumentState()))


@agent.tool
async defupdate_state(ctx: RunContext[StateDeps[DocumentState]]) -> ToolReturn:
    return ToolReturn(
        return_value='State updated',
        metadata=[
            StateSnapshotEvent(
                type=EventType.STATE_SNAPSHOT,
                snapshot=ctx.deps.state,
            ),
        ],
    )


@agent.tool_plain
async defcustom_events() -> ToolReturn:
    return ToolReturn(
        return_value='Count events sent',
        metadata=[
            CustomEvent(
                type=EventType.CUSTOM,
                name='count',
                value=1,
            ),
            CustomEvent(
                type=EventType.CUSTOM,
                name='count',
                value=2,
            ),
        ]
    )
```

ag\_ui\_tool\_events.py

```
fromag_ui.coreimport CustomEvent, EventType, StateSnapshotEvent
frompydanticimport BaseModel

frompydantic_aiimport Agent, RunContext, ToolReturn
frompydantic_ai.uiimport StateDeps
frompydantic_ai.ui.ag_ui.appimport AGUIApp


classDocumentState(BaseModel):
"""State for the document being written."""

    document: str = ''


agent = Agent(
    'openai:gpt-5',
    instructions='Be fun!',
    deps_type=StateDeps[DocumentState],
)
app = AGUIApp(agent, deps=StateDeps(DocumentState()))


@agent.tool
async defupdate_state(ctx: RunContext[StateDeps[DocumentState]]) -> ToolReturn:
    return ToolReturn(
        return_value='State updated',
        metadata=[
            StateSnapshotEvent(
                type=EventType.STATE_SNAPSHOT,
                snapshot=ctx.deps.state,
            ),
        ],
    )


@agent.tool_plain
async defcustom_events() -> ToolReturn:
    return ToolReturn(
        return_value='Count events sent',
        metadata=[
            CustomEvent(
                type=EventType.CUSTOM,
                name='count',
                value=1,
            ),
            CustomEvent(
                type=EventType.CUSTOM,
                name='count',
                value=2,
            ),
        ]
    )
```

Since `app` is an ASGI application, it can be used with any ASGI server:

```
uvicornag_ui_tool_events:app--host0.0.0.0--port9000
```

## Examples

For more examples of how to use [`AGUIApp`](https://ai.pydantic.dev/api/ui/ag_ui/#pydantic_ai.ui.ag_ui.app.AGUIApp "AGUIApp") see [`pydantic_ai_examples.ag_ui`](https://github.com/pydantic/pydantic-ai/tree/main/examples/pydantic_ai_examples/ag_ui), which includes a server for use with the [AG-UI Dojo](https://docs.ag-ui.com/tutorials/debugging#the-ag-ui-dojo).