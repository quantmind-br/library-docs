---
title: v1.3.57
url: https://docs.getbifrost.ai/changelogs/v1.3.57.md
source: llms
fetched_at: 2026-01-21T19:42:38.676018035-03:00
rendered_js: false
word_count: 134
summary: This document details the version 1.3.57 release notes for Bifrost, including bug fixes for configuration parsing and framework upgrades across multiple service modules.
tags:
    - changelog
    - release-notes
    - bifrost
    - version-update
    - bug-fixes
    - framework-upgrade
category: reference
---

# v1.3.57

> v1.3.57 changelog - 2026-01-01

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.57
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.57
    docker run -p 8080:8080 maximhq/bifrost:v1.3.57
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.57">
  * fix: fixes allowed\_keys parsing from config.json as a string array
  * chore: removes some extra debug logs
</Update>

<Update label="Framework" description="1.1.56">
  * fix: fixes allowed\_keys parsing from config.json as a string array
</Update>

<Update label="governance" description="1.3.57">
  * chore: upgrades framework to 1.1.56
</Update>

<Update label="jsonparser" description="1.3.57">
  * chore: upgrades framework to 1.1.56
</Update>

<Update label="logging" description="1.3.57">
  * chore: upgrades framework to 1.1.56
</Update>

<Update label="maxim" description="1.4.57">
  * chore: upgrades framework to 1.1.56
</Update>

<Update label="mocker" description="1.3.56">
  * chore: upgrades framework to 1.1.56
</Update>

<Update label="otel" description="1.0.56">
  * chore: upgrades framework to 1.1.56
</Update>

<Update label="semanticcache" description="1.3.56">
  * chore: upgrades framework to 1.1.56
</Update>

<Update label="telemetry" description="1.3.56">
  * chore: upgrades framework to 1.1.56
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt