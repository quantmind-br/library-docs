---
title: SDK Examples
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/examples/sdk/README.md
source: git
fetched_at: 2026-05-03T09:31:54.438634241-03:00
optimized: true
word_count: 256
summary: Programmatic agent sessions via createAgentSession() and createAgentSessionRuntime(), covering initialization, configuration, tools, events.
tags:
    - sdk-usage
    - coding-agent
    - typescript
    - session-management
    - agent-configuration
category: guide
---
# SDK Examples

Programmatic usage via `createAgentSession()` and `createAgentSessionRuntime()`.

## Examples Index

| File | Description |
|------|-------------|
| `01-minimal.ts` | Minimal usage, all defaults |
| `02-custom-model.ts` | Select model and thinking level |
| `03-custom-prompt.ts` | Replace/modify system prompt |
| `04-skills.ts` | Discover, filter, replace skills |
| `05-tools.ts` | Built-in and custom tools |
| `06-extensions.ts` | Logging, blocking, result modification |
| `07-context-files.ts` | AGENTS.md context files |
| `08-slash-commands.ts` | File-based slash commands |
| `09-api-keys-and-oauth.ts` | API key resolution, OAuth config |
| `10-settings.ts` | Compaction, retry, terminal settings |
| `11-sessions.ts` | In-memory, persistent, continue, list |
| `12-full-control.ts` | Replace everything, no discovery |
| `13-session-runtime.ts` | Runtime-backed session replacement |

## Running

```bash
cd packages/coding-agent
npx tsx examples/sdk/01-minimal.ts
```

## Quick Reference

### Setup

```typescript
import { getModel } from "@mariozechner/pi-ai";
import {
  AuthStorage, createAgentSession, DefaultResourceLoader,
  ModelRegistry, SessionManager, SettingsManager,
  codingTools, readOnlyTools,
  readTool, bashTool, editTool, writeTool,
} from "@mariozechner/pi-coding-agent";

const authStorage = AuthStorage.create();
const modelRegistry = ModelRegistry.create(authStorage);
```

### Minimal Session

```typescript
const { session } = await createAgentSession({ authStorage, modelRegistry });
```

### Custom Model

```typescript
const model = getModel("anthropic", "claude-opus-4-5");
const { session } = await createAgentSession({
  model, thinkingLevel: "high", authStorage, modelRegistry
});
```

### Modify System Prompt

```typescript
const loader = new DefaultResourceLoader({
  systemPromptOverride: (base) => `${base}\n\nBe concise.`,
});
await loader.reload();
const { session } = await createAgentSession({ resourceLoader: loader, authStorage, modelRegistry });
```

### Read-Only Mode

```typescript
const { session } = await createAgentSession({
  tools: readOnlyTools, authStorage, modelRegistry
});
```

### In-Memory Session

```typescript
const { session } = await createAgentSession({
  sessionManager: SessionManager.inMemory(),
  authStorage, modelRegistry,
});
```

### Full Control

```typescript
const customAuth = AuthStorage.create("/my/app/auth.json");
customAuth.setRuntimeApiKey("anthropic", process.env.MY_KEY!);
const customRegistry = ModelRegistry.create(customAuth);

const resourceLoader = new DefaultResourceLoader({
  systemPromptOverride: () => "You are helpful.",
  extensionFactories: [myExtension],
  skillsOverride: () => ({ skills: [], diagnostics: [] }),
  agentsFilesOverride: () => ({ agentsFiles: [] }),
  promptsOverride: () => ({ prompts: [], diagnostics: [] }),
});
await resourceLoader.reload();

const { session } = await createAgentSession({
  model, authStorage: customAuth, modelRegistry: customRegistry,
  resourceLoader, tools: [readTool, bashTool],
  customTools: [{ tool: myTool }],
  sessionManager: SessionManager.inMemory(),
  settingsManager: SettingsManager.inMemory(),
});
```

### Event Handling

```typescript
session.subscribe((event) => {
  switch (event.type) {
    case "message_update":
      if (event.assistantMessageEvent.type === "text_delta") {
        process.stdout.write(event.assistantMessageEvent.delta);
      }
      break;
    case "tool_execution_start":
      console.log(`Tool: ${event.toolName}`);
      break;
    case "tool_execution_end":
      console.log(`Result: ${event.result}`);
      break;
    case "agent_end":
      console.log("Done");
      break;
  }
});

await session.prompt("Hello");
```

## Options

| Option | Default | Description |
|--------|---------|-------------|
| `authStorage` | `AuthStorage.create()` | Credential storage |
| `modelRegistry` | `ModelRegistry.create(authStorage)` | Model registry |
| `cwd` | `process.cwd()` | Working directory |
| `agentDir` | `~/.pi/agent` | Config directory |
| `model` | From settings/first available | Model to use |
| `thinkingLevel` | From settings/"off" | off, low, medium, high |
| `tools` | `codingTools` | Built-in tools |
| `customTools` | `[]` | Additional tool definitions |
| `resourceLoader` | DefaultResourceLoader | Extensions, skills, prompts, themes |
| `sessionManager` | `SessionManager.create(cwd)` | Persistence |
| `settingsManager` | `SettingsManager.create(cwd, agentDir)` | Settings overrides |
