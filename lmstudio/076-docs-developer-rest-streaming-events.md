---
title: Streaming events
url: https://lmstudio.ai/docs/developer/rest/streaming-events
source: sitemap
fetched_at: 2026-04-07T21:30:16.932173578-03:00
rendered_js: false
word_count: 1064
summary: This document details the structure and various types of named events streamed via Server-Sent Events (SSE) when calling the `/api/v1/chat` endpoint for incremental chat response rendering. It covers lifecycle stages such as model loading, prompt processing, reasoning, tool calling, message streaming, and final error handling.
tags:
    - sse
    - streaming-events
    - chat-api
    - event-types
    - tool-calling
    - model-response
category: reference
---

Streaming events let you render chat responses incrementally over Server‑Sent Events (SSE). When you call `POST /api/v1/chat` with `stream: true`, the server emits a series of named events that you can consume. These events arrive in order and may include multiple deltas (for reasoning and message content), tool call boundaries and payloads, and any errors encountered. The stream always begins with `chat.start` and concludes with `chat.end`, which contains the aggregated result equivalent to a non‑streaming response.

List of event types that can be sent in an `/api/v1/chat` response stream:

- `chat.start`
- `model_load.start`
- `model_load.progress`
- `model_load.end`
- `prompt_processing.start`
- `prompt_processing.progress`
- `prompt_processing.end`
- `reasoning.start`
- `reasoning.delta`
- `reasoning.end`
- `tool_call.start`
- `tool_call.arguments`
- `tool_call.success`
- `tool_call.failure`
- `message.start`
- `message.delta`
- `message.end`
- `error`
- `chat.end`

Events will be streamed out in the following raw format:

```

event: <event type>
data: <JSON event data>
```

### `chat.start`[](#chatstart)

An event that is emitted at the start of a chat response stream.

model\_instance\_id : string

Unique identifier for the loaded model instance that will generate the response.

type : "chat.start"

The type of the event. Always `chat.start`.

### `model_load.start`[](#modelloadstart)

Signals the start of a model being loaded to fulfill the chat request. Will not be emitted if the requested model is already loaded.

model\_instance\_id : string

Unique identifier for the model instance being loaded.

type : "model\_load.start"

The type of the event. Always `model_load.start`.

### `model_load.progress`[](#modelloadprogress)

Progress of the model load.

model\_instance\_id : string

Unique identifier for the model instance being loaded.

progress : number

Progress of the model load as a float between `0` and `1`.

type : "model\_load.progress"

The type of the event. Always `model_load.progress`.

### `model_load.end`[](#modelloadend)

Signals a successfully completed model load.

model\_instance\_id : string

Unique identifier for the model instance that was loaded.

load\_time\_seconds : number

Time taken to load the model in seconds.

type : "model\_load.end"

The type of the event. Always `model_load.end`.

### `prompt_processing.start`[](#promptprocessingstart)

Signals the start of the model processing a prompt.

type : "prompt\_processing.start"

The type of the event. Always `prompt_processing.start`.

### `prompt_processing.progress`[](#promptprocessingprogress)

Progress of the model processing a prompt.

progress : number

Progress of the prompt processing as a float between `0` and `1`.

type : "prompt\_processing.progress"

The type of the event. Always `prompt_processing.progress`.

### `prompt_processing.end`[](#promptprocessingend)

Signals the end of the model processing a prompt.

type : "prompt\_processing.end"

The type of the event. Always `prompt_processing.end`.

### `reasoning.start`[](#reasoningstart)

Signals the model is starting to stream reasoning content.

type : "reasoning.start"

The type of the event. Always `reasoning.start`.

### `reasoning.delta`[](#reasoningdelta)

A chunk of reasoning content. Multiple deltas may arrive.

content : string

Reasoning text fragment.

type : "reasoning.delta"

The type of the event. Always `reasoning.delta`.

### `reasoning.end`[](#reasoningend)

Signals the end of the reasoning stream.

type : "reasoning.end"

The type of the event. Always `reasoning.end`.

### `tool_call.start`[](#toolcallstart)

Emitted when the model starts a tool call.

tool : string

Name of the tool being called.

provider\_info : object

