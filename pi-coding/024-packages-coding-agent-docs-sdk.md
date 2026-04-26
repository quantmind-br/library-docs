---
title: Sdk
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/sdk.md
source: git
fetched_at: 2026-04-26T05:48:22.352821971-03:00
rendered_js: false
word_count: 3669
summary: This document provides an overview and technical reference for the pi SDK, enabling developers to integrate agent capabilities, build custom interfaces, and manage agent session lifecycles programmatically.
tags:
    - sdk-reference
    - agent-framework
    - typescript-api
    - session-management
    - llm-integration
    - event-streaming
category: api
optimized: true
optimized_at: 2026-04-26T09:00:00Z
---

> [!tip] pi can build an SDK integration for your use case — just ask it.

# SDK

The SDK provides programmatic access to pi's agent capabilities — embed pi in apps, build custom interfaces, or integrate with automated workflows.

**Use cases:** custom UI, agent integration into existing apps, automated pipelines with agent reasoning, custom tools spawning sub-agents, programmatic testing.

See [examples/sdk/](../examples/sdk/) for working examples.

## Quick Start

```typescript
import { AuthStorage, createAgentSession, ModelRegistry, SessionManager } from "@mariozechner/pi-coding-agent";

// Set up credential storage and model registry
const authStorage = AuthStorage.create();
const modelRegistry = ModelRegistry.create(authStorage);

const { session } = await createAgentSession({
  sessionManager: SessionManager.inMemory(),
  authStorage,
  modelRegistry,
});

session.subscribe((event) => {
  if (event.type === "message_update" && event.assistantMessageEvent.type === "text_delta") {
    process.stdout.write(event.assistantMessageEvent.delta);
  }
});

await session.prompt("What files are in the current directory?");
```

## Installation

```bash
npm install @mariozechner/pi-coding-agent
```

The SDK is included in the main package — no separate installation needed.

## Core Concepts

### createAgentSession()

Main factory for a single `AgentSession`. Uses a `ResourceLoader` to supply extensions, skills, prompt templates, themes, and context files. Defaults to `DefaultResourceLoader` with standard discovery.

```typescript
import { createAgentSession } from "@mariozechner/pi-coding-agent";

// Minimal: defaults with DefaultResourceLoader
const { session } = await createAgentSession();

// Custom: override specific options
const { session } = await createAgentSession({
  model: myModel,
  tools: [readTool, bashTool],
  sessionManager: SessionManager.inMemory(),
});
```

### AgentSession

Manages agent lifecycle, message history, model state, compaction, and event streaming.

```typescript
interface AgentSession {
  // Send a prompt and wait for completion
  prompt(text: string, options?: PromptOptions): Promise<void>;

  // Queue messages during streaming
  steer(text: string): Promise<void>;
  followUp(text: string): Promise<void>;

  // Subscribe to events (returns unsubscribe function)
  subscribe(listener: (event: AgentSessionEvent) => void): () => void;

  // Session info
  sessionFile: string | undefined;
  sessionId: string;

  // Model control
  setModel(model: Model): Promise<void>;
  setThinkingLevel(level: ThinkingLevel): void;
  cycleModel(): Promise<ModelCycleResult | undefined>;
  cycleThinkingLevel(): ThinkingLevel | undefined;

  // State access
  agent: Agent;
  model: Model | undefined;
  thinkingLevel: ThinkingLevel;
  messages: AgentMessage[];
  isStreaming: boolean;

  // In-place tree navigation within the current session file
  navigateTree(targetId: string, options?: { summarize?: boolean; customInstructions?: string; replaceInstructions?: boolean; label?: string }): Promise<{ editorText?: string; cancelled: boolean }>;

  // Compaction
  compact(customInstructions?: string): Promise<CompactionResult>;
  abortCompaction(): void;

  // Abort current operation
  abort(): Promise<void>;

  // Cleanup
  dispose(): void;
}
```

> [!note] Session replacement APIs (new-session, resume, fork, import) live on `AgentSessionRuntime`, not on `AgentSession`.

### createAgentSessionRuntime() and AgentSessionRuntime

Use the runtime API to replace the active session and rebuild cwd-bound runtime state — the same layer used by built-in interactive, print, and RPC modes.

`createAgentSessionRuntime()` takes a runtime factory plus the initial cwd/session target. The factory closes over process-global fixed inputs, recreates cwd-bound services, resolves session options, and returns a full runtime result.

```typescript
import {
  type CreateAgentSessionRuntimeFactory,
  createAgentSessionFromServices,
  createAgentSessionRuntime,
  createAgentSessionServices,
  getAgentDir,
  SessionManager,
} from "@mariozechner/pi-coding-agent";

const createRuntime: CreateAgentSessionRuntimeFactory = async ({ cwd, sessionManager, sessionStartEvent }) => {
  const services = await createAgentSessionServices({ cwd });
  return {
    ...(await createAgentSessionFromServices({
      services,
      sessionManager,
      sessionStartEvent,
    })),
    services,
    diagnostics: services.diagnostics,
  };
};

const runtime = await createAgentSessionRuntime(createRuntime, {
  cwd: process.cwd(),
  agentDir: getAgentDir(),
  sessionManager: SessionManager.create(process.cwd()),
});
```

`AgentSessionRuntime` handles replacement of the active runtime across:

- `newSession()` / `switchSession()` / `fork()` / clone via `fork(entryId, { position: "at" })` / `importFromJsonl()`

> [!warning] After replacement operations:
> - `runtime.session` changes — re-subscribe to events
> - Re-call `runtime.session.bindExtensions(...)` if using extensions
> - Creation returns diagnostics on `runtime.diagnostics`
> - On failure, the method throws — caller handles the error

```typescript
let session = runtime.session;
let unsubscribe = session.subscribe(() => {});

await runtime.newSession();

unsubscribe();
session = runtime.session;
unsubscribe = session.subscribe(() => {});
```

### Prompting and Message Queueing

`PromptOptions` controls prompt expansion, queueing behavior while streaming, and prompt preflight notifications:

```typescript
interface PromptOptions {
  expandPromptTemplates?: boolean;
  images?: ImageContent[];
  streamingBehavior?: "steer" | "followUp";
  source?: InputSource;
  preflightResult?: (success: boolean) => void;
}
```

`preflightResult` fires once per `prompt()` invocation:
- `true` — prompt was accepted, queued, or handled immediately
- `false` — preflight rejected before acceptance

It fires before `prompt()` resolves. `prompt()` resolves only after the full accepted run finishes (including retries). Post-acceptance failures are reported through the event/message stream, not `preflightResult`.

```typescript
// Basic prompt (when not streaming)
await session.prompt("What files are here?");

// With images
await session.prompt("What's in this image?", {
  images: [{ type: "image", source: { type: "base64", mediaType: "image/png", data: "..." } }]
});

// During streaming: must specify how to queue the message
await session.prompt("Stop and do this instead", { streamingBehavior: "steer" });
await session.prompt("After you're done, also check X", { streamingBehavior: "followUp" });
```

**`prompt()` behavior:**

| Input | Behavior |
|---|---|
| Extension commands (e.g. `/mycommand`) | Execute immediately, even during streaming; manage own LLM interaction via `pi.sendMessage()` |
| File-based prompt templates (`.md` files) | Expanded to content before sending or queueing |
| During streaming without `streamingBehavior` | Throws error — use `steer()`, `followUp()`, or specify the option |

For explicit queueing during streaming:

```typescript
await session.steer("New instruction"); // delivered after current turn's tool calls finish
await session.followUp("After you're done, also do this"); // delivered only when agent stops
```

> [!note] `steer()` and `followUp()` expand file-based prompt templates but error on extension commands (cannot be queued).

### Agent and AgentState

`Agent` (from `@mariozechner/pi-agent-core`) handles core LLM interaction. Access via `session.agent`.

```typescript
const state = session.agent.state;
// state.messages: AgentMessage[]
// state.model: Model
// state.thinkingLevel: ThinkingLevel
// state.systemPrompt: string
// state.tools: AgentTool[]
// state.streamingMessage?: AgentMessage
// state.errorMessage?: string

// Replace messages (branching/restoration) — copies top-level array
session.agent.state.messages = messages;

// Replace tools — copies top-level array
session.agent.state.tools = tools;

// Wait for agent to finish processing
await session.agent.waitForIdle();
```

### Events

Subscribe to events for streaming output and lifecycle notifications.

```typescript
session.subscribe((event) => {
  switch (event.type) {
    // Streaming text from assistant
    case "message_update":
      if (event.assistantMessageEvent.type === "text_delta") {
        process.stdout.write(event.assistantMessageEvent.delta);
      }
      if (event.assistantMessageEvent.type === "thinking_delta") {
        // Thinking output (if thinking enabled)
      }
      break;
    
    // Tool execution
    case "tool_execution_start":
      console.log(`Tool: ${event.toolName}`);
      break;
    case "tool_execution_update":
      // Streaming tool output
      break;
    case "tool_execution_end":
      console.log(`Result: ${event.isError ? "error" : "success"}`);
      break;
    
    // Message lifecycle
    case "message_start":
      // New message starting
      break;
    case "message_end":
      // Message complete
      break;
    
    // Agent lifecycle
    case "agent_start":
      // Agent started processing prompt
      break;
    case "agent_end":
      // Agent finished (event.messages contains new messages)
      break;
    
    // Turn lifecycle (one LLM response + tool calls)
    case "turn_start":
      break;
    case "turn_end":
      // event.message: assistant response
      // event.toolResults: tool results from this turn
      break;
    
    // Session events (queue, compaction, retry)
    case "queue_update":
      console.log(event.steering, event.followUp);
      break;
    case "compaction_start":
    case "compaction_end":
    case "auto_retry_start":
    case "auto_retry_end":
      break;
  }
});
```

## Options Reference

### Directories

```typescript
const { session } = await createAgentSession({
  cwd: process.cwd(),      // Working directory for DefaultResourceLoader discovery
  agentDir: "~/.pi/agent", // Global config directory (expands ~)
});
```

**`cwd` — used by `DefaultResourceLoader` for:**

- Project extensions (`.pi/extensions/`)
- Project skills: `.pi/skills/`, `.agents/skills/` in cwd and ancestors (up to git repo root or filesystem root)
- Project prompts (`.pi/prompts/`)
- Context files (`AGENTS.md` walking up from cwd)
- Session directory naming

**`agentDir` — used by `DefaultResourceLoader` for:**

- Global extensions (`extensions/`)
- Global skills: `skills/` under agentDir (e.g. `~/.pi/agent/skills/`), `~/.agents/skills/`
- Global prompts (`prompts/`)
- Global context file (`AGENTS.md`)
- Settings (`settings.json`), custom models (`models.json`), credentials (`auth.json`), sessions (`sessions/`)

> [!note] With a custom `ResourceLoader`, `cwd`/`agentDir` no longer control resource discovery but still influence session naming and tool path resolution.

### Model

```typescript
import { getModel } from "@mariozechner/pi-ai";
import { AuthStorage, ModelRegistry } from "@mariozechner/pi-coding-agent";

const authStorage = AuthStorage.create();
const modelRegistry = ModelRegistry.create(authStorage);

const opus = getModel("anthropic", "claude-opus-4-5"); // doesn't check API key
const customModel = modelRegistry.find("my-provider", "my-model"); // includes models.json
const available = await modelRegistry.getAvailable(); // only models with valid API keys

const { session } = await createAgentSession({
  model: opus,
  thinkingLevel: "medium", // off, minimal, low, medium, high, xhigh
  scopedModels: [
    { model: opus, thinkingLevel: "high" },
    { model: haiku, thinkingLevel: "off" },
  ],
  authStorage,
  modelRegistry,
});
```

Model fallback when none provided: (1) restore from session if continuing, (2) default from settings, (3) first available model.

> See [examples/sdk/02-custom-model.ts](../examples/sdk/02-custom-model.ts)

### API Keys and OAuth

API key resolution priority (via `AuthStorage`):

| Priority | Source |
|---|---|
| 1 | Runtime overrides (`setRuntimeApiKey`, not persisted) |
| 2 | Stored credentials in `auth.json` (API keys or OAuth tokens) |
| 3 | Environment variables (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, etc.) |
| 4 | Fallback resolver (custom provider keys from `models.json`) |

```typescript
import { AuthStorage, ModelRegistry } from "@mariozechner/pi-coding-agent";

const authStorage = AuthStorage.create();
const modelRegistry = ModelRegistry.create(authStorage);

const { session } = await createAgentSession({
  sessionManager: SessionManager.inMemory(),
  authStorage,
  modelRegistry,
});

authStorage.setRuntimeApiKey("anthropic", "sk-my-temp-key"); // not persisted

// Custom locations
const customAuth = AuthStorage.create("/my/app/auth.json");
const customRegistry = ModelRegistry.create(customAuth, "/my/app/models.json");
const simpleRegistry = ModelRegistry.inMemory(authStorage); // built-in models only
```

> See [examples/sdk/09-api-keys-and-oauth.ts](../examples/sdk/09-api-keys-and-oauth.ts)

### System Prompt

Override via `ResourceLoader`:

```typescript
import { createAgentSession, DefaultResourceLoader } from "@mariozechner/pi-coding-agent";

const loader = new DefaultResourceLoader({
  systemPromptOverride: () => "You are a helpful assistant.",
});
await loader.reload();

const { session } = await createAgentSession({ resourceLoader: loader });
```

> See [examples/sdk/03-custom-prompt.ts](../examples/sdk/03-custom-prompt.ts)

### Tools

```typescript
import {
  codingTools,   // read, bash, edit, write (default)
  readOnlyTools, // read, grep, find, ls
  readTool, bashTool, editTool, writeTool,
  grepTool, findTool, lsTool,
} from "@mariozechner/pi-coding-agent";

const { session } = await createAgentSession({ tools: readOnlyTools });
const { session } = await createAgentSession({ tools: [readTool, bashTool, grepTool] });
```

#### Tools with Custom cwd

> [!warning] Pre-built tool instances use `process.cwd()`. When specifying both `cwd` (different from `process.cwd()`) AND `tools`, use factory functions:

```typescript
import {
  createCodingTools, createReadOnlyTools,
  createReadTool, createBashTool, createEditTool, createWriteTool,
  createGrepTool, createFindTool, createLsTool,
} from "@mariozechner/pi-coding-agent";

const cwd = "/path/to/project";

const { session } = await createAgentSession({
  cwd,
  tools: createCodingTools(cwd),
});

const { session } = await createAgentSession({
  cwd,
  tools: [createReadTool(cwd), createBashTool(cwd), createGrepTool(cwd)],
});
```

| Scenario | Use factories? |
|---|---|
| Omit `tools` | No — pi creates them with correct `cwd` |
| `cwd` = `process.cwd()` | No — pre-built instances work |
| Custom `cwd` AND explicit `tools` | **Yes** |

> See [examples/sdk/05-tools.ts](../examples/sdk/05-tools.ts)

### Custom Tools

```typescript
import { Type } from "typebox";
import { createAgentSession, defineTool } from "@mariozechner/pi-coding-agent";

const myTool = defineTool({
  name: "my_tool",
  label: "My Tool",
  description: "Does something useful",
  parameters: Type.Object({
    input: Type.String({ description: "Input value" }),
  }),
  execute: async (_toolCallId, params) => ({
    content: [{ type: "text", text: `Result: ${params.input}` }],
    details: {},
  }),
});

const { session } = await createAgentSession({ customTools: [myTool] });
```

- Use `defineTool()` for standalone definitions and `customTools` arrays
- `customTools` are combined with extension-registered tools
- Extensions loaded by ResourceLoader can also register tools via `pi.registerTool()`

> See [examples/sdk/05-tools.ts](../examples/sdk/05-tools.ts)

### Extensions

Extensions are loaded by `ResourceLoader`. `DefaultResourceLoader` discovers from `~/.pi/agent/extensions/`, `.pi/extensions/`, and settings.json sources.

```typescript
import { createAgentSession, DefaultResourceLoader } from "@mariozechner/pi-coding-agent";

const loader = new DefaultResourceLoader({
  additionalExtensionPaths: ["/path/to/my-extension.ts"],
  extensionFactories: [
    (pi) => {
      pi.on("agent_start", () => console.log("[Inline Extension] Agent starting"));
    },
  ],
});
await loader.reload();

const { session } = await createAgentSession({ resourceLoader: loader });
```

Extensions can register tools, subscribe to events, add commands. See [extensions.md](extensions.md) for full API.

**Event Bus** — extensions communicate via `pi.events`. Pass a shared `eventBus` for external emit/listen:

```typescript
import { createEventBus, DefaultResourceLoader } from "@mariozechner/pi-coding-agent";

const eventBus = createEventBus();
const loader = new DefaultResourceLoader({ eventBus });
await loader.reload();

eventBus.on("my-extension:status", (data) => console.log(data));
```

> See [examples/sdk/06-extensions.ts](../examples/sdk/06-extensions.ts) and [docs/extensions.md](extensions.md)

### Skills

```typescript
import { createAgentSession, DefaultResourceLoader, type Skill } from "@mariozechner/pi-coding-agent";

const customSkill: Skill = {
  name: "my-skill",
  description: "Custom instructions",
  filePath: "/path/to/SKILL.md",
  baseDir: "/path/to",
  source: "custom",
};

const loader = new DefaultResourceLoader({
  skillsOverride: (current) => ({
    skills: [...current.skills, customSkill],
    diagnostics: current.diagnostics,
  }),
});
await loader.reload();

const { session } = await createAgentSession({ resourceLoader: loader });
```

> See [examples/sdk/04-skills.ts](../examples/sdk/04-skills.ts)

### Context Files

```typescript
import { createAgentSession, DefaultResourceLoader } from "@mariozechner/pi-coding-agent";

const loader = new DefaultResourceLoader({
  agentsFilesOverride: (current) => ({
    agentsFiles: [
      ...current.agentsFiles,
      { path: "/virtual/AGENTS.md", content: "# Guidelines\n\n- Be concise" },
    ],
  }),
});
await loader.reload();

const { session } = await createAgentSession({ resourceLoader: loader });
```

> See [examples/sdk/07-context-files.ts](../examples/sdk/07-context-files.ts)

### Slash Commands

```typescript
import { createAgentSession, DefaultResourceLoader, type PromptTemplate } from "@mariozechner/pi-coding-agent";

const customCommand: PromptTemplate = {
  name: "deploy",
  description: "Deploy the application",
  source: "(custom)",
  content: "# Deploy\n\n1. Build\n2. Test\n3. Deploy",
};

const loader = new DefaultResourceLoader({
  promptsOverride: (current) => ({
    prompts: [...current.prompts, customCommand],
    diagnostics: current.diagnostics,
  }),
});
await loader.reload();

const { session } = await createAgentSession({ resourceLoader: loader });
```

> See [examples/sdk/08-prompt-templates.ts](../examples/sdk/08-prompt-templates.ts)

### Session Management

Sessions use a tree structure with `id`/`parentId` linking, enabling in-place branching.

```typescript
import {
  type CreateAgentSessionRuntimeFactory,
  createAgentSession,
  createAgentSessionFromServices,
  createAgentSessionRuntime,
  createAgentSessionServices,
  getAgentDir,
  SessionManager,
} from "@mariozechner/pi-coding-agent";

// In-memory (no persistence)
const { session } = await createAgentSession({
  sessionManager: SessionManager.inMemory(),
});

// New persistent session
const { session: persisted } = await createAgentSession({
  sessionManager: SessionManager.create(process.cwd()),
});

// Continue most recent
const { session: continued, modelFallbackMessage } = await createAgentSession({
  sessionManager: SessionManager.continueRecent(process.cwd()),
});
if (modelFallbackMessage) {
  console.log("Note:", modelFallbackMessage);
}

// Open specific file
const { session: opened } = await createAgentSession({
  sessionManager: SessionManager.open("/path/to/session.jsonl"),
});

// List sessions
const currentProjectSessions = await SessionManager.list(process.cwd());
const allSessions = await SessionManager.listAll(process.cwd());

// Runtime for replacement APIs
const createRuntime: CreateAgentSessionRuntimeFactory = async ({ cwd, sessionManager, sessionStartEvent }) => {
  const services = await createAgentSessionServices({ cwd });
  return {
    ...(await createAgentSessionFromServices({ services, sessionManager, sessionStartEvent })),
    services,
    diagnostics: services.diagnostics,
  };
};

const runtime = await createAgentSessionRuntime(createRuntime, {
  cwd: process.cwd(),
  agentDir: getAgentDir(),
  sessionManager: SessionManager.create(process.cwd()),
});

await runtime.newSession();
await runtime.switchSession("/path/to/session.jsonl");
await runtime.fork("entry-id");
await runtime.fork("entry-id", { position: "at" }); // clone
```

**SessionManager tree API:**

```typescript
const sm = SessionManager.open("/path/to/session.jsonl");

const currentProjectSessions = await SessionManager.list(process.cwd());
const allSessions = await SessionManager.listAll(process.cwd());

const entries = sm.getEntries();        // All entries (excludes header)
const tree = sm.getTree();              // Full tree structure
const path = sm.getPath();              // Path from root to current leaf
const leaf = sm.getLeafEntry();         // Current leaf entry
const entry = sm.getEntry(id);          // Get entry by ID
const children = sm.getChildren(id);    // Direct children of entry

const label = sm.getLabel(id);          // Get label for entry
sm.appendLabelChange(id, "checkpoint"); // Set label

sm.branch(entryId);                     // Move leaf to earlier entry
sm.branchWithSummary(id, "Summary..."); // Branch with context summary
sm.createBranchedSession(leafId);       // Extract path to new file
```

> See [examples/sdk/11-sessions.ts](../examples/sdk/11-sessions.ts) and [docs/session.md](session.md)

### Settings Management

```typescript
import { createAgentSession, SettingsManager, SessionManager } from "@mariozechner/pi-coding-agent";

// Default: loads from files (global + project merged)
const { session } = await createAgentSession({
  settingsManager: SettingsManager.create(),
});

// With overrides
const settingsManager = SettingsManager.create();
settingsManager.applyOverrides({
  compaction: { enabled: false },
  retry: { enabled: true, maxRetries: 5 },
});
const { session } = await createAgentSession({ settingsManager });

// In-memory (no file I/O, for testing)
const { session } = await createAgentSession({
  settingsManager: SettingsManager.inMemory({ compaction: { enabled: false } }),
  sessionManager: SessionManager.inMemory(),
});

// Custom directories
const { session } = await createAgentSession({
  settingsManager: SettingsManager.create("/custom/cwd", "/custom/agent"),
});
```

**Static factories:**
- `SettingsManager.create(cwd?, agentDir?)` — load from files
- `SettingsManager.inMemory(settings?)` — no file I/O

**Merge order:** global `~/.pi/agent/settings.json` + project `<cwd>/.pi/settings.json`. Project overrides global. Nested objects merge keys. Setters modify global by default.

**Persistence semantics:**
- Getters/setters are synchronous for in-memory state
- Setters enqueue async persistence writes
- Call `await settingsManager.flush()` for durability boundaries (before process exit or test assertions)
- `SettingsManager` does not print I/O errors — use `settingsManager.drainErrors()` and report in your app layer

