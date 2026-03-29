---
title: v1.3.6
url: https://docs.getbifrost.ai/changelogs/v1.3.6.md
source: llms
fetched_at: 2026-01-21T19:42:41.645062547-03:00
rendered_js: false
word_count: 184
summary: This document details the changes and updates in Bifrost version 1.3.6, including bug fixes for tool message outputs and core component version bumps. It provides installation commands for updating via NPX and Docker.
tags:
    - changelog
    - release-notes
    - bifrost
    - docker
    - version-update
    - bug-fixes
category: reference
---

# v1.3.6

> v1.3.6 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.6
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.6
    docker run -p 8080:8080 maximhq/bifrost:v1.3.6
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.6">
  * chore: version update core to 1.2.11 and framework to 1.1.12
  * fix: responses tool message output struct overlapping fields fixed
</Update>

<Update label="Core" description="v1.3.6">
  * fix: responses tool message output struct overlapping fields fixed
</Update>

<Update label="Framework" description="v1.3.6">
  * chore: version update core to 1.2.11
</Update>

<Update label="governance" description="v1.3.6">
  * chore: version update core to 1.2.11 and framework to 1.1.12
</Update>

<Update label="jsonparser" description="v1.3.6">
  * chore: version update core to 1.2.11 and framework to 1.1.12
</Update>

<Update label="logging" description="v1.3.6">
  * chore: version update core to 1.2.11 and framework to 1.1.12
</Update>

<Update label="maxim" description="v1.3.6">
  * chore: version update core to 1.2.11 and framework to 1.1.12
</Update>

<Update label="mocker" description="v1.3.6">
  * chore: version update core to 1.2.11 and framework to 1.1.12
</Update>

<Update label="otel" description="v1.3.6">
  * chore: version update core to 1.2.11 and framework to 1.1.12
</Update>

<Update label="semanticcache" description="v1.3.6">
  * chore: version update core to 1.2.11 and framework to 1.1.12
</Update>

<Update label="telemetry" description="v1.3.6">
  * chore: version update core to 1.2.11 and framework to 1.1.12
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt