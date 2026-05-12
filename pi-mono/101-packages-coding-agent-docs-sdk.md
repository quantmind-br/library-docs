---
title: Sdk
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/sdk.md
source: git
fetched_at: 2026-05-03T09:31:19.813130402-03:00
rendered_js: false
word_count: 642
summary: Programmatic SDK for embedding pi agent capabilities in applications — AgentSession API, tools, extensions, skills, session management, settings, and run modes.
tags:
    - sdk
    - agent-sessions
    - typescript
    - automation
    - integration
    - llm-framework
category: api
optimized: true
optimized_at: 2026-05-03T13:07:00Z
---
> [!note]
> Ask pi to build an integration for your use case.

# SDK

Programmatic access to pi's agent capabilities. Embed in applications, build custom interfaces, integrate with automated workflows.

**Use cases:**
- Custom UIs (web, desktop, mobile)
- Integrate agent capabilities into existing apps
- Automated pipelines with agent reasoning
- Spawn sub-agents with custom tools
- Programmatic behavior testing

See [[008-packages-coding-agent-examples-sdk-readme|SDK examples]] from minimal to full control.

## Quick Start

```typescript
import { AuthStorage, createAgentSession, ModelRegistry, SessionManager } from "@mariozechner/pi-coding-agent";

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

SDK included in main package.

## Core Concepts

### `createAgentSession()`

Main factory for `AgentSession`. Uses `DefaultResourceLoader` for extensions, skills, prompts, themes, and context files if not provided.

```typescript
import { createAgentSession } from "@mariozechner/pi-coding-agent";

// Minimal: defaults with DefaultResourceLoader
const { session } = await createAgentSession();

// Custom: override options
const { session } = await createAgentSession({
  model: myModel,
  tools: [readTool, bashTool],
  sessionManager: SessionManager.inMemory(),
});
```

### `AgentSession`

Manages agent lifecycle, message history, model state, compaction, and event streaming.

```typescript
interface AgentSession {
  // Send prompt, wait for completion
  prompt(text: string, options?: PromptOptions): Promise<void>;

  // Queue during streaming
  steer(text: string): Promise<void>;
  followUp(text: string): Promise<void>;

  // Subscribe (returns unsubscribe function)
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

  // Tree navigation
  navigateTree(targetId: string, options?: { summarize?: boolean; customInstructions?: string; replaceInstructions?: boolean; label?: string }): Promise<{ editorText?: string; cancelled: boolean }>;

  // Compaction
  compact(customInstructions?: string): Promise<CompactionResult>;
  abortCompaction(): void;

  // Abort and cleanup
  abort(): Promise<void>;
  dispose(): void;
}
```

Session replacement APIs (`newSession`, `resume`, `fork`, `import`) live on `AgentSessionRuntime`, not `AgentSession`.

### `AgentSessionRuntime`

Use when replacing active session and rebuilding cwd-bound state. Same layer used by interactive, print, and RPC modes.

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
```

`AgentSessionRuntime` owns session replacement:
- `newSession()`, `switchSession()`, `fork()`, clone flows

> [!warning]
> After replacement operations, `runtime.session` changes. Re-subscribe to events and call `runtime.session.bindExtensions(...)` for the new session.

### Prompting and Queueing

```typescript
interface PromptOptions {
  expandPromptTemplates?: boolean;
  images?: ImageContent[];
  streamingBehavior?: "steer" | "followUp";
  source?: InputSource;
  preflightResult?: (success: boolean) => void;
}
```

| Option | Behavior |
|--------|----------|
| `expandPromptTemplates` | Expand file-based templates before sending |
| `streamingBehavior` | Queue strategy during streaming: `"steer"` (after current turn) or `"followUp"` (after agent stops) |
| `preflightResult` | Callback: `true` = accepted/queued/handled, `false` = rejected before acceptance |

```typescript
// Basic prompt
await session.prompt("What files are here?");

// With images
await session.prompt("What's in this image?", {
  images: [{ type: "image", source: { type: "base64", mediaType: "image/png", data: "..." } }]
});

// During streaming: must specify queue strategy
await session.prompt("Stop and do this instead", { streamingBehavior: "steer" });
await session.prompt("After you're done, also check X", { streamingBehavior: "followUp" });
```

**Extension commands** (`/mycommand`): Execute immediately, even during streaming. Manage own LLM interaction via `pi.sendMessage()`.

**File-based templates**: Expanded before sending/queueing.

**During streaming without `streamingBehavior`**: Throws error. Use `steer()` or `followUp()` directly.

### Explicit Queueing

```typescript
// Steering: delivered after current turn finishes tool calls
await session.steer("New instruction");

// Follow-up: delivered only when agent stops
await session.followUp("After you're done, also do this");
```

Both expand file-based templates but error on extension commands.

### `Agent` and `AgentState`

Access via `session.agent`. The `Agent` class (from `@mariozechner/pi-agent-core`) handles core LLM interaction.

```typescript
const state = session.agent.state;

// state.messages: AgentMessage[]
// state.model: Model
// state.thinkingLevel: ThinkingLevel
// state.systemPrompt: string
// state.tools: AgentTool[]
// state.streamingMessage?: AgentMessage (partial message)
// state.errorMessage?: string (latest error)

// Replace messages/tools (copies arrays)
session.agent.state.messages = messages;
session.agent.state.tools = tools;

// Wait for agent idle
await session.agent.waitForIdle();
```

### Events

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
      console.log(`Result: ${event.isError ? "error" : "success"}`);
      break;
    case "agent_start":
    case "agent_end":
    case "turn_start":
    case "turn_end":
    case "message_start":
    case "message_end":
    case "queue_update":
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
  cwd: process.cwd(),           // DefaultResourceLoader discovery base
  agentDir: "~/.pi/agent",      // Global config directory
});
```

| Directory | Used For |
|-----------|----------|
| `cwd` | Project extensions (`.pi/extensions/`), skills (`.pi/skills/`, `.agents/skills/`), prompts (`.pi/prompts/`), context files, session naming |
| `agentDir` | Global extensions, skills, prompts, context, settings, custom models, credentials, sessions |

Custom `ResourceLoader` overrides discovery. `cwd`/`agentDir` still affect session naming and tool path resolution.

### Model

```typescript
import { getModel } from "@mariozechner/pi-ai";
import { AuthStorage, ModelRegistry } from "@mariozechner/pi-coding-agent";

const authStorage = AuthStorage.create();
const modelRegistry = ModelRegistry.create(authStorage);

// Built-in model (doesn't check API key)
const opus = getModel("anthropic", "claude-opus-4-5");

// Custom model from models.json
const customModel = modelRegistry.find("my-provider", "my-model");

// Only models with valid API keys
const available = await modelRegistry.getAvailable();

const { session } = await createAgentSession({
  model: opus,
  thinkingLevel: "medium",  // off, minimal, low, medium, high, xhigh
  scopedModels: [           // Ctrl+P cycling
    { model: opus, thinkingLevel: "high" },
    { model: haiku, thinkingLevel: "off" },
  ],
  authStorage,
  modelRegistry,
});
```

No model provided: try session restore → settings default → first available.

### API Keys and OAuth

Resolution priority:
1. Runtime overrides (`setRuntimeApiKey` — not persisted)
2. `auth.json` credentials
3. Environment variables (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, etc.)
4. Fallback resolver (custom providers from `models.json`)

```typescript
const authStorage = AuthStorage.create();
const modelRegistry = ModelRegistry.create(authStorage);

const { session } = await createAgentSession({
  sessionManager: SessionManager.inMemory(),
  authStorage,
  modelRegistry,
});

// Runtime override (not persisted)
authStorage.setRuntimeApiKey("anthropic", "sk-my-temp-key");

// Custom auth storage
const customAuth = AuthStorage.create("/my/app/auth.json");
const customRegistry = ModelRegistry.create(customAuth, "/my/app/models.json");

// Built-in models only
const simpleRegistry = ModelRegistry.inMemory(authStorage);
```

### System Prompt

```typescript
import { createAgentSession, DefaultResourceLoader } from "@mariozechner/pi-coding-agent";

const loader = new DefaultResourceLoader({
  systemPromptOverride: () => "You are a helpful assistant.",
});
await loader.reload();

const { session } = await createAgentSession({ resourceLoader: loader });
```

### Tools

```typescript
import {
  codingTools,   // read, bash, edit, write
  readOnlyTools, // read, grep, find, ls
  readTool, bashTool, editTool, writeTool,
  grepTool, findTool, lsTool,
} from "@mariozechner/pi-coding-agent";

const { session } = await createAgentSession({
  tools: readOnlyTools,
});

// Pick specific tools
const { session } = await createAgentSession({
  tools: [readTool, bashTool, grepTool],
});
```

> [!warning]
> Pre-built tool instances use `process.cwd()`. When specifying custom `cwd` AND providing tools, use factory functions:

```typescript
import {
  createCodingTools,    // [read, bash, edit, write] for specific cwd
  createReadOnlyTools,   // [read, grep, find, ls] for specific cwd
  createReadTool, createBashTool, createEditTool, createWriteTool,
  createGrepTool, createFindTool, createLsTool,
} from "@mariozechner/pi-coding-agent";

const cwd = "/path/to/project";
const { session } = await createAgentSession({
  cwd,
  tools: createCodingTools(cwd),  // Paths resolve relative to cwd
});
```

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

const { session } = await createAgentSession({
  customTools: [myTool],
});
```

Custom tools combine with extension-registered tools.

### Extensions

Loaded by `ResourceLoader`. `DefaultResourceLoader` discovers from `~/.pi/agent/extensions/`, `.pi/extensions/`, and settings.

```typescript
import { createAgentSession, DefaultResourceLoader } from "@mariozechner/pi-coding-agent";

const loader = new DefaultResourceLoader({
  additionalExtensionPaths: ["/path/to/my-extension.ts"],
  extensionFactories: [
    (pi) => {
      pi.on("agent_start", () => console.log("[Ext] Agent starting"));
    },
  ],
});
await loader.reload();

const { session } = await createAgentSession({ resourceLoader: loader });
```

**Event bus** for cross-extension communication:

```typescript
import { createEventBus, DefaultResourceLoader } from "@mariozechner/pi-coding-agent";

const eventBus = createEventBus();
const loader = new DefaultResourceLoader({ eventBus });
await loader.reload();

eventBus.on("my-extension:status", (data) => console.log(data));
```

See [[025-packages-coding-agent-docs-extensions|extensions.md]] for full API.

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

### Session Management

Sessions use tree structure with `id`/`parentId` linking for in-place branching.

```typescript
import { createAgentSession, SessionManager } from "@mariozechner/pi-coding-agent";

// In-memory
const { session } = await createAgentSession({
  sessionManager: SessionManager.inMemory(),
});

// Persistent
const { session } = await createAgentSession({
  sessionManager: SessionManager.create(process.cwd()),
});

// Continue recent
const { session, modelFallbackMessage } = await createAgentSession({
  sessionManager: SessionManager.continueRecent(process.cwd()),
});

// Open specific file
const { session } = await createAgentSession({
  sessionManager: SessionManager.open("/path/to/session.jsonl"),
});

// List sessions
const projectSessions = await SessionManager.list(process.cwd());
const allSessions = await SessionManager.listAll(process.cwd());
```

**Runtime session replacement:**

```typescript
await runtime.newSession();
await runtime.switchSession("/path/to/session.jsonl");
await runtime.fork("entry-id");
await runtime.fork("entry-id", { position: "at" });
```

**Tree API:**

```typescript
const sm = SessionManager.open("/path/to/session.jsonl");

sm.getEntries();        // All entries
sm.getTree();           // Full tree structure
sm.getPath();           // Path from root to leaf
sm.getLeafEntry();      // Current leaf
sm.getEntry(id);        // Entry by ID
sm.getChildren(id);     // Direct children

sm.getLabel(id);                    // Get label
sm.appendLabelChange(id, "checkpoint"); // Set label

sm.branch(entryId);                 // Move leaf
sm.branchWithSummary(id, "...");    // Branch with summary
sm.createBranchedSession(leafId);  // Extract path to new file
```

See [[102-packages-coding-agent-docs-session-format|session-format.md]] for file format.

### Settings Management

```typescript
import { createAgentSession, SettingsManager, SessionManager } from "@mariozechner/pi-coding-agent";

// Load from files (global + project merged)
const { session } = await createAgentSession({
  settingsManager: SettingsManager.create(),
});

// With overrides
const settingsManager = SettingsManager.create();
settingsManager.applyOverrides({
  compaction: { enabled: false },
  retry: { enabled: true, maxRetries: 5 },
});

// In-memory (no file I/O)
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
- `SettingsManager.create(cwd?, agentDir?)` — Load from files
- `SettingsManager.inMemory(settings?)` — No file I/O

**Merging:** Global (`~/.pi/agent/settings.json`) + Project (`<cwd>/.pi/settings.json`). Project overrides global. Nested objects merge.

**Persistence:**
- Getters/setters synchronous for in-memory state
- Setters enqueue async writes
- `await settingsManager.flush()` for durability boundary
- `settingsManager.drainErrors()` to report I/O errors

## `ResourceLoader`

`DefaultResourceLoader` discovers extensions, skills, prompts, themes, context files.

```typescript
import { DefaultResourceLoader, getAgentDir } from "@mariozechner/pi-coding-agent";

const loader = new DefaultResourceLoader({
  cwd,
  agentDir: getAgentDir(),
});
await loader.reload();

const extensions = loader.getExtensions();
const skills = loader.getSkills();
const prompts = loader.getPrompts();
const themes = loader.getThemes();
const contextFiles = loader.getAgentsFiles().agentsFiles;
```

## Return Value

```typescript
interface CreateAgentSessionResult {
  session: AgentSession;
  extensionsResult: LoadExtensionsResult;
  modelFallbackMessage?: string;  // Warning if session model couldn't be restored
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

// Auth storage
const authStorage = AuthStorage.create("/custom/agent/auth.json");
if (process.env.MY_KEY) {
  authStorage.setRuntimeApiKey("anthropic", process.env.MY_KEY);
}

// Model registry
const modelRegistry = ModelRegistry.create(authStorage);

// Custom tool
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

// Settings (in-memory with overrides)
const settingsManager = SettingsManager.inMemory({
  compaction: { enabled: false },
  retry: { enabled: true, maxRetries: 2 },
});

// Resource loader
const loader = new DefaultResourceLoader({
  cwd: process.cwd(),
  agentDir: "/custom/agent",
  settingsManager,
  systemPromptOverride: () => "You are a minimal assistant. Be concise.",
});
await loader.reload();

// Create session
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

// Subscribe and prompt
session.subscribe((event) => {
  if (event.type === "message_update" && event.assistantMessageEvent.type === "text_delta") {
    process.stdout.write(event.assistantMessageEvent.delta);
  }
});

await session.prompt("Get status and list files.");
```

## Run Modes

SDK exports run mode utilities for custom interfaces.

### `InteractiveMode`

Full TUI with editor, chat history, built-in commands.

```typescript
import { InteractiveMode } from "@mariozechner/pi-coding-agent";

const mode = new InteractiveMode(runtime, {
  migratedProviders: [],
  modelFallbackMessage: undefined,
  initialMessage: "Hello",
  initialImages: [],
  initialMessages: [],
});

await mode.run();
```

### `runPrintMode`

Single-shot: send prompts, output result, exit.

```typescript
import { runPrintMode } from "@mariozechner/pi-coding-agent";

await runPrintMode(runtime, {
  mode: "text",
  initialMessage: "Hello",
  initialImages: [],
  messages: ["Follow up"],
});
```

### `runRpcMode`

JSON-RPC subprocess mode. See [[100-packages-coding-agent-docs-rpc|RPC documentation]].

```typescript
import { runRpcMode } from "@mariozechner/pi-coding-agent";

await runRpcMode(runtime);
```

## SDK vs RPC Mode

| Aspect | SDK | RPC |
|--------|-----|-----|
| Type safety | Full | Client-side |
| Process | Same Node.js | Subprocess |
| State access | Direct | Via events |
| Customization | Tools/extensions programmatically | Command flags |
| Languages | TypeScript/JS | Any |

## Exports

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

// Built-in tools (process.cwd())
codingTools
readOnlyTools
readTool, bashTool, editTool, writeTool
grepTool, findTool, lsTool

// Tool factories (custom cwd)
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

See [[025-packages-coding-agent-docs-extensions|extensions.md]] for extension types.

#sdk #agent-sessions #typescript #automation #integration #llm-framework
