---
title: Appendix
url: https://ampcode.com/manual/appendix
source: crawler
fetched_at: 2026-02-06T02:07:52.623205047-03:00
rendered_js: false
word_count: 2349
summary: This document provides technical guidance on troubleshooting, UI customization, and the configuration of the Amp permission system and MCP registry.
tags:
    - amp-platform
    - debugging-tools
    - permission-management
    - vscode-integration
    - mcp-registry
    - cli-configuration
category: reference
---

We may ask you to share your thread with authorized Amp staff members to help diagnose quality issues:

1. In the Amp sidebar in VS Code or when viewing the thread on ampcode.com, open the sharing menu.
2. Select Share Thread with Support.

You can also share your thread via the CLI:

```
$ amp threads share <thread-id> --support
```

Or, from within a TUI session, open the command palette (`Ctrl-O`) and select `thread: share with support`.

This will allow authorized Amp staff members to view your thread for debugging purposes.

## Visual Studio Code Developer Console[#](#visual-studio-code-developer-console)[#](#visual-studio-code-developer-console)

We may ask you to share information from your Visual Studio Code Developer Console.

**To open the Developer Console:**

**macOS/Windows/Linux:**

- Press `Ctrl/Cmd+Shift+P` to open the Command Palette
- Type “Developer: Toggle Developer Tools” and press Enter

**Or:**

- Use the keyboard shortcut: `Ctrl/Cmd+Option/Alt+I`

The Developer Console will open as a separate window or panel, showing the Console, Network, and other debugging tabs that can help authorized Amp staff members diagnose quality issues.

## Amp CLI in tmux[#](#amp-cli-tmux)[#](#amp-cli-tmux)

Tmux will not distinguish `Shift+Enter` from `Enter` by default. In order for `Shift+Enter` to insert a newline in the Amp CLI, enable `extended-keys` in your tmux config.

```
$ tmux set -s extended-keys on
```

To make it persistent, add `set -s extended-keys on` to `~/.tmux.conf`, then reload: `tmux source-file ~/.tmux.conf`.

Third-party extensions are automatically placed in the primary (left) sidebar in Cursor. To move Amp to the right sidebar:

- Open the Command Pallete using `Ctrl/⌘ + Shift + P`
- Search for `View: Move View`
- Select `Amp` from the drop down list
- Choose your desired location (`New Panel Entry` and `New Secondary Side Bar Entry` are the most common)

## Service Status[#](#service-status)[#](#service-status)

Check [ampcodestatus.com](https://ampcodestatus.com) for service status and to sign up for alerts via email, RSS, Slack. Alternatively, follow [@ampcodestatus](https://x.com/ampcodestatus) on X.

## MCP Registry Allowlist[#](#mcp-registry-allowlist)[#](#mcp-registry-allowlist)

Enterprise workspace admins can enforce an MCP registry so that only approved MCP servers are available to workspace members. If the registry is unreachable, all MCP servers are blocked. The registry protocol and schema are defined at [registry.modelcontextprotocol.io](https://registry.modelcontextprotocol.io/docs#/operations/list-servers-v0.1).

**Set the registry URL:**

1. Open [workspace settings](https://ampcode.com/workspace) and find **MCP Registry**.
2. Enter the registry URL (the `v0.1/servers` endpoint) and save.

**Optionally limit to specific users:**

1. Switch **Apply To** to **Specific users only**.
2. Enter workspace member emails (one per line or comma-separated) and save.

Notes:

- If you scope to specific users, only those users are restricted by the registry; everyone else is unaffected.
- Clear the URL to remove the registry and allow all MCP servers.

## Frequently Ignored Feedback[#](#fif)[#](#fif)

See Amp's [Frequently Ignored Feedback](https://ampcode.com/fif) for the most common valid feedback that we've chosen to not address.

## Permissions Reference[#](#permissions-reference)[#](#permissions-reference)

Amp’s permission system controls **every** tool invocation before execution. The system uses a single, ordered list of rules that are evaluated sequentially until the first match is found.

### How Permissions Work[#](#permissions-how)[#](#permissions-how)

Before running any tool, Amp evaluates permissions through these steps:

1. **Find matching rule**: The first rule that matches the tool *and* its arguments wins
2. **Determine action**: The matching rule tells Amp to:
   
   - `allow` - run the tool silently
   - `reject` - block the call (optionally with custom message)
   - `ask` - prompt the operator for approval
   - `delegate` - delegate decision to an external program
3. **Examine builtin rules**: If no user rule matches, Amp falls back to built-in rules (e.g., allowing `ls` via Bash)
4. **Default Behavior**: If no matching entry is found at all:
   
   - Main thread: Amp asks the operator
   - Sub-agent: Amp rejects the tool call

### Configuration[#](#permissions-configuration)[#](#permissions-configuration)

Rules are defined in the `amp.permissions` setting. Each rule is a JSON object with these properties:

KeyTypeRequiredDescription`tool`string (glob)YesName of the tool this rule applies to. Supports globs (`Bash`, `mcp__playwright__*`, `**/my-tool`)`matches`object–Map of *tool-argument → condition*. If omitted, the rule matches *all* calls to the tool`action``"allow"` / `"reject"` / `"ask"` / `"delegate"`YesWhat Amp should do if the rule matches`context``"thread"` / `"subagent"`–Restrict the rule to the main thread or to sub-agents. Omit to apply everywhere`to`string (program)only when `action = "delegate"`Program that decides. Must be on `$PATH``message`stringonly when `action = "reject"`Message returned to the model. If set, the rejection continues the conversation instead of halting it

### Match Conditions[#](#permissions-match-conditions)[#](#permissions-match-conditions)

Each `matches` key corresponds to a tool argument. Values can be:

- **string** – glob pattern (`*` = any characters) or regex pattern (`/pattern/`)
- **array** – OR of each entry (`["rm -rf *", "git commit *"]`)
- **boolean/number/null/undefined** – literal value match
- **object** – nested structure matching

#### Regular Expression Patterns[#](#permissions-regular-expressions)[#](#permissions-regular-expressions)

Strings that start and end with `/` are treated as regular expressions:

```
{
  "tool": "Bash",
  "matches": { "cmd": "/^git (status|log|diff)$/" },
  "action": "allow"
}
```

This matches exactly `git status`, `git log`, or `git diff` but not `git commit`.

#### Value Type Matching[#](#permissions-value-type-matching)[#](#permissions-value-type-matching)

- **String patterns** only match string values using glob syntax
- **Literal values** (boolean, number, null, undefined) require exact matches
- **Array conditions** provide OR logic across multiple patterns
- **Nested objects** enable deep property matching with dot notation for objects and numeric strings for array indices

### Examples[#](#permissions-examples)[#](#permissions-examples)

#### Basic Permission Rules[#](#permissions-basic-rules)[#](#permissions-basic-rules)

Allow all Bash commands in main thread, but restrict sub-agents:

```
{
  "tool": "Bash",
  "action": "allow",
  "context": "thread"
},
{
  "tool": "Bash",
  "matches": { "cmd": ["rm -rf *", "find *", "git commit *"] },
  "action": "reject",
  "context": "subagent"
}
// In text form:
// allow --context thread Bash
// reject --context subagent Bash --cmd "rm -rf *" --cmd "find *" --cmd "git commit *"
```

Ask before grepping in the home directory:

```
{
  "tool": "Grep",
  "matches": { "path": "$HOME/*" },
  "action": "ask"
}
// In text form:
// ask Grep --path '$HOME/*'
```

Forbid editing dotfiles:

```
{
  "tool": "edit_file",
  "matches": { "path": ".*" },
  "action": "reject"
}
// In text form:
// reject edit_file --path '.*'
```

Reject destructive git commands with a helpful message (allows the model to continue):

```
{
  "tool": "Bash",
  "matches": { "cmd": ["*git checkout*", "*git reset*"] },
  "action": "reject",
  "message": "Do not use git checkout or git reset. Use edit_file to make manual changes instead."
}
```

#### Delegation[#](#permissions-delegation)[#](#permissions-delegation)

Delegate GitHub CLI calls to external validator:

```
{
  "tool": "Bash",
  "matches": { "cmd": "gh *" },
  "action": "delegate",
  "to": "my-gh-permission-helper"
}
// In text form:
// delegate --to my-gh-permission-helper Bash --cmd "gh *"
```

When instructed to delegate, Amp will:

- Execute the program named in `to` (must be on `$PATH`, or an absolute path)
- Export `AMP_THREAD_ID`, `AGENT_TOOL_NAME=nameOfInvokedTool` and `AGENT=amp` environment variables
- Pipe tool parameters to **stdin** as JSON
- Interpret exit status:
  
  - `0` → allow
  - `1` → ask operator
  - `≥ 2` → reject (stderr is surfaced to the model)

### Text Format[#](#permissions-text-format)[#](#permissions-text-format)

For editing many rules conveniently, you can use the text format with `amp permissions` commands:

```
<action> [--<action-arg> ...] <tool> [--<match-key>[:<op>] <value>] ...
```

The text format is designed to be compatible with UNIX shell syntax, allowing you to copy/paste rules from and to the command line without further editing.

```
# Basic allow/reject rules
allow Bash --cmd 'git *'
reject Bash --cmd 'python *'

# Multiple conditions
allow Bash --cmd 'git diff*' --cmd 'git commit*'

# Delegation
delegate --to amp-git-permissions Bash --cmd '*'
```

- Single- and double-quoted strings are supported
- unquoted true, false, null and numeric words are interpreted as JSON literals
- Any value containing `*` must be quoted

### Listing Rules[#](#permissions-listing-rules)[#](#permissions-listing-rules)

```
amp permissions list                    # Show user rules
amp permissions list --builtin          # Only built-in rules
```

### Testing Rules[#](#permissions-testing-rules)[#](#permissions-testing-rules)

For example, testing if it would ask on a git commit:

```
$ amp permissions test Bash --cmd "git commit -m 'test'"
tool: Bash
arguments: {"cmd":"git commit -m 'test'"}
action: ask
matched-rule: 12
source: builtin
```

or testing if it would ask to edit .env in the current directory

```
$ amp permissions test edit_file --path "$PWD/README.md"
tool: edit_file
arguments: {"path":"/Users/your/project/README.md"}
action: allow
matched-rule: 29
source: builtin
```

The test subcommand allows you to test permission rules without actually running any tools or hoping that the agent will generate the right parameters.

### Editing Rules[#](#permissions-editing-rules)[#](#permissions-editing-rules)

You can use `$EDITOR` to edit rules interactively in the text format:

```
$ amp permissions edit
```

And you can edit from STDIN:

```
$ amp permissions edit <<'EOF'
# Ask before every tool use
ask '*'
EOF
```

### Add Rules[#](#permissions-add-rules)[#](#permissions-add-rules)

For example, reject all mermaid diagrams:

```
$ amp permissions add reject mermaid
```

or ask before searching about node.js or npm packages:

```
$ amp permissions add ask web_search --query "*node*" --query "*npm*"
```

### Matching multiple tools with a single rule[#](#multiple-tools-single-rule)[#](#multiple-tools-single-rule)

Tool names support glob patterns for managing groups of tools:

- `Bash` - matches only the Bash tool
- `mcp__playwright__*` - matches all Playwright MCP tools

### Context Restrictions[#](#context-restrictions)[#](#context-restrictions)

Use the `context` field to restrict rules to the main agent or subagents

- `"context": "thread"` - only applies in main conversation thread
- `"context": "subagent"` - only applies to sub-agent tool calls
- Omit `context` - applies everywhere

Toolboxes let you create custom tools using any programming language. Tools are executable files that communicate with Amp via stdin/stdout using a simple protocol. See the [Toolboxes](https://ampcode.com/news/toolboxes) news article for an introduction.

### Overview[#](#toolboxes-overview)[#](#toolboxes-overview)

A toolbox is a directory containing executable files that become tools available to Amp. Each executable file in the directory represents a single tool.

Tools from toolboxes are registered with a `tb__` prefix (e.g., `run_tests` becomes `tb__run_tests`), and must implement the toolbox protocol (described below).

As long as the executables adhere to the protocol, they can be written in any language.

### Tool Discovery[#](#toolboxes-discovery)[#](#toolboxes-discovery)

Amp discovers tools by scanning directories specified in the `AMP_TOOLBOX` environment variable at startup, which works like the `PATH` variable: multiple directories separated by colons.

By default, if `AMP_TOOLBOX` is not set, Amp uses `~/.config/amp/tools` as the default toolbox directory.

When `AMP_TOOLBOX` is set to an empty string, or is not present in the environment, no toolbox directories are scanned.

Otherwise Amp scans the directories listed in `AMP_TOOLBOX` left-to-right, giving precedence to earlier directories for tools with conflicting names:

```
# Example: a run_tests tool in $PWD/.agents/tools will be used even if
# a tol with the same name exists in $HOME/.config/amp/tools
export AMP_TOOLBOX="$PWD/.agents/tools:$HOME/.config/amp/tools"
```

### Protocol Specification[#](#toolboxes-protocol)[#](#toolboxes-protocol)

Tools communicate with Amp through two actions: **describe** and **execute**. The action is determined by the `TOOLBOX_ACTION` environment variable.

The `describe` action is used to tell Amp about when and how to use the tool.

Once Amp decides to execute the tool, the executable is invoked again, but with `TOOLBOX_ACTION` set to `execute`.

**Communication:**

- Tools receive tool parameters via **stdin**, either as JSON or line-based key-value pairs.
- Tools write a message to the model to **stdout**.
- Exit code **0** indicates success, non-zero indicates error
- Stderr is used for error messages and diagnostics

**Environment variables passed to tools:**

VariableValueAvailable During`TOOLBOX_ACTION``"describe"` or `"execute"`Both actions`AGENT``"amp"`Both actions`CLAUDECODE``"1"`Both actions`AMP_THREAD_ID`Current thread IDExecute only`AGENT_THREAD_ID`Current thread IDExecute only`PATH`Inherited from environmentBoth actions

### Communication Formats[#](#toolboxes-formats)[#](#toolboxes-formats)

Tools can use either **JSON format** or **text format** for communicating the tool schema and input parameters. Amp auto-detects the format during the **describe** action:

1. First attempts to parse output as JSON
2. If JSON parsing fails, falls back to text format
3. The detected format is used for both describe and execute actions

Amp remembers the format that the tool advertised and will provide tool input parameters in the same format.

When `TOOLBOX_ACTION` is **execute** Amp takes any output from the tool and passes it directly to the model.

#### JSON Format[#](#toolboxes-json-format)[#](#toolboxes-json-format)

The JSON format is easy to work with in most programming languages and the recommended way to write toolbox tools when most of the tool logic is expressed in an existing programming language library.

For tools that mostly call out to shell commands, the text format is recommended.

**Describe Action:**

Output a JSON object with `name`, `description`, and either `args` (compact) or `inputSchema` (full):

*Compact args format for simple tools:*

```
{
  "name": "run_tests",
  "description": "Run the tests in the project using this tool instead of Bash",
  "args": {
    "workspace": ["string", "optional name of the workspace directory"],
    "test": ["string", "optional test name pattern to match"]
  }
}
```

For more structured parameters with deeply nested objects, use the full MCP `inputSchema`:

*Full inputSchema format (JSON Schema draft 2020-12):*

```
{
  "name": "run_tests",
  "description": "Run the tests in the project using this tool instead of Bash",
  "inputSchema": {
    "type": "object",
    "properties": {
      "workspace": {
        "type": "array",
		"items": {
			"type": "string"
		},
        "description": "list of names of the workspace directories"
      },
      "test": {
        "type": "string",
        "description": "optional test name pattern to match"
      }
    },
    "required": ["workspace"]
  }
}
```

**Execute Action:**

- **Input:** JSON object with tool arguments via stdin
- **Output:** Free-form text written to stdout
- **Exit code:** 0 for success, non-zero for error

#### Text Format[#](#toolboxes-text-format)[#](#toolboxes-text-format)

The text format is convenient for simple tool definitions that mostly need a handful of string parameters.

It is easy to emit and easy to parse in any programming language.

**Describe Action**:

Output a line-based tool description:

```
name: run_tests
description: Run the tests in the project using this tool instead of Bash.
workspace: string optional name of the workspace directory
test: string optional test name pattern
```

Multiple description lines are concatenated with newlines.

Parameter lines without a type prefix default to string type.

Empty lines are ignored.

**Optional Parameters:**

Parameters can be marked as optional in three ways:

1. **Type suffix with `?`** : `param: string? description`
2. **`(optional)` in description**: `param: string (optional) description`
3. **Description starts with `optional`** : `param: string optional description` or `param: optional description`

All three methods are case-insensitive. Parameters not marked as optional are required by default.

**Execute Action:**

- **Input:** Key-value pairs separated by newlines (e.g., `param1=value1\nparam2=value2\n`)
- **Output:** Any output written to stdout

### CLI Commands[#](#toolboxes-cli)[#](#toolboxes-cli)

The `amp tools` command allows you to work with tools directly from the command line.

To get a list of all tools known to Amp, run `amp tools list`:

```
Bash                              built-in  Executes the given shell command in the user's default shell
# ...
mcp__context7__get-library-docs   local-mcp Fetches up-to-date documentation for a library
mcp__context7__resolve-library-id local-mcp Resolves a package/product name to a Context7-compatible library ID and returns a list of matching libraries
tb__run_tests                     toolbox   Run tests using this tool instead of Bash
```

Tools provided by MCP servers have an `mcp__` prefix, tools coming from toolboxes get `tb__` as a prefix.

To create a new toolbox tool, use the `amp tools make` command:

```
$ amp tools make --bash run_tests
Tool created at: /Users/dhamidi/.config/amp/tools/run_tests

Inspect with: amp tools show tb__run_tests

Execute with: amp tools use tb__run_tests
```

By default a JavaScript tool using bun is created, the `--bash` and `--zsh` parameters scaffold the tool using the respective shell. This is useful when your tool is mostly just calling out other processes.

Using `amp tools show` you can see the schema of the generated tool:

```
amp tools show tb__run_tests
# tb__run_tests (toolbox: /Users/dhamidi/.config/amp/tools/run_tests)

Use this tool to get the current time.
Supported actions are:
date to retrieve the current time

# Schema

- action (string): the action to take
```

To invoke the tool as is, we’ll use `amp tools use`:

```
$ amp tools use tb__run_tests --action date
{
  "output": "Got action: date\nTue Oct 14 15:03:46 EEST 2025\n",
  "exitCode": 0
}
```

Amp collects the output of the toolbox executable and reports the collected output together with the exit status to the model.

After editing the scaffold to actually run Go tests for this example, it now looks like this:

```
#!/usr/bin/env bash

main() {
  case "${TOOLBOX_ACTION:-${1:-describe}}" in
  describe) print_tool_definition ;;
  execute) read_args_and_run ;;
  *)
    printf "Unknown action: %s\n" "$action" >&2
    exit 1
    ;;
  esac
}

print_tool_definition() {
  cat <<-'EOF'
		name: run_tests
		description: Run Go tests using this tool instead of Bash
		description: The pattern parameter limits the tests to a given pattern.

		pattern: string optional Only run tests matching this pattern
	EOF
}

read_args_and_run() {
  local pattern
  local input=$(</dev/stdin)
  while IFS=": " read name value; do
    if [ -n "$name" ]; then
      local $name="$value"
    fi
  done <<<"$input"

  go test ./... ${pattern:+-run "$pattern"}
}

main "$@"
```

We can verify that it works using `amp toosl use` again:

```
$ amp tools use --only output tb__run_tests
ok      github.com/dhamidi/proompt/cmd/proompt  (cached)
ok      github.com/dhamidi/proompt/pkg/config   (cached)
ok      github.com/dhamidi/proompt/pkg/copier   (cached)
ok      github.com/dhamidi/proompt/pkg/editor   (cached)
ok      github.com/dhamidi/proompt/pkg/filesystem       (cached)
ok      github.com/dhamidi/proompt/pkg/picker   (cached)
ok      github.com/dhamidi/proompt/pkg/prompt   (cached)
```

## Stream JSON Output[#](#stream-json-output)[#](#stream-json-output)

Amp’s CLI supports Claude Code compatible stream JSON output format for programmatic integration and real-time conversation monitoring.

### Usage[#](#usage)[#](#usage)

Use the `--stream-json` flag with `--execute` mode to output in stream JSON format instead of plain text: To include assistant thinking blocks, add `--stream-json-thinking` (this extends the schema and is not Claude Code compatible).

Basic usage with argument:

```
$ amp --execute "what is 3 + 5?" --stream-json
```

With stdin input:

```
$ echo "analyze this code" | amp --execute --stream-json
```

Streaming JSON input mode (see below for more information):

```
$ echo '{"type":"user","message":{"role":"user","content":[{"type":"text","text":"what is 2+2?"}]}}' | amp --execute --stream-json --stream-json-input
```

**Note:** The `--stream-json` flag requires `--execute` mode. It cannot be used standalone. `--stream-json-thinking` implies `--stream-json`.

Each conversation begins with an initial `init` system message, followed by a list of user and assistant messages, followed by a final `result` system message with stats. Each message is emitted as a separate JSON object.

### Message Schema[#](#message-schema)[#](#message-schema)

When `--stream-json-thinking` is enabled, assistant content may include `thinking` and `redacted_thinking` blocks.

Messages returned from the stream JSON API are strictly typed according to the following schema:

```
type StreamJSONMessage =
  // An assistant message
  | {
      type: "assistant";
      message: {
        type: "message";
        role: "assistant";
        content: Array<{
          type: "text";
          text: string;
        } | {
          type: "tool_use";
          id: string;
          name: string;
          input: Record<string, unknown>;
        } | {
          type: "thinking";
          thinking: string;
        } | {
          type: "redacted_thinking";
          data: string;
        }>;
        stop_reason: "end_turn" | "tool_use" | "max_tokens" | null;
        usage?: {
          input_tokens: number;
		  max_tokens: number;
          cache_creation_input_tokens?: number;
          cache_read_input_tokens?: number;
          output_tokens: number;
          service_tier?: string;
        };
      };
      parent_tool_use_id: string | null;
      session_id: string;
    }

  // A user message (tool results)
  | {
      type: "user";
      message: {
        role: "user";
        content: Array<{
          type: "tool_result";
          tool_use_id: string;
          content: string;
          is_error: boolean;
        }>;
      };
      parent_tool_use_id: string | null;
      session_id: string;
    }

  // Emitted as the last message on success
  | {
      type: "result";
      subtype: "success";
      duration_ms: number;
      is_error: false;
      num_turns: number;
      result: string;
      session_id: string;
      usage?: {
        input_tokens: number;
		max_tokens: number;
        cache_creation_input_tokens?: number;
        cache_read_input_tokens?: number;
        output_tokens: number;
        service_tier?: string;
      };
      permission_denials?: string[];
    }

  // Emitted as the last message on error
  | {
      type: "result";
      subtype: "error_during_execution" | "error_max_turns";
      duration_ms: number;
      is_error: true;
      num_turns: number;
      error: string;
      session_id: string;
      usage?: {
        input_tokens: number;
		max_tokens: number;
        cache_creation_input_tokens?: number;
        cache_read_input_tokens?: number;
        output_tokens: number;
        service_tier?: string;
      };
      permission_denials?: string[];
    }

  // Emitted as the first message at the start of a conversation
  | {
      type: "system";
      subtype: "init";
      cwd: string;
      session_id: string;
      tools: string[];
      mcp_servers: { name: string; status: "connected" | "connecting" | "connection-failed" | "disabled" }[];
    };
```

### Example Output[#](#example-output)[#](#example-output)

Simple math query:

```
$ amp --execute "what is 3 + 5?" --stream-json
{"type":"system","subtype":"init","cwd":"/Users/orb","session_id":"T-f9941a55-3765-421e-972f-05dc1138c3a3","tools":["Bash","finder","create_file","edit_file","glob","Grep","mcp__postgres__query","mermaid","oracle","Read","read_mcp_resource","read_web_page","Task","todo_read","todo_write","undo_edit","web_search"],"mcp_servers":[{"name":"postgres","status":"connected"}]}
{"type":"user","message":{"role":"user","content":[{"type":"text","text":"what is 3 + 5?"}]},"parent_tool_use_id":null,"session_id":"T-f9941a55-3765-421e-972f-05dc1138c3a3"}
{"type":"assistant","message":{"type":"message","role":"assistant","content":[{"type":"text","text":"8"}],"stop_reason":"end_turn","usage":{"input_tokens":10,"cache_creation_input_tokens":16256,"cache_read_input_tokens":0,"output_tokens":99,"max_tokens":968000,"service_tier":"standard"}},"parent_tool_use_id":null,"session_id":"T-f9941a55-3765-421e-972f-05dc1138c3a3"}
{"type":"result","subtype":"success","duration_ms":5400,"is_error":false,"num_turns":1,"result":"8","session_id":"T-f9941a55-3765-421e-972f-05dc1138c3a3"}
```

Tool usage example:

```
$ amp --execute "list files using a tool" --stream-json
{"type":"system","subtype":"init","cwd":"/Users/orb/project","session_id":"T-d2fc4acc-dd1d-497f-9609-ed0da22a7c95","tools":["Bash","finder" ,"create_file","edit_file","glob","Grep","mcp__postgres__query","mermaid","oracle","Read","read_mcp_resource","read_web_page","Task","todo_rea d","todo_write","undo_edit","web_search"],"mcp_servers":[{"name":"postgres","status":"connected"}]}
{"type":"user","message":{"role":"user","content":[{"type":"text","text":"list files using a tool"}]},"parent_tool_use_id":null,"session_id":"T-d2fc4acc-dd1d-4 97f-9609-ed0da22a7c95"}
{"type":"assistant","message":{"type":"message","role":"assistant","content":[{"type":"tool_use","id":"toolu_019cyniPYrSgaJitUSMyxyNV","name": "read", "input":{"path":"/Users/orb/project"}}],"stop_reason":"tool_use","usage":{"input_tokens":10,"cache_creation_input_tokens":13150,"cache_read_input_tokens": 0,"output_tokens":111,"max_tokens":968000,"service_tier":"standard"}},"parent_tool_use_id":null,"session_id":"T-d2fc4acc-dd1d-497f-9609-ed0da22a7c95"}
{"type":"user","message":{"role":"user","content":[{"type":"tool_result","tool_use_id":"toolu_019cyniPYrSgaJitUSMyxyNV","content":"[\"index.js\",\"README.md\"] ","is_error":false}]},"parent_tool_use_id":null,"session_id":"T-d2fc4acc-dd1d-497f-9609-ed0da22a7c95"}
{"type":"assistant","message":{"type":"message","role":"assistant","content":[{"type":"text","text":"Two files: index.js and README.md"}],"stop_reason":"end_tu rn","usage":{"input_tokens":7,"cache_creation_input_tokens":133,"cache_read_input_tokens":13150,"output_tokens":13,"max_tokens":968000,"service_tier":"standard "}},"parent_tool_use_id":null,"session_id":"T-d2fc4acc-dd1d-497f-9609-ed0da22a7c95"}
{"type":"result","subtype":"success","duration_ms":7363,"is_error":false,"num_turns":2,"result":"Two files: index.js and README.md","session_id":"T-d2fc4acc-dd1d-497f-9609-ed0da22a7c95"}
```

### Streaming JSON Input (`--stream-json-input`)[#](#streaming-json-input-stream-json-input)[#](#streaming-json-input-stream-json-input)

The `--stream-json-input` flag enables **streaming input** where Amp reads messages from stdin until it’s closed.

Each message should be a valid JSON object on a single line:

```
{"type": "user", "message": { "role": "user", "content": [{ "type": "text", "text": "Your message here"}]}}
```

When using `--stream-json-input`, the behavior of `--execute` changes in that Amp will only exit once both the assistant is done *and* stdin has been closed.

This allows for programmatic use of the Amp CLI to have conversations with multiple user messages.

Example:

```
#!/bin/bash

send_message() {
  local text="$1"
  echo '{"type":"user","message":{"role":"user","content":[{"type":"text","text":"'$text'"}]}}'
}

{
  send_message "what's 2+2?"
  sleep 10

  send_message "now add 8 to that"
  sleep 10

  send_message "now add 5 to that"
} | amp --execute --stream-json --stream-json-input
```

This script produces the following output:

```
$ ./script.sh
{"type":"system","subtype":"init","cwd":"/Users/orb","session_id":"T-addfb7a4-61d9-41e1-890b-7330aa54087a","tools":["Bash","finder","create_file","edit_file","glob","Grep","mcp__postgres__query","mermaid","oracle","Read","read_mcp_resource","read_web_page","Task","todo_read","todo_write","undo_edit","web_search"],"mcp_servers":[{"name":"postgres","status":"connected"}]}
{"type":"user","message":{"role":"user","content":[{"type":"text","text":"what's 2+2?"}]},"parent_tool_use_id":null,"session_id":"T-addfb7a4-61d9-41e1-890b-7330aa54087a"}
{"type":"assistant","message":{"type":"message","role":"assistant","content":[{"type":"text","text":"4"}],"stop_reason":"end_turn","usage":{"input_tokens":10,"cache_creation_input_tokens":13993,"cache_read_input_tokens":0,"output_tokens":67,"max_tokens":968000,"service_tier":"standard"}},"parent_tool_use_id":null,"session_id":"T-addfb7a4-61d9-41e1-890b-7330aa54087a"}
{"type":"user","message":{"role":"user","content":[{"type":"text","text":"now add 8 to that"}]},"parent_tool_use_id":null,"session_id":"T-addfb7a4-61d9-41e1-890b-7330aa54087a"}
{"type":"assistant","message":{"type":"message","role":"assistant","content":[{"type":"text","text":"12"}],"stop_reason":"end_turn","usage":{"input_tokens":10,"cache_creation_input_tokens":36,"cache_read_input_tokens":13993,"output_tokens":76,"max_tokens":968000,"service_tier":"standard"}},"parent_tool_use_id":null,"session_id":"T-addfb7a4-61d9-41e1-890b-7330aa54087a"}
{"type":"user","message":{"role":"user","content":[{"type":"text","text":"now add 5 to that"}]},"parent_tool_use_id":null,"session_id":"T-addfb7a4-61d9-41e1-890b-7330aa54087a"}
{"type":"assistant","message":{"type":"message","role":"assistant","content":[{"type":"text","text":"17"}],"stop_reason":"end_turn","usage":{"input_tokens":10,"cache_creation_input_tokens":36,"cache_read_input_tokens":14029,"output_tokens":43,"max_tokens":968000,"service_tier":"standard"}},"parent_tool_use_id":null,"session_id":"T-addfb7a4-61d9-41e1-890b-7330aa54087a"}
{"type":"result","subtype":"success","duration_ms":21639,"is_error":false,"num_turns":3,"result":"17","session_id":"T-addfb7a4-61d9-41e1-890b-7330aa54087a"}
```

### Subagent Support[#](#subagent-support)[#](#subagent-support)

Stream JSON mode fully supports subagents created by the Task tool:

- **Subagent messages** have their `parent_tool_use_id` field set to the Task tool’s ID
- **Main agent messages** have `parent_tool_use_id` set to `null`
- **Completion logic** waits for all subagents to finish before emitting the final result

Example with subagents:

```
$ amp --execute "use Task tool to calculate 4+7" --stream-json
{"type":"system","subtype":"init",...}
{"type":"assistant","message":{"content":[{"type":"tool_use","id":"toolu_123","name":"Task",...}]},"parent_tool_use_id":null,...}
{"type":"assistant","message":{"content":[{"type":"text","text":"11"}]},"parent_tool_use_id":"toolu_123",...}
{"type":"user","message":{"content":[{"type":"tool_result","tool_use_id":"toolu_123",...}]},"parent_tool_use_id":null,...}
{"type":"result","subtype":"success",...}
```

### Claude Code Compatibility[#](#claude-code-compatibility)[#](#claude-code-compatibility)

Amp’s stream JSON output tries to be compatible with Claude Code’s format as much as possible. When `--stream-json-thinking` is enabled, the output includes extra content block types that are not part of Claude Code’s public schema.

## Workspace Thread Visibility Controls[#](#workspace-thread-visibility-controls)[#](#workspace-thread-visibility-controls)

By default, threads created by workspace members are [shared with the workspace](https://ampcode.com/manual#sharing).

[Enterprise](https://ampcode.com/manual#enterprise) workspaces can configure additional options for thread visibility in the [workspace settings](https://ampcode.com/workspace) page. The currently supported options include:

- Disabling public (unlisted or discoverable) threads
- Disabling private threads
- Private-by-default threads

Upon request, Enterprise workspaces can also enable user groups and per-group thread visibility.

Learn more thread visibility in [Privacy & Permissions](https://ampcode.com/manual#privacy-and-permissions).

## Workspace Entitlements[#](#workspace-entitlements)[#](#workspace-entitlements)

[Amp Enterprise Premium](https://ampcode.com/manual#enterprise) workspaces can set per-user usage quotas through entitlements, such as:

- A default of $50/week for regular users and $200/week for senior engineers
- A team-wide limit of $100/day that applies to everyone
- Different limits for contractors vs. full-time employees

To get started, head over to the [workspace settings](https://ampcode.com/workspace) page and navigate to the “Entitlements” section.