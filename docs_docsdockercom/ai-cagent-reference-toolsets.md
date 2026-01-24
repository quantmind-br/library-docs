---
title: Toolsets
url: https://docs.docker.com/ai/cagent/reference/toolsets/
source: llms
fetched_at: 2026-01-24T14:13:44.784171611-03:00
rendered_js: false
word_count: 1263
summary: This reference documents the toolsets available in cagent and explains how agents use them to perform actions like file manipulation and command execution. It provides detailed descriptions and configuration options for built-in, MCP, and custom tool types.
tags:
    - cagent
    - toolsets
    - agent-capabilities
    - mcp-tools
    - configuration
    - filesystem-access
    - shell-commands
category: reference
---

## Toolsets reference

This reference documents the toolsets available in cagent and what each one does. Tools give agents the ability to take action—interacting with files, executing commands, accessing external resources, and managing state.

For configuration file syntax and how to set up toolsets in your agent YAML, see the [Configuration file reference](https://docs.docker.com/ai/cagent/reference/config/).

When you configure toolsets for an agent, those tools become available in the agent's context. The agent can invoke tools by name with appropriate parameters based on the task at hand.

Tool invocation flow:

1. Agent analyzes the task and determines which tool to use
2. Agent constructs tool parameters based on requirements
3. cagent executes the tool and returns results
4. Agent processes results and decides next steps

Agents can call multiple tools in sequence or make decisions based on tool results. Tool selection is automatic based on the agent's understanding of the task and available capabilities.

cagent supports three types of toolsets:

Built-in toolsets

Core functionality built directly into cagent (`filesystem`, `shell`, `memory`, etc.). These provide essential capabilities for file operations, command execution, and state management. MCP toolsets

Tools provided by Model Context Protocol servers, either local processes (stdio) or remote servers (HTTP/SSE). MCP enables access to a wide ecosystem of standardized tools. Custom toolsets

Shell scripts wrapped as tools with typed parameters (`script_shell`). This lets you define domain-specific tools for your use case.

Toolsets are configured in your agent's YAML file under the `toolsets` array:

### [Common configuration options](#common-configuration-options)

All toolset types support these optional properties:

PropertyTypeDescription`instruction`stringAdditional instructions for using the toolset`tools`arraySpecific tool names to enable (defaults to all)`env`objectEnvironment variables for the toolset`toon`stringComma-delimited regex patterns matching tool names whose JSON outputs should be compressed. Reduces token usage by simplifying/compressing JSON responses from matched tools using automatic encoding. Example: `"search.*,list.*"``defer`boolean or arrayControl which tools load into initial context. Set to `true` to defer all tools, or array of tool names to defer specific tools. Deferred tools don't consume context until explicitly loaded via `search_tool`/`add_tool`.

### [Tool selection](#tool-selection)

By default, agents have access to all tools from their configured toolsets. You can restrict this using the `tools` option:

This is useful for:

- Limiting agent capabilities for security
- Reducing context size for smaller models
- Creating specialized agents with focused tool access

### [Deferred loading](#deferred-loading)

Deferred loading keeps tools out of the initial context window, loading them only when explicitly requested. This is useful for large toolsets where most tools won't be used, significantly reducing context consumption.

Defer all tools in a toolset:

Or defer specific tools while loading others immediately:

Agents can discover deferred tools via `search_tool` and load them into context via `add_tool` when needed. Best for toolsets with dozens of tools where only a few are typically used.

### [Output compression](#output-compression)

The `toon` property compresses JSON outputs from matched tools to reduce token usage. When a tool's output is JSON, it's automatically compressed using efficient encoding before being returned to the agent:

Useful for tools that return large JSON responses (API results, file listings, search results). The compression is transparent to the agent but can significantly reduce context consumption for verbose tool outputs.

### [Per-agent tool configuration](#per-agent-tool-configuration)

Different agents can have different toolsets:

This allows specialized agents with focused capabilities, security boundaries, and optimized performance.

### [Filesystem](#filesystem)

The `filesystem` toolset gives your agent the ability to work with files and directories. Your agent can read files to understand context, write new files, make targeted edits to existing files, search for content, and explore directory structures. Essential for code analysis, documentation updates, configuration management, and any agent that needs to understand or modify project files.

Access is restricted to the current working directory by default. Agents can request access to additional directories at runtime, which requires your approval.

#### [Configuration](#configuration-1)

### [Shell](#shell)

The `shell` toolset lets your agent execute commands in your system's shell environment. Use this for agents that need to run builds, execute tests, manage processes, interact with CLI tools, or perform system operations. The agent can run commands in the foreground or background.

Commands execute in the current working directory and inherit environment variables from the cagent process. This toolset is powerful but should be used with appropriate security considerations.

#### [Configuration](#configuration-2)

### [Think](#think)

The `think` toolset provides your agent with a reasoning scratchpad. The agent can record thoughts and reasoning steps without taking actions or modifying data. Particularly useful for complex tasks where the agent needs to plan multiple steps, verify requirements, or maintain context across a long conversation.

Agents use this to break down problems, list applicable rules, verify they have all needed information, and document their reasoning process before acting.

#### [Configuration](#configuration-3)

### [Todo](#todo)

The `todo` toolset gives your agent task-tracking capabilities for managing multi-step operations. Your agent can break down complex work into discrete tasks, track progress through each step, and ensure nothing is missed before completing a request. Especially valuable for agents handling complex workflows with multiple dependencies.

The `shared` option allows todos to persist across different agents in a multi-agent system, enabling coordination.

#### [Configuration](#configuration-4)

### [Memory](#memory)

The `memory` toolset allows your agent to store and retrieve information across conversations and sessions. Your agent can remember user preferences, project context, previous decisions, and other information that should persist. Useful for agents that interact with users over time or need to maintain state about a project or environment.

Memories are stored in a local database file and persist across cagent sessions.

#### [Configuration](#configuration-5)

### [Fetch](#fetch)

The `fetch` toolset enables your agent to retrieve content from HTTP/HTTPS URLs. Your agent can fetch documentation, API responses, web pages, or any content accessible via HTTP GET requests. Useful for agents that need to access external resources, check API documentation, or retrieve web content.

The agent can specify custom HTTP headers when needed for authentication or other purposes.

#### [Configuration](#configuration-6)

### [API](#api)

The `api` toolset lets you define custom tools that call HTTP APIs. Similar to `script_shell` but for web services, this allows you to expose REST APIs, webhooks, or any HTTP endpoint as a tool your agent can use. The agent sees these as typed tools with automatic parameter validation.

Use this to integrate with external services, call internal APIs, trigger webhooks, or interact with any HTTP-based system.

#### [Configuration](#configuration-7)

Each API tool is defined with an `api_config` containing the endpoint, HTTP method, and optional typed parameters:

For GET requests, parameters are interpolated into the endpoint URL. For POST requests, parameters are sent as JSON in the request body.

Supported argument types: `string`, `number`, `boolean`, `array`, `object`.

### [Script Shell](#script-shell)

The `script_shell` toolset lets you define custom tools by wrapping shell commands with typed parameters. This allows you to expose domain-specific operations to your agent as first-class tools. The agent sees these custom tools just like built-in tools, with parameter validation and type checking handled automatically.

Use this to create tools for deployment scripts, build commands, test runners, or any operation specific to your project or workflow.

#### [Configuration](#configuration-8)

Each custom tool is defined with a command, description, and optional typed parameters:

Supported argument types: `string`, `number`, `boolean`, `array`, `object`.

#### [Tools](#tools)

The tools you define become available to your agent. In the previous example, the agent would have access to `deploy` and `run_tests` tools.

Some tools are automatically added to agents based on their configuration. You don't configure these explicitly—they appear when needed.

### [transfer\_task](#transfer_task)

Automatically available when your agent has `sub_agents` configured. Allows the agent to delegate tasks to sub-agents and receive results back.

### [handoff](#handoff)

Automatically available when your agent has `handoffs` configured. Allows the agent to transfer the entire conversation to a different agent.

- Read the [Configuration file reference](https://docs.docker.com/ai/cagent/reference/config/) for YAML file structure
- Review the [CLI reference](https://docs.docker.com/ai/cagent/reference/cli/) for running agents
- Explore [MCP servers](https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/) for extended capabilities
- Browse [example configurations](https://github.com/docker/cagent/tree/main/examples)