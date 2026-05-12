---
title: v1.3.17
url: https://docs.getbifrost.ai/changelogs/v1.3.17.md
source: llms
fetched_at: 2026-01-21T19:41:46.701439006-03:00
rendered_js: false
word_count: 169
summary: This document provides the release notes and installation commands for Bifrost version 1.3.17, covering bug fixes for virtual keys and framework updates.
tags:
    - changelog
    - release-notes
    - bifrost
    - version-update
    - docker
    - npx
category: other
---

# v1.3.17

> v1.3.17 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.17
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.17
    docker run -p 8080:8080 maximhq/bifrost:v1.3.17
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.17">
  * chore: version update framework to 1.1.24
  * fix: resolve MCP client deletion when attached to a virtual key
  * chore: allowed changing name when updating a virtual key
  * fix: vk team/customer association issue when updating a vk
</Update>

<Update label="Framework" description="v1.3.17">
  * fix: resolve MCP client deletion when attached to a virtual key
  * fix: vk team/customer association issue when updating a vk
</Update>

<Update label="governance" description="v1.3.17">
  * chore: version update framework to 1.1.23
</Update>

<Update label="jsonparser" description="v1.3.17">
  * chore: version update framework to 1.1.24
</Update>

<Update label="logging" description="v1.3.17">
  * chore: version update framework to 1.1.24
</Update>

<Update label="maxim" description="v1.3.17">
  * chore: version update framework to 1.1.24
</Update>

<Update label="mocker" description="v1.3.17">
  * chore: version update framework to 1.1.24
</Update>

<Update label="otel" description="v1.3.17">
  * chore: version update framework to 1.1.24
</Update>

<Update label="semanticcache" description="v1.3.17">
  * chore: version update framework to 1.1.24
</Update>

<Update label="telemetry" description="v1.3.17">
  * chore: version update framework to 1.1.24
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt