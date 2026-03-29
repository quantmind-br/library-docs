---
title: Release Cycle | liteLLM
url: https://docs.litellm.ai/docs/proxy/release_cycle
source: sitemap
fetched_at: 2026-01-21T19:53:29.850184445-03:00
rendered_js: false
word_count: 125
summary: This document outlines the release cycle and versioning strategy for LiteLLM Proxy, defining the criteria for nightly, release candidate, and stable versions.
tags:
    - release-cycle
    - versioning
    - litellm-proxy
    - software-maintenance
    - release-policy
    - stable-releases
category: reference
---

Litellm Proxy has the following release cycle:

- `v1.x.x-nightly`: These are releases which pass ci/cd.
- `v1.x.x.rc`: These are releases which pass ci/cd + [manual review](https://github.com/BerriAI/litellm/discussions/8495#discussioncomment-12180711).
- `v1.x.x:main-stable`: These are releases which pass ci/cd + manual review + 3 days of production testing.

In production, we recommend using the latest `v1.x.x:main-stable` release.

Follow our release notes [here](https://github.com/BerriAI/litellm/releases).

## FAQ[​](#faq "Direct link to FAQ")

### Is there a release schedule for LiteLLM stable release?[​](#is-there-a-release-schedule-for-litellm-stable-release "Direct link to Is there a release schedule for LiteLLM stable release?")

Stable releases come out every week (typically Sunday)

### What is considered a 'minor' bump vs. 'patch' bump?[​](#what-is-considered-a-minor-bump-vs-patch-bump "Direct link to What is considered a 'minor' bump vs. 'patch' bump?")

- 'patch' bumps: extremely minor addition that doesn't affect any existing functionality or add any user-facing features. (e.g. a 'created\_at' column in a database table)
- 'minor' bumps: add a new feature or a new database table that is backward compatible.
- 'major' bumps: break backward compatibility.