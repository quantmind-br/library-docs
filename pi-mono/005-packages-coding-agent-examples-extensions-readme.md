---
title: Extension Examples
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/examples/extensions/README.md
source: git
fetched_at: 2026-05-03T09:31:33.627513205-03:00
optimized: true
word_count: 750
summary: Index of pi-coding-agent extension examples covering custom tools, UI elements, lifecycle hooks, system integrations, and agent delegation.
tags:
    - extension-development
    - pi-coding-agent
    - plugin-architecture
    - custom-tools
    - ui-customization
category: reference
---
# Extension Examples

## Quick Start

```bash
# Load extension via flag
pi --extension examples/extensions/permission-gate.ts

# Auto-discovery location
cp permission-gate.ts ~/.pi/agent/extensions/
```

> See [[025-packages-coding-agent-docs-extensions|Extensions]] for full API documentation.

## Extension Categories

### Lifecycle & Safety

| File | Purpose |
|------|---------|
| `permission-gate.ts` | Confirms before dangerous commands (`rm -rf`, `sudo`) |
| `protected-paths.ts` | Blocks writes to `.env`, `.git/`, `node_modules/` |
| `confirm-destructive.ts` | Confirms before destructive session actions |
| `dirty-repo-guard.ts` | Prevents switch with uncommitted git changes |
| `sandbox/` | OS-level sandboxing via `@anthropic-ai/sandbox-runtime` |

### Custom Tools

| File | Purpose |
|------|---------|
| `todo.ts` | Todo list + `/todos` command with state persistence |
| `hello.ts` | Minimal custom tool example |
| `question.ts` | Demonstrates `ctx.ui.select()` for user questions |
| `questionnaire.ts` | Multi-question input with tab navigation |
| `tool-override.ts` | Override built-in tools (add logging/access control) |
| `dynamic-tools.ts` | Register tools post-startup via `session_start` or runtime command |
| `structured-output.ts` | Returns `terminate: true` for agent to end on tool call |
| `built-in-tool-renderer.ts` | Custom compact rendering for built-in tools |
| `minimal-mode.ts` | Minimal tool display (only calls, no output in collapsed) |
| `truncated-tool.ts` | Wraps ripgrep with truncation (50KB/2000 lines) |
| `ssh.ts` | Delegates tools to remote machine via SSH |
| `subagent/` | Delegates tasks to specialized subagents |

### Commands & UI

| File | Purpose |
|------|---------|
| `preset.ts` | Named presets for model/thinking/tools via `--preset` + `/preset` |
| `plan-mode/` | Claude Code-style plan mode with `/plan` command |
| `tools.ts` | Interactive `/tools` to enable/disable tools |
| `handoff.ts` | Transfer context via `/handoff <goal>` |
| `qna.ts` | Extracts questions to editor via `ctx.ui.setEditorText()` |
| `status-line.ts` | Footer progress via `ctx.ui.setStatus()` |
| `github-issue-autocomplete.ts` | `#1234` completions from `gh issue list` |
| `widget-placement.ts` | Widgets above/below editor via `ctx.ui.setWidget()` |
| `hidden-thinking-label.ts` | Custom collapsed thinking label |
| `working-indicator.ts` | Custom streaming indicator |
| `model-status.ts` | Model changes in status bar |
| `snake.ts` | Snake game with custom UI and keyboard handling |
| `tic-tac-toe.ts` | Tic-tac-toe vs agent with `executionMode: "sequential"` |
| `send-user-message.ts` | Demonstrates `pi.sendUserMessage()` |
| `timed-confirm.ts` | `AbortSignal` for auto-dismissing dialogs |
| `rpc-demo.ts` | All RPC extension UI methods |
| `modal-editor.ts` | Vim-like editor via `ctx.ui.setEditorComponent()` |
| `rainbow-editor.ts` | Animated rainbow text effect |
| `notify.ts` | Desktop notifications via OSC 777 (Ghostty, iTerm2, WezTerm) |
| `titlebar-spinner.ts` | Braille spinner in terminal titlebar |
| `summarize.ts` | GPT-5.2 conversation summary in transient UI |
| `custom-footer.ts` | Git branch + token stats via `ctx.ui.setFooter()` |
| `custom-header.ts` | Custom header via `ctx.ui.setHeader()` |
| `overlay-test.ts` | Overlay compositing with inline inputs |
| `overlay-qa-tests.ts` | Comprehensive overlay QA tests |
| `doom-overlay/` | DOOM at 35 FPS as overlay |
| `shutdown-command.ts` | `/quit` demonstrating `ctx.shutdown()` |
| `reload-runtime.ts` | `/reload-runtime` + tool for safe reload |
| `interactive-shell.ts` | Interactive commands (vim, htop) via `user_bash` hook |
| `inline-bash.ts` | Expands `!{command}` patterns via `input` transformation |

### Git Integration

| File | Purpose |
|------|---------|
| `git-checkpoint.ts` | Git stash checkpoints each turn |
| `auto-commit-on-exit.ts` | Auto-commits on exit |

### System Prompt & Compaction

| File | Purpose |
|------|---------|
| `pirate.ts` | Demonstrates `systemPromptAppend` |
| `claude-rules.ts` | Scans `.claude/rules/` for system prompt |
| `custom-compaction.ts` | Custom conversation summarization |
| `trigger-compact.ts` | Compaction at 100k tokens + `/trigger-compact` |

### System Integration

| File | Purpose |
|------|---------|
| `mac-system-theme.ts` | Syncs pi theme with macOS dark/light |

### Resources

| File | Purpose |
|------|---------|
| `dynamic-resources/` | Loads skills, prompts, themes via `resources_discover` |

### Messages & Communication

| File | Purpose |
|------|---------|
| `message-renderer.ts` | Custom message rendering via `registerMessageRenderer` |
| `event-bus.ts` | Inter-extension communication via `pi.events` |

### Session Metadata

| File | Purpose |
|------|---------|
| `session-name.ts` | Names sessions via `setSessionName` |
| `bookmark.ts` | Bookmarks with labels for `/tree` navigation |

### Custom Providers

| File | Purpose |
|------|---------|
| `custom-provider-anthropic/` | Custom Anthropic with OAuth + streaming |
| `custom-provider-gitlab-duo/` | GitLab Duo via pi-ai proxy |

### External Dependencies

| File | Purpose |
|------|---------|
| `with-deps/` | Extension with own `package.json` (jiti resolution) |
| `file-trigger.ts` | Watches trigger file, injects contents |

## Writing Extensions

### Minimal Template

```typescript
import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";
import { Type } from "typebox";

export default function (pi: ExtensionAPI) {
  // Lifecycle events
  pi.on("tool_call", async (event, ctx) => {
    if (event.toolName === "bash" && event.input.command?.includes("rm -rf")) {
      const ok = await ctx.ui.confirm("Dangerous!", "Allow rm -rf?");
      if (!ok) return { block: true, reason: "Blocked by user" };
    }
  });

  // Custom tool
  pi.registerTool({
    name: "greet",
    label: "Greeting",
    description: "Generate a greeting",
    parameters: Type.Object({
      name: Type.String({ description: "Name to greet" }),
    }),
    async execute(toolCallId, params, onUpdate, ctx, signal) {
      return {
        content: [{ type: "text", text: `Hello, ${params.name}!` }],
        details: {},
      };
    },
  });

  // Slash command
  pi.registerCommand("hello", {
    description: "Say hello",
    handler: async (args, ctx) => {
      ctx.ui.notify("Hello!", "info");
    },
  });
}
```

## Key Patterns

> [!IMPORTANT]
> Use `StringEnum` for string parameters (required for Google API compatibility)

```typescript
import { StringEnum } from "@mariozechner/pi-ai";

// Good
action: StringEnum(["list", "add"] as const)

// Bad - incompatible with Google
action: Type.Union([Type.Literal("list"), Type.Literal("add")])
```

> [!NOTE]
> State persistence: store in `details` of tool result for proper fork support

```typescript
// Store state
return {
  content: [{ type: "text", text: "Done" }],
  details: { todos: [...todos], nextId },  // Persisted in session
};

// Reconstruct on session_start
pi.on("session_start", async (_event, ctx) => {
  for (const entry of ctx.sessionManager.getBranch()) {
    if (entry.type === "message" && entry.message.toolName === "my_tool") {
      const details = entry.message.details;
      // Reconstruct state
    }
  }
});
```
