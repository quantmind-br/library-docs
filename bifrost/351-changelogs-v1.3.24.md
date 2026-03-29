---
title: v1.3.24
url: https://docs.getbifrost.ai/changelogs/v1.3.24.md
source: llms
fetched_at: 2026-01-21T19:41:55.704923706-03:00
rendered_js: false
word_count: 200
summary: This document provides the changelog for Bifrost version 1.3.24, detailing core and framework updates, logging improvements, and installation instructions via NPX and Docker.
tags:
    - release-notes
    - changelog
    - bifrost
    - software-update
    - docker
    - npx
    - version-history
category: reference
---

# v1.3.24

> v1.3.24 changelog - 2025-11-11

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.24
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.24
    docker run -p 8080:8080 maximhq/bifrost:v1.3.24
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.24">
  * chore: update core version to 1.2.22 and framework version to 1.1.27
  * feat: Adds input message in logs table for easier navigation
</Update>

<Update label="Core" description="v1.3.24">
  * chore: Adds index to ChatAssistantMessageToolCall
  * fix: responses text output standardization to content blocks
</Update>

<Update label="Framework" description="v1.3.24">
  * chore: update core version to 1.2.22
</Update>

<Update label="governance" description="v1.3.24">
  * chore: update core version to 1.2.22 and framework version to 1.1.27
</Update>

<Update label="jsonparser" description="v1.3.24">
  * chore: update core version to 1.2.22 and framework version to 1.1.27
</Update>

<Update label="logging" description="v1.3.24">
  * chore: update core version to 1.2.22 and framework version to 1.1.27
</Update>

<Update label="maxim" description="v1.3.24">
  * chore: update core version to 1.2.22 and framework version to 1.1.27
</Update>

<Update label="mocker" description="v1.3.24">
  * chore: update core version to 1.2.22 and framework version to 1.1.27
</Update>

<Update label="otel" description="v1.3.24">
  * chore: update core version to 1.2.22 and framework version to 1.1.27
</Update>

<Update label="semanticcache" description="v1.3.24">
  * chore: update core version to 1.2.22 and framework version to 1.1.27
</Update>

<Update label="telemetry" description="v1.3.24">
  * chore: update core version to 1.2.22 and framework version to 1.1.27
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt