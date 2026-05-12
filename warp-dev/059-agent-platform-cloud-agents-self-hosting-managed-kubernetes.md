---
title: 'Managed: Kubernetes | Agents | Warp'
url: https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/managed-kubernetes
source: sitemap
fetched_at: 2026-04-29T15:04:47.163419665-03:00
rendered_js: false
word_count: 1348
summary: This guide explains how to deploy the oz-agent-worker daemon into a Kubernetes cluster using Helm for task execution and orchestration.
tags:
    - kubernetes
    - helm
    - agent-worker
    - deployment
    - self-hosting
    - task-orchestration
category: guide
optimized: true
optimized_at: 2026-04-29T15:04:47.163419665-03:00
---
Deploy the `oz-agent-worker` daemon into a Kubernetes cluster using the included Helm chart. Each agent task runs as a **Kubernetes Job** in your cluster. Oz orchestrates runs end to end (Slack, Linear, schedules, API, `oz agent run-cloud`); your cluster provides compute, scheduling, and policy enforcement.

## When to use the Kubernetes backend

- You already operate a Kubernetes cluster and want agents to run there
- You need Kubernetes-native scheduling, resource management, or policy enforcement
- You want to use Kubernetes Secrets, ServiceAccounts, and admission policies

## How it works

1. The worker connects to the Kubernetes API server (in-cluster auth by default, or explicit kubeconfig)
2. On startup, the worker runs a **preflight Job** to verify cluster permissions, admission policies, and Pod Security Standards
3. For each assigned task, the worker creates a Kubernetes Job in the configured namespace
4. The worker monitors Job and Pod status via Kubernetes Watch (30-second safety-net poll for watch disconnects)
5. After task completion, the Job is cleaned up (unless `--no-cleanup` is set)

If the preflight fails, the worker exits with a diagnostic error before accepting any tasks.

## Prerequisites

- **Enterprise plan with self-hosting enabled** — [Contact sales](https://warp.dev/contact-sales)
- **A Kubernetes cluster** where the worker process can reach the API server, with:
  - Namespace must allow creation of Jobs with a **root init container**
  - Namespace-scoped permissions: `create`, `get`, `list`, `watch`, `delete` on `jobs`; `get`, `list`, `watch` on `pods`; `get` on `pods/log`; `list` on `events`
- **Helm** and **kubectl** authenticated against the target cluster
- **A team API key** — In the Warp app, go to **Settings** > **Cloud platform** > **Oz Cloud API Keys**

## Install with the Helm chart

The `oz-agent-worker` repository includes a namespace-scoped Helm chart at `charts/oz-agent-worker`.

### What the chart deploys

| Resource | Description |
|----------|-------------|
| `Deployment` | Long-lived deployment running `oz-agent-worker` with Kubernetes backend |
| `ServiceAccount` | Namespaced service account for the worker |
| `Role` / `RoleBinding` | Minimum permissions to manage task Jobs and Pods |
| `ConfigMap` | Worker config YAML |
| `Secret` | Optional `WARP_API_KEY` Secret |

The chart does not create CRDs or cluster-scoped RBAC resources.

### 1. Set your API key and namespace

```bash
kubectl create namespace warp-oz
export WARP_API_KEY="your-api-key"
```

### 2. Create the API key Secret

```bash
kubectl create secret generic oz-agent-worker \
  -n warp-oz \
  --from-literal=WARP_API_KEY="$WARP_API_KEY"
```

**Expected outcome:** `kubectl get secret -n warp-oz oz-agent-worker` shows the Secret.

### 3. Install the chart

```bash
git clone https://github.com/warpdotdev/oz-agent-worker.git
cd oz-agent-worker
helm install oz-agent-worker ./charts/oz-agent-worker \
  -n warp-oz \
  --set worker.workerId="my-worker" \
  --set image.tag="latest"
```

**Expected outcome:** `kubectl get pods -n warp-oz` shows the worker Deployment pod as `Running`, and worker logs show `Connected to Oz` / `Listening for tasks`.

> [!info]
> To scale horizontally, deploy multiple Helm releases with distinct worker IDs rather than increasing replicas on a single release.

## Key chart values

### Required

| Value | Description |
|-------|-------------|
| `worker.workerId` | Worker ID (same as `--worker-id`) |
| `image.tag` | Worker image tag to deploy |

### Worker configuration

| Value | Default | Description |
|-------|---------|-------------|
| `worker.logLevel` | `info` | Log verbosity (`debug`, `info`, `warn`, `error`) |
| `worker.cleanup` | `true` | Whether to clean up task Jobs after execution |
| `worker.maxConcurrentTasks` | `0` | Maximum concurrent tasks (0 = unlimited) |
| `worker.idleOnComplete` | - | Duration to keep oz process alive after task completion |
| `worker.resources` | `100m` CPU, `128Mi` memory | Resource requests/limits for worker Deployment |
| `worker.livenessProbe` | `exec` probe (`kill -0 1`) | Override with custom probe or set to `null` to disable |
| `worker.nodeSelector` | - | Scheduling constraints |
| `worker.tolerations` | - | Scheduling constraints |
| `worker.affinity` | - | Scheduling constraints |

### Kubernetes backend

| Value | Default | Description |
|-------|---------|-------------|
| `kubernetesBackend.namespace` | release namespace | Namespace for task Jobs |
| `kubernetesBackend.defaultImage` | `ubuntu:22.04` | Default Docker image for task pods |
| `kubernetesBackend.imagePullPolicy` | `IfNotPresent` | Image pull policy for task pods |
| `kubernetesBackend.preflightImage` | `busybox:1.36` | Image for startup preflight Job |
| `kubernetesBackend.unschedulableTimeout` | `30s` | How long a pod may remain unschedulable before failing |
| `kubernetesBackend.setupCommand` | - | Shell command to run before each task |
| `kubernetesBackend.teardownCommand` | - | Shell command to run after each task |
| `kubernetesBackend.extraLabels` | - | Additional labels for task Jobs and Pods |
| `kubernetesBackend.extraAnnotations` | - | Additional annotations for task Jobs and Pods |
| `kubernetesBackend.activeDeadlineSeconds` | - | Maximum task Job lifetime |
| `kubernetesBackend.workspaceSizeLimit` | - | Size limit for workspace `emptyDir` volume |
| `kubernetesBackend.podTemplate` | - | Raw PodSpec YAML for task Jobs |

### API key Secret

| Value | Default | Description |
|-------|---------|-------------|
| `warp.apiKeySecret.create` | `false` | Create Secret from `warp.apiKeySecret.value` |
| `warp.apiKeySecret.value` | - | API key value (only when `create: true`) |
| `warp.apiKeySecret.name` | `oz-agent-worker` | Name of Secret containing `WARP_API_KEY` |
| `warp.apiKeySecret.key` | `WARP_API_KEY` | Key within the Secret |

See the [self-hosted worker reference](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/reference#kubernetes-backend-config) for the full config file schema.

## Cluster selection

Cluster selection follows Kubernetes client config conventions:

- Set `backend.kubernetes.kubeconfig` to use an explicit kubeconfig file
- If `kubeconfig` is omitted and the worker runs inside a Kubernetes pod, the worker uses in-cluster config automatically
- Otherwise, the worker falls back to default kubeconfig loading rules and uses the current context

`namespace` selects the namespace inside the chosen cluster. Defaults to `default`.

## Pod template

The `pod_template` field accepts standard Kubernetes PodSpec YAML for declarative task pod configuration (scheduling, service accounts, image pull secrets, resources, environment variables).

When using `pod_template`, define a container named `task` to customize the main task container directly. Otherwise, the worker appends its own `task` container to the PodSpec.

Use `valueFrom.secretKeyRef` to inject Kubernetes Secret values into task container environment variables:

```yaml
podTemplate:
  spec:
    serviceAccountName: "task-service-account"
    containers:
      - name: task
        env:
          - name: DATABASE_PASSWORD
            valueFrom:
              secretKeyRef:
                name: db-credentials
                key: password
```

> [!info]
> The worker Deployment's ServiceAccount is separate from the task Job `serviceAccountName` you configure in `pod_template`. The Deployment ServiceAccount needs RBAC to manage Jobs and Pods. The task ServiceAccount controls what the agent process can access at runtime.

## Preflight check

On startup, the worker creates a short-lived preflight Job to verify:
- The worker has sufficient RBAC permissions in the target namespace
- Cluster admission policies (Pod Security Standards, OPA Gatekeeper, Kyverno, etc.) allow the worker's task pod shape
- The preflight image can be pulled

If the preflight fails, the worker logs a diagnostic error and exits before accepting any tasks. This surfaces policy and configuration issues at deploy time rather than at task execution time.

The preflight image defaults to `busybox:1.36`. If your cluster restricts allowed registries, set `preflightImage` to an allowlisted image. When `imagePullSecrets` is configured in `pod_template`, those secrets apply to the preflight Job as well.

## Environment variables for Kubernetes tasks

Two ways to pass environment variables to Kubernetes task containers:

1. **`pod_template`** (recommended) — Use standard Kubernetes `env` syntax in the `task` container, including `valueFrom.secretKeyRef` for Kubernetes Secrets
2. **`-e` / `--env` flags** — Backend-agnostic runtime overrides across all managed backends

> [!info]
> If your organization uses an external secrets manager (HashiCorp Vault, AWS Secrets Manager, GCP Secret Manager, etc.), inject secrets into task pods via the CSI Secrets Store Driver. Configure `volumes`, `volumeMounts`, and annotations in `pod_template`. See your secrets provider's documentation.

## Setup and teardown commands

Use `kubernetesBackend.setupCommand` (Helm value) or `backend.kubernetes.setup_command` ([config file](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/reference#kubernetes-backend-config)) to run a shell command before each task. Use `teardownCommand` / `teardown_command` for cleanup after the task finishes.

## Operational notes

- **Scaling** — Deploy multiple Helm releases with distinct worker IDs rather than scaling a single release horizontally
- **Security context** — Deployment defaults to non-root (`runAsUser: 10001`) with `allowPrivilegeEscalation: false` and all capabilities dropped
- **Liveness probe** — Default `exec` probe (`kill -0 1`). Override with `worker.livenessProbe` or set to `null` to disable
- **In-cluster auth** — Chart assumes worker runs inside the target cluster and uses in-cluster Kubernetes auth by default
- **Root init containers** — Task Jobs require a root init container for sidecar materialization. Ensure the task namespace's Pod Security Standards allow this

## Related pages

- [[209-agent-platform-cloud-agents-self-hosting#routing-runs-to-self-hosted-workers|Routing runs to self-hosted workers]] — Send tasks to your connected worker
- [[205-agent-platform-cloud-agents-environments|Environments]] — Define the task image, repos, and setup commands

Last updated 21 hours ago