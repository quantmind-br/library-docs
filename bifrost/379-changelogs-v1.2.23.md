---
title: v1.2.23
url: https://docs.getbifrost.ai/changelogs/v1.2.23.md
source: llms
fetched_at: 2026-01-21T19:41:22.90052484-03:00
rendered_js: false
word_count: 153
summary: This document details the release notes and changelog for version 1.2.23 of the Bifrost platform, including bug fixes and dependency updates across multiple modules.
tags:
    - changelog
    - release-notes
    - bifrost
    - software-update
    - bug-fixes
    - version-1-2-23
category: reference
---

# v1.2.23

> v1.2.23 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.2.23
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.2.23
    docker run -p 8080:8080 maximhq/bifrost:v1.2.23
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.2.23">
  * Fix: Fixes editing experience of weight for API keys.
</Update>

<Update label="Core" description="v1.2.23">
  * Fix: Updates token calculation for streaming responses. #520
</Update>

<Update label="Framework" description="v1.2.23">
  * upgrade: core upgrades to 1.1.38
</Update>

<Update label="governance" description="v1.2.23">
  * upgrade: core to 1.1.38
  * upgrade: framework to 1.0.24
</Update>

<Update label="jsonparser" description="v1.2.23">
  * upgrade: core to 1.1.38
  * upgrade: framework to 1.0.24
</Update>

<Update label="logging" description="v1.2.23">
  * fix: fixes error logging for streaming and non-streaming responses.
  * upgrade: core to 1.1.38
  * upgrade: framework to 1.0.24
</Update>

<Update label="maxim" description="v1.2.23">
  * upgrade: core to 1.1.38
  * upgrade: framework to 1.0.24
</Update>

<Update label="mocker" description="v1.2.23">
  * upgrade: core to 1.1.38
  * upgrade: framework to 1.0.24
</Update>

<Update label="semanticcache" description="v1.2.23">
  * upgrade: core to 1.1.38
  * upgrade: framework to 1.0.24
</Update>

<Update label="telemetry" description="v1.2.23">
  * upgrade: core to 1.1.38
  * upgrade: framework to 1.0.24
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt