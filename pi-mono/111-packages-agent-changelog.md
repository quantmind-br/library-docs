---
title: Changelog
url: https://github.com/badlogic/pi-mono/blob/main/packages/agent/CHANGELOG.md
source: git
fetched_at: 2026-05-03T09:30:55.526647364-03:00
rendered_js: false
word_count: 1527
summary: Versioned record of updates, breaking changes, new features, and bug fixes for the agent development API.
tags:
    - changelog
    - agent-framework
    - api-changes
    - breaking-changes
    - tool-execution
    - release-notes
category: reference
optimized: true
optimized_at: 2026-05-03T12:00:00Z
---
# Changelog

## [Unreleased]

## [0.72.1] - 2026-05-02

> [!changed]
> Default agent transport changed to `auto` — providers use their best available transport by default ([#4083](https://github.com/badlogic/pi-mono/issues/4083)).

## [0.72.0] - 2026-05-01

> [!added]
> Added `shouldStopAfterTurn` to low-level agent loop config for gracefully exiting after a completed turn before polling queued messages or starting another LLM call.

## [0.71.1] - 2026-05-01

## [0.71.0] - 2026-04-30

## [0.70.6] - 2026-04-28

## [0.70.5] - 2026-04-27

## [0.70.4] - 2026-04-27

## [0.70.3] - 2026-04-27

## [0.70.2] - 2026-04-24

## [0.70.1] - 2026-04-24

## [0.70.0] - 2026-04-23

## [0.69.0] - 2026-04-22

> [!breaking]
> Migrated public TypeBox-facing types and examples from `@sinclair/typebox` 0.34.x to `typebox` 1.x. Install and import from `typebox` instead of `@sinclair/typebox` ([#3112](https://github.com/badlogic/pi-mono/issues/3112))

> [!added]
> Added `terminate: true` tool-result hints to skip the automatic follow-up LLM call when every finalized tool result in the current batch opts into early termination ([#3525](https://github.com/badlogic/pi-mono/issues/3525))

## [0.68.1] - 2026-04-22

> [!fixed]
> - `streamProxy()` preserves the proxy-safe serializable subset of stream options (session, transport, retry-delay, metadata, header, cache-retention, thinking-budget) ([#3512](https://github.com/badlogic/pi-mono/issues/3512))
> - Parallel tool execution emits `tool_execution_end` as soon as each tool is finalized, while emitting persisted tool-result messages in assistant source order ([#3503](https://github.com/badlogic/pi-mono/issues/3503))

## [0.68.0] - 2026-04-20

> [!changed]
> Clarified parallel tool execution ordering: final tool lifecycle and tool-result artifacts are emitted in tool completion order.

## [0.67.68] - 2026-04-17

## [0.67.67] - 2026-04-17

> [!fixed]
> Parallel tool-call finalization converts `afterToolCall` hook throws into error tool results instead of aborting the batch ([#3084](https://github.com/badlogic/pi-mono/issues/3084))

## [0.67.6] - 2026-04-16

## [0.67.5] - 2026-04-16

## [0.67.4] - 2026-04-16

## [0.67.3] - 2026-04-15

## [0.67.2] - 2026-04-14

## [0.67.1] - 2026-04-13

## [0.67.0] - 2026-04-13

## [0.66.1] - 2026-04-08

## [0.66.0] - 2026-04-08

## [0.65.2] - 2026-04-06

## [0.65.1] - 2026-04-05

## [0.65.0] - 2026-04-03

> [!breaking]
> **`AgentState` reshaped:**
> - `streamMessage` → `streamingMessage`
> - `error` → `errorMessage`
> - `isStreaming`, `streamingMessage`, `pendingToolCalls`, `errorMessage` → readonly in public API
> - `pendingToolCalls` → `ReadonlySet<string>`
> - `tools` and `messages` → accessor properties (assigning copies top-level array)

> [!breaking]
> **`AgentOptions.initialState`** no longer accepts runtime-owned fields. Remove `isStreaming`, `streamingMessage`, `pendingToolCalls`, `errorMessage`.

> [!breaking]
> **Removed `Agent` mutator methods** — use direct property access:
> | Old method | New property |
> |---|---|
> | `agent.setSystemPrompt(value)` | `agent.state.systemPrompt = value` |
> | `agent.setModel(model)` | `agent.state.model = model` |
> | `agent.setThinkingLevel(level)` | `agent.state.thinkingLevel = level` |
> | `agent.setTools(tools)` | `agent.state.tools = tools` |
> | `agent.replaceMessages(messages)` | `agent.state.messages = messages` |
> | `agent.appendMessage(message)` | `agent.state.messages.push(message)` |
> | `agent.clearMessages()` | `agent.state.messages = []` |
> | `agent.setToolExecution(mode)` | `agent.toolExecution = mode` |
> | `agent.setBeforeToolCall(fn)` | `agent.beforeToolCall = fn` |
> | `agent.setAfterToolCall(fn)` | `agent.afterToolCall = fn` |
> | `agent.setTransport(transport)` | `agent.transport = transport` |

> [!breaking]
> **Removed queue mode getter/setter methods:**
> | Old | New |
> |---|---|
> | `agent.setSteeringMode(mode)` | `agent.steeringMode = mode` |
> | `agent.getSteeringMode()` | `agent.steeringMode` |
> | `agent.setFollowUpMode(mode)` | `agent.followUpMode = mode` |
> | `agent.getFollowUpMode()` | `agent.followUpMode` |

> [!breaking]
> **`Agent.subscribe()`** — listeners are now awaited and receive the `AbortSignal`:
> - `agent.subscribe(async (event, signal) => { ... })`
> - `agent_end` is the final emitted event
> - `agent.waitForIdle()`, `agent.prompt(...)`, `agent.continue()` settle only after awaited `agent_end` listeners finish
> - `agent.state.isStreaming` remains `true` until settlement completes

## [0.64.0] - 2026-03-29

> [!added]
> Added `AgentTool.prepareArguments` hook to prepare raw tool call arguments before schema validation, enabling compatibility shims for resumed sessions with outdated tool schemas.

## [0.63.2] - 2026-03-29

> [!added]
> Added `Agent.signal` to expose the active abort signal for the current turn ([#2660](https://github.com/badlogic/pi-mono/issues/2660))

## [0.63.1] - 2026-03-27

## [0.63.0] - 2026-03-27

## [0.62.0] - 2026-03-23

## [0.61.1] - 2026-03-20

## [0.61.0] - 2026-03-20

## [0.60.0] - 2026-03-18

## [0.59.0] - 2026-03-17

## [0.58.4] - 2026-03-16

> [!fixed]
> Steering messages wait until the current assistant message's tool-call batch fully finishes instead of skipping pending tool calls.

## [0.58.3] - 2026-03-15

## [0.58.2] - 2026-03-15

## [0.58.1] - 2026-03-14

## [0.58.0] - 2026-03-14

> [!added]
> Added `beforeToolCall` and `afterToolCall` hooks to `AgentOptions` and `AgentLoopConfig` for preflight blocking and post-execution tool result mutation.

> [!added]
> Configurable tool execution mode via `toolExecution: "parallel" | "sequential"`, defaulting to `parallel`. Parallel mode preflights tool calls sequentially, executes allowed tools concurrently, and emits final tool results in assistant source order.

## [0.57.1] - 2026-03-07

## [0.57.0] - 2026-03-07

## [0.56.3] - 2026-03-06

## [0.56.2] - 2026-03-05

## [0.56.1] - 2026-03-05

## [0.56.0] - 2026-03-04

## [0.55.4] - 2026-03-02

## [0.55.3] - 2026-02-27

## [0.55.2] - 2026-02-27

## [0.55.1] - 2026-02-26

## [0.55.0] - 2026-02-24

## [0.54.2] - 2026-02-23

## [0.54.1] - 2026-02-22

## [0.54.0] - 2026-02-19

## [0.53.1] - 2026-02-19

## [0.53.0] - 2026-02-17

## [0.52.12] - 2026-02-13

> [!added]
> Added `transport` to `AgentOptions` and `AgentLoopConfig` forwarding, allowing stream transport preference (`"sse"`, `"websocket"`, `"auto"`) to flow into provider calls.

## [0.52.11] - 2026-02-13

## [0.52.10] - 2026-02-12

## [0.52.9] - 2026-02-08

## [0.52.8] - 2026-02-07

## [0.52.7] - 2026-02-06

> [!fixed]
> `continue()` resumes queued steering/follow-up messages when context currently ends in an assistant message, and preserves one-at-a-time steering ordering during assistant-tail resumes ([#1312](https://github.com/badlogic/pi-mono/pull/1312) by [@ferologics](https://github.com/ferologics))

## [0.52.6] - 2026-02-05

## [0.52.5] - 2026-02-05

## [0.52.4] - 2026-02-05

## [0.52.3] - 2026-02-05

## [0.52.2] - 2026-02-05

## [0.52.1] - 2026-02-05

## [0.52.0] - 2026-02-05

## [0.51.6] - 2026-02-04

## [0.51.5] - 2026-02-04

## [0.51.4] - 2026-02-03

## [0.51.3] - 2026-02-03

## [0.51.2] - 2026-02-03

## [0.51.1] - 2026-02-02

## [0.51.0] - 2026-02-01

## [0.50.9] - 2026-02-01

## [0.50.8] - 2026-02-01

> [!added]
> Added `maxRetryDelayMs` option to `AgentOptions` to cap server-requested retry delays. Passed through to the underlying stream function ([#1123](https://github.com/badlogic/pi-mono/issues/1123))

## [0.50.7] - 2026-01-31

## [0.50.6] - 2026-01-30

## [0.50.5] - 2026-01-30

## [0.50.3] - 2026-01-29

## [0.50.2] - 2026-01-29

## [0.50.1] - 2026-01-26

## [0.50.0] - 2026-01-26

## [0.49.3] - 2026-01-22

## [0.49.2] - 2026-01-19

## [0.49.1] - 2026-01-18

## [0.49.0] - 2026-01-17

## [0.48.0] - 2026-01-16

## [0.47.0] - 2026-01-16

## [0.46.0] - 2026-01-15

## [0.45.7] - 2026-01-13

## [0.45.6] - 2026-01-13

## [0.45.5] - 2026-01-13

## [0.45.4] - 2026-01-13

## [0.45.3] - 2026-01-13

## [0.45.2] - 2026-01-13

## [0.45.1] - 2026-01-13

## [0.45.0] - 2026-01-13

## [0.44.0] - 2026-01-12

## [0.43.0] - 2026-01-11

## [0.42.5] - 2026-01-11

## [0.42.4] - 2026-01-10

## [0.42.3] - 2026-01-10

## [0.42.2] - 2026-01-10

## [0.42.1] - 2026-01-09

## [0.42.0] - 2026-01-09

## [0.41.0] - 2026-01-09

## [0.40.1] - 2026-01-09

## [0.40.0] - 2026-01-08

## [0.39.1] - 2026-01-08

## [0.39.0] - 2026-01-08

## [0.38.0] - 2026-01-08

> [!added]
> `thinkingBudgets` option on `Agent` and `AgentOptions` to customize token budgets per thinking level ([#529](https://github.com/badlogic/pi-mono/pull/529) by [@melihmucuk](https://github.com/melihmucuk))

## [0.37.8] - 2026-01-07

## [0.37.7] - 2026-01-07

## [0.37.6] - 2026-01-06

## [0.37.5] - 2026-01-06

## [0.37.4] - 2026-01-06

## [0.37.3] - 2026-01-06

> [!added]
> `sessionId` option on `Agent` to forward session identifiers to LLM providers for session-based caching.

## [0.37.2] - 2026-01-05

## [0.37.1] - 2026-01-05

## [0.37.0] - 2026-01-05

> [!fixed]
> `minimal` thinking level now maps to `minimal` reasoning effort instead of being treated as `low`.

## [0.36.0] - 2026-01-05

## [0.35.0] - 2026-01-05

## [0.34.2] - 2026-01-04

## [0.34.1] - 2026-01-04

## [0.34.0] - 2026-01-04

## [0.33.0] - 2026-01-04

## [0.32.3] - 2026-01-03

## [0.32.2] - 2026-01-03

## [0.32.1] - 2026-01-03

## [0.32.0] - 2026-01-03

> [!breaking]
> **Queue API replaced with steer/followUp** ([#403](https://github.com/badlogic/pi-mono/issues/403)):
> - `steer(msg)` — interrupts agent mid-run. Delivered after current tool execution, skips remaining tools.
> - `followUp(msg)` — waits until agent finishes. Delivered only when no more tool calls or steering messages.

> [!breaking]
> **`queueMode` renamed to `steeringMode`**. Added `followUpMode`. Both control whether messages are delivered one-at-a-time or all at once.

> [!breaking]
> **`AgentLoopConfig` callbacks renamed:** `getQueuedMessages` → `getSteeringMessages` + `getFollowUpMessages`.

> [!breaking]
> **Agent methods renamed:**
> | Old | New |
> |---|---|
> | `queueMessage()` | `steer()` + `followUp()` |
> | `clearMessageQueue()` | `clearSteeringQueue()` + `clearFollowUpQueue()` + `clearAllQueues()` |
> | `setQueueMode()`/`getQueueMode()` | `setSteeringMode()`/`getSteeringMode()` + `setFollowUpMode()`/`getFollowUpMode()` |

> [!fixed]
> `prompt()` and `continue()` throw if called while agent is already streaming.

## [0.31.1] - 2026-01-02

## [0.31.0] - 2026-01-02

> [!breaking]
> **Transport abstraction removed**: `ProviderTransport`, `AppTransport`, `AgentTransport` interface removed. Use `streamFn` option directly.

> [!breaking]
> **Agent options renamed:**
> - `transport` → removed (use `streamFn`)
> - `messageTransformer` → `convertToLlm`
> - `preprocessor` → `transformContext`

> [!breaking]
> **`AppMessage` → `AgentMessage`**: All references renamed for consistency.

> [!breaking]
> **`CustomMessages` → `CustomAgentMessages`**: Declaration merging interface renamed.

> [!breaking]
> **`UserMessageWithAttachments` and `Attachment` types removed**: Attachment handling is now the `convertToLlm` function's responsibility.

> [!breaking]
> **Agent loop moved from `@mariozechner/pi-ai`** to this package. Import from `@mariozechner/pi-agent-core`.

> [!added]
> - `streamFn` option for custom stream implementations
> - `streamProxy()` utility for browser apps proxying LLM calls through backend
> - `getApiKey` option for dynamic API key resolution (OAuth tokens)
> - `agentLoop()` and `agentLoopContinue()` low-level functions
> - New exported types: `AgentLoopConfig`, `AgentContext`, `AgentTool`, `AgentToolResult`, `AgentToolUpdateCallback`, `StreamFn`

> [!changed]
> - `Agent` constructor options now all optional (empty = defaults)
> - `queueMessage()` is now synchronous (no Promise return)

#changelog #agent-framework #api-changes #breaking-changes
