---
title: v1.2.22
url: https://docs.getbifrost.ai/changelogs/v1.2.22.md
source: llms
fetched_at: 2026-01-21T19:41:22.64354558-03:00
rendered_js: false
word_count: 184
summary: This document provides the release notes for Bifrost version 1.2.22, detailing bug fixes for streaming responses and UI components alongside various module dependency upgrades.
tags:
    - release-notes
    - changelog
    - bifrost
    - bug-fixes
    - version-update
    - streaming-responses
category: other
---

# v1.2.22

> v1.2.22 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.2.22
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.2.22
    docker run -p 8080:8080 maximhq/bifrost:v1.2.22
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.2.22">
  * Fix: Users can now delete custom providers from the UI
  * Fix: Token count no longer displays as N/A in certain streaming response cases
  * Fix: Streaming responses now properly display errors on the UI instead of getting stuck in processing state
</Update>

<Update label="Core" description="v1.2.22">
  * Fix: Updates token calculation for streaming responses. #520
</Update>

<Update label="Framework" description="v1.2.22">
  * upgrade: core upgrades to 1.1.38
</Update>

<Update label="governance" description="v1.2.22">
  * upgrade: core to 1.1.38
  * upgrade: framework to 1.0.24
</Update>

<Update label="jsonparser" description="v1.2.22">
  * upgrade: core to 1.1.38
  * upgrade: framework to 1.0.24
</Update>

<Update label="logging" description="v1.2.22">
  * fix: fixes error logging for streaming and non-streaming responses.
  * upgrade: core to 1.1.38
  * upgrade: framework to 1.0.24
</Update>

<Update label="maxim" description="v1.2.22">
  * upgrade: core to 1.1.38
  * upgrade: framework to 1.0.24
</Update>

<Update label="mocker" description="v1.2.22">
  * upgrade: core to 1.1.38
  * upgrade: framework to 1.0.24
</Update>

<Update label="semanticcache" description="v1.2.22">
  * upgrade: core to 1.1.38
  * upgrade: framework to 1.0.24
</Update>

<Update label="telemetry" description="v1.2.22">
  * upgrade: core to 1.1.38
  * upgrade: framework to 1.0.24
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt