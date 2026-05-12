---
title: Ledger & Debugging for RL Rollouts - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/rl-rollout-debugging
source: sitemap
fetched_at: 2026-04-27T20:15:13.028424214-03:00
rendered_js: false
word_count: 447
summary: This document details how hot-load deployments track their history via a ledger, providing methods to inspect this history, reset the ledger, and explains the differences between asynchronous and synchronous snapshot transition behaviors.
tags:
    - hot-load
    - ledger
    - snapshot-history
    - transition-mode
    - deployment-status
    - api-behavior
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Ledger & Debugging for RL Rollouts

A hot-load deployment maintains a **ledger** tracking every snapshot loaded, which replica finished it, and when. The ledger answers "what weights is my deployment serving right now?" and enables recovery from stuck states.

## Inspect snapshot history

Dump the ledger (most recent snapshot first):

```bash
firectl get ledger <deployment_id>
```

Each row shows the `identity` signaled, whether it was a full or delta snapshot, per-replica `readiness` transition timestamps, and any load error.

## Inspect deployment status and failures

If the deployment is unhealthy (crashlooping after a bad snapshot, out-of-memory on merge, etc.), the reason is on the deployment resource itself:

```bash
firectl deployment get <deployment_id>
```

Look at `status`, `latestStatus.reason`, and the most recent ledger entry together to determine if the problem is load-side, weights-side, or infra-side.

## Reset the ledger

If the delta chain is wedged or you want to force the deployment back to the base model, clear server-side ledger history:

```bash
curl -X DELETE \
  https://api.fireworks.ai/v1/accounts/<account_id>/deployments/<deployment_id>/ledger \
  -H "Authorization: Bearer <fireworks_api_key>"
```

> [!warning]
> After reset, your next signal must be a **full** snapshot — delta metadata will be rejected because there's nothing to diff against.

## Checkpoint-swap behavior

When signaling a new snapshot, in-flight and new request behavior during the swap depends on the transition mode.

### Async transition (recommended, default for RL)

Similar in spirit to [PipelineRL](https://arxiv.org/pdf/2509.19128):

- **In-flight requests**: paused for the swap duration, then resumed on the same HTTP connection. The active turn keeps its current KV state and continues streaming instead of restarting.
- **New requests**: queued until the swap finishes, causing elevated time-to-first-token (TTFT).
- No 4xx or 5xx is returned for the swap itself. Set `x-fireworks-hot-load-drain-timeout` header (default `90` seconds) to receive HTTP 425 Too Early once the timeout expires.

![](https://mintcdn.com/fireworksai/sCma6Z58mSRQ1WIG/fine-tuning/assets/hotload-async-transition.drawio.svg?fit=max&auto=format&n=sCma6Z58mSRQ1WIG&q=85&s=929f422e1cc9e8a777f72134707f9b5b) ![](https://mintcdn.com/fireworksai/sCma6Z58mSRQ1WIG/fine-tuning/assets/hotload-async-transition-dark.drawio.svg?fit=max&auto=format&n=sCma6Z58mSRQ1WIG&q=85&s=3c95651d84d41213dbb0bd3f348793be)

### Synchronous transition

- **In-flight requests**: server waits for them to complete on the *old* weights before swapping.
- **New requests** arriving during the swap are rejected with HTTP `425 Too Early`. Back off and retry, ideally using the same session-affinity key to land on a replica that has already finished the swap.

![](https://mintcdn.com/fireworksai/sCma6Z58mSRQ1WIG/fine-tuning/assets/hotload-sync-transition.drawio.svg?fit=max&auto=format&n=sCma6Z58mSRQ1WIG&q=85&s=e8339927f60139d25b787a1b6ea73808) ![](https://mintcdn.com/fireworksai/sCma6Z58mSRQ1WIG/fine-tuning/assets/hotload-sync-transition-dark.drawio.svg?fit=max&auto=format&n=sCma6Z58mSRQ1WIG&q=85&s=e225c5ce42d874d62d210350cc208d6c)

### Prompt cache reset behavior

`reset_prompt_cache` affects what can be reused **after** the swap (not the active turn):

| Value | Behavior |
|-------|----------|
| `all` (default) | After swap, later requests refill prompt cache broadly |
| `new_session` | Existing session IDs keep current cache namespace; new sessions refill |
| `none` | Preserve prompt-cache state across the swap |

Configure per snapshot in `POST /hot_load/v1/models/hot_load`:

```json
{ "identity": "version_002", "reset_prompt_cache": "new_session" }
```

## Need help?

If the ledger stops advancing, a snapshot never becomes ready, or the deployment stays unhealthy after falling back to a full snapshot, contact Fireworks. Include the account ID, deployment ID, snapshot identity tried to load, and the latest ledger output.

#hot-load #ledger #snapshot-history #transition-mode #deployment-status #api-behavior
