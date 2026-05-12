---
title: Configure Fireworks logging sink once at startup
url: https://docs.fireworks.ai/fine-tuning/environments
source: sitemap
fetched_at: 2026-04-27T20:18:40.522801946-03:00
rendered_js: false
word_count: 704
summary: Agent tracing for Reinforcement Learning (RL) capturing full action trajectories for credit assignment, reproducibility, and debuggability via structured logging sinks and correlation metadata.
tags:
    - rl-tracing
    - fireworks-ai
    - agent-behavior
    - credit-assignment
    - structured-logging
    - llm-lifecycle
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Agent Tracing

Agent tracing captures the full action trajectory required for reinforcement learning: tool calls, state transitions, and intermediate decisions—not just the final answer.

## Why agent tracing is critical to doing RL

- **Credit assignment**: Complete record of each step to attribute reward to the decisions that caused success or failure.
- **Reproducibility**: Deterministic replays require the exact prompts, model parameters, tool I/O, and environment state.
- **Debuggability**: Pinpoint where an episode fails (model output, tool error, data mismatch, timeout).

## How Fireworks tracing works for RFT

- **Traced completions**: The trainer provides a `model_base_url` on `https://tracing.fireworks.ai` that encodes correlation metadata. Your agent uses this OpenAI-compatible URL for LLM calls; tracing.fireworks.ai records the calls as traces automatically.
- **Structured logging sink**: Your agent logs to Fireworks via `FireworksTracingHttpHandler`, including a structured `Status` when a rollout finishes or errors.
- **Join traces and logs**: The trainer polls the logging sink by `rollout_id` to detect completion, then loads the full trace. Logs and traces are deterministically joined using the same correlation tags.

### Correlation metadata

- **Correlate every log and trace** with these metadata fields provided in `/init`: `invocation_id`, `experiment_id`, `rollout_id`, `run_id`, `row_id`.
- **Emit structured completion** from your server logs:
  
  - Add `FireworksTracingHttpHandler` and `RolloutIdFilter` to attach the `rollout_id`
  - Log `Status.rollout_finished()` on success, or `Status.rollout_error(message)` on failure
- **Alternative**: If you run one rollout per process, set `EP_ROLLOUT_ID` in the child process instead of adding a filter.
- **Record model calls as traces** by using the `model_base_url` from the trainer. It encodes the correlation IDs so your completions are automatically captured.

### tracing.fireworks.ai base URL

- **Purpose-built for RL**: tracing.fireworks.ai is the Fireworks gateway used during RFT to capture traces and correlate them with rollout status.
- **OpenAI-compatible**: It exposes Chat Completions-compatible endpoints, so you set it as your client's `base_url`.
- **Correlation-aware**: The trainer embeds `rollout_id`, `run_id`, and related IDs into the `model_base_url` path so your completions are automatically tagged and joinable with logs.
- **Drop-in usage**: Always use the `model_base_url` provided in `/init`—do not override it—so traces and logs are correctly linked.

## End-to-end tracing setup with tracing.fireworks.ai

### Remote server minimal example

```python
import logging
import os
from eval_protocol import InitRequest, Status, FireworksTracingHttpHandler, RolloutIdFilter

# Configure Fireworks logging sink once at startup
logging.getLogger().addHandler(FireworksTracingHttpHandler())

@app.post("/init")
def init(request: InitRequest):
    # Option A: add filter that injects rollout_id on every log record
    logger = logging.getLogger(f"eval.{request.metadata.rollout_id}")
    logger.addFilter(RolloutIdFilter(request.metadata.rollout_id))

    # Option B: per-process correlation (use when spawning one rollout per process)
    # os.environ["EP_ROLLOUT_ID"] = request.metadata.rollout_id

    # Make model calls via the correlated base URL so completions are traced
    # client = YourLLMClient(base_url=request.model_base_url, api_key=request.api_key)
    try:
        # ... execute rollout steps, tool calls, etc. ...
        logger.info("rollout finished", extra={"status": Status.rollout_finished()})
    except Exception as e:
        logger.error("rollout error", extra={"status": Status.rollout_error(str(e))})
```

### What to capture in a trace

- **Inputs and context**: Task ID, dataset split, initial state, seeds, and any retrieval results provided to the agent.
- **Model calls**: System/user messages, tool messages, model/version, parameters (e.g., temperature, top_p, seed), token counts, and optional logprobs.
- **Tool and API calls**: Request/response summaries, status codes, durations, retries, and sanitized payload snippets.
- **Environment state transitions**: Key state before/after each action that affects reward or next-step choices.
- **Rewards**: Per-step shaping rewards, terminal reward, and component breakdowns with weights and units.
- **Errors and timeouts**: Exceptions, stack traces, and where they occurred in the trajectory.
- **Artifacts**: Files, code, unit test results, or other outputs needed to verify correctness.

### How tracing powers the training loop

1. **Rollout begins**: Trainer creates a rollout and sends it to your environment (local or remote) with a unique identifier.
2. **Agent executes**: Your agent emits spans for model calls, tool calls, and state changes; your evaluator computes step and terminal rewards.
3. **Rewards aggregate**: The trainer consumes your rewards and updates the policy; traces are stored for replay and analysis.
4. **Analyze and iterate**: You filter traces by reward, failure type, latency, or cost to refine prompts, tools, or reward shaping.

### How RemoteRolloutProcessor uses Fireworks Tracing

1. **Remote server logs completion** with structured status: `Status.rollout_finished()` or `Status.rollout_error()`.
2. **Trainer polls Fireworks Tracing** by `rollout_id` until completion status is found.
3. **Status extracted** from structured fields (`code`, `message`, `details`) to finalize the rollout result.

### Best practices

- **Make it deterministic**: Record seeds, versions, and any non-deterministic knobs; prefer idempotent tool calls or cached fixtures in test runs.
- **Keep signals bounded**: Normalize rewards to a consistent range (e.g., [0, 1]) and document your components and weights.
- **Summarize, don't dump**: Log compact summaries and references for large payloads to keep traces fast and cheap.
- **Emit heartbeats**: Send periodic status updates so long-running rollouts are observable; always finalize with success or failure.
- **Use consistent schemas**: Keep field names and structures stable to enable dashboards, filters, and automated diagnostics.

#rl-tracing #structured-logging #credit-assignment
