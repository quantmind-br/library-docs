---
title: pi-agent-core
tags:
  - agent-framework
  - llm
  - event-streaming
  - tool-execution
  - typescript
category: guide
optimized: true
optimized_at: 2026-05-03T12:31:00Z
related:
  - "[[002-packages-ai-readme|pi-ai]]"
  - "[[009-packages-coding-agent-readme|coding-agent]]"
word_count: 428
optimized: true
optimized_at: 2026-05-03T12:00:00Z
---
# @mariozechner/pi-agent-core

Stateful agent with tool execution and event streaming. Built on [[002-packages-ai-readme|@mariozechner/pi-ai]].

```bash
npm install @mariozechner/pi-agent-core
```

## Quick Start

```typescript
import { Agent } from "@mariozechner/pi-agent-core";
import { getModel } from "@mariozechner/pi-ai";

const agent = new Agent({
  initialState: {
    systemPrompt: "You are a helpful assistant.",
    model: getModel("anthropic", "claude-sonnet-4-20250514"),
  },
});

agent.subscribe((event) => {
  if (event.type === "message_update" && event.assistantMessageEvent.type === "text_delta") {
    process.stdout.write(event.assistantMessageEvent.delta);
  }
});

await agent.prompt("Hello!");
```

## Core Concepts

### AgentMessage vs LLM Message

`AgentMessage` is flexible — supports standard LLM messages (`user`, `assistant`, `toolResult`) plus custom app-specific types via declaration merging.

LLMs only understand `user`, `assistant`, `toolResult`. `convertToLlm` bridges the gap by filtering/transforming messages before each LLM call.

### Message Flow

```
AgentMessage[] → transformContext() → AgentMessage[] → convertToLlm() → Message[] → LLM
                    (optional)                           (required)
```

1. **transformContext**: Prune old messages, inject external context
2. **convertToLlm**: Filter UI-only messages, convert custom types

## Event Flow

### prompt() Event Sequence

```
prompt("Hello")
├─ agent_start
├─ turn_start
├─ message_start   { message: userMessage }      // Your prompt
├─ message_end     { message: userMessage }
├─ message_start   { message: assistantMessage } // LLM starts
├─ message_update  { message: partial... }       // Streaming
├─ message_end     { message: assistantMessage }
├─ turn_end        { message, toolResults: [] }
└─ agent_end       { messages: [...] }
```

### With Tool Calls

```
prompt("Read config.json")
├─ agent_start
├─ turn_start
├─ message_start/end  { userMessage }
├─ message_start      { assistantMessage with toolCall }
├─ message_update...
├─ message_end        { assistantMessage }
├─ tool_execution_start  { toolCallId, toolName, args }
├─ tool_execution_update { partialResult }           // If tool streams
├─ tool_execution_end    { toolCallId, result }
├─ message_start/end  { toolResultMessage }
├─ turn_end           { message, toolResults: [toolResult] }
│
├─ turn_start                                        // Next turn
├─ message_start      { assistantMessage }
├─ message_update...
├─ message_end
├─ turn_end
└─ agent_end
```

### Tool Execution Modes

- **parallel** (default): Preflight sequentially, execute concurrently, emit events as each tool finalizes
- **sequential**: Execute one-by-one

Mode can be global (`toolExecution` in config) or per-tool (`executionMode` on `AgentTool`).

### Hooks

- **beforeToolCall**: Runs after validation, can block execution
- **afterToolCall**: Runs after execution, before final events

### Early Termination

Tools can return `terminate: true` to skip follow-up LLM call. Loop stops when every tool in batch sets `terminate: true`.

### Low-Level Loop Control

```typescript
const stream = agentLoop(prompts, context, {
  model,
  convertToLlm,
  shouldStopAfterTurn: async ({ message, toolResults, context, newMessages }) => {
    return shouldCompactBeforeNextTurn(context.messages);
  },
});
```

## continue()

Resumes from existing context without adding a message. Last message must be `user` or `toolResult`.

```typescript
await agent.continue();
```

## Event Types

| Event | Description |
|-------|-------------|
| `agent_start` | Agent begins processing |
| `agent_end` | Final event. Awaited subscribers count toward settlement |
| `turn_start` | New turn begins |
| `turn_end` | Turn completes with assistant message and tool results |
| `message_start` | Any message begins |
| `message_update` | Assistant only. Contains `assistantMessageEvent` with delta |
| `message_end` | Message completes |
| `tool_execution_start` | Tool begins |
| `tool_execution_update` | Tool streams progress |
| `tool_execution_end` | Tool completes |

`agent_end` means no more events will emit, but `await agent.waitForIdle()` and `await agent.prompt(...)` only settle after awaited `agent_end` listeners finish.

## Agent Options

```typescript
const agent = new Agent({
  // Initial state
  initialState: {
    systemPrompt: string,
    model: Model<any>,
    thinkingLevel: "off" | "minimal" | "low" | "medium" | "high" | "xhigh",
    tools: AgentTool<any>[],
    messages: AgentMessage[],
  },

  // Convert AgentMessage[] to LLM Message[] (required for custom types)
  convertToLlm: (messages) => messages.filter(...),

  // Transform context before convertToLlm
  transformContext: async (messages, signal) => pruneOldMessages(messages),

  // Steering/follow-up modes: "one-at-a-time" (default) or "all"
  steeringMode: "one-at-a-time",
  followUpMode: "one-at-a-time",

  // Custom stream function (for proxy backends)
  streamFn: streamProxy,

  // Session ID for provider caching
  sessionId: "session-123",

  // Dynamic API key resolution
  getApiKey: async (provider) => refreshToken(),

  // Tool execution mode: "parallel" (default) or "sequential"
  toolExecution: "parallel",

  // Hooks
  beforeToolCall: async ({ toolCall, args, context }) => {
    if (toolCall.name === "bash") {
      return { block: true, reason: "bash is disabled" };
    }
  },

  afterToolCall: async ({ toolCall, result, isError, context }) => {
    if (toolCall.name === "notify_done" && !isError) {
      return { terminate: true };
    }
    if (!isError) {
      return { details: { ...result.details, audited: true } };
    }
  },

  // Thinking budgets
  thinkingBudgets: {
    minimal: 128,
    low: 512,
    medium: 1024,
    high: 2048,
  },
});
```

## Agent State

```typescript
interface AgentState {
  systemPrompt: string;
  model: Model<any>;
  thinkingLevel: ThinkingLevel;
  tools: AgentTool<any>[];
  messages: AgentMessage[];
  readonly isStreaming: boolean;
  readonly streamingMessage?: AgentMessage;
  readonly pendingToolCalls: ReadonlySet<string>;
  readonly errorMessage?: string;
}
```

Access via `agent.state`. Assigning `agent.state.tools = [...]` or `agent.state.messages = [...]` copies the top-level array.

During streaming, `agent.state.streamingMessage` contains the current partial assistant message. `agent.state.isStreaming` remains `true` until run fully settles.

## Methods

### Prompting

```typescript
// Text prompt
await agent.prompt("Hello");

// With images
await agent.prompt("What's in this image?", [
  { type: "image", data: base64Data, mimeType: "image/jpeg" }
]);

// AgentMessage directly
await agent.prompt({ role: "user", content: "Hello", timestamp: Date.now() });

// Continue from current context
await agent.continue();
```

### State Management

```typescript
agent.state.systemPrompt = "New prompt";
agent.state.model = getModel("openai", "gpt-4o");
agent.state.thinkingLevel = "medium";
agent.state.tools = [myTool];
agent.toolExecution = "sequential";
agent.beforeToolCall = async ({ toolCall }) => undefined;
agent.afterToolCall = async ({ toolCall, result }) => undefined;
agent.state.messages = newMessages;
agent.reset();
```

### Session and Thinking

```typescript
agent.sessionId = "session-123";

agent.thinkingBudgets = {
  minimal: 128,
  low: 512,
  medium: 1024,
  high: 2048,
};
```

### Control

```typescript
agent.abort();           // Cancel current operation
await agent.waitForIdle(); // Wait for completion
```

### Events

```typescript
const unsubscribe = agent.subscribe(async (event, signal) => {
  if (event.type === "agent_end") {
    await flushSessionState(signal);
  }
});
unsubscribe();
```

## Steering and Follow-up

Steering interrupts while tools run. Follow-up queues work after agent stops.

```typescript
agent.steeringMode = "one-at-a-time";
agent.followUpMode = "one-at-a-time";

// While running
agent.steer({
  role: "user",
  content: "Stop! Do this instead.",
  timestamp: Date.now(),
});

agent.followUp({
  role: "user",
  content: "Also summarize the result.",
  timestamp: Date.now(),
});

agent.clearSteeringQueue();
agent.clearFollowUpQueue();
agent.clearAllQueues();
```

## Custom Message Types

Extend via declaration merging:

```typescript
declare module "@mariozechner/pi-agent-core" {
  interface CustomAgentMessages {
    notification: { role: "notification"; text: string; timestamp: number };
  }
}
```

Handle in `convertToLlm`:

```typescript
convertToLlm: (messages) => messages.flatMap(m => {
  if (m.role === "notification") return [];
  return [m];
}),
```

## Tools

```typescript
import { Type } from "typebox";

const readFileTool: AgentTool = {
  name: "read_file",
  label: "Read File",
  description: "Read a file's contents",
  parameters: Type.Object({
    path: Type.String({ description: "File path" }),
  }),
  executionMode: "sequential",  // optional
  execute: async (toolCallId, params, signal, onUpdate) => {
    const content = await fs.readFile(params.path, "utf-8");
    onUpdate?.({ content: [{ type: "text", text: "Reading..." }], details: {} });
    return {
      content: [{ type: "text", text: content }],
      details: { path: params.path, size: content.length },
    };
  },
};

agent.state.tools = [readFileTool];
```

### Error Handling

**Throw** errors on failure. Do not return error messages as content.

```typescript
execute: async (toolCallId, params, signal, onUpdate) => {
  if (!fs.existsSync(params.path)) {
    throw new Error(`File not found: ${params.path}`);
  }
  return { content: [{ type: "text", text: "..." }] };
}
```

## Proxy Usage

```typescript
import { Agent, streamProxy } from "@mariozechner/pi-agent-core";

const agent = new Agent({
  streamFn: (model, context, options) =>
    streamProxy(model, context, {
      ...options,
      authToken: "...",
      proxyUrl: "https://your-server.com",
    }),
});
```

## Low-Level API

```typescript
import { agentLoop, agentLoopContinue } from "@mariozechner/pi-agent-core";

const context: AgentContext = {
  systemPrompt: "You are helpful.",
  messages: [],
  tools: [],
};

const config: AgentLoopConfig = {
  model: getModel("openai", "gpt-4o"),
  convertToLlm: (msgs) => msgs.filter(m => ["user", "assistant", "toolResult"].includes(m.role)),
  toolExecution: "parallel",
  beforeToolCall: async ({ toolCall, args, context }) => undefined,
  afterToolCall: async ({ toolCall, result, isError, context }) => undefined,
};

const userMessage = { role: "user", content: "Hello", timestamp: Date.now() };

for await (const event of agentLoop([userMessage], context, config)) {
  console.log(event.type);
}

for await (const event of agentLoopContinue(context, config)) {
  console.log(event.type);
}
```

Low-level streams are observational — they do not wait for async event handling to settle before later phases continue. Use the `Agent` class if you need message processing to act as a barrier.

---

**License:** MIT
