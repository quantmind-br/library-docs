---
title: v1.3.56
url: https://docs.getbifrost.ai/changelogs/v1.3.56.md
source: llms
fetched_at: 2026-01-21T19:42:37.165503266-03:00
rendered_js: false
word_count: 199
summary: This document provides the changelog for Bifrost version 1.3.56, detailing bug fixes for configuration handling, new hashing support for provider keys, and package version updates.
tags:
    - changelog
    - release-notes
    - bifrost
    - version-update
    - bug-fixes
    - configuration-management
category: reference
---

# v1.3.56

> v1.3.56 changelog - 2026-01-01

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.56
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.56
    docker run -p 8080:8080 maximhq/bifrost:v1.3.56
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.56">
  * fix: handles overwriting of key values in case of collision between config.json and db
  * fix: fixes support for referring allowed keys in virtual\_keys when setting up Bifrost using config.json
</Update>

<Update label="Core" description="1.2.45">
  * feat: adds hashing support for provider keys
</Update>

<Update label="Framework" description="1.1.55">
  * feat: adds config\_hash columns for provider keys
  * chore: adds CRUD testcases for config store
  * chore: upgrade core to 1.2.45
</Update>

<Update label="governance" description="1.3.56">
  * chore: upgrade core to 1.2.45 and framework to 1.1.55
</Update>

<Update label="jsonparser" description="1.3.56">
  * chore: upgrade core to 1.2.45 and framework to 1.1.55
</Update>

<Update label="logging" description="1.3.56">
  * chore: upgrade core to 1.2.45 and framework to 1.1.55
</Update>

<Update label="maxim" description="1.4.56">
  * chore: upgrade core to 1.2.45 and framework to 1.1.55
</Update>

<Update label="mocker" description="1.3.55">
  * chore: upgrade core to 1.2.45 and framework to 1.1.55
</Update>

<Update label="otel" description="1.0.55">
  * chore: upgrade core to 1.2.45 and framework to 1.1.55
</Update>

<Update label="semanticcache" description="1.3.55">
  * chore: upgrade core to 1.2.45 and framework to 1.1.55
</Update>

<Update label="telemetry" description="1.3.55">
  * chore: upgrade core to 1.2.45 and framework to 1.1.55
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt