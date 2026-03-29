---
title: v1.2.24
url: https://docs.getbifrost.ai/changelogs/v1.2.24.md
source: llms
fetched_at: 2026-01-21T19:41:22.897888705-03:00
rendered_js: false
word_count: 163
summary: This document details the updates and bug fixes for Bifrost version 1.2.24, including component upgrades and UI improvements. It provides instructions for pulling and running the specific version via NPX and Docker.
tags:
    - release-notes
    - changelog
    - bifrost
    - version-update
    - bug-fixes
    - docker
category: other
---

# v1.2.24

> v1.2.24 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.2.24
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.2.24
    docker run -p 8080:8080 maximhq/bifrost:v1.2.24
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.2.24">
  * Fix: Adds `Base URL` input in custom provider creation dialog.
  * Fix: Fixes `x` button getting hidden behind dialog header.
</Update>

<Update label="Core" description="v1.2.24">
  * Fix: Updates token calculation for streaming responses. #520
</Update>

<Update label="Framework" description="v1.2.24">
  * upgrade: core upgrades to 1.1.38
</Update>

<Update label="governance" description="v1.2.24">
  * upgrade: core to 1.1.38
  * upgrade: framework to 1.0.24
</Update>

<Update label="jsonparser" description="v1.2.24">
  * upgrade: core to 1.1.38
  * upgrade: framework to 1.0.24
</Update>

<Update label="logging" description="v1.2.24">
  * fix: fixes error logging for streaming and non-streaming responses.
  * upgrade: core to 1.1.38
  * upgrade: framework to 1.0.24
</Update>

<Update label="maxim" description="v1.2.24">
  * upgrade: core to 1.1.38
  * upgrade: framework to 1.0.24
</Update>

<Update label="mocker" description="v1.2.24">
  * upgrade: core to 1.1.38
  * upgrade: framework to 1.0.24
</Update>

<Update label="semanticcache" description="v1.2.24">
  * upgrade: core to 1.1.38
  * upgrade: framework to 1.0.24
</Update>

<Update label="telemetry" description="v1.2.24">
  * upgrade: core to 1.1.38
  * upgrade: framework to 1.0.24
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt