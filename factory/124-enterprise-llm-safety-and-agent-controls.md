---
title: LLM Safety & Agent Controls - Factory Documentation
url: https://docs.factory.ai/enterprise/llm-safety-and-agent-controls
source: sitemap
fetched_at: 2026-01-13T19:04:02.425123324-03:00
rendered_js: false
word_count: 742
summary: This document outlines the multi-layered security architecture for the Droid AI agent, detailing deterministic controls, command risk classification, allow/deny lists, secret scanning, programmable hooks, and sandboxing strategies to ensure safe operation in enterprise environments.
tags:
    - security-architecture
    - llm-safety
    - access-control
    - droid-agent
    - enterprise-compliance
    - sandboxing
    - risk-management
    - data-loss-prevention
category: guide
---

Factory treats LLMs as powerful but untrusted components. Droid’s safety model combines **deterministic controls, programmable hooks, and sandboxed runtimes** so that even frontier models can operate safely in high‑security environments.

* * *

## Two layers of safety

We differentiate between:

1. **Deterministic controls** – hard boundaries that do not depend on model behavior.
2. **LLM steering** – prompts and context that guide models toward better behavior without providing guarantees.

Enterprise security should be built primarily on deterministic controls; steering is a quality‑of‑life improvement.

* * *

## Command risk classification

Every shell command Droid proposes is classified into a **risk level** based on patterns and context (for example, file deletion, network access, package installation, database access). Typical levels include:

- **Low risk** – read‑only commands and local diagnostics (for example, `ls`, `cat`, `git status`).
- **Medium risk** – commands that modify code or install dependencies (for example, `npm install`, `go test ./...`).
- **High risk** – commands that delete data, change system configuration, or interact with sensitive resources (for example, `rm -rf`, `kubectl delete`, `psql` against production).

Org and project policies can map risk levels to behavior, such as:

- Always allow low‑risk commands.
- Require user approval for medium‑risk commands.
- Block high‑risk commands entirely or only allow them in specific environments (for example, isolated devcontainers).

Risk information is also emitted via OTEL so security teams can monitor how often high‑risk commands are proposed or attempted.

* * *

## Command allowlists and denylists

Admins can define **global and project‑specific allow/deny lists** in hierarchical settings:

- **Deny lists** – patterns for commands that are never permitted (for example, `rm -rf`, `sudo *`, `curl *://sensitive-endpoint`).
- **Allow lists** – specific commands or patterns that can run without additional approval in certain environments.

Because settings are extension‑only:

- Org‑level denies and allows **cannot be removed** by projects or users.
- Projects can add additional allows or denies within their repos.
- Users cannot weaken the policy; they can only choose stricter personal defaults.

This keeps command policy consistent across thousands of machines while still allowing local specialization.

* * *

## Droid Shield: secret scanning and DLP

**Droid Shield** adds a dedicated layer of protection for secrets and sensitive content. When enabled, Droid Shield can:

- Scan **files** before they are read or edited.
- Scan **prompts** before they are sent to models.
- Scan **commands** before they are executed.

It detects patterns such as:

- API tokens and access keys.
- Passwords and database connection strings.
- Private keys and certificates.
- Organization‑specific identifiers (configurable patterns).

Based on policy, Droid Shield can:

- Block the operation entirely.
- Redact the sensitive portions before continuing.
- Emit OTEL events and logs for security review.
- Call out to a **customer DLP service** via hooks for deeper analysis.

Org admins configure Droid Shield at the org and project levels; users cannot disable it where it is enforced.

* * *

## Hooks for enforcement and logging

Hooks are Droid’s **programmable safety and observability interface**. They allow you to run your own code at key points in the agent loop. Common hook points include:

- **Before prompt submission** – inspect prompts for secrets, PII, or policy violations.
- **Before file reads or writes** – block or redact access to sensitive files.
- **Before command execution** – enforce approval workflows or block dangerous commands.
- **Before git operations** – prevent unauthorized `git push` or interactions with restricted branches.
- **After code generation or edits** – run linters, security scanners, or internal compliance checks.

Typical enterprise use cases:

See [Hooks Guide](https://docs.factory.ai/cli/configuration/hooks-guide) and [Hooks Reference](https://docs.factory.ai/reference/hooks-reference) for implementation details and examples.

* * *

## Sandboxing with containers and VMs

Running Droid in **sandboxed devcontainers and VMs** lets you safely grant more autonomy where it is useful, without exposing production systems. Recommended patterns:

- Use Docker/Podman devcontainers with restricted filesystem mounts and network egress.
- Run Droid with higher autonomy only inside containers or VMs that **do not have direct access to production databases or secrets**.
- Use separate credentials and environment variables for sandboxed versus production‑adjacent environments.

In OTEL telemetry, you can tag sessions by environment (for example, `environment.type=local|ci|sandbox`) to build environment‑specific dashboards and alerts.

* * *

## Steering models toward safe behavior

While deterministic controls are the foundation, **LLM steering** improves quality and reduces how often dangerous actions are even proposed. Org and project settings can define:

- **Rules and instructions** – security guidelines, coding standards, and organization‑specific instructions that apply to every request.
- **Standardized commands and workflows** – shared commands (for example, `/security-review`, `/migrate-service`) that bake in safe patterns.
- **Context enrichment** – MCP servers that expose documentation, runbooks, and internal APIs so models have accurate information instead of guessing.

Because these are instructions, not enforcement, they complement rather than replace the hard boundaries described above.