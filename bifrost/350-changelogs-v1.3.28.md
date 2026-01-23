---
title: v1.3.28
url: https://docs.getbifrost.ai/changelogs/v1.3.28.md
source: llms
fetched_at: 2026-01-21T19:42:01.503364388-03:00
rendered_js: false
word_count: 142
summary: This document outlines the v1.3.28 release notes for Bifrost, detailing performance optimizations for log processing on SQLite and framework updates across various internal modules.
tags:
    - changelog
    - release-notes
    - bifrost
    - performance-optimization
    - sqlite
    - log-management
    - version-update
category: reference
---

# v1.3.28

> v1.3.28 changelog - 2025-11-18

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.28
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.28
    docker run -p 8080:8080 maximhq/bifrost:v1.3.28
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.28">
  feat: Improves log page loading performance for millions of logs stored on sqlite
</Update>

<Update label="Framework" description="1.1.31">
  feat: splits logs APIs into `getStats` and `getLogs` to improve speed for sqlite
</Update>

<Update label="governance" description="1.3.32">
  chore: update framework version to 1.1.31
</Update>

<Update label="jsonparser" description="1.3.32">
  chore: update framework version to 1.1.31
</Update>

<Update label="logging" description="1.3.32">
  chore: update framework version to 1.1.31
</Update>

<Update label="maxim" description="1.4.31">
  chore: update framework version to 1.1.31
</Update>

<Update label="mocker" description="1.3.31">
  chore: update framework version to 1.1.31
</Update>

<Update label="otel" description="1.0.31">
  chore: update framework version to 1.1.31
</Update>

<Update label="semanticcache" description="1.3.31">
  chore: update framework version to 1.1.31
</Update>

<Update label="telemetry" description="1.3.31">
  chore: update framework version to 1.1.31
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt