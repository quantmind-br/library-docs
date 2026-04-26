---
title: Json
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/json.md
source: git
fetched_at: 2026-04-26T05:48:14.108953489-03:00
rendered_js: false
word_count: 330
summary: JSON event stream mode outputs all session events as line-delimited JSON objects for integration into external tools.
tags:
    - pi-cli
    - json-output
    - event-stream
    - integration
    - cli-reference
    - data-processing
category: reference
optimized: true
optimized_at: 2026-04-26T09:00:00Z
---

# JSON Event Stream Mode

```bash
pi --mode json "Your prompt"
```

Outputs all session events as JSON lines to stdout for integration with external tools or custom UIs.

## Event Types

Events defined in [`AgentSessionEvent`](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/src/core/agent-session.ts#L102):

```typescript
type AgentSessionEvent =
  | AgentEvent
  | { type: "queue_update"; steering: readonly string[]; followUp: readonly string[] }
  | { type: "compaction_start"; reason: "manual" | "threshold" | "overflow" }
  | { type: "compaction_end"; reason: "manual" | "threshold" | "overflow"; result: CompactionResult | undefined; aborted: boolean; willRetry: boolean; errorMessage?: string }
  | { type: "auto_retry_start"; attempt: number; maxAttempts: number; delayMs: number; errorMessage: string }
  | { type: "auto_retry_end"; success: boolean; attempt: number; finalError?: string };
```

- **`queue_update`** — full pending steering and follow-up queues on change
- **`compaction_start` / `compaction_end`** — manual and automatic compaction

Base events from [`AgentEvent`](https://github.com/badlogic/pi-mono/blob/main/packages/agent/src/types.ts#L179):

```typescript
type AgentEvent =
  // Agent lifecycle
  | { type: "agent_start" }
  | { type: "agent_end"; messages: AgentMessage[] }
  // Turn lifecycle
  | { type: "turn_start" }
  | { type: "turn_end"; message: AgentMessage; toolResults: ToolResultMessage[] }
  // Message lifecycle
  | { type: "message_start"; message: AgentMessage }
  | { type: "message_update"; message: AgentMessage; assistantMessageEvent: AssistantMessageEvent }
  | { type: "message_end"; message: AgentMessage }
  // Tool execution
  | { type: "tool_execution_start"; toolCallId: string; toolName: string; args: any }
  | { type: "tool_execution_update"; toolCallId: string; toolName: string; args: any; partialResult: any }
  | { type: "tool_execution_end"; toolCallId: string; toolName: string; result: any; isError: boolean };
```

## Message Types

Base messages from [`packages/ai/src/types.ts`](https://github.com/badlogic/pi-mono/blob/main/packages/ai/src/types.ts#L134):

| Type | Line |
|------|------|
| `UserMessage` | 134 |
| `AssistantMessage` | 140 |
| `ToolResultMessage` | 152 |

Extended messages from [`packages/coding-agent/src/core/messages.ts`](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/src/core/messages.ts#L29):

| Type | Line |
|------|------|
| `BashExecutionMessage` | 29 |
| `CustomMessage` | 46 |
| `BranchSummaryMessage` | 55 |
| `CompactionSummaryMessage` | 62 |

## Output Format

Each line is a JSON object. First line is the session header:

```json
{"type":"session","version":3,"id":"uuid","timestamp":"...","cwd":"/path"}
```

Followed by events:

```json
{"type":"agent_start"}
{"type":"turn_start"}
{"type":"message_start","message":{"role":"assistant","content":[],...}}
{"type":"message_update","message":{...},"assistantMessageEvent":{"type":"text_delta","delta":"Hello",...}}
{"type":"message_end","message":{...}}
{"type":"turn_end","message":{...},"toolResults":[]}
{"type":"agent_end","messages":[...]}
```

## Example

```bash
pi --mode json "List files" 2>/dev/null | jq -c 'select(.type == "message_end")'
```

#json-output #event-stream #pi-cli
