---
title: Enterprise with Droids - Factory Documentation
url: https://docs.factory.ai/enterprise
source: sitemap
fetched_at: 2026-01-13T19:04:06.6713927-03:00
rendered_js: false
word_count: 560
summary: This document outlines the deployment strategies, security controls, and governance features of the Droid agent runtime for high-security enterprise environments.
tags:
    - enterprise
    - security
    - deployment
    - airgap
    - observability
    - compliance
    - governance
    - access-control
category: guide
---

Factory’s enterprise platform is designed for the **highest‑security customers**—systemically important banks, governments, healthcare, national security, and other regulated organizations. Instead of forcing you into a single cloud IDE, Droid is a **CLI and agent runtime that runs anywhere**:

- On developer laptops, in any terminal or IDE
- In CI/CD pipelines (GitHub, GitLab, internal runners)
- In VMs, Kubernetes clusters, and hardened devcontainers
- In **fully airgapped environments** with no outbound internet access

This section explains how to deploy Droid safely, govern which models and tools it can use, and observe its behavior at enterprise scale.

* * *

## What this section covers

Use these pages together as your enterprise playbook for Droids:

* * *

## Enterprise foundations

### Multi‑deployment by design

Factory supports three deployment patterns for Droid, all built on the same core binary and configuration model:

1. **Cloud‑managed** – Droid runs on developer machines and CI but uses Factory’s cloud for coordination and optional analytics. Models are either Factory‑brokered or brought by you.
2. **Hybrid enterprise** – Droid runs entirely in your infrastructure (VMs, CI runners, containers), optionally connecting to Factory cloud for UX while all LLMs and telemetry terminate inside your network.
3. **Fully airgapped** – Droid runs in a network with **no outbound internet access**. Models and OTEL collectors are hosted entirely inside this environment; Factory never receives traffic.

You can start in cloud‑managed mode, then migrate critical workloads to hybrid or airgapped environments without changing how developers talk to Droid.

### Hierarchical control, not per‑device drift

Enterprise policy is expressed through a **hierarchical settings model**:

- **Org** → global defaults and hard security policies
- **Project** → repo‑level settings committed to `.factory/`
- **Folder** → narrower team or subsystem overrides inside a repo
- **User** → personal preferences only where higher levels are silent

Higher levels **cannot be overridden** by lower ones. Org and project settings extend downward; users can opt into stricter controls but never weaken them. This hierarchy governs models, tools, MCP servers, droids, commands, autonomy levels, and telemetry destinations. Learn more in [Hierarchical Settings & Org Control](https://docs.factory.ai/enterprise/hierarchical-settings-and-org-control).

### Defense‑in‑depth agent safety

LLMs are probabilistic; Factory treats them as powerful but untrusted components. Droid’s safety story combines:

- **Deterministic controls** – command risk classification, allow/deny lists, file and repo protections, and sandbox boundaries
- **Droid Shield** – secret scanning and DLP‑style checks across prompts, files, and commands
- **Hooks** – programmable enforcement points (pre‑prompt, pre‑tool, pre‑command, pre‑git, post‑edit) to integrate with your own security systems
- **Sandboxed runtimes** – running Droid inside devcontainers and hardened VMs for high‑risk work

These layers are independent of which LLM or IDE a developer prefers.

### OTEL‑native observability

All serious enterprise deployments need to answer: *“What are agents doing, where, and at what cost?”* Droid emits **OpenTelemetry metrics, traces, and logs** so you can:

- Send telemetry directly to existing collectors (Prometheus, Datadog, Splunk, Jaeger, etc.)
- Track sessions, LLM usage, code edits, tool invocations, and errors per org/team/user
- Correlate Droid activity with SDLC metrics you already use

Factory’s own cloud analytics are **optional**; high‑security customers can route all telemetry exclusively to their own infrastructure. See [Usage, Cost & Productivity Analytics](https://docs.factory.ai/enterprise/usage-cost-and-analytics) and [Compliance, Audit & Monitoring](https://docs.factory.ai/enterprise/compliance-audit-and-monitoring).

* * *

## Trust & compliance

Factory maintains a security and compliance posture suitable for the most demanding organizations:

- **SOC 2**
- **ISO 27001**
- **ISO 42001**

You can find the latest reports, sub‑processor lists, and security architecture details in our **Trust Center**. For a deeper dive into how Droid fits your regulatory and audit requirements, start with [Compliance, Audit & Monitoring](https://docs.factory.ai/enterprise/compliance-audit-and-monitoring).