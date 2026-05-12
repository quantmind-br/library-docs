---
title: Remote Environment Setup
url: https://docs.fireworks.ai/fine-tuning/connect-environments
source: sitemap
fetched_at: 2026-04-27T20:18:40.269672376-03:00
rendered_js: false
word_count: 327
summary: This document explains how to integrate an agent with RFT using a RemoteRolloutProcessor, detailing the required structure of the `/init` endpoint and demonstrating methods for logging rollout status via Fireworks tracing.
tags:
    - remote-rollout
    - fireworks-tracing
    - agent-integration
    - eval-protocol
    - http-endpoint
    - logging-setup
category: guide
optimized: true
optimized_at: 2026-04-27T23:27:00Z
---
Integrate your existing agent with RFT using a `RemoteRolloutProcessor`. This delegates rollout execution to an HTTP service you control. Remote agents are ideal for:

- Multi-turn agentic workflows with tool use
- Access to private databases, APIs, or internal services
- Integration with existing agent codebases
- Complex simulations that require your infrastructure

## How remote rollouts work

The `RemoteRolloutProcessor` sends rollout requests to your `/init` endpoint. You execute the agent logic and report status via Fireworks tracing.

## Implementing the /init endpoint

Your remote service must implement a single `/init` endpoint.

### Request schema

| Field | Type | Description |
|-------|------|-------------|
| `completion_params` | object | Model configuration (name, temperature, max_tokens, etc.) |
| `messages` | array | Conversation messages to send to the model |
| `tools` | array | Available tools for function calling |
| `model_base_url` | string | URL for LLM calls through Fireworks tracing (includes correlation metadata) |
| `metadata` | object | Rollout execution metadata (`rollout_id`, `run_id`, `row_id`, etc.) |
| `api_key` | string | Fireworks API key for model calls |

### Example request

```json
{
  "completion_params": {
    "model": "accounts/fireworks/models/llama-v3p1-8b-instruct",
    "temperature": 0.7,
    "max_tokens": 2048
  },
  "messages": [
    { "role": "user", "content": "What is the weather in San Francisco?" }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "Get the weather for a city",
        "parameters": {
          "type": "object",
          "properties": { "city": { "type": "string" } }
        }
      }
    }
  ],
  "model_base_url": "https://tracing.fireworks.ai/rollout_id/.../invocation_id/.../experiment_id/.../run_id/.../row_id/...",
  "metadata": {
    "invocation_id": "wise-ocean-15",
    "experiment_id": "calm-forest-28",
    "rollout_id": "brave-night-42",
    "run_id": "quick-river-07",
    "row_id": "bright-star-91"
  },
  "api_key": "fw_your_api_key"
}
```

> [!warning]
> The `metadata` object contains correlation IDs you must include when logging to Fireworks tracing. Required fields: `invocation_id`, `experiment_id`, `rollout_id`, `run_id`, `row_id`.

## Fireworks tracing integration

Eval Protocol polls Fireworks logs by `rollout_id` to detect when rollouts complete.

### Basic setup

```python
import logging
from eval_protocol import Status, InitRequest, FireworksTracingHttpHandler, RolloutIdFilter

# Configure Fireworks tracing handler globally
fireworks_handler = FireworksTracingHttpHandler()
logging.getLogger().addHandler(fireworks_handler)

@app.post("/init")
def init(request: InitRequest):
    # Create rollout-specific logger with filter
    rollout_logger = logging.getLogger(f"eval_server.{request.metadata.rollout_id}")
    rollout_logger.addFilter(RolloutIdFilter(request.metadata.rollout_id))

    try:
        result = execute_agent(request)
        rollout_logger.info(
            f"Rollout {request.metadata.rollout_id} completed",
            extra={"status": Status.rollout_finished()}
        )
        return {"status": "success"}
    except Exception as e:
        rollout_logger.error(
            f"Rollout {request.metadata.rollout_id} failed: {e}",
            extra={"status": Status.rollout_error(str(e))}
        )
        raise
```

### Key components

| Component | Description |
|-----------|-------------|
| `FireworksTracingHttpHandler` | Sends logs to Fireworks tracing service |
| `RolloutIdFilter` | Tags logs with rollout ID for correlation |
| `Status.rollout_finished()` | Signals successful completion |
| `Status.rollout_error(message)` | Signals failure with error details |

### Alternative: Environment variable approach

For simpler setups (single rollout per instance or separate processes per rollout):

```python
import os
from eval_protocol import Status, InitRequest, FireworksTracingHttpHandler

os.environ["EP_ROLLOUT_ID"] = request.metadata.rollout_id
fireworks_handler = FireworksTracingHttpHandler()
logging.getLogger().addHandler(fireworks_handler)

@app.post("/init")
def init(request: InitRequest):
    logger = logging.getLogger(__name__)
    logger.info("Processing rollout...")
    # ... execute agent logic ...
```

For spawning separate processes:

```python
import os
import multiprocessing
from eval_protocol import FireworksTracingHttpHandler, InitRequest

def execute_rollout_step_sync(request):
    os.environ["EP_ROLLOUT_ID"] = request.metadata.rollout_id
    logging.getLogger().addHandler(FireworksTracingHttpHandler())

@app.post("/init")
async def init(request: InitRequest):
    p = multiprocessing.Process(
        target=execute_rollout_step_sync,
        args=(request,)
    )
    p.start()
    return {"status": "started"}
```

## Complete example

```python
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from eval_protocol import InitRequest, FireworksTracingHttpHandler, RolloutIdFilter, Status
import logging

app = FastAPI()

fireworks_handler = FireworksTracingHttpHandler()
logging.getLogger().addHandler(fireworks_handler)

@app.post("/init")
async def init(request: InitRequest):
    rollout_logger = logging.getLogger(f"eval_server.{request.metadata.rollout_id}")
    rollout_logger.addFilter(RolloutIdFilter(request.metadata.rollout_id))

    rollout_logger.info(f"Starting rollout {request.metadata.rollout_id}")

    try:
        result = run_your_agent(
            messages=request.messages,
            tools=request.tools,
            model_config=request.completion_params,
            api_key=request.api_key
        )
        rollout_logger.info(
            f"Rollout {request.metadata.rollout_id} completed successfully",
            extra={"status": Status.rollout_finished()}
        )
        return {"status": "success", "result": result}
    except Exception as e:
        rollout_logger.error(
            f"Rollout {request.metadata.rollout_id} failed: {str(e)}",
            extra={"status": Status.rollout_error(str(e))}
        )
        return JSONResponse(status_code=500, content={"status": "error", "message": str(e)})

def run_your_agent(messages, tools, model_config, api_key):
    # Implement your agent logic here
    pass
```

## Connecting to RFT

Once your remote server is deployed, create an RFT job that uses it:

```bash
eval-protocol create rft \
  --base-model accounts/fireworks/models/llama-v3p1-8b-instruct \
  --remote-server-url https://your-evaluator.example.com \
  --dataset my-dataset
```

> [!tip]
> See [[096-fine-tuning-evaluators]] and [[044-fine-tuning-parameter-tuning]] for more on evaluators and tuning parameters.