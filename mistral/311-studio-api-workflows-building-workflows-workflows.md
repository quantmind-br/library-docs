---
title: Workflows | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/building-workflows/workflows
source: sitemap
fetched_at: 2026-04-26T04:13:55.379223863-03:00
rendered_js: false
word_count: 1242
summary: This document explains the architecture and implementation of durable, deterministic workflows, detailing how to enforce determinism, manage execution state, and structure code using the SDK.
tags:
    - workflows
    - determinism
    - orchestration
    - python-sdk
    - event-driven
    - sandbox-execution
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Workflows define the high-level business logic and coordinate activities in your application.

A workflow is a durable, deterministic process that orchestrates activities and manages execution state. Key characteristics:
- Defined as Python classes
- Can run for seconds to years (with proper checkpointing)
- Maintains complete execution history
- Automatically recovers from failures
- Input/output limited to 2MB
- Timeout if synchronous CPU-bound Python code exceeds 2 seconds ([see more](https://docs.mistral.ai/studio-api/workflows/managing-workflows-in-production/rate_limiting))

## Determinism

Workflows must be **deterministic**: given the same inputs, they must always produce the same sequence of commands. This is fundamental to the replay mechanism: when a worker restarts or a workflow is recovered, the system re-executes the workflow code from the beginning, matching each command against the recorded event history. If the code produces different commands on replay, the workflow fails with a non-determinism error.

## Determinism Enforcement (Sandbox)

Determinism is **enforced by default**. Workflow code runs inside a sandbox that intercepts non-deterministic calls and raises errors at runtime. You can opt out per-workflow with `enforce_determinism=False` or worker-wide with `DEFAULT_ENFORCE_DETERMINISM=0`.

### Safe Operations

Always use these in workflow code:

```python
```

### Unsafe Operations

Don't use these directly in workflow code:

```python
```

Also dangerous in workflows:
- File system access (`open()`, `os.listdir()`, etc.)
- Direct HTTP calls or database queries
- Modifying global variables
- System calls (`os.environ`, `os.getcwd()`, etc.)

For operations like external API calls, database queries, or file I/O, use activities.

### Sandbox Behavior

When determinism enforcement is enabled, your workflow code runs inside a sandbox. The sandbox:
- **Re-imports modules** in an isolated environment so that side-effectful module-level code is contained
- **Intercepts dangerous standard library calls** such as `datetime.now()`, `random.random()`, `uuid.uuid4()`, `open()`, `os.environ`, and other non-deterministic operations
- **Restricts the asyncio event loop** to prevent spawning uncontrolled coroutines

If your workflow code attempts any of these operations, the sandbox raises an error at runtime rather than silently producing a non-determinism bug that surfaces only on replay.

If you disable the sandbox, determinism is your responsibility. Your code will still break on replay if it's non-deterministic, you just won't get an immediate error telling you so.

### Opting Out

Determinism enforcement is enabled by default. To opt out for a specific workflow, pass `enforce_determinism=False` to the `@workflow.define` decorator:

```python
```

Set the `DEFAULT_ENFORCE_DETERMINISM` environment variable to disable sandboxing for all workflows on a worker by default:

```bash
```

This sets `config.worker.default_enforce_determinism` to `False`.

The decorator-level setting takes priority over the environment variable:

```python
```

> [!warning] These escape hatches defeat the purpose of determinism enforcement. Use them only when you understand the implications and have no alternative.

## Unsafe Operations (Advanced)

When determinism enforcement is enabled, you may occasionally need to perform an operation that the sandbox blocks, for example importing a module that has non-deterministic side effects at import time, or performing a one-off read that you know is safe.

The SDK exposes two context managers under `workflow.unsafe`:

**`workflow.unsafe.imports_passed_through()`** — Allows imports inside the context to bypass the sandbox's module re-import mechanism. Use this when a third-party library performs side effects at import time that conflict with the sandbox.

**`workflow.unsafe.skip_determinism_enforcement()`** — Temporarily disables all sandbox restrictions within the context. Code inside this block runs as if `enforce_determinism=False`.

## Best Practices

1. **Keep enforcement enabled.** Determinism enforcement is on by default. Catching non-determinism at development time is far cheaper than debugging replay failures in production. Only disable it temporarily while migrating legacy workflows.
2. **Migrate existing workflows incrementally.** If you have workflows that are not yet compliant, set `enforce_determinism=False` on those specific workflows while you fix them. Avoid disabling enforcement worker-wide.
3. **Keep unsafe blocks small and documented.** When you must bypass the sandbox, wrap the minimum amount of code and leave a comment explaining why.
4. **Move side effects to activities.** The best way to avoid sandbox issues is to keep workflow code pure orchestration logic. All I/O, network calls, and non-deterministic operations belong in activities.

## Basic Workflow Structure

```python
```

## Input Handling

The `run` method accepts any JSON-serializable types as parameters.

**Simple input:**

```python
```

**Pydantic model input:**

When the entrypoint takes a single Pydantic `BaseModel`, its fields become the top-level input keys — there is no wrapper object:

```python
```

**Union input:**

When a workflow can be triggered with different input shapes, use a union of `BaseModel` subclasses:

```python
```

The SDK validates the input against each member in order and passes the first match to the handler:

> [!tip] Use `extra="forbid"` on each member model. It produces precise discrimination and clear error messages when the input doesn't match any expected shape.

Append `| None` (or use `Optional` from `typing`) to make the input optional:

```python
```

> [!warning] Unions that combine a `BaseModel` with a non-model type (`str`, `int`, etc.) are not supported and will fail when the `@workflow.entrypoint` decorator is applied.

If you genuinely need a union that includes a non-model type, define a named `RootModel` subclass and use that instead:

```python
```

The named subclass also produces a cleaner generated JSON schema.

## Execution Timeout

Every workflow has a maximum total execution time — `execution_timeout` — that caps its lifetime including all retries and [continue-as-new](#7-continue-as-new) iterations.

Set it on the `@workflow.define` decorator:

```python
```

When the workflow is started via the API, the platform uses this value as the hard cap. A workflow that is still running (or waiting) after `execution_timeout` has elapsed is cancelled with a `WORKFLOW_EXECUTION_TIMED_OUT` error.

**Default: 1 hour.** Workflows that need to run longer must opt in explicitly:

```python
```

> [!note] `execution_timeout` is a *total* wall-clock limit, not an activity timeout. Individual activity timeouts are controlled by `start_to_close_timeout` / `schedule_to_close_timeout` on each activity call.

## Interactions

Handle external events with signals:

```python
```

[Learn more about signals](https://docs.mistral.ai/studio-api/workflows/interacting-with-workflows/signals)

Expose workflow state through queries:

```python
```

[Learn more about queries](https://docs.mistral.ai/studio-api/workflows/interacting-with-workflows/queries)

Handle workflow updates:

```python
```

[Learn more about updates](https://docs.mistral.ai/studio-api/workflows/interacting-with-workflows/updates)

Define scheduled workflow executions using cron expressions:

```python
```

Key schedule features:
- Cron-based scheduling with standard cron expressions
- Input parameters for scheduled executions
- Multiple cron expressions can be specified

[Learn more about scheduling](https://docs.mistral.ai/studio-api/workflows/building-workflows/scheduling)

Execute other workflows as children:

```python
```

You can also start a child workflow without waiting for its result (fire-and-forget) by passing `wait=False`:

```python
```

By default, `wait=False` sets the parent close policy to `ABANDON`, so the child continues running even if the parent completes. You can override this with the `parent_close_policy` parameter:

```python
```

Pause the workflow until a condition becomes true — typically set by an incoming signal or update. The workflow sleeps without consuming resources. If the condition is not met within the `timeout`, a `TimeoutError` is raised.

Reset workflow history for long-running or iterative workflows. Use this to prevent history from growing too large when processing large datasets or running indefinitely.

> [!important] Your workflow's `run` method must accept a state parameter to restore its state when continuing as new. This parameter will receive the state passed to `continue_as_new()`.

**When to use continue-as-new:**
- Long-running workflows that iterate indefinitely
- When workflow history approaches size limits (~50K events)
- Workflows that need to run for weeks/months

You can "reset" a Workflow Execution to restart it from a specific point in its history. This is useful if your workflow gets stuck (for example, because of a non-deterministic error) or cannot complete. When you reset, the workflow ends its current run and starts again from the event you pick in the event history.

All workflow events up to the reset point are copied to the new execution. The workflow then continues running from there using the latest version of your code. Any progress made after the reset event will be lost.

Resetting should only be used after fixing the underlying problem. It's best practice to provide a reason for the reset, which is recorded in the workflow's event history.

## Workflow Execution Context

Retrieve the current execution's unique identifier at runtime. This is useful for logging, correlating events across services, or passing the execution ID to external systems so they can send signals back.