---
title: Chat with a model
url: https://lmstudio.ai/docs/developer/rest/chat
source: sitemap
fetched_at: 2026-04-07T21:30:18.643665645-03:00
rendered_js: false
word_count: 901
summary: This document details the structure and parameters for a POST request to the `/api/v1/chat` endpoint, which is used to communicate with a model for chat interactions. It covers the required request body fields, optional configuration parameters like temperature and context length, and describes the various possible structures found within the response payload.
tags:
    - api-endpoint
    - chat-completion
    - model-parameters
    - request-body
    - response-schema
category: reference
---

`POST /api/v1/chat`

**Request body**

model : string

Unique identifier for the model to use.

input : string | array&lt;object&gt;

Message to send to the model.

Input text : string

Text content of the message.

Input object : object

Object representing a message with additional metadata.

Text Input (optional) : object

Text input to provide user messages

type : "message"

Type of input item.

content : string

Text content of the message.

Image Input (optional) : object

Image input to provide user messages

type : "image"

Type of input item.

data\_url : string

Image data as a base64-encoded data URL.

system\_prompt (optional) : string

System message that sets model behavior or instructions.

integrations (optional) : array&lt;string | object&gt;

List of integrations (plugins, ephemeral MCP servers, etc...) to enable for this request.

Plugin id : string

Unique identifier of a plugin to use. Plugins contain `mcp.json` installed MCP servers (id `mcp/<server_label>`). Shorthand for plugin object with no custom configuration.

Plugin : object

Specification of a plugin to use. Plugins contain `mcp.json` installed MCP servers (id `mcp/<server_label>`).

type : "plugin"

Type of integration.

id : string

Unique identifier of the plugin.

allowed\_tools (optional) : array&lt;string&gt;

List of tool names the model can call from this plugin. If not provided, all tools from the plugin are allowed.

Ephemeral MCP server specification : object

Specification of an ephemeral MCP server. Allows defining MCP servers on-the-fly without needing to pre-configure them in your `mcp.json`.

type : "ephemeral\_mcp"

Type of integration.

server\_label : string

Label to identify the MCP server.

server\_url : string

URL of the MCP server.

allowed\_tools (optional) : array&lt;string&gt;

List of tool names the model can call from this server. If not provided, all tools from the server are allowed.

headers (optional) : object

Custom HTTP headers to send with requests to the server.

stream (optional) : boolean

Whether to stream partial outputs via SSE. Default `false`. See [streaming events](https://lmstudio.ai/docs/developer/rest/streaming-events) for more information.

temperature (optional) : number

Randomness in token selection. 0 is deterministic, higher values increase creativity \[0,1].

top\_p (optional) : number

Minimum cumulative probability for the possible next tokens \[0,1].

top\_k (optional) : integer

Limits next token selection to top-k most probable tokens.

min\_p (optional) : number

Minimum base probability for a token to be selected for output \[0,1].

repeat\_penalty (optional) : number

Penalty for repeating token sequences. 1 is no penalty, higher values discourage repetition.

max\_output\_tokens (optional) : integer

Maximum number of tokens to generate.

reasoning (optional) : "off" | "low" | "medium" | "high" | "on"

Reasoning setting. Will error if the model being used does not support the reasoning setting using. Defaults to the automatically chosen setting for the model.

context\_length (optional) : integer

Number of tokens to consider as context. Higher values recommended for MCP usage.

store (optional) : boolean

Whether to store the chat. If set, response will return a `"response_id"` field. Default `true`.

previous\_response\_id (optional) : string

Identifier of existing response to append to. Must start with `"resp_"`.

* * *

**Response fields**

model\_instance\_id : string

Unique identifier for the loaded model instance that generated the response.

output : array&lt;object&gt;

Array of output items generated. Each item can be one of three types.

Message : object

A text message from the model.

type : "message"

Type of output item.

content : string

Text content of the message.

Tool call : object

A tool call made by the model.

type : "tool\_call"

Type of output item.

tool : string

Name of the tool called.

arguments : object

Arguments passed to the tool. Can have any keys/values depending on the tool definition.

output : string

Result returned from the tool.

provider\_info : object

Information about the tool provider.

type : "plugin" | "ephemeral\_mcp"

Provider type.

plugin\_id (optional) : string

Identifier of the plugin (when `type` is `"plugin"`).

server\_label (optional) : string

Label of the MCP server (when `type` is `"ephemeral_mcp"`).

Reasoning : object

Reasoning content from the model.

type : "reasoning"

Type of output item.

content : string

Text content of the reasoning.

Invalid tool call : object

An invalid tool call made by the model - due to invalid tool name or tool arguments.

type : "invalid\_tool\_call"

Type of output item.

reason : string

Reason why the tool call was invalid.

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

stats : object

Token usage and performance metrics.

input\_tokens : number

Number of input tokens. Includes formatting, tool definitions, and prior messages in the chat.

total\_output\_tokens : number

Total number of output tokens generated.

reasoning\_output\_tokens : number

Number of tokens used for reasoning.

tokens\_per\_second : number

Generation speed in tokens per second.

time\_to\_first\_token\_seconds : number

Time in seconds to generate the first token.

model\_load\_time\_seconds (optional) : number

Time taken to load the model for this request in seconds. Present only if the model was not already loaded.

response\_id (optional) : string

Identifier of the response for subsequent requests. Starts with `"resp_"`. Present when `store` is `true`.