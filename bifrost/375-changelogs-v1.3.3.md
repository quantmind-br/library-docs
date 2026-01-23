---
title: v1.3.3
url: https://docs.getbifrost.ai/changelogs/v1.3.3.md
source: llms
fetched_at: 2026-01-21T19:42:05.11400697-03:00
rendered_js: false
word_count: 159
summary: This document details the changelog for version 1.3.3 of the Bifrost platform, highlighting bug fixes for JSON serialization and core dependency updates across various modules.
tags:
    - changelog
    - release-notes
    - bifrost
    - version-update
    - bug-fix
    - json-serialization
category: reference
---

# v1.3.3

> v1.3.3 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.3
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.3
    docker run -p 8080:8080 maximhq/bifrost:v1.3.3
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.3">
  * Upgrade dependency: core to 1.2.9
  * Fix: JSON serialization for error objects and tool function parameters
</Update>

<Update label="Core" description="v1.3.3">
  * Fix: Fixed JSON serialization for error objects and tool function parameters
</Update>

<Update label="Framework" description="v1.3.3">
  * Upgrade dependency: core to 1.2.9
  * Fix: JSON serialization for error objects and tool function parameters
</Update>

<Update label="governance" description="v1.3.3">
  * chore: version update core to 1.2.9
</Update>

<Update label="jsonparser" description="v1.3.3">
  * chore: version update core to 1.2.9
</Update>

<Update label="logging" description="v1.3.3">
  * chore: version update core to 1.2.9
</Update>

<Update label="maxim" description="v1.3.3">
  * chore: version update core to 1.2.9
</Update>

<Update label="mocker" description="v1.3.3">
  * chore: version update core to 1.2.9
</Update>

<Update label="otel" description="v1.3.3">
  * chore: version update core to 1.2.9
</Update>

<Update label="semanticcache" description="v1.3.3">
  * chore: version update core to 1.2.9
</Update>

<Update label="telemetry" description="v1.3.3">
  * chore: version update core to 1.2.9
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt