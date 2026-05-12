---
title: Self-hosted worker reference | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/reference
source: sitemap
fetched_at: 2026-04-29T15:04:49.182357719-03:00
rendered_js: false
word_count: 816
summary: This document provides a comprehensive reference for configuring the oz-agent-worker daemon, including CLI flags and YAML configuration schemas for Docker, Kubernetes, and Direct backends.
tags:
    - oz-agent-worker
    - configuration
    - docker
    - kubernetes
    - cli-reference
    - backend-setup
    - daemon-config
category: reference
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Reference for the `oz-agent-worker` daemon: CLI flags and YAML config schema for all three [managed backends](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting#managed-architecture) — Docker, Kubernetes, and Direct.

---

## Worker flags

### Required

| Flag | Description |
|------|-------------|
| `--worker-id` | String identifying this worker. Passed to `--host` when routing tasks. Multiple workers can share the same ID for load balancing. |
| `--api-key` or `WARP_API_KEY` env var | Team API key for authentication. Docker: `-e WARP_API_KEY="..."`. Binary: `--api-key` or env var. |

### Optional

| Flag | Default | Description |
|------|---------|-------------|
| `--config-file` | — | Path to YAML config file. CLI flags take precedence over config file values. |
| `--backend` | `docker` | Backend type: `docker`, `kubernetes`, or `direct`. |
| `--log-level` | `info` | Log verbosity: `debug`, `info`, `warn`, `error`. |
| `--no-cleanup` | `false` | Keep task containers/Jobs/workspaces after execution for debugging. |
| `-v` / `--volumes` | — | Mount host directories into task containers (Docker only). Format: `HOST_PATH:CONTAINER_PATH` or `HOST_PATH:CONTAINER_PATH:MODE` (`ro`/`rw`). Repeatable. |
| `-e` / `--env` | — | Set environment variables for tasks. Format: `KEY=VALUE` or `KEY` (pass through from host). Repeatable. |
| `--max-concurrent-tasks` | `0` (unlimited) | Maximum concurrent tasks. Additional tasks wait until a slot is available. |
| `--idle-on-complete` | `45m` | How long to keep `oz` process alive after conversation finishes (e.g., `45m`, `10m`, `0s`). Set `0s` to disable. |

> [!warning]
> Worker IDs starting with `warp` are reserved and cannot be used.

### Example with all flags

```bash
oz-agent-worker \
  --worker-id "prod-runner-1" \
  --api-key "your-api-key" \
  --backend docker \
  --log-level debug \
  --no-cleanup \
  --volumes /host/data:/container/data:ro \
  --env MY_VAR=value \
  --env SECRET_VAR \
  --max-concurrent-tasks 5 \
  --idle-on-complete 45m
```

> [!warning]
> When running via Docker, there are two levels of `-e` flags: Docker's `-e` passes env vars to the **worker container**, while the worker's `-e` / `--env` passes env vars into **task containers**. Keep these distinct.

---

## Config file

For complex setups, use a YAML config file instead of (or in addition to) CLI flags via `--config-file`. CLI flags always take precedence.

### Docker backend config

```yaml
worker_id: prod-runner-1
cleanup: true
max_concurrent_tasks: 5
idle_on_complete: 45m
backend:
  docker:
    volumes:
      - /host/data:/container/data:ro
    environment:
      - name: MY_VAR
        value: value
      - name: SECRET_VAR  # inherits from host
```

### Kubernetes backend config

```yaml
worker_id: prod-runner-1
cleanup: true
max_concurrent_tasks: 5
idle_on_complete: 45m
backend:
  kubernetes:
    namespace: default
    default_image: ubuntu:22.04
    image_pull_policy: IfNotPresent
    preflight_image: busybox:1.36
    setup_command: ./setup.sh
    teardown_command: ./teardown.sh
    extra_labels:
      env: production
    extra_annotations:
      team: platform
    active_deadline_seconds: 3600
    workspace_size_limit: 10Gi
    unschedulable_timeout: 30s
    pod_template:
      # Raw Kubernetes PodSpec YAML
```

### Direct backend config

```yaml
worker_id: prod-runner-1
cleanup: true
max_concurrent_tasks: 5
idle_on_complete: 45m
backend:
  direct:
    workspace_root: /var/lib/oz/workspaces
    oz_path: /usr/local/bin/oz
    setup_command: ./setup.sh
    teardown_command: ./teardown.sh
    environment:
      - name: MY_VAR
        value: value
      - name: SECRET_VAR
```

### Config file fields

**Top-level:**

| Field | Default | Description |
|-------|---------|-------------|
| `worker_id` | — | Worker identifier (same as `--worker-id`). |
| `cleanup` | `true` | Clean up after tasks. Set `false` to keep for debugging. |
| `max_concurrent_tasks` | unlimited | Maximum concurrent tasks. |
| `idle_on_complete` | — | Duration to keep `oz` alive after task completion (e.g., `"45m"`, `"0s"`). |
| `backend` | — | Backend configuration block (one of `docker`, `kubernetes`, `direct`). |

**`backend.docker`:**

| Field | Description |
|-------|-------------|
| `volumes` | List of volume mounts (same as `-v` flag). |
| `environment` | List of env vars with `name` and optional `value`. Omit `value` to inherit from host. |

**`backend.kubernetes`:**

| Field | Default | Description |
|-------|---------|-------------|
| `namespace` | `default` | Kubernetes namespace for task Jobs. |
| `kubeconfig` | — | Path to explicit kubeconfig. Falls back to in-cluster config or default loading rules. |
| `default_image` | — | Default Docker image when run has no Warp environment. Precedence: Warp env image > `default_image` > `ubuntu:22.04`. |
| `image_pull_policy` | `IfNotPresent` | `Always`, `Never`, or `IfNotPresent`. |
| `preflight_image` | `busybox:1.36` | Image for startup preflight Job. |
| `setup_command` | — | Shell command to run before each task. |
| `teardown_command` | — | Shell command to run after each task. |
| `extra_labels` | — | Additional labels for task Jobs and Pods. |
| `extra_annotations` | — | Additional annotations for task Jobs and Pods. |
| `active_deadline_seconds` | — | Maximum lifetime for task Job. |
| `workspace_size_limit` | — | Size limit for workspace `emptyDir` volume (e.g., `10Gi`). |
| `unschedulable_timeout` | `30s` | Time before failing early when pod unschedulable. Set `0s` to disable. |
| `pod_template` | — | Raw Kubernetes PodSpec YAML merged at runtime. Define a container named `task` to customize it. |

**`backend.direct`:**

| Field | Default | Description |
|-------|---------|-------------|
| `workspace_root` | `/var/lib/oz/workspaces` | Directory for per-task workspaces. |
| `oz_path` | `oz` in PATH | Path to oz CLI binary. |
| `setup_command` | — | Shell command before each task. Receives `OZ_WORKSPACE_ROOT`, `OZ_RUN_ID`, `OZ_ENVIRONMENT_FILE`, `OZ_WORKER_BACKEND` as env vars. |
| `teardown_command` | — | Shell command after each task. |
| `environment` | — | List of env vars (same format as Docker backend). |

> [!info]
> Only one backend can be configured at a time. Specifying more than one is an error.

---

## Routing runs to self-hosted workers

Once a worker is running, route cloud agent runs with the `--host` flag or its equivalents. See [Routing runs to self-hosted workers](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting#routing-runs-to-self-hosted-workers) for examples across CLI, schedules, integrations, API, and web UI.

## Related pages

- [Managed: Docker](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/managed-docker) — Docker backend setup, connectivity, private registries.
- [Managed: Kubernetes](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/managed-kubernetes) — Kubernetes backend setup, Helm chart, pod template.
- [Environments](https://docs.warp.dev/agent-platform/cloud-agents/environments) — Define Docker image, repos, setup commands for task containers.

#oz-agent-worker #self-hosting #configuration
