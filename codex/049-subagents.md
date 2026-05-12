---
title: Subagents
url: https://developers.openai.com/codex/subagents.md
source: llms
fetched_at: 2026-04-30T10:16:09.540962303-03:00
rendered_js: false
word_count: 786
summary: This document explains how to utilize subagent workflows in Codex to execute parallelized tasks and defines the process for creating and configuring custom specialized agents.
tags:
    - codex
    - subagents
    - agent-orchestration
    - automation
    - parallel-processing
    - custom-agents
category: concept
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Subagents

Spawn specialized agents in parallel and collect their results in one response. Helpful for complex, highly parallel tasks such as codebase exploration or implementing multi-step feature plans.

For concepts and tradeoffs (context pollution, context rot, model selection), see [[045-concepts-subagents|Subagent concepts]].

## Availability

Enabled by default in current Codex releases. Subagent activity surfaced in Codex app and CLI; IDE Extension visibility coming soon.

Codex only spawns subagents when explicitly asked. Each subagent does its own model and tool work, so subagent workflows consume more tokens than single-agent runs.

## Typical workflow

Codex handles orchestration: spawning subagents, routing follow-up instructions, waiting for results, closing agent threads. When many agents run, Codex waits until all requested results are available, then returns a consolidated response.

Example prompt:
```text
I would like to review the following points on the current PR (this branch vs main). Spawn one agent per point, wait for all of them, and summarize the result for each point.
1. Security issue
2. Code quality
3. Bugs
4. Race
5. Test flakiness
6. Maintainability of the code
```

## Managing subagents

- Use `/agent` in the CLI to switch between active agent threads and inspect ongoing threads.
- Ask Codex directly to steer a running subagent, stop it, or close completed threads.

## Approvals and sandbox

Subagents inherit your current sandbox policy.

In interactive CLI sessions, approval requests can surface from inactive agent threads even while viewing the main thread. The approval overlay shows the source thread label; press `o` to open that thread before approving, rejecting, or answering.

In non-interactive flows or when a run can't surface a fresh approval, an action needing new approval fails and Codex surfaces the error back to the parent workflow.

Codex reapplies the parent turn's live runtime overrides when spawning a child — including sandbox and approval choices set interactively (e.g., `/approvals` changes or `--yolo`), even if the custom agent file sets different defaults.

You can override sandbox configuration for individual [[049-subagents#custom-agents|custom agents]], such as explicitly marking one to work in read-only mode.

## Custom agents

Built-in agents:
- `default` — general-purpose fallback
- `worker` — execution-focused for implementation and fixes
- `explorer` — read-heavy codebase exploration

Define custom agents with standalone TOML files:
- Personal: `~/.codex/agents/`
- Project-scoped: `.codex/agents/`

Each file defines one custom agent. Custom agents can override the same settings as a normal Codex session config.

Required fields:
- `name`
- `description`
- `developer_instructions`

Optional: `nickname_candidates`, `model`, `model_reasoning_effort`, `sandbox_mode`, `mcp_servers`, `skills.config` — inherit from parent session when omitted.

### Global settings

In `[agents]` in [[055-config-basic|configuration]]:

| Field | Type | Default | Purpose |
|-------|------|---------|---------|
| `agents.max_threads` | number | `6` | Concurrent open agent thread cap |
| `agents.max_depth` | number | `1` | Spawned agent nesting depth (root = 0). Keep default unless you need recursive delegation. Deeper recursion increases token usage, latency, and local resource consumption. |
| `agents.job_max_runtime_seconds` | number | `1800` | Default timeout per worker for `spawn_agents_on_csv` jobs |

If a custom agent name matches a built-in agent (e.g., `explorer`), your custom agent takes precedence.

### Display nicknames

Use `nickname_candidates` for more readable display names when running many instances of the same custom agent. Presentation-only; Codex still identifies and spawns by `name`.

Must be non-empty list of unique names using ASCII letters, digits, spaces, hyphens, underscores.

Example:
```toml
name = "reviewer"
description = "PR reviewer focused on correctness, security, and missing tests."
developer_instructions = """
Review code like an owner.
Prioritize correctness, security, behavior regressions, and missing test coverage.
"""
nickname_candidates = ["Atlas", "Delta", "Echo"]
```

### Example custom agents

Best custom agents are narrow and opinionated: clear job, matching tool surface, instructions that prevent drift into adjacent work.

#### Example 1: PR review

Splits review across three focused agents:
- `pr_explorer` — maps codebase and gathers evidence
- `reviewer` — correctness, security, test risks
- `docs_researcher` — checks framework/API documentation via dedicated MCP server

`.codex/config.toml`:
```toml
[agents]
max_threads = 6
max_depth = 1
```

`.codex/agents/pr-explorer.toml`:
```toml
name = "pr_explorer"
description = "Read-only codebase explorer for gathering evidence before changes are proposed."
model = "gpt-5.3-codex-spark"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Stay in exploration mode.
Trace the real execution path, cite files and symbols, and avoid proposing fixes unless the parent agent asks for them.
Prefer fast search and targeted file reads over broad scans.
"""
```

`.codex/agents/reviewer.toml`:
```toml
name = "reviewer"
description = "PR reviewer focused on correctness, security, and missing tests."
model = "gpt-5.4"
model_reasoning_effort = "high"
sandbox_mode = "read-only"
developer_instructions = """
Review code like an owner.
Prioritize correctness, security, behavior regressions, and missing test coverage.
Lead with concrete findings, include reproduction steps when possible, and avoid style-only comments unless they hide a real bug.
"""
```

`.codex/agents/docs-researcher.toml`:
```toml
name = "docs_researcher"
description = "Documentation specialist that uses the docs MCP server to verify APIs and framework behavior."
model = "gpt-5.4-mini"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Use the docs MCP server to confirm APIs, options, and version-specific behavior.
Return concise answers with links or exact references when available.
Do not make code changes.
"""

[mcp_servers.openaiDeveloperDocs]
url = "https://developers.openai.com/mcp"
```

Prompt:
```text
Review this branch against main. Have pr_explorer map the affected code paths, reviewer find real risks, and docs_researcher verify the framework APIs that the patch relies on.
```

## Process CSV batches with subagents (experimental)

Use `spawn_agents_on_csv` for many similar tasks mapping one row per work item. Codex reads the CSV, spawns one worker per row, waits for the full batch, and exports combined results to CSV.

Good for:
- reviewing one file, package, or service per row
- checking a list of incidents, PRs, or migration targets
- generating structured summaries for many similar inputs

Parameters:
- `csv_path` — source CSV
- `instruction` — worker prompt template using `{column_name}` placeholders
- `id_column` — stable item IDs from specific column
- `output_schema` — fixed JSON shape per worker
- `output_csv_path`, `max_concurrency`, `max_runtime_seconds` — job control

Each worker must call `report_agent_job_result` exactly once. If a worker exits without reporting, Codex marks that row with an error in the exported CSV.

Example prompt:
```text
Create /tmp/components.csv with columns path,owner and one row per frontend component.

Then call spawn_agents_on_csv with:
- csv_path: /tmp/components.csv
- id_column: path
- instruction: "Review {path} owned by {owner}. Return JSON with keys path, risk, summary, and follow_up via report_agent_job_result."
- output_csv_path: /tmp/components-review.csv
- output_schema: an object with required string fields path, risk, summary, and follow_up
```

When run through `codex exec`, Codex shows a single-line progress update on `stderr`. Exported CSV includes original row data plus metadata: `job_id`, `item_id`, `status`, `last_error`, `result_json`.

Related settings:
- `agents.max_threads` — caps concurrent open threads
- `agents.job_max_runtime_seconds` — default per-worker timeout for CSV fan-out
- `sqlite_home` — where Codex stores SQLite-backed state for agent jobs and exported results

#### Example 2: Frontend integration debugging

Useful for UI regressions, flaky browser flows, or integration bugs crossing application code and running product.

`.codex/agents/code-mapper.toml`:
```toml
name = "code_mapper"
description = "Read-only codebase explorer for locating relevant frontend and backend code paths."
model = "gpt-5.4-mini"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Map the code that owns the failing UI flow.
Identify entry points, state transitions, and likely files before the worker starts editing.
"""
```

`.codex/agents/browser-debugger.toml`:
```toml
name = "browser_debugger"
description = "UI debugger that uses browser tooling to reproduce issues and capture evidence."
model = "gpt-5.4"
model_reasoning_effort = "high"
sandbox_mode = "workspace-write"
developer_instructions = """
Reproduce the issue in the browser, capture exact steps, and report what the UI actually does.
Use browser tooling for screenshots, console output, and network evidence.
Do not edit application code.
"""

[mcp_servers.chrome_devtools]
url = "http://localhost:3000/mcp"
startup_timeout_sec = 20
```

`.codex/agents/ui-fixer.toml`:
```toml
name = "ui_fixer"
description = "Implementation-focused agent for small, targeted fixes after the issue is understood."
model = "gpt-5.3-codex-spark"
model_reasoning_effort = "medium"
developer_instructions = """
Own the fix once the issue is reproduced.
Make the smallest defensible change, keep unrelated files untouched, and validate only the behavior you changed.
"""

[[skills.config]]
path = "/Users/me/.agents/skills/docs-editor/SKILL.md"
enabled = false
```

Prompt:
```text
Investigate why the settings modal fails to save. Have browser_debugger reproduce it, code_mapper trace the responsible code path, and ui_fixer implement the smallest fix once the failure mode is clear.
```

#subagents #parallel-processing #custom-agents #orchestration #codex