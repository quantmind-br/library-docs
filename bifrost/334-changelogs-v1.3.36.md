---
title: v1.3.36
url: https://docs.getbifrost.ai/changelogs/v1.3.36.md
source: llms
fetched_at: 2026-01-21T19:42:11.776427035-03:00
rendered_js: false
word_count: 137
summary: This document provides the changelog and release notes for Bifrost version 1.3.36, detailing new features, bug fixes, and module-specific framework updates.
tags:
    - changelog
    - release-notes
    - bifrost
    - bug-fixes
    - version-update
    - opus-support
category: reference
---

# v1.3.36

> v1.3.36 changelog - 2025-11-25

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.36
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.36
    docker run -p 8080:8080 maximhq/bifrost:v1.3.36
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.36">
  * feat: opus 4.5 is supported
  * chore: changelog structure update
  * fix: race conditions in stream accumulator
</Update>

<Update label="Framework" description="1.1.39">
  * fix: Fixes race condition in accumulator
</Update>

<Update label="governance" description="1.3.40">
  * chore: upgrades framework version to 1.1.39
</Update>

<Update label="jsonparser" description="1.3.40">
  * chore: upgrades framework version to 1.1.39
</Update>

<Update label="logging" description="1.3.40">
  * chore: upgrades framework version to 1.1.39
</Update>

<Update label="maxim" description="1.4.39">
  * chore: upgrades framework version to 1.1.39
</Update>

<Update label="mocker" description="1.3.39">
  * chore: upgrades framework version to 1.1.39
</Update>

<Update label="otel" description="1.0.39">
  * chore: upgrades framework version to 1.1.39
</Update>

<Update label="semanticcache" description="1.3.39">
  * chore: upgrades framework version to 1.1.39
</Update>

<Update label="telemetry" description="1.3.39">
  * chore: upgrades framework version to 1.1.39
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt