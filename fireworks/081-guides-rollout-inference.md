---
title: Inference for RL Rollouts
url: https://docs.fireworks.ai/guides/rollout-inference
source: sitemap
fetched_at: 2026-04-27T20:15:29.122040407-03:00
rendered_js: false
word_count: 382
summary: Advanced inference features for RL rollout traffic: session affinity, hot-load weight swap behavior, and MoE Router Replay (R3).
tags:
    - inference-api
    - multi-turn-rollouts
    - session-affinity
    - hot-load-swap
    - moe-models
    - routing-matrix
category: guide
optimized: true
optimized_at: 2026-04-27T23:00:00Z
---
Use Fireworks inference endpoints for RL rollouts. The [`/v1/completions`](https://docs.fireworks.ai/api-reference/post-completions) and [`/v1/chat/completions`](https://docs.fireworks.ai/api-reference/post-chatcompletions) endpoints expose extra features for multi-turn, stateful rollout traffic.

## Session Affinity

Multi-turn rollouts reuse a long prefix between turns. For KV cache hits, all turns of a trajectory should land on the same inference replica.

Two headers enable this:

- `x-multi-turn-session-id` — identifies the agent trajectory. Set once per trajectory and keep constant across turns. Fireworks prefers this value when deriving the session-affinity key.
- `x-session-affinity` — fallback sticky routing key when `x-multi-turn-session-id` is absent.

```python
from openai import OpenAI

client = OpenAI(
    api_key="<FIREWORKS_API_KEY>",
    base_url="https://api.fireworks.ai/inference/v1",
)

trajectory_id = "traj-42f1"

for turn in trajectory:
    response = client.chat.completions.create(
        model="accounts/<account_id>/models/<model_id>",
        messages=turn.messages,
        extra_headers={
            "x-multi-turn-session-id": trajectory_id,
            "x-session-affinity": trajectory_id,
            "fireworks-deployment": "accounts/<account_id>/deployments/<deployment_id>",
        },
    )
```

```bash
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Authorization: Bearer <fireworks_api_key>" \
  -H "fireworks-model: accounts/<account_id>/models/<model_id>" \
  -H "fireworks-deployment: accounts/<account_id>/deployments/<deployment_id>" \
  -H "x-multi-turn-session-id: traj-42f1" \
  -H "x-session-affinity: traj-42f1" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "accounts/<account_id>/models/<model_id>",
    "messages": [{"role": "user", "content": "..."}]
  }'
```

## Weight Swap Behavior

If rollout traffic hits a hot-load deployment, a new checkpoint can arrive mid-rollout. Behavior depends on the deployment's transition mode:

- **Async transition (recommended for RL):** in-flight requests pause then resume on the same HTTP connection with new weights. The active turn keeps its KV state and continues rather than restarting. New requests queue up. Elevated TTFT but no errors.
- **Synchronous transition:** in-flight requests finish on old weights; new requests get HTTP `425 Too Early` until the swap is done. Client should retry with back-off, keeping the same session-affinity key to land on a replica that has finished the swap.

`reset_prompt_cache` only affects what future requests or session IDs can reuse after the swap. See [[046-fine-tuning-rl-rollout-debugging#checkpoint-swap-behavior|Checkpoint-swap behavior]] for full semantics.

## MoE Router Replay (R3)

For Mixture-of-Experts models, training-inference divergence comes from the router picking different top-K experts at the same token position between trainer and inference. Aligning those choices across rollouts and training is known as [Rollout Router Replay (R3)](https://arxiv.org/abs/2510.11370).

Pass `include_routing_matrix: true` with `logprobs: true`:

```bash
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Authorization: Bearer <fireworks_api_key>" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "accounts/<account_id>/models/<model_id>",
    "messages": [{"role": "user", "content": "..."}],
    "include_routing_matrix": true,
    "logprobs": true
  }'
```

Selected expert indices for each token are returned alongside logprobs:

- `/v1/chat/completions`: `choices[i].logprobs.content[j].routing_matrix`
- `/v1/completions`: analogous structure

Each value is a flattened, base64-encoded `uint8` array of shape `[num_layers_with_moe, num_active_experts]`.

### Example Response (DeepSeek V3)

```json
{
  "object": "text_completion",
  "model": "...my-deepseek-v3-model...",
  "choices": [
    {
      "index": 0,
      "logprobs": {
        "content": [
          {
            "token": " ",
            "logprob": -0.00014507,
            "sampling_logprob": -0.0001450882,
            "token_id": 223,
            "routing_matrix": "CYvWPzaOl8g/o7q2XPVTMJ7w/Y8G..."
          }
        ]
      }
    }
  ]
}
```

### Decoding the Routing Matrix

DeepSeek V3 has 58 MoE layers (first 3 of 61 total are dense) and selects 8 active experts per token, so each decoded buffer is `58 * 8 = 464` bytes:

```python
import base64
import numpy as np

num_layers_with_moe = 58
num_active_experts = 8

encoded = choice["logprobs"]["content"][0]["routing_matrix"]
raw_bytes = base64.b64decode(encoded)
routing_matrix = np.frombuffer(raw_bytes, dtype=np.uint8).reshape(
    num_layers_with_moe, num_active_experts
)
# routing_matrix[layer_idx] -> array of 8 expert indices for that token
```

### Other API Modes

- **Completions API (`/v1/completions`)**: `include_routing_matrix` and `logprobs` are top-level body fields.
- **Streaming (`stream: true`)**: `routing_matrix` included on each streamed token chunk's `logprobs.content` entry.
- **Prompt tokens (`echo: true`)**: returns expert selection for prompt tokens. Combine with `echo_last: N` to include expert selection for last N prompt tokens only.