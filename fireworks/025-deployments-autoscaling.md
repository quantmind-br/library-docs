---
title: Autoscaling - Fireworks AI Docs
url: https://docs.fireworks.ai/deployments/autoscaling
source: sitemap
fetched_at: 2026-04-27T20:18:52.434616046-03:00
rendered_js: false
word_count: 240
summary: This document details the configuration options for controlling deployment scaling based on traffic and load, outlining various parameters like replica counts and load targets. It also provides common usage patterns and specific logic for handling requests when a deployment is in the process of scaling up from zero replicas.
tags:
    - deployment-scaling
    - load-balancing
    - replica-count
    - config-options
    - scale-to-zero
    - performance
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Control how your deployment scales based on traffic and load.

## Configuration options

| Flag | Type | Default | Description |
|---|---|---|---|
| `--min-replica-count` | Integer | `0` | Minimum replicas. Set to `0` for scale-to-zero |
| `--max-replica-count` | Integer | `1` | Maximum replicas |
| `--scale-up-window` | Duration | `30s` | Wait before scaling up |
| `--scale-down-window` | Duration | `10m` | Wait before scaling down |
| `--scale-to-zero-window` | Duration | `1h` | Idle time before scaling to zero (min: `5m`) |
| `--load-targets` | Key-value | `default=0.8` | Scaling thresholds |

**Load target options** (`--load-targets <key>=<value>[,<key>=<value>...]`):

- `default=<Fraction>` — general load target (0–1)
- `tokens_generated_per_second=<Integer>` — tokens/s/replica target
- `prompt_tokens_per_second=<Integer>` — prompt tokens/s/replica target
- `requests_per_second=<Number>` — requests/s/replica target
- `concurrent_requests=<Number>` — concurrent requests/replica target

When multiple targets are specified, the maximum replica count across all is used.

## Common patterns

### Cost optimization (scale-to-zero)

```
firectl deployment create <MODEL_NAME> \
  --min-replica-count 0 \
  --max-replica-count 3 \
  --scale-to-zero-window 1h
```

Best for: development, testing, intermittent production workloads.

### Performance-focused (keep replicas warm)

```
firectl deployment create <MODEL_NAME> \
  --min-replica-count 2 \
  --max-replica-count 10 \
  --scale-up-window 15s \
  --load-targets concurrent_requests=5
```

Best for: low-latency requirements, avoiding cold starts.

### Predictable traffic

```
firectl deployment create <MODEL_NAME> \
  --min-replica-count 3 \
  --max-replica-count 5 \
  --scale-down-window 30m \
  --load-targets tokens_generated_per_second=150
```

Best for: steady workloads with known load ranges.

## Scaling from zero behavior

When a deployment is scaled to zero and receives a request, the system immediately returns a `503` with error code `DEPLOYMENT_SCALING_UP`:

```json
{
  "error": {
    "message": "Deployment is currently scaled to zero and is scaling up. Please retry your request in a few minutes.",
    "code": "DEPLOYMENT_SCALING_UP",
    "type": "error"
  }
}
```

### Handling scale-from-zero responses

Implement retry logic with exponential backoff to gracefully handle scale-up delays.

> [!tip]
> Cap the delay at 60 seconds to avoid excessive wait times.

```python
import time
import requests

def query_deployment_with_retry(url, payload, max_retries=30, initial_delay=5):
    """Query a deployment with retry logic for scale-from-zero scenarios."""
    delay = initial_delay
    for attempt in range(max_retries):
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 503:
            error_code = response.json().get("error", {}).get("code")
            if error_code == "DEPLOYMENT_SCALING_UP":
                print(f"Deployment scaling up, retrying in {delay}s...")
                time.sleep(delay)
                delay = min(delay * 1.5, 60)  # Cap at 60 seconds
                continue
        response.raise_for_status()
        return response.json()
    raise Exception("Deployment did not scale up in time")
```

```javascript
async function queryDeploymentWithRetry(url, payload, maxRetries = 30, initialDelay = 5000) {
  let delay = initialDelay;
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    const response = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', ...headers },
      body: JSON.stringify(payload)
    });
    if (response.status === 503) {
      const body = await response.json();
      if (body.error?.code === 'DEPLOYMENT_SCALING_UP') {
        console.log(`Deployment scaling up, retrying in ${delay/1000}s...`);
        await new Promise(resolve => setTimeout(resolve, delay));
        delay = Math.min(delay * 1.5, 60000);
        continue;
      }
    }
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return response.json();
  }
  throw new Error('Deployment did not scale up in time');
}
```

```bash
# Simple retry loop for scale-from-zero
MAX_RETRIES=30
RETRY_DELAY=5

for i in $(seq 1 $MAX_RETRIES); do
  response=$(curl -s -w "\n%{http_code}" \
    https://api.fireworks.ai/inference/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $FIREWORKS_API_KEY" \
    -d '{"model": "accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>", ...}')

  http_code=$(echo "$response" | tail -n1)
  body=$(echo "$response" | head -n -1)

  if [ "$http_code" -eq 503 ]; then
    error_code=$(echo "$body" | jq -r '.error.code // empty')
    if [ "$error_code" = "DEPLOYMENT_SCALING_UP" ]; then
      echo "Deployment scaling up, retrying in ${RETRY_DELAY}s..."
      sleep $RETRY_DELAY
      RETRY_DELAY=$((RETRY_DELAY * 2))
      continue
    fi
    echo "$body"
    exit 1
  fi

  if [ "$http_code" -ge 200 ] && [ "$http_code" -lt 300 ]; then
    echo "$body"
    exit 0
  fi

  echo "$body"
  exit 1
done

echo "Deployment did not scale up in time"
exit 1
```

#autoscaling #scale-to-zero #deployment-scaling