Information about the tool provider. Discriminated union upon possible provider types.

Plugin provider info : object

Present when the tool is provided by a plugin.

type : "plugin"

Provider type.

plugin\_id : string

Identifier of the plugin.

Ephemeral MCP provider info : object

Present when the tool is provided by a ephemeral MCP server.

type : "ephemeral\_mcp"

Provider type.

server\_label : string

Label of the MCP server.

type : "tool\_call.start"

The type of the event. Always `tool_call.start`.

### `tool_call.arguments`[](#toolcallarguments)

Arguments streamed for the current tool call.

tool : string

Name of the tool being called.

arguments : object

Arguments passed to the tool. Can have any keys/values depending on the tool definition.

provider\_info : object

Information about the tool provider. Discriminated union upon possible provider types.

Plugin provider info : object

Present when the tool is provided by a plugin.

type : "plugin"

Provider type.

plugin\_id : string

Identifier of the plugin.

Ephemeral MCP provider info : object

Present when the tool is provided by a ephemeral MCP server.

type : "ephemeral\_mcp"

Provider type.

server\_label : string

Label of the MCP server.

type : "tool\_call.arguments"

The type of the event. Always `tool_call.arguments`.

### `tool_call.success`[](#toolcallsuccess)

Result of the tool call, along with the arguments used.

tool : string

Name of the tool that was called.

arguments : object

Arguments that were passed to the tool.

output : string

Raw tool output string.

provider\_info : object

Information about the tool provider. Discriminated union upon possible provider types.

Plugin provider info : object

Present when the tool is provided by a plugin.

type : "plugin"

Provider type.

plugin\_id : string

Identifier of the plugin.

Ephemeral MCP provider info : object

Present when the tool is provided by a ephemeral MCP server.

type : "ephemeral\_mcp"

Provider type.

server\_label : string

Label of the MCP server.

type : "tool\_call.success"

The type of the event. Always `tool_call.success`.

### `tool_call.failure`[](#toolcallfailure)

Indicates that the tool call failed.

reason : string

Reason for the tool call failure.

metadata : object

Metadata about the invalid tool call.

type : "invalid\_name" | "invalid\_arguments"

Type of error that occurred.

tool\_name : string

Name of the tool that was attempted to be called.

arguments (optional) : object

Arguments that were passed to the tool (only present for `invalid_arguments` errors).

provider\_info (optional) : object

Information about the tool provider (only present for `invalid_arguments` errors).

type : "plugin" | "ephemeral\_mcp"

Provider type.

plugin\_id (optional) : string

Identifier of the plugin (when `type` is `"plugin"`).

server\_label (optional) : string

Label of the MCP server (when `type` is `"ephemeral_mcp"`).

type : "tool\_call.failure"

The type of the event. Always `tool_call.failure`.

### `message.start`[](#messagestart)

Signals the model is about to stream a message.

type : "message.start"

The type of the event. Always `message.start`.

### `message.delta`[](#messagedelta)

A chunk of message content. Multiple deltas may arrive.

content : string

Message text fragment.

type : "message.delta"

The type of the event. Always `message.delta`.

### `message.end`[](#messageend)

Signals the end of the message stream.

type : "message.end"

The type of the event. Always `message.end`.

### `error`[](#error)

An error occurred during streaming. The final payload will still be sent in `chat.end` with whatever was generated.

error : object

Error information.

type : "invalid\_request" | "unknown" | "mcp\_connection\_error" | "plugin\_connection\_error" | "not\_implemented" | "model\_not\_found" | "job\_not\_found" | "internal\_error"

High-level error type.

message : string

Human-readable error message.

code (optional) : string

More detailed error code (e.g., validation issue code).

param (optional) : string

Parameter associated with the error, if applicable.

type : "error"

The type of the event. Always `error`.

### `chat.end`[](#chatend)

Final event containing the full aggregated response, equivalent to the non-streaming `POST /api/v1/chat` response body.

result : object

Final response with `model_instance_id`, `output`, `stats`, and optional `response_id`. See [non-streaming chat docs](https://lmstudio.ai/docs/developer/rest/chat) for more details.

type : "chat.end"

The type of the event. Always `chat.end`.