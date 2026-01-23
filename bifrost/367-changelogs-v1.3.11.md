---
title: v1.3.11
url: https://docs.getbifrost.ai/changelogs/v1.3.11.md
source: llms
fetched_at: 2026-01-21T19:41:37.915508389-03:00
rendered_js: false
word_count: 193
summary: This document details the release notes for Bifrost version 1.3.11, highlighting new features such as the models endpoint and core framework updates.
tags:
    - release-notes
    - bifrost
    - version-update
    - api-changes
    - deployment
category: other
---

# v1.3.11

> v1.3.11 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.11
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.11
    docker run -p 8080:8080 maximhq/bifrost:v1.3.11
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.11">
  * chore: version update core to 1.2.14 and framework to 1.1.16
  * feat: added `/v1/models` endpoint to list models of configured providers
</Update>

<Update label="Core" description="v1.3.11">
  * feat: added ListModels method to Provider interface
  * feat: enabled provider tracking in Bifrost core for API exposure
</Update>

<Update label="Framework" description="v1.3.11">
  * chore: version update core to 1.2.14
</Update>

<Update label="governance" description="v1.3.11">
  * chore: version update core to 1.2.14 and framework to 1.1.16
</Update>

<Update label="jsonparser" description="v1.3.11">
  * chore: version update core to 1.2.14 and framework to 1.1.16
</Update>

<Update label="logging" description="v1.3.11">
  * chore: version update core to 1.2.14 and framework to 1.1.16
</Update>

<Update label="maxim" description="v1.3.11">
  * chore: version update core to 1.2.14 and framework to 1.1.16
</Update>

<Update label="mocker" description="v1.3.11">
  * chore: version update core to 1.2.14 and framework to 1.1.16
</Update>

<Update label="otel" description="v1.3.11">
  * chore: version update core to 1.2.14 and framework to 1.1.16
</Update>

<Update label="semanticcache" description="v1.3.11">
  * chore: version update core to 1.2.14 and framework to 1.1.16
</Update>

<Update label="telemetry" description="v1.3.11">
  * chore: version update core to 1.2.14 and framework to 1.1.16
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt