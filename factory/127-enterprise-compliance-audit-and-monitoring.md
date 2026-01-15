---
title: Compliance, Audit & Monitoring - Factory Documentation
url: https://docs.factory.ai/enterprise/compliance-audit-and-monitoring
source: sitemap
fetched_at: 2026-01-13T19:04:06.828347367-03:00
rendered_js: false
word_count: 522
summary: Explains how to integrate Droids into a security and compliance posture, detailing audit trails, OpenTelemetry telemetry, and configuration steps for regulatory adherence.
tags:
    - compliance
    - audit-logs
    - opentelemetry
    - security
    - siem-integration
    - droid-shield
    - regulatory
    - observability
category: guide
---

Security and compliance teams need clear answers to **who did what, when, where, and with which data**. This page explains how Droids fit into your compliance posture and how to integrate them with your existing monitoring and audit infrastructure.

* * *

## Certifications and Trust Center

Factory maintains an enterprise‑grade security and compliance program, including:

- **SOC 2**
- **ISO 27001**
- **ISO 42001**

Our **Trust Center** provides up‑to‑date reports, security architecture documentation, and sub‑processor lists. Use it as the primary reference for security and compliance reviews.

* * *

## Audit trails and events

There are two complementary sources of audit information:

1. **Factory‑side audit logs** (for cloud‑managed features).
2. **Customer‑side OTEL telemetry** emitted by Droid.

### Factory‑side audit logs (cloud‑managed)

When you use Factory’s hosted services, the control plane records key events such as:

- Authentication events and SSO/SCIM changes.
- Org and project configuration updates.
- Policy changes (model allow/deny lists, autonomy limits, Droid Shield settings, hooks configuration).
- Administrative actions in the web UI.

These logs can be exported via the Trust Center or integrations agreed upon in your enterprise engagement.

### Customer‑side OTEL telemetry

Droid emits OTEL metrics, traces, and logs that can serve as **fine‑grained audit data** inside your own systems, including:

- Session start and end events, tagged with user, team, environment, and project information.
- Tool usage events (which tools were invoked, how long they ran, and whether they succeeded).
- Command execution metadata, including risk classification and outcome.
- Code modification events (which files and repositories were changed).

You control how long these signals are retained and how they are correlated with other systems such as CI/CD pipelines, SIEMs, and case management tools.

* * *

## OpenTelemetry schema and collectors

Factory’s OTEL support is designed to integrate with existing observability tooling. At a high level, telemetry includes:

- **Resource attributes** – describing the environment, service, org, team, and user.
- **Metrics** – counters and histograms for sessions, LLM usage, tools, and errors.
- **Traces and spans** – describing the lifecycle of sessions and automated runs.
- **Logs** – structured events for key actions and errors.

You can deploy OTEL collectors that:

- Receive OTLP data from Droid.
- Enrich or redact attributes based on your own policies.
- Forward telemetry to multiple destinations (for example, Prometheus + Loki, Datadog, Splunk, or S3).

This architecture keeps **ownership of telemetry firmly in your hands**, even when using Factory’s cloud‑managed features. For more details on the metrics and traces useful for cost and productivity analysis, see [Usage, Cost & Productivity Analytics](https://docs.factory.ai/enterprise/usage-cost-and-analytics).

* * *

## Regulatory and industry use cases

Factory is designed to support organizations operating under strict regulatory regimes. While implementation details differ, common patterns include:

* * *

## Deployment and configuration for compliance teams

To integrate Droid into your compliance and monitoring stack:

1. **Decide on deployment pattern** – cloud‑managed, hybrid, or fully airgapped.
2. **Define model and gateway policies** – which providers and gateways are allowed, and where.
3. **Configure OTEL collectors and destinations** – ensure all Droid telemetry flows into your SIEM and observability tools.
4. **Set up hooks and Droid Shield** – enforce DLP, approval workflows, and environment‑specific controls.
5. **Document policies and mappings** – connect Droid controls to your internal control framework and regulatory obligations.

Most of this configuration is expressed via the hierarchical settings system described in [Hierarchical Settings & Org Control](https://docs.factory.ai/enterprise/hierarchical-settings-and-org-control).