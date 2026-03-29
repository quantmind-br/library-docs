---
title: v1.3.13
url: https://docs.getbifrost.ai/changelogs/v1.3.13.md
source: llms
fetched_at: 2026-01-21T19:41:40.586264176-03:00
rendered_js: false
word_count: 221
summary: This document provides the release notes and changelog for Bifrost version 1.3.13, detailing new features like provider config hot reloading and environment variable support for Postgres.
tags:
    - bifrost
    - release-notes
    - changelog
    - versioning
    - deployment
    - hot-reloading
category: reference
---

# v1.3.13

> v1.3.13 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.13
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.13
    docker run -p 8080:8080 maximhq/bifrost:v1.3.13
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.13">
  * chore: version update framework to 1.1.18 and core to 1.2.16
  * Adds env variable support for postgres config
  * feat: standardize finish reason and single response handling across providers
  * feat: provider config hot reloading added (no need to restart Bifrost after updating provider configs now)
</Update>

<Update label="Core" description="v1.3.13">
  * feat: standardize finish reason and single response handling across providers
  * feat: provider config hot reloading added
</Update>

<Update label="Framework" description="v1.3.13">
  * Adds env variable resolution for postgres config
  * chore: Upgrades core to 1.2.16
</Update>

<Update label="governance" description="v1.3.13">
  * chore: version update core to 1.2.16 and framework to 1.1.18
</Update>

<Update label="jsonparser" description="v1.3.13">
  * chore: version update core to 1.2.16 and framework to 1.1.18
</Update>

<Update label="logging" description="v1.3.13">
  * chore: version update core to 1.2.16 and framework to 1.1.18
</Update>

<Update label="maxim" description="v1.3.13">
  * chore: version update core to 1.2.16 and framework to 1.1.18
</Update>

<Update label="mocker" description="v1.3.13">
  * chore: version update core to 1.2.16 and framework to 1.1.18
</Update>

<Update label="otel" description="v1.3.13">
  * chore: version update core to 1.2.16 and framework to 1.1.18
</Update>

<Update label="semanticcache" description="v1.3.13">
  * chore: version update core to 1.2.16 and framework to 1.1.18
</Update>

<Update label="telemetry" description="v1.3.13">
  * chore: version update core to 1.2.16 and framework to 1.1.18
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt