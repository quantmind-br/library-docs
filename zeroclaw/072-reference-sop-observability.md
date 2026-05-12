---
title: SOP Observability & Audit
date: 2026-05-05T00:00:00Z
url: https://github.com/openagen/zeroclaw/blob/master/docs/reference/sop/observability.md
source: git
fetched_at: 2026-05-02T14:52:03.555068883-03:00
rendered_js: false
word_count: 177
summary: This document outlines the observability and audit mechanisms for SOP execution, detailing how audit logs are persisted and how operators can inspect run states and metrics.
tags:
    - sop
    - observability
    - audit-logging
    - run-state
    - metrics
    - cli-tools
category: guide
optimized: true
optimized_at: 2026-05-05T00:00:00Z
---
# SOP Observability & Audit

Covers where SOP execution evidence is stored and how to inspect it.

## 1. Audit Persistence

SOP audit entries persisted via `SopAuditLogger` into configured Memory backend, category `sop`.

Common key patterns:

- `sop_run_{run_id}` — run snapshot (start + completion updates)
- `sop_step_{run_id}_{step_number}` — per-step result
- `sop_approval_{run_id}_{step_number}` — operator approval record
- `sop_timeout_approve_{run_id}_{step_number}` — timeout auto-approval record
- `sop_gate_decision_{gate_id}_{timestamp_ms}` — gate evaluator decision record (when `ampersona-gates` enabled)
- `sop_phase_state` — persisted trust-phase state snapshot (when `ampersona-gates` enabled)

## 2. Inspection Paths

### 2.1 Definition-level CLI

```bash
zeroclaw sop list
zeroclaw sop validate [name]
zeroclaw sop show <name>
```

### 2.2 Runtime run-state tools

SOP run state queried from in-agent tools:

- `sop_status` — active/finished runs and optional metrics
- `sop_status` with `include_gate_status: true` — trust phase and gate evaluator state
- `sop_approve` — approve waiting run step
- `sop_advance` — submit step result and move run forward

## 3. Metrics

- `/metrics` exposes observer metrics when `[observability] backend = "prometheus"`
- Current exported names are `zeroclaw_*` families (general runtime metrics)
- SOP-specific aggregates available through `sop_status` with `include_metrics: true`

#sop #observability #audit-logging #run-state #metrics #cli-tools
