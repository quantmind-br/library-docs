---
title: Codex App Server
url: https://developers.openai.com/codex/app-server.md
source: llms
fetched_at: 2026-04-30T10:15:12.117222834-03:00
rendered_js: false
word_count: 2889
summary: This document provides a technical specification and implementation guide for the Codex app-server, which facilitates bidirectional communication for integrating Codex capabilities into external products.
tags:
    - json-rpc
    - api-integration
    - codex-server
    - websocket
    - protocol-specification
    - client-side-development
category: reference
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Codex App Server

Interface Codex uses to power rich clients (e.g., VS Code extension). Use for deep integration: authentication, conversation history, approvals, streamed agent events. Open source: [openai/codex/codex-rs/app-server](https://github.com/openai/codex/tree/main/codex-rs/app-server). See [[033-open-source|Open Source]] for full component list.

If automating jobs or running in CI, use [[071-sdk|Codex SDK]] instead.

## Protocol

Bidirectional JSON-RPC 2.0 (with `"jsonrpc":"2.0"` header omitted on wire).

Supported transports:
- `stdio` (`--listen stdio://`, default): newline-delimited JSON (JSONL)
- `websocket` (`--listen ws://IP:PORT`, experimental): one JSON-RPC message per WebSocket text frame
- `off` (`--listen off`): no local transport

WebSocket transport serves basic HTTP health probes:
- `GET /readyz` — `200 OK` once listener accepts new connections
- `GET /healthz` — `200 OK` when no `Origin` header; `403 Forbidden` otherwise

WebSocket is experimental and unsupported. Loopback listeners (`ws://127.0.0.1:PORT`) appropriate for localhost and SSH port-forwarding. Non-loopback listeners currently allow unauthenticated connections by default during rollout — configure WebSocket auth before exposing remotely.

WebSocket auth flags:
- `--ws-auth capability-token --ws-token-file /absolute/path`
- `--ws-auth capability-token --ws-token-sha256 HEX`
- `--ws-auth signed-bearer-token --ws-shared-secret-file /absolute/path`

For signed bearer tokens, also set `--ws-issuer`, `--ws-audience`, `--ws-max-clock-skew-seconds`. Clients present credential as `Authorization: Bearer <token>` during handshake; app-server enforces auth before JSON-RPC `initialize`.

Prefer `--ws-token-file` over passing raw tokens on command line. Use `--ws-token-sha256` only when client keeps raw high-entropy token in separate local secret store; hash is verifier only — clients still need original token.

In WebSocket mode, app-server uses bounded queues. When request ingress is full, rejects new requests with JSON-RPC error code `-32001` and message `"Server overloaded; retry later."` Clients should retry with exponentially increasing delay and jitter.

## Message schema

Requests: `method`, `params`, `id`
```json
{ "method": "thread/start", "id": 10, "params": { "model": "gpt-5.4" } }
```

Responses: echo `id` with `result` or `error`
```json
{ "id": 10, "result": { "thread": { "id": "thr_123" } } }
{ "id": 10, "error": { "code": 123, "message": "Something went wrong" } }
```

Notifications: omit `id`, use `method` + `params`
```json
{ "method": "turn/started", "params": { "turn": { "id": "turn_456" } } }
```

Generate schemas from CLI (version-specific):
```bash
codex app-server generate-ts --out ./schemas
codex app-server generate-json-schema --out ./schemas
```

## Getting started

1. Start server: `codex app-server` (default stdio) or `codex app-server --listen ws://127.0.0.1:4500` (experimental WebSocket)
2. Connect client over selected transport
3. Send `initialize`, then `initialized` notification
4. Start thread and turn, then read notifications from active transport stream

Example (Node.js / TypeScript):
```ts
const proc = spawn("codex", ["app-server"], {
  stdio: ["pipe", "pipe", "inherit"],
});
const rl = readline.createInterface({ input: proc.stdout });

const send = (message: unknown) => {
  proc.stdin.write(`${JSON.stringify(message)}\n`);
};

let threadId: string | null = null;

rl.on("line", (line) => {
  const msg = JSON.parse(line) as any;
  console.log("server:", msg);

  if (msg.id === 1 && msg.result?.thread?.id && !threadId) {
    threadId = msg.result.thread.id;
    send({
      method: "turn/start",
      id: 2,
      params: {
        threadId,
        input: [{ type: "text", text: "Summarize this repo." }],
      },
    });
  }
});

send({
  method: "initialize",
  id: 0,
  params: {
    clientInfo: {
      name: "my_product",
      title: "My Product",
      version: "0.1.0",
    },
  },
});
send({ method: "initialized", params: {} });
send({ method: "thread/start", id: 1, params: { model: "gpt-5.4" } });
```

## Core primitives

- **Thread** — conversation between user and Codex agent; contains turns
- **Turn** — single user request + agent work that follows; contains items and streams incremental updates
- **Item** — unit of input or output (user message, agent message, command runs, file change, tool call, etc.)

Use thread APIs to create, list, archive conversations. Drive with turn APIs; stream progress via turn notifications.

## Lifecycle overview

1. **Initialize once per connection** — send `initialize` request with client metadata, then emit `initialized`. Server rejects any request before handshake.
2. **Start or resume thread** — `thread/start` for new conversation, `thread/resume` to continue existing, `thread/fork` to branch history into new thread id
3. **Begin turn** — `turn/start` with target `threadId` and user input. Optional fields override model, personality, `cwd`, sandbox policy, etc.
4. **Steer active turn** — `turn/steer` to append user input to in-flight turn without creating new turn
5. **Stream events** — read notifications on stdout: `thread/archived`, `thread/unarchived`, `item/started`, `item/completed`, `item/agentMessage/delta`, tool progress, etc.
6. **Finish turn** — server emits `turn/completed` with final status when model finishes or after `turn/interrupt` cancellation

## Initialization

Single `initialize` request per transport connection required before any other method. Repeated `initialize` calls return `Already initialized`.

Server returns user agent string, `platformFamily`, `platformOs`. Set `clientInfo` to identify your integration.

`initialize.params.capabilities` supports per-connection notification opt-out via `optOutNotificationMethods` — exact method names (no wildcards/prefixes). Unknown names accepted and ignored.

**Important**: Use `clientInfo.name` to identify your client for OpenAI Compliance Logs Platform. If developing a new Codex integration for enterprise use, contact OpenAI to get added to known clients list. See [Codex logs reference](https://chatgpt.com/admin/api-reference#tag/Logs:-Codex).

Example:
```json
{
  "method": "initialize",
  "id": 0,
  "params": {
    "clientInfo": {
      "name": "codex_vscode",
      "title": "Codex VS Code Extension",
      "version": "0.1.0"
    }
  }
}
```

Example with notification opt-out:
```json
{
  "method": "initialize",
  "id": 1,
  "params": {
    "clientInfo": { "name": "my_client", "title": "My Client", "version": "0.1.0" },
    "capabilities": {
      "experimentalApi": true,
      "optOutNotificationMethods": ["thread/started", "item/agentMessage/delta"]
    }
  }
}
```

## Experimental API opt-in

Some methods and fields gated behind `experimentalApi` capability.
- Omit `capabilities` or set `experimentalApi: false` → stable API surface; experimental methods/fields rejected
- Set `capabilities.experimentalApi: true` → enables experimental methods and fields

If experimental method/field sent without opting in, app-server rejects with:
`"<descriptor> requires experimentalApi capability"`

## API overview

| Method | Description |
|--------|-------------|
| `thread/start` | Create new thread; emits `thread/started`, auto-subscribes to turn/item events |
| `thread/resume` | Reopen existing thread by id |
| `thread/fork` | Fork thread into new id by copying history; emits `thread/started` |
| `thread/read` | Read stored thread without resuming; `includeTurns` for full history |
| `thread/list` | Page through stored thread logs; cursor pagination + filters |
| `thread/turns/list` | Page through stored thread's turn history without resuming |
| `thread/loaded/list` | Thread ids currently loaded in memory |
| `thread/name/set` | Set/update user-facing name; emits `thread/name/updated` |
| `thread/metadata/update` | Patch stored thread metadata (supports `gitInfo`) |
| `thread/archive` | Move thread log to archived directory; emits `thread/archived` |
| `thread/unsubscribe` | Unsubscribe connection from thread turn/item events |
| `thread/unarchive` | Restore archived thread; emits `thread/unarchived` |
| `thread/status/changed` | Notification: loaded thread's runtime `status` changed |
| `thread/compact/start` | Trigger history compaction; returns `{}` immediately, progress streams via notifications |
| `thread/shellCommand` | Run user-initiated shell command against thread (outside sandbox, full access) |
| `thread/backgroundTerminals/clean` | Stop all background terminals for thread (experimental; requires `experimentalApi`) |
| `thread/rollback` | Drop last N turns from in-memory context; persist rollback marker |
| `turn/start` | Add user input and begin Codex generation; streams events |
| `thread/inject_items` | Append raw Responses API items to loaded thread's history without starting user turn |
| `turn/steer` | Append user input to active in-flight turn |
| `turn/interrupt` | Request cancellation of in-flight turn |
| `review/start` | Kick off Codex reviewer; emits `enteredReviewMode` and `exitedReviewMode` |
| `command/exec` | Run single command under server sandbox without thread/turn |
| `command/exec/write` | Write `stdin` bytes to running `command/exec` session or close `stdin` |
| `command/exec/resize` | Resize running PTY-backed `command/exec` session |
| `command/exec/terminate` | Stop running `command/exec` session |
| `command/exec/outputDelta` (notify) | Base64-encoded stdout/stderr chunks from streaming session |
| `model/list` | List available models; `includeHidden: true` for hidden entries |
| `experimentalFeature/list` | List feature flags with lifecycle stage metadata |
| `experimentalFeature/enablement/set` | Patch in-memory runtime enablement for supported feature keys |
| `collaborationMode/list` | List collaboration mode presets (experimental) |
| `skills/list` | List skills for one or more `cwd` values |
| `skills/changed` (notify) | Emitted when watched local skill files change |
| `marketplace/add` | Add remote plugin marketplace |
| `plugin/list` | List discovered marketplaces and plugin state |
| `plugin/read` | Read one plugin by marketplace path or name |
| `plugin/install` | Install plugin from marketplace |
| `plugin/uninstall` | Uninstall installed plugin |
| `app/list` | List available apps (connectors) with pagination |
| `skills/config/write` | Enable or disable skills by path |
| `mcpServer/oauth/login` | Start OAuth login for configured MCP server |
| `tool/requestUserInput` | Prompt user with 1-3 short questions for tool call (experimental) |
| `config/mcpServer/reload` | Reload MCP server configuration from disk |
| `mcpServerStatus/list` | List MCP servers, tools, resources, auth status |
| `mcpServer/resource/read` | Read single MCP resource |
| `mcpServer/tool/call` | Call tool on thread's configured MCP server |
| `mcpServer/startupStatus/updated` (notify) | MCP server startup status changed for loaded thread |
| `windowsSandbox/setupStart` | Start Windows sandbox setup; emits `windowsSandbox/setupCompleted` |
| `feedback/upload` | Submit feedback report |
| `config/read` | Fetch effective configuration after resolving layering |
| `externalAgentConfig/detect` | Detect external-agent artifacts for migration |
| `externalAgentConfig/import` | Apply selected migration items |
| `config/value/write` | Write single config key/value to user's `config.toml` |
| `config/batchWrite` | Apply config edits atomically |
| `configRequirements/read` | Fetch requirements from `requirements.toml` and/or MDM |
| `fs/readFile`, `fs/writeFile`, `fs/createDirectory`, `fs/getMetadata`, `fs/readDirectory`, `fs/remove`, `fs/copy`, `fs/watch`, `fs/unwatch`, `fs/changed` (notify) | v2 filesystem API on absolute paths |

Plugin `source` union:
- Local: `{ "type": "local", "path": ... }`
- Git: `{ "type": "git", "url": ..., "path": ..., "refName": ..., "sha": ... }`
- Remote: `{ "type": "remote" }`

For remote-only catalog entries, `PluginMarketplaceEntry.path` may be `null`; pass `remoteMarketplaceName` instead of `marketplacePath`.

## Models

### List models (`model/list`)

Discover available models and capabilities before rendering selectors.
```json
{ "method": "model/list", "id": 6, "params": { "limit": 20, "includeHidden": false } }
```

Response includes:
- `supportedReasoningEfforts` — effort options
- `defaultReasoningEffort` — suggested default
- `upgrade` — recommended upgrade model id
- `upgradeInfo` — upgrade metadata
- `hidden` — hidden from default picker
- `inputModalities` — supported input types (e.g., `text`, `image`)
- `supportsPersonality` — supports personality-specific instructions
- `isDefault` — recommended default

Default returns picker-visible models only. Set `includeHidden: true` for full list. When `inputModalities` missing (older catalogs), treat as `["text", "image"]`.

### List experimental features (`experimentalFeature/list`)

```json
{ "method": "experimentalFeature/list", "id": 7, "params": { "limit": 20 } }
```

`stage` values: `beta`, `underDevelopment`, `stable`, `deprecated`, `removed`. For non-beta flags, `displayName`, `description`, `announcement` may be `null`.

## Threads

### Start or resume a thread

```json
{ "method": "thread/start", "id": 10, "params": {
  "model": "gpt-5.4", "cwd": "/Users/me/project",
  "approvalPolicy": "never", "sandbox": "workspaceWrite",
  "personality": "friendly", "serviceName": "my_app_server_client"
} }
```

`serviceName` optional — tags thread-level metrics with your integration's service name.

`thread/resume` continues stored session by `thread.id`. Response shape matches `thread/start`. Supports same overrides (e.g., `personality`).

Resuming doesn't update `thread.updatedAt` by itself — timestamp updates when you start a turn.

If enabled MCP server is `required` and fails to initialize, `thread/start` and `thread/resume` fail.

`dynamicTools` on `thread/start` is experimental (requires `experimentalApi`). Persisted in thread rollout metadata; restored on `thread/resume` when no new dynamic tools supplied.

If resuming with different model than recorded in rollout, Codex emits warning and applies one-time model-switch instruction on next turn.

`thread/fork` branches from stored session, creating new thread id and emitting `thread/started`.

When user-facing title set, app-server hydrates `thread.name` on `thread/list`, `thread/read`, `thread/resume`, `thread/unarchive`, `thread/rollback`. `thread/start` and `thread/fork` may omit `name` until title set later.

### Read a stored thread (without resuming)

`thread/read` — `includeTurns` for full history. Returned `thread` includes runtime `status` (`notLoaded`, `idle`, `systemError`, `active` with `activeFlags`).

Unlike `thread/resume`, doesn't load into memory or emit `thread/started`.

### List thread turns

`thread/turns/list` — pages stored turn history without resuming. Default newest-first. `nextCursor` for older turns; `backwardsCursor` with `sortDirection: "asc"` for newer turns.

### List threads (with pagination & filters)

`thread/list` — filters: `cursor`, `limit`, `sortKey` (`created_at` or `updated_at`), `modelProviders`, `sourceKinds` (`cli`, `vscode`, `exec`, `appServer`, `subAgent`, `subAgentReview`, `subAgentCompact`, `subAgentThreadSpawn`, `subAgentOther`, `unknown`), `archived`, `cwd`, `searchTerm`.

Default `sourceKinds`: interactive only (`cli`, `vscode`).

### Update stored thread metadata

`thread/metadata/update` — patches stored metadata. Today supports `gitInfo`; omitted fields unchanged, explicit `null` clears.

### Track thread status changes

`thread/status/changed` notification — `threadId` + new `status`.

### Unsubscribe from a loaded thread

`thread/unsubscribe` — removes connection's subscription. Status: `unsubscribed`, `notSubscribed`, `notLoaded`.

If last subscriber, server keeps thread loaded for 30 minutes of inactivity, then unloads and emits `thread/status/changed` → `notLoaded` + `thread/closed`.

### Archive / unarchive

`thread/archive` — moves persisted JSONL log to archived directory; emits `thread/archived`. Archived threads excluded from `thread/list` unless `archived: true`.

`thread/unarchive` — restores to active sessions directory; emits `thread/unarchived`.

### Trigger thread compaction

`thread/compact/start` — returns `{}` immediately. Progress streams via `turn/*` and `item/*` notifications, including `contextCompaction` item lifecycle.

### Run a thread shell command

`thread/shellCommand` — user-initiated shell command running **outside sandbox with full access**, not inheriting thread sandbox policy.

Returns `{}` immediately; progress streams via notifications. If thread has active turn, command runs as auxiliary action with output injected into message stream. If idle, starts standalone turn.

### Clean background terminals

`thread/backgroundTerminals/clean` — stops all background terminals for thread. Experimental; requires `experimentalApi`.

### Roll back recent turns

`thread/rollback` — removes last `numTurns` entries from in-memory context, persists rollback marker. Returned `thread` includes `turns` after rollback.

## Turns

`input` accepts items:
- `{ "type": "text", "text": "..." }`
- `{ "type": "image", "url": "https://..." }`
- `{ "type": "localImage", "path": "/tmp/..." }`

Override per turn: model, effort, personality, `cwd`, sandbox policy, summary. These become defaults for later turns on same thread. `outputSchema` applies only to current turn.

For `sandboxPolicy.type = "externalSandbox"`, set `networkAccess` to `restricted` or `enabled`; for `workspaceWrite`, `networkAccess` is boolean.

For `turn/start.collaborationMode`, `settings.developer_instructions: null` means "use built-in instructions for selected mode."

### Sandbox read access (`ReadOnlyAccess`)

`sandboxPolicy` supports explicit read-access controls:
- `readOnly`: optional `access` (`{ "type": "fullAccess" }` default, or restricted roots)
- `workspaceWrite`: optional `readOnlyAccess` (`{ "type": "fullAccess" }` default, or restricted roots)

Restricted read access shape:
```json
{ "type": "restricted", "includePlatformDefaults": true, "readableRoots": ["/Users/me/shared-read-only"] }
```

On macOS, `includePlatformDefaults: true` appends curated platform-default Seatbelt policy for restricted-read sessions.

Examples:
```json
{ "type": "readOnly", "access": { "type": "fullAccess" } }
{ "type": "workspaceWrite", "writableRoots": ["/Users/me/project"], "readOnlyAccess": { "type": "restricted", "includePlatformDefaults": true, "readableRoots": ["/Users/me/shared-read-only"] }, "networkAccess": false }
```

### Start a turn

```json
{ "method": "turn/start", "id": 30, "params": {
  "threadId": "thr_123",
  "input": [{ "type": "text", "text": "Run tests" }],
  "cwd": "/Users/me/project",
  "approvalPolicy": "unlessTrusted",
  "sandboxPolicy": { "type": "workspaceWrite", "writableRoots": ["/Users/me/project"], "networkAccess": true },
  "model": "gpt-5.4", "effort": "medium", "summary": "concise", "personality": "friendly",
  "outputSchema": { "type": "object", "properties": { "answer": { "type": "string" } }, "required": ["answer"], "additionalProperties": false }
} }
```

### Inject items into a thread

`thread/inject_items` — append prebuilt Responses API items to loaded thread's prompt history without starting user turn. Persisted to rollout and included in subsequent model requests.

### Steer an active turn

`turn/steer` — append more user input to in-flight turn.
- Include `expectedTurnId`; must match active turn id
- Fails if no active turn
- Doesn't emit new `turn/started`
- Doesn't accept turn-level overrides (`model`, `cwd`, `sandboxPolicy`, `outputSchema`)

### Invoke a skill

Include `$\u003cskill-name\u003e` in text input and add `skill` input item:
```json
{ "method": "turn/start", "id": 33, "params": {
  "threadId": "thr_123",
  "input": [
    { "type": "text", "text": "$skill-creator Add a new skill for triaging flaky CI..." },
    { "type": "skill", "name": "skill-creator", "path": "/Users/me/.codex/skills/skill-creator/SKILL.md" }
  ]
} }
```

### Interrupt a turn

`turn/interrupt` — on success, turn finishes with `status: "interrupted"`.

## Review

`review/start` runs Codex reviewer for thread. Targets:
- `uncommittedChanges`
- `baseBranch` (diff against branch)
- `commit` (review specific commit)
- `custom` (free-form instructions)

`delivery: "inline"` (default) — review on existing thread. `delivery: "detached"` — fork new review thread.

Example:
```json
{ "method": "review/start", "id": 40, "params": {
  "threadId": "thr_123", "delivery": "inline",
  "target": { "type": "commit", "sha": "1234567deadbeef", "title": "Polish tui colors" }
} }
```

Detached review: `reviewThreadId` is new review thread id (different from original). Server emits `thread/started` for new thread before streaming review turn.

Codex streams `turn/started` then `item/started` with `enteredReviewMode` item. When reviewer finishes, emits `item/started` + `item/completed` containing `exitedReviewMode` with final review text.

## Command execution

`command/exec` — run single `argv` command under server sandbox without creating thread.

```json
{ "method": "command/exec", "id": 50, "params": {
  "command": ["ls", "-la"], "cwd": "/Users/me/project",
  "sandboxPolicy": { "type": "workspaceWrite" }, "timeoutMs": 10000
} }
```

Use `sandboxPolicy.type = "externalSandbox"` if you already sandbox the server process and want Codex to skip its own sandbox. For external sandbox, set `networkAccess` to `restricted` (default) or `enabled`.

Notes:
- Empty `command` arrays rejected
- `sandboxPolicy` accepts same shape as `turn/start` (`dangerFullAccess`, `readOnly`, `workspaceWrite`, `externalSandbox`)
- `timeoutMs` falls back to server default when omitted
- `tty: true` for PTY-backed sessions; use `processId` for follow-up with `command/exec/write`, `command/exec/resize`, `command/exec/terminate`
- `streamStdoutStderr: true` → receive `command/exec/outputDelta` notifications

### Read admin requirements (`configRequirements/read`)

Inspect effective admin requirements from `requirements.toml` and/or MDM:
```json
{ "method": "configRequirements/read", "id": 52, "params": {} }
```

`result.requirements` is `null` when none configured.

### Windows sandbox setup (`windowsSandbox/setupStart`)

Custom Windows clients can trigger sandbox setup asynchronously:
```json
{ "method": "windowsSandbox/setupStart", "id": 53, "params": { "mode": "elevated" } }
```

Modes: `elevated`, `unelevated`. Returns `{ "started": true }`; later emits `windowsSandbox/setupCompleted`.

## Filesystem

v2 filesystem APIs operate on absolute paths. `fs/watch` invalidates UI state after file/directory changes.

```json
{ "method": "fs/watch", "id": 54, "params": { "watchId": "...", "path": "/Users/me/project/.git/HEAD" } }
{ "method": "fs/changed", "params": { "watchId": "...", "changedPaths": ["/Users/me/project/.git/HEAD"] } }
{ "method": "fs/unwatch", "id": 55, "params": { "watchId": "..." } }
```

Watching a file emits `fs/changed` for that path, including updates from replace or rename operations.

## Events

Server-initiated stream for thread lifecycles, turn lifecycles, and items.

### Notification opt-out

Suppress specific notifications per connection via `initialize.params.capabilities.optOutNotificationMethods`:
- Exact match only
- Unknown names ignored
- Applies to current `thread/*`, `turn/*`, `item/*` notifications
- Doesn't apply to requests, responses, or errors

### Turn events

- `turn/started` — `{ turn }` with id, empty `items`, `status: "inProgress"`
- `turn/completed` — `status`: `completed`, `interrupted`, or `failed` (with `error`)
- `turn/diff/updated` — latest aggregated unified diff across file changes
- `turn/plan/updated` — agent plan updates; each entry `{ step, status }` (`pending`, `inProgress`, `completed`)
- `thread/tokenUsage/updated` — usage updates for active thread

Use `item/*` notifications as source of truth for turn items.

### Items

Common `ThreadItem` types:
- `userMessage` — `{id, content}` (list of `text`, `image`, `localImage`)
- `agentMessage` — `{id, text, phase?}` (`phase`: `commentary`, `final_answer`)
- `plan` — `{id, text}` proposed plan text
- `reasoning` — `{id, summary, content}`
- `commandExecution` — `{id, command, cwd, status, commandActions, aggregatedOutput?, exitCode?, durationMs?}`
- `fileChange` — `{id, changes, status}`; `changes` list `{path, kind, diff}`
- `mcpToolCall` — `{id, server, tool, status, arguments, result?, error?}`
- `dynamicToolCall` — client-executed dynamic tool invocations
- `collabToolCall` — collaboration tool calls
- `webSearch` — `{id, query, action?}` (`search`, `openPage`, `findInPage`)
- `imageView` — `{id, path}`
- `enteredReviewMode` / `exitedReviewMode` — reviewer lifecycle
- `contextCompaction` — history compaction

Lifecycle events:
- `item/started` — full item when work begins
- `item/completed` — final item when work finishes (authoritative state)

### Item deltas

- `item/agentMessage/delta` — streamed text for agent message
- `item/plan/delta` — streamed plan text
- `item/reasoning/summaryTextDelta` — readable reasoning summaries
- `item/reasoning/summaryPartAdded` — boundary between reasoning sections
- `item/reasoning/textDelta` — raw reasoning text
- `item/commandExecution/outputDelta` — stdout/stderr chunks
- `item/fileChange/outputDelta` — `apply_patch` tool call response

## Errors

Turn failure: `error` event with `{ error: { message, codexErrorInfo?, additionalDetails? } }`, then `status: "failed"`. Upstream HTTP status in `codexErrorInfo.httpStatusCode`.

Common `codexErrorInfo`:
- `ContextWindowExceeded`
- `UsageLimitExceeded`
- `HttpConnectionFailed` (4xx/5xx)
- `ResponseStreamConnectionFailed`
- `ResponseStreamDisconnected`
- `ResponseTooManyFailedAttempts`
- `BadRequest`, `Unauthorized`, `SandboxError`, `InternalServerError`, `Other`

## Approvals

Command execution and file changes may require approval. App-server sends server-initiated JSON-RPC request; client responds with decision.

### Command execution approvals

Order:
1. `item/started` — pending `commandExecution` item
2. `item/commandExecution/requestApproval` — `itemId`, `threadId`, `turnId`, optional `reason`, `command`, `cwd`, `commandActions`, `proposedExecpolicyAmendment`, `networkApprovalContext`, `availableDecisions`
3. Client responds: `accept`, `acceptForSession`, `decline`, `cancel`, or `{ "acceptWithExecpolicyAmendment": { "execpolicy_amendment": [...] } }`
4. `serverRequest/resolved` — pending request answered or cleared
5. `item/completed` — final `commandExecution` with `status`

When `networkApprovalContext` present, prompt is for managed network access (not shell command). Schema exposes target `host` and `protocol`; render network-specific prompt.

Codex groups concurrent network approval prompts by destination (`host`, protocol, port). One prompt may unblock multiple queued requests to same destination; different ports on same host treated separately.

### File change approvals

Order:
1. `item/started` — `fileChange` with proposed `changes`, `status: "inProgress"`
2. `item/fileChange/requestApproval` — `itemId`, `threadId`, `turnId`, optional `reason`, `grantRoot`
3. Client responds: `accept`, `acceptForSession`, `decline`, `cancel`
4. `serverRequest/resolved`
5. `item/completed` — final `fileChange` with `status`

### Dynamic tool calls (experimental)

`dynamicTools` on `thread/start` and `item/tool/call` flow are experimental.

When invoked, app-server emits:
1. `item/started` with `item.type = "dynamicToolCall"`, `status = "inProgress"`, plus `tool` and `arguments`
2. `item/tool/call` as server request to client

#app-server #json-rpc #api #websocket #protocol #codex