> See [examples/sdk/10-settings.ts](../examples/sdk/10-settings.ts)

## ResourceLoader

`DefaultResourceLoader` discovers extensions, skills, prompts, themes, and context files.

```typescript
import { DefaultResourceLoader, getAgentDir } from "@mariozechner/pi-coding-agent";

const loader = new DefaultResourceLoader({ cwd, agentDir: getAgentDir() });
await loader.reload();

const extensions = loader.getExtensions();
const skills = loader.getSkills();
const prompts = loader.getPrompts();
const themes = loader.getThemes();
const contextFiles = loader.getAgentsFiles().agentsFiles;
```

## Return Value

`createAgentSession()` returns:

```typescript
interface CreateAgentSessionResult {
  session: AgentSession;
  extensionsResult: LoadExtensionsResult;
  modelFallbackMessage?: string; // warning if session model couldn't be restored
}

interface LoadExtensionsResult {
  extensions: Extension[];
  errors: Array<{ path: string; error: string }>;
  runtime: ExtensionRuntime;
}
```

## Complete Example

```typescript
import { getModel } from "@mariozechner/pi-ai";
import { Type } from "typebox";
import {
  AuthStorage,
  bashTool,
  createAgentSession,
  DefaultResourceLoader,
  defineTool,
  ModelRegistry,
  readTool,
  SessionManager,
  SettingsManager,
} from "@mariozechner/pi-coding-agent";

// Set up auth storage (custom location)
const authStorage = AuthStorage.create("/custom/agent/auth.json");

// Runtime API key override (not persisted)
if (process.env.MY_KEY) {
  authStorage.setRuntimeApiKey("anthropic", process.env.MY_KEY);
}

// Model registry (no custom models.json)
const modelRegistry = ModelRegistry.create(authStorage);

// Inline tool
const statusTool = defineTool({
  name: "status",
  label: "Status",
  description: "Get system status",
  parameters: Type.Object({}),
  execute: async () => ({
    content: [{ type: "text", text: `Uptime: ${process.uptime()}s` }],
    details: {},
  }),
});

const model = getModel("anthropic", "claude-opus-4-5");
if (!model) throw new Error("Model not found");

// In-memory settings with overrides
const settingsManager = SettingsManager.inMemory({
  compaction: { enabled: false },
  retry: { enabled: true, maxRetries: 2 },
});

const loader = new DefaultResourceLoader({
  cwd: process.cwd(),
  agentDir: "/custom/agent",
  settingsManager,
  systemPromptOverride: () => "You are a minimal assistant. Be concise.",
});
await loader.reload();

const { session } = await createAgentSession({
  cwd: process.cwd(),
  agentDir: "/custom/agent",

  model,
  thinkingLevel: "off",
  authStorage,
  modelRegistry,

  tools: [readTool, bashTool],
  customTools: [statusTool],
  resourceLoader: loader,

  sessionManager: SessionManager.inMemory(),
  settingsManager,
});

session.subscribe((event) => {
  if (event.type === "message_update" && event.assistantMessageEvent.type === "text_delta") {
    process.stdout.write(event.assistantMessageEvent.delta);
  }
});

await session.prompt("Get status and list files.");
```

## Run Modes

The SDK exports run mode utilities for building custom interfaces on top of `createAgentSession()`.

### InteractiveMode

Full TUI interactive mode with editor, chat history, and all built-in commands:

```typescript
import {
  type CreateAgentSessionRuntimeFactory,
  createAgentSessionFromServices,
  createAgentSessionRuntime,
  createAgentSessionServices,
  getAgentDir,
  InteractiveMode,
  SessionManager,
} from "@mariozechner/pi-coding-agent";

const createRuntime: CreateAgentSessionRuntimeFactory = async ({ cwd, sessionManager, sessionStartEvent }) => {
  const services = await createAgentSessionServices({ cwd });
  return {
    ...(await createAgentSessionFromServices({ services, sessionManager, sessionStartEvent })),
    services,
    diagnostics: services.diagnostics,
  };
};
const runtime = await createAgentSessionRuntime(createRuntime, {
  cwd: process.cwd(),
  agentDir: getAgentDir(),
  sessionManager: SessionManager.create(process.cwd()),
});

const mode = new InteractiveMode(runtime, {
  migratedProviders: [],
  modelFallbackMessage: undefined,
  initialMessage: "Hello",
  initialImages: [],
  initialMessages: [],
});

await mode.run();
```

### runPrintMode

Single-shot mode: send prompts, output result, exit:

```typescript
import {
  type CreateAgentSessionRuntimeFactory,
  createAgentSessionFromServices,
  createAgentSessionRuntime,
  createAgentSessionServices,
  getAgentDir,
  runPrintMode,
  SessionManager,
} from "@mariozechner/pi-coding-agent";

const createRuntime: CreateAgentSessionRuntimeFactory = async ({ cwd, sessionManager, sessionStartEvent }) => {
  const services = await createAgentSessionServices({ cwd });
  return {
    ...(await createAgentSessionFromServices({ services, sessionManager, sessionStartEvent })),
    services,
    diagnostics: services.diagnostics,
  };
};
const runtime = await createAgentSessionRuntime(createRuntime, {
  cwd: process.cwd(),
  agentDir: getAgentDir(),
  sessionManager: SessionManager.create(process.cwd()),
});

await runPrintMode(runtime, {
  mode: "text",
  initialMessage: "Hello",
  initialImages: [],
  messages: ["Follow up"],
});
```

### runRpcMode

JSON-RPC mode for subprocess integration:

```typescript
import {
  type CreateAgentSessionRuntimeFactory,
  createAgentSessionFromServices,
  createAgentSessionRuntime,
  createAgentSessionServices,
  getAgentDir,
  runRpcMode,
  SessionManager,
} from "@mariozechner/pi-coding-agent";

const createRuntime: CreateAgentSessionRuntimeFactory = async ({ cwd, sessionManager, sessionStartEvent }) => {
  const services = await createAgentSessionServices({ cwd });
  return {
    ...(await createAgentSessionFromServices({ services, sessionManager, sessionStartEvent })),
    services,
    diagnostics: services.diagnostics,
  };
};
const runtime = await createAgentSessionRuntime(createRuntime, {
  cwd: process.cwd(),
  agentDir: getAgentDir(),
  sessionManager: SessionManager.create(process.cwd()),
});

await runRpcMode(runtime);
```

See [RPC documentation](rpc.md) for the JSON protocol.

## RPC Mode Alternative

For subprocess-based integration without the SDK:

```bash
pi --mode rpc --no-session
```

See [RPC documentation](rpc.md) for the JSON protocol.

| SDK preferred for | RPC preferred for |
|---|---|
| Type safety | Another language |
| Same Node.js process | Process isolation |
| Direct agent state access | Language-agnostic client |
| Programmatic tools/extensions customization | |

## Exports

Main entry point exports:

```typescript
// Factory
createAgentSession
createAgentSessionRuntime
AgentSessionRuntime

// Auth and Models
AuthStorage
ModelRegistry

// Resource loading
DefaultResourceLoader
type ResourceLoader
createEventBus

// Helpers
defineTool

// Session management
SessionManager
SettingsManager

// Built-in tools (use process.cwd())
codingTools
readOnlyTools
readTool, bashTool, editTool, writeTool
grepTool, findTool, lsTool

// Tool factories (for custom cwd)
createCodingTools
createReadOnlyTools
createReadTool, createBashTool, createEditTool, createWriteTool
createGrepTool, createFindTool, createLsTool

// Types
type CreateAgentSessionOptions
type CreateAgentSessionResult
type ExtensionFactory
type ExtensionAPI
type ToolDefinition
type Skill
type PromptTemplate
type Tool
```

Extension types: see [extensions.md](extensions.md).

#sdk-reference #typescript-api #session-management #agent-framework #llm-integration
