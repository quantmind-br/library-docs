---
title: Security and networking | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/security-and-networking
source: sitemap
fetched_at: 2026-04-29T15:04:49.962613589-03:00
rendered_js: false
word_count: 596
summary: This document outlines the security architecture, network egress requirements, and backend-specific considerations for self-hosting Warp workers on various infrastructure types.
tags:
    - self-hosting
    - security-architecture
    - network-egress
    - infrastructure-security
    - kubernetes-security
    - docker-security
    - data-privacy
category: concept
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Self-hosting uses a split-plane architecture. This page summarizes the data model, network egress requirements, and backend-specific security considerations.

> [!info]
> Applies to both [managed](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting#managed-architecture) and [unmanaged](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting/unmanaged) architectures. Backend-specific notes call out Docker-, Kubernetes-, and Direct-only considerations.

## Data boundaries

**Stored and executed only on your infrastructure:**
- Repository clones and source files
- Build artifacts and compiled outputs
- Runtime secrets and environment variables
- Container filesystem state (managed) or host workspace (Direct/unmanaged)

**Routes through Warp's backend** (under [ZDR](https://docs.warp.dev/enterprise/security-and-compliance/security-overview#zero-data-retention-zdr)):
- Orchestration metadata (task status, lifecycle events)
- Session transcripts (agent-generated summaries of code context, file contents, command output)
- LLM inference requests and responses

> [!info]
> While repositories stay on your infrastructure, code content appears in session transcripts and LLM prompts. All data routed through Warp's backend is covered by [ZDR](https://docs.warp.dev/enterprise/security-and-compliance/security-overview#zero-data-retention-zdr)—Warp does not persistently store source code or use it for model training.

## Network requirements

Self-hosted Oz agents **do not require any network ingress**. They require outbound (egress) access:

| Service | Port | Required for |
|---------|------|--------------|
| `app.warp.dev` | 443 | All architectures |
| `rtc.app.warp.dev` | 443 | All architectures |
| `sessions.app.warp.dev` | 443 | All architectures |
| `oz.warp.dev` | 443 | Managed architecture only |
| Docker Hub | 443 | Managed architecture only (pulling task images) |
| `github.com` | 443 | Managed architecture only (GitHub repo access in environments) |
| Linux package repos | 443 | Managed architecture only (if base image lacks Git) |

> [!info]
> All traffic uses HTTPS (port 443). No inbound ports need to be opened.

## Backend-specific security considerations

### Docker backend

- **Docker socket access** – worker requires access to Docker daemon via `/var/run/docker.sock`. Ensure appropriate access controls.
- **Volume mounts** – be mindful of host paths exposed to task containers with `-v`/`--volumes`.
- **Task isolation** – each task runs in its own container. Containers removed after execution by default (disable with `--no-cleanup` for debugging).

### Kubernetes backend

- **Kubernetes RBAC** – worker needs namespaced permissions to create, get, list, watch, delete Jobs and Pods. Helm chart creates minimal Role/RoleBinding scoped to single namespace.
- **Service accounts** – worker Deployment's ServiceAccount is separate from optional task Job `serviceAccountName`. Scope each appropriately.
- **API key management** – store `WARP_API_KEY` in a Kubernetes Secret. Avoid hardcoding. Use CSI Secrets Store Driver or similar for external secrets managers (Vault, AWS Secrets Manager, GCP Secret Manager).
- **Task isolation** – each task runs as separate Kubernetes Job/Pod. Jobs removed after execution by default.

### Direct backend

- **Shared host kernel** – no container-level isolation. Each task runs in isolated workspace directory but shares host OS and kernel.
- **Minimal environment by default** – tasks start with minimal environment (`HOME`, `TMPDIR`, `PATH` only). `WARP_API_KEY` not passed to tasks unless explicitly configured.
- **Workspace cleanup** – workspaces under `workspace_root` removed after execution by default.

### Unmanaged

- **Host inheritance** – agents inherit host's network access, tools, and credentials. If host has VPN or internal service access, agent will too.
- **Kubernetes pod isolation** – evaluate pod security policies, network policies, RBAC settings based on your organization's requirements.

## VPN and on-premises access

Since self-hosted agents run on your infrastructure, they inherit your network access—reaching services behind VPNs, self-hosted GitLab/Bitbucket, databases, and internal resources. See [GitLab](https://docs.warp.dev/agent-platform/cloud-agents/integrations/gitlab) and [Bitbucket](https://docs.warp.dev/agent-platform/cloud-agents/integrations/bitbucket) setup guides.

## LLM inference and BYOLLM

LLM inference routes through Warp's backend under [ZDR](https://docs.warp.dev/enterprise/security-and-compliance/security-overview#zero-data-retention-zdr) agreements. Enterprise teams can use [BYOLLM](https://docs.warp.dev/enterprise/enterprise-features/bring-your-own-llm) to route inference through their own cloud provider accounts (currently local agents only; cloud agent support coming).

## Related pages

Last updated 21 hours ago
