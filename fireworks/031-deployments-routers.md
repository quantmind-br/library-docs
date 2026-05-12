---
title: Routers - Fireworks AI Docs
url: https://docs.fireworks.ai/deployments/routers
source: sitemap
fetched_at: 2026-04-27T20:18:48.846534537-03:00
rendered_js: false
word_count: 340
summary: This document explains the concept and functionality of a Router, detailing how it controls and distributes inference traffic across multiple deployments for purposes like A/B testing, gradual migration, and load balancing. It also provides commands and strategies for managing these routers.
tags:
    - router
    - traffic-routing
    - deployment-management
    - a-b-testing
    - replica-weighting
    - inference-traffic
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
A **Router** controls how inference traffic is routed to one or more deployments. Traffic is split proportionally based on replica count — a deployment with 3 replicas and another with 2 receives 60% and 40% of traffic respectively.

## Use cases

### Stable alias for deployment replacement

Give your application the **router name** instead of the deployment name. Swap the underlying deployment without changing your application:

```
accounts/<ACCOUNT_ID>/routers/my-router
  └── Initially routes to: accounts/<ACCOUNT_ID>/deployments/v1
  └── Later updated to:    accounts/<ACCOUNT_ID>/deployments/v2
```

### A/B testing

Place multiple deployments under one router. Control the traffic ratio by adjusting replicas:

```bash
firectl router create \
    --router-id=ab-test \
    --deployments=model-a,model-b
```

### Gradual traffic migration

Shift traffic with zero downtime by scaling replicas up on the new deployment and down on the old.

## Traffic routing mechanics

Traffic is distributed using **weighted replica** selection — each request is randomly assigned to a deployment, weighted by its replica count.

| Deployment | Replicas | Traffic share |
|---|---|---|
| `deployment-a` | 3 | 60% |
| `deployment-b` | 2 | 40% |
| **Total** | **5** | **100%** |

To change the split, scale replica counts on the underlying deployments. The router adjusts automatically.

### Sending traffic to a router

Use the router ID in the `model` field, just like a deployment:

```bash
curl -s -X POST https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "accounts/<ACCOUNT_ID>/routers/<ROUTER_ID>",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

## Managing routers

### Create

```bash
firectl router create \
    --deployments=<DEPLOYMENT_1>,<DEPLOYMENT_2>
```

| Flag | Description |
|---|---|
| `--router-id` | Specific router ID (otherwise random) |
| `--display-name` | Human-readable name |
| `--model` | Model to route traffic to |
| `--strategy` | Routing strategy. Default: `weighted-random` |
| `--public` | Make accessible to other accounts |

### List

```bash
firectl router list
```

### Get details

```bash
firectl router get <ROUTER_ID>
# or
firectl router get accounts/<ACCOUNT_ID>/routers/<ROUTER_ID>
```

### Update

```bash
firectl router update <ROUTER_ID> \
    --deployments=<DEPLOYMENT_1>,<DEPLOYMENT_2>,<DEPLOYMENT_3>
```

### Delete

```bash
firectl router delete <ROUTER_ID>
```

## Example: traffic migration

### Step 1 — Create a router for the existing deployment

```bash
firectl router create \
    --router-id=my-router \
    --deployments=current-deployment
```

Your app sends traffic to `accounts/<ACCOUNT_ID>/routers/my-router`. All traffic goes to `current-deployment`.

### Step 2 — Add the new deployment to the router

```bash
firectl deployment create accounts/<ACCOUNT_ID>/models/<MODEL_ID> \
    --deployment-id=new-deployment

firectl router update my-router \
    --deployments=current-deployment,new-deployment
```

New deployment starts with 1 replica by default, so with 4 replicas on `current-deployment`, the split is immediately 80%/20%.

### Step 3 — Shift more traffic

```bash
firectl deployment update new-deployment \
    --min-replica-count=4 \
    --max-replica-count=4

firectl deployment update current-deployment \
    --min-replica-count=1 \
    --max-replica-count=1
```

Split is now 20% old / 80% new.

### Step 4 — Complete the migration

```bash
# Scale old deployment to zero
firectl deployment update current-deployment \
    --min-replica-count=0 \
    --max-replica-count=0

# Remove old deployment from router
firectl router update my-router --deployments=new-deployment
```

All traffic now flows to `new-deployment`.

#router #traffic-routing #a-b-testing
