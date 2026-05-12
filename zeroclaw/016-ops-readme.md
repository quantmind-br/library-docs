---
optimized: true
optimized_at: 2026-05-05T00:00:00Z
title: Operations & Deployment Docs
tags:
  - zeroclaw
  - operations-runbook
  - production-deployment
  - troubleshooting
  - system-maintenance
  - service-management
category: guide
word_count: 76
---
# Operations & Deployment Docs

For operators running ZeroClaw in persistent or production-like environments.

## Core Operations

- [[./operations-runbook|Day-2 runbook]]
- [[../contributing/release-process|Release runbook]]
- [[./troubleshooting|Troubleshooting matrix]]
- [[./network-deployment|Safe network/gateway deployment]]
- [[../setup-guides/mattermost-setup|Mattermost setup (channel-specific)]]

## Common Flow

1. Validate runtime (`status`, `doctor`, `channel doctor`)
2. Apply one config change at a time
3. Restart service/daemon
4. Verify channel and gateway health
5. Roll back quickly if behavior regresses

## Related

- [[../reference/api/config-reference|Config reference]]
- [[../security/README|Security collection]]
