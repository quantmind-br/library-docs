---
title: Overview - Pydantic AI
url: https://ai.pydantic.dev/ui/overview/
source: sitemap
fetched_at: 2026-01-22T22:26:22.141704945-03:00
rendered_js: false
word_count: 570
summary: This document explains how to stream real-time agent events to frontends using UI event stream protocols like AG-UI and Vercel AI through the UIAdapter interface. It provides implementation details for Starlette-based frameworks like FastAPI as well as advanced usage for other web frameworks.
tags:
    - pydantic-ai
    - ui-event-streams
    - streaming-responses
    - fastapi
    - ag-ui
    - vercel-ai-protocol
    - server-sent-events
category: guide
---

## UI Event Streams

If you're building a chat app or other interactive frontend for an AI agent, your backend will need to receive agent run input (like a chat message or complete [message history](https://ai.pydantic.dev/message-history/)) from the frontend, and will need to stream the [agent's events](https://ai.pydantic.dev/agents/#streaming-all-events) (like text, thinking, and tool calls) to the frontend so that the user knows what's happening in real time.

While your frontend could use Pydantic AI's [`ModelRequest`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest "ModelRequest            dataclass   ") and [`AgentStreamEvent`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AgentStreamEvent "AgentStreamEvent            module-attribute   ") directly, you'll typically want to use a UI event stream protocol that's natively supported by your frontend framework.

Pydantic AI natively supports two UI event stream protocols:

- [Agent-User Interaction (AG-UI) Protocol](https://ai.pydantic.dev/ui/ag-ui/)
- [Vercel AI Data Stream Protocol](https://ai.pydantic.dev/ui/vercel-ai/)

These integrations are implemented as subclasses of the abstract [`UIAdapter`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter "UIAdapter            dataclass   ") class, so they also serve as a reference for integrating with other UI event stream protocols.

## Usage

The protocol-specific [`UIAdapter`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter "UIAdapter            dataclass   ") subclass (i.e. [`AGUIAdapter`](https://ai.pydantic.dev/api/ui/ag_ui/#pydantic_ai.ui.ag_ui.AGUIAdapter "AGUIAdapter            dataclass   ") or [`VercelAIAdapter`](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.VercelAIAdapter "VercelAIAdapter            dataclass   ")) is responsible for transforming agent run input received from the frontend into arguments for [`Agent.run_stream_events()`](https://ai.pydantic.dev/agents/#running-agents), running the agent, and then transforming Pydantic AI events into protocol-specific events. The event stream transformation is handled by a protocol-specific [`UIEventStream`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIEventStream "UIEventStream            dataclass   ") subclass, but you typically won't use this directly.

If you're using a Starlette-based web framework like FastAPI, you can use the [`UIAdapter.dispatch_request()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.dispatch_request "dispatch_request            async       classmethod   ") class method from an endpoint function to directly handle a request and return a streaming response of protocol-specific events. This is demonstrated in the next section.

If you're using a web framework not based on Starlette (e.g. Django or Flask) or need fine-grained control over the input or output, you can create a `UIAdapter` instance and directly use its methods. This is demonstrated in "Advanced Usage" section below.

### Usage with Starlette/FastAPI

Besides the request, [`UIAdapter.dispatch_request()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.dispatch_request "dispatch_request            async       classmethod   ") takes the agent, the same optional arguments as [`Agent.run_stream_events()`](https://ai.pydantic.dev/agents/#running-agents), and an optional `on_complete` callback function that receives the completed [`AgentRunResult`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult "AgentRunResult            dataclass   ") and can optionally yield additional protocol-specific events.

Note

These examples use the `VercelAIAdapter`, but the same patterns apply to all `UIAdapter` subclasses.

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) dispatch\_request.py

```
fromfastapiimport FastAPI
fromstarlette.requestsimport Request
fromstarlette.responsesimport Response

frompydantic_aiimport Agent
frompydantic_ai.ui.vercel_aiimport VercelAIAdapter

agent = Agent('gateway/openai:gpt-5')

app = FastAPI()

@app.post('/chat')
async defchat(request: Request) -> Response:
    return await VercelAIAdapter.dispatch_request(request, agent=agent)
```

dispatch\_request.py

```
fromfastapiimport FastAPI
fromstarlette.requestsimport Request
fromstarlette.responsesimport Response

frompydantic_aiimport Agent
frompydantic_ai.ui.vercel_aiimport VercelAIAdapter

agent = Agent('openai:gpt-5')

app = FastAPI()

@app.post('/chat')
async defchat(request: Request) -> Response:
    return await VercelAIAdapter.dispatch_request(request, agent=agent)
```

### Advanced Usage

If you're using a web framework not based on Starlette (e.g. Django or Flask) or need fine-grained control over the input or output, you can create a `UIAdapter` instance and directly use its methods, which can be chained to accomplish the same thing as the `UIAdapter.dispatch_request()` class method shown above:

1. The [`UIAdapter.build_run_input()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.build_run_input "build_run_input            abstractmethod       classmethod   ") class method takes the request body as bytes and returns a protocol-specific run input object, which you can then pass to the [`UIAdapter()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter "UIAdapter            dataclass   ") constructor along with the agent.
   
   - You can also use the [`UIAdapter.from_request()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.from_request "from_request            async       classmethod   ") class method to build an adapter directly from a Starlette/FastAPI request.
2. The [`UIAdapter.run_stream()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.run_stream "run_stream") method runs the agent and returns a stream of protocol-specific events. It supports the same optional arguments as [`Agent.run_stream_events()`](https://ai.pydantic.dev/agents/#running-agents) and an optional `on_complete` callback function that receives the completed [`AgentRunResult`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult "AgentRunResult            dataclass   ") and can optionally yield additional protocol-specific events.
   
   - You can also use [`UIAdapter.run_stream_native()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.run_stream_native "run_stream_native") to run the agent and return a stream of Pydantic AI events instead, which can then be transformed into protocol-specific events using [`UIAdapter.transform_stream()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.transform_stream "transform_stream").
3. The [`UIAdapter.encode_stream()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.encode_stream "encode_stream") method encodes the stream of protocol-specific events as SSE (HTTP Server-Sent Events) strings, which you can then return as a streaming response.
   
   - You can also use [`UIAdapter.streaming_response()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.streaming_response "streaming_response") to generate a Starlette/FastAPI streaming response directly from the protocol-specific event stream returned by `run_stream()`.

Note

This example uses FastAPI, but can be modified to work with any web framework.

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) run\_stream.py

```
importjson
fromhttpimport HTTPStatus

fromfastapiimport FastAPI
fromfastapi.requestsimport Request
fromfastapi.responsesimport Response, StreamingResponse
frompydanticimport ValidationError

frompydantic_aiimport Agent
frompydantic_ai.uiimport SSE_CONTENT_TYPE
frompydantic_ai.ui.vercel_aiimport VercelAIAdapter

agent = Agent('gateway/openai:gpt-5')

app = FastAPI()


@app.post('/chat')
async defchat(request: Request) -> Response:
    accept = request.headers.get('accept', SSE_CONTENT_TYPE)
    try:
        run_input = VercelAIAdapter.build_run_input(await request.body())
    except ValidationError as e:
        return Response(
            content=json.dumps(e.json()),
            media_type='application/json',
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
        )

    adapter = VercelAIAdapter(agent=agent, run_input=run_input, accept=accept)
    event_stream = adapter.run_stream()

    sse_event_stream = adapter.encode_stream(event_stream)
    return StreamingResponse(sse_event_stream, media_type=accept)
```

run\_stream.py

```
importjson
fromhttpimport HTTPStatus

fromfastapiimport FastAPI
fromfastapi.requestsimport Request
fromfastapi.responsesimport Response, StreamingResponse
frompydanticimport ValidationError

frompydantic_aiimport Agent
frompydantic_ai.uiimport SSE_CONTENT_TYPE
frompydantic_ai.ui.vercel_aiimport VercelAIAdapter

agent = Agent('openai:gpt-5')

app = FastAPI()


@app.post('/chat')
async defchat(request: Request) -> Response:
    accept = request.headers.get('accept', SSE_CONTENT_TYPE)
    try:
        run_input = VercelAIAdapter.build_run_input(await request.body())
    except ValidationError as e:
        return Response(
            content=json.dumps(e.json()),
            media_type='application/json',
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
        )

    adapter = VercelAIAdapter(agent=agent, run_input=run_input, accept=accept)
    event_stream = adapter.run_stream()

    sse_event_stream = adapter.encode_stream(event_stream)
    return StreamingResponse(sse_event_stream, media_type=accept)
```