---
title: v1.3.18
url: https://docs.getbifrost.ai/changelogs/v1.3.18.md
source: llms
fetched_at: 2026-01-21T19:41:47.903204284-03:00
rendered_js: false
word_count: 142
summary: This document outlines the updates and bug fixes introduced in Bifrost version 1.3.18, including changes to the health endpoint, framework fixes, and module version updates.
tags:
    - bifrost
    - changelog
    - release-notes
    - v1-3-18
    - deployment
    - bug-fixes
category: other
---

# v1.3.18

> v1.3.18 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.18
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.18
    docker run -p 8080:8080 maximhq/bifrost:v1.3.18
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.18">
  * change: health endpoint is whitelisted from auth middleware
</Update>

<Update label="Framework" description="v1.3.18">
  * fix: resolve MCP client deletion when attached to a virtual key
  * fix: vk team/customer association issue when updating a vk
</Update>

<Update label="governance" description="v1.3.18">
  * chore: version update framework to 1.1.23
</Update>

<Update label="jsonparser" description="v1.3.18">
  * chore: version update framework to 1.1.24
</Update>

<Update label="logging" description="v1.3.18">
  * chore: version update framework to 1.1.24
</Update>

<Update label="maxim" description="v1.3.18">
  * chore: version update framework to 1.1.24
</Update>

<Update label="mocker" description="v1.3.18">
  * chore: version update framework to 1.1.24
</Update>

<Update label="otel" description="v1.3.18">
  * chore: version update framework to 1.1.24
</Update>

<Update label="semanticcache" description="v1.3.18">
  * chore: version update framework to 1.1.24
</Update>

<Update label="telemetry" description="v1.3.18">
  * chore: version update framework to 1.1.24
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt