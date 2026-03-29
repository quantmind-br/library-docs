---
title: goose Logging System | goose
url: https://block.github.io/goose/docs/guides/logs
source: github_pages
fetched_at: 2026-01-22T22:13:59.879655926-03:00
rendered_js: true
word_count: 647
summary: This document outlines the local storage architecture for goose, detailing where session records, command history, and system logs are stored across different operating systems.
tags:
    - storage-locations
    - session-management
    - log-files
    - data-privacy
    - cross-platform
category: reference
---

goose uses a unified storage system for conversations and interactions. All conversations and interactions (both CLI and Desktop) are stored **locally** in the following locations:

**Type****Unix-like (macOS, Linux)****Windows****Command History**`~/.config/goose/history.txt``%APPDATA%\Block\goose\data\history.txt`**Session Records**`~/.local/share/goose/sessions/sessions.db``%APPDATA%\Block\goose\data\sessions\sessions.db`**System Logs**`~/.local/state/goose/logs/``%APPDATA%\Block\goose\data\logs\`

Privacy

goose is a local application and all goose log files are stored locally. These logs are never sent to external servers or third parties, ensuring that all goose data remains private and under your control. Note that the LLMs and tools goose uses on your behalf may have their own logs and privacy considerations.

## Command History[​](#command-history "Direct link to Command History")

goose stores command history persistently across chat sessions, allowing goose to recall previous commands.

Command history logs are stored in:

- Unix-like: `~/.config/goose/history.txt`
- Windows: `%APPDATA%\Block\goose\data\history.txt`

## Session Records[​](#session-records "Direct link to Session Records")

goose maintains session records that track the conversation history and interactions for each session. Sessions are stored in an SQLite database at:

- **Unix-like**: `~/.local/share/goose/sessions/sessions.db`
- **Windows**: `%APPDATA%\Block\goose\data\sessions\sessions.db`

Session Storage Migration

Prior to version 1.10.0, goose stored session records in individual `.jsonl` files under `~/.local/share/goose/sessions/`. When you upgrade to v1.10.0 or later, your existing sessions are automatically imported into the database. Legacy `.jsonl` files remain on disk but are no longer managed by goose.

This database contains all saved session data including:

- Session metadata (ID, name, working directory, timestamps)
- Conversation messages (user commands, assistant responses, role information)
- Tool calls and results (IDs, arguments, responses, success/failure status)
- Token usage statistics
- Extension data and configuration

Session IDs are named using `YYYYMMDD_<COUNT>` format, for example: `20250310_2`. goose CLI outputs the session ID at the start of each session. To get session IDs, use [`goose session list` command](https://block.github.io/goose/docs/guides/goose-cli-commands#session-list-options) to see all available sessions.

Also see [Session Management](https://block.github.io/goose/docs/guides/sessions/session-management) for details about searching sessions.

## System Logs[​](#system-logs "Direct link to System Logs")

goose stores logs for its various components. CLI and server logs are automatically organized into date-based directories and cleaned up after two weeks to prevent excessive disk usage.

When [prompt injection detection](https://block.github.io/goose/docs/guides/security/prompt-injection-detection) is enabled, CLI and server logs also include:

- Security findings with unique IDs (format: `SEC-{uuid}`)
- User decisions (allow/deny) associated with finding IDs

info

Extensions may optionally log to subdirectories under `~/.local/state/goose/logs/`. The specific subdirectory structure is determined by each extension's implementation.

### Desktop Application Log[​](#desktop-application-log "Direct link to Desktop Application Log")

The desktop application maintains its own logs:

- macOS: `~/Library/Application Support/Goose/logs/main.log`
- Windows: `%APPDATA%\Block\goose\logs\main.log`

The desktop application follows platform conventions for its own operational logs and state data, but uses the standard goose [session records](#session-records) for actual conversations and interactions. This means your conversation history is consistent regardless of which interface you use to interact with goose.

### CLI Logs[​](#cli-logs "Direct link to CLI Logs")

CLI logs are stored in:

- Unix-like: `~/.local/state/goose/logs/cli/`
- Windows: `%APPDATA%\Block\goose\data\logs\cli\`

Logs are organized into date-based subdirectories (e.g., `cli/2025-11-13/`) and subdirectories older than two weeks are automatically deleted.

CLI session logs contain:

- Tool invocations and responses
- Command execution details
- Session identifiers
- Timestamps

CLI logs also capture extension-related activity, including:

- Tool initialization
- Tool capabilities and schemas
- Extension-specific operations
- Command execution results
- Error messages and debugging information
- Extension configuration states
- Extension-specific protocol information

### Server Logs[​](#server-logs "Direct link to Server Logs")

Server logs are stored in:

- Unix-like: `~/.local/state/goose/logs/server/`
- Windows: `%APPDATA%\Block\goose\data\logs\server\`

Logs are organized into date-based subdirectories (e.g., `server/2025-11-13/`) and subdirectories older than two weeks are automatically deleted.

The Server logs contain information about the goose daemon (`goosed`), which is a local server process that runs on your computer. This server component manages communication between the CLI, extensions, and LLMs.

Server logs include:

- Server initialization details
- JSON-RPC communication logs
- Server capabilities
- Protocol version information
- Client-server interactions
- Extension loading and initialization
- Tool definitions and schemas
- Extension instructions and capabilities
- Debug-level transport information
- System capabilities and configurations
- Operating system information
- Working directory information
- Transport layer communication details
- Message parsing and handling information
- Request/response cycles
- Error states and handling
- Extension initialization sequences

### LLM Request Logs[​](#llm-request-logs "Direct link to LLM Request Logs")

LLM request logs capture the raw request and response data sent to language model providers:

- Unix-like: `~/.local/state/goose/logs/llm_request.*.jsonl`
- Windows: `%APPDATA%\Block\goose\data\logs\llm_request.*.jsonl`

These logs use a numbered rotation system that keeps the 10 most recent completed requests (`llm_request.0.jsonl` through `llm_request.9.jsonl`). Each log contains the model configuration, input payload, response data, and token usage information.