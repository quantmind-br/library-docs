---
title: v1.3.0-prerelease5
url: https://docs.getbifrost.ai/changelogs/v1.3.0-prerelease5.md
source: llms
fetched_at: 2026-01-21T19:41:30.864138076-03:00
rendered_js: false
word_count: 179
summary: This document outlines the changes and updates included in the v1.3.0-prerelease5 release of Bifrost, specifically detailing bug fixes for Anthropic tool aggregation and new logging features.
tags:
    - release-notes
    - changelog
    - bifrost
    - anthropic
    - logging
    - version-update
category: reference
---

# v1.3.0-prerelease5

> v1.3.0-prerelease5 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.0-prerelease5
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.0-prerelease5
    docker run -p 8080:8080 maximhq/bifrost:v1.3.0-prerelease5
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.0-prerelease5">
  * Fix: Anthropic tool results aggregation logic (core 1.2.4)
  * Feat: Raw response saved in logs (framework 1.1.4)
</Update>

<Update label="Core" description="v1.3.0-prerelease5">
  * Fix: Anthropic tool results aggregation logic.
</Update>

<Update label="Framework" description="v1.3.0-prerelease5">
  * Feat: Raw response saved in logs.
  * Upgrade dependency: core to 1.2.4
</Update>

<Update label="governance" description="v1.3.0-prerelease5">
  * Chore: using core 1.2.4 and framework 1.1.4
</Update>

<Update label="jsonparser" description="v1.3.0-prerelease5">
  * Upgrade dependency: core to 1.2.4 and framework to 1.1.4
</Update>

<Update label="logging" description="v1.3.0-prerelease5">
  * Feat: Raw response saved in logs.
  * Upgrade dependency: core to 1.2.4 and framework to 1.1.4
</Update>

<Update label="maxim" description="v1.3.0-prerelease5">
  * Upgrade dependency: core to 1.2.4 and framework to 1.1.4
</Update>

<Update label="mocker" description="v1.3.0-prerelease5">
  * Upgrade dependency: core to 1.2.4 and framework to 1.1.4
</Update>

<Update label="otel" description="v1.3.0-prerelease5">
  * Upgrade dependency: core to 1.2.4 and framework to 1.1.4
</Update>

<Update label="semanticcache" description="v1.3.0-prerelease5">
  * Upgrade dependency: core to 1.2.4 and framework to 1.1.4
</Update>

<Update label="telemetry" description="v1.3.0-prerelease5">
  * Upgrade dependency: core to 1.2.4 and framework to 1.1.4
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt