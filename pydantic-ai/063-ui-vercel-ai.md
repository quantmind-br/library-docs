---
title: Vercel AI - Pydantic AI
url: https://ai.pydantic.dev/ui/vercel-ai/
source: sitemap
fetched_at: 2026-01-22T22:26:24.067730173-03:00
rendered_js: false
word_count: 453
summary: This document explains how to use Pydantic AI's VercelAIAdapter to integrate with the Vercel AI Data Stream Protocol for streaming agent events to frontends.
tags:
    - pydantic-ai
    - vercel-ai-sdk
    - data-stream-protocol
    - fastapi
    - streaming-events
    - server-sent-events
category: guide
---

## Vercel AI Data Stream Protocol

Pydantic AI natively supports the [Vercel AI Data Stream Protocol](https://ai-sdk.dev/docs/ai-sdk-ui/stream-protocol#data-stream-protocol) to receive agent run input from, and stream events to, a [Vercel AI Elements](https://ai-sdk.dev/elements) frontend.

## Usage

The [`VercelAIAdapter`](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.VercelAIAdapter "VercelAIAdapter            dataclass   ") class is responsible for transforming agent run input received from the frontend into arguments for [`Agent.run_stream_events()`](https://ai.pydantic.dev/agents/#running-agents), running the agent, and then transforming Pydantic AI events into Vercel AI events. The event stream transformation is handled by the [`VercelAIEventStream`](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.VercelAIEventStream "VercelAIEventStream            dataclass   ") class, but you typically won't use this directly.

If you're using a Starlette-based web framework like FastAPI, you can use the [`VercelAIAdapter.dispatch_request()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.dispatch_request "dispatch_request            async       classmethod   ") class method from an endpoint function to directly handle a request and return a streaming response of Vercel AI events. This is demonstrated in the next section.

If you're using a web framework not based on Starlette (e.g. Django or Flask) or need fine-grained control over the input or output, you can create a `VercelAIAdapter` instance and directly use its methods. This is demonstrated in "Advanced Usage" section below.

### Usage with Starlette/FastAPI

Besides the request, [`VercelAIAdapter.dispatch_request()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.dispatch_request "dispatch_request            async       classmethod   ") takes the agent, the same optional arguments as [`Agent.run_stream_events()`](https://ai.pydantic.dev/agents/#running-agents), and an optional `on_complete` callback function that receives the completed [`AgentRunResult`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult "AgentRunResult            dataclass   ") and can optionally yield additional Vercel AI events.

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

If you're using a web framework not based on Starlette (e.g. Django or Flask) or need fine-grained control over the input or output, you can create a `VercelAIAdapter` instance and directly use its methods, which can be chained to accomplish the same thing as the `VercelAIAdapter.dispatch_request()` class method shown above:

1. The [`VercelAIAdapter.build_run_input()`](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.VercelAIAdapter.build_run_input "build_run_input            classmethod   ") class method takes the request body as bytes and returns a Vercel AI [`RequestData`](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.RequestData "RequestData            module-attribute   ") run input object, which you can then pass to the [`VercelAIAdapter()`](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.VercelAIAdapter "VercelAIAdapter            dataclass   ") constructor along with the agent.
   
   - You can also use the [`VercelAIAdapter.from_request()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.from_request "from_request            async       classmethod   ") class method to build an adapter directly from a Starlette/FastAPI request.
2. The [`VercelAIAdapter.run_stream()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.run_stream "run_stream") method runs the agent and returns a stream of Vercel AI events. It supports the same optional arguments as [`Agent.run_stream_events()`](https://ai.pydantic.dev/agents/#running-agents) and an optional `on_complete` callback function that receives the completed [`AgentRunResult`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult "AgentRunResult            dataclass   ") and can optionally yield additional Vercel AI events.
   
   - You can also use [`VercelAIAdapter.run_stream_native()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.run_stream_native "run_stream_native") to run the agent and return a stream of Pydantic AI events instead, which can then be transformed into Vercel AI events using [`VercelAIAdapter.transform_stream()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.transform_stream "transform_stream").
3. The [`VercelAIAdapter.encode_stream()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.encode_stream "encode_stream") method encodes the stream of Vercel AI events as SSE (HTTP Server-Sent Events) strings, which you can then return as a streaming response.
   
   - You can also use [`VercelAIAdapter.streaming_response()`](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter.streaming_response "streaming_response") to generate a Starlette/FastAPI streaming response directly from the Vercel AI event stream returned by `run_stream()`.

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