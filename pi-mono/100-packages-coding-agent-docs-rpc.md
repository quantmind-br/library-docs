---
title: Rpc
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/rpc.md
source: git
fetched_at: 2026-05-03T09:31:18.358013713-03:00
rendered_js: false
word_count: 1194
summary: JSON-based RPC protocol over stdin/stdout for headless pi-coding-agent operation, including commands, events, extension UI, types, and client examples.
tags:
    - rpc
    - json-protocol
    - headless-mode
    - cli-automation
    - ipc
    - agent-integration
category: reference
optimized: true
optimized_at: 2026-05-03T13:07:00Z
---
# RPC Mode

Headless agent operation via JSONL protocol over stdin/stdout. Embed in IDEs, custom UIs, or automated pipelines.

> [!note]
> For Node.js/TypeScript applications, consider `AgentSession` from `@mariozechner/pi-coding-agent` directly instead of subprocess spawning. See [`src/core/agent-session.ts`](../src/core/agent-session.ts) and [`src/modes/rpc/rpc-client.ts`](../src/modes/rpc/rpc-client.ts).

## Starting RPC Mode

```bash
pi --mode rpc [options]
```

| Option | Description |
|--------|-------------|
| `--provider <name>` | LLM provider (anthropic, openai, google, etc.) |
| `--model <pattern>` | Model pattern or ID (`provider/id` or `provider/id:<thinking>`) |
| `--no-session` | Disable session persistence |
| `--session-dir <path>` | Custom session storage directory |

## Protocol Overview

- **Commands**: JSON objects to stdin, one per line
- **Responses**: JSON with `type: "response"` indicating success/failure
- **Events**: Agent events streamed to stdout as JSON lines

Optional `id` field enables request/response correlation.

### Framing

Strict JSONL with LF (`\n`) as sole record delimiter. Clients must:
- Split on `\n` only
- Strip optional trailing `\r`
- Avoid generic line readers that split on Unicode separators (`U+2028`, `U+2029`)

> [!warning]
> Node `readline` is not protocol-compliant — it splits on `U+2028`/`U+2029`.

## Commands

### Prompting

#### `prompt`

Send a user prompt. Events stream asynchronously after acceptance.

```json
{"id": "req-1", "type": "prompt", "message": "Hello, world!"}
```

With images:
```json
{"type": "prompt", "message": "What's in this image?", "images": [{"type": "image", "data": "base64-encoded-data", "mimeType": "image/png"}]}
```

**During streaming**: Specify `streamingBehavior` to queue:

| Value | Behavior |
|-------|----------|
| `"steer"` | Queue until current turn finishes tool calls, deliver before next LLM call |
| `"followUp"` | Wait until agent stops, deliver then |

Omitting `streamingBehavior` while streaming returns an error.

**Extension commands** (`/mycommand`) execute immediately during streaming. Extension commands manage their own LLM interaction via `pi.sendMessage()`.

**Skill commands** (`/skill:name`) and **prompt templates** (`/template`) expand before sending.

Response:
```json
{"id": "req-1", "type": "response", "command": "prompt", "success": true}
```

`success: true` = accepted/queued/handled. `success: false` = rejected before acceptance. Post-acceptance failures stream via normal events.

#### `steer`

Queue steering message. Delivered after current turn finishes tool calls, before next LLM call. Skill templates expand; extension commands not allowed.

```json
{"type": "steer", "message": "Stop and do this instead"}
```

With images:
```json
{"type": "steer", "message": "Look at this instead", "images": [{"type": "image", "data": "base64-encoded-data", "mimeType": "image/png"}]}
```

Response:
```json
{"type": "response", "command": "steer", "success": true}
```

#### `follow_up`

Queue follow-up message for delivery when agent stops. Skill templates expand; extension commands not allowed.

```json
{"type": "follow_up", "message": "After you're done, also do this"}
```

With images:
```json
{"type": "follow_up", "message": "Also check this image", "images": [{"type": "image", "data": "base64-encoded-data", "mimeType": "image/png"}]}
```

Response:
```json
{"type": "response", "command": "follow_up", "success": true}
```

#### `abort`

Abort current operation.

```json
{"type": "abort"}
```

Response:
```json
{"type": "response", "command": "abort", "success": true}
```

#### `new_session`

Start fresh session. Cancelled by `session_before_switch` extension handler.

```json
{"type": "new_session"}
```

With parent tracking:
```json
{"type": "new_session", "parentSession": "/path/to/parent-session.jsonl"}
```

Response:
```json
{"type": "response", "command": "new_session", "success": true, "data": {"cancelled": false}}
```

### State

#### `get_state`

```json
{"type": "get_state"}
```

Response:
```json
{
  "type": "response",
  "command": "get_state",
  "success": true,
  "data": {
    "model": {...},
    "thinkingLevel": "medium",
    "isStreaming": false,
    "isCompacting": false,
    "steeringMode": "all",
    "followUpMode": "one-at-a-time",
    "sessionFile": "/path/to/session.jsonl",
    "sessionId": "abc123",
    "sessionName": "my-feature-work",
    "autoCompactionEnabled": true,
    "messageCount": 5,
    "pendingMessageCount": 0
  }
}
```

#### `get_messages`

```json
{"type": "get_messages"}
```

Response:
```json
{
  "type": "response",
  "command": "get_messages",
  "success": true,
  "data": {"messages": [...]}
}
```

Messages are `AgentMessage` objects (see [Types](#types)).

### Model

#### `set_model`

```json
{"type": "set_model", "provider": "anthropic", "modelId": "claude-sonnet-4-20250514"}
```

Response:
```json
{
  "type": "response",
  "command": "set_model",
  "success": true,
  "data": {...}
}
```

#### `cycle_model`

Cycle to next available model. Returns `null` data if only one model.

```json
{"type": "cycle_model"}
```

Response:
```json
{
  "type": "response",
  "command": "cycle_model",
  "success": true,
  "data": {"model": {...}, "thinkingLevel": "medium", "isScoped": false}
}
```

#### `get_available_models`

```json
{"type": "get_available_models"}
```

Response:
```json
{
  "type": "response",
  "command": "get_available_models",
  "success": true,
  "data": {"models": [...]}
}
```

### Thinking

#### `set_thinking_level`

```json
{"type": "set_thinking_level", "level": "high"}
```

Levels: `"off"`, `"minimal"`, `"low"`, `"medium"`, `"high"`, `"xhigh"` (OpenAI codex-max only)

Response:
```json
{"type": "response", "command": "set_thinking_level", "success": true}
```

#### `cycle_thinking_level`

```json
{"type": "cycle_thinking_level"}
```

Response:
```json
{"type": "response", "command": "cycle_thinking_level", "success": true, "data": {"level": "high"}}
```

### Queue Modes

#### `set_steering_mode`

```json
{"type": "set_steering_mode", "mode": "one-at-a-time"}
```

| Mode | Behavior |
|------|----------|
| `"all"` | Deliver all steering messages after current turn |
| `"one-at-a-time"` | One steering message per completed turn (default) |

#### `set_follow_up_mode`

```json
{"type": "set_follow_up_mode", "mode": "one-at-a-time"}
```

| Mode | Behavior |
|------|----------|
| `"all"` | Deliver all follow-ups when agent finishes |
| `"one-at-a-time"` | One follow-up per agent completion (default) |

### Compaction

#### `compact`

```json
{"type": "compact"}
```

With custom instructions:
```json
{"type": "compact", "customInstructions": "Focus on code changes"}
```

Response:
```json
{
  "type": "response",
  "command": "compact",
  "success": true,
  "data": {
    "summary": "Summary of conversation...",
    "firstKeptEntryId": "abc123",
    "tokensBefore": 150000,
    "details": {}
  }
}
```

#### `set_auto_compaction`

```json
{"type": "set_auto_compaction", "enabled": true}
```

### Retry

#### `set_auto_retry`

Enable/disable auto-retry on transient errors (overloaded, rate limit, 5xx).

```json
{"type": "set_auto_retry", "enabled": true}
```

#### `abort_retry`

Cancel in-progress retry.

```json
{"type": "abort_retry"}
```

### Bash

#### `bash`

Execute shell command. Output added to conversation context on next `prompt`.

```json
{"type": "bash", "command": "ls -la"}
```

Response:
```json
{
  "type": "response",
  "command": "bash",
  "success": true,
  "data": {
    "output": "total 48\ndrwxr-xr-x ...",
    "exitCode": 0,
    "cancelled": false,
    "truncated": false
  }
}
```

If truncated:
```json
{"type": "response", "command": "bash", "success": true, "data": {"output": "...", "truncated": true, "fullOutputPath": "/tmp/pi-bash-abc123.log"}}
```

> [!info]
> Bash output reaches the LLM on the **next prompt**. A `BashExecutionMessage` is created and converted to a `UserMessage` before LLM submission:
> ````
> Ran `ls -la`
> ```
> total 48
> drwxr-xr-x ...
> ```
> ````

#### `abort_bash`

```json
{"type": "abort_bash"}
```

### Session

#### `get_session_stats`

```json
{"type": "get_session_stats"}
```

Response:
```json
{
  "type": "response",
  "command": "get_session_stats",
  "success": true,
  "data": {
    "sessionFile": "/path/to/session.jsonl",
    "sessionId": "abc123",
    "userMessages": 5,
    "assistantMessages": 5,
    "toolCalls": 12,
    "toolResults": 12,
    "totalMessages": 22,
    "tokens": {"input": 50000, "output": 10000, "cacheRead": 40000, "cacheWrite": 5000, "total": 105000},
    "cost": 0.45,
    "contextUsage": {"tokens": 60000, "contextWindow": 200000, "percent": 30}
  }
}
```

`contextUsage` omitted when no model/context window available. Fields null after compaction until fresh usage data.

#### `export_html`

```json
{"type": "export_html"}
```

With custom path:
```json
{"type": "export_html", "outputPath": "/tmp/session.html"}
```

#### `switch_session`

Load different session. Cancelled by `session_before_switch` handler.

```json
{"type": "switch_session", "sessionPath": "/path/to/session.jsonl"}
```

#### `fork`

Create fork from previous user message. Cancelled by `session_before_fork` handler.

```json
{"type": "fork", "entryId": "abc123"}
```

Response:
```json
{"type": "response", "command": "fork", "success": true, "data": {"text": "The original prompt text...", "cancelled": false}}
```

#### `clone`

Duplicate current branch into new session. Cancelled by `session_before_fork` handler.

```json
{"type": "clone"}
```

#### `get_fork_messages`

```json
{"type": "get_fork_messages"}
```

Response:
```json
{
  "type": "response",
  "command": "get_fork_messages",
  "success": true,
  "data": {
    "messages": [
      {"entryId": "abc123", "text": "First prompt..."},
      {"entryId": "def456", "text": "Second prompt..."}
    ]
  }
}
```

#### `get_last_assistant_text`

```json
{"type": "get_last_assistant_text"}
```

Response:
```json
{"type": "response", "command": "get_last_assistant_text", "success": true, "data": {"text": "The assistant's response..."}}
```

Returns `{"text": null}` if no assistant messages.

#### `set_session_name`

```json
{"type": "set_session_name", "name": "my-feature-work"}
```

Name appears in session listings.

### Commands

#### `get_commands`

List available commands (extension commands, prompt templates, skills). Invoke via `prompt` with `/` prefix.

```json
{"type": "get_commands"}
```

Response:
```json
{
  "type": "response",
  "command": "get_commands",
  "success": true,
  "data": {
    "commands": [
      {"name": "session-name", "description": "Set or clear session name", "source": "extension", "path": "/path/to/extension.ts"},
      {"name": "fix-tests", "description": "Fix failing tests", "source": "prompt", "location": "project", "path": "/path/to/fix-tests.md"},
      {"name": "skill:brave-search", "description": "Web search via Brave API", "source": "skill", "location": "user", "path": "/path/to/brave-search/SKILL.md"}
    ]
  }
}
```

| Field | Description |
|-------|-------------|
| `name` | Command name (invoke with `/name`) |
| `description` | Human-readable (optional for extensions) |
| `source` | `"extension"`, `"prompt"`, or `"skill"` |
| `location` | `"user"`, `"project"`, or `"path"` (not present for extensions) |
| `path` | Absolute file path |

> [!note]
> Built-in TUI commands (`/settings`, `/hotkeys`, etc.) not included — handled only in interactive mode.

## Events

Events streamed to stdout as JSON lines during operation. No `id` field.

### Event Types

| Event | Description |
|-------|-------------|
| `agent_start` | Agent begins processing |
| `agent_end` | Agent completes with all generated messages |
| `turn_start` / `turn_end` | One LLM response + tool calls |
| `message_start` / `message_end` | Message lifecycle |
| `message_update` | Streaming text/thinking/toolcall deltas |
| `tool_execution_start` / `tool_execution_update` / `tool_execution_end` | Tool lifecycle |
| `queue_update` | Pending queue changed |
| `compaction_start` / `compaction_end` | Compaction lifecycle |
| `auto_retry_start` / `auto_retry_end` | Retry lifecycle |
| `extension_error` | Extension threw error |

### Streaming Deltas (`message_update`)

```json
{
  "type": "message_update",
  "message": {...},
  "assistantMessageEvent": {
    "type": "text_delta",
    "contentIndex": 0,
    "delta": "Hello ",
    "partial": {...}
  }
}
```

| Delta Type | Description |
|------------|-------------|
| `start` | Message generation started |
| `text_start` / `text_delta` / `text_end` | Text content block |
| `thinking_start` / `thinking_delta` / `thinking_end` | Thinking block |
| `toolcall_start` / `toolcall_delta` / `toolcall_end` | Tool call |
| `done` | Complete (`reason`: `"stop"`, `"length"`, `"toolUse"`) |
| `error` | Error (`reason`: `"aborted"`, `"error"`) |

### Tool Execution

```json
{"type": "tool_execution_start", "toolCallId": "call_abc123", "toolName": "bash", "args": {"command": "ls -la"}}
```

Streaming progress:
```json
{
  "type": "tool_execution_update",
  "toolCallId": "call_abc123",
  "toolName": "bash",
  "partialResult": {"content": [{"type": "text", "text": "partial output..."}], "details": {}}
}
```

Complete:
```json
{
  "type": "tool_execution_end",
  "toolCallId": "call_abc123",
  "result": {"content": [{"type": "text", "text": "..."}], "details": {}},
  "isError": false
}
```

### Queue Update

```json
{"type": "queue_update", "steering": ["Focus on error handling"], "followUp": ["After that, summarize"]}
```

### Compaction

```json
{"type": "compaction_start", "reason": "threshold"}
```

`reason`: `"manual"`, `"threshold"`, or `"overflow"`

```json
{"type": "compaction_end", "reason": "threshold", "result": {...}, "aborted": false, "willRetry": false}
```

If `"overflow"` succeeds, `willRetry` is `true` and agent auto-retries. If aborted: `aborted: true`, `result: null`. If failed: `aborted: false`, `result: null`, `errorMessage` present.

### Auto Retry

```json
{"type": "auto_retry_start", "attempt": 1, "maxAttempts": 3, "delayMs": 2000, "errorMessage": "529 overloaded"}
```

```json
{"type": "auto_retry_end", "success": true, "attempt": 2}
```

Final failure:
```json
{"type": "auto_retry_end", "success": false, "attempt": 3, "finalError": "529 overloaded_error: Overloaded"}
```

## Extension UI Protocol

Extensions request user interaction via `ctx.ui.select()`, `ctx.ui.confirm()`, etc. Translated to request/response sub-protocol.

### Dialog Methods

Emit `extension_ui_request` on stdout, block until `extension_ui_response` on stdin with matching `id`.

| Method | Fields | Response |
|--------|--------|----------|
| `select` | `title`, `options[]`, `timeout?` | `value` (selected string) or `cancelled: true` |
| `confirm` | `title`, `message`, `timeout?` | `confirmed: true/false` or `cancelled: true` |
| `input` | `title`, `placeholder?` | `value` (text) or `cancelled: true` |
| `editor` | `title`, `prefill?` | `value` (text) or `cancelled: true` |

### Fire-and-Forget Methods

Emit `extension_ui_request` but don't expect response.

| Method | Fields |
|--------|--------|
| `notify` | `message`, `notifyType` (`"info"`, `"warning"`, `"error"`) |
| `setStatus` | `statusKey`, `statusText` (undefined to clear) |
| `setWidget` | `widgetKey`, `widgetLines[]`, `widgetPlacement` (`"aboveEditor"`, `"belowEditor"`) |
| `setTitle` | `title` |
| `set_editor_text` | `text` |

> [!warning]
> `ctx.hasUI` is `true` in RPC mode because dialog/fire-and-forget methods are functional via sub-protocol. These are degraded/no-op in RPC: `custom()`, `setWorkingMessage()`, `setWorkingIndicator()`, `setFooter()`, `setHeader()`, `setEditorComponent()`, `setToolsExpanded()`, `getEditorText()`, `getAllThemes()`, `getTheme()`, `setTheme()`.

## Error Handling

```json
{"type": "response", "command": "set_model", "success": false, "error": "Model not found: invalid/model"}
```

Parse errors:
```json
{"type": "response", "command": "parse", "success": false, "error": "Failed to parse command: Unexpected token..."}
```

## Types

Source files:
- [`packages/ai/src/types.ts`](../../ai/src/types.ts) — `Model`, `UserMessage`, `AssistantMessage`, `ToolResultMessage`
- [`packages/agent/src/types.ts`](../../agent/src/types.ts) — `AgentMessage`, `AgentEvent`
- [`src/core/messages.ts`](../src/core/messages.ts) — `BashExecutionMessage`
- [`src/modes/rpc/rpc-types.ts`](../src/modes/rpc/rpc-types.ts) — RPC types

### `Model`

```json
{
  "id": "claude-sonnet-4-20250514",
  "name": "Claude Sonnet 4",
  "api": "anthropic-messages",
  "provider": "anthropic",
  "baseUrl": "https://api.anthropic.com",
  "reasoning": true,
  "input": ["text", "image"],
  "contextWindow": 200000,
  "maxTokens": 16384,
  "cost": {"input": 3.0, "output": 15.0, "cacheRead": 0.3, "cacheWrite": 3.75}
}
```

### `UserMessage`

```json
{"role": "user", "content": "Hello!", "timestamp": 1733234567890, "attachments": []}
```

`content` can be string or `TextContent`/`ImageContent` blocks.

### `AssistantMessage`

```json
{
  "role": "assistant",
  "content": [
    {"type": "text", "text": "Hello!"},
    {"type": "thinking", "thinking": "User is greeting me..."},
    {"type": "toolCall", "id": "call_123", "name": "bash", "arguments": {"command": "ls"}}
  ],
  "api": "anthropic-messages",
  "provider": "anthropic",
  "model": "claude-sonnet-4-20250514",
  "usage": {"input": 100, "output": 50, "cacheRead": 0, "cacheWrite": 0, "cost": {...}},
  "stopReason": "stop",
  "timestamp": 1733234567890
}
```

Stop reasons: `"stop"`, `"length"`, `"toolUse"`, `"error"`, `"aborted"`

### `ToolResultMessage`

```json
{"role": "toolResult", "toolCallId": "call_123", "toolName": "bash", "content": [{"type": "text", "text": "..."}], "isError": false, "timestamp": 1733234567890}
```

### `BashExecutionMessage`

Created by `bash` RPC command (not LLM tool calls):

```json
{"role": "bashExecution", "command": "ls -la", "output": "...", "exitCode": 0, "cancelled": false, "truncated": false, "fullOutputPath": null, "timestamp": 1733234567890}
```

### `Attachment`

```json
{"id": "img1", "type": "image", "fileName": "photo.jpg", "mimeType": "image/jpeg", "size": 102400, "content": "base64...", "extractedText": null, "preview": null}
```

## Examples

### Python Client

```python
import subprocess
import json

proc = subprocess.Popen(
    ["pi", "--mode", "rpc", "--no-session"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)

def send(cmd):
    proc.stdin.write(json.dumps(cmd) + "\n")
    proc.stdin.flush()

def read_events():
    for line in proc.stdout:
        yield json.loads(line)

send({"type": "prompt", "message": "Hello!"})

for event in read_events():
    if event.get("type") == "message_update":
        delta = event.get("assistantMessageEvent", {})
        if delta.get("type") == "text_delta":
            print(delta["delta"], end="", flush=True)
    if event.get("type") == "agent_end":
        print()
        break
```

### Node.js Client

See [`test/rpc-example.ts`](../test/rpc-example.ts) and [`examples/rpc-extension-ui.ts`](../examples/rpc-extension-ui.ts) for full examples including extension UI handling.

```javascript
const { spawn } = require("child_process");
const { StringDecoder } = require("string_decoder");

const agent = spawn("pi", ["--mode", "rpc", "--no-session"]);

function attachJsonlReader(stream, onLine) {
    const decoder = new StringDecoder("utf8");
    let buffer = "";

    stream.on("data", (chunk) => {
        buffer += typeof chunk === "string" ? chunk : decoder.write(chunk);

        while (true) {
            const newlineIndex = buffer.indexOf("\n");
            if (newlineIndex === -1) break;

            let line = buffer.slice(0, newlineIndex);
            buffer = buffer.slice(newlineIndex + 1);
            if (line.endsWith("\r")) line = line.slice(0, -1);
            onLine(line);
        }
    });
}

attachJsonlReader(agent.stdout, (line) => {
    const event = JSON.parse(line);

    if (event.type === "message_update") {
        const { assistantMessageEvent } = event;
        if (assistantMessageEvent.type === "text_delta") {
            process.stdout.write(assistantMessageEvent.delta);
        }
    }
});

agent.stdin.write(JSON.stringify({ type: "prompt", "message": "Hello" }) + "\n");

process.on("SIGINT", () => {
    agent.stdin.write(JSON.stringify({ type: "abort" }) + "\n");
});
```

#rpc #json-protocol #headless-mode #cli-automation #ipc #agent-integration
