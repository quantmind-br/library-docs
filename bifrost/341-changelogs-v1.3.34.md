---
title: v1.3.34
url: https://docs.getbifrost.ai/changelogs/v1.3.34.md
source: llms
fetched_at: 2026-01-21T19:42:09.89083236-03:00
rendered_js: false
word_count: 154
summary: This document outlines the release notes and changelog for Bifrost version 1.3.34, detailing feature updates, bug fixes, and dependency upgrades across various components.
tags:
    - release-notes
    - changelog
    - bifrost
    - version-update
    - software-maintenance
category: reference
---

# v1.3.34

> v1.3.34 changelog - 2025-11-21

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.34
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.34
    docker run -p 8080:8080 maximhq/bifrost:v1.3.34
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.34">
  * feat: Log view is enabled even if config\_store is disabled
  * fix: Add missing cache and batch pricing columns to ensure we compute costs for those operations accurately.
</Update>

<Update label="Framework" description="1.1.37">
  hotfix: Adds missing batch and cache token pricing columns in config\_store
</Update>

<Update label="governance" description="1.3.38">
  * chore: upgrades framework version to 1.1.37
</Update>

<Update label="jsonparser" description="1.3.38">
  * chore: upgrades framework version to 1.1.37
</Update>

<Update label="logging" description="1.3.38">
  * chore: upgrades framework version to 1.1.37
</Update>

<Update label="maxim" description="1.4.37">
  * chore: upgrades framework version to 1.1.37
</Update>

<Update label="mocker" description="1.3.37">
  * chore: upgrades framework version to 1.1.37
</Update>

<Update label="otel" description="1.0.37">
  * chore: upgrades framework version to 1.1.37
</Update>

<Update label="semanticcache" description="1.3.37">
  * chore: upgrades framework version to 1.1.37
</Update>

<Update label="telemetry" description="1.3.37">
  * chore: upgrades framework version to 1.1.37
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt