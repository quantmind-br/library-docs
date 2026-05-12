---
title: 'Advanced: Incremental Snapshots'
url: https://docs.fireworks.ai/fine-tuning/rl-rollout-delta-checkpoints
source: sitemap
fetched_at: 2026-04-27T20:15:29.818895611-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - rl-rollouts
    - hot-load
    - incremental-snapshot
    - byot
category: reference
word_count: 126
---
# Advanced: Incremental Snapshots

Use incremental snapshots between full snapshots to reduce upload and load time during RL training.

> [!warning]
> **Early Access Feature.** Contact Fireworks to enable external bucket hot-load on your account before using non-`FW_HOSTED` storage.

Most readers should follow the linear workflow in [[047-fine-tuning-rl-rollout-integration]] instead of this page.

## Cadence

- **First snapshot:** full.
- **Every 20th or 30th snapshot:** full.
- **All other snapshots:** incremental against the currently loaded snapshot.

## Rules

- Give every snapshot a new `identity`.
- Point `incremental_snapshot_metadata.previous_snapshot_identity` at the previous snapshot in the chain.
- Use `arc_v2` for `incremental_snapshot_metadata.compression_format`.
- Upload the incremental snapshot under the normal snapshot directory for the new `identity`.
- If an incremental hot-load fails, fall back to a new full snapshot.