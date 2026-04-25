---
title: Plugins | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins
source: crawler
fetched_at: 2026-04-24T17:00:09.855979848-03:00
rendered_js: false
word_count: 827
summary: This document serves as a comprehensive guide detailing Hermes' plugin system, explaining how users can extend the agent's functionality by adding custom tools, hooks, and commands without modifying core code.
tags:
    - hermes-plugin
    - agent-extension
    - tool-integration
    - lifecycle-hooks
    - configuration
    - plugin-management
category: guide
---

Hermes has a plugin system for adding custom tools, hooks, and integrations without modifying core code.

**→ [Build a Hermes Plugin](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin)** — step-by-step guide with a complete working example.

## Quick overview[​](#quick-overview "Direct link to Quick overview")

Drop a directory into `~/.hermes/plugins/` with a `plugin.yaml` and Python code:

```text
~/.hermes/plugins/my-plugin/
├── plugin.yaml      # manifest
├── __init__.py      # register() — wires schemas to handlers
├── schemas.py       # tool schemas (what the LLM sees)
└── tools.py         # tool handlers (what runs when called)
```

Start Hermes — your tools appear alongside built-in tools. The model can call them immediately.

### Minimal working example[​](#minimal-working-example "Direct link to Minimal working example")

Here is a complete plugin that adds a `hello_world` tool and logs every tool call via a hook.

**`~/.hermes/plugins/hello-world/plugin.yaml`**

```yaml
name: hello-world
version:"1.0"
description: A minimal example plugin
```

**`~/.hermes/plugins/hello-world/__init__.py`**

```python
"""Minimal Hermes plugin — registers a tool and a hook."""


defregister(ctx):
# --- Tool: hello_world ---
    schema ={
"name":"hello_world",
"description":"Returns a friendly greeting for the given name.",
"parameters":{
"type":"object",
"properties":{
"name":{
"type":"string",
"description":"Name to greet",
}
},
"required":["name"],
},
}

defhandle_hello(params):
        name = params.get("name","World")
returnf"Hello, {name}! 👋  (from the hello-world plugin)"

    ctx.register_tool("hello_world", schema, handle_hello)

# --- Hook: log every tool call ---
defon_tool_call(tool_name, params, result):
print(f"[hello-world] tool called: {tool_name}")

    ctx.register_hook("post_tool_call", on_tool_call)
```

Drop both files into `~/.hermes/plugins/hello-world/`, restart Hermes, and the model can immediately call `hello_world`. The hook prints a log line after every tool invocation.

Project-local plugins under `./.hermes/plugins/` are disabled by default. Enable them only for trusted repositories by setting `HERMES_ENABLE_PROJECT_PLUGINS=true` before starting Hermes.

## What plugins can do[​](#what-plugins-can-do "Direct link to What plugins can do")

CapabilityHowAdd tools`ctx.register_tool(name, schema, handler)`Add hooks`ctx.register_hook("post_tool_call", callback)`Add slash commands`ctx.register_command(name, handler, description)` — adds `/name` in CLI and gateway sessionsAdd CLI commands`ctx.register_cli_command(name, help, setup_fn, handler_fn)` — adds `hermes <plugin> <subcommand>`Inject messages`ctx.inject_message(content, role="user")` — see [Injecting Messages](#injecting-messages)Ship data files`Path(__file__).parent / "data" / "file.yaml"`Bundle skills`ctx.register_skill(name, path)` — namespaced as `plugin:skill`, loaded via `skill_view("plugin:skill")`Gate on env vars`requires_env: [API_KEY]` in plugin.yaml — prompted during `hermes plugins install`Distribute via pip`[project.entry-points."hermes_agent.plugins"]`

## Plugin discovery[​](#plugin-discovery "Direct link to Plugin discovery")

SourcePathUse caseBundled`<repo>/plugins/`Ships with Hermes — see [Built-in Plugins](https://hermes-agent.nousresearch.com/docs/user-guide/features/built-in-plugins)User`~/.hermes/plugins/`Personal pluginsProject`.hermes/plugins/`Project-specific plugins (requires `HERMES_ENABLE_PROJECT_PLUGINS=true`)pip`hermes_agent.plugins` entry\_pointsDistributed packages

Later sources override earlier ones on name collision, so a user plugin with the same name as a bundled plugin replaces it.

## Plugins are opt-in[​](#plugins-are-opt-in "Direct link to Plugins are opt-in")

**Every plugin — user-installed, bundled, or pip — is disabled by default.** Discovery finds them (so they show up in `hermes plugins` and `/plugins`), but nothing loads until you add the plugin's name to `plugins.enabled` in `~/.hermes/config.yaml`. This stops anything with hooks or tools from running without your explicit consent.

```yaml
plugins:
enabled:
- my-tool-plugin
- disk-cleanup
disabled:# optional deny-list — always wins if a name appears in both
- noisy-plugin
```

Three ways to flip state:

```bash
hermes plugins                    # interactive toggle (space to check/uncheck)
hermes plugins enable<name># add to allow-list
hermes plugins disable <name># remove from allow-list + add to disabled
```

After `hermes plugins install owner/repo`, you're asked `Enable 'name' now? [y/N]` — defaults to no. Skip the prompt for scripted installs with `--enable` or `--no-enable`.

### Migration for existing users[​](#migration-for-existing-users "Direct link to Migration for existing users")

When you upgrade to a version of Hermes that has opt-in plugins (config schema v21+), any user plugins already installed under `~/.hermes/plugins/` that weren't already in `plugins.disabled` are **automatically grandfathered** into `plugins.enabled`. Your existing setup keeps working. Bundled plugins are NOT grandfathered — even existing users have to opt in explicitly.

## Available hooks[​](#available-hooks "Direct link to Available hooks")

Plugins can register callbacks for these lifecycle events. See the [**Event Hooks page**](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#plugin-hooks) for full details, callback signatures, and examples.

HookFires when[`pre_tool_call`](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#pre_tool_call)Before any tool executes[`post_tool_call`](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#post_tool_call)After any tool returns[`pre_llm_call`](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#pre_llm_call)Once per turn, before the LLM loop — can return `{"context": "..."}` to [inject context into the user message](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#pre_llm_call)[`post_llm_call`](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#post_llm_call)Once per turn, after the LLM loop (successful turns only)[`on_session_start`](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#on_session_start)New session created (first turn only)[`on_session_end`](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#on_session_end)End of every `run_conversation` call + CLI exit handler[`pre_gateway_dispatch`](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#pre_gateway_dispatch)Gateway received a user message, before auth + dispatch. Return `{"action": "skip" | "rewrite" | "allow", ...}` to influence flow.

## Plugin types[​](#plugin-types "Direct link to Plugin types")

Hermes has three kinds of plugins:

TypeWhat it doesSelectionLocation**General plugins**Add tools, hooks, slash commands, CLI commandsMulti-select (enable/disable)`~/.hermes/plugins/`**Memory providers**Replace or augment built-in memorySingle-select (one active)`plugins/memory/`**Context engines**Replace the built-in context compressorSingle-select (one active)`plugins/context_engine/`

Memory providers and context engines are **provider plugins** — only one of each type can be active at a time. General plugins can be enabled in any combination.

## Managing plugins[​](#managing-plugins "Direct link to Managing plugins")

```bash
hermes plugins                               # unified interactive UI
hermes plugins list                          # table: enabled / disabled / not enabled
hermes plugins install user/repo             # install from Git, then prompt Enable? [y/N]
hermes plugins install user/repo --enable# install AND enable (no prompt)
hermes plugins install user/repo --no-enable # install but leave disabled (no prompt)
hermes plugins update my-plugin              # pull latest
hermes plugins remove my-plugin              # uninstall
hermes plugins enable my-plugin              # add to allow-list
hermes plugins disable my-plugin             # remove from allow-list + add to disabled
```

### Interactive UI[​](#interactive-ui "Direct link to Interactive UI")

Running `hermes plugins` with no arguments opens a composite interactive screen:

```text
Plugins
  ↑↓ navigate  SPACE toggle  ENTER configure/confirm  ESC done

  General Plugins
 → [✓] my-tool-plugin — Custom search tool
   [ ] webhook-notifier — Event hooks
   [ ] disk-cleanup — Auto-cleanup of ephemeral files [bundled]

  Provider Plugins
     Memory Provider          ▸ honcho
     Context Engine           ▸ compressor
```

- **General Plugins section** — checkboxes, toggle with SPACE. Checked = in `plugins.enabled`, unchecked = in `plugins.disabled` (explicit off).
- **Provider Plugins section** — shows current selection. Press ENTER to drill into a radio picker where you choose one active provider.
- Bundled plugins appear in the same list with a `[bundled]` tag.

Provider plugin selections are saved to `config.yaml`:

```yaml
memory:
provider:"honcho"# empty string = built-in only

context:
engine:"compressor"# default built-in compressor
```

### Enabled vs. disabled vs. neither[​](#enabled-vs-disabled-vs-neither "Direct link to Enabled vs. disabled vs. neither")

Plugins occupy one of three states:

StateMeaningIn `plugins.enabled`?In `plugins.disabled`?`enabled`Loaded on next sessionYesNo`disabled`Explicitly off — won't load even if also in `enabled`(irrelevant)Yes`not enabled`Discovered but never opted inNoNo

The default for a newly-installed or bundled plugin is `not enabled`. `hermes plugins list` shows all three distinct states so you can tell what's been explicitly turned off vs. what's just waiting to be enabled.

In a running session, `/plugins` shows which plugins are currently loaded.

## Injecting Messages[​](#injecting-messages "Direct link to Injecting Messages")

Plugins can inject messages into the active conversation using `ctx.inject_message()`:

```python
ctx.inject_message("New data arrived from the webhook", role="user")
```

**Signature:** `ctx.inject_message(content: str, role: str = "user") -> bool`

How it works:

- If the agent is **idle** (waiting for user input), the message is queued as the next input and starts a new turn.
- If the agent is **mid-turn** (actively running), the message interrupts the current operation — the same as a user typing a new message and pressing Enter.
- For non-`"user"` roles, the content is prefixed with `[role]` (e.g. `[system] ...`).
- Returns `True` if the message was queued successfully, `False` if no CLI reference is available (e.g. in gateway mode).

This enables plugins like remote control viewers, messaging bridges, or webhook receivers to feed messages into the conversation from external sources.

note

`inject_message` is only available in CLI mode. In gateway mode, there is no CLI reference and the method returns `False`.

See the [**full guide**](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin) for handler contracts, schema format, hook behavior, error handling, and common mistakes.