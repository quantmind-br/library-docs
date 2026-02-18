---
title: README
url: https://github.com/zeroclaw-labs/zeroclaw/blob/main/docs/operations/README.md
source: git
fetched_at: 2026-02-18T07:18:42.06242-03:00
rendered_js: false
word_count: 79
summary: This document provides a collection of resources and standard operating procedures for deploying, maintaining, and troubleshooting ZeroClaw in production-like environments.
tags:
    - zeroclaw
    - operations
    - deployment
    - troubleshooting
    - maintenance
    - runbook
category: guide
---

# Operations & Deployment Docs

For operators running ZeroClaw in persistent or production-like environments.

## Core Operations

- Day-2 runbook: [../operations-runbook.md](../operations-runbook.md)
- Troubleshooting matrix: [../troubleshooting.md](../troubleshooting.md)
- Safe network/gateway deployment: [../network-deployment.md](../network-deployment.md)
- Mattermost setup (channel-specific): [../mattermost-setup.md](../mattermost-setup.md)

## Common Flow

1. Validate runtime (`status`, `doctor`, `channel doctor`)
2. Apply one config change at a time
3. Restart service/daemon
4. Verify channel and gateway health
5. Roll back quickly if behavior regresses

## Related

- Config reference: [../config-reference.md](../config-reference.md)
- Security collection: [../security/README.md](../security/README.md)
