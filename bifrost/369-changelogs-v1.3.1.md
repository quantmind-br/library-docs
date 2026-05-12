---
title: v1.3.1
url: https://docs.getbifrost.ai/changelogs/v1.3.1.md
source: llms
fetched_at: 2026-01-21T19:41:35.078533559-03:00
rendered_js: false
word_count: 168
summary: Detailed release notes for Bifrost version 1.3.1, covering installation steps and specific updates across various core modules and dependencies.
tags:
    - bifrost
    - changelog
    - release-notes
    - bug-fixes
    - dependency-upgrades
    - docker
    - npx
category: other
---

# v1.3.1

> v1.3.1 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.1
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.1
    docker run -p 8080:8080 maximhq/bifrost:v1.3.1
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.1">
  * Bug: "x-bf-vk" missing error fixed.
</Update>

<Update label="Core" description="v1.3.1">
  * Refactor: Bifrost Response structure seggragated.
</Update>

<Update label="Framework" description="v1.3.1">
  * Upgrade dependency: core to 1.2.7
  * Fix: Added missing migration for `parent_request_id_column` in logs table.
</Update>

<Update label="governance" description="v1.3.1">
  * Chore: taking context key from core package instead of governance package
</Update>

<Update label="jsonparser" description="v1.3.1">
  * Upgrade dependency: core to 1.2.7 and framework to 1.1.7
</Update>

<Update label="logging" description="v1.3.1">
  * Upgrade dependency: core to 1.2.7 and framework to 1.1.7
</Update>

<Update label="maxim" description="v1.3.1">
  * Upgrade dependency: core to 1.2.7 and framework to 1.1.7
</Update>

<Update label="mocker" description="v1.3.1">
  * Upgrade dependency: core to 1.2.7 and framework to 1.1.7
</Update>

<Update label="otel" description="v1.3.1">
  * Upgrade dependency: core to 1.2.6 and framework to 1.1.6
</Update>

<Update label="semanticcache" description="v1.3.1">
  * Upgrade dependency: core to 1.2.7 and framework to 1.1.7
</Update>

<Update label="telemetry" description="v1.3.1">
  * Upgrade dependency: core to 1.2.7 and framework to 1.1.7
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